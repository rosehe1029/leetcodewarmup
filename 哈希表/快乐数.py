'''
Author: philosophylato
Date: 2022-11-01 17:29:47
LastEditors: philosophylato
LastEditTime: 2022-11-01 21:52:28
Description: your project
version: 1.0
'''
def isHappy(n):
    def calculate_happy(num):
        sum_=0
        #从个位开始依次取，平方求和
        while num:
            sum_+=(num%10)**2
            num=num//10
        return sum_
    record=set()

    while True:
        n=calculate_happy(n)
        if n==1:
            return True
        
        if n in record:
            return False
        else:
            record.add(n)










