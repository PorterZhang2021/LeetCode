"""
27.移除元素

给你一个数组 nums 和一个值 val，你需要 原地 移除所有数值等于 val 的元素，并返回移除后数组的新长度。

不要使用额外的数组空间，你必须仅使用 O(1) 额外空间并 原地 修改输入数组。

元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。

此题移除数组题目，有点类似于实现线性表的删除功能

暴力解法 -> 貌似有问题
如果我访问数组的时候遇到了val值 -> 循环，查找所有的val值
那么我就要开始一个循环
这个循环的功能是从val值的索引开始，把所有值往前递进一格
完成后数组长度-1 -> 提前要获取数组长度

如果一道题目直接用库函数就可以解决
那么就不使用库函


"""

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # 获取数组长度
        length = len(nums)

        # 获取数组下标
        for i in range(length):
            # 判断是否有等于val值的元素
            if nums[i] == val:
                #从此开始进行平移
                for j in range(i + 1, length):
                    # 进行平移
                    nums[j - 1] = nums[j]
                # 长度减1
                length = length - 1
                # i减1
                i -= 1

        return length