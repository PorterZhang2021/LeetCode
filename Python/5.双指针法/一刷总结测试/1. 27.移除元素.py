from typing import *

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # 确定本题使用的方法
        # 双指针法
        # 确定使用本方法是同向还是异向 - 同向
        # 确定双指针的用途
        # cur用于进行遍历
        # index用于进行值的修改
        # 这里要记住index最后的长度为数组的最终的长度
        # 确定本题是否有特殊的边界条件 - 暂无
        
        # 起始索引
        index = 0
        for cur in range(len(nums)):
            # 如果不等于这个值
            if nums[cur] != val:
                # 将值保存进数组
                nums[index] = nums[cur]
                # 索引自增
                index += 1
            
        # 最终长度
        length = index
        return length


def main():
    sl = Solution()
    # case 1
    nums = [3,2,2,3]
    val = 3
    print(sl.removeElement(nums, val))
    # case 2
    nums = [0,1,2,2,3,0,4,2]
    val = 2
    print(sl.removeElement(nums, val))

if __name__ == '__main__':
    main()