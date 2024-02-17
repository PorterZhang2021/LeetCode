from typing import *
from BinaryTree import TreeNode
from BinaryTree import creatTree

# 确定本题的使用方法
# 递归法
# 确定本题的边界条件-本题暂无边界条件



class Solution:
        # 确定参数与返回值
        # 参数为节点 返回值为节点
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # 确定边界条件
        # 当有空节点，或者p，或者q时返回节点
        if not root or root is p or root is q:
            return root
        
        # 确定单层逻辑
        # 由于本题要将结果返回上去，因此需要使用后序遍历
        # 本题返回结果所以左右返回具有节点
        left = self.lowestCommonAncestor(root, p, q)
        right = self.lowestCommonAncestor(root, p, q)
        
        # 如果左边与右边都有值的情况下
        if left and right:
            return root
        # 如果左边与右边只有一边有值 返回有值的一边
        if left and not right:
            return left
        elif not left and right:
            return right
        # 如果左边与右边都没有值
        else:
            return None
        

def main():
    pass

if __name__ == '__main__':
    main()