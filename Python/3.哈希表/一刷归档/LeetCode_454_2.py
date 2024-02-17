"""
454. 四数相加 II
给你四个整数数组 nums1、nums2、nums3 和 nums4 ，
数组长度都是 n ，请你计算有多少个元组 (i, j, k, l) 能满足：
0 <= i, j, k, l < n
nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0

本题算是对两数相加结果的拆解
将a与b拆解做一次结果
在对c和d拆解做一次结果
"""


class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        # 定义一个字典
        num_count = dict()
        # 记录次数
        count = 0

        # 对a与b进行求和操作
        for num1 in nums1:
           for num2 in nums2:
               # 如果有话增加次数
               if num1+num2 in num_count:
                    num_count[num1+num2] += 1
                # 否则构建一个
               else:
                   num_count[num1+num2] = 1

        

        # 对c与d进行求和操作
        for num3 in nums3:
           for num4 in nums4:
               # 如果相减之后有结果那么就把count取出来
               if 0 - (num3 + num4) in num_count:
                    count += num_count[0-(num3+num4)]
        
        # 返回值
        return count