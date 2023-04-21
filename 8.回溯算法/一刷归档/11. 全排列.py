# 确定本题的使用方法
# 回溯法
# 确定本题的边界条件

from typing import *

class Solution:
    def __init__(self) -> None:
        self.paths = []
        self.path = []

    def permute(self, nums: List[int]) -> List[List[int]]:
        self.path.clear()
        self.paths.clear()
        usage_list = [False] * len(nums)
        self.backtracking(nums=nums, usage_list=usage_list)
        return self.paths
    
    # 确定本题的参数与返回值
    def backtracking(self, nums, usage_list):
        # 确定本题的边界条件
        # 如果满足长度那么此时返回
        if len(self.path) == len(nums):
            self.paths.append(self.path[:])
            return

        # 确定处理逻辑
        for i in range(len(nums)):
            # 确定处理方式
            num = nums[i]
            if usage_list[i] == True:
                continue
            usage_list[i] = True
            self.path.append(num)

            # 确定回溯函数
            self.backtracking(nums, usage_list)
            
            self.path.pop()
            usage_list[i] = False

            


def main():
    # 
    sl = Solution()
    nums = [1, 2, 3]
    print(sl.permute(nums=nums))

if __name__ == '__main__':
    main()