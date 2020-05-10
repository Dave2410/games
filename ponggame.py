# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 20:19:12 2020

@author: DSE063
"""

#Simple pong game

import turtle


turtle.TurtleScreen._RUNNING = True
wn = turtle.Screen()
wn.title("Pong Back")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)


#PaddleA
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("red")
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)

#PaddleB
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("blue")
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)

#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball_dx = 0.5
ball_dy = 0.5

#Scores
scoreA=0
scoreB=0
pen = turtle.Turtle()
pen.speed(0)
pen.color("green")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.clear()
pen.write("Player A: {} Player B: {}".format(scoreA,scoreB) ,align="center",font=("Courier",24,"normal"))

#Functions
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

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

#Keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up,"w")
wn.onkeypress(paddle_a_down,"s")
wn.onkeypress(paddle_b_up,"Up")
wn.onkeypress(paddle_b_down,"Down")


#Main game loop
while True:
    wn.update()
    #Ball movement
    ball.setx(ball.xcor() + ball_dx)
    ball.sety(ball.ycor() + ball_dy)
    
    #Border check for ball
    if ball.xcor()>390:
        ball.goto(0,0)
        ball_dx=-0.5
        scoreA +=1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(scoreA,scoreB) ,align="center",font=("Courier",24,"normal"))

    if ball.ycor()>290:
        ball_dy=-0.5
        
    if ball.xcor()<-390:
        ball.goto(0,0)
        ball_dx=0.5
        scoreB +=1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(scoreA,scoreB) ,align="center",font=("Courier",24,"normal"))

    if ball.ycor()<-290:
        ball_dy=0.5
    
    #Paddle Pong A
    if paddle_a.ycor()<-290:
        paddle_a.sety(-290)
    if paddle_a.ycor()>290:
        paddle_a.sety(290)
    if ball.xcor() <= paddle_a.xcor()+30 and ball.ycor() <= paddle_a.ycor()+50 and ball.ycor() >= paddle_a.ycor()-50:
        ball_dx= 0.5
            
    #Paddle Pong B
    if paddle_b.ycor()<-240:
        paddle_b.sety(-240)
    if paddle_b.ycor()>240:
        paddle_b.sety(240)
    if ball.xcor() >= paddle_b.xcor()-30 and ball.ycor() <= paddle_b.ycor()+50 and ball.ycor() >= paddle_b.ycor()-50:
        ball_dx= -0.5
    
