'''
Author: philosophylato
Date: 2022-10-10 17:42:34
LastEditors: philosophylato
LastEditTime: 2022-10-12 17:11:27
Description: 
version: 1.0
'''
def rotate(matrix):
    matrix[:]=zip(*matrix[::-1])
    return matrix
matrix=[[1,2,3],[4,5,6],[7,8,9]]
print(rotate(matrix))
def rotate_(matrix):
    N=len(matrix)
    for i in range(N):
        '''第一层，这里的i即里面每个列表作为一个整体元素，遍历它们N次'''
        for j in range(i):
            '''第二层，这里j的遍历次数为i次，随着第一层的i增大，j遍历的范围也随之增大到
            最终的i，在j每一轮遍历里，i都是一个固定值，而且下面的公式同时进行没有先后，
            即横坐标纵坐标互换
            '''
            matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        #沿着垂直中心线翻转
        for  i in range(N):
            matrix[i][:]=matrix[i][::-1]



'''
如果是顺时针旋转90度，一定是先对角线翻转，再水平翻转

'''
