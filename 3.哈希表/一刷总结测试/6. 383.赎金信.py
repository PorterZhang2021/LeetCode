from typing import *

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # 确定本题使用的方法
        # 本题是一种包含题，要保证magazine包含ransomNote的所有字母
        # 确定是否具有特殊的边界条件
        # 字母集
        character_dict = {}
        # 将所有的值存入字母集中
        for ch in magazine:
            # 如果字母集中key存在
            if character_dict.__contains__(ch):
                # 字母集增加1
                character_dict[ch] += 1
            else:
                character_dict[ch] = 1
        # 计算字符情况
        for ch in ransomNote:
            # 如果字母集中key存在
            if character_dict.__contains__(ch):
                # 字母集减少
                character_dict[ch] -= 1
                if character_dict[ch] < 0:
                    return False
            else:
                return False
        
        # 剩余情况即为都满足的结果
        return True


def main():
    s = Solution()
    # case 1
    ransomNote = "a"
    magazine = "b"
    print(s.canConstruct(ransomNote, magazine))
    # case 2
    ransomNote = "aa"
    magazine = "ab"
    print(s.canConstruct(ransomNote, magazine))
    # case 3
    ransomNote = "aa"
    magazine = "aab"
    print(s.canConstruct(ransomNote, magazine))

if __name__ == '__main__':
    main()
