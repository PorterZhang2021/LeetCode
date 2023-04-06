"""
617.合并二叉树
本题合并二叉树并不是利用层序遍历来解题
层序遍历解题无法对叶子结点进行正确的判断
因此要完成这个问题，依然是递归思路
1. 确认递归的参数和返回值
    参数就是两个树
    返回值为返回的结点
2. 确定边界条件
    如果树1为空那么就返回树2的结点
    如果树2为空那么就返回树1的结点
3. 确定单层逻辑遍历
    左右子树递归获取到结点即可
    中逻辑 将 r1与r2的值相加后 返回r1结点
"""

from typing import *
from NewTree import TreeNode

class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        # 边界条件
        # 如果root1不存在就返回root2的结点
        if not root1:
            return root2
        # 如果root2不存在就返回root1的结点
        if not root2:
            return root1
        
        # 对中间逻辑进行处理
        root1.val += root2.val
        # 进行左右子树的遍历
        # 左子树结点递归
        root1.left = self.mergeTrees(root1.left, root2.left)
        # 右子树结点递归
        root1.right = self.mergeTrees(root1.right, root2.right)
        # 返回根结点
        return root1
