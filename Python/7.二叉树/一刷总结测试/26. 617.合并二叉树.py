from typing import *
from BinaryTree import TreeNode
from BinaryTree import creatTree

# 确定本题的使用方法
# 本题使用迭代法

# 确定本题是否具有特殊的边界条件
# 如果一个结点为空，另一个结点也为空 那么就返回None
# 如果两个都只有一个结点 那么就返回两个结点之和
# 如果两个结点中一个有，一个没有那么就返回有的那一个

# 确定参数与返回值
# 确定本题的边界条件
# 如果两个结点都为空那么返回空
# 如果一个结点为空另一个结点不为空那么就返回不空的结点

# 确定本题的单层逻辑
# 单层情况下每层都需要将结点返回，因此采用后序遍历的方式
# 那么左部分就直接返回左边结点的情况
# 右部分就直接返回右边结点的情况
# 本身的情况下直接将两边的值累加后返回

class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        # 如果两个结点都为空
        if not root1 and not root2:
            return None
        # 如果只有一个结点为空
        if (root1 and not root1.left and not root1.right) and not root2:
            return root1
        if not root2 and (root1 and not root1.left and not root2.right):
            return root2
        
        # 整体递归
        def merge_tree(root1, root2):
            # 如果两个结点都为空
            if not root1 and not root2:
                return None
            # 如果一个结点为空另一个结点不为空
            if root1 and not root2:
                return root1
            if not root1 and root2:
                return root2
            
            # 进入左子树
            root1.left = merge_tree(root1.left, root2.left)
            # 进入右子树
            root1.right = merge_tree(root1.right, root2.right)
            # 本身情况
            root1.val = root1.val + root2.val
            # 返回结点值
            return root1
        
        # 输出树
        root = merge_tree(root1, root2)
        return root


def main():
    pass

if __name__ == '__main__':
    main()