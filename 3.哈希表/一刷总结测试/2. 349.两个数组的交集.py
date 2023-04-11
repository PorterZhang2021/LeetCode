from typing import *

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # 确定本题使用的方法
        # 本题可以使用暴力法，但暴力法的执行效率为n^2
        # 本题可以采用哈希表，通过空间换时间
        # 确定是否有特殊的边界条件
        # 本题没有特殊边界的问题

        # 构建结果集
        result = []
        # 构建哈希验证集
        com_hash = {}

        # 进行元素的验证
        # 第一个部分进行哈希验证集的构建
        for num in nums1:
            # 直接构建即可
            com_hash[num] = 0
        
        # 第二个部分用来对哈希验证集进行验证
        for num in nums2:
            # 如果存在那么就将其置为1
            if com_hash.__contains__(num):
                com_hash[num] = 1
        
        # 将置为1的部分保存进列表
        for key, value in com_hash.items():
            if value == 1:
                result.append(key)
        
        # 返回交集
        return result

def main():
    s = Solution()
    # case 1
    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]
    print(s.intersection(nums1, nums2))
    # case 2
    nums1 = [4,9,5]
    nums2 = [9,4,9,8,4]
    print(s.intersection(nums1, nums2))

if __name__ == '__main__':
    main()