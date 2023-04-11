from typing import *

class Solution:
    def removeDuplicates(self, s: str) -> str:
        # 确定本题的使用方法
        # 本题使用栈
        # 确定本题是否具有特殊边界 - 暂无
        
        # 构建一个元素栈
        character_stack = []
        # 字符串序列化
        s = list(s)

        for ch in s:
            # 如果栈不为空
            if len(character_stack) > 0:
                # 将一个元素移出
                character = character_stack.pop()
                # 移出元素后比对
                if character == ch:
                    continue
                else:
                    # 将两个不相同的元素放入
                    character_stack.append(character)
                    character_stack.append(ch)
            else:
                # 添加元素
                character_stack.append(ch)
                    
        # 将最后栈内的元素重新组合
        s = ''.join(character_stack)
        return s


def main():
    sl = Solution()
    # case 1
    s = "abbaca"
    print(sl.removeDuplicates(s))

if __name__ == '__main__':
    main()
