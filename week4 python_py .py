# -*- coding: utf-8 -*-
"""python.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1eQ9jXh_BXAR1nV3npQpHWyrlbYK2xiTF
"""

double=lambda x:2*x
print(double(5))
add=lambda x,y:x+y
print(add(5,4))

list1=[1,2,3,4,5]
iseven=lambda x:x%2==0
list2=list(filter(iseven,list1))
print(list2)

def addition(n):
  return n+n
numbers=[1,2,3,4]
result=map(addition,numbers)
print(list(result))

import functools
lis=[1,3,6,2,5]
print("the sum of list elements is:",end="")
print(functools.reduce(lambda a,b:a+b,lis))