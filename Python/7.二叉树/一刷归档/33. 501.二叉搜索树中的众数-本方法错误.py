"""
501. 二叉搜索树中的众数
给你一个含重复值的二叉搜索树（BST）的根节点 root ，
找出并返回 BST 中的所有 众数（即，出现频率最高的元素）。

如果树中有不止一个众数，可以按 任意顺序 返回。

假定 BST 满足如下定义：

结点左子树中所含节点的值 小于等于 当前节点的值
结点右子树中所含节点的值 大于等于 当前节点的值
左子树和右子树都是二叉搜索树

1. 确定参数与返回值
    参数 根结点
    返回值 返回字典
2. 确定边界条件
    如果根节点为空则返回
3. 确定单层逻辑
    递归左子树
    中间将结点输出保存
    递归右子树

"""

from typing import *
from NewTree import TreeNode
from NewTree import creatTree

class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        num_root = {}
        def findTree(root):
            nonlocal num_root

            if not root:
                return
            
            findTree(root.left)
            findTree(root.right)
            if  num_root.__contains__(root.val):
                num_root[root.val] += 1
            else:
                num_root[root.val] = 1
        findTree(root)
        pre_root = {}
        # 将索引和值输出
        for key, value in num_root.items():
            # 如果频次索引存在
            if pre_root.__contains__(value):
                # 添加索引
                val_root.append(key)
            else:
                # 否则创建新的
                val_root = []
        # 找出索引当中最大的
        max_val = max(pre_root.values())
        # 输出最大的众数
        return pre_root[max_val]


def main():
    s = Solution()
    tree = creatTree([1,None,2,2])
    print(s.findMode(tree))

if __name__ == '__main__':
    main()
