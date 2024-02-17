from typing import *

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # 确定本题使用方法
        # 本题使用双指针法
        # 双指针为同向还是异向 - 异向
        # 双指针的用途是什么
        # 左指针用于从起始索引向终止索引遍历
        # 右指针用于从终止索引向起始索引遍历
        # 每次遍历交换两者的值
        # 确定是否具有特殊的边界条件
        # 本题暂无

        left = 0
        right = len(s) - 1

        # 进行遍历循环
        while left <= right:
            tmp_str = s[left]
            s[left] = s[right]
            s[right] = tmp_str
            # 向内缩进
            left += 1
            right -= 1
        
        return s

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