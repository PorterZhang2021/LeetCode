"""
剑指Offer 05.替换空格
请实现一个函数，
把字符串 s 中的每个空格替换成"%20"。

此题处理应该比较容易
可以先将其转换成list
然后判断除是否有空格的位置
如果有空格的位置就换成%20
然后在集体拼接起来
"""

class Solution:
    def replaceSpace(self, s: str) -> str:
        # 更改成列表
        s = list(s)

        # 查找空格
        for i in range(len(s)):
            # 如果是空格
            if s[i] == " ":
                # 更改值
                s[i] = "%20"
        
        # 重新拼接成字符串
        s = "".join(s)

        # 返回字符串
        return s