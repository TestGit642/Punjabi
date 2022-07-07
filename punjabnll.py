#print function
def ਛਾਪੋ(data):
    print(data)  #ਛਾਪੋ
#input function
def ਨਿਬੇਸ(data):
    a = input(data)
    return a


#math module start
def ਜੋੜ(*args):
    sum = 0
    for i in args:
        sum += i
    return sum


def ਘਟਾਓ (x, y):
    result = x - y
    return result

def ਅਯੋਗ(x,y):
    result = x - y
    return result

def ਗੁਣਾ(*args):
    mul = 1
    for i in args:
        mul *= i
    return mul

def ਭਾਗ(x,y):
    result = x / y
    return result

def ਅਗਵਾ(x,y):
    result = x / y
    return result


#factorial function
def ਕਾਰਕੰਬੰਧੀ(num):
    z = 1
    while (1):
        z = z * num
        num = num - 1
        if (num == 0):
            break

    print(z)
ਕਾਰਕੰਬੰਧੀ(4)
#PI function
import math #importing the math functions
ਪਾਈ= math.pi #getting the value of pi
ਛਾਪੋ(ਪਾਈ) #printing the result

#square root
def ਵਰਗਮੂਲ(num):
  	return num**0.5

#power
"""def ਸਟ(n):
    for i in range(2, int(n**.5) + 1):
        number = n
        times = 0
        while number % i == 0:
            number /= i
            times += 1
            if number == 1:
                return [i, times]
    return None
"""
#HCF FUNCTION
def ਗਸਾਗੁ(x, y):
        if x > y:
            smaller = y
        else:
            smaller = x
        for i in range(1, smaller + 1):
            if ((x % i == 0) and (y % i == 0)):
                hcf = i
        return hcf

#LCM FUNCTION
def   ਲਾਸਗਨਾ(a, b):
    i = 1
    if a > b:
        c = a
        d = b
    else:
        c = b
        d = a
    while True:
        if ((c * i) / d).is_integer():
            return c * i
        i += 1;

#string module
ਪੂੰਜੀਕਰਣ=str.capitalize
ਵੱਡਾਕਿਰਦਾਰ=str.casefold
ਸਾਰੇਸ਼ਬਦਅਤੇਨੰਬਰ=str.isalnum
ਸਭਤੋਂਵੱਡਾ=str.swapcase
ਏਖਾਲਿਸ਼ਬਦਤ=str.isalpha
ਏਖਾਲਿਸਮਸ਼ਹੂਰਹੈ=str.isdigit
ਪਛਾਣਕਰਤਾ=str.isidentifier
ਛੋਟਾ=str.islower
ਈਲੋਕਲਕੂਲਸ=str.upper
ਖੱਬੇਹੱਥਵਾਲਾ=str.lstrip

ਕਿੰਨੇਸ਼ਬਦ=len

def ਉਲਟਾਅੱਖਰ(a):
    return a[::-1]
# function which return reverse of a string

def ਉਲਟਸੱਚਹੈ(str):
    # Run loop from 0 to len/2
    for i in range(0, int(len(str) / 2)):
        if str[i] != str[len(str) - i - 1]:
            return False
    return True

def ਪਹਿਲਾਸ਼ਬਦ(str):
    for i in range(0, len(str)):

        if (str[i].istitle()):
            return str[i]

    return 0

def ਬਹੁਤਸਾਰੇਸ਼ਬਦ(a):
    max_frequency = {}
    for i in a:
        if i in max_frequency:
            max_frequency[i] += 1
        else:
            max_frequency[i] = 1
    my_result = max(max_frequency, key=max_frequency.get)
    return my_result

# string module Complete

#sorting start(bubble sort)
def ਲੜੀਬੱਧ(list):
    # Swap the elements to arrange in order
    for iter_num in range(len(list) - 1, 0, -1):
        for idx in range(iter_num):
            if list[idx] > list[idx + 1]:
                temp = list[idx]
                list[idx] = list[idx + 1]
                list[idx + 1] = temp
    return list

#merge sort
def ਕ੍ਰਮਬੱਧਅਭੇਦ(unsorted_list):
   if len(unsorted_list) <= 1:
      return unsorted_list
# Find the middle point and devide it
   middle = len(unsorted_list) // 2
   left_list = unsorted_list[:middle]
   right_list = unsorted_list[middle:]

   left_list = ਕ੍ਰਮਬੱਧਅਭੇਦ(left_list)
   right_list = ਕ੍ਰਮਬੱਧਅਭੇਦ(right_list)
   return list(merge(left_list, right_list))

# Merge the sorted halves
def merge(left_half,right_half):
   res = []
   while len(left_half) != 0 and len(right_half) != 0:
      if left_half[0] < right_half[0]:
         res.append(left_half[0])
         left_half.remove(left_half[0])
      else:
         res.append(right_half[0])
         right_half.remove(right_half[0])
   if len(left_half) == 0:
      res = res + right_half
   else:
      res = res + left_half
   return res

#insertion sort
def ਸੰਮਿਲਨਲੜੀਬੱਧ(InputList):
    for i in range(1, len(InputList)):
        j = i - 1
        nxt_element = InputList[i]
    # Compare the current element with next one
    while (InputList[j] > nxt_element) and (j >= 0):
        InputList[j + 1] = InputList[j]
        j = j - 1
    InputList[j + 1] = nxt_element
    return InputList

#selection sort
def ਚੋਣਲੜੀ(inp):
   for idx in range(len(inp)):
      min_idx = idx
      for j in range( idx +1, len(inp)):
         if inp[min_idx] > inp[j]:
            min_idx = j
# Swap the minimum value with the compared value
   inp[idx], inp[min_idx] = inp[min_idx], inp[idx]
   return inp

#linear search
def ਰੇਖਿਕਖੋਜ(lys, element):
    for i in range (len(lys)):
        if lys[i] == element:
            return i
    return -1

#binary search
def ਤੇਜ਼ਖੋਜ(lys, val):
    first = 0
    last = len(lys) - 1
    index = -1
    while (first <= last) and (index == -1):
        mid = (first + last) // 2
        if lys[mid] == val:
            index = mid
        else:
            if val < lys[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return index


#jump search
import math
def ਛਾਲਖੋਜ(lys,val):
    length = len(lys)
    jump = int(math.sqrt(length))
    left, right = 0, 0
    while left < length and lys[left] <= val:
        right = min(length - 1, left + jump)
        if lys[left] <= val and lys[right] >= val:
            break
        left += jump;
    if left >= length or lys[left] > val:
        return -1
    right = min(length - 1, right)
    i = left
    while i <= right and lys[i] <= val:
        if lys[i] == val:
            return i
        i += 1
    return -1

#fibonacci search
def ਫਿਬੋਨਾਚੀਖੋਜ(lys,val):
    fibM_minus_2 = 0
    fibM_minus_1 = 1
    fibM = fibM_minus_1 + fibM_minus_2
    while (fibM < len(lys)):
        fibM_minus_2 = fibM_minus_1
        fibM_minus_1 = fibM
        fibM = fibM_minus_1 + fibM_minus_2
    index = -1;
    while (fibM > 1):
        i = min(index + fibM_minus_2, (len(lys) - 1))
        if (lys[i] < val):
            fibM = fibM_minus_1
            fibM_minus_1 = fibM_minus_2
            fibM_minus_2 = fibM - fibM_minus_1
            index = i
        elif (lys[i] > val):
            fibM = fibM_minus_2
            fibM_minus_1 = fibM_minus_1 - fibM_minus_2
            fibM_minus_2 = fibM - fibM_minus_1
        else:
            return i
    if (fibM_minus_1 and index < (len(lys) - 1) and lys[index + 1] == val):
        return index + 1;
    return -1

#interpolation search
def ਵਿਸਥਾਰ(lys,val):
    low = 0
    high = (len(lys) - 1)
    while low <= high and val >= lys[low] and val <= lys[high]:
        index = low + int(((float(high - low) / (lys[high] - lys[low])) * (val - lys[low])))
        if lys[index] == val:
            return index
        if lys[index] < val:
            low = index + 1;
        else:
            high = index - 1;
    return -1

#platform and os start
from os import *
from platform import *

def ਭਾਰ(a):
    return path.getsize(a)  # file size in byte
def ਕੀਹੋਰਿਹਾਹੈ(a):
    return listdir(a)

def ਮੈਨੂੰਨਹੀਂਪਤਾ(a):
    return help(a)

ਕਿਹੜੀਥਾਂ=getcwd()  # current directory o
ਸੰਚਾਲਕ=processor()  # computer processor name p
ਸੰਚਾਲਕਸਨਸਕਰਨ=architecture()  # computer bit 32/64 p
ਸੰਚਾਲਕਦਾਨਾਮ=machine()  # amd64 p
ਕੰਪਿਊਟਰਦਾਨਾਮ=node()  # computer name p
ਪਰਿਚਾਲਨਣਾਂਸੰਸਕਰਨ=platform()  # osname p
ਪਰਿਚਾਲਨਦਨਾਮ=system()  # which os


#other start
def ਝੂਠਾ():
    return False
def ਸਤਯ():
    return True

#time function
import turtle
import datetime
def ਘੜੀ():
    currentDT = datetime.datetime.now()
    screen = turtle.Screen()
    trtl = turtle.Turtle()
    screen.setup(620, 620)
    screen.bgcolor('black')
    clr = ['red', 'green', 'blue', 'yellow', 'purple']
    trtl.pensize(4)
    trtl.shape('turtle')
    trtl.penup()
    trtl.pencolor('red')
    m = 0
    for i in range(12):
        m = m + 1
        trtl.penup()
        trtl.setheading(-30 * i + 60)
        trtl.forward(150)
        trtl.pendown()
        trtl.forward(25)
        trtl.penup()
        trtl.forward(20)
        trtl.write(str(m), align="center", font=("Arial", 12, "normal"))
        if m == 12:
            m = 0
        trtl.home()
    trtl.home()
    trtl.setpos(0, -250)
    trtl.pendown()
    trtl.pensize(10)
    trtl.pencolor('blue')
    trtl.circle(250)
    trtl.penup()
    trtl.setpos(150, -270)
    trtl.pendown()
    trtl.pencolor('olive')
    trtl.write((str(currentDT)), font=("Arial", 22, "normal"))
    trtl.ht()
    turtle.done()
#ਘੜੀ()
#animal function
import turtle as t
def ਕੁੱਤਾ():
    t.screensize(500, 500)
    # 【 head outline 】
    t.pensize(5)
    t.home()
    t.seth(0)
    t.pd()  # pendown
    t.color('black')
    t.circle(20, 80)  # 0
    t.circle(200, 30)  # 1
    t.circle(30, 60)  # 2
    t.circle(200, 29.5)  # 3
    t.color('black')
    t.circle(20, 60)  # 4
    t.circle(-150, 22)  # 5
    t.circle(-50, 10)  # 6
    t.circle(50, 70)  # 7
    #  determine the approximate position of the nose t.xcor and t. ycor the position of the tortoise at the beginning
    x_nose = t.xcor()
    y_nose = t.ycor()
    t.circle(30, 62)  # 8
    t.circle(200, 15)  # 9
    # 【 nose 】
    t.pu()  # penup
    t.goto(x_nose, y_nose + 25)
    t.seth(90)
    t.pd()
    t.begin_fill()
    t.circle(8)
    t.end_fill()
    # 【 eye 】
    t.pu()
    t.goto(x_nose + 48, y_nose + 55)
    t.seth(90)
    t.pd()
    t.begin_fill()
    t.circle(8)
    t.end_fill()
    # 【 ear 】
    t.pu()
    t.color('#444444')
    t.goto(x_nose + 100, y_nose + 110)
    t.seth(182)
    t.pd()
    t.circle(15, 45)
    t.color('black')
    t.circle(10, 15)
    t.circle(90, 70)
    t.circle(25, 110)
    t.rt(4)
    t.circle(90, 70)
    t.circle(10, 15)
    t.color('#444444')
    t.circle(15, 45)
    # 【 body 】
    t.pu()
    t.color('black')
    t.goto(x_nose + 90, y_nose - 30)
    t.seth(-130)
    t.pd()
    t.circle(250, 28)
    t.circle(10, 140)
    t.circle(-250, 25)
    t.circle(-200, 25)
    t.circle(-50, 85)
    t.circle(8, 145)
    t.circle(90, 45)
    t.circle(550, 5)
    # 【 tail 】
    t.seth(0)
    t.circle(60, 85)
    t.circle(40, 65)
    t.circle(40, 60)
    t.lt(150)  # left
    t.circle(-40, 90)
    t.circle(-25, 100)
    t.lt(5)
    t.fd(20)
    t.circle(10, 60)
    # 【 back 】
    t.rt(80)  # right
    t.circle(200, 35)
    # 【 collar 】
    t.pensize(20)
    t.color('#F03C3F')
    t.lt(10)
    t.circle(-200, 25)
    # 【 love bell 】
    t.pu()
    t.fd(18)
    t.lt(90)
    t.fd(18)
    t.pensize(6)
    t.seth(35)  # setheading
    t.color('#FDAF17')
    t.begin_fill()
    t.lt(135)
    t.fd(6)
    t.right(180)  # brush turn around
    t.circle(6, -180)
    t.backward(8)
    t.right(90)
    t.forward(6)
    t.circle(-6, 180)
    t.fd(15)
    t.end_fill()
    # 【 front calf 】
    t.pensize(5)
    t.pu()
    t.color('black')
    t.goto(x_nose + 100, y_nose - 125)
    t.pd()
    t.seth(-50)
    t.fd(25)
    t.circle(10, 150)
    t.fd(25)
    # 【 posterior calf 】
    t.pensize(4)
    t.pu()
    t.goto(x_nose + 314, y_nose - 125)
    t.pd()
    t.seth(-95)
    t.fd(25)
    t.circle(-5, 150)
    t.fd(2)
    t.hideturtle()
    t.done()
#ਕੁੱਤਾ()

#date and time functionss
from datetime import datetime
now=datetime.now()
def ਪੂਰੀਤਾਰੀਖ():
    return datetime.isoformat(now)
ਤਾਰੀਖ਼=datetime.today()
ਪੂਰਾਸਾਲ=now.strftime("%A %m %Y")
ਬਾਰਾਂਸਾਲ=now.strftime("%a %m %y")
ਸਮਾਂ੧੨=now.strftime("%I %p %S")
ਸਮਾਂ੨੪=now.strftime("%H:%M:%S")

#help module
def ਮਦਦਕਰੋ(a):
    return help(a)

#graphics and turtle functionsss
def ਪਾਂਡਾ():
    pen = turtle.Turtle()

    # Defining method to draw a colored circle
    # with a dynamic radius
    def ring(col, rad):
        # Set the fill
        pen.fillcolor(col)

        # Start filling the color
        pen.begin_fill()

        # Draw a circle
        pen.circle(rad)

        # Ending the filling of the color
        pen.end_fill()

    ##########################Main Section#############################

    # pen.up			 --> move turtle to air
    # pen.down		 --> move turtle to ground
    # pen.setpos		 --> move turtle to given position
    # ring(color, radius) --> draw a ring of specified color and radius
    ###################################################################

    ##### Draw ears #####
    # Draw first ear
    pen.up()
    pen.setpos(-35, 95)
    pen.down
    ring('black', 15)

    # Draw second ear
    pen.up()
    pen.setpos(35, 95)
    pen.down()
    ring('black', 15)

    ##### Draw face #####
    pen.up()
    pen.setpos(0, 35)
    pen.down()
    ring('white', 40)

    ##### Draw eyes black #####

    # Draw first eye
    pen.up()
    pen.setpos(-18, 75)
    pen.down
    ring('black', 8)

    # Draw second eye
    pen.up()
    pen.setpos(18, 75)
    pen.down()
    ring('black', 8)

    ##### Draw eyes white #####

    # Draw first eye
    pen.up()
    pen.setpos(-18, 77)
    pen.down()
    ring('white', 4)

    # Draw second eye
    pen.up()
    pen.setpos(18, 77)
    pen.down()
    ring('white', 4)

    ##### Draw nose #####
    pen.up()
    pen.setpos(0, 55)
    pen.down
    ring('black', 5)

    ##### Draw mouth #####
    pen.up()
    pen.setpos(0, 55)
    pen.down()
    pen.right(90)
    pen.circle(5, 180)
    pen.up()
    pen.setpos(0, 55)
    pen.down()
    pen.left(360)
    pen.circle(5, -180)
    pen.hideturtle()
    turtle.done()
#ਪਾਂਡਾ()

#rainbow
def ਸਤਰੰਗੀਪੀਂਘ():
    colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']
    t = turtle.Pen()
    turtle.bgcolor('black')
    for x in range(360):
        t.pencolor(colors[x % 6])
        t.width(x // 100 + 1)
        t.forward(x)
        t.left(59)
    turtle.done()

# Python program to draw square
# using Turtle Programming
def ਆਇਤਕਾਰ():
    skk = turtle.Turtle()

    for i in range(4):
        skk.forward(50)
        skk.right(90)

    turtle.done()

# Python program to draw star
# using Turtle Programming
def ਤਾਰਾ():
    star = turtle.Turtle()

    star.right(75)
    star.forward(100)

    for i in range(4):
        star.right(144)
        star.forward(100)

    turtle.done()

# Python program to draw hexagon
# using Turtle Programming
def ਹੈਕਸਾਗਨ():
    polygon = turtle.Turtle()

    num_sides = 6
    side_length = 70
    angle = 360.0 / num_sides

    for i in range(num_sides):
        polygon.forward(side_length)
        polygon.right(angle)

    turtle.done()

def ਅਸ਼ਟਭੁਜ():
    # making a workScreen
    ws = turtle.Screen()

    # defining a turtle instance
    geekyTurtle = turtle.Turtle()

    # iterating the loop 8 times
    for i in range(8):
        # moving turtle 100 units forward
        geekyTurtle.forward(100)

        # turning turtle 45 degrees so
        # as to make perfect angle for an octagon
        geekyTurtle.left(45)
    turtle.done()
def ਬਹੁਭੁਜ():
    # creating turtle pen
    t = turtle.Turtle()

    # taking input for the no of the sides of the polygon
    n = int(input("Enter the no of the sides of the polygon : "))

    # taking input for the length of the sides of the polygon
    l = int(input("Enter the length of the sides of the polygon : "))

    for _ in range(n):
        turtle.forward(l)
        turtle.right(360 / n)
    turtle.done()

# turtle library
# This to make turtle object
# tess=turtle.Turtle()

# self defined function to print coordinate
def ਕਨੈਕਸ਼ਨ():
    def buttonclick(x, y):
        print("ਤੁਸੀਂ ਇੱਥੇ ਕਲਿੱਕ ਕੀਤਾ ਹੈ ({0},{1})".format(x, y))

        # onscreen function to send coordinate

    turtle.onscreenclick(buttonclick, 1)
    turtle.listen()  # listen to incoming connections
    turtle.speed(10)  # set the speed
    turtle.done()  # hold the screen

#socket module start
def ਹੋਸਟਨਾਮ():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #Here we import two modules,and  a socket.
    #or host
    ਟੀਚਾ=input('-->')
    ਟੀਚਾ_ip= socket.gethostbyname(ਟੀਚਾ)
    print('ਹੋਸਟ ਤੇ ਸਕੈਨ ਕਰਨਾ ਸ਼ੁਰੂ ਕਰੋ:',ਟੀਚਾ_ip)
   #Work to scan # ports
def port_scan(port):
    try:
        s.connect((ਟੀਚਾ_ip,port))
        return True
    except:
            return False
    start = time.time()
    for port in range(5):
        if port_scan(port):
            print(f'ਪੋਰਟ {port} ਖੁੱਲ੍ਹਾ ਹੈ')
        else:
            print(f'ਪੋਰਟ  {port} ਬੰਦ ਕਰੋ')
            end = time.time()
            print(f' ਸਮਾਂ ਲਿਆ ਗਿਆ ਹੈ{end - start:.2f}ਦੂਜਾ')

#import module
import subprocess
#from englisttohindi.englisttohindi import EngtoHindi
# Traverse the ipconfig information
def ਨੈੱਟਵਰਕਿੰਗ():
    ਨੈੱਟਵਰਕਿੰਗ=subprocess.check_output(['ipconfig','/all']).decode('utf-8').split('\n')
    # Arrange the bytes data
    for item in  ਨੈੱਟਵਰਕਿੰਗ:
        print(item.split('\r')[:-1])

























































