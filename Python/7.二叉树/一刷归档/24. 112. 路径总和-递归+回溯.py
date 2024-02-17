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
    使用递归法 联想到获取所有路径题目 这里是递归+回溯
3. 确定使用哪一种遍历方式
    这里使用的是后序遍历的方式，将节点的情况返回回去

递归三部曲：
1. 确定参数与返回值
    参数 root 根节点  targetSum 目标总和
    返回值 这里的返回值无
2. 确定边界条件
    这里的边界条件是遇到叶子节点就进行布尔的操作
    这里边界条件为布尔的两种情况
    true：此时满足叶子节点与目标值为0
    false：此时满足叶子节点
3. 确定单层逻辑循环
    左逻辑
        这一部分要先判断是否还有左节点，因为边界条件部分并没有进行判断
        将左节点部分的值减去
        然后进行递归的判断，这里递归判断获取到叶子节点是true那么就返回
        将左节点部分的值回溯
    右逻辑
        这一部分要先判断是否还有右节点，因为边界条件部分并没有进行判断
        将右节点部分的值减去
        然后进行递归的判断，这里递归判断获取到叶子节点是true那么就返回
        将右节点部分的值回溯
    中逻辑
        这部分正好用来返回false，也就是叶子节点没有找到满足的情况
    
"""

from typing import *
from NewTree import TreeNode
from NewTree import creatTree

class Solution:
    def traversal(self, root, targetSum) -> bool:
        # 遇到叶子节点并且找到目标情况 返回true
        if not root.left and not root.right and targetSum == 0:
            return True
        # 遇到叶子节点没有找到目标情况 返回false
        if not root.left and not root.right:
            return False
        
        # 左操作
        if root.left:
            # 将节点值减去
            targetSum -= root.left.val
            # 如果遇到叶子节点返回true，则直接返回true
            if self.traversal(root.left, targetSum):
                return True
            # 回溯情况
            targetSum += root.left.val
        # 右操作
        if root.right:
            # 将节点值减去
            targetSum -= root.right.val
            # 如果遇到叶子节点返回true，则直接返回true
            if self.traversal(root.right, targetSum):
                return True
            # 回溯情况
            targetSum += root.right.val
        # 中逻辑操作，直接返回false
        return False

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False
        return self.traversal(root, targetSum - root.val)


def main():
    s = Solution()
    tree = creatTree([5,4,8,11,None,13,4,7,2,None,None,None,1])
    targetSum = 22
    print(s.hasPathSum(tree, targetSum))

if __name__ == '__main__':
    main()