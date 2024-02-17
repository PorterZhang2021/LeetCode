"""
1047. 删除字符串中的所有相邻重复项
给出由小写字母组成的字符串 S，
重复项删除操作会选择两个相邻且相同的字母，
并删除它们。

在 S 上反复执行重复项删除操作，
直到无法继续删除。

在完成所有重复项删除操作后返回最终的字符串。
答案保证唯一。

这个匹配操作题目同上一题我自己使用的方法类似
只不过这一题可能需要更加的抽象化
之前只是对括号匹配这里是只要两者相同就算匹配成功

"""

class Solution:
    def removeDuplicates(self, s: str) -> str:
        # 将其转化成列表形式 -> 以列表来模拟栈
        str1_list = list(s)
        # 设置一个空栈
        str2_list = []

        # 如果字母不为空的情况下 那么我们可以继续进栈
        while len(str1_list) > 0:
            # 取出字母元素
            ch1 = str1_list.pop()
            # 如果栈不为空
            if len(str2_list) > 0:
                # 取出元素
                ch2 = str2_list.pop()
                # 如果两个元素相等
                if ch1 == ch2:
                    # 继续
                    continue
                # 不等
                else:
                    # 将两个元素一起存入
                    str2_list.append(ch2)
                    str2_list.append(ch1)
            # 如果栈为空
            else:
                # 置放元素
                str2_list.append(ch1)

        # 转成字符串 将其逆置 由于栈原因
        s = ''.join(str2_list[::-1])
        return s
    

def main():
    s = Solution()
    print(s.removeDuplicates('abbaca'))



if __name__ == '__main__':
    main()