'''
@Author: your name
@Date: 2020-06-24 14:11:48
@LastEditTime: 2020-06-24 15:55:18
@LastEditors: Please set LastEditors
@Description: 给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。
假定每组输入只存在唯一答案。
@FilePath: \python_code\leetcode\threesumclosest.py
'''

#解题思路： 排序+双指针
 
from typing import List
 
class Solution:
    def threeSumClosest(self, nums: List[int], target: int):
        n=len(nums)
        if(not nums or n<3):
            return None
        nums.sort()
        res=float("inf")
        for i in range(n):
            if(i>0 and nums[i]==nums[i-1]):
                continue
            L=i+1
            R=n-1
            while(L<R):
                cur_sum=nums[i]+nums[L]+nums[R]
                
                if(cur_sum==target):
                    return target
                if(abs(cur_sum-target)<abs(res-target)):
                    res=cur_sum
                if(cur_sum-target<0):
                    L+=1
                else:
                    R-=1
        return res

"""
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # 特判：n=3，返回sum(nums)
        n = len(nums)
        if n == 3:
            return sum(nums)
        # 令最小差的绝对值为无限大
        minDiff = float("inf")
        closestSum = 0
        # nums排序
        nums.sort()
        # 遍历nums
        for i in range(n-2):
            if i > 1 and nums[i] == nums[i-1]:
                continue
            # 双指针
            L = i + 1
            R = n - 1
            while(L < R):
                threeSum = nums[i] + nums[L] + nums[R]
                diff = threeSum - target
                # 如果diff的绝对值比minDiff小，那么更新minDiff和closestSum
                if abs(diff) < minDiff:
                    minDiff = abs(diff)
                    closestSum = threeSum
                if diff == 0:
                    # 如果diff为0，直接返回threeSum
                    return closestSum
                elif diff < 0:
                    # 说明threeSum < target，L右移
                    L += 1
                    while(L<R and nums[L]==nums[L-1]):
                        L +=1
                else:
                    # 说明threeSum > target，R左移
                    R -= 1
                    while(L<R and nums[R]==nums[R+1]):
                        R -= 1
        return closestSum
"""
if __name__ == "__main__":
    nums = [1,-2,1,4]
    target = 0
    print(Solution().threeSumClosest(nums, target))
