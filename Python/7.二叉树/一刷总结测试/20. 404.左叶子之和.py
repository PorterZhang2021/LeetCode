from typing import *
from BinaryTree import TreeNode
from BinaryTree import creatTree

# 确定本题使用方法
# 本题使用方法为递归法
# 确定本题的边界条件
# 本题的边界条件有两个
# 一个是空结点直接返回0
# 一个是一个结点此时直接返回0
# 递归法
# 确定参数与返回值
# 参数为结点
# 返回值为整数
# 确定边界条件
# 如果结点为空 返回
# 确定单层逻辑
# 递归进入左结点
# 递归进入右结点
# 如果结点有左节点且左节点为叶子结点
# 那么就将值放入

class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        # 如果结点为空结点
        if not root:
            return 0
        # 如果只有一个结点
        if root and not root.left and not root.right:
            return 0
        # 结果集
        result = 0
        def sumOfLeft(root):
            nonlocal result

            if not root:
                return
            
            if root.left and not root.left.left and not root.left.right:
                # 如果为左叶子结点
                result += root.left.val
            # 进入左子树
            sumOfLeft(root.left)
            # 进入右子树
            sumOfLeft(root.right)
        sumOfLeft(root)
        return result
            



def main():
    sl = Solution()
    # case 1
    root = [3,9,20,None,None,15,7] 
    tree = creatTree(root)
    print(sl.sumOfLeftLeaves(tree))
    # case 2
    root = [1]
    tree = creatTree(root)
    print(sl.sumOfLeftLeaves(tree))


if __name__ == '__main__':
    main()
