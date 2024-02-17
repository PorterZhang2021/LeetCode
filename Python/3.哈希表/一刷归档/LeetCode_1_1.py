"""
两数之和问题
给定一个整数数组 nums 
和一个整数目标值 target，
请你在该数组中找出 和
为目标值 target  的那 两个 整数，
并返回它们的数组下标。

你可以假设每种输入只会对应一个答案。
但是，数组中同一个元素在答案里不能重复出现。

你可以按任意顺序返回答案。

暴力破解
利用两层循环的方式，进行结果的计算
如果出现一致的结果，那么就输出两者的下标
这种情况下要注意排除 索引一致的情况
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # 进行循环
        # 第一个数的索引
        for i in range(len(nums)):
            # 第二个数的索引
            for j in range(len(nums)):
                # 如果索引一致，直接跳过
                if i == j:
                    continue
                # 如果出现相加结果满足要求的
                if nums[i] + nums[j] == target:
                    # 返回坐标
                    return [i, j]