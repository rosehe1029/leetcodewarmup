'''
Author: philosophylato
Date: 2022-11-02 14:18:50
LastEditors: philosophylato
LastEditTime: 2022-11-02 14:21:03
Description: your project
version: 1.0
'''
def groupAnagrams(strs):
    hash_map=dict()
    for str in strs:
        str_tuple=tuple(sorted(str))
        if str_tuple in hash_map.keys():
            hash_map[str_tuple].append(str)
        else:
            hash_map[str_tuple]=[str]
    return list(hash_map.values())