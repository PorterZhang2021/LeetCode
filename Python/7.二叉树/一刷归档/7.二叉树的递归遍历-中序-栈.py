from typing import *

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # 如果为空
        if not root:
            return []
        
        # 栈 不能提前将root结点加入stack中
        stack = []
        # 结果
        result = []
        # 当前结点
        cur = root        
        while cur or stack:
            # 先迭代访问最底层的左子树
            if cur:
                # 在栈中加入结点
                stack.append(cur)
                # 栈的左结点
                cur = cur.left
            # 到达最左结点后处理栈顶结点
            else:
                # 输出结点
                cur = stack.pop()
                # 将输出的结点值存入
                result.append(cur.val)
                # 取栈顶元素右结点
                # 这里如果没有右结点就输出，如果有右节点会重新存入栈中
                cur = cur.right
        
        return result