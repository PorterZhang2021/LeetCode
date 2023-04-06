"""
617. 合并二叉树
给你两棵二叉树： root1 和 root2 。
想象一下，当你将其中一棵覆盖到另一棵之上时，
两棵树上的一些节点将会重叠（而另一些不会）。
你需要将这两棵树合并成一棵新二叉树。

合并的规则是：如果两个节点重叠，
那么将这两个节点的值相加作为合并后节点的新值；
否则，不为 null 的节点将直接作为新二叉树的节点。
返回合并后的二叉树。
注意: 合并过程必须从两个树的根节点开始。

如果两个节点重叠，相加得到新的值
不为null的节点直接做为新二叉树的节点
返回合并后的二叉树

这里直觉思路为层序遍历
这里层序遍历存值的时候要思考一个问题
如果没有值的地方直接用0先存入
这里在遍历的时候没有值的地方就用0输入
"""

from typing import *
from NewTree import TreeNode
from NewTree import creatTree

class Solution:
    def get_level_list(self, root):
        """
            此函数获取层序遍历的值
            返回一个result_list
        """
        # 结果集
        result = []
        # 构建一个队列
        queue = [root]

        # 进行循环 如果队列存在值
        while queue:
            # 获取队列的长度
            queue_len = len(queue)
            # 本层值
            level_list = []
            # 队列的长度
            for i in range(queue_len):
                # 取出节点
                root = queue.pop(0)
                # 如果根节点存在
                if root:
                    # 存入节点的值
                    level_list.append(root.val)

                    # 如果左子树有值
                    if root.left:
                        # 存入左节点
                        queue.append(root.left)
                    # 否则存入一个None
                    else:
                        if root.right:
                            queue.append(None)
                    
                    # 如果右子树有值
                    if root.right:
                        # 存入右节点
                        queue.append(root.right)
                    # 否则存入一个None
                    else:
                        if root.left:
                            queue.append(None)
                # 如果不存在
                else:
                    # 存入0
                    level_list.append(0)
            # 将结果集存入
            result.append(level_list)
        # 返回结果集
        return result
    
    def createNewTree(self, result):

        # 利用层序遍历创建二叉树
        # 构建一个队列
        queue = []
        # 构建第一层的结点
        # 提取第一层的元素列表
        level_list = result.pop(0)
        # 获取第一层元素的值
        val = level_list.pop(0)
        # 利用第一层元素构建根结点
        root = TreeNode(val)
        # 将根结点存入队列中
        queue.append(root)
        # head指引根结点
        head = root

        # 如果存在层数就继续
        while result:
            # 下层元素出栈
            level_list = result.pop(0)
            while queue:
                # 将结点出栈
                root = queue.pop(0)
                # 构建左孩子
                # 出栈一个元素
                val = level_list.pop(0)
                # 如果左孩子不为0
                if val != 0:
                    # 构建一个新的结点
                    node = TreeNode(val)
                    # 将其放置在左孩子上
                    root.left = node
                    # 将此结点存入队列中
                    queue.append(root.left)
                else:
                    # 左孩子为空
                    root.left = None
                
                # 构建右孩子
                # 出栈一个元素
                val = level_list.pop(0)
                # 如果右孩子不为0
                if val != 0:
                    # 构建一个新的结点
                    node = TreeNode(val)
                    # 将其放置在右孩子上
                    root.right = node
                    # 将此结点存入队列中
                    queue.append(root.right)
                else:
                    # 右孩子为空
                    root.right = None
        return head


    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        
        # 获取第一个树的结果集
        root1_result = self.get_level_list(root1)
        # 获取第二个树的结果集
        root2_result = self.get_level_list(root2)
        
        # 结果集
        result = []
        # 构建合成的结果集
        for i in range(len(root1_result)):
            # 第一个树的层次
            level_root1_list = root1_result[i]
            # 第二个树的层次
            level_root2_list = root2_result[i]
            level_list = []
            for j in range(len(level_root1_list)):
                result = level_root1_list[j] + level_root2_list[j]
                level_list.append(result)
            result.append(level_list)
        
        root = self.createNewTree(result)
        return root

def main():
    s = Solution()
    tree1 = creatTree([1,3,2,5])
    tree2 = creatTree([[2,1,3,None,4,None,7]])
    print(s.mergeTrees(tree1, tree2))


if __name__ == '__main__':
    main()