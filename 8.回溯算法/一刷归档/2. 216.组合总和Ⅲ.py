from typing import *

# 确定本题的使用方法
# 本题使用回溯法
# 确定本题是否具有特殊条件 - 无

# 回溯法完成后
# 进行剪枝操作
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        # 集合
        result = []
        tmp_result = []
        # 确定回溯的参数与返回值
        def backtracking(k, n, tmp_result, start, end):
            nonlocal result
            # 确定边界条件
            if k == 0:
                # 获取结果
                # 此部分用于保存结果集
                if n == 0:
                    result.append(list(tmp_result))
                return
            # 确定回溯的操作
            for i in range(start, end+1):
                # 处理操作
                # 减数
                k -= 1
                # 结果和
                n -= i
                start = i + 1
                tmp_result.append(i)
                backtracking(k, n, tmp_result, start, end)
                # 回溯操作
                # 回溯
                k += 1
                # 总和撤销
                n += i
                tmp_result.pop()
        backtracking(k, n, tmp_result, 1, 9)
        return result

def main():
    sl = Solution()
    # case 1
    n = 7
    k = 3
    print(sl.combinationSum3(k, n))
    # case 2
    n = 9
    k = 3
    print(sl.combinationSum3(k, n))
    # case 3
    k = 4
    n = 1
    print(sl.combinationSum3(k, n))

if __name__ == '__main__':
    main()