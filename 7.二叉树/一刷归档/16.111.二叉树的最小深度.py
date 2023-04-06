"""
111.二叉树的最小深度
给定一个二叉树，找出其最小深度。
最小深度是从根节点到最近叶子节点的最短路径上的节点数量。
说明：叶子节点是指没有子节点的节点。

本题也就是说我需要找到最小深度的叶子节点
这一题和上一题正好处于一种反向的态势
"""
# 确定参数与返回值
# 参数依然时节点 返回值依然是整数
# 确定返回的边界条件
# 如果节点为空 那么这个时候就返回0
# 确定单层逻辑循环
# 这里可以先尝试一下保存最小的情况加1呢？

from typing import *

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        # 确定边界条件
        if root is None:
            return 0
        # 单层逻辑循环
        # 左子树
        left_level = Solution.minDepth(self, root.left)
        # 右子树
        right_level = Solution.minDepth(self, root.right)
        # 中子树
        # 如果比它小就返回
        if left_level == 0 and right_level == 0:
            return left_level + 1
        elif left_level < right_level:
            return left_level + 1
        elif left_level > right_level:
            return right_level + 1
        