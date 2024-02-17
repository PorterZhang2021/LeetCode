from typing import *
from BinaryTree import TreeNode
from BinaryTree import creatTree

class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        # 如果发现列表为空那么返回None
        if not nums:
            return None
        
        # 构建一个结点
        # 获取最大值
        num = max(nums)
        root = TreeNode(num)
        # 获取最大值的索引
        index = nums.index(num)
        # 左数值区间
        left_nums = nums[:index] 
        # 右数值区间
        right_nums = nums[index+1:]
        # 左子节点
        root.left = self.constructMaximumBinaryTree(left_nums)
        # 右子节点
        root.right = self.constructMaximumBinaryTree(right_nums)
        return root


def main():
    pass

if __name__ == '__main__':
    main()