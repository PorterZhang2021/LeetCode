"""
538.把二叉搜索树转换为累加树
给出二叉 搜索 树的根节点，该树的节点值各不相同，
请你将其转换为累加树（Greater Sum Tree），
使每个节点 node 的新值等于原树中大于或等于 node.val 的值之和。

提醒一下，二叉搜索树满足下列约束条件：

节点的左子树仅包含键 小于 节点键的节点。
节点的右子树仅包含键 大于 节点键的节点。
左右子树也必须是二叉搜索树。

本题示例的结果为逆中序遍历
1. 确定参数与返回值
    参数 节点
    返回值 节点
2. 确定边界条件
    如果为到达根节点就返回节点
3. 确定单层逻辑
    如果有前一个结点那么就将前一个结点+现在结点的值组合存入
    返回现在的结点
    左递归
    右递归
"""

from typing import *
from NewTree import TreeNode
from NewTree import creatTree

class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        pre = None

        def createBST(root):
            nonlocal pre

            if not root:
                return root
            
            createBST(root.right)
            
            
            if pre:
                root.val = root.val + pre.val
            else:
                root.val = root.val
            pre = root

            createBST(root.left)
            
            return root
        
        return createBST(root)

        