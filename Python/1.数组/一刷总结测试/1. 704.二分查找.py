from typing import *

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 本题需要考虑到循环不变量，即循环时不能更改区间情况
        # 如果是左闭右开，那么后面依然是左闭右开

        # 找得到
        # 左 中 右
        # 左为起始索引
        # 右为终止索引
        # 中间为进行比对的值

        left = 0
        right = len(nums) - 1
        

        # 进行比对
        while left <= right:
            mid = int(right - left / 2)
            # 如果目标值大于获取值
            if target > nums[mid]:
                # 更改起始索引位置
                left = mid + 1
            # 如果目标值小于获取值
            elif target < nums[mid]:
                # 缩小终止索引位置
                right = mid - 1
            # 剩余为相等情况 返回索引
            else:
                return mid

        # 找不到返回-1
        return -1
        

def main():
    s = Solution()
    # case1
    nums = [-1,0,3,5,9,12]
    target = 9
    print(s.search(nums, target))
    # case2
    nums = [-1,0,3,5,9,12]
    target = 2
    print(s.search(nums, target))

if __name__ == '__main__':
    main()