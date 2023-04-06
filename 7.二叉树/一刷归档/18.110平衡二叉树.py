"""
110.平衡二叉树
给定一个二叉树，判断它是否是高度平衡的二叉树。
本题中，一棵高度平衡二叉树定义为：
一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1 。

本题首先想到的思路就是使用 递归
在递归的方式下可以计算这种情况
这里由于我们要知道左右节点的深度情况下，
才可以判断其左子树和右子树的绝对值之差
因此本题是和前面的最大深度具有着一定的关联的
那么按三部曲走，方式如下：
确定参数以及返回值
参数是 节点
返回值是整数类型
确定边界条件
如果为根节点就直接返回0
确定单层逻辑
进入左子树
进入右子树
这里的逻辑部分进行更改
如果出现大于的情况那么就直接返回-1
如果没有出现这样的情况那么就找出最大的后返回层数值
至于这里要求的布尔类型返回，可以单独调用返回
"""
from typing import *

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def isBalanceTree(root) -> int:
            # 如果节点为空
            if root is None:
                return 0
            # 左子树层次
            left_level = isBalanceTree(root.left)
            # 如果左子树已经是-1了
            if left_level == -1:
                return -1
            # 右子树层次
            right_level = isBalanceTree(root.right)
            # 如果右子树已经是-1了
            if right_level == -1:
                return -1
            # 中层逻辑
            # 如果绝对值大于1
            if abs(left_level - right_level) > 1:
                # 直接返回
                return -1
            # 如果不是大于1
            else:
                # 找到两者中最大的并+1返回
                return 1 + max(left_level, right_level)
        
        test_number = isBalanceTree(root)
        # 如果为-1返回false
        if test_number == -1:
            return False
        # 否则返回true
        else:
            return True
