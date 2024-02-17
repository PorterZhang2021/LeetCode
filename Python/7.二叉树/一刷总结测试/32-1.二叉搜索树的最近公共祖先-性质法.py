from typing import *
from BinaryTree import TreeNode
from BinaryTree import creatTree

# 确定本题的使用方法
# 递归+二叉搜索树性质
# 确定本题的边界条件

# 本题需要利用到二叉搜索树的性质
# 并且本题需要进行讨论
# 本题讨论方式如下
# 如果p和q都比现有的root小 那么需要往左边走 此时大的可能是公共祖先
# 如果p和q都比现有的root大 那么需要往右边走 此时小的可能是公共祖先
# 如果p和q分别分布在root的两边，那么root可能是两者的公共祖先

# 如果找到p或者找到q或者为空的时候返回节点


class Solution:
    # 确定参数与返回值
    # 参数为根节点 返回值为节点
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # 确定本题的边界条件
        if not root or p or q:
            return root
        
        # 确定单层逻辑循环
        left = self.lowestCommonAncestor(root.left, p, q)
        # 如果p或者q为现在的root
        if root is p or root is q:
            return root

        right = self.lowestCommonAncestor(root.right, p, q)

        
        pass

def main():
    pass

if __name__ == '__main__':
    main()