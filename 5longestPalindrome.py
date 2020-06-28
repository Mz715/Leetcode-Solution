'''
@Author: your name
@Date: 2020-06-28 13:08:44
@LastEditTime: 2020-06-28 17:22:02
@LastEditors: Please set LastEditors
@Description: 给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。
@FilePath: \python_code\leetcode\longestPalindrome.py
'''

class Solution:
    def longestPalindrome(self, s: str) -> str:
        size = len(s)
        if size < 2:
            return s

        dp = [[False for _ in range(size)] for _ in range(size)]

        max_len = 1
        start = 0

        #对角线都是True，因为单个字符一定是回文串
        for i in range(size):
            dp[i][i] = True

        #从竖列开始填表，注意状态转移的方向
        for j in range(1, size):
            for i in range(0, j):
                #首尾相等
                if s[i] == s[j]:
                    #首尾相等并且字符串长度小于等于3，一定是回文
                    if j - i < 3:
                        dp[i][j] = True
                    else:# 此处为状态转移方程，回文串去掉首尾字符依旧是回文串
                        dp[i][j] = dp[i + 1][j - 1]
                else:
                    dp[i][j] = False
                
                #dp[i][j]为True时，判断字符串长度，更新输出，找到最大回文串
                if dp[i][j]:
                    cur_len = j - i + 1
                    if cur_len > max_len:
                        max_len = cur_len
                        start = i
        return s[start:start + max_len]
