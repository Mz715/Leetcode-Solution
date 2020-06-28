'''
@Author: Zikuan
@Date: 2020-03-24 16:45:42
@LastEditTime: 2020-05-09 00:51:18
@LastEditors: Please set LastEditors
@Description: 给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。

示例:

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]

@FilePath: \python_code\leetcode\twosum.py
'''

#哈希map解法

class Solution:
    def __init__(self):
        pass

    def twoSum(self, nums, target):
        hashmap={}
        for index, num in enumerate(nums, start=0):
            hashmap[num]=index
        for i, num in enumerate(nums):
            j=hashmap.get(target-num)
            if j is not None and j!=i:
                return [i,j]

if __name__ == "__main__":
    print(Solution().twoSum([2, 7, 11, 15], 9))
