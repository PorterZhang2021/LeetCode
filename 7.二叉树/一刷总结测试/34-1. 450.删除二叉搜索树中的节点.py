from typing import *
from BinaryTree import TreeNode
from BinaryTree import creatTree

# 确定本题的使用方法
# 确定本题的边界条件
# 如果本题只有一个节点，且key等于此节点 直接返回None

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root and not root.left and not root.right:
            if root.val == key:
                return None
        
        pre = None
        def delete_node(root):
            nonlocal pre
            # 如果节点为空
            if not root:
                return None
           # 如果节点满足条件
            if root.val == key:
                # 如果为叶子节点
                if not root.left and not root.right:
                    return None
                # 如果只有左节点没有右节点
                if root.left and not root.right:
                    root = root.left
                # 如果左右都有
                if root.left and root.right:
                    # 找到右边的节点
                    cur = root.right
                    # 往其左边不断遍历
                    while cur.left:
                        cur = cur.left
                    # 交换两者
                    aux_node = root
                    root = cur
                    cur = aux_node
                    cur = None
            
            delete_node(root.left)
            # 进入右子树
            delete_node(root.right)
        delete_node(root)
        return root

def main():
    pass

if __name__ == '__main__':
    main()