from typing import *
from BinaryTree import TreeNode
from BinaryTree import creatTree

# 确定本题使用的方法
# 本题使用二分法+递归法
# 确定本题是否有特殊的边界条件
# 如果具有那么就是[]和[1]这两种情况需要讨论
# 使用二分加递归可以构造出我们所需要的值

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # 边界条件
        # 如果只有[]
        if not nums:
            return None
        if len(nums) == 1:
            root = TreeNode(nums)
            return root
        
        # 确定参数与返回值
        # 本题的参数为根节点 返回值为None

        def sorted_array_to_bst(root, nums, left, right):
            # 本题的边界条件有误
            # if mid == left or mid == right:
            #     return None
            # 正确边界条件
            if left < right:
                return None
            mid = int((left + right) / 2)
            value = nums[mid]
            root  = TreeNode(value)
            root.left = sorted_array_to_bst(root, nums, left, mid-1)
            root.right = sorted_array_to_bst(root, nums, mid+1, right)
        # 这里要赋值
        root = sorted_array_to_bst(root, nums, 0, len(nums) - 1)
        return root

def main():
    pass

if __name__ == '__main__':
    main()