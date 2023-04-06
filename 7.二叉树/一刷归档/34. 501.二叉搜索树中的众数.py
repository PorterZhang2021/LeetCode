"""
501.二叉搜索树中的众数
"""

from typing import *
from NewTree import creatTree
from NewTree import TreeNode

class Solution:
    def __init__(self):
        # 前一个结点
        self.pre = TreeNode()
        # 统计频率
        self.count = 0
        # 最大频率
        self.max_count = 0
        # 结果集
        self.result = []
    
    def search_BST(self, cur: TreeNode) -> None:
        # 如果结点不存在的
        if not cur:
            return None
        # 左节点遍历
        self.search_BST(cur.left)
        # 第一个结点
        if not self.pre:
            self.count = 1
        # 与前一个结点数值相同
        elif self.pre.val == cur.val:
            self.count += 1
        # 与前一个结点数值不相同
        else:
            self.count = 1
        # 前一个结点
        self.pre = cur
        
        if self.count == self.max_count:
            self.result.append(cur.val)
        
        if self.count > self.max_count:
            self.max_count = self.count
            # 清空self.result, 确保result之前的元素都失效
            self.result = [cur.val]
        # 右递归
        self.search_BST(cur.right)
    
    def findMode(self, root: Optional[TreeNode]):
        # 如果根节点为空
        if not root:
            return None
        # 搜索二叉树
        self.search_BST(root)
        # 返回结果集
        return self.result
    


def main():
    s = Solution()
    tree = creatTree([1,None,2,2])
    print(s.findMode(tree))


if __name__ == '__main__':
    main()