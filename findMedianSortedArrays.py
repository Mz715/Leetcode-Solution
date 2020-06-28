'''
@Author: your name
@Date: 2020-06-27 12:49:25
@LastEditTime: 2020-06-27 14:51:36
@LastEditors: Please set LastEditors
@Description:给定两个大小为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。

请你找出这两个正序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。

你可以假设 nums1 和 nums2 不会同时为空。

特别需要注意时间复杂度要求！！！

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/median-of-two-sorted-arrays
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
@FilePath: \python_code\leetcode\findMedianSortedArrays.py
'''
from typing import List

class Solution:
    def get_kth(self, nums1, nums2, k):#找第k小数的方法
        # print(nums1, nums2, 'k=', k)
        m, n = len(nums1), len(nums2)
        if m == 0: return nums2[k-1]
        if n == 0: return nums1[k-1]
        if k == 1: return min(nums1[0], nums2[0])

        drop1, drop2 = min(k//2, m), min(k//2, n)   # 丢弃个数，如果数组总个数小于k/2则丢弃整个数组
        
        if nums1[drop1-1] <= nums2[drop2-1]:  # 丢弃小的那一部分
            return self.get_kth(nums1[drop1:m], nums2, k-drop1)
        else:
            return self.get_kth(nums1, nums2[drop2:n], k-drop2)
    
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        # 整合奇偶数情况
        mid_left = self.get_kth(nums1, nums2, (m+n+1)//2)
        mid_right = self.get_kth(nums1, nums2, (m+n+2)//2)
        return (mid_left+mid_right)/2
'''
from typing import List

class Solution:
    
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        nums = nums1 + nums2
        nums.sort()
        
        mid_left = nums[(m+n+1)//2-1]
        
        mid_right =  nums[(m+n+2)//2-1]
        return (mid_left+mid_right)/2
'''
if __name__ == "__main__":
    print(Solution().findMedianSortedArrays([1,3],[2]))