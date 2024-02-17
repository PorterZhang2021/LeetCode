from typing import *
from BinaryTree import TreeNode
from BinaryTree import creatTree

# 确定本题的使用方法
# 本题使用性质+递归

# 确定本题是否具有特殊的边界条件
# 如果本题为空节点
# 如果只有一个空节点的时候直接进行置换
# 如果本题只有一个节点
# 如果只有一个节点那么就同节点比较大小，左小，右大

class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # 边界条件
        if not root:
            node = TreeNode(val)
            root = node
            return root
        if root and not root.left and not root.right:
            node = TreeNode(val)
            if root.val > val:
                root.left = node
            else:
                root.right = node
            return root
        
        def insert_to_bst(root):
            # 如果节点为空返回
            if not root:
                return None
            
            # 如果val值小于root.val
            if root.val > val:
                insert_to_bst(root.left)
            # 如果val值大于root.val
            if root.val < val:
                insert_to_bst(root.right)
            # 如果节点的左边或者右边有空
            if not root.left:
                node = TreeNode(val)
                root.left = node
            if not root.right:
                node = TreeNode(val)
                root.right = node
            
        insert_to_bst(root)
        return root

def main():
    pass

if __name__ == '__main__':
    main()