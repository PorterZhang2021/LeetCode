"""
700.二叉搜索树中的搜索
给定二叉搜索树（BST）的根节点 root 和一个整数值 val。

你需要在 BST 中找到节点值等于 val 的节点。 
返回以该节点为根的子树。 如果节点不存在，则返回 null 。

本题只需要找到我们需要的值就可以将根结点返回了
按照递归三部曲：
1. 确认递归参数与返回值
    参数 根结点
    返回值 返回根节点 或者 None
2. 确认边界条件
    边界条件就是如果结点为空就返回None或者找到对应的值就返回root
3. 确定单层逻辑循环
    这里可以有序搜索减少时间的消耗效率
    如果要搜的值小，搜左边
    如果搜的值大，搜右边
    没搜索到就返回None
"""
from typing import *
from NewTree import TreeNode

class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # 边界条件
        if not root or root.val == val:
            return root
        # 构建一个结点 用于保存搜索到的情况
        result = None
        # 如果现在的结点值大了搜索右边
        if root.val > val:
            result = self.searchBST(root.left, val)
        # 如果现在的结点值小了搜索左边
        if root.val < val:
            result = self.searchBST(root.right, val)
        # 返回搜索到的结点情况
        return result