from typing import *
from BinaryTree import TreeNode
from BinaryTree import creatTree

# 确定本题的使用方法
# 本题使用递归法
# 确定本题的边界条件
# 如果为空的情况下直接返回true
# 如果只有一个节点也返回true

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        if root and not root.left and not root.right:
            return True
        
        def is_balance_tree(root):
            if not root:
                return 0
            # 这个验证方式并不是最好的边界验证
            # 这种验证可能需要对下面进行左右子树节点的考虑
            # if root and not root.left and not root.right:
            #     return 1
            # 确定参数与返回值
            # 本题的参数为节点 返回值为整数值
            # 确定本题的边界条件
            # 如果为空的情况下那么就返回0
            left_hight = is_balance_tree(root.left)
            right_hight = is_balance_tree(root.right)
            # 确定本题的单层执行逻辑
            # 使用后序遍历，收集两边的深度进行验证
            # 这里先实现对深度的验证
            # 如果左边为-1或者右边为-1
            if left_hight == -1 or right_hight == -1:
                # 那么此时直接返回-1
                return -1
            # 否则
            else:
                # 求出两边的差距
                hight = abs(left_hight - right_hight)
                # 如果两边的差距 大于等于0小于等于1 那么就返回两边的最大深度
                if 0 <= hight <= 1:
                    return max(left_hight, right_hight) + 1
                else:
                    # 返回-1
                    return -1
        
        result = is_balance_tree(root)
        # 如果结果为-1则说明False
        if result == -1:
            return False
        # 否则为True
        else:
            return True

def main():
    sl = Solution()
    # case 1
    root = [3,9,20,None,None,15,7]
    tree = creatTree(root)
    print(sl.isBalanced(tree))
    # case 2
    root = [1,2,2,3,3,None,None,4,4]
    tree = creatTree(root)
    print(sl.isBalanced(tree))
    # case 3
    root = []
    tree = creatTree(root)
    print(sl.isBalanced(tree))

if __name__ == '__main__':
    main()