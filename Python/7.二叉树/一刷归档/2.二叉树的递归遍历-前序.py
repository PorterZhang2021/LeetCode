# 二叉树的递归遍历
"""
递归算法的三要素:
1. 确定递归函数的参数和返回值：
    1. 递归函数内部需要调用处理的参数
    2. 递归函数的返回值类型
2. 确定终止条件：
    1. 解决栈溢出问题，那么需要确定栈终止条件
3. 确定单层递归的逻辑：
    1.将会重复调用的递归过程
tips:
1. 二叉树条件下，终止条件最好和参数一致
"""

# 确定递归函数的参数和返回值
# 返回值是节点
# 参数节点

# 确定终止条件
# 终止条件是节点为NULL 此时开始回去

# 确定单层递归的逻辑
# 获取值-左节点-右节点

from typing import *

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # 保存结果
        result = []
        
        def traversal(root: TreeNode):
            # 终止条件
            if root is None:
                return
            
            # 放入值
            result.append(root.val)
            # 左节点
            traversal(root.left)
            # 右节点
            traversal(root.right)
        
        traversal(root)
        return result
            

def main():
    pass

if __name__ == '__main__':
    main()
