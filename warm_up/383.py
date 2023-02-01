'''
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.
Each letter in magazine can only be used once in ransomNote.
Example 1:
Input: ransomNote = "a", magazine = "b"
Output: false
Example 2:
Input: ransomNote = "aa", magazine = "ab"
Output: false
Example 3:
Input: ransomNote = "aa", magazine = "aab"
Output: true
Constraints:
    1 <= ransomNote.length, magazine.length <= 105
    ransomNote and magazine consist of lowercase English letters.
来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/ransom-note
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

'''
from collections import Counter

def canConstruct( ransomNote: str, magazine: str) -> bool:
    return  not ( Counter(ransomNote)-Counter(magazine))

#1.用哈希表存储magazine字符及个数
#2.遍历ransomNote：
#  2.1.如果哈希表中有该字符并且字符计数大于零，说明仍能由magzine构成，此时对应的字符计数减一
#  2.2.否则，无法构成，返回False
def canConstruct2(ransomNote:str,magazine:str)->bool:
    magazine_dict={}
    for c in magazine:
        if c in magazine_dict:
            magazine_dict[c]+=1
        else:
            magazine_dict[c]=1
    
    for c in ransomNote:
        if c in magazine_dict and magazine_dict[c]>0:
            magazine_dict[c]-=1
        else:
            return False
    
    return True

ransomNote = "aa"
magazine = "aab"

print(canConstruct(ransomNote, magazine))

