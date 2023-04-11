from typing import *
from LinkList import ListNode
from LinkList import create_linklist
from LinkList import print_linked_list

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 1. 确定使用哪种方法
        # 本题使用单个节点进行遍历
        # 此节点用来操作后面两个节点
        # 双指针操作时此情况出错
        # 2. 确定是否有边界条件或者特殊情况考虑
        # 如果头节点为空那么就直接返回None
        # 如果只有单个节点那么就直接返回此节点
        # 如果出现三个节点，那么对最后一个节点不进行置换
        # 那么此时循环条件的验证需要验证本身以及下一个节点
        
        # 特殊情况
        if not head:
            return None
        if not head.next:
            return head
        
        # 构建一个头节点
        aummy_head = ListNode(0, head)
        # 进行遍历
        cur = aummy_head
        # 对cur的后面两个结点进行检查，如果存在，那么就需要调换
        while cur and cur.next and cur.next.next:
            # 保存节点情况
            handle_node_1 = cur.next
            handle_node_2 = cur.next.next

            # 进行处理操作
            # 前一个结点指向后一个结点的下一个结点
            handle_node_1.next = handle_node_2.next
            # 后一个结点指向前一个结点
            handle_node_2.next = handle_node_1
            # 遍历结点联通后一个结点
            cur.next = handle_node_2

            # 保存新节点的位置
            cur = handle_node_1
        return aummy_head.next


def main():
    s = Solution()
    head = [1,2,3,4]
    head_list = create_linklist(head)
    handled_list = s.swapPairs(head_list)
    print(print_linked_list(handled_list))
    head = []
    head_list = create_linklist(head)
    handled_list = s.swapPairs(head_list)
    print(print_linked_list(handled_list))
    head = [1]
    head_list = create_linklist(head)
    handled_list = s.swapPairs(head_list)
    print(print_linked_list(handled_list))

if __name__ == '__main__':
    main()