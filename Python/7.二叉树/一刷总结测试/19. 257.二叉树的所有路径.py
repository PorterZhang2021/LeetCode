from typing import *
from BinaryTree import TreeNode
from BinaryTree import creatTree

# 确定本题的使用方法
# 本题使用递归+回溯
# 确定本题是否具有特殊边界

# 递归法
# 如果为空节点那么直接返回结果集
# 确定递归的参数与返回值
# 参数为节点 返回值直接return 因为这里在边界上会进行一部分逻辑操作
# 确定单层的边界条件
# 如果遇到叶子节点那么就进行操作
# 将节点值全部遍历出来，然后存放到结果集里面

# 确定单层逻辑
# 这里的结果可以发现是前序遍历，因此这里直接进行前序遍历
# 这里因为是对叶子节点进行判断
# 那么遍历时注意对节点的左子树与右子树进行判断
# 这里要注意的是，每次递归结束后将元素剔除实现回溯

class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        # 结果集
        result = []
        # 路径集
        path = []
        def get_path(root, path):
            nonlocal result
            # 如果为叶子节点
            if root and not root.left and not root.right:
                
                # 将节点值进行构建
                s = ""
                for node in path:
                    s = s + str(node.val) + "->"
                
                # 将最后的值加入
                s = s + str(root.val)
                # 将节点加入
                path.append(root)
                # 将值存入
                result.append(s)
                return
            
            # 将节点放入其中
            path.append(root)
            # 如果有左节点
            if root.left:
                get_path(root.left, path)
                # 回溯
                path.pop()
            # 如果有右节点
            if root.right:
                get_path(root.right, path)
                # 回溯
                path.pop()
        
        get_path(root, path)
        return result
            

def main():
    sl = Solution()
    # case 1
    root = [1,2,3,None,5]
    tree = creatTree(root)
    print(sl.binaryTreePaths(tree))
    # case 2
    root = [1]
    tree = creatTree(root)
    print(sl.binaryTreePaths(tree))

if __name__ == '__main__':
    main()