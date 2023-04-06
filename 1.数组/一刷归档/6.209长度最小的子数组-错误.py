"""
209，长度最小的子数组
给定一个含有 n 个正整数的数组和一个正整数 target 。
找出该数组中满足其和 ≥ target 的长度最小的
连续子数组
[numsl, numsl+1, ..., numsr-1, numsr] ，
并返回其长度。
如果不存在符合条件的子数组，返回 0 。

穷举法，暴力破解
两层循环
第一层循环 用于确定起始索引
第二层循环 用于确定结束索引
    进行求和运算，如果出现与目标数相等的就保存好最小长度与两个索引的位置
    最小长度问题：
    当出现最小长度比现有最小长度小的时候，进行新一轮的更新
构建一个数组用来存放最小长度以及返回最小长度，如果没有则返回0

暴力求解这个方法现在有误
"""


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # 最小长度
        min_len = 0
        # 数组长度
        nums_len = len(nums) - 1

        # 获取起始索引位置
        for i in range(nums_len):
            # 数的总和
            total = 0
            # 从起始索引开始累加运算
            for j in range(i, nums_len):
                # 获取计算结果
                total += nums[i]
                # 如果计算的结果和目标所需目标一致
                if target == total:
                    # 比现在的最小长度小
                    if min_len > (j - i):
                        # 保存最新的最小长度
                        min_len = j - i
                        # 保存索引值
                        index = i
                        # 保存终点值
                        end = j

        # 返回最小长度
        return min_len
