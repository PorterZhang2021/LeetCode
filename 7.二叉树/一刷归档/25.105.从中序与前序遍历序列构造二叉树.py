"""
105. 从前序与中序遍历序列构造二叉树
给定两个整数数组 preorder 和 inorder ，
其中 preorder 是二叉树的先序遍历， 
inorder 是同一棵树的中序遍历，
请构造二叉树并返回其根节点。

1. 确定边界情况 这里是前序遍历数组为空 返回
2. 前序遍历数组的第一个值就是根节点
3. 找到中序遍历数组中对应的索引
4. 切割中序遍历数组分成左与右
5. 切割前序遍历数组分成左与右
6. 进行左右节点的递归
7. 返回根节点
"""

from typing import *
from NewTree import TreeNode
from NewTree import creatTree

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # 1. 确定边界情况 这里是前序遍历数组为空 返回
        if not preorder:
            return
        
        # 2. 前序遍历数组的第一个值就是根节点
        val = preorder[0]
        root = TreeNode(val)
        
        # 3. 找到中序遍历数组中对应的索引
        index = inorder.index(val)

        # 4. 切割中序遍历数组分成左与右
        left_inorder = inorder[:index]
        right_inorder = inorder[index+1:]
        # 5. 切割前序遍历数组分成左与右
        left_preorder = preorder[1:len(left_inorder)]
        right_preorder = preorder[len(right_inorder):]

        # 6. 进行左右节点的递归
        root.left = self.buildTree(left_preorder, left_inorder)
        root.right = self.buildTree(right_preorder, right_inorder)
        
        # 7. 返回根节点
        return root