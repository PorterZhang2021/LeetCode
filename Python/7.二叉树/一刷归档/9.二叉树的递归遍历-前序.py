from typing import *

class TreeNode:
    # 初始化
    def __init__(self, right, left, val):
        self.right = right
        self.left = left
        self.val = val

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        # 这个方式是对迭代法的中序遍历进行了更改
        # 通过其方式便可以得到我们需要的结果
        # 输出结果
        result = []
        # 栈
        stack = []
        if root:
            # 将节点加入栈中
            stack.append(root)
        # 如果栈不为空
        while stack:
            # 将栈的节点输出
            node = stack.pop()
            # 如果节点不为空
            if node != None:
                # 如果右节点不空
                if node.right:
                    # 将栈右节点入栈
                    stack.append(node.right)
                # 如果左节点不空
                if node.left:
                    # 将栈左节点入栈
                    stack.append(node.left)
                # 栈内加入元素
                stack.append(node)
                # 栈内加入空指针
                stack.append(None)
            else:
                # 输出栈的元素
                node = stack.pop()
                # 输出栈的值
                result.append(node.val)
        # 返回输出结果
        return result