"""
KMP算法模板题目
这个题目的理解难度较高
单独抽时间理解一遍
"""

class Solution:
    
    def get_next(self, a, needle):
        # 自身匹配
        # 构建前缀表
        next = [' ' for i in range(a)]
        # 初始化前缀表
        k = -1
        next[0] = k
        for i in range(1, len(needle)):
            # 在前缀表中进行回溯，这一部分借用到了之前求解的结果，可以说是一种递归
            while(k > -1 and needle[k+1] != needle[i]):
                k = next[k]
            
            if needle[k+1] == needle[i]:
                k += 1
            next[i] = k
        # 返回前缀表
        return next
    
    def strStr(self, haystack: str, needle: str) -> int:
        # 
        a = len(needle)
        # 
        b = len(haystack)
        if a == 0:
            return 0
        next = self.getnext(a, needle)
        # 设置开始
        p = -1
        # 两个数组间的匹配
        for j in range(b):
            while p >= 0 and needle[p+1] != haystack[j]:
                p = next[p]
            if needle[p+1] == haystack[j]:
                p += 1
            if p == a - 1:
                return j - a + 1
        return -1
    
