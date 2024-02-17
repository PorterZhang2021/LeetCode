from typing import *
from BinaryTree import TreeNode
from BinaryTree import creatTree

# 确定本题的使用方法
# 本题的使用方法为递归法
# 确定本题是否具有特殊的边界条件

# 构建一个结点
# 拆分左右区间
# 利用后序遍历获取根结点
# 利用中序遍历划分区间

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if len(inorder) == 0 or len(postorder) == 0:
            return
            
        # 获取根结点值
        value = postorder[-1]
        # 创建一个结点
        root = TreeNode(value)
        
        # 获取两个列表的长度
        # 中序列表长度
        in_length = len(inorder)
        # 后序列表长度
        post_length = len(postorder)

        # 查找索引
        index = inorder.index(value)

        
        # 利用此划分中序列表
        left_in_order = inorder[:index]
        right_in_order = inorder[index+1:]
        # 利用此划分后序序列
        left_post_order = postorder[0:index]
        right_post_order = postorder[index:post_length-1]
        # 构建左结点
        root.left = self.buildTree(left_in_order, left_post_order)
        # 构建右结点
        root.right = self.buildTree(right_in_order, right_post_order)
        return root

def main():
    sl = Solution()
    # case 1
    inorder = [9,3,15,20,7]
    postorder = [9,15,7,20,3]
    print(sl.buildTree(inorder, postorder))

if __name__ == '__main__':
    main()