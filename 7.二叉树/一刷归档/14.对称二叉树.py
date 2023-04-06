from typing import *

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # 如节点为空返回True
        if not root:
            # 返回空
            return True
        
        # 进行比对
        def compare(self, left, right):
            # 首先排除空节点的情况
            if left is None and right is None:
                return False
            elif left is not None and right is None:
                return False
            elif left is None and right is None:
                return True
            # 排除空节点，再排除数值不相同的情况
            elif left.val != right.val:
                return False
            
            # 此时就是：左右节点都不为空，且数值相同的情况
            # 此时才做递归，并做下一层的判断
            # 左子树 左 右子树 右
            outside = self.compare(left.left, right.right)
            # 左子树 右 右子树 左
            inside = self.compare(left.right, right.left)
            # 进行逻辑的判断处理
            # 左子树：中 、 右子树：中
            isSame = outside and inside
            # 返回计算结果
            return isSame