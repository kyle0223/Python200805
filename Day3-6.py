# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 15:16:36 2020

@author: user
"""

d={}

print("歡迎進入Kyle字典")

while True:
    print("1. 建立詞彙")
    print("2. 中翻英")
    print("3. 英翻中")
    print("4. 列出所有詞彙")
    print("5. 學習測驗")
    print("6. 離開")
    sel=input("請輸入數字")
    sel=int(sel)
    if sel==1:
        while True:
            E=str(input("輸入英文(按0返回)"))
            M=str(input("輸入中文(同上)"))
            d[E]=M
            if E=='0':
                break
        
    if sel==4:
       for k,v, in d.items():
           print(k,v)
           
           
    if sel==2:
        EM=input("")
           
           
           
           
           
           
           
           
           
           
           
           
           
           