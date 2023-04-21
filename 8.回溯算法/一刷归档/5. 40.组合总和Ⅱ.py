from typing import *

# 确定本题的使用方法
# 本题使用回溯法
# 确定本题是否具有特殊边界条件
# 如果结果集为空 那么直接返回空
# 如果结果集只有一个，且不相等那么同样返回空

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result_list = []
        used = [False] * len(candidates)

        # 边界条件
        if not candidates:
            return result_list
        if len(candidates) == 1:
            if target == candidates[0]:
                return [[target]]
            else:
                return result_list
        
        # 起始值
        start = 0
        # 终止值
        end = len(candidates)
        candidates.sort()

        # 确定参数与返回值
        def combination_sum2(target, tmp_result, start, end):
            nonlocal used
            nonlocal result_list
            # 确定边界条件
            if target <= 0:
                # 进行结果的处理
                if target == 0:
                    result_list.append(list(tmp_result))
                return
            
            # 确定回溯的执行逻辑
            for i in range(start, end):
                # 确定回溯处理逻辑
                num = candidates[i]
                # 这里False正好说明了前面已经完全用完了，此时再用那么就会出现重复的答案
                if i > 0 and candidates[i - 1] == num and used[i - 1] == False:
                    continue
                target -= num
                tmp_result.append(num)
                used[i] = True
                
                start = i + 1
                
                # 递归函数
                combination_sum2(target, tmp_result, start, end)

                # 回溯逻辑
                target += num
                tmp_result.pop()
                used[i] = False
                        
        combination_sum2(target, tmp_result=[], start=start, end=end)
        return result_list

def main():
    sl = Solution()
    # case 1
    candidates = [10,1,2,7,6,1,5] 
    target = 8
    print(sl.combinationSum2(candidates, target))


if __name__ == '__main__':
    main()
