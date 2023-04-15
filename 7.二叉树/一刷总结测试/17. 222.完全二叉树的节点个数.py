# 确定本题的使用方法
# 确定本题的边界条件
# 如果为空节点 那么返回0
# 如果为一个节点 那么返回1

# 本题使用迭代法
# 如果直接使用迭代法应该也很好解决
# 直接完成一遍对元素的遍历输出 其实最终就能得到结果？

from typing import *
from BinaryTree import TreeNode
from BinaryTree import creatTree

class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        # 这里给出节点值
        nums = 0
        # 如果节点为空
        # 那么直接返回
        if not root:
            return 0
        # 如果节点只有一个值也直接返回
        if root and not root.left and not root.right:
            return 1
        
        # 这里进行遍历操作
        def countNodes(root):
            nonlocal nums
            # 如果为空返回
            if not root:
                return
            
            # 进入左子树
            countNodes(root.left)
            # 获取值
            nums += 1
            # 进入右子树
            countNodes(root.right)
        
        countNodes(root)
        return nums

def main():
    sl = Solution()
    # case 1
    root = [1,2,3,4,5,6]
    tree = creatTree(root)
    print(sl.countNodes(tree))
    # case 2
    root = []
    tree = creatTree(root)
    print(sl.countNodes(tree))
    # case 3
    root = [1]
    tree = creatTree(root)
    print(sl.countNodes(tree))

if __name__ == '__main__':
    main()