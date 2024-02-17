"""
404.左叶子之和
这个部分用来调试思考递归返回值思路的一个问题
因为我没能有效的理解这个思路的问题
"""

from typing import *
from NewTree import TreeNode
from NewTree import creatTree


class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        # 确定终止条件
        if not root:
            return 0
        if not root.left and not root.right:
            return 0
        
        # 单层逻辑
        # 左子树逻辑
        left_value = Solution.sumOfLeftLeaves(self, root.left)
        if root.left and not root.left.left and not root.left.right:
            left_value = root.left.val
        # 右子树逻辑
        right_value = Solution.sumOfLeftLeaves(self, root.right)
        # 中逻辑，这个部分是将左右获取的情况整合起来
        sum = left_value + right_value
        # 这边的返回是将其返回到上一层的节点，这里可以假设为上一层节点获取到的值
        return sum

def main():
    s = Solution()
    tree = creatTree([3,9,20,None,None,15,7])
    print(s.sumOfLeftLeaves(tree))


if __name__ == '__main__':
    main()
