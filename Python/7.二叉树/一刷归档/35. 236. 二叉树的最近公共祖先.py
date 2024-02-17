"""
236.二叉树的最近公共祖先
给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。

百度百科中最近公共祖先的定义为：
“对于有根树 T 的两个节点 p、q，
最近公共祖先表示为一个节点 x，
满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”

递归三部曲：
1. 确定参数与返回值
    参数 节点
    返回值 返回节点
2. 确定边界条件
    边界条件 如果为根节点返回空
3. 确定单层逻辑循环
    这里使用后序遍历即左右中，将每次节点的数据向上返回
    递归进入左子树
    递归进入右子树
    遍历二叉搜索树即寻找[p.val, q.val]
    如果cur.val>p.val and cur.val>q.val 向左遍历
    如果cur.val<p.val and cur.val<q.val 向右遍历
"""

from typing import *
from NewTree import TreeNode
from NewTree import creatTree

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # 如果根节点为空
        if not root:
            return None

        # 向左搜索
        if root.val > p.val and root.val > q.val:
            # 进行左递归
            left = self.lowestCommonAncestor(root.left, p, q)
            # 如果不为空
            if left:
                return left
        # 向右搜索
        if root.val < p.val and root.val < q.val:
            # 进行右递归
            right = self.lowestCommonAncestor(root.right, p, q)
            # 如果不为空
            if right:
                return right
        
        # 返回根节点
        return root