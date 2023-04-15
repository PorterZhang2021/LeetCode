from typing import *
from BinaryTree import TreeNode
from BinaryTree import creatTree

# 确定本题的使用方法
# 本题使用递归法
# 确定本题是否具有边界条件
# 如果节点为空那么此时返回0

# 递归法
# 确定参数与返回值
# 参数为根节点 返回值为整数
# 确定边界条件
# 如果为空节点的情况下返回0
# 确定单层逻辑
# 本题同样使用后序遍历进行节点的收集
# 这里收集需要考虑到一件事情，那么就是如果出现0怎么处理
# 也就是一个特殊的边界情况
# 那么这里考虑的情况如下
# 如果左边为0右边不为0 此时返回右边部分
# 如果左边不为0右边为0 此时返回左边部分

class Solution:
    def getDepath(self, root):
        # 确定边界情况
        if not root:
            return 0

        # 单层逻辑执行
        # 左最小深度
        min_left_hight = self.getDepath(root.left)
        # 右最小深度
        min_right_hight = self.getDepath(root.right)
        # 如果左边为0，右边也为0那么返回1
        # if min_right_hight == 0 and min_left_hight == 0:
        #     return 1
        # 如果左边为0，那么返回右边
        # if min_left_hight == 0:
        #     return min_right_hight + 1
        # # 如果右边为0 那么返回左边
        # if min_right_hight == 0:
        #     return min_left_hight + 1

        # 这一部分是精华，但是不太能理解为什么这样
        if min_left_hight != 0:
            return min_left_hight + 1
        # 
        if min_right_hight != 0:
            return min_right_hight + 1
        
        # 这部分出错的原因是单单只验证了值的最小深度，而不是考虑节点本身上
        # 这里应该考虑节点本身
        # if root.left and not root.right:
        #     # 如果左边存在
        #     return min_left_hight + 1
        # # 如果右边存在
        # if not root.left and root.right:
        #     # 返回右边
        #     return min_right_hight + 1
        
        hight = min(min_left_hight, min_right_hight) + 1
        return hight
    
    def minDepth(self, root: Optional[TreeNode]) -> int:
        result = self.getDepath(root)
        return result


def main():
    sl = Solution()
    # case 1
    root = [3,9,20,None,None,15,7]
    tree = creatTree(root)
    print(sl.minDepth(tree))
    # case 2
    root = [2,None,3,None,4,None,5,None,6]
    tree = creatTree(root)
    print(sl.minDepth(tree))
    
if __name__ == '__main__':
    main()