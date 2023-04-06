"""
404.左叶子之和
给定二叉树的根节点 root ，返回所有左叶子之和。
本题主要是要将左节点的值全部加载一起即可
那么采用何种遍历模式是不是并没有关系

这里我实验采用前序和后序遍历
优先凭直觉使用后序遍历，因为后序遍历会每次返回值给中节点

1. 确定参数与返回值
    参数为 root 与 total 这个total用于存放所有左叶子节点值
2. 确定边界条件
    这个部分如果为空就返回
3. 确定单层循环逻辑
    左右两部分递归即可
    中的部分可以直接判断是否为左叶子节点然后存值

"""

from typing import *
from NewTree import TreeNode
from NewTree import creatTree

class Solution:
    def get_sum_of_leftleves(root):
        # 边界条件
        if not root:
            return 0;
        # 如果节点为左叶子

        

        # 进入左子树
        left_value = Solution.get_sum_of_leftleves(root.left)
        
        # 进入右子树
        right_vale = Solution.get_sum_of_leftleves(root.right)

        # 先判断是不是有左节点 因为这个内容其实是对中间的判断
        # 这个地方在哪个位置影响并不大，写在左子树部分，主要是逻辑一致
        if root.left:
            left_root = root.left
            # 判断是不是左叶子节点
            if not left_root.left and not left_root.right:
                # 将左叶子节点的值加入
                left_value = left_root.val
        
        # 将左右部分的值整合
        sum = left_value + right_vale
        # 中节点返回整合后的值
        return sum
        
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        return Solution.get_sum_of_leftleves(root)


def main():
    s = Solution()
    tree = creatTree([3,9,20,None,None,15,7])
    print(s.sumOfLeftLeaves(tree))


if __name__ == '__main__':
    main()