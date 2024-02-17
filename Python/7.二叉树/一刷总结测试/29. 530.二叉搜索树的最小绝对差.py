from typing import *
from BinaryTree import TreeNode
from BinaryTree import creatTree
import sys

# 确定本题的使用方法
# 递归法
# 确定本题的特殊边界条件
# 本题因为要确定树中任意两个不同节点值之间的最小差值
# 因此其最少应该有两个节点

# 本题在递归法的使用上有一些特殊
# 因为本题的递归是在中序遍历的基础上
# 而二叉搜索树的中序遍历的情况下是按升序进行输出的
# 因此比较两个值的大小就可以得到我们所需要的最小绝对差值



class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        pre = None
        min_num = sys.maxsize
        # 确定参数
        # 参数为节点 返回值 无
        def get_min_num(root):
            nonlocal min_num
            nonlocal pre
            # 确定边界条件
            # 如果节点为空则结束
            if not root:
                return
            
            # 确定单层逻辑
            # 遍历左子树
            get_min_num(root.left)
            # 如果有了前节点
            if pre:
                # 比较两者的值
                num = abs(root.val - pre.val)
                # 如果这个值比min_num小
                if min_num > num:
                    min_num = num
            # 更新pre
            pre = root
            # 遍历右子树
            get_min_num(root.right)
        # 输出结果
        get_min_num(root)
        return min_num

def main():
    sl = Solution()
    # case 1
    root = [4,2,6,1,3]
    tree = creatTree(root)
    print(sl.getMinimumDifference(tree))

if __name__ == '__main__':
    main()