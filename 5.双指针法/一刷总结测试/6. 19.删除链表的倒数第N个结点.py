from typing import *
from LinkList import ListNode
from LinkList import create_linklist
from LinkList import print_linked_list

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 确定本题使用的方法
        # 本题使用双指针法
        # 双指针是同向还是异向 - 同向
        # 双指针的用途是什么 
        # fast指针 用于先行的遍历
        # slow指针 当满足条件后开始遍历
        # 确定本题是否有特殊的边界条件
        # 如果头结点为空或者只有单个结点且满足1的要求直接返回None
        if not head:
            return head
        if not head.next and n == 1:
            return None
        
        # 构建一个虚拟的头节点
        aummy_head = ListNode(0, head)
        fast = aummy_head
        slow = aummy_head
        index = 0
        # 进行遍历
        while fast:
            if index > n:
                slow = slow.next
            fast = fast.next
            # 索引每次自增
            index += 1
        # 删除结点
        slow.next = slow.next.next
        # 返回删除后的情况
        return aummy_head.next

def main():
    sl = Solution()
    # case 1
    head = [1,2,3,4,5]
    n = 2
    head_list = create_linklist(head)
    handled_list = sl.removeNthFromEnd(head_list, n)
    print(print_linked_list(handled_list))
    # case 2
    head = [1]
    n = 1
    head_list = create_linklist(head)
    handled_list = sl.removeNthFromEnd(head_list, n)
    print(print_linked_list(handled_list))
    # case 3
    head = [1,2]
    n = 1
    head_list = create_linklist(head)
    handled_list = sl.removeNthFromEnd(head_list, n)
    print(print_linked_list(handled_list))
if __name__ == '__main__':
    main()