"""
20. 有效的括号
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
每个右括号都有一个对应的相同类型的左括号。

利用栈来解决此问题 - 上面的思路是错误的
将元素一个个入栈，入栈后对元素进行匹配
入栈只入栈前一半
如果为奇数 那么直接就是非有效字符串
如果是偶数
1. 前一半先入栈
2. 取出一个元素 判断是否与其匹配 如果匹配那么继续
    不匹配那么就说明是非有效的

# 取出栈内元素
# 栈内元素是否匹配， 匹配那么两个都取出，不匹配那么存入元素 直到所有的都结束
# 如果结束了还有元素，那么就为false 否则为true

这里的栈可以使用list进行模拟 
"""

class Solution:
    def isValid(self, s: str) -> bool:
        # 转换成list
        str1_list = list(s)
        # 栈
        str2_list = []

        # 进行检验
        while len(str1_list) > 0:
            # 判断栈中是否有元素
            if len(str2_list) > 0:
                # 栈内有元素
                # 取出元素
                ch1 = str1_list.pop()
                ch2 = str2_list.pop()
                # 如果ch1与ch2两者匹配
                if ch1 == '(' and ch2 == ')':
                    continue
                elif ch1 == '[' and ch2 == ']':
                    continue
                elif ch1 == '{' and ch2 == '}':
                    continue
                else:
                    # ch2与ch1入栈
                    str2_list.append(ch2)
                    str2_list.append(ch1)
            else:
                # 栈内无元素
                str2_list.append(str1_list.pop())

        
        # 最终检验 为空则为true
        return len(str2_list) == 0

def main():
    s = Solution()
    flag = s.isValid('()[]{}')
    print(flag)


if __name__ == '__main__':
    main()