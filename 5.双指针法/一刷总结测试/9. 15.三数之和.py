from typing import *

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 三数之和
        # 确定本题的使用方法
        # 本题需要使用哈希表 + 双指针
        # 双指针是同向还是异向 - 同向
        # 双指针的用途是什么？
        # 双指针用于遍历
        # 确定是否具有特殊的边界条件 - 暂无
        # 结果集
        result = [[]]
        # 整体排序
        nums = sorted(nums)
        # 用于存放长度
        length = len(nums)
        # 对整体进行遍历
        for i in range(length):
            # 如果出现大于0的情况
            if nums[i] > 0:
                # 直接返回结果
                return result
            # 去重逻辑
            if i > 0 and nums[i] == nums[i-1]:
                continue
            # 左索引指针
            left = i + 1
            # 右索引指针
            right = length - 1
            # 如果右指针大于左指针
            while right > left:
                # 如果相加的值大于0 那么就调整右指针
                if nums[i] + nums[left] + nums[right] > 0:
                    right -= 1
                # 如果相加的值小于0 那么就调整左指针
                elif nums[i] + nums[left] + nums[right] < 0:
                    left += 1
                else:
                    # 等于0的情况下就将值入栈
                    result.append([nums[i], nums[left], nums[right]])
                    # 此部分为对b与c进行去重
                    while right > left and nums[right] == nums[right - 1]:
                        right -= 1
                    while right > left and nums[left] == nums[left + 1]:
                        left += 1
                    # 找到答案后进行收缩
                    right -= 1
                    left += 1

        return result

def main():
    pass

if __name__ == '__main__':
    main()