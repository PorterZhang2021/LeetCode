"""
541.反转字符串Ⅱ
给定一个字符串 s 和一个整数 k，
从字符串开头算起，
每计数至 2k 个字符，
就反转这 2k 字符中的前 k 个字符。

如果剩余字符少于 k 个，则将剩余字符全部反转。
如果剩余字符小于 2k 但大于或等于 k 个，
则反转前 k 个字符，其余字符保持原样。

边界指针法+计数
计数
计数总共的情况有：
剩余字符少于k个，剩余字符全部反转

剩余字符小于2k但大于或等于k个
反转前k个字符，其余字符保持不变

正常情况，计数2k个字符，反转2k字符中的前k个字符


直接的计数模拟方式并不是一个好的解决方案
而是直接每次移动2*k
"""

class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        # 将其转成列表
        s = list(s)
        # 用于计数
        count = 0
        # 左边界指针
        left = 0
        # 右边界指针
        right = len(s) - 1
        # 左边界坐标
        cur_k = 0

        # 用于计数字符
        while cur_k < len(s):
            # 如果字符为2k了
            if count == 2 * k:
                # 左边界指针
                left = cur_k - 2 * k
                # 右边界指针
                right = cur_k - k
                # 进行反转
                while left <= right:
                    s[left], s[right] = s[right], s[left]
                # 重置计数
                count = 0
            # 进行移动
            cur_k += 1
            # 进行计数
            count += 1
        
        # 最后部分的处理
        # 如果剩余字符少于k个
        if count < k:
            # 左边界指针
            left = len(s) - count - 1
        # 如果剩余字符小于2k但大于或等于k个
        elif count >= k and count < 2 * k:
            # 左边界指针
            left = len(s) - count - 1
        # 右边界指针
        right = len(s) - 1
        # 进行反转
        while left <= right:
            s[left], s[right] = s[right], s[left]
