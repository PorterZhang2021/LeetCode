"""
654. 最大二叉树
给定一个不重复的整数数组 nums 。 
最大二叉树 可以用下面的算法从 nums 递归地构建:
创建一个根节点，其值为 nums 中的最大值。
递归地在最大值 左边 的 子数组前缀上 构建左子树。
递归地在最大值 右边 的 子数组后缀上 构建右子树。
返回 nums 构建的 最大二叉树 。

二叉树的构建
1. 如果数组为空 那么就进行返回
2. 找到最大的数用来构建节点
3. 找到最大的数的索引
4. 将其划分成左半边与右半边
5. 左半边构建条件
6. 右半边构建条件
7. 返回节点
"""

from typing import *
from NewTree import TreeNode
from NewTree import creatTree

class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        # 1. 如果数组为空 那么就进行返回
        if not nums:
            return None
        # 2. 找到最大的数用来构建节点
        max_val = max(nums)
        root = TreeNode(max_val)
        # 3. 找到最大的数的索引
        index = nums.index(max_val)
        # 4. 将其划分成左半边与右半边
        left_nums = nums[:index]
        right_nums = nums[index+1:]
        # 5. 左半边构建条件
        root.left = self.constructMaximumBinaryTree(left_nums)
        # 6. 右半边构建条件
        root.right = self.constructMaximumBinaryTree(right_nums)
        # 7. 返回节点
        return root