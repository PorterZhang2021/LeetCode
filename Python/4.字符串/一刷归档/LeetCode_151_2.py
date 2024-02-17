"""
151.反转字符串里面的单词
不使用辅助空间，空间复杂度要求为O(1)
解题思路：
1. 移除多余空格
2. 将整个字符串反转
3. 将每个单词反转

1. 移除多余空格部分 可以改造使用27.移除元素的方法
快指针：快指针移动
慢指针：慢指针更新索引坐标

"""

class Solution:
    # 1. 去除多余的空格
    def trim_spaces(self, s):
        n = len(s)
        left = 0
        right = n - 1

        # 去除开头的空格
        while left <= right and s[left] == ' ':
            left += 1
        # 去除结尾的空格
        while left <= right and s[right] == ' ':
            right -= 1
        
        # 临时存放
        tmp = []
        
        # 去除单词中间多余的空格
        while left <= right:
            if s[left] != ' ':
                tmp.append(s[left])
            # 当前位置是空格
            # 但相邻的上一个位置不是空格
            # 则该空格是合理的
            elif tmp[-1] != ' ':
                tmp.append(s[left])
            left += 1
        return tmp
    
    # 反转字符数组
    def reverse_string(self, nums, left, right):
        # 边界指针法
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        return None

    # 翻转每个单词
    def reverse_each_word(self, nums):
        # 起始
        start = 0
        # 结束
        end = 0
        n = len(nums)
        # 开始到n
        while start < n:
            # 结束到n 并且 最后一个不是空格
            while end < n and nums[end] != ' ':
                end += 1
            # 进行翻转
            self.reverse_string(nums, start, end-1)
            start = end + 1
            # 去除空格
            end += 1
        return None
    # 4. 翻转字符串里的单词
    def reverseWords(self, s):
        l = self.trim_spaces(s)
        self.reverse_string(l, 0, len(l) - 1)
        self.reverse_each_word(l)
        return ''.join(l)

# 测试
def main():
    s = Solution()
    print(s.reverseWords("  hello world  "))

if __name__ == '__main__':
    main()
