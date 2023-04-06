"""
513.找树左下角的值
给定一个二叉树的 根节点 root，请找出该二叉树的 最底层 最左边 节点的值。
假设二叉树中至少有一个节点。

1. 确定是否有边界问题 暂无
2. 决定使用哪种遍历方式 
    本题使用层序遍历方式 解决获取最底层的问题
3. 根据遍历方式选择用迭代法还是用递归法
    迭代法

满足条件是最底层 最左边
迭代法这部分最重要的逻辑就是左子树部分，
这里最好使用的是队列分层，然后获取层数中第一个值
本题就需要构建队列了
"""

from typing import *
from NewTree import TreeNode
from NewTree import creatTree

class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        # 栈
        queue = [root]
        # 结果集
        results = []
        
        # 队列出栈
        while queue:
            # 本层长度
            level_len = len(queue)
            # 本层值
            level_val_list = []
            # 进行遍历
            for i in range(level_len):
                # 取出头部元素
                node = queue.pop(0)
                # 将值存入层中
                level_val_list.append(node.val)
                # 进入左子树
                if node.left:
                    # 存入左子树节点
                    queue.append(node.left)
                # 进入右子树
                if node.right:
                    # 存入右子树节点
                    queue.append(node.right)
            # 将本层值存入结果集中
            results.append(level_val_list)

        # 获取最后一层
        last_level_val_list = results[-1]
        # 获取最后一层第一个值
        left_val = last_level_val_list[0]
        # 输出获取到的值
        return left_val


def main():
    s = Solution()
    tree = creatTree([2,1,3])
    print(s.findBottomLeftValue(tree))

if __name__ == '__main__':
    main()