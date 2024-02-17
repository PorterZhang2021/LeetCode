"""
701.二叉搜索树中的插入操作
给定二叉搜索树（BST）的根节点 root 和要插入树中的值 value ，
将值插入二叉搜索树。 返回插入后二叉搜索树的根节点。 
输入数据 保证 ，新值和原始二叉搜索树中的任意节点值都不同。

注意，可能存在多种有效的插入方式，
只要树在插入后仍保持为二叉搜索树即可。 你可以返回 任意有效的结果 。

这里进行前序的递归遍历即可，达到对应的地方将节点插入即可
利用验证二叉搜索树的方式进行构建
首先先构建好实现验证二叉搜索树的部分
1. 确定递归函数参数与返回值
    参数 根结点
    返回值  返回根结点
2. 确定终止条件
    如果结点为空，创建一个结点后返回此结点
3. 确定单层递归的逻辑
    如果根结点的值大于值

    如果根结点的值小于值
"""

from typing import *
from NewTree import TreeNode
from NewTree import creatTree

class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
       # 返回更新后的以当前root为根节点的新树
       # 方便用于更新上一层的父子节点关系链

        if not root:
           return TreeNode(val)
        
        # 单层递归逻辑
        if val < root.val:
            # 将val插入到当前root的左子树中合适的位置
            # 并更新当前root的左子树为包含目标val的新左子树
            root.left = self.insertIntoBST(root.left, val)

        if root.val < val:
           # 将val插入到当前root的右子树中合适的位置
           # 并更新当前root的右子树为包含目标vla的新右子树
           root.right = self.insertIntoBST(root.right, val)
        
        # 返回更新以后的以当前root为根节点的新树
        return root