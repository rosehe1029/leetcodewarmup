'''
Author: philosophylato
Date: 2022-11-02 14:51:38
LastEditors: philosophylato
LastEditTime: 2022-11-02 14:58:39
Description: your project
version: 1.0
'''
def findDuplicateSubtrees(root):
    hashmap={}
    output=[]
    DFS(root,hashmap,output)
    return output
def DFS(root,hashmap,output):
    if root ==None:return ""
    temp_root=str(root.val)
    temp_left=DFS(root.left,hashmap,output)
    temp_right=DFS(root.right,hashmap,output)
    temp=temp_root+","+temp_left+","+temp_right
    print(temp)
    if temp not in hashmap:
        hashmap[temp]=1
    elif temp in hashmap:
        if hashmap[temp]==1:
            output.append(root)
        hashmap[temp]+=1
    return temp
    