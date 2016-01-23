#coding:utf-8
import turtle
import time

boxsize = 200
caught = False
score = 0
#盒子大小，游戏终止条件，成绩
def up():
    mouse.forward(10)
    checkbound()

def left():
    mouse.left(45)

def right():
    mouse.right(45)

def back():
    mouse.backward(10)
    checkbound()

def quitTurtles():
    window.bye()
#以上是触发    方向，以及游戏结束的函数，其中中庸前进后退有移动。
def checkbound():
    global boxsize
    if mouse.xcor() > boxsize:
        mouse.goto(boxsize,mouse.ycor())
    if mouse.xcor()  < -boxsize:
        mouse.goto(-boxsize,mouse.ycor())
    if mouse.ycor()  > boxsize:
        mouse.goto(mouse.xcor(),boxsize)
    if mouse.ycor()  < -boxsize:
        mouse.goto(mouse.xcor(),-boxsize)
#以上是防止老鼠跑到外面去的。所以一旦接触边缘就修改
window = turtle.Screen()
#设定窗口
mouse = turtle.Turtle()
cat = turtle.Turtle()
mouse.penup()
mouse.penup()
mouse.goto(100,100)
#将老鼠放在100.100那里
window.onkeypress(up,"Up")
window.onkeypress(left,"Left")
window.onkeypress(right,"Right")
window.onkeypress(back,"Down")
window.onkeypress(quitTurtles,"Escape")
#设定按键触发的函数
difficulty = window.numinput("Difficulty",
"enter a difficulty from easy(1) ,for hard(5)",minval = 1,maxval = 5)
#初始设定难度值。
window.listen()
#开始监听
while not caught:
    cat.setheading(cat.towards(mouse))
    cat.forward(8+difficulty)
    #前进速度
    score = score + 1
    if cat.distance(mouse) < 5:
        caught = Ture
    #如果两者距离小与五个像素，则停止循环
    time.sleep(0.2 - (0.01*difficulty))
    #这个代表每次追逐的时间间隔，，越短则猫越快。。
window.textinput("game over", "well done, you scored:"+str(score*difficulty))
window.bye()
#最后输出成绩，不过似乎有点闪退。。
		

 
