from typing import *
import sys

# 确定本题的解题方式
# 本题使用回溯法
# 确定本题的边界条件
# 如果为空那么直接返回空
# 如果只有一个值，那么直接返回一个值的情况

class Solution:
    def __init__(self) -> None:
        self.path = []
        self.paths = []

        
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        self.path.clear()
        self.paths.clear()
        self.used = [False] * len(nums)
        self.max_num = nums[0]
        self.backtracking(nums=nums, start=0, end=len(nums))
        return self.paths

    # 确定回溯函数与返回值
    def backtracking(self, nums, start, end):
        
        # 确定边界条件
        if start <= len(nums):
            if len(self.path) > 1:
                self.paths.append(self.path[:])
            if start == len(nums):
                return

        usage_list = set()
        # 确定执行逻辑
        for i in range(start, end):
            # 处理逻辑
            num = nums[i]
            if (self.path and self.path[-1] > num) or (num in usage_list):
                continue
            usage_list.add(num)
            self.path.append(num)
            start = i + 1
            # 回溯函数
            self.backtracking(nums=nums, start=start, end=end)
            # 回溯逻辑
            self.path.pop()

            
def main():
    # 
    sl = Solution()
    # case 1
    nums = [4,6,7,7]
    print(sl.findSubsequences(nums=nums))
    # case 2
    nums = [4,4,3,2,1]
    print(sl.findSubsequences(nums=nums))
    # case 3
    print(sl.findSubsequences([1,2,3,4,5,6,7,8,9,10,1,1,1,1,1]))

if __name__ == '__main__':
    main()