"""
后序遍历-迭代法
先序遍历-中左右 调整一下变成 中右左
调整结束逆序形成 左右中
"""
from typing import *

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # 如果为空直接返回
        if not root:
            return []
        
        # 构建一个栈
        stack_list = [root]
        # 结果数组
        result = []

        # 栈不为空
        while stack_list:
            # 取出栈中的栈顶元素
            node = stack_list.pop()
            # 将值存入输出栈中
            result.append(node.val)
            # 如果左边有值，存放左边值
            if node.left:
                stack_list.append(node.left)
            # 如果右边有值，存放右边值
            if node.right:
                stack_list.append(node.right)
        
        # 将输出的值逆转
        result = result[::-1]
        # 最后的结果
        return result
