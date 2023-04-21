from typing import *

# 确定本题的使用方法
# 确定本题是否有特殊边界条件
# 如果candidates为空那么直接返回空
# 如果candidates只有一个值
# 且这个值不能整除目标那么同样返回空

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result_list = []
        # 特殊边界条件
        if not candidates:
            return result_list
        if len(candidates) == 1:
            result = candidates[0] / target
            if result != 0:
                return result_list
        
        # 开始值
        start = 0
        # 终止值
        end = len(candidates)
        
        # 确定回溯参数与返回值
        def combination_sum(target, tmp_result, start, end):
            nonlocal result_list
            # 确定边界条件
            # 这里的边界条件为结果 小于等于0时就进行返回
            if target <= 0:
                # 进行结果的处理
                # 如果目标结果为0那么加入
                if target == 0:
                    result_list.append(list(tmp_result))
                return
            
            # 确定回溯的执行逻辑
            for i in range(start, end):
                # 处理逻辑
                # 减去目标值
                num = candidates[i]
                target -= num
                # 添加减去的目标值
                tmp_result.append(num)


                # 递归函数 - 此位置的参数可以用于缩减递归的宽度
                combination_sum(target, tmp_result, start=i, end=end)
                
                # 回溯逻辑
                # 增加目标值
                target += num
                # 增加减去的目标值
                tmp_result.pop()


        combination_sum(target, tmp_result=[], start=start, end=end)
        return result_list

def main():
    sl = Solution()
    # case 1
    candidates = [2,3,5]
    target = 8
    print(sl.combinationSum(candidates, target))
    # case 2
    candidates = [2,3,6,7]
    target = 7
    print(sl.combinationSum(candidates, target))
    # case 3
    candidates = [2]
    target = 1
    print(sl.combinationSum(candidates, target))

if __name__ == '__main__':
    main()