"""
541.反转字符串Ⅱ
给定一个字符串 s 和一个整数 k，
从字符串开头算起，
每计数至 2k 个字符，
就反转这 2k 字符中的前 k 个字符。

如果剩余字符少于 k 个，则将剩余字符全部反转。
如果剩余字符小于 2k 但大于或等于 k 个，
则反转前 k 个字符，其余字符保持原样。

本题为一道模拟题
这种题目和需要利用递归的题目有点类似

他们的特点都需要将其拆分成一个小的问题
然后将小的问题解决，或者是他们总是有一个独立的步骤
这个步骤循环操作几次就能解决问题

对于这道题目
我们可以把它拆分成这样的问题
1. 解决2k区间里面的数的前k个数的反转
2. 判断区间是不是2k的情况
    如果是字符大于或等于k且小于2k那么用解决2k区间里面的数的前k个数反转
    如果是小于k则全部反转

那这种情况下，我们就可以明确的知道如果要解决这个题目就是要分成两种可能性
然后每次验证好区间的情况
在区间内找好2k的位置
"""

class Solution:
    @staticmethod
    def reverseString(s: List[str], left, right) -> None :
        while left <= right:
            # 交换两个指针之间的元素
            s[left], s[right] = s[right], s[left]
            # 两个指针缩小边界
            left += 1
            right -= 1

    def reverseStr(self, s: str, k: int) -> str:
        # 将其先转换成list模式
        s = list(s)
        # 工作区间
        cur_k = 0

        # 每次的步进为2*k
        for i in range(0, len(s), 2 * k):
            # 如果i + k的值小于字符长度 
            # 那么说明其剩余字符少于k个，则剩余的部分全部反转
            if i + k <= len(s):
                Solution.reverseString(s, i, i + k - 1)
                continue
            # 否则就是直接反转前k个字符
            else:
                Solution.reverseString(s, i, len(s) - 1)

        # 重新转回成字典
        s = "".join(s)

        return s