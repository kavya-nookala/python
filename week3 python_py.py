# -*- coding: utf-8 -*-
"""python.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/18TbAlkYclsYtmCiJqCt7KM0HIOuBmXWI
"""

def add(a,b):
  return a+b
def sub(c,d):
  return c-d
def mul(e,f):
  return e*f
def div(g,h):
  return g/h
print("***************")
print("1.to perform addition")
print("2.to perform subtraction")
print("3.to perform multiplication")
print("4.to perform division")
print("***************")
ch=int(input("enter your choice"))
if ch==1:
  a=int(input("enter 1st number"))
  b=int(input("enter 2nd number"))
  print(add(a,b))
elif ch==2:
  c=int(input("enter 1st number"))
  d=int(input("enter 2nd number"))
  print(sub(c,d))
elif ch==3:
  e=int(input("enter 1st number"))
  f=int(input("enter 2nd number"))
  print(mul(e,f))
elif ch==4:
  g=int(input("enter 1st number"))
  h=int(input("enter 2nd number"))
  print(div(g/h))
else:
  print("wrong choice")

def fun(list1,list2):
  for x in list1:
    for y in list2:
      if x==y:
        result=True
      else:
        result=False
  return result
print(fun([1,2,3,4,5],[1,2,3,4,5]))

s=input("enter a string")
if (s==s[::-1]):
  print("palindrome")
else:
  print("not a palindrome")

for _ in range(10):
  print("python")

def fact(n):
  if n==1:
    return n
  else:
    return n*fact(n-1)
num=int(input("enter a number"))
if num<0:
  print("no factorial")
elif num==0:
  print("factorial of 0 is 1")
else:
  print("factorial of ",num," is" ,fact(num))

list1=['python','sita',20,30]
print(list1)

#integers
list1=[]
n=int(input("enter integer list size"))
for i in range(0,n):
  ele=int(input("enter element"))
  list1.append(ele)
#strings
list2=[]
m=int(input("enter string list size"))
for j in range(0,m):
  elem=input()
  list2.append(elem)
lst=list1+list2
print(lst)
y=len(lst)
if (y==0):
  print("list is empty")
else:
  print("list is not empty")

innp=input("enter list elements seperated by spaces")
list1=innp.split()
print(list1)
