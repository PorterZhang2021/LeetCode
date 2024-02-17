"""
454.四数相加Ⅱ
给你四个整数数组 nums1、nums2、nums3 和 nums4 ，
数组长度都是 n ，
请你计算有多少个元组 (i, j, k, l) 能满足：
0 <= i, j, k, l < n
nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0

1. 暴力求解法，使用暴力求解法的复杂度大概是o(n^4)
此题超出时间限制
"""
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        # 元组
        tuple_list = []

        # 进行循环
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                for k in range(len(nums3)):
                    for l in range(len(nums4)):
                        # 如果结果合成为0
                        if nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0:
                            # 存放元组
                            tuple_list.append((i, j, k, l))
        
        # 返回长度
        return len(tuple_list)