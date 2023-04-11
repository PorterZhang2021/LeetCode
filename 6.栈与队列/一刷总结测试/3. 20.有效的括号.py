from typing import *

class Solution:
    def isValid(self, s: str) -> bool:
        # 确定本题的使用方法
        # 本题需要使用栈
        # 确定是否有特殊的边界条件 - 暂无

        # 步骤
        # 将元素入栈
        # 构建一个符号栈
        sign_stack = []
        # 将字符串列表化
        s = list(s)

        # 进行入栈操作
        for ch in s:
            # 如果是(, {, [ 就进行入栈操作
            if ch == '(' or ch == '{' or ch == '[':
                # 将符号入栈
                sign_stack.append(ch)
            # 其余情况进行出栈
            else:
                # 如果此部分出现为空的情况直接返回False
                if len(sign_stack) == 0:
                    return False
                
                # 元素间的比较
                left_sign = sign_stack.pop()    
                # 进行配对
                if left_sign == '(' and ch == ')':
                    continue
                elif left_sign == '{' and ch == '}':
                    continue
                elif left_sign == '[' and ch == ']':
                    continue
                else:
                    # 如果匹配那么就返回False
                    return False
        
        
        
        # 返回最后的true和false的情况
        # 如果栈为空那么返回True否则返回False
        if len(sign_stack) == 0:
            return True
        else:
            return False


def main():
    sl = Solution()
    # case 1
    s = "()"
    print(sl.isValid(s))
    # case 2
    s = "()[]{}"
    print(sl.isValid(s))
    # case 3
    s = "(]"
    print(sl.isValid(s))


if __name__ == '__main__':
    main()