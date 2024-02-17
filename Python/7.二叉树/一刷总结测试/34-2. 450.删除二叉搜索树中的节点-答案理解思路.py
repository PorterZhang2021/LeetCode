from typing import *
from BinaryTree import TreeNode
from BinaryTree import creatTree

# 确定本题的使用方法
# 递归法
# 确定本题是否具有特殊条件
# 如果只有一个节点且节点的值为key 那么直接返回None

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        if root and not root.left and not root.right:
            if root.val == key:
                return None
            else:
                return root

        # 确认参数与返回值
        # 参数为节点 返回值为空
        def delete_node(root):
            # 确认边界条件
            # 如果节点为空 那么返回None
            if not root:
                return None
            
            # 确认单层逻辑
            # 本题的单层逻辑同节点的方式有关
            # 如果val值小于root.val:
            if root.val > key:
                # 此时往左边走
                root.left = delete_node(root.left)
            elif root.val < key:
                # 此时往右边
                root.right = delete_node(root.right)
            else:
                # 此时分情况讨论满足的key
                # 如果此时节点为叶子节点
                if not root.left:
                    return root.right
                # 此时只有左边叶子
                if not root.right:
                    return root.left
                # 此时两边都有节点
                # 左叶子用于遍历
                cur = root.right
                while cur.left:
                    cur = cur.left
                # 将当前节点的左孩子挂到现在遍历的节点上
                cur.left = root.left
                # 利用右子树节点替换掉当前节点
                root = root.right
            return root
        # 此方式下由于会有返回值，如果要保证root的更改
        # 那么要对root重新赋值
        root = delete_node(root)
        return root
    
def main():
    sl = Solution()
    # case 1
    root = [5,3,6,2,4,None,7]
    key = 5
    tree = creatTree(root)
    print(sl.deleteNode(tree, key))
if __name__ == '__main__':
    main()


