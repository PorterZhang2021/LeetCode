"""
106. Construct Binary Tree from Inorder and Postorder Traversal
给定两个整数数组 inorder 和 postorder ，
其中 inorder 是二叉树的中序遍历， 
postorder 是同一棵树的后序遍历，
请你构造并返回这颗 二叉树 。

中 + 前，后，层 可以 唯一确定一棵二叉树

中序 + 后序
中序 左中右
后序 左右中

1. 提取中序的最后一个值作为根节点
2. 通过根节点划分中序数组，将其分为两个部分

1. 如果数组大小为零的话，说明是空节点。
2. 如果不为空，那么取后序数组最后一个元素作为节点元素。
3. 找到后序数组最后一个元素在中序数组的位置，作为切割点
4. 切割中序数组，切成中序左数组，中序右数组
5. 切割后序数组，切成后序左数组和后序有右数组
6. 递归处理左区间和右区间
"""

from typing import *
from NewTree import TreeNode
from NewTree import creatTree

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        # 1: 如果为空，递归终止
        if not postorder:
            return
        
        # 2：后序遍历的最后一个就是当前的中间节点
        val = postorder[-1]
        # 根节点
        root = TreeNode(val)

        # 3：找到中间切割点
        index = inorder.index(val)

        # 4：切割inorder数组，得到inorder数组的左，右半边
        left_inorder = inorder[:index]
        right_inorder = inorder[index+1:]

        # 5：切割postorder数组，得到postorder数组的左，右半边
        # 中序数组大小一定同后序数组大小相同
        left_postorder = postorder[:len(left_inorder)]
        right_postorder = postorder[len(left_inorder):len(postorder)-1]

        # 6：进行递归
        root.left = self.buildTree(left_inorder, left_postorder)
        root.right = self.buildTree(right_inorder, right_postorder)

        # 7：返回最终答案
        return root