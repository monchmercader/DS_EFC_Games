import turtle
import os

wn = turtle.Screen()
wn.title("Pong by Monch")
wn.bgcolor("white")
wn.setup(width=800, height=600)
wn.tracer(0)

# Scores
score_a = 0
score_b = 0


# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("pink")
paddle_a.shapesize(stretch_wid=7, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)


# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("blue")
paddle_b.shapesize(stretch_wid=7, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("red")
ball.penup()
ball.goto(0, 0)
ball.dx = 2
ball.dy = -2

# Pen writing the Scores
pen = turtle.Turtle()
pen.speed(0)
pen.color("green")
pen.penup()
pen.hideturtle()
pen.goto(0, 240)
pen.write("Pink: 0 Blue: 0", align="center", font=("Helvetica", 30, "bold"))

# Center Net
center_net = turtle.Turtle()
center_net.speed(0)
center_net.shape("square")
center_net.color("black")
center_net.shapesize(stretch_wid=25, stretch_len=0.1)
center_net.penup()
center_net.goto( 0, 0)

# Function
def paddle_a_down():
    a_y = paddle_a.ycor()
    a_y -= 30
    # Paddle A lower border check
    if a_y < -240:
        a_y = -240
    paddle_a.sety(a_y)
    
def paddle_a_up():
    a_y = paddle_a.ycor()
    a_y += 30
    # Paddle A upper border check
    if a_y > 240:
        a_y = 240
    paddle_a.sety(a_y)
    
def paddle_b_down():
    b_y = paddle_b.ycor()
    b_y -= 30
    # Paddle B lower border check
    if b_y < -240:
        b_y = -240
    paddle_b.sety(b_y)
    
def paddle_b_up():
    b_y = paddle_b.ycor()
    b_y += 30
    # Paddle B upper border check
    if b_y > 240:
        b_y = 240
    paddle_b.sety(b_y)    

    
# Keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")


# Main Game Loop#
while True:
    wn.update()
    
    # Moving the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    
    # Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        os.system("aplay bounce.wav&")
        
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        os.system("aplay bounce.wav&")
    
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Pink {} Blue: {}".format(score_a, score_b), align="center", font=("Helvetica", 30, "bold"))
        
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Pink: {} Blue: {}".format(score_a, score_b), align="center", font=("Helvetica", 30, "bold"))
        
    # Paddle and ball collision
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 70 and ball.ycor() > paddle_b.ycor() -70):
        ball.setx(340)
        ball.dx *= -1
        os.system("aplay bounce.wav&")
    
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 70 and ball.ycor() > paddle_a.ycor() -70):
        ball.setx(-340)
        ball.dx *= -1
        os.system("aplay bounce.wav&")
