'''
Author: philosophylato
Date: 2022-10-01 22:18:44
LastEditors: philosophylato
LastEditTime: 2022-10-01 22:19:50
Description: your project
version: 1.0
'''
class Solution:
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """

        ss = list(s)

        aeiou = ['a', 'e', 'i', 'o', 'u', 'A','E','I','O','U']
        n = len(s)
        i = 0
        j = n-1

        while i < j:
            if ss[i] not in aeiou:
                i += 1
                continue
            if ss[j] not in aeiou:
                j -= 1
                continue
            if (i < j):
                ss[i], ss[j] = ss[j], ss[i]
            i += 1
            j -= 1
        d = ''
        return d.join(ss)