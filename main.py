# -*- coding: utf-8 -*-
"""
Created on Sat Nov 12 23:17:30 2022

@author: tanay
"""

a = 1 #integer
b = 2.0 #float
c = 'abc' #string
d = "def" #string


# print(a, b, c, d)

# H.W. :: All the data types in python

# ______________________DATA STRUCTURES _____________________________

l = [1,2,3,4, 3, 4,5] #list, mutable
t = (12,3,45,0,23,23,23,2) # tuple, immutable
s = {1,2,3,4,4,5,5} #set, does not stores any duplicates, immutable
d = {1:1, 2:2, 2:4, 4:1} #dictionary


# print(l)
# print(t)
# print(s)
# print(d)

# H.W. :: All the data structures in python
# ________________________________________________________________

# LIST: Data strucuture in python, to hold the data in continous fashion in the memory
# it can have duplicates
# it can be changes, hence it is mutable
# it has mutliple functions and can be looped

l = [4, 12, 21, 2121,12,12,1,1,5]

# print(l)
# print(l.index(2121))
# print(l[2])
# print(len(l))
# print(l*2)
# l.reverse()
# print(l)


# l.sort()
# print(l)
# H.W.: how to sort a list in descending order?


# ---------------------------------------------------------------------

a = [1,2,3,4,5,6,7,8,9,10]
a[0] = 11
print(a)
# c= a.index(b)
# print(c)


# ------------------------------------------------------------------
# TUPLES: Tuple is a data structure in python, it is immutable, so we cannot change the value of a tuple


t = (1,2,2,3,4,5)

# t[0] = 11
'''assiging 1st element of typle as 11'''
# print(t)

# ---------------------------------------------------------------------

# comments in python are starting from # sign
'''this is comment'''


# ----------------------------------------------------------------------
abc = {1,2,3,4,4,4,4,4,5,6,3}
print(abc)
# abc[0] = 10
# print(abc)



# -----------------------------------------------------------------------
# DICTIONARY: consists of key value pairs, it is mutables

di = {1:2, 
      'a':1,
      'b':2}


# print(di.keys())
# print(di.values())
# print(di.items())

di[1] = 10
# print(di)

# # -------------------------------------------------------------
# # Reserved keyword
# there are some keyword which have some meaning and are interpreted as they are doing some task

# print, import, if, else, elif, try, except, break, continue, 

# H/w: how many reserved keywords are there in python? -- 16/11/22


# -------------------------------------------------------------

#CONDITIONAL STATEMENT IN PYTHON
# THEY CONTROL THE FLOW OF THE CODE, LIKE:-
# 1. IF, ELSE, ELIF

# if (condtion):
#     STATEMENT
# elif condition2:
#     STATMENT 3
# else:
#     STATEMENT 2


# a = 3
# b = 3

# if a == b:
#     print('Both the numbers are same.')
# elif a>b:
#     print('a is greater')
# else:
#     print('b is greater')


# H. W - Write a program to find greatest of3 numbers.
a = 3
b = 1
c = 2

if a>b and a>c:
    print('a is greatest')
elif b>a and b>c:
    print('b is greatest')
elif c>a and c>b:
    print('c is greatest')
else:
    print('numbers are equal.')


# ----------------------------------------------------------
# LOGICAL OPERATORS in python
# 1. or - checks if any one condition is correct.
# 2. and - checks if all conditions are correct.

if a==b or c==b:
    print('2 number are equal')
else:
    print('Blabla')
    
    
# ------------------------------------------------------------

# LOOP - Loop is basically a control flow statrement in python which transfers the control of the code from one statement 
# to other


# 1. for - for loop is generally used when we have to loop over a specific ranges of values
# 2. while - is generally used until a condition is met


l = [1,2,3,4,5,6]

# for i in l:
#     print(i)
    
n = len(l)
print(n)

for i in range(n):
    # print(i)
    print(l[i])
    
    
# for k in range(10):
#     print(k)

# H.W. - how to run a for loop on a list to print reverse list
# --------------------------------------------------------------------

# WHILE LOOP
# a = 2
# b = 0

# while a>=b:
#     print(a, b)
#     b+=1 #b = b+!

# -------------------------------------------------------------------------
# OPERATORS IN PYTHON
# the algebric operators that we used in maths
# + --> addtion
# - --> sub
# * --> mul
# / --> division (float)
# // --> division integer
# % --> reminder from division


# print(3%2)

# -----------------------------------------------------------------------------
# FUNCTIONS - functins are nothing but resuable piece of code which we can define and call whenever we need



# def function_name(arg1, arg2, ....., argn):
#     statements


def mul(a, b):
    return (a*b)


v = mul(1, 3)
print(v)
# h.w --> create a function for all the arithematic operators in python and use 3 argumnets
    

# -------------------------------------------------------------------------------
def abc(a, b):
    def subtract(a,b):
        return a-b
    return subtract(a, b)
    
a =2
b=3
print(abc(a, b))
# ---------------------------------------------------------------------------------

# OOPS : Object Oriented Programming

# Class, Object, methods, inheritence, abstraction, encapsulation

# Class: it is a wrapper where you can define the properties of an object
print('-----------------------------------------------------------------')
class Math:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def subtract(self):
        return self.a- self.b
    def multiply(self):
        return self.a * self.b
    def divide(self):
        return self.a // self.b
    def reminder(self):
        return self.a % self.b
    
    
#object: object is a real world entity which brings the class into real life
mat = Math(2, 5)
s = mat.subtract()
print(s)


mat2 = Math(19, 9)
s = mat2.subtract()
print(s)

# ------------------------------------------------------------------------------
# Inheritence: Passing the attributes of a parent class to its child 

# ABC --> Child
# Math --> Parent
class ABC(Math):
    print('inside abc')
    
    
abc = ABC(2,5)
print(abc.subtract())


# H/w: What are the different types of inhreitence in pythn and their example? code?
# -------------------------------------------------------------------------------


# Access modifiers: They control the access of any variable, attribute, member, function, etc.

# 1. Public: Accessible by anyone inside the same code
# 2. Protected: Accessible by same class object or by its child class
# 3. Private: Not accessible anywhere 

class A:
    a = 10
    _b = 20
    __c = 30
    print(_b + __c)
    


class B(A):
    print(A._b)

d = B

# -------------------------------------------------------------------------------
# package: is basically collection of python programs
# module: is  a collection of packages
# import pandas as pd
# import numpy as np
import datetime

# pandas --> is used to deal with the data, helps in data manipultaion
# numpy --> is used for mathematical computations
# os --> is used to deal with operating system concepts
# sys --> is used to deal with system properties and attributes
# datetime --> used for date time


today = datetime.date.today()
print(today)

time = datetime.datetime.now()
print(time)

# H.w: to list down 5 modules in python? the usage of the same?