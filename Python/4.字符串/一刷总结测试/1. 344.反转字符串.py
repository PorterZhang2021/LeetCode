from typing import *

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # 确认本题使用的方法
        # 本题使用双指针法
        # 确定双指针是同向还是异向 - 异向
        # 确定双指针的用途 - 用于进行双方的元素置换
        # 是否具有特殊的边界条件 - 本题特殊边界条件暂无
        
        # 左起始索引
        left = 0
        # 右终止索引
        right = len(s) - 1

        # 使用双指针要注意循环不变量
        while left <= right:
            # 将左边的元素先临时存放
            tmp_str = s[left]
            # 置换元素
            s[left] = s[right]
            s[right] = tmp_str
            # 左右指针进行移动
            left += 1
            right -= 1
        


def main():
    sl = Solution()
    # case 1
    s = ["h","e","l","l","o"]
    print(sl.reverseString(s))
    # case 2
    s = ["H","a","n","n","a","h"]
    print(sl.reverseString(s))


if __name__ == '__main__':
    main()