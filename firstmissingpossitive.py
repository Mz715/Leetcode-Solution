'''
@Author: your name
@Date: 2020-06-24 14:11:48
@LastEditTime: 2020-06-27 12:10:18
@LastEditors: Please set LastEditors
@Description: 给你一个未排序的整数数组，请你找出其中没有出现的最小的正整数。
@FilePath: \python_code\leetcode\firstmissingpossitive.py
'''

from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort(reverse = True)
        for i in range(1,nums[0]+2):
            if i not in nums:
                return i
        

if __name__ == "__main__":

    print(Solution().firstMissingPositive([1,2,0]))