"""
中序遍历-迭代法
1.一路向左遍历存放左边的节点
2.取出栈中的节点
    1. 输出节点的值
    2. 查看是否有右端节点
    3. 如果有-查看是否有左节点，如果有左节点，一路向左遍历
    4. 如果没有-输出值

1. 对于对象的操作要想到使用not is等

此题错误
"""

from typing import *

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # 存放结果
        result = []
        # 模拟栈
        stack_list = [root]
        
        def is_left_None(root):
            # 进行一串到底
            while not root.left:
                # 将root的左孩子放入
                root = root.left
                # 存放进堆中
                stack_list.append(root)
        
        # 先进行一次一串到底
        is_left_None(root)

        # 栈不为空
        while not stack_list:
            # 取出栈元素
            node = stack_list.pop()
            # 存放栈元素的值
            result.append(node.val)
            # 判断其右边的值 如果存在右节点
            if node.right:
                # 如果右节点有左孩子
                if node.right.left:
                    is_left_None(node.right.left)
                # 如果右节点没有左孩子
                else:
                    # 存放此节点的值
                    result.append(node.right.val)

        # 返回结果值
        return result
