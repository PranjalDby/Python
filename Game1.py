import turtle;

def start():
    wm = turtle.Screen();
    wm.title("PingPong Game")
    wm.bgcolor("black")
    wm.setup(width=800,height=600)
    wm.tracer(0.9)
    paddleA = turtle.Turtle()
    paddleA.speed(0);
    paddleA.shape("square")
    paddleA.color("white")
    paddleA.penup()
    paddleA.shapesize(5.0,stretch_len=1)
    paddleA.goto(-350,0)
    paddleB = turtle.Turtle()
    paddleB.speed(0);
    paddleB.shape("square")
    paddleB.color("white")
    paddleB.penup()
    paddleB.shapesize(5.0,stretch_len=1)
    paddleB.goto(350,0)
    def movePaddleAUp():
        y = paddleA.ycor()
        y+=20;
        paddleA.sety(y=y)

    def movePaddleADown():
        y = paddleA.ycor()
        y-=20;
        paddleA.sety(y=y)
    def movePaddleBUp():
        y = paddleB.ycor()
        y+=20;
        paddleB.sety(y=y)

    def movePaddleBDown():
        y = paddleB.ycor()
        y-=20;
        paddleB.sety(y=y)

    ball = turtle.Turtle()
    ball.shape("square")
    ball.color("white")
    ball.penup()
    ball.goto(0,0)
    ball.dx = 1;
    ball.dy = -1;
    wm.listen()
    wm.onkey(movePaddleAUp,"w")
    wm.onkey(movePaddleADown,"s")
    wm.onkey(movePaddleBUp,"Up")
    wm.onkey(movePaddleBDown,"Down")
    while True:
        wm.update()
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)
        if(ball.ycor()> 290):
            ball.sety(290)
            ball.dy *= -1
        
        if(ball.ycor()< -290):
            ball.sety(-290)
            ball.dy *= -1

        if(ball.xcor()>390):
            ball.goto(0,0)
            ball.dx *=-1

        if(ball.xcor()<-390):
            ball.goto(0,0)
            ball.dx *=-1
        if(ball.xcor()>340 and ball.xcor()<350 and ball.ycor() < paddleB.ycor() + 40 and ball.ycor() > paddleB.ycor() - 40):
            ball.setx(340)
            ball.dx *=-1


    