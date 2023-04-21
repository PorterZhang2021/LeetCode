from typing import *

# 确定本题的使用方法
# 回溯法
# 确定本题的边界条件
# 如果数字为空字符串
# 那么直接返回一个空的结果集

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # 结果集
        result = []
        # 边界情况
        if digits == "":
            return []

        # 处理数字情况
        # 数字集
        digits_table = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }

        digits_list = []
        
        for ch in digits:
            if digits_table.__contains__(ch):
                digits_list.append(digits_table[ch])
        
        k = len(digits)


        # 确定回溯函数参数与返回值
        def backtracking(nums_index, tmp_list=[]):
            nonlocal result
            # 确定回溯的边界条件
            if k == nums_index:
                word = ''.join(tmp_list)
                result.append(word)
                # 结果处理
                return
            # 确定回溯的逻辑处理
            # 同层集合 此部分拿到本层的子集
            for ch in digits_list[nums_index]:
                # 取出字母放入
                tmp_list.append(ch)
                # 数字增加
                nums_index += 1
                backtracking(nums_index, tmp_list)
                # 回溯逻辑
                # 字母回溯
                tmp_list.pop()
                # 数字回溯
                nums_index -= 1
        backtracking(0, [])
        return result

def main():
    sl = Solution()
    digits = "23"
    print(sl.letterCombinations(digits))

if __name__ == '__main__':
    main()
