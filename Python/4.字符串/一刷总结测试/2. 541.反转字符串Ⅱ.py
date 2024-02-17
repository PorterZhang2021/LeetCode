from typing import *

class Solution:
    @staticmethod
    def reverString(self, s:list, left: int, right: int) -> list:
        # 双指针法
        # 左部分为起始
        # 右部分为终止
        while left <= right:
            tmp_str = s[left]
            s[left] = s[right]
            s[right] = tmp_str
            left += 1
            right -= 1
        
        return s
        
    def reverseStr(self, s: str, k: int) -> str:
        # 给定一个字符串s
        # 一个整数k
        # 每计数2k就反转前k个
        # 少于k个则剩余部分全部反转
        # 剩余小于2k但大于或等于k个，则反转前k个字符

        # 确定使用方法
        # 确定使用双指针法
        # 双指针的方法是同向还是异向 - 异向
        # 双指针的用途是什么 - 用于置换元素
        # 确定是否有特殊的边界情况 - 暂无
        
        s = list(s)
        # 获取长度
        length = len(s)
        # 每次步进2k的值
        for start in range(0, length, 2 * k):
            if start + k > length:
                end = length - 1
            else:
                end = start + k - 1
            # 进行结果的逆置
            self.reverString(self, s, start, end)
        s = ''.join(s)

        return s

def main():
    sl = Solution()
    # case 1
    s = "abcdefg"
    k = 2
    print(sl.reverseStr(s, k))
    # case 2
    s = "abcd"
    k = 2
    print(sl.reverseStr(s, k))
    # case 3
    s = "abcdefg"
    k = 8
    print(sl.reverseStr(s, k))
    # case 4
    s = "abcdefg"
    k = 4
    print(sl.reverseStr(s, k))


if __name__ == '__main__':
    main()