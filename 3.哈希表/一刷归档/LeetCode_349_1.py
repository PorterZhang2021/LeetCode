"""
349.两个数组的交集
给定两个数组 nums1 和 nums2，
返回 它们的交集 。
输出结果中的每个元素一定是 唯一 的。
我们可以 不考虑输出结果的顺序 。

1. 利用字典，验证两个字典当中是否有相同的值
2. 利用双层循环来验证是否有相同的值，存入字典
"""


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # 字典
        dict_number = {}
        # 存放集合
        number_list = []

        # 循环查找nums1
        for num1 in nums1:
            # 判断是否在其内部
            if num1 in nums2:
                # 存入字典
                dict_number[num1] = 0

        # 将字典的key输出放入一个list中
        for key in dict_number.keys():
            # 加入要存放的集合中
            number_list.append(key)

        # 返回值
        return number_list
