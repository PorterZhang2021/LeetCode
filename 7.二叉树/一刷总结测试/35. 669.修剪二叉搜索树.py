from typing import *
from BinaryTree import TreeNode
from BinaryTree import creatTree

# 确定本题的使用方法
# 递归法
# 确定本题是否具有特殊条件
# 暂无

class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        # 确定参数与返回值
        # 参数为节点 返回值为None
        if not root:
            return None
        
        # 确定单层循环逻辑
        # 如果节点的值比low小
        # 此时应该递归右子树找到满足条件的值
        if root.val < low:
            right = self.trimBST(root.right, low, high)
            return right
        # 如果节点的值比high大
        # 此时应该递归左子树找到满足条件的值
        if root.val > high:
            left = self.trimBST(root.left, low, high)
            return left
        # 进入左子树
        root.left = self.trimBST(root.left, low, high)
        # 进入右子树
        root.right = self.trimBST(root.right, low, high)
        return root


def main():
    pass

if __name__ == '__main__':
    main()