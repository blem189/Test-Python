import sys
import os
import time
import random
import math
from time import sleep
from datetime import *
from tkinter import *


'''
def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
        print()


def square(z):
    a, b = 1, 1
    while a < z:
        print(b, end=' ')
        b = 2 * b
        a = a + 1
        print()
root = Tk()
label_1 = Label(root, text="Name")
label_2 = Label(root, text="Password")
entry_1 = Entry(root)
entry_2 = Entry(root)

label_1.grid(row=0)
label_2.grid(row=1)
entry_1.grid(row=0, column=1)
entry_2.grid(row=1, column=1)
root.mainloop()

'''


count = 0
Temp_Sum = 0
Ret_Sum = 0
avg = 0
random.seed(a=None)

def average(t):
    x1 = random.random()        #Generate arbitrary numbers for coordinates
    x2 = random.random()
    y1 = random.random()
    y2 = random.random()
    tx = math.sqrt((x2 - x1)**2)
    ty = math.sqrt((y2 - y1)**2)
    t = tx + ty

while count != 1000000:
    x1 = random.random()      #Generate arbitrary numbers for coordinates
    x2 = random.random()
    y1 = random.random()
    y2 = random.random()
    tx = math.sqrt((x2 - x1)**2)
    ty = math.sqrt((y2 - y1)**2)
    Temp_Sum = Temp_Sum + tx + ty
    count += 1


Print_Sum = Temp_Sum / count
print (Print_Sum)
