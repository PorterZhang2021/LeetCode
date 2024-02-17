"""
双指针操作
此题可以利用快慢指针进行操作来解题
与其有操作有点类似的是选择排序，但内部核心还是有所不同
这里用于类比

此题实际上的方式是，构建两个指针
而我们需要的就是对指针操作
快指针，慢指针

快指针的值只有当其不等于val时会进行更改，更改的操作是：
    将快指针的值赋值给慢指针
    慢指针自增一次

最后慢指针的值+1就是数组的长度
"""

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        # 慢指针
        low = 0

        # 快指针运行
        for fast in range(len(nums)):
            # 如果快指针的值与val不等
            if nums[fast] != val:
                # 将快指针的值赋值给慢指针
                nums[low] = nums[fast]
                # 慢指针自增
                low += 1

        # 返回长度
        return low + 1