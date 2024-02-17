from typing import *
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # 输出结果
        result = []
        # 队列 
        queue = [root]
        
        # 队列不为空
        # 此题需要对其进行分层
        # 此部分没有想到
        while queue:
            # 获取队列长度
            que_len = len(queue)
            level = []
            # 进行遍历输出
            for i in range(que_len):
                # 获取节点
                node = queue[i]
                # 输出结果
                level.append(node.val)
                # 放入结果
                if node.left:
                    # 将左节点值放入
                    queue.append(node.left)
                if node.right:
                    # 将右节点值放入
                    queue.append(node.right)
            # 存放本层的结果
            result.append(level)
        
        # 返回输出结果
        return result