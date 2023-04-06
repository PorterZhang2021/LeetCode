"""
150. 逆波兰表达式求值
给你一个字符串数组 tokens ，表示一个根据 逆波兰表示法 表示的算术表达式。
请你计算该表达式。返回一个表示表达式值的整数。
注意：
有效的算符为 '+'、'-'、'*' 和 '/' 。
每个操作数（运算对象）都可以是一个整数或者另一个表达式。
两个整数之间的除法总是 向零截断 。
表达式中不含除零运算。
输入是一个根据逆波兰表示法表示的算术表达式。
答案及所有中间计算结果可以用 32 位 整数表示。

是否本身需要进行一个逆转？因为利用pop()取出的是最后一位的元素 -> 考虑到之前的方式，这里可以直接对list进行遍历就可以了

判定符号 
出现符号的情况 -> 
1. 取出栈中的两个元素
2. 判断是什么符号
3. 进行对应符号的运算

不是符号的情况 -> 将其放入其中
此代码除操作有问题 
"""

from typing import *

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
	    # 逆波兰表达式栈
        num_list = []

        for ch in tokens:
            # 如果是符号的情况下
            if ch in ['+', '-', '*', '/']:
                # 1. 取出栈中的两个元素
                num1 = num_list.pop()
                num2 = num_list.pop()
                # 交换两者 保证其运算顺序的正确 因为栈是逆序的
                num1, num2 = num2, num1
                # 2. 判断符号进行对应运算
                if ch == '+':
                    sum = num1 + num2
                elif ch == '*':
                    sum = num1 * num2
                elif ch == '-':
                    sum = num1 - num2
                elif ch == '/':
                    # 这里是有bug
                    # # 这里注意的是 两者负变正然后进行相除操作
                    # if num2 < 0:
                    #     sum = num1 // (-num2)
                    #     sum = -sum
                    # else:
                    #     # 这里使用整除
                    #     sum = num1 // num2

                    # 实际写法
                    sum = int(num1 / num2)
                # 3.存放新的数据
                num_list.append(sum)
            # 不是符号的情况
            else:
                num_list.append(int(ch))
        
        # 取出最后的元素
        num = num_list.pop()
        return num
                

def main():
    s = Solution()
    tokens = ["2","1","+","3","*"]
    print(s.evalRPN(tokens))
    tokens = ["4","13","5","/","+"]
    print(s.evalRPN(tokens))
    tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    print(s.evalRPN(tokens))
    tokens = ["4","-2","/","2","-3","-","-"]
    print(s.evalRPN(tokens))


if __name__ == '__main__':
	main()

