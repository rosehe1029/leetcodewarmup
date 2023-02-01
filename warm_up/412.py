'''
Given an integer n, return a string array answer (1-indexed) where:
    answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
    answer[i] == "Fizz" if i is divisible by 3.
    answer[i] == "Buzz" if i is divisible by 5.
    answer[i] == i (as a string) if none of the above conditions are true.
Example 1:
Input: n = 3
Output: ["1","2","Fizz"]
Example 2:
Input: n = 5
Output: ["1","2","Fizz","4","Buzz"]
Example 3:
Input: n = 15
Output: ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]
Constraints:
    1 <= n <= 104
来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/fizz-buzz
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

def fizzBuzz( n: int):
    res = [] #设置一个空的返回数组
    for i in range(1, n + 1): #开始遍历，因为是从1~n开始，所以这边循环从1开始
        if i % 3 == 0 and i % 5 == 0: #如果i 同时是 3 和 5 的倍数
            res.append('FizzBuzz') #则把字符串'FizzBuzz'放入res中，append是从数组后面加新的字符的函数
        elif i % 3 == 0 and i % 5 != 0:#如果i是3的倍数
            res.append('Fizz')#则把字符串'Fizz'放入res中，
        elif i % 3 != 0 and i % 5 == 0:#如果i是5的倍数
            res.append('Buzz')#则把字符串'Buzz'放入res中，
        else:
            res.append(str(i)) #否则的话，这是i本身，这边函数str是将数字转换为字符串的命令
    return res #返回res即可


print(fizzBuzz(7))