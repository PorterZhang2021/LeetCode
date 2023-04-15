from typing import *
from BinaryTree import TreeNode
from BinaryTree import creatTree

# 确定本题的使用方法
# 递归法
# 确定本题是否具有特殊边界
# 如果本题结点为空那么返回False
# 如果本题只有一个结点 那么返回True

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # 边界条件
        # 如果为空结点
        if not root:
            return False
        # 如果只有一个结点
        if root and not root.left and not root.right:
            return True
        
        # 构建一个找有效二叉树的内容
        # 确定参数与返回值
        # 本题的参数为结点 返回值为布尔值
        pre = None
        def is_valid_bst(root):
            nonlocal pre
            # 确定本题的边界条件
            # 如果结点为空那么结束
            if not root:
                return True
            
            # 确定单层逻辑
            # 本题使用中序遍历
            # 因为在中序遍历的情况下
            # 二叉搜索树为有序树 
            # 如果其值出现前一个值比后一个值大
            # 那么这个时候就要返回false
            # 这里对左右要分开取值，然后对其进行求和操作
            left_result = is_valid_bst(root.left)
            if pre and pre.val >= root.val:
                return False
            pre = root
            right_result = is_valid_bst(root.right)
            result = left_result and right_result
            return result
        result = is_valid_bst(root)
        return result

def main():
    sl = Solution()
    # case 1
    root = [2, 1, 3]
    tree = creatTree(root)
    print(sl.isValidBST(tree))
    # case 2
    root = [5,1,4,None,None,3,6]
    tree = creatTree(root)
    print(sl.isValidBST(tree))
    root = [5,4,6,None,None,3,7]
    tree = creatTree(root)
    print(sl.isValidBST(tree))

if __name__ == '__main__':
    main()
