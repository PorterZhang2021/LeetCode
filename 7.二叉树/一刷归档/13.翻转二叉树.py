from typing import *

"""
# 左节点不为空 右节点为空
if left is not None and right is None:
    pass
# 左节点为空 右节点不为空
if left is None and right is not None:
    pass
"""

# 本题首先是要解决翻转问题 每个节点的左右孩子进行交换
# 选择使用前序，中序还有后序，层序遍历
# 这里中序遍历会出现多次遍历

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # 确定参数与返回值 这里已经弄好了
        # 确定好边界的相关条件
        # 当节点为空的时候结束
        # 确定好单层的逻辑循环
        # 左节点与右节点进行交换
        if root is None:
            return root
        # 进行交换
        root.left, root.right = root.right, root.left
        # 进入左子树
        Solution.invertTree(self, root.left)
        # 进入右子树
        Solution.invertTree(self, root.right)
        # 返回根节点
        return root
        
