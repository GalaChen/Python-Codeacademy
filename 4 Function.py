########################################
############    Function    ############
########################################

def tax(bill):
  """Adds 8% tax to a restaurant bill."""
  bill *= 1.08
  print "With tax: %f" % bill
  return bill

def tip(bill):
  """Adds 15% tip to a restaurant bill."""
  bill *= 1.15
  print "With tip: %f" % bill
  return bill
  
meal_cost = 100
meal_with_tax = tax(meal_cost)
meal_with_tip = tip(meal_with_tax)

#定义函数
def hello_world():
  print "Hello World!"

#一个典型的函数应包含三部分
#def作为开头，紧接着连接函数名；
#函数名紧跟的括号内填写参数，括号外有冒号
#函数体是函数执行的任务及其返回的内容

#函数的嵌套
def fun_one(n):
  return n * 5

def fun_two(m):
  return fun_one(m) + 7
  
##################  module的使用  ##################
import math 
print math.sqrt(25)
#注意module导入后，相应的函数前应添加module名称

from math import sqrt
print sqrt(5)
#也可以通过这种方式来导入module中具体的函数

from math import *
print sqrt(4)
#导入所有的变量和函数，module内任何函数都可直接调用

import math # Imports the math module
everything = dir(math) # Sets everything to a list of things from math
print everything # Prints 'em all!
#dir可罗列module里面所有的函数

def smallest_number(*args)
#*args表示可以传递多个参数

max() min() abs() type() 
