import turtle
#setup window
window = turtle.Screen()
window.title("PING PONG GAME BY HAZEM YAKOUT")
window.setup(width = 800, height = 600 )
window.tracer(0)#set delay for update drawings
window.bgcolor(.1, .1, .1) 
#setup game objects
  #ball
ball = turtle.Turtle()
ball.speed(0) #fastest speed
ball.shape("square")
ball.color("white")
#scale factor * default size (1px * 20px)
ball.shapesize(stretch_len=1, stretch_wid=1)
ball.goto(x=0, y=0)
ball.penup() #طلع القلم
ball_dx, ball_dy=1, 1
ball_speed = .35
  # center line
center_line = turtle.Turtle()
center_line.speed(0)
center_line.shape("square")
center_line.color("white")
#width => 500px (25 * 20)
center_line.shapesize(stretch_len=1, stretch_wid=25)
center_line.goto(x=0, y=0)
center_line.penup()
   #player 1
player1 = turtle.Turtle()
player1.speed(0)
player1.shape("square")
player1.color("blue")
player1.penup()
player1.shapesize(stretch_len=1, stretch_wid=5)
player1.goto(x= -350, y=0)
    #player2
player2 = turtle.Turtle()
player2.speed(0)
player2.shape("square")
player2.color("red")
player2.penup()
player2.shapesize(stretch_len=1, stretch_wid=5)
player2.goto(x= 350, y=0)
    #scorre text
score = turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.goto(x=0, y=260)
score.write("player1: 0 player2: 0", align="center", font=("courier", 14, 'normal'))
score.hideturtle()# we hide the the object because we need text only
p1_score = 0
p2_score = 0
#players movement
player_speed = 20
def p1_move_up():
    player1.sety(player1.ycor() + player_speed) #مكانه زائد 20

def p1_move_down():
    player1.sety(player1.ycor() - player_speed)#مكانه ناقص 20

def p2_move_up():
    player2.sety(player2.ycor() + player_speed)

def p2_move_down():
    player2.sety(player2.ycor() - player_speed)
   
     

# get user inputs
window.listen() # tell window to expect user inputs
window.onkeypress(p1_move_up, "w")
window.onkeypress(p1_move_down, "s")
window.onkeypress(p2_move_up, "Up")
window.onkeypress(p2_move_down, "Down")
#game loop
while True:
    window.update()
      # ball movement
    ball.setx(ball.xcor() + (ball_dx * ball_speed))
    ball.sety(ball.ycor() + (ball_dy * ball_speed))

    # ball and borders collisions
    if(ball.ycor() > 290):   #290 => 300(top bordrer) - 10(half size ball)
        ball.sety(290)
        ball_dy *= -1  #invert y direction
    if(ball.ycor() < -290):   #290 => 300(top bordrer) - 10(half size ball)
         ball.sety(-290)
         ball_dy *= -1  #invert y direction
    #ball and players collisions 
    #collisions with player1
    if ball.xcor() < -340 and ball.xcor() > -350 and ball.ycor() > (player1.ycor()-60)and ball.ycor() < (player1.ycor()+60):
        ball.setx(-340)
        ball_dx *= -1
    #collisions with player2
    if ball.xcor() > 340 and ball.xcor() < 350 and ball.ycor() > (player2.ycor()-60)and ball.ycor() < (player2.ycor()+60):
        ball.setx(340)
        ball_dx *= -1
    #score handeling
    if (ball.xcor() > 390):
        ball.goto(x=0, y= 0)
        ball_dx *= -1 # invert x direction
        score.clear()
        p1_score += 1
        score.write(f"player1: {p1_score} player2: {p2_score}", align="center", font=("courier", 14, 'normal'))
    
    if ball.xcor() < -390:
        ball.goto(x=0, y= 0)
        ball_dx *= -1 # invert x direction
        score.clear()
        p2_score += 1
        score.write(f"player1: {p1_score} player2: {p2_score}", align="center", font=("courier", 14, 'normal'))
    if p1_score == 10:
        print("congrats player1")
        break
    elif p2_score == 10:
        print("congrats player2")
