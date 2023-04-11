from typing import *

class Solution:
    def stripSpace(self, s: str) -> str:
        # 1. 移除多余的空格问题
        # 确定本步骤的使用方法
        # 本步骤使用双指针法
        # 双指针法是同向还是异向 - 同向
        # 双指针法的用途是什么？
        # cur用于对整体进行遍历
        # index用于对索引情况进行保存
        
        # 序列化
        s = list(s)
        # 长度
        length = len(s)
        # 索引
        index = 0
        # 标志位
        flag = True

        for cur in range(length):
            # 如果为空且标志位为True
            if s[cur] == ' ' and flag == True:
                # 将此部分保存
                s[index] = s[cur]
                # 索引自增
                index += 1
                # 标志位复位
                flag = False
            elif s[cur] == ' ' and flag == False:
                continue
            else:
                # 将此部分保存
                s[index] = s[cur]
                # 索引自增
                index += 1
                # 标志位复位
                flag = True
        
        # 重新构建
        s = s[:index]
        
        # 对前空格和后空格进行消去
        if s[0] == ' ':
            s.pop(0)
        if s[-1] == ' ':
            s.pop()

        s = ''.join(s)
        
        # 返回字符串
        return s
    # 单词反转
    def reverseString(self, s: str, left: int, right: int) -> str:
        # 2. 将单词按要求进行反转
        # 确定本题使用的方法
        # 本题使用双指针法
        # 1. 双指针是同向还是异向 - 异向
        # 2. 双指针的用途是什么？
        # left 与 right 两个从外向内，完成对其位置的字母交换

        # 序列化
        s = list(s)

        while left <= right:
            tmp_word = s[left]
            s[left] = s[right]
            s[right] = tmp_word

            left += 1
            right -= 1
        
        s = ''.join(s)
        return s

    def reverseWords(self, s: str) -> str:
        # 确定本题基本的步骤
        
        
        # 确定本题是否有特殊的边界条件 - 暂无
        
        s = self.stripSpace(s)
        # 字符串长度
        length = len(s)
        # 进行第一次转置
        s = self.reverseString(s, 0, length - 1)
        # 起始索引
        start = 0
        # 对单词进行转置
        for end in range(length):
            # 如果遇到空格
            if s[end] == ' ':
                # 进行单词的转置
                s = self.reverseString(s, start, end - 1)
                # 重置起始索引
                start = end + 1
        
        # 将最后一个单词转置
        s = self.reverseString(s, start, length - 1)

        return s

def main():
    sl = Solution()
    # case 1
    s = "  the   sky   is   blue  "
    print(sl.reverseWords(s))

if __name__ == '__main__':
    main()
