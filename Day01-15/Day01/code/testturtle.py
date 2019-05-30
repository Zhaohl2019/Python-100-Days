# 导入turtle包的所有内容:
from turtle import *
import turtle
import time
import peppa_pig
# 设置笔刷宽度:
width(4)
'''
# 前进:
forward(200)
# 右转90度:
right(90)
time.sleep(0.5)

# 笔刷颜色:
pencolor('red')
forward(100)
right(90)
time.sleep(0.5)

pencolor('green')
forward(200)
right(90)
time.sleep(0.5)

pencolor('blue')
forward(100)
right(90)
time.sleep(0.5)
'''

#screen=Turtle().getscreen()
#screen.bgcolor('blue')
#screen.bgpic(r'E:\Python-100-Days\Day01-15\Day01\code\烟花.gif')

Turtle().write('生日',move=False,font=('微软雅黑',14,'normal'))
time.sleep(0.5)
Turtle().write('生日快乐',font=('微软雅黑',14,'normal'))
time.sleep(0.5)
Turtle().write('生日快乐,送你',font=('微软雅黑',14,'normal'))
time.sleep(0.5)
Turtle().write('生日快乐,送你一只猪',font=('微软雅黑',14,'normal'))
time.sleep(0.5)
Turtle().write('生日快乐,送你一只猪以示尊敬！',font=('微软雅黑',14,'normal'))
time.sleep(0.5)

peppa_pig.main()
time.sleep(1)
for i in range(500):
    turtle.undo()
# 调用done()使得窗口等待被关闭，否则将立刻关闭窗口:
done()