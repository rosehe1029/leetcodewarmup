'''
Author: philosophylato
Date: 2022-10-27 16:50:06
LastEditors: philosophylato
LastEditTime: 2022-10-27 16:59:30
Description: your project
version: 1.0
'''
class MyHashMap:
    def __init__(self):
        self.map=[[-1]*1000 for i in range(1001)]
    
    def put(self,key:int,value:int)
        row,col=key//1000,key%1000
        self.map[row][col]=value

    def get(self,key:int):
        row,col=key//1000,key%1000
        return self.map[row][col]
    
    def remove(self,key:int):
        row,col=key//1000,key%1000
        self.map[row][col]=-1
        










