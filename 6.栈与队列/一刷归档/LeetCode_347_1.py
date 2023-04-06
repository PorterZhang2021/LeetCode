""" 
前K个高频元素
给你一个整数数组 nums 和一个整数 k ，
请你返回其中出现频率前 k 高的元素。你可以按 任意顺序 返回答案。

这里需要使用到堆，也就是大顶堆或者小顶堆一类
此题涉及到三个内容：
1. 要统计元素的出现频率
2. 对频率排序
3. 找出前K个高频的元素


"""
from typing import *
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 要统计元素出现的频率
        _map = {}
        for i in range(len(nums)):
            _map[nums[i]] = _map.get(nums[i], 0) + 1
        
        # 对频率排序
        # 定义一个小顶堆，大小为k
        pri_que = []

        # 用固定大小为k的小顶堆，扫描所有频率的数值
        for key, freq in _map.items():
            heapq.heappush(pri_que, (freq, key))
            # 如果堆的大小大于K，则队列弹出
            # 保证堆的大小一直为k
            if len(pri_que) > k:
                heapq.heappop(pri_que)

        # 找出前K个高频元素，因为小顶堆先弹出的是最小的
        # 所以倒序来输出到数组
        result = [0] * k
        for i in range(k-1, -1, -1):
            result[i] = heapq.heappop(pri_que)[1]
        return result
    

def main():
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    s = Solution()
    print(s.topKFrequent(nums, k))


if __name__ == '__main__':
    main()