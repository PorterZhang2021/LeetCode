"""
给定一个 n 个元素有序的（升序）整型数组 nums 和一个目标值 target
，写一个函数搜索 nums 中的 target，
如果目标值存在返回下标，否则返回 -1。

二分查找法

循环不变量，循环不变量指的是在其工作时有一个相关的区间
如果这个区间值在使用循环的时候进行了变化，那么将不正确
所以要在循环时保证其正确性

循环时需要 左left，中mid，右right
left 初始为0
right 初始为 列表的长度

mid由公式计算 -> mid = (left + right) / 2

核心步骤就是 比较目标值和mid索引下的值
如果mid索引下的值比目标值小 -> 更改左半边
left = mid + 1
如果mid索引下的值比目标值大 -> 更改右半边
left = mid - 1
如果两者相等，那么就输出索引

本题已过
"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 初始索引
        left = 0
        right = len(nums) - 1

        # 进行循环
        while left <= right:
            # mid计算
            mid =int((left + right) / 2)

            # 如果mid索引下的值比目标值小，更改左半边
            if nums[mid] < target:
                left = mid + 1

            # 如果mid索引下的值比目标值大，更改右半边
            elif nums[mid] > target:
                right = mid - 1

            # 如果相等输出下标
            elif nums[mid] == target:
                return mid

        # 否则输出未找到的-1
        return -1