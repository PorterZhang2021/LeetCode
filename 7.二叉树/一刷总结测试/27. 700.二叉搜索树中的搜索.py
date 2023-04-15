from typing import *
from BinaryTree import TreeNode
from BinaryTree import creatTree

# 确定本题的使用方法
# 递归法
# 确定本题是否具有特殊条件
# 如果结点为空的情况下直接返回None
# 如果只有一个结点且val相同返回root 否则返回None


class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # 边界条件
        # 如果结点为空的情况下直接返回None
        if not root:
            return None
        # 如果只有一个结点且val相同那么返回root否则返回None
        if (root and not root.left and not root.right) and root.val == val:
            return root
        elif (root and not root.left and not root.right) and root.val != val:
            return None
        # 确定参数与返回值
        # 参数为根结点，返回值也为结点
        result = None
        def search_bst(root):
            nonlocal result
            # 确定边界条件
            # 如果为空结点则代表没有找到
            if not root:
                return None
            
            # 确定单层逻辑
            # 因为每次寻找后要返回找到之后的结点情况
            # 这里通过遍历进行判断
            # 如果比现在的结点值小 那么就去左边
            if root.val > val:
                search_bst(root.left)
            # 如果比现在的结点值大，那么就去右边
            if root.val < val:
                search_bst(root.right)
            if root.val == val:
                result = root
        search_bst(root)
        return result
        
        

def main():
    pass

if __name__ == '__main__':
    main()