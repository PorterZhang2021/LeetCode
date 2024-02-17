from typing import *
from BinaryTree import TreeNode
from BinaryTree import creatTree

# 确定本题的使用方法
# 如果为空节点，那么创建一个节点作为root节点
# 如果只有一个节点，那么此时比较左右两边值的情况 左小右大

class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # 边界条件
        if not root:
            root = TreeNode(val)
            return root
        if root and not root.left and not root.right:
            node = TreeNode(val)
            if root.val > val:
                root.left = node
            else:
                root.right = node
        
        # 确定参数与返回值
        # 参数为根节点
        def insert_into_bst(root):
            # 边界条件
            # 如果找到根为空的节点，此时直接创建节点后返回
            if not root:
                node = TreeNode(val)
                return node
            
            if root.val > val:
                root.left = insert_into_bst(root.left)
            if root.val < val:
                root.right = insert_into_bst(root.right)
            return root
        insert_into_bst(root)
        return root

def main():
    pass

if __name__ == '__main__':
    main()
