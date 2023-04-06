"""
450.删除二叉搜索树中的节点
给定一个二叉搜索树的根节点 root 和一个值 key，
删除二叉搜索树中的 key 对应的节点，
并保证二叉搜索树的性质不变。
返回二叉搜索树（有可能被更新）的根节点的引用。
一般来说，删除节点可分为两个步骤：
首先找到需要删除的节点；
如果找到了，删除它。

1. 确定参数与返回值
    参数 节点
    返回值 节点
2. 确定边界条件
    如果节点为空则返回
3. 确定单层逻辑
    删除的情况：
    1. 没找到删除的节点，遍历到空节点直接返回
    2. 找到删除的节点
        1. 左右孩子都为空即叶子节点，直接删除节点，返回None
        2. 左孩子为空，右孩子不空，删除节点，右孩子补位，返回右孩子为根节点
        3. 右孩子为空，左孩子不为空，删除节点，左孩子补位，返回左孩子为根节点
        4. 左右孩子节点都不为空，删除节点的左孩子放到删除节点的右子树的最
           左边节点的左孩子上，返回删除节点右孩子为新的根节点。
"""

from typing import *
from NewTree import TreeNode
from NewTree import creatTree


class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # 如果根节点为空
        if not root:
            return root
        
        if root.val < key:
            root.right = self.deleteNode(root.right, key)
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            # 当前节点的左子树为空，返回当前的右子树
            if not root.left:
                return root.right
            # 当前节点的右子树为空，返回当前的左子树
            if not root.right:
                return root.left
            # 左右子树都不为空，找到右孩子的最左节点记为p
            node = root.right
            while node.left:
                node = node.left
            # 将当前节点的左子树挂在p的左孩子上
            node.left = root.left
            # 当前节点的右子树替换掉当前节点，完成当前节点的删除
            root = root.right
        return root
        