from typing import *
import sys

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # 确定本题使用的方法
        # 本题使用方法为双指针 
        # 双指针为同向还是异向 - 异向
        # 双指针的用途：
        # 1. 先用指针判定整个满足目标值的大小
        # 2. 再用另一个指针对其不断缩小
        # 确定本题是否有边界条件情况
        # 边界条件就是不存在符合条件的子数组返回0
        
        # 长度
        length = len(nums)
        # 最小长度
        min_len = sys.maxsize
        # 总体的值
        total = 0
        # 起始索引指针
        start = 0

        # 用末尾索引指针来计算目标大小
        for end in range(length):
            # 将值进行累加
            total += nums[end]
            
            # 如果总体值大于等于目标的值
            # 那么就继续 这里就是用来验证最小数组的情况
            while total >= target:
                # 计算一下现在的长度大小
                aux_len = end - start + 1
                # 进行缩小
                total -= nums[start]
                # 起始索引增加
                start += 1
                if aux_len < min_len:
                    min_len = aux_len
                    min_start = start
                    min_end = end
        
        # 如果没有长度最小子数组
        if min_len == sys.maxsize:
            return 0
        else:
            return min_len


def main():
    s = Solution()
    target = 7
    nums = [2,3,1,2,4,3]
    print(s.minSubArrayLen(target, nums))
    target = 4
    nums = [1,4,4]
    print(s.minSubArrayLen(target, nums))
    target = 11
    nums = [1,1,1,1,1,1,1,1]
    print(s.minSubArrayLen(target, nums))

if __name__ == '__main__':
    main()