# -*- coding: utf-8 -*-
"""TP0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1b_RB8tRYzX9kU1VHNPeuzvo2HNbJ1q57
"""

#EX1
def updatech(chaine):
  v=['a','o','u','i','e']
  V=['A','O','U','I','E']
  for i in range(len(chaine)):
    m=1
    for j in range(len(v)):
      if chaine[i]==v[j]:
        m=0;
        print(V[j], end="")
    if m==1:
      print(chaine[i], end="")
updatech("souad")

#EX2
def sumprod(x,y):
  produit=x*y
  somme=x+y
  print("la somme de",x,"et",y,"est:",somme,"et leur produit est:",produit)
sumprod(2,3)

#EX3
def sumstring(ch1,ch2,ch3):
  print(ch1+ch2+ch3)
sumstring("sum","str","ing")

#EX4
def compter():
  for i in range (1,11):
    print(i)
compter()

#EX5
def pyramide(x):
  s=1
  while s<x+1:
    for i in range(1,s+1):
      print(i,end=" ")
    print("\n")
    s=s+1
pyramide(5)

#EX6
def table_multipl(x):
  for i in range(1,13):
    print(i,"*",x,"=",x*i)
table_multipl(5)

#EX7
def ex7(tab):
  if tab[0]==tab[len(tab)-1] :
    return True
  else:
    return False
print(ex7([1,3,1]))
print(ex7([1,2,3]))

#EX8
def ex8(x,y):
  p=x*y
  if p>1000:
    return p
  else:
    return x+y
print(ex6(50,30))