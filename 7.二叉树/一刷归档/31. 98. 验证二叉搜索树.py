"""
98.验证二叉搜索树
给你一个二叉树的根节点 root ，
判断其是否是一个有效的二叉搜索树。

有效 二叉搜索树定义如下：
节点的左子树只包含 小于 当前节点的数。
节点的右子树只包含 大于 当前节点的数。
所有左子树和右子树自身必须也是二叉搜索树。

1. 确定参数以及返回值
    参数为 结点
    返回值 为 布尔类型
2. 确定边界条件
    边界条件 如果为空那么就返回true
3. 确定单层逻辑
    进入左子树
    如果前一个结点非空 并且 前一个结点的值大于等于现在结点的值 返回False
    前一个结点 赋值为 现在的结点
    进入右子树

"""

from typing import *
from NewTree import TreeNode
from NewTree import creatTree

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        pre = None
        def __isValiBST(root: TreeNode) -> bool:
            nonlocal pre
            # 如果为空结点
            if not root:
                # 返回True
                return True

            # 进入左子树
            left_bool = __isValiBST(root.left)        
            # 如果前一个结点存在且其大于等于现在的结点 返回false
            if pre and pre.val >= root.val: return False
            pre = root
            # 进入右子树
            rigth_bool = __isValiBST(root.right)
            return left_bool and rigth_bool
        return __isValiBST(root)

