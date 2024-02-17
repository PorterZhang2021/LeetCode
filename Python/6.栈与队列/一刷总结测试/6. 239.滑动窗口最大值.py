from typing import *
import sys

class Solution:
    def get_max(self, nums: List[int]) -> int:
        max_num = -sys.maxsize
        for num in nums:
            if max_num < num:
                max_num = num
        return max_num
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # 确定本题的使用方法
        # 本题使用队列实现先进先出
        # 确定本题是否具有边界情况
        # 如果只有一个元素的时候且k=1时那么直接输出
        if len(nums) == 1 and k == 1:
            return nums
        
        # 元素队列
        nums_queue = []
        # 结果集
        result = []
        # 如果本身就小于k，那么直接找出最大值
        if len(nums) < k:
            max_num = self.get_max(nums)
            result.append(max_num)
        else:
            for num in nums:
                # 首次进值
                if len(nums_queue) != k:
                    nums_queue.append(num)
                    continue
                # 找出队列中的最大值
                max_num = self.get_max(nums_queue)
                # 队列出队与入队
                nums_queue.pop(0)
                nums_queue.append(num)
                # 存放结果集
                result.append(max_num)
            # 找出队列中的最大值
            max_num = self.get_max(nums_queue)
            # 存放结果集
            result.append(max_num)
        # 输出最后的结果集
        return result

def main():
    sl = Solution()
    # case 1
    nums = [1,3,-1,-3,5,3,6,7]
    k = 3
    print(sl.maxSlidingWindow(nums, k))

if __name__ == '__main__':
    main()
