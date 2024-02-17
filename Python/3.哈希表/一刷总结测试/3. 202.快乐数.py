from typing import *

class Solution:
    def divide_sum(self, nums):
        result = 0
        # 如果不为0那么就继续
        while nums:
            # 获取个位数
            divide = nums % 10
            # 对结果位数进行添加
            result = result + divide ** 2
            # 减少位数
            nums = nums // 10
        # 返回结果
        return result
    
    def isHappy(self, n: int) -> bool:
        # 确定本题的使用方法
        # 本题使用方法并未想到如何使用哈希法
        # 后续做题后发现，此部分使用哈希法
        # 哈希法的部分在于对结果集的验证
        # 本题主要部分为一个数的组合与重置
        # 确定是否有特殊的边界情况
        # 此题可能有一个特殊情况，为1，本身应该就是快乐数
        if n == 1:
            return True
        # 这里需要构建一个用于进行除法计算的部分
        # 存放结果的部分 
        result_list = [n]
        # 初始化的result
        result = n

        # 进行循环验证
        while True:
            # 获取结果
            result = self.divide_sum(result)
            # 如果结果出现了1，那么就是快乐数
            if result == 1:
                return True
            
            # 验证结果情况，如果两者相等
            # 那么就说明循环了，不是快乐数
            # 这个部分需要对整体的空间进行验证
            if result in result_list:
                return False
            
            # 将获取到的结果放入结果集
            result_list.append(result)

def main():
    s = Solution()
    n = 19
    print(s.isHappy(n))
    n = 2
    print(s.isHappy(n))

if __name__ == '__main__':
    main()
