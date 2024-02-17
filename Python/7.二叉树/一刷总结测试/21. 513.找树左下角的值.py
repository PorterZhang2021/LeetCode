# 确定本题的使用方法
# 本题使用递归法
# 确定本题的边界条件
# 本题由于二叉树中只要有一个结点
# 那么此时考虑边界就不需要考虑无结点的情况
# 如果只有一个结点那么树最左下角是不是就为root本身呢？

# 本题使用的方法为迭代法
# 迭代法使用层序遍历获取出结果集
# 最终将结果集的最底层的第一个值放出

from typing import *
from BinaryTree import TreeNode
from BinaryTree import creatTree

class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        # 结果集 
        result = []
        # 处理序列
        handle_queue = [root]

        while handle_queue:
            # 处理序列
            length = len(handle_queue)
            # 层次列表
            level_list = []
            for i in range(length):
                # 子节点
                node = handle_queue.pop(0)
                # 如果有左结点
                if node.left:
                    handle_queue.append(node.left)
                # 如果有右结点
                if node.right:
                    handle_queue.append(node.right)
                # 存入值
                level_list.append(node.val)
            # 存入值
            result.append(level_list)
        
        # 输出值 最底层 最左边
        num = result[-1][0]
        return num

def main():
    sl = Solution()
    # case 1
    root = [2,1,3]
    tree = creatTree(root)
    print(sl.findBottomLeftValue(tree))
    # case 2
    root = [1,2,3,4,None,5,6,None,None,7]
    tree = creatTree(root)
    print(sl.findBottomLeftValue(tree))

if __name__ == '__main__':
    main()