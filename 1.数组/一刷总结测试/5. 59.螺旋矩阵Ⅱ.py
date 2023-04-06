from typing import *

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        # 确定本题使用方法
        # 本题是一个特殊的数组模拟题，并没有特定的方法
        # 模拟步骤分为两部分
        # 第一部分为循环执行的次数
        # 第二部分为步骤内的螺旋计算 此部分为循环不变量

        # 确定是否有边界情况
        # 如果是1个的情况下，那么直接输出一个即可
        if n == 1:
            return [[1]]

        # 循环执行次数如何设置
        # 此部分不仅仅为循环执行次数，如果是奇数的情况
        # 那么也是中间的值
        mid = int(n / 2)
        # 构建一个最基本的矩阵
        # 以下两者构建的列表都是同一内存地址
        # matrix =[[0] * n] * n
        # matrix = [[0 for _ in range(n)]] * n
        matrix = [[0] * n for _ in range(n)]

        # 起始边界
        start = 0
        # 终止边界
        end = n - 1
        # 计数器
        count = 1

        # 进行循环的计算
        # 这里为循环不变量
        for i in range(mid):
            # 从左到右
            for startY in range(start,end):
                matrix[start][startY] = count
                count += 1
            # 从上到下
            for startX in range(start,end):
                matrix[startX][end] = count
                count += 1
            # 从右到左
            for startY in range(end , start, -1):
                matrix[end][startY] = count
                count += 1
            # 从下到上
            for startX in range(end, start, -1):
                matrix[startX][start] = count
                count += 1
            start += 1
            end -= 1
        
        if n % 2 == 1:
            matrix[mid][mid] = count
        
        return matrix


def main():
    s = Solution()
    n = 3
    print(s.generateMatrix(3))
    n = 4
    print(s.generateMatrix(4))


if __name__ == '__main__':
    main()
