"""
1047. 删除字符串中的所有相邻重复项
"""

class Solution:
    def removeDuplicates(self, s: str) -> str:
        # 构建一个栈
        res = list()
        # 循环遍历元素
        for item in s:
            # 如果res不为空 且 res最后一个元素 与 遍历元素一样
            if res and res[-1] == item:
                # 移除最后的元素
                res.pop()
            else:
                # 将元素放入其中
                res.append(item)
        
        return "".join(res) # 字符串拼接