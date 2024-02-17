from typing import *

"""
给定两个整数n和k，返回范围[1, n]中所有可能的k个数的组合
集合: [1, n]
k个数: 深度
"""

# 确定本题的使用方法
# 本题使用回溯法
# 确定本题是否有特殊的边界条件 - 无

# 确定返回值以及参数
# 回溯函数的终止条件
# 回溯搜索的遍历过程
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # 结果集
        result = []
        # 此部分出现的问题是同内存地址
        # 因此这里要解决同内存地址的问题
        tmp_result = []
        def backtracking(start, end, k, tmp_result):
            nonlocal result
            if k == 0:
                result.append(list(tmp_result))
                return
            for i in range(start, end+1):
                k -= 1
                start = i + 1
                tmp_result.append(i)
                backtracking(start, end, k, tmp_result)
                tmp_result.pop()
                k += 1
        backtracking(1, n, k, tmp_result)
        return result

def main():
    sl = Solution()
    # case 1
    n = 4
    k = 2
    print(sl.combine(n, k))
    n = 1
    k = 1
    print(sl.combine(n, k))


if __name__ == '__main__':
    main()