"""
344.反转字符串
编写一个函数，其作用是将输入的字符串反转过来。
输入字符串以字符数组 s 的形式给出。
不要给另外的数组分配额外的空间，
你必须原地修改输入数组、使用 O(1) 的额外空间解决这一问题。

边界指针法
设定一个左边界指针和一个右边界指针
每次交换两个边界指针的元素
交换结束后将两个边界指针往内收缩

"""

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # 左边界指针
        left = 0
        # 右边界指针
        right = len(s) - 1

        while left <= right:
            # 交换两个指针之间的元素
            s[left], s[right] = s[right], s[left]
            # 两个指针缩小边界
            left += 1
            right -= 1
        