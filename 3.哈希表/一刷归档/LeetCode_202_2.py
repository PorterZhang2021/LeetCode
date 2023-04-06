"""
202.快乐数
这里的循环判断主要是判断构建的数
是否已经出现在集合元素当中了
利用集合元素的好处就是能够省一定的空间
"""

class Solution:
    def isHappy(self, n: int) -> bool:
        # 构建快乐数
        def calculate_happy(num):
            _sum = 0

            # 从个位数取值，依次平方求和
            while num:
                _sum += (num % 10) ** 2
                num = num // 10

            return _sum
        
        # 记录中间结果
        record = set()

        # 无限循环
        while True:
            n = calculate_happy(n)
            # 如果为1的情况下是快乐数
            if n == 1:
                return True

            # 如果中间结果重复出现，说明陷入死循环
            # 这个时候不是快乐数
            if n in record:
                return False
            else:
                record.add(n)