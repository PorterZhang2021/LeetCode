"""
977.有序数组平方
给你一个按 非递减顺序 排序的整数数组 nums，
返回 每个数字的平方 组成的新数组，
要求也按 非递减顺序 排序。

双指针
双指针的情况下需要先拷贝一个数组，因此需要使用深度拷贝

此题双指针为两个方向，一个为left，一个为right
如果出现left的平方值比right的平方值大的情况下，那么选择left，并自增
否则选择right，并自减

"""

import copy

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # 结果数组
        result = copy.deepcopy(nums)

        # left与right的情况
        left = 0
        right = len(nums) - 1
        # 结果数组索引下标
        index = len(nums) - 1

        # 判断两个是否还能比较，这里不能少了=的情况
        while left <= right:
            # 如果左边大，那么选择左边并自增
            if nums[left] ** 2 > nums[right] ** 2:
                # 存放平方值
                result[index] = nums[left]
                # left 自增
                left += 1
            # 如果左边小，选择右边，右边自减
            else:
                # 存放平方值
                result[index] = nums[right]
                # right 自减
                right -= 1
            # 索引减1
            index -= 1

        # 返回数组
        return result