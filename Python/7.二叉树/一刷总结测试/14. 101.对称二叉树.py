# 确定本题的使用方法
# 确定本题是否有特殊的边界条件
# 如果只有一个节点那么直接返回True
# 如果为空那么直接返回False

# 本题使用方法为递归法
# 确定递归的参数与返回值
# 参数为 两个根节点 返回值为布尔类型
# 确定递归是否具有边界条件
# 两个不同的叶子节点进行比较
# 叶子节点的情况 空，有值
# 一个叶子为空 另一个叶子也为空 那么返回True
# 一个叶子为空 另一个叶子有值 那么返回False 这里分为两种可能
# 一个叶子有值且另一个叶子也有值 相等 返回True 不相等返回False
# 确定递归的单层逻辑
# 由于每个步骤的result需要栈将结果提供给上一层
# 因此此时采用后序遍历并且递归函数需要进行变量传值
# 最终返回结果值

from typing import *
from BinaryTree import TreeNode
from BinaryTree import creatTree

class Solution:
    # 对称二叉树验证
    def is_two_tree_symmetric(self, left, right):
        # 边界条件
        # 如果两个根节点为空
        if not left and not right:
            return True
        # 如果一个节点为空，另一个节点不为空
        elif not left and right:
            return False
        elif left and not right:
            return False
        # 如果两个节点都存在比较值
        elif left and right and left.val != right.val:
            return False
        # 这里我对两个值相等进行了比较
        # 然后就直接跳出了循环，这里两值相等的判断是不是不属于边界
        # 而是属于下方的验证部分，可是作为下方的验证部分
        # 如果没有验证，它是如何得到使用True还是False呢？
        # elif left and right and left.val == right.val:
        #     return True
        
        # 构建一个结果集
        # 此部分是比较第一个树的左节点与第二棵树的右节点
        left_result = self.is_two_tree_symmetric(left.left, right.right)
        # 此部分是比较第一个数的右节点与第二个数的左节点
        right_result = self.is_two_tree_symmetric(left.right, right.left)
        # 将两部分的结果整合
        result = left_result and right_result
        # 返回每一次获得结果
        return result
    
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # 边界条件情况
        # 如果节点为空
        if not root:
            return False
        # 如果只有一个节点
        if root and not root.left and not root.right:
            return True
        
        

        # 进行验证
        result = self.is_two_tree_symmetric(root.left, root.right)
        return result

def main():
    sl = Solution()
    # case 1
    root = [1,2,2,3,4,4,3]
    tree = creatTree(root)
    print(sl.isSymmetric(root=tree))
    # case 2
    root = [1,2,2,None,3,None,3]
    tree = creatTree(root)
    print(sl.isSymmetric(root=tree))

if __name__ == '__main__':
    main()