from typing import *

class Solution:
    def replaceSpace(self, s: str) -> str:
        # 确定使用哪种方法 
        # 使用双指针法
        # 双指针是异向还是同向 - 同向
        # 双指针的用途
        # cur用于对其进行遍历
        # index用于进行索引的自增与替换
        # 确定是否具有边界条件 - 无特殊边界

        # 列表化
        s = list(s)
        # 长度
        length = len(s)
        # 索引值情况
        index = 0
        # 进行遍历替换值
        for cur in range(length):
            if s[cur] == ' ':
                s[index] = '%20'
            else:
                s[index] = s[cur]
            index += 1
        # 重新组合成字符串
        s = ''.join(s)
        return s

def main():
    sl = Solution()
    # case 1
    s = "We are happy."
    print(sl.replaceSpace(s))
    # case 2

if __name__ == '__main__':
    main()