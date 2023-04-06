"""
98.验证二叉搜索树
给你一个二叉树的根节点 root ，
判断其是否是一个有效的二叉搜索树。

有效 二叉搜索树定义如下：
节点的左子树只包含 小于 当前节点的数。
节点的右子树只包含 大于 当前节点的数。
所有左子树和右子树自身必须也是二叉搜索树。

1. 确定参数与返回值
    参数 root 
    返回值 ture或者false
2. 确定边界条件
    如果其结果能够到最底部那么就返回true
3. 确定单层逻辑
    构建一个参数用于保存每次递归返回后的结果
    如果现有结点的左结点大于现有结点 那么就返回false
    如果现有结点的右结点小于现有结点 那么就返回false
    左子树进行递归
    右子树进行递归
    返回最终结果

本思考过程只解决了左右中的遍历方式问题，遍历方式选择错误
本质上来说：我不知道如何构建一个前序遍历的方式并带有参数
或者来说我对递归的理解并不到位。
"""

from typing import *
from NewTree import TreeNode
from NewTree import creatTree

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # 确定参数与返回值
        if not root:
            return True
        
        # 确定边界条件
        bool_left = self.isValidBST(root.left)
        if root.left and root.left.val >= root.val:
            return False
        if root.right and root.right.val <= root.val:
            return False
        # 确定单层逻辑
        bool_right = self.isValidBST(root.right)
        result = bool_left and bool_right
        return result


def main():
    s = Solution()
    root = [5,1,4,None,None,3,6]
    tree = creatTree(root)
    print(s.isValidBST(tree))


if __name__ == '__main__':
    main()