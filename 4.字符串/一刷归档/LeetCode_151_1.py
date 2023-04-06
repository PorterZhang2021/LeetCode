"""
151.反转字符串中的单词
给你一个字符串 s ，
请你反转字符串中 单词 的顺序。

单词 是由非空格字符组成的字符串。
s 中使用至少一个空格将字符串中的 单词 分隔开。

返回 单词 顺序颠倒且 单词 之间用单个空格连接的结果字符串。

注意：输入字符串 s中可能会存在前导空格、
尾随空格或者单词间的多个空格。
返回的结果字符串中，单词间应当仅用单个空格分隔，且不包含任何额外的空格。

1. 单词整体反转 -> 对句子整体反转
2. 当中可能会有空格，每次单词之间空一个空格，其余空格清除

单词判定-> 前面可能有空格或者没有空格 这个判定较为麻烦
后面必定有空格用于分隔，利用此来进行单词的判定

本题利用了空间换时间，并不是最优解

"""

class Solution:
    def reverseWords(self, s: str) -> str:
        # 将单词先转换成列表
        s = list(s)
        # 构建一个新的列表 用于存放结果
        result = []

        # 获取单词
        # 第一层循环 用来循环字符
        word = ""
        for ch in s:         
            # 如果碰到空格
            if ch == " ":
                # 拼接的单词放入列表中
                # 如果word不为空那么就存入
                if word != "":
                    result.append(word)
                word = ""
                continue
            
            # 拼接单词
            word =  word + ch
        
        # 末尾单词添加
        if word != "":
            result.append(word)

        # 左右边界指针法
        left = 0
        right = len(result) - 1
        
        # 反转单词
        while left <= right:
            result[left], result[right] = result[right], result[left]
            # 缩小边界
            left += 1
            right -= 1

        # 改成字符
        s = " ".join(result)
        
        # 返回字符
        return s


def main():
    s = Solution()
    print(s.reverseWords("a good   example"))


if __name__ == '__main__':
    main()
