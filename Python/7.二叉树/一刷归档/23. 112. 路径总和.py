"""
112. 路径总和
给你二叉树的根节点 root 和一个表示目标和的整数 targetSum 。
判断该树中是否存在 根节点到叶子节点 的路径，
这条路径上所有节点值相加等于目标和 targetSum 。
如果存在，返回 true ；否则，返回 false 。
叶子节点 是指没有子节点的节点。

1. 确定是否有边界问题需要思考 
    本题并不需要特殊边界思考
    这里有一个二叉树为空的边界思考条件 - 未想到
2. 确定使用迭代法还是递归法
    使用递归法 联想到获取所有路径题目 这里是路径+回溯
3. 确定使用哪一种遍历方式
    这里使用的是前序遍历的方式

递归三部曲：
1. 确定参数与返回值
    参数 root 根节点  path 路径  results 结果集
    返回值 这里的返回值无
2. 确定边界条件
    这里的边界条件是 如果是叶子节点就返回 这一部分逻辑主要处理路径的形成
    将节点放入路径中
    存入结果集
3. 确定单层逻辑循环
    中逻辑 放入节点进path
    左逻辑与右逻辑
        1. 判断好是否还具有节点 - 因为边界条件部分用于处理叶子节点了
        2. 每次进行回溯
"""

from typing import *
from NewTree import TreeNode
from NewTree import creatTree

class Solution:
    def get_path_results(self, root, path, results):
        # 边界情况 如果是叶子节点就操作
        if root.left is None and root.right is None:
            # 将节点加入path中
            path.append(root)
            # 获取结果值
            result = 0
            for node in path:
                result += node.val
            # 存入结果集
            results.append(result)
            return
        # 中逻辑
        path.append(root)
        # 左逻辑
        if root.left:
            # 递归
            self.get_path_results(root.left, path, results)
            # 回溯
            path.pop()
        # 右逻辑
        if root.right:
            # 递归
            self.get_path_results(root.right, path, results)
            # 回溯
            path.pop()

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # 路径
        path = []
        # 结果集
        results = []
        if not root:
            return False
        # 获取所有结果
        self.get_path_results(root, path, results)
        # 对结果判断
        for result in results:
            if result == targetSum:
                return True
        return False


def main():
    s = Solution()
    tree = creatTree([5,4,8,11,None,13,4,7,2,None,None,None,1])
    targetSum = 22
    print(s.hasPathSum(tree, targetSum))

if __name__ == '__main__':
    main()