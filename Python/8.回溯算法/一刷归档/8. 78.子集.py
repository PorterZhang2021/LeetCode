from typing import *

# 确定本题的使用方法
# 确定本题的特殊边界条件
# 如果空值则返回一个空的

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result_list = []
        # 边界条件
        if not nums:
            return [[]]
        
        # 回溯函数
        k = len(nums)
        
        # 确定参数与返回值
        def backtracing(tmp_result, start, end):
            nonlocal result_list
            # 边界条件 - 此部分为终止情况
            if start <= k:
                result_list.append(list(tmp_result))
                if start == k:
                    return

            # 单层逻辑处理
            for i in range(start, end):
                # 确定处理逻辑
                num = nums[i]
                tmp_result.append(num)
                # 确定函数
                backtracing(tmp_result, start=i+1, end=len(nums))
                # 确定回溯内容
                tmp_result.pop()
        
        backtracing(tmp_result=[], start=0, end=len(nums))
        return result_list

def main():
    sl = Solution()
    # case 1
    nums = [1, 2, 3]
    print(sl.subsets(nums))

if __name__ == '__main__':
    main()