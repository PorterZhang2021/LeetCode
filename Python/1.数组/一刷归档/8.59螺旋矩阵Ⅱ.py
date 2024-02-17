"""
59.螺旋矩阵Ⅱ
给你一个正整数 n ，
生成一个包含 1 到 n2 所有元素，
且元素按顺时针顺序螺旋排列的 n x n 正方形矩阵 matrix 。

此问题是给了一个数 n
然后用这个数来进行数组的生成

数组螺旋问题
两个循环 - 交替运行？ - 因此这个操作并不对
一个用来控制行
一个用来控制列

对数组进行计算
1 [0][0]

2   1 [0][0] 2[0][1]
    4 [1][0] 3[1][1]

3   1[0][0] 2[0][1] 3[0][2]
    8[1][0] 9[1][1] 4[1][2]
    7[2][0] 6[2][1] 5[2][2]

4   1   2   3   4
    12  13  14  5
    11  16  15  6
    10  9   8   7

此类问题属于数组模拟问题 考虑4个部分的边界的问题
其实是一个正方形
起点          点1
终点          点2

分成两个步骤
外面的步骤控制正方形缩圈
缩圈时改动的部分
移动的额度 offset
x的起始边界
y的起始边界
里面的步骤控制正方形的四条边
每条边注意起始位置的更改
横向 改变 列数 增加
竖向 改变 行数 增加
横向 改变 列数 减少
竖向 改变 行数 减少

本题同样遵循循环不变量原则，及每次循环后不改动其区间的可能性。

"""

from typing import *

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        # 构造矩阵 利用迭代器进行构造
        nums = [[0] * n for _ in range(n)]
        # 起始点
        startx, starty = 0, 0
        # 迭代次数，n为 奇数时，矩阵的中心点
        loop, mid = n // 2, n // 2
        # 计数
        count = 1

        # 每循环一层偏移量加1，偏移量从1开始
        for offset in range(1, loop + 1):
            # 从左到右，左闭右开 循环不变量
            for i in range(starty, n - offset):
                nums[startx][i] = count
                # 自增一次
                count += 1
            # 从上到下
            for i in range(startx, n - offset):
                nums[i][n - offset] = count
                count += 1
            # 从右到左
            for i in range(n - offset, starty, -1):
                nums[n - offset][i] = count
                count += 1
            # 从下到上
            for i in range(n - offset, startx, -1):
                nums[i][starty] = count
                count += 1
            
            # 更新起始点
            startx += 1
            starty += 1

        # n为奇数时，填充中心点
        if n % 2 != 0:
            nums[mid][mid] = count
        
        return nums
                



if __name__ == "__main__":
    # 创建实例类
    test = Solution()
    print(test.generateMatrix(3))

