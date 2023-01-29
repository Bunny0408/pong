import turtle
import winsound
from turtle import *


# Screen
wn = turtle.Screen() 
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Middle Line
left(90)
forward(300)
left(180)
forward(300)

#Score
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)


# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)


# Ball 
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = 0.08
ball.dy = 0.08

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0 Player B : 0", align="center", font=("Courier", 20, "normal"))

# instead of writing those three lines in each fun we can cut it down to one wich is paddle_a.sety(paddle_a.ycor() + 20)

# Function
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)
    # paddle_a.sety(paddle_a.ycor() + 20)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)
    


# Keyboard listen 
wn.listen()
wn.onkeypress(paddle_a_up, "w" )
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up" )
wn.onkeypress(paddle_b_down, "Down") 



# Main Game loop
while True:
       
    wn.update()

    # Movement of the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy) 

    # Border checking for ball
    # For top border y axis
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    # For bottom border -y axis
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    # For right border x axis
    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {} Player B : {}".format(score_a, score_b), align="center", font=("Courier", 20, "normal"))

    # For left border -x axis
    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {} Player B : {}".format(score_a, score_b), align="center", font=("Courier", 20, "normal"))


    # Border checking for paddle
    if paddle_b.ycor() > 250:
        paddle_b.sety(250)

    if paddle_b.ycor() < -250:
        paddle_b.sety(-250)
        
    if paddle_a.ycor() > 250:
        paddle_a.sety(250)

    if paddle_a.ycor() < -250:
        paddle_a.sety(-250)




    # Paddle and ball Collision
    # here we check if cor ball is beyond 340 and under 350(for right side) and also check if ball is hitting the paddle or not

    # Right Side
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() -50):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound("pong-sound.wav", winsound.SND_ASYNC)

    # Left Side
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() -50):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound("pong-sound.wav", winsound.SND_ASYNC)





