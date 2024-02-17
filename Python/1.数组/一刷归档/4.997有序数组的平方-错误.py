"""
977.有序数组平方
给你一个按 非递减顺序 排序的整数数组 nums，
返回 每个数字的平方 组成的新数组，
要求也按 非递减顺序 排序。

将所有的数平方后存入原来的位置
利用选择排序对数组重新排序

复杂度降重到o(n)
本题 暴力破解结果并不ok，因此采用双指针法

"""


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:

        # 获取长度
        length = len(nums)

        # 对所有数进行平方
        for i in range(length):
            nums[i] = nums[i] ** 2

        # 进行选择排序
        # 两层循环 一层为要放索引，一层为挑选最小数
        # 索引
        for i in range(length):
            # 挑选最小数
            for j in range(i + 1, length):
                # 如果现在的min小，交换两个数
                if nums[i] > nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]

        # 返回值
        return nums
