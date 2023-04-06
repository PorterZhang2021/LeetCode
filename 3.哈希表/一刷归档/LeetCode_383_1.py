"""
383.赎金信
给你两个字符串：ransomNote 和 magazine ，
判断 ransomNote 能不能由 magazine 里面的字符构成。
如果可以，返回 true ；否则返回 false 。
magazine 中的每个字符只能在 ransomNote 中使用一次。

此问题实际上是有效的字母异位词的一个翻版问题，
解决此问题的办法很简单，那就是用magazine构建一个字母的哈希表，每次递增
然后将ransomNote的值匹配，每次递减
最后查看到字母哈希表如果出现有负数的情况那么就代表没有构成成功
否则就构成成功了
"""

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # 构建字母哈希表
        char_list = [0] * 26

        # 将magazine数组内的字母 自增存放
        for ch in magazine:
            # 获得字母的索引
            index = ord(ch) - ord('a')
            # 存入字母哈希表
            char_list[index] += 1

        # 将ransomNote数组内的字母 自减存放
        for ch in ransomNote:
            # 获得字母的索引
            index = ord(ch) - ord('a')
            # 减少字母哈希表
            char_list[index] -= 1

        # 判断是否有负值
        for num in char_list:
            if num < 0:
                return False
        
        return True