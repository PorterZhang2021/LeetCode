"""
15.三数之和
给你一个整数数组 nums ，
判断是否存在三元组 [nums[i], nums[j], nums[k]] 
满足 i != j、i != k 且 j != k ，
同时还满足 nums[i] + nums[j] + nums[k] == 0 。请
你返回所有和为 0 且不重复的三元组。

注意：答案中不可以包含重复的三元组。

本题有个要求就是 3个值不相等 那就是说明整数数组里面的元素不能重用，具有唯一性，
这里的唯一性说的是索引使用唯一

接下来完成的就是3个索引形成的值为0

"""


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 结果集
        ans = []
        # 长度
        n = len(nums)
        # 对数组排序
        nums.sort()

        # 找出a+b+c=0
        # a = nums[i], b = nums[left], c = nums[right]
        for i in range(n):
            # 左
            left = i + 1
            # 右
            right = n - 1
            # 排序后如果第一个元素已经大于零，那么无论如何组合都不可能
            # 凑成三元素，直接返回结果就可以了
            if nums[i] > 0:
                break
            # 如果i大于等于1 并且 两个索引的值相同 去重
            if i >= 1 and nums[i] == nums[i - 1]:
                continue
            # 组合三数之和
            while left < right:
                # 总值
                total = nums[i] + nums[left] + nums[right]
                # 三数之和大于0
                if total > 0:
                    # 移动右边界
                    right -= 1
                # 三数之和小于0
                elif total < 0:
                    # 移动左边界
                    left += 1
                # 否则
                else:
                    # 将元素放入
                    ans.append([nums[i], nums[left], nums[right]])
                    # 去重逻辑因该放在找到一个三元组之后，对b和c去重
                    while left != right and nums[left] == nums[left + 1]:
                        left += 1
                    while left != right and nums[right] == nums[right - 1]:
                        right -=1
                    left += 1
                    right -= 1
        
        return ans