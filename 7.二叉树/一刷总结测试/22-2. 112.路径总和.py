from typing import *
from BinaryTree import TreeNode
from BinaryTree import creatTree

# 确定本题的使用方法
# 本题使用递归法
# 确定本题的边界条件
# 结点为空时返回False

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        if root and not root.left and root.right:
            if root.val == targetSum:
                return True
        def is_has_path(root, count):
            # 如果为叶子结点且计数值为0 返回True
            if root and not root.left and not root.right and count == 0:
                return True
            # 如果为叶子结点但是值不等
            if root and not root.left and not root.right:
                return False

            # 左结点
            if root.left:
                count -= root.left.val
                if is_has_path(root.left, count):
                    return True
                count += root.left.val
            # 右结点
            if root.right:
                count -= root.right.val
                if is_has_path(root.right, count):
                    return True
                count += root.right.val
            return False
        # 为什么起始计算要减去？
        return is_has_path(root, targetSum-root.val)

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