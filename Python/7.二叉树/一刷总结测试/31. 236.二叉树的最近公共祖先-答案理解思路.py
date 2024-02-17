from typing import *
from BinaryTree import TreeNode
from BinaryTree import creatTree

# 确定本题的使用方法
# 本题使用迭代法
# 确定本题是否具有特殊边界条件
# 如果没有节点的情况下返回None
# 如果只有一个节点的情况下返回自身

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # 确定边界情况
        if not root:
            return None
        if root and not root.left and not root.right:
            return root
        

        # 确定参数与返回值
        # 本题的参数为节点
        # 返回值为节点
        def get_common_ancestor(root, p, q):
            # 确定边界情况
            # 如果遇到p结点或者q结点或者空节点那么就开始返回
            if not root or root is p or root is q:
                return root
            
            # 确定本题的单层逻辑情况
            # 本题单层逻辑情况使用后序遍历将结果回溯上去
            # 此时我们需要注意判断的就是左右子树是否接到结点
            left = get_common_ancestor(root.left , p, q)
            right = get_common_ancestor(root.right, p, q)

            # 如果两边都接到了那么此时我们就可以返回现在的这个结点
            # 因为现在的这个结点可能就是父亲结点 32
            if left and right:
                return root
            # 如果左边有了右边没有那么此时返回左边的情况
            if left and not right:
                return left
            # 如果左边没有右边有了那么此时返回右边的情况
            elif not left and right:
                return right
            # 如果两边都没有那么说明没有父亲结点
            else:
                return None
        return get_common_ancestor(root, p, q)

def main():
    pass

if __name__ == '__main__':
    main()