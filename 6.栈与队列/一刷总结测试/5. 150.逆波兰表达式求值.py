from typing import *

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # 确定本题的操作方法
        # 本题需要进行栈的操作
        # 确定本题是否具有边界条件
        # 特殊边界条件 假如只有一个值的情况，那么这个时候直接转换成int

        # 元素栈
        character_stack = []

        # 对元素进行入栈操作
        for ch in tokens:
            # 如果是+、-、*、/
            # 如果是加法
            if ch == '+' or ch == '-' or ch == '*' or ch == '/':
                # 进行两次出栈 - 先出栈的为后一个
                num2 = int(character_stack.pop())
                num1 = int(character_stack.pop())
                # 进行元素计算
                if ch == '+':
                    num = num1 + num2
                elif ch == '-':
                    num = num1 - num2
                elif ch == '*':
                    num = num1 * num2
                elif ch == '/':
                    num = int(num1 / num2)
                # 将值重新存入进去
                character_stack.append(num)
            else:
                character_stack.append(ch)
        num = int(character_stack.pop())
        # 输出最后的结果
        return num

def main():
    sl = Solution()
    # case 1
    tokens = ["2","1","+","3","*"]
    print(sl.evalRPN(tokens))
    # case 2
    tokens = ["4","13","5","/","+"]
    print(sl.evalRPN(tokens))
    # case 3
    tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    print(sl.evalRPN(tokens))

if __name__ == '__main__':
    main()