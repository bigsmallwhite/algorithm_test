#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   2-最长公共子串.py
@Time    :   2020/10/14 00:12:55
@Author  :   Dll 
@Contact :   dengll1783600@foxmail.com
@Desc    :   查找两个字符串的最大公共子串
'''

# here put the import lib
'''
公共子串必须是连续的子串
a = 'abcd'
b = 'abdc'
最大的公共子串：'ab'
'''

# 暴力解决
def solution1(str1, str2):
    n1 = len(str1)
    n2 = len(str2)
    n = min(n1, n2)
    for i in range(n, 0, -1):
        

if __name__ == '__main__':
    str1 = 'abcd'
    str2 = 'abdc'
    print(solution1(str1, str2))