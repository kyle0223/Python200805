# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 14:31:29 2020

@author: user
"""

d={}

while True:
    print('----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    print('1. 加法')
    print('2. 減法')
    print('3. 乘法')      
    print('4. 除法')
    print('5. go away')
    
    num=int(input("enter number"))
    
    if num==1:
        add1=int(input("enter num"))
        add2=int(input("enter num"))
        print(add1,'+',add2,'=',add1+add2)
        
    elif num==2:
        min1=int(input("enter num"))
        min2=int(input("enter num"))
        print(min1,'-',min2,'=',min1-min2)      
          
    elif num==3:
        mul1=int(input("enter num"))
        mul2=int(input("enter num"))
        print(mul1,'*',mul2,'=',mul1*mul2)
           
    elif num==4:
        div1=int(input("enter num"))
        div2=int(input("enter num"))
        print(div1,'/',div2,'=',div1/div2)
    else:
         break