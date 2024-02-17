"""
利用一个列表完成此问题
首先构建好字母哈希表
也就是说0-25分别代表a到z的字母
对于第一个字符串s，利用遍历的方式将其自增
对于第二个字符串t，利用遍历的方式将其自减
检查哈希表是否有不为零的，如果不为零就False
否则就True
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # 构建哈希字母表
        char = [0] * 26

        # # 哈希字母表初始化
        # for i in range(26):
        #     char.append(0)

        # 遍历第一个字符串s
        for ch in s:
            # 获取索引
            index = ord(ch) - ord('a')
            # 对应的位置自增一次
            char[index] += 1
        
        # 遍历第二个字符串t
        for ch in t:
            # 获取索引
            index = ord(ch) - ord('a')
            # 对应的位置自减一次
            char[index] -= 1
        
        # 遍历整个哈希字母表
        for i in range(26):
            # 如果出现有不等于0的情况
            if char[i] != 0:
                # 返回False
                return False
        
        # 返回True
        return True