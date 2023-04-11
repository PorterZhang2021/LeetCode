from typing import *

class Solution:
    def reverseString(self, s: str, left: int, right: int) -> str:
        s = list(s)

        while left <= right:
            tmp_str = s[left]
            s[left] = s[right]
            s[right] = tmp_str
            
            left += 1
            right -= 1

        s = ''.join(s)
        
        return s

    def reverseLeftWords(self, s: str, n: int) -> str:
        # 左旋转字符串
        # 确定使用方法
        # 确定使用双指针法
        # 双指针法为同向还是异向 - 异向
        # 双指针法的用途是什么 - 用于替换两者的字符
        # 是否具有特殊的边界条件 - 暂无
        
        # 字符串长度
        length = len(s)
        # 整体进行一个逆置
        s = self.reverseString(s, 0, length - 1)
        # 对倒数k个的前面进行逆置
        s = self.reverseString(s, 0, length - n - 1)
        # 对倒数k个进行逆置
        s = self.reverseString(s, length - n, length - 1)
        return s


def main():
    sl = Solution()
    # case 1
    s = "abcdefg"
    k = 2
    print(sl.reverseLeftWords(s, k))
    # case 2
    s = "lrloseumgh"
    k = 6
    print(sl.reverseLeftWords(s, k))


if __name__ == '__main__':
    main()