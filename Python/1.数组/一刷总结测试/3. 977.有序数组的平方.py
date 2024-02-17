from typing import *


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # 确定使用方法
        # 1.本题使用双指针法
        # 双指针法使用同向还是异向
        # 双指针法使用异向
        # 双指针两者的用途
        # 用于索引两边的值进行比较
        # 大的部分存放，这里存放需要倒序存放，
        # 因此需要提前构建一个数组

        # 确定是否具有边界问题
        # 如果数组为空直接返回
        # 如果数组为一个值 那么直接返回2倍的情况

        # 边界问题处理
        # 数组为空
        if not len(nums):
            return nums
        # 数组只有一个值
        if len(nums) == 1:
            # 直接将其进行平方返回
            nums[0] = nums[0] ** 2
            return nums
        
        # 其余情况
        # 起始索引位置
        left = 0
        # 终止索引位置
        right = len(nums) - 1
        # 构建一个用于存放的平方数组
        double_nums = [0] * len(nums)
        # 构建一个索引
        index = len(nums) - 1
        
        # 进行比较 这里的边界设定为index大于等于0
        # 因为数组本身有0下标
        while index >= 0:
            # 进行比较
            # 获取两边的值并平方
            left_nums = nums[left] ** 2
            right_nums = nums[right] ** 2
            # 如果左边的值大
            if left_nums > right_nums:
                # 存放左边的值
                double_nums[index] = left_nums
                # 左边的索引自增一次
                left += 1
            else:
                # 否则就是右边的值大
                double_nums[index] = right_nums
                # 右边索引递减一次
                right -= 1
            
            # 每次递减
            index -= 1
        # 输出最终获得的数组
        return double_nums


def main():
    s = Solution()
    # case1
    nums = [-4,-1,0,3,10]
    print(s.sortedSquares(nums))
    # case2
    nums = [-7,-3,2,3,11]
    print(s.sortedSquares(nums))


if __name__ == '__main__':
    main()