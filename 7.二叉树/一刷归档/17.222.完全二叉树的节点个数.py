"""
222. 完全二叉树的节点个数
给你一棵 完全二叉树 的根节点 root ，
求出该树的节点个数。
完全二叉树 的定义如下：
在完全二叉树中，除了最底层节点可能没填满外，
其余每层节点数都达到最大值，
并且最下面一层的节点都集中在该层最左边的若干位置。
若最底层为第 h 层，则该层包含 1~ 2h 个节点。

此题其实最简单的就是性质法：
也就是说完全二叉树本身的一个性质问题 
- 这个直接套公式就可以完成了 此部分可以没事的时候写一个推导文
理解一下思路

层序遍历 - 利用层序遍历可以轻松解决，每次出栈的时候就计数就行了
最主要的是要知道层序遍历的模板与写法

递归 - 这种应该是最不容易想到的
"""

from typing import *

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        # 如果我们单独就用一个栈实现的话，并不涉及分层问题
        # 那么层序遍历只需要先进右节点然后进左节点
        # 节点数量 
        node_number = 0
        # 如果root为空直接返回
        if root is None:
            return node_number
        # 栈 先放入第一个元素
        stack = [root]
        # 如果栈不空
        while stack:
            # 元素出栈
            node = stack.pop()
            # 记录节点的数量 自增1
            node_number += 1
            # 如果右子树有节点
            if node.right is not None:
                # 右子树有节点
                stack.append(node.right)
            # 如果左子树有节点
            if node.left is not None:
                # 左子树有节点
                stack.append(node.left)
        # 返回节点数量
        return node_number

def main():
    s = Solution()
    root = [1, 2, 3, 4, 5, 6]
    number = s.countNodes(root)
    print(number)


if __name__ == '__main__':
    main()