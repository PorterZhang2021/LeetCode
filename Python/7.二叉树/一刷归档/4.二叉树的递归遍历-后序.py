# 二叉树的后序遍历

# 确定参数与返回值
# 参数：root
# 返回值：root

# 确认终止条件
# root不能为空

# 确定单层逻辑
# 遍历左节点
# 遍历右节点
# 将节点值输出

from typing import *

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # 存放值
        result = []
        
        def traversal(root: TreeNode):
            # root节点不能为空
            if root is None:
                return
            
            # 遍历左节点
            traversal(root.left)
            # 遍历右节点
            traversal(root.right)
            # 输出值
            result.append(root.val)
        
        # 运行
        traversal(root)
        # 返回值
        return result

def main():
    pass


if __name__ == '__main__':
    main()


