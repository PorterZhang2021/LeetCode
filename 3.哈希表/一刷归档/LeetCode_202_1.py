""" 
202.快乐数
编写一个算法来判断一个数 n 是不是快乐数。

「快乐数」 定义为：
对于一个正整数，
每一次将该数替换为它每个位置上的数字的平方和。
然后重复这个过程直到这个数变为 1，
也可能是 无限循环 但始终变不到 1。
如果这个过程 结果为 1，
那么这个数就是快乐数。
如果 n 是 快乐数 就返回 true ；
不是，则返回 false 。

这个题目的难点主要在于无限循环时候的判定，
因为无法确定到底什么情况下会变成1

这里要解决的问题是拆了位数之后再进行判断
如何拆位数
如果这个数大于0 循环条件
每次求余获得位数
每次除10减少一次位数
获取到计算的结果

存放计算的结果
将计算的结果重新赋值过去

此问题应该大数值的判断较少，所以很方便就过了

"""

class Solution:
    def isHappy(self, n: int) -> bool:
        # 用于存放循环后的数
        number_list = []
        number_list.append(n)

        # 无限循环
        while True:
            # 进行操作
            count = n
            n = 0
            # 如果数大于0
            while count > 0:
                # 每次求余获得个位数
                pos_num = count % 10
                # 新数值
                n += pos_num ** 2
                # 除法操作
                count = count // 10
            # 如果结果为1 那么返回True
            if n == 1:
                return True
            # 如果出现循环 返回false
            if n in number_list:
                return False
            # 存放数
            number_list.append(n)
        
