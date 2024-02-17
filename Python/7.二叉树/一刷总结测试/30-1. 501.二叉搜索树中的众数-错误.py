from typing import *
from BinaryTree import TreeNode
from BinaryTree import creatTree

# 确定本题的使用方法
# 确定本题是否具有边界条件
# 如果为空节点时，直接返回[]
# 如果只有一个节点，直接返回[root.val]

class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        # 结果集 默认情况下把此值加入
        result = set()
        result.add(root.val)
        # 前一个结点
        pre = None
        # 计数值
        count = 0
        # 最大计数值
        max_count = 0

        # 边界条件
        if not root:
            return result
        if root and not root.left and not root.right:
            return [root.val]
        
        # 确定参数与返回值
        # 参数为根结点，返回值无
        def find_mode(root):
            nonlocal result
            nonlocal pre
            nonlocal count
            nonlocal max_count
            # 确定是否具有边界条件
            if not root:
                return None
            # 确定单层逻辑 
            # 二叉搜索树，默认思考中序遍历
            find_mode(root.left)
            # 如果有值且前一个值等于后一个值
            # 那么此时可以对count进行自增操作
            if pre and pre.val == root.val:
                count += 1
            # 如果两者不等了
            if pre and pre.val != root.val:
                # 如果大于最大count值
                if count > max_count:
                    # 更新结果集
                    result = set()
                    # 将值存入结果集
                    result.add(root.val)
                    # 更新max_count
                    max_count = count
                # 如果count值与最大count值相等
                if count == max_count:
                    # 将值存入
                    result.add(root.val)
                # 进行重置
                count = 0
            pre = root
            find_mode(root.right)
        
        find_mode(root)
        result = list(result)
        return result
    
def main():
    # 这里验证方式出错
    # 因为构建的是二叉搜索树 而这里构建的是二叉树
    sl = Solution()
    root = [1, 2, 3]
    tree = creatTree(root)
    print(tree)
    print(sl.findMode(tree))

if __name__ == '__main__':
    main()