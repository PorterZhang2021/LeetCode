from typing import *
from BinaryTree import TreeNode
from BinaryTree import creatTree

# 确定本题的使用方法
# 本题使用递归法+二叉搜索树的性质
# 确定本题的边界条件
# 如果本题没有节点 那么返回root
# 如果本题只有一个节点 那么同样返回root

class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # 边界情况
        # 空节点 或 只有一个节点
        if (not root) or (root and not root.left and not root.right):
            return root
        # 本题可以利用二叉搜索树的性质
        # 确定参数与返回值
        # 本题的参数为节点 返回空

        result = 0
        def conver_bst(root):
            nonlocal result
            # 如果节点为空
            if not root:
                return None
            
            # 进入右子树
            conver_bst(root.right)
            # 中序遍历
            # 如果pre存在
            result = result + root.val
            root.val = result
            # 进入左子树
            conver_bst(root.left)
        conver_bst(root)
        return  root

def main():
    pass

if __name__ == '__main__':
    main()
