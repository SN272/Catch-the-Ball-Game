'''Project - Catch The Ball Game
Class - XI (2021-22)
Authors - Nandini Sharma (R.No.32)'''

import turtle as t
import os, winsound

win1=t.Screen()
win1.setup(500,400)
q=t.textinput("Catch the ball", "INSTRUCTIONS : \nThe paddle can be controlled through arrow keys (left arrow key = move left, right arrow key = move right)\nEvery time the ball touches the red border a chance is lost. After 5 chances, game is over \nEvery time the paddle touches the ball, 1 point is added to score\nDo you want to start the game? (yes/no)")
q=q.lower()
if q in 'yes':
        win2 = t.Screen()
        win2.title("Catch the Ball")
        win2.bgcolor('black')
        win2.bgpic("bg.gif")
        win2.setup(width=800,height=600)  
        win2.tracer(0)      

        #drawing ball
        ball = t.Turtle()
        ball.shape('circle')
        ball.color('yellow')
        ball.shapesize(stretch_wid=1.5,stretch_len=1.5)
        ball.penup()
        ball.speed(0)
        ball.goto(0,0)
        ball_dx = 1
        ball_dy = 1

        #drawing paddle
        paddle = t.Turtle()
        paddle.shape('square')
        paddle.color('White')
        paddle.speed(0)
        paddle.shapesize(0.7,5)
        #paddle.shapesize(stretch_wid=1,stretch_len=5)
        paddle.penup()
        paddle.goto(0,-277)
        #initializing score variables
        score,chances=0,5
        
        #pen
        mypen=t.Turtle()
        mypen.hideturtle
        mypen.color("red")
        mypen.penup()
        mypen.goto(-450,-290)
        mypen.pendown()
        mypen.pensize(10)
        mypen.forward(1000)

        
        #functions of paddle
        def paddle_left():
                x=paddle.xcor()
                x-=45
                paddle.setx(x)
        
        def paddle_right():
                x=paddle.xcor()
                x+=45
                paddle.setx(x)
                
        #movement of paddle
        if paddle.xcor()<390 and paddle.xcor()>-390:
                win2.listen()
                win2.onkeypress(paddle_right,"Right")
                win2.onkeypress(paddle_left,"Left")

        #working of the main loop
        while True:
                win2.update()
                
                #ball
                ball.setx(ball.xcor() + ball_dx)
                ball.sety(ball.ycor() + ball_dy)
                if ball.ycor()>290: #top
                        ball.sety(290)
                        ball_dy *=-1
                        
                if paddle.distance(ball)<=37: #Ball and paddle collision
                        ball.goto(0,0)
                        ball_dx*=-1
                        score+=1
                        winsound.PlaySound("soundeffect.mp3",winsound.SND_ASYNC)
                elif ball.ycor()<=-285: #bottom
                        ball.sety(-285)
                        ball_dy *= -1
                        chances-=1
                        
                if ball.xcor()>390: #right
                        ball.setx(390)
                        ball_dx *= -1
                elif ball.xcor()<-390: #left
                        ball.setx(-390)
                        ball_dx *= -1
                        

                

                #score text
                mypen.clear()
                mypen.penup()
                mypen.color("red")
                mypen.penup()
                mypen.goto(-450,-290)
                mypen.pendown()
                mypen.pensize(10)
                mypen.forward(1000)
                mypen.penup()
                mypen.color("white")
                mypen.hideturtle()
                mypen.setposition(-350,270)
                scorestr="Score : {}     Chances : {} ".format(score,chances)
                mypen.write(scorestr,align='left',font=("Times New Roman",14,"normal"))
                
                #terminating (chances checking)
                if chances==0:
                        win3=t.Screen()
                        win3.bgcolor("black")
                        t.color("green")
                        style=("Times New Roman",50,"bold")
                        t.write("Game Over!",font=style,align="center")
                        t.hideturtle()
                        break
                        
else:
        win4=t.Screen()
        win4.bgcolor("black")
        t.hideturtle()
        t.color("red")
        style=("Times New Roman",50,"bold")
        t.write("Thank you",font=style,align="center")
