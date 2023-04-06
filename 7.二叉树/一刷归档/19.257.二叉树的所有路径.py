"""
257.二叉树的所有路径
给你一个二叉树的根节点 root ，
按 任意顺序 ，返回所有从根节点到叶子节点的路径。
叶子节点 是指没有子节点的节点。

递归-> 前序，中序，后序
迭代-> 层序遍历

本题使用递归+回溯 此部分是第一次遇到回溯
本题在使用是利用前序遍历解题

"""

# 递归函数的参数以及返回值
# 参数为节点，路径path，结果集result 返回值无需

# 确定递归的终止条件
# 一般情况下是利用cur==NULL的方式
# 本题由于需要找到叶子节点就进行处理
# 所以情况为节点不为空，左右孩子都为空，找到叶子节点
# 这里的终止条件也与其他的题目有些不同，
# 这里终止是进行叶子节点的处理，对于递归终止部分则交给了单层递归逻辑中

# 确定单层递归逻辑
# 前序遍历，优先处理中间节点，将记录的中间节点放入路径中
# 递归终止条件部分只判断了如何处理叶子节点
# 因此这个地方递归要单独判断节点是否为空
# 同时在这部分的递归需要做回溯的相关处理
# 这里的回溯同递归是一一对应的，有一个递归就有一个回溯

from NewTree import creatTree
from typing import *

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        # 构建一个获取二叉树所有路径的函数
        # 这里的参数有根节点，路径，结果集
        path = []
        results = []

        def get_path_from_binaryTree(root, path, results):
            # 确定递归终止条件
            # 这里的终止条件是找到叶子节点
            if not root.left and not root.right:
                # 构建字符串
                str_path = ''
                # 构建出满足LeetCode所需要的格式
                for path_root in path:
                    # 取出值
                    num = path_root.val
                    # 构建字符串
                    str_path += str(num)
                    str_path += '->'
                # 加入最后一个节点 - 这个部分不要忘了要加入节点
                path.append(root)
                # 这个地方知识完成了leetcode所需要的输出
                str_path += str(root.val)
                # 存入results
                results.append(str_path)
                # 无返回值
                return

            # 单层逻辑内容部分
            # 处理中间节点的部分
            # 这里中间节点部分就是将其加入到路径当中
            path.append(root)
            # 这里注意判断是否有左子树节点，因为我们这里实行的是根节点的判断
            if root.left:
                # 进入左子树递归
                get_path_from_binaryTree(root.left, path, results)
                # 回溯节点情况
                path.pop()
            if root.right:
                # 进入右子树递归
                get_path_from_binaryTree(root.right, path, results)
                # 回溯节点情况
                path.pop()
        # 如果本身为空直接返回
        if not root:
            return []
        else:
            # 获取需要的内容
            get_path_from_binaryTree(root, path, results)
            return results

def main():
    s = Solution()
    tree = creatTree([1,2,3,None,5])
    print(s.binaryTreePaths(tree))


if __name__ == '__main__':
    main()