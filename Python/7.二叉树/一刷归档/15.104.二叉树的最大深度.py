"""
104.二叉树的最大深度

给定一个二叉树，找出其最大深度。
二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。
说明: 叶子节点是指没有子节点的节点。

"""
# 确定参数与返回值 参数为 节点root  返回值为 整数类型 int
# 确定边界条件 节点为空的时候 返回0
# 确定单层逻辑
# 进入左子树
# 进入右子树
# 中层逻辑 判断左子树与右子树 哪一个的层次更多 
# 出现多的那个层次 就作为返回值+1
from typing import *

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # 如果节点为空
        if root is None:
            return 0
        
        # 进入左子树
        left_level = Solution.maxDepth(self, root.left)
        # 进入右子树
        right_level = Solution.maxDepth(self, root.right)
        # 中间子树情况判定
        if left_level > right_level:
            return  left_level + 1
        else:
            return right_level + 1
