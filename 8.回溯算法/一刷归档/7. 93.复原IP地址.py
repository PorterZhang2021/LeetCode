from typing import *

# 确定本题的使用方法
# 回溯法
# 确定本题是否具有边界条件 - 暂无

class Solution:
    def __init__(self) -> None:
        self.path = []
        self.paths = []

    def restoreIpAddresses(self, s: str) -> List[str]:
        self.backtarcking(s, start=0, end=len(s), pointNum=0)
        return self.paths

    
    # 确定回溯的参数与返回值
    def backtarcking(self, s, start, end, pointNum):
        # 确定回溯的边界条件
        # 由于回溯是深度的部分，因此这里为最后嵌套的情况
        # 此时IP地址应该完成了前3位的赋值
        # 那么此时对最后一部分进行赋值即可
        if pointNum == 3:
            if self.is_valid(s, start, len(s) - 1):
                self.paths.append(s[:])
            return
        
        # 确定单层的回溯逻辑
        # 这里的循环是对字符串进行切割，因此这里为字符串进行循环
        for i in range(start, end):
            # 处理逻辑
            # 判断字段是否合法
            if self.is_valid(s, start, i):
                # 插入分好的字段
                s = s[:i+1] + '.' + s[i+1:]
                # 回溯函数
                self.backtarcking(s, start=i+2, end=len(s), pointNum=pointNum+1)
                s = s[:i+1] + s[i+2:] 
            else:
                continue
    
    # 确定是否合法
    def is_valid(self, s, start, end):
        # 如果起始位置大于终止位置
        if start > end:
            return False
        
        if s[start] == '0' and start != end:
            return False
        
        if not 0 <= int(s[start:end+1]) <= 255:
            return False
        
        return True


def main():
    sl = Solution()
    s = "25525511135"
    print(sl.restoreIpAddresses(s))

if __name__ == '__main__':
    main()
