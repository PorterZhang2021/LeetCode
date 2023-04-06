"""
1.两数之和
代码随想录版本
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 字典
        records = dict()

        # 列举
        for index, value in enumerate(nums):
            # 遍历当前元素，并在map中寻找是否有匹配的key
            if target - value in records:
                return [records[target-value], index]
            
            # 遍历当前元素，并在map中寻找是否有匹配的key
            records[value] = index
        
        return []