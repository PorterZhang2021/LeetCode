from typing import *
from BinaryTree import TreeNode
from BinaryTree import creatTree

# 确定本题的使用方法
# 本题使用递归法
# 确定本题的特殊边界条件
# 如果节点为空的情况下那么直接返回[]
# 如果节点只有一个那么直接返回[root.val]

class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        
        result = []
        pre = None
        count = 0
        max_count = 0
        # 边界条件
        if not root:
            return result
        
        if root and not root.left and not root.right:
            return [root.val]
        
        # 确定参数与返回值
        # 参数为根节点
        # 返回值无
        def find_mode(root):
            nonlocal pre
            nonlocal result
            nonlocal count
            nonlocal max_count

            # 确定本题的边界条件
            # 如果节点为空那么就返回
            if not root:
                return
            
            # 确定单层逻辑循环
            # 由于是二叉搜索树，利用其性质优先考虑中序遍历
            # 左遍历
            find_mode(root.left)
            # 此时如果还没有前一个结点那么此时初始化
            if not pre:
                count = 1
            # 如果pre出现，且出现前者与后者值相等
            elif pre and pre.val == root.val:
                # 对其进行自增
                count += 1
            # 如果pre出现，但前者与后者值不相等
            elif pre and pre.val != root.val:
               # 重新计数
               count = 1
            # 前一个结点更新
            pre = root
             # 更新最大值的情况
            if count > max_count:
                max_count = count
                # 那么进行重置
                result = []
                # 将元素放入
                result.append(root.val)
            # 两者相等的情况下
            elif count == max_count:
                # 将元素放入
                result.append(root.val)

            # 右遍历
            find_mode(root.right)
        find_mode(root)
        return result

def main():
    pass

if __name__ == '__main__':
    main()