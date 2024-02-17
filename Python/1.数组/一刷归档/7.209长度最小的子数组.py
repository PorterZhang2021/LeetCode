"""
209，长度最小的子数组
给定一个含有 n 个正整数的数组和一个正整数 target 。
找出该数组中满足其和 ≥ target 的长度最小的
连续子数组
[numsl, numsl+1, ..., numsr-1, numsr] ，
并返回其长度。
如果不存在符合条件的子数组，返回 0 。

采用滑动窗口的方法来完成此题目 复杂度为O(N)

利用循环来确定终止位置的参数
    获取一个总和的结果
    如果出现总和结果>=目标值
    那么开始移动起始位置并记录最小长度
        每次记录一下更新的最小长度
        减去要更新的索引值
        对起始索引自增一次

"""

import sys


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # 最小长度 默认为python最大支持长度
        min_len = sys.maxsize
        # 数组长度
        nums_len = len(nums)
        # 总和
        total = 0
        # 起始索引
        start = 0

        for end in range(nums_len):
            # 获取总和
            total += nums[end]
            # 缩小窗口
            # 这里的条件是说明有可能有最小数组的情况
            while total >= target:
                # 记录一下更新的最小长度
                # 减去要更新的索引值
                sub_length = (end - start + 1)
                # 计算一下最小索引
                if min_len > sub_length:
                    min_len = sub_length
                # 减少数
                total -= nums[start]
                # 对起始索引自增
                start += 1

        # 如果没变那么返回0否则返回长度
        if min_len == sys.maxsize:
            # 返回0
            return 0
        else:
            # 返回最小长度
            return min_len
