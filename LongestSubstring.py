'''
@Author: wzk
@Date: 2020-06-24 13:13:41
@LastEditTime: 2020-06-24 14:10:12
@LastEditors: Please set LastEditors
@Description: 给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
@FilePath: \python_code\leetcode\LongestSubstring.py
'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "": return 0
        if len(s) ==  1: return 1

        max = 0
        cur = 0
        check = list()
        n = len(s)
       
        for i in range(n):
            val = s[i]
            if not val in check:
                check.append(val)
                cur += 1
            else:
                index = check.index(val)
                check = check[index+1:]
                check.append(val)
                cur = len(check)
            if cur>max: max=cur
        return max

"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 如果字符串s为空，返回0
        if not s:return 0
        # 保存窗口内字符串
        lookup = list()
        n = len(s)
        # 最大子串长度
        max_len = 0
        # 当前窗口长度
        cur_len = 0
        # 遍历字符串s
        for i in range(n):
            val = s[i]
            # 如果该值不在窗口中
            if not val in lookup:
                # 添加到窗口内
                lookup.append(val)
                # 当前长度+1
                cur_len+=1
            # 如果该值在窗口中已存在
            else:
                # 获取其在窗口中的位置
                index = lookup.index(val)
                # 移除该位置及之前的字符，相当于上图中的图3到图4
                lookup = lookup[index+1:]
                lookup.append(val)
                # 当前长度更新为窗口长度
                cur_len = len(lookup)
            # 如果当前长度大于最大长度，更新最大长度值
            if cur_len > max_len:max_len = cur_len
        # 返回最大子串长度
        return max_len
"""