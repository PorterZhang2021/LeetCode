from typing import *

class Solution:
    def stripSpace(self, s: str) -> str:
        # 确定是否具有边界条件 - 本题暂无边界条件
        s = list(s)
        new_str = []
        length = len(s)
        start = 0
        # 默认为True
        flag = True
        for end in range(length):
            # 如果值为空且标志位为true
            if s[end] == ' ' and flag == True:
                new_str.append(s[end])
                start += 1
                # 标志位重置
                flag = False
            elif s[end] == ' ' and flag == False:
                continue
            else:
                new_str.append(s[end])
                # 标志位重置
                flag = True
        
        # 获取新的长度
        # 剔除两边的空格
        if new_str[0] == ' ':
            new_str.pop(0)
        if new_str[len(new_str) - 1] == ' ':
            new_str.pop()

        new_str = ''.join(new_str)

        return new_str
    
    def reverString(self, s: str, left: int, right: int) -> str:
        # 序列化
        s = list(s)
        # 双指针法 - 异向 - 用于确定起始索引与终止索引 - 交换元素

        while left <= right:
            tmp_str = s[left]
            s[left] = s[right]
            s[right] = tmp_str
            # 索引变更
            left += 1
            right -= 1
        
        s = ''.join(s)
        return s
    
    def reverseWords(self, s: str) -> str:
        # 确定本题使用的方法
        # 本题使用两次双指针的方法
        # 确定双指针是同向还是异向 - 同向
        # 确定双指针的用途 - 用于进行索引的遍历，构建新的单词
        
        # 剔除空格
        s = self.stripSpace(s)
        # 进行一次整体逆置
        s = self.reverString(s, 0, len(s) - 1)
        start = 0 
        for end in range(len(s)):
            if s[end] == ' ':
                left = start
                right = end - 1
                s = self.reverString(s, left, right)
                start = end + 1
        # 最后一次逆转
        s = self.reverString(s, start, len(s) - 1)
        # 返回值
        return s
        

def main():
    sl = Solution()
    s = "  the  sky  is  blue  "
    print(sl.reverseWords(s))

if __name__ == '__main__':
    main()