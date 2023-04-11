from typing import *

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # 确定本题方法
        # 本题可以采用暴力法，此时时间复杂度较高
        # 本题利用哈希表，可以减少时间复杂度
        # 是否有特殊的边界条件
        # 无 - 这里没有思考到位
        # 由于测试用例的情况，没有思考到两个字符串
        # 数量不相等的情况

        # 构建一个存放字母的字典
        str_dict = {}
        # 进行第一次循环，此时循环为增加值
        for ch in s:
            # 如果字典中存在那么就+1
            if str_dict.__contains__(ch):
                str_dict[ch] += 1
            else:
                # 这里要注意初始的情况下就要为1了
                # 因为这里验证出结果了
                str_dict[ch] = 1
        
        # 进行第二次循环，此时循环用来验证情况
        for ch in t:
            # 如果字典中存在那么就减少1
            if str_dict.__contains__(ch):
                str_dict[ch] -= 1
                # 如果减少后小于0那么就说明false
                if str_dict[ch] < 0:
                    return False
            else:
                # 如果字典中没有此字母，那么直接返回false
                return False
        # 本题验证时有个特殊情况要验证
        # 那么就是如果一个字母比另一个字母少
        # 那么字典中会有多出来的值
        for value in str_dict.values():
            # 这里只需要对值进行验证即可
            if value != 0:
                return False
        # 如果没有出现被移除的情况，那么就返回true
        return True


def main():
    s = Solution()
    # case 1
    s_str = "anagram"
    t_str = "nagaram"
    print(s.isAnagram(s_str, t_str))
    # case 2
    s_str = "rat"
    t_str = "car"
    print(s.isAnagram(s_str, t_str))


if __name__ == '__main__':
    main()