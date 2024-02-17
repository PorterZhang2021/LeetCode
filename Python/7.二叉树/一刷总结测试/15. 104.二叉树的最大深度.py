# 确定本题的使用方法
# 确定本题是否有特别的边界条件
# 本题边界条件可以直接包含在递归的情况中
# 如果本题没有节点的话，那么深度应该是0

# 本题使用方法为递归法
# 确定本题的参数与返回值
# 本题的参数为根节点 返回值为整数
# 确定本题的边界条件
# 本题的边界条件为节点为空 那么此时返回0
# 确定本题的单层逻辑
# 本题需要考虑的是最大深度，因此使用后序遍历收集结果
# 本题发现需要收集结果的情况下，那么左右递归需要赋值给变量
# 每个变量最终都会返回一个值 这里需要比较左右变量中哪个值
# 比较大，将大的那个+1进行返回

from typing import *
from BinaryTree import TreeNode
from BinaryTree import creatTree

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # 这里单独最边界的情况不需要考虑
        # 边界情况
        if not root:
            return 0
        
        # 后序遍历
        # 将左子树进行遍历
        left_hight = self.maxDepth(root.left)
        # 将右子树进行遍历
        right_hight = self.maxDepth(root.right)
        # 对左右子树的结果找到最大值
        hight = max(left_hight, right_hight)
        # 返回结果给上一层
        return hight + 1

def main():
    sl = Solution()
    # case 1
    root = [3,9,20,None,None,15,7]
    tree = creatTree(root)
    print(sl.maxDepth(tree))
    # case 2

if __name__ == '__main__':
    main()