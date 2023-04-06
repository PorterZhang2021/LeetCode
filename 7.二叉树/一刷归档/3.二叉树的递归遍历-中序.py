
# 确定参数与返回值
# 返回值 树节点
# 参数 树节点

# 确定终止条件
# 节点不为空

# 确定单层逻辑
# 进入左节点
# 获取值
# 进入右节点

from typing import *

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def traversal(root: TreeNode):
            # 终止条件 对象常用is少用==
            if root is None:
                return
            
            # 进入左节点
            traversal(root.left)
            # 获取中间值
            result.append(root.val)
            # 进入右节点
            traversal(root.right)

        traversal(root)
        return result

def main():
    pass

if __name__ == '__main__':
    main()
