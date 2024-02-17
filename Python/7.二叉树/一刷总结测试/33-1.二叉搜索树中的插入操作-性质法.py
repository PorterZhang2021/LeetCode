from typing import *
from BinaryTree import TreeNode
from BinaryTree import creatTree

# 确定本题的使用方法
# 本题使用递归法
# 确定本题的边界条件
# 本题的边界条件为
# 如果为空节点需要进行插入，那么此时将空节点置换即可
# 如果只有一个节点，那么比较节点大小做好插入

class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # 边界条件
        if not root:
            root = TreeNode(val)
            return root
        if root and not root.left and not root.right:
            # 如果val大于root.val 插入右边
            if val > root.val:
                node = TreeNode(val)
                root.right = node
            else:
                node = TreeNode(val)
                root.left = node
            return root
        
        # 确定参数与返回值
        # 参数为节点，返回值为节点
        pre = None
        def insert_to_bst(root):
            nonlocal pre
            # 确定边界条件
            # 如果节点为空
            if not root:
                # 如果这时候val > pre.val 那么放入右边, 且pre存在
                if pre and pre.val < val:
                    node = TreeNode(val)
                    pre.right = node
                return None
            
            # 确定单层逻辑循环
            # 本部分使用中层遍历
            # 中层遍历会进行升序输出
            # 此时可以验证后找到存放位置
            # 左遍历
            insert_to_bst(root.left)
            # 此时如果pre不存在，那么就先验证这个值是不是比现在的root小
            if not pre:
                # 如果val这个值小于root.val,那么就加入左节点
                if val < root.val:
                    node = TreeNode(val)
                    root.left = node
            # 如果pre存在了,并且val大于pre.val且小于root.val
            elif pre and pre.val < val < root.val:
                node = TreeNode(val)
                # 此时判断左边与右边哪个为空
                if not pre.right:
                    pre.right = node
                else:
                    root.left = node
            # 如果pre有值但是root没有值且val比pre大
            elif not root and pre.val < val:
                node = TreeNode(val)
                pre.right = node
            pre = root
            # 右遍历
            insert_to_bst(root.right)
        insert_to_bst(root)
        return root
            


def main():
    pass

if __name__ == '__main__':
    main()
