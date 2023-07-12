'''
dongwu=input()
sheng=input()
print("王老先生有块地 咿呀咿呀哟")
print("他在田边养小鸡"+ dongwu+"咿呀咿呀哟")
print(sheng*3+" "+sheng*3+" "+sheng*6+" "+sehng*4)
'''

'''
import math
sqrt=math.sqrt
a=float(input())
b=float(input())
c=float(input())
p=(a+b+c)/2
s=sqrt(p*(p-a)*(p-b)*(p-c))
print("%f"%s)
'''


'''
import turtle as t
import math

# 设置速度
t.speed(100)  # 速度
t.delay(10)  # 延迟
# turtle.tracer(False)
# 双耳
# 左耳
t.penup()
t.goto(-150, 200)
t.setheading(160)
t.begin_fill()
t.pendown()
t.circle(-30, 230)
t.setheading(180)
t.circle(37, 90)
t.end_fill()
# 右耳
t.penup()
t.goto(60, 200)
t.setheading(20)
t.begin_fill()
t.pendown()
t.circle(30, 230)
t.setheading(0)
t.circle(-37, 90)
t.end_fill()
# 头
t.pensize(5)
t.penup()
t.goto(-113, 237)
t.setheading(30)
t.pendown()
t.circle(-134, 60)

t.penup()
t.goto(-150, 200)
t.setheading(-120)
t.pendown()
t.circle(200, 80)

t.penup()
t.goto(60, 200)
t.setheading(-60)
t.pendown()
t.circle(-200, 80)

t.penup()
t.setheading(210)
t.pendown()
t.circle(-120, 60)
# 双眼
# 左眼
# 眼圈
t.penup()
t.goto(-140, 100)
t.setheading(-45)
t.begin_fill()
t.pendown()
a = 0.2
for i in range(120):
    if 0 <= i < 30 or 60 <= i < 90:
        a = a + 0.1
        t.lt(3)  # 向左转3度
        t.fd(a)  # 向前走a的步长
    else:
        a = a - 0.1
        t.lt(3)
        t.fd(a)
t.end_fill()
# 眼白
t.fillcolor("white")
t.penup()
t.goto(-103, 125)
t.setheading(0)
t.begin_fill()
t.pendown()
t.circle(13, 360)
t.end_fill()
# 眼珠
t.fillcolor("sienna")
t.pencolor("sienna")
t.penup()
t.goto(-102, 133)
t.setheading(0)
t.begin_fill()
t.pendown()
t.circle(5, 360)
t.end_fill()
# 右眼
# 眼圈
t.penup()
t.goto(50, 100)
t.setheading(45)
t.fillcolor("black")
t.pencolor("black")
t.begin_fill()
t.pendown()
a = 0.2
for i in range(120):
    if 0 <= i < 30 or 60 <= i < 90:
        a = a + 0.1
        t.lt(3)  # 向左转3度
        t.fd(a)  # 向前走a的步长
    else:
        a = a - 0.1
        t.lt(3)
        t.fd(a)
t.end_fill()
# 眼白
t.fillcolor("white")
t.penup()
t.goto(13, 125)
t.setheading(0)
t.begin_fill()
t.pendown()
t.circle(13, 360)
t.end_fill()
# 眼珠
t.fillcolor("sienna")
t.pencolor("sienna")
t.penup()
t.goto(12, 133)
t.setheading(0)
t.begin_fill()
t.pendown()
t.circle(5, 360)
t.end_fill()
# 鼻子
t.pencolor("black")
t.fillcolor("black")
t.penup()
t.goto(-55, 133)
t.begin_fill()
t.pendown()
t.fd(20)
t.seth(-120)
t.fd(20)
t.seth(120)
t.fd(20)
t.end_fill()
# 嘴
t.penup()
t.goto(-70, 110)
t.setheading(-30)
t.fillcolor("red")
t.begin_fill()
t.pendown()
t.circle(50, 60)
t.setheading(-120)
t.circle(-100, 15)
t.circle(-15, 90)
t.circle(-100, 15)
t.end_fill()
# 四肢
# 左臂
t.penup()
t.goto(-175, 100)
t.fillcolor("black")
t.begin_fill()
t.setheading(-120)
t.pendown()
t.fd(100)
t.setheading(-110)
t.circle(20, 180)
t.fd(30)
t.circle(-5, 160)
t.end_fill()
# 右臂
t.penup()
t.goto(85, 100)
t.setheading(60)
t.begin_fill()
t.pendown()
t.fd(100)
t.setheading(70)
t.circle(20, 180)
t.fd(30)
t.circle(-5, 160)
t.end_fill()
# 小红心
t.penup()
t.pencolor("red")
t.fillcolor('red')
t.goto(105, 200)
t.begin_fill()
t.pendown()
t.circle(-5, 180)
t.setheading(90)
t.circle(-5, 180)
t.setheading(-120)
t.fd(17)
t.penup()
t.goto(105, 200)
t.pendown()
t.setheading(-60)
t.fd(17)
t.end_fill()
t.pencolor("black")
t.fillcolor("black")
# 左腿
t.penup()
t.goto(-120, -45)
t.begin_fill()
t.pendown()
t.setheading(-90)
t.circle(-140, 20)
t.circle(5, 109)
t.fd(30)
t.circle(10, 120)
t.setheading(90)
t.circle(-140, 10)
t.end_fill()
# 右腿
t.penup()
t.goto(30, -45)
t.begin_fill()
t.pendown()
t.setheading(-90)
t.circle(140, 20)
t.circle(-5, 109)
t.fd(30)
t.circle(-10, 120)
t.setheading(90)
t.circle(140, 10)
t.end_fill()
# 冰糖外壳
t.pensize(1)
t.penup()
t.goto(-160, 195)
t.setheading(160)
t.pendown()
t.circle(-40, 230)
t.setheading(30)
t.circle(-134, 58)
t.setheading(60)
t.circle(-40, 215)
t.setheading(-60)
t.fd(15)
t.circle(2, 200)
t.setheading(65)
t.fd(30)
t.circle(-25, 180)
t.fd(100)
t.circle(2, 25)
t.circle(-200, 47)
t.circle(2, 60)
t.circle(140, 23)
t.circle(-2, 90)
t.setheading(180)
t.fd(70)
t.circle(-2, 90)
t.fd(30)
t.setheading(-160)
t.circle(-100, 35)
t.setheading(-90)
t.fd(30)
t.circle(-2, 90)
t.fd(70)
t.circle(-2, 90)
t.setheading(60)
t.circle(140, 30)
t.circle(2, 45)
t.circle(-200, 19)
t.circle(2, 130)
t.fd(30)
t.circle(-25, 180)
t.fd(100)
t.setheading(90)
t.circle(-200, 30)
# 冰糖面罩
t.pensize(3)
t.penup()
t.goto(65, 120)
t.setheading(90)
t.pendown()
t.pencolor("red")
a = 1
for i in range(120):
    if 0 <= i < 30 or 60 <= i < 90:  # 控制a的变化
        a = a + 0.25
        t.lt(3)  # 向左转3度
        t.fd(a)  # 向前走a的步长
    else:
        a = a - 0.25
        t.lt(3)
        t.fd(a)
t.pencolor("orange")
t.penup()
t.goto(66, 120)
t.pendown()
a = 1
for i in range(120):
    if 0 <= i < 30 or 60 <= i < 90:
        a = a + 0.255
        t.lt(3)
        t.fd(a)
    else:
        a = a - 0.255
        t.lt(3)
        t.fd(a)
t.pencolor("green")
t.penup()
t.goto(67, 120)
t.pendown()
a = 1
for i in range(120):
    if 0 <= i < 30 or 60 <= i < 90:
        a = a + 0.2555
        t.lt(3)
        t.fd(a)
    else:
        a = a - 0.2555
        t.lt(3)
        t.fd(a)
t.pencolor("deep sky blue")
t.penup()
t.goto(68, 120)
t.pendown()
a = 1
for i in range(120):
    if 0 <= i < 30 or 60 <= i < 90:
        a = a + 0.25955
        t.lt(3)
        t.fd(a)
    else:
        a = a - 0.25955
        t.lt(3)
        t.fd(a)
t.pencolor("pink")
t.penup()
t.goto(71, 120)
t.pendown()
a = 1
for i in range(120):
    if 0 <= i < 30 or 60 <= i < 90:
        a = a + 0.26
        t.lt(3)
        t.fd(a)
    else:
        a = a - 0.26
        t.lt(3)
        t.fd(a)
t.pencolor("purple")
t.penup()
t.goto(72, 120)
t.pendown()
a = 1
for i in range(120):
    if 0 <= i < 30 or 60 <= i < 90:
        a = a + 0.269
        t.lt(3)
        t.fd(a)
    else:
        a = a - 0.269
        t.lt(3)
        t.fd(a)

# 五环
t.penup()
t.goto(-55, -10)
t.pendown()
t.pencolor("blue")
t.circle(10)
t.penup()
t.goto(-40, -10)
t.pendown()
t.pencolor("black")
t.circle(10)
t.penup()
t.goto(-25, -10)
t.pendown()
t.pencolor("red")
t.circle(10)
t.penup()
t.goto(-50, -20)
t.pendown()
t.pencolor("yellow")
t.circle(10)
t.penup()
t.goto(-30, -20)
t.pendown()
t.pencolor("green")
t.circle(10)

t.done()


'''

'''
months="JanFebMarAprMayJunJulAugSepOctNovDec"

n=input("请输入您要查询的月份数（1-12）:")

pos=(int(n)-1)*3

print("该月份的简写为"+months[pos :pos+3]+" . ")

'''


'''
str1='i like you,but just i like you.'
a = str1.split(' ')
print(a)
print(type(a))
a=a[::-1]
str2=" ".join(a)
print(str2)
print(type(str2))
if '.' in str2:
    str2 = str2.replace('you.','.you')
if ',' in str2:
    str2 = str2.replace('you,but','but,you')
print(str2)


'''
'''
a=input()

b=input()

if b.find(a)==1:

    print(b.find(a))

else:
    print("not found")
'''






'''
str = input('请输入字符串:')

for i in range(len(str) - 1, -1, -1):

    print(str[i],end='')

'''
'''
for i in range(100,999):

    a = i//100

    b = (i-a*100)//10

    c = (i-a*100-b*10)

    if i == pow(a,3)+pow(b,3)+pow(c,3):

        print(i)
'''

'''
print('欢迎来到生鲜快递查询系统')
pay=(input('请输入商品价格'))
weight=int(input('请输入订单生鲜商品重量'))


p=0

if pay<99:
    if weight<=10:
       p=12+(weight-10)
    elif weight>10:
       p=12+1*(weight-10)
    else:
        print('输入错误重新输入')

           
elif pay>=99 and pay<199:
    if weight<=10:
        p=12
    elif weight>10:
        p=1*(weight-10)
    else:
        print
'''



'''
year = int(input("请输入一个年份："))

if(year%4) == 0:
    if(year%100) != 0:
        print("{0}年是闰年！".format(year))
    else:
        if(year%400)== 0:
            print("{0}年是闰年！".format(year))
        else:
            print("{0}年不是闰年！".format(year))
else:
    print("{0}年不是闰年！".format(year))

'''





'''
#guess 0.1 open

import random

a = random.randint(1,100)

b = input("请输入一个数字")

if int(b)>a:

    print("比你小")

    print(a)
    
elif int(b)==a:

    print("你猜中了")

    print(a)
    
elif int(b)<a:

    print("比你大")

    print(a)

'''

'''

#guess 0.2

import random

secret_number=random.randint(1,100)

print("")
# 限制次数为6次

for counter in range(6):

        print("我心里正在默念着今天的幸运数字，它在1到100之间，你知道是那个吗？")

        guess=int(input())

        if guess<1 or guess>100:

            print("我的幸运数字在1到100之间，你再猜猜看？")

            continue

        if guess<secret_number:

            print("我想的比你所猜的要大一点......")

        elif guess>secret_number:

            print("我所想的比你所猜的要小一点......")

        else:

            break

if guess==secret_number:

    print("恭喜！ 聪明的你"+str(counter+1)+"次就猜中了我的幸运数字！")


else:
    print("其实你不懂我的心（^_^)我今天的幸运数字是"+str(secret_number))
'''



'''''
import numpy as np
 
persontype = np.dtype({
'names':['name','chinese','english','math'],
'formats':['S32','i','i','i']})
 
peoples = np.array([("ZhangFei",66,65,30),("GuanYu",95,85,98), ("ZhaoYun",93,92,96),("HuangZhong",90,88,77),("DianWei",80,90,90)],dtype=persontype)
 
#语文、英语、数学
chineses = peoples[:]['chinese']
englishs = peoples[:]['english']
maths = peoples[:]['math']
 
#平均成绩
print(np.mean(chineses))
print(np.mean(englishs))
print(np.mean(maths))
 
#最小成绩
print(np.amin(chineses))
print(np.amin(englishs))
print(np.amin(maths))
 
#最大成绩
print(np.amax(chineses))
print(np.amax(englishs))
print(np.amax(maths))


print(np.sort(chineses+englishs+maths))
 
#按姓名排序
print(np.sort(peoples,order='name'))


from inspect import getsourcefile
from os import fdatasync
from tkinter import image_names
from traceback import format_exception

'''


'''
file_name = imnput("请输入要操作的文件:") 
try: 
    my _file= open(file_name,"a+")
except: 
    print("程序运行发生了异常！") 
else: 
    my_file.seek(0)
    data= my _file.read(5)
    print(data,rstrip()) 
    data = my_file.readline()
    print(data.rstrip()) 
    for data in my_file：
        print(data.rstrip()) 
    my_file.write("静夜诗\n")  
    lines=["床前明月光\n","疑是地上霜ln","举头望明月\n","低头思故乡\n"] 
    my_file.writelines(lines) 
    print("-----------------")
    my_file.seek(60)
    data= my_file.read()
    print(data) 
finally： 
    my _file.close()


'''


'''
#升序文档归并

txt1 = open(input("第一个数据文件："),"rt")
txt2 = open(input("第二个数据文件："),"rt")
out = open(input("输出文件名："),"w")
data1 = txt1.readline()
data2 = txt2.readline()
while data1!=""and data2!="":
    if int(datal)<int(data2):
            out.write(data1)
            datal = txt1.readline()
    else:
            out.write(data2)
            data2 = txt2.readlines()
while data1!="":
    out.write(data1)
    data1 = txt1.readline()
while data2!=""
    out.write(data2)
    data2 = txt.readline()

txt1.close()
txt2.close()
print("文件输出完毕")


'''

'''
import turtle
def drawLine(draw):
        turtle.pendown() if draw else turtle.penup()
        turtle.fd(40)
        turtle.left(90)
def drawDigit(d):
        drawLine(True) if d in [2,3,4,5,6,8,9] else drawLine(False)
        drawLine(True) if d in [0.1,2,3,4,7,8,9] else drawLine(False)
        drawLine(True) if d in [0,2,3,5,6,7,8,9] else drawDigit(False)
        drawLine(True) if d in [0,4,5,6,8,9] else drawLine(False)
        turtle.right(90)
        drawLine(True) if d in [0,2,6,8] else drawLine(False)
        drawLine(True) if d in [0,2,3,5,6,8,9] else drawLine(False)
        drawLine(True) if d in [0,1,3,4,5,6,7,8,9] else drawLine(False)
        turtle.right(180)
        turtle.penup()
        turtle.fd(20)
def main()
        turtle.penup()
        turtle.fd(-300)
        turtle.pensize(8)
        drawDigit(3)

main()


'''




def idchangdu(n):
    if len(str(n)) != 18:
        print("只支持18位身份证号查询")
        return False
    else:
        return True
        

def idjiaoyian(n):
        var=[7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
        var_id=['1','0','x','9','8','7','6','5','4','3','2']
        n = str(n)
        sum = 0
        for i in range(0,17):
            sum += int(n[i])*var[i]
        sum %= 11
        if (var_id[sum])==str(n[17]):
            print("yes")  
            return sum
        else:
            print("no")
            return 0
n = input("请输入18位身份证号:")

if idchangdu(n):

  idjiaoyian(n)

else:
    
    print("请重新输入")