from typing import *

class Solution:
    def replaceSpace(self, s: str) -> str:
        # 进行一遍遍历即可完成任务
        s = list(s)
        # 长度
        length = len(s)
        for i in range(length):
            if s[i] == ' ':
                s[i] = '%20'
        s = ''.join(s)
        return s

def main():
    sl = Solution()
    # case 1
    s = "We are happy."
    print(sl.replaceSpace(s))
    # case 2
    pass

if __name__ == '__main__':
    main()