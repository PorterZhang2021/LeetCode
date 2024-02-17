"""
108. 将有序数组转换为二叉搜索树
给你一个整数数组 nums ，其中元素已经按 升序 排列，请你将其转换为一棵 高度平衡 二叉搜索树。

高度平衡 二叉树是一棵满足「每个节点的左右两个子树的高度差的绝对值不超过 1 」的二叉树。

传入的值为整数数组升序
1. 高度平衡
2. 二叉搜索树

1. 确定参数与返回值
    参数 节点 起始索引  终止索引
2. 确定边界条件
    如果起始索引>终止索引就结束
3. 确定单层逻辑循环
    找到中间位置
    构建一个节点
    左子树递归
    右子树递归
    返回构建好的节点
"""

from typing import *
from NewTree import creatTree
from NewTree import TreeNode

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def travesal(nums, left, right):
            # 如果起始索引大于终止索引就结束
            if left > right:
                return None
            # 找到中间位置
            mid = left + int((left + right) / 2)
            # 构建节点
            root = TreeNode(nums[mid])
            # 左子树递归
            root.left = travesal(nums, left, mid)
            # 右子树递归
            root.right = travesal(nums, mid+1, right)
            # 返回节点
            return root
        return travesal(nums, 0, len(nums) - 1)