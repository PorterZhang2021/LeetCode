from typing import *
from BinaryTree import TreeNode
from BinaryTree import creatTree

# 确定本题的使用方法
# 确定本题是否有特殊的边界条件
# 如果结点为空的情况下，那么直接返回false
# 如果只有一个结点的情况下
# 比较一下目标值和路径值的情况 如果相等返回True 否则返回False
# 

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root and not root.left and not root.right:
            targetSum -= root.val
            if targetSum == 0:
                return True
            else:
                return False
        
        targetSum -= root.val
        if root.left:
            # 此步骤下会出现未定义的问题，因此这种情况下
            # 我们需要直接在内部使用if进行处理
            left = self.hasPathSum(root.left, targetSum)
            targetSum += root.val
        if root.right:
            right = self.hasPathSum(root.right, targetSum)
            targetSum += root.val
        result = left or right
        return result

def main():
    sl = Solution()
    # case 1
    root = [5,4,8,11,None,13,4,7,2,None,None,None,1]
    tree = creatTree(root)
    targetSum = 22
    print(sl.hasPathSum(tree, targetSum))
    # case 2
    root = [1,2,3]
    tree = creatTree(root)
    targetSum = 5
    print(sl.hasPathSum(tree, targetSum))

if __name__ == '__main__':
    main()
