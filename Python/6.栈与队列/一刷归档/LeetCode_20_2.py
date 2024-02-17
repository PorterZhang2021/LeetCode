class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for item in s:
            # 左边元素匹配
            if item == '(':
                # 右边入栈
                stack.append(')')
            elif item == '[':
                stack.append(']')
            elif item == '{':
                stack.append('}')
            # 栈不为空 或者 不匹配
            elif not stack or stack[-1] != item:
                return False
            else:
                # 元素出栈
                stack.pop()
        
        return True if not stack else False

def main():
    s = Solution()
    s1 = s.isValid('()')
    s2 = s.isValid('()[]{}')
    s3 = s.isValid('(]')
    s4 = s.isValid('([)]')
    s5 = s.isValid('{[]}')

if __name__ == '__main__':
    main()