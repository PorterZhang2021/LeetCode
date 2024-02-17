from typing import *

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 确定使用哪个方法
        # 确定使用双指针
        # 两个指针方向为同向还是异向-同向
        # 两个指针的用途 
        # 用于遍历，一个指针用于固定一个索引
        # 另一个指针用于对后续的值进行遍历
        # 确定是否有边界条件
        # 边界条件情况下未知
        # 结果集
        result_dict = {}
        # 双指针
        # 慢指针用于固定一个值
        # 滑动窗口一题最终结果为O(n)
        # 那么这里的结果是不是也是O(n^2)
        for slow in range(len(nums) - 1):
            result = 0
            # 快指针用于对其他情况遍历
            # 这个部分要注意到左闭右开的问题
            # 因此是slow + 1
            for fast in range(slow+1, len(nums)):
                # 计算其结果
                result = nums[slow] + nums[fast]
                # 将结果存入结果集中
                result_dict[result] = [slow, fast]
        
        # 对结果进行验证
        for key in result_dict.keys():
            if key == target:
                return result_dict[key]



def main():
    s = Solution()
    # case 1
    nums = [2,7,11,15]
    target = 9
    print(s.twoSum(nums, target))
    # case 2
    nums = [3,2,4]
    target = 6
    print(s.twoSum(nums, target))
    # case 3
    nums = [3,3]
    target = 6
    print(s.twoSum(nums, target))

if __name__ == '__main__':
    main()