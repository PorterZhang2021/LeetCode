from typing import *

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # 本题使用双指针
        # 确定双指针是同向还是异向
        # 确定双指针的用途
        # 1. 使用同向双指针
        # 2. 一个指针为索引指针，另一个指针为遍历指针

        # 确定特殊边界情况
        # 如果数组为空的时候直接返回长度
        if not len(nums):
            return 0
        
        # 获取到整体的长度，后续需要用来进行遍历
        length = len(nums)
        # 索引指针
        index = 0

        # 利用for循环进行遍历 利用遍历指针遍历
        for cur in range(length):
            # 如果出现不等于val的情况
            if nums[cur] != val:
                # 将现在位置的值更改
                nums[index] = nums[cur]
                # 将索引指针加1
                index += 1

        # 输出最终的长度 = 索引指针 + 1 -> 此过程不需要
        # length = index + 1
        # 出现此问题的主要原因是因为索引指针最后还会自增一次，所以不需要我们自增了
        # 它直接变成了需要的数组长度
        length = index
        return length

def main():
    s = Solution()
    # case1
    nums = [3,2,2,3]
    val = 3
    print(s.removeElement(nums, val))
    # case2
    nums = [0,1,2,2,3,0,4,2]
    val = 2
    print(s.removeElement(nums, val))

if __name__ == '__main__':
    main()