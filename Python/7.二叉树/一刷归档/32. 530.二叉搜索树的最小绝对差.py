"""
530. 二叉搜索树的最小绝对差
给你一个二叉搜索树的根节点 root ，
返回 树中任意两不同节点值之间的最小差值 。
差值是一个正数，其数值等于两值之差的绝对值。

不同结点之间的最小差值
最小差值满足的条件肯定是一个升序的数组
升序的数组中最小的两个值是不是就是最小差值

由于本题有一个提示，那就是二叉搜索树，
那么按照二叉搜索树的定义来看，其实最
靠近的两个结点是容易产生最小绝对差值的
因此我们只需要在验证二叉搜索树的基础上进行改造就可以

1. 确定参数与返回值
    参数 结点
    返回值 整数
2. 确定边界返回条件
    如果为空就返回
3. 确定单层逻辑循环
    进入左子树
    如果前一个结点存在 那么就 计算现在的结点和它的
    绝对差值
    进入右子树
"""

from typing import *
from NewTree import creatTree
from NewTree import TreeNode

class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        pre = None
        min_val = -1
        def get_min_difference(root: TreeNode):
            nonlocal pre
            nonlocal min_val
            
            if not root:
                return
            get_min_difference(root.left)        
            if pre:
                aux_val = abs(pre.val - root.val)
                if min_val == -1 or aux_val < min_val:
                    min_val = aux_val
            pre = root
            get_min_difference(root.right)