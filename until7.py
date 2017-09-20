def sayHello():
	print("Hello")

sayHello()

def sayHello(name):
	print("Hello " + str(name))

sayHello('Bobi')

def sayAge(name, age=18):
	print('My name is ' + name + '. I\'m ' + str(age))

sayAge('xiaoli', 20)
sayAge(age=30, name='Huluwa')
sayAge('bingbing')

def addNub(a, b):
	return a+b

print(addNub(40,90))

def addAll(*toppings):
	b=0;
	for a in toppings:
		b+=a
	return b

print(addAll(1,2,3,4,5,6))

# 函数的导入 
'''
import py
py.make(0)

from py import make
make(0)

import py as pyth
python.make(0)

from py import make as mk
mk(0)

from py import *

