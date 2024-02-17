from typing import *
from BinaryTree import TreeNode
from BinaryTree import creatTree

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # 确认参数与返回值
        # 参数为根节点 返回值为None

        # 确认边界条件 如果节点为空直接返回
        if not root:
            return None
        
        # 二叉树递归的几个问题
        # 采用哪一种递归遍历方式
        # 什么情况下对递归部分的函数需要单独赋值

        # 确定单层逻辑
        # 进行左子树递归
        self.invertTree(root.right)
        # 进行右子树递归
        self.invertTree(root.left)
        # 如果碰到需要使用的节点
        # 不直接返回节点
        # 将节点的左右子节点调换
        # 临时存放左节点
        aux_node = root.left
        # 右节点放置到左边
        root.left = root.right
        # 左节点放置到右边
        root.right = aux_node
        return root
