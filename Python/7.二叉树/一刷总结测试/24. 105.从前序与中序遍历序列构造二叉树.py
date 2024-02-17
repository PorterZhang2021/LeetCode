from typing import *
from BinaryTree import creatTree
from BinaryTree import TreeNode

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # 确定边界条件
        # 如果前序或者中序为空那么就直接返回None
        if len(preorder) == 0 and len(inorder) == 0:
            return None
        
        # 构建一个结点
        # 获取值
        value = preorder[0]
        root = TreeNode(value)
        
        # 获取索引
        index = inorder.index(value)

        # 划分子区间
        left_in_order = inorder[:index]
        right_in_order = inorder[index+1:]
        left_pre_order = preorder[1:index+1]
        right_pre_order = preorder[index+1:]

        # 左节点
        root.left = self.buildTree(left_pre_order, left_in_order)
        # 右结点
        root.right = self.buildTree(right_pre_order, right_in_order)
        return root


def main():
    pass

if __name__ == '__main__':
    main()
