"""
二叉树的前序遍历-栈实现
模拟题
循环终止条件，栈内出栈的元素左右节点为空
右节点不为空 将右节点的值加入栈中
左节点不为空 将左节点的值加入栈中
将顶点元素出栈
"""

from typing import *

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        

        # 利用列表做一个栈
        stack_list = [root]
        # 结果
        result = []
        # 如果root为None直接返回
        if not root:
            return result

        # 栈为空则结束
        while stack_list:
            # 将栈顶指针的值取出
            node = stack_list.pop()
            # 存入节点中的值
            result.append(node.val)
            # 判断节点有没有右孩子
            if node.right is not None:
                # 存入节点右孩子
                stack_list.append(node.right)
            # 判断节点有没有左孩子
            if node.left is not None:
                # 存入节点左孩子
                stack_list.append(node.left)
        
        # 返回结果
        return result


