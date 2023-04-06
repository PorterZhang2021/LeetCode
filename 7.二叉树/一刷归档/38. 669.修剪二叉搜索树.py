"""
669. 修剪二叉搜索树
给你二叉搜索树的根节点 root ，
同时给定最小边界low 和最大边界 high。
通过修剪二叉搜索树，使得所有节点的值在[low, high]中。
修剪树 不应该 改变保留在树中的元素的相对结构 
(即，如果没有被移除，原有的父代子代关系都应当保留)。 
可以证明，存在 唯一的答案 。

所以结果应当返回修剪好的二叉搜索树的新的根节点。注意，根节点可能会根据给定的边界发生改变。

1.确定参数与返回值
    参数 根节点
    返回值 节点
2. 确定边界条件
    如果边界条件为空返回空
3. 确定单层逻辑
    寻找符合区间的元素并返回
    左子树
    右子树
"""

from typing import *
from NewTree import TreeNode
from NewTree import creatTree

class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        # 如果节点为空则返回
        if not root:
            return root
        
        # 如果节点值小于边界，那么向右寻找
        if root.val < low:
            right = self.trimBST(root.right, low, high)
            return right
        # 如果节点值大于边界，那么向左寻找
        if root.val > high:
            left = self.trimBST(root.left, low, high)
            return left
        # 接入符合条件的左孩子
        root.left = self.trimBST(root.left, low, high)
        # 接入符合条件的右孩子
        root.right = self.trimBST(root.right, low, high)
        return root