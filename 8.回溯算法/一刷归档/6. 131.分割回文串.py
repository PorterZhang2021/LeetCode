from typing import *

class Solution:
    def __init__(self) -> None:
        self.paths = []
        self.path = []

    def partition(self, s: str) -> List[List[str]]:
        # 边界情况
        # 如果为空
        if not s:
            return []
        # 如果只有一个值
        if len(s) == 1:
            return [[s]]
        self.backtracking(s, start=0)
        return self.paths
    
    def backtracking(self, s, start):
        # 确定边界条件
        # 由于边界条件和深度有关因此这里要考虑深度最后的情况
        # 每次循环其实就是再一次套一个循环，那么循环到最后会超过边界
        # 那么此时就是返回的时机
        if start >= len(s):
            # 这里存放所有结果
            self.paths.append(self.path[:])
            return

        # 确定回溯函数的逻辑
        # 本题循环的内容为字母字符因此这里
        # 起始位置和终止位置为字符的索引
        for i in range(start, len(s)):
            # 处理逻辑
            # 如果满足回文的情况下，我们就需要将结果进行保存了
            # 这里的回文长度同start与i有关
            # start可以回溯从1位到多位的情况
            if self.is_palindrome(s, start, i):
                # 这里将结果存入
                self.path.append(s[start:i+1])
                # 递归内容 此部分的start要缩小集合域，因此这里利用的应该是i
                self.backtracking(s, start=i+1)
                # 回溯逻辑 
                # 结果进行回溯
                self.path.pop()
            else:
                continue
    # 双指针构建反转字符串查询
    def is_palindrome(self, s, left, right):
        while left <= right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

def main():
    pass

if __name__ == '__main__':
    sl = Solution()
    s = "aab"
    print(sl.partition(s))