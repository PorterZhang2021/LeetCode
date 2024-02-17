from typing import *

# 确定本题的使用方法
# 本题使用回溯法
# 本题在前面某个题目中有相关的解法
#  因此本题的难度就有些下降了
# 确定边界条件


class Solution:
    def __init__(self) -> None:
        self.path = []
        self.paths = []
        self.used = []

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        self.used = [False] * len(nums)
        self.backtracking(nums, start=0, end=len(nums))
        return self.paths
    
    # 确定参数与返回值
    def backtracking(self,nums, start, end):
        # 确定边界条件
        if start <= end:
            self.paths.append(self.path[:])
            if start == end:
                return
        for i in range(start, end):
            # 确定处理逻辑
            num = nums[i]
            if i > 0 and nums[i - 1] == num and self.used[i-1] == False:
                continue
            self.path.append(num)
            start = i + 1
            self.used[i] = True
            # 回溯函数
            self.backtracking(nums, start, end)
            # 确定回溯函数的回撤
            self.path.pop()
            self.used[i] = False

def main():
    sl = Solution()
    # case 1
    nums = [1, 2, 2]
    print(sl.subsetsWithDup(nums))

if __name__ == '__main__':
    main()
