from typing import *

class TreeNode:
    # 初始化
    def __init__(self, right, left, val):
        self.right = right
        self.left = left
        self.val = val

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        # 存放输出结果
        result = []
        # 栈
        stack = []
        # 放置栈元素 如果root不为空
        if root:
            stack.append(root)
        # 如果栈不为空
        while stack:
            # 输出栈中的元素
            node = stack.pop()
            # 如果栈元素不为空
            if node is not None:
                # 自己进栈
                stack.append(node)
                # 并且增加一个None标记
                stack.append(None)
                # 右边元素进栈
                if node.right:
                    stack.append(node.right)
                # 左边元素进栈
                if node.left:
                    stack.append(node.left)
            else:
                # 节点为空了，那么就需要出栈了
                node = stack.pop()
                # 输出元素
                result.append(node.val)
        return result