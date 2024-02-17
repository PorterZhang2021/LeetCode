from typing import *
from LinkList import ListNode
from LinkList import print_linked_list
from LinkList import create_linklist

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 确定本题的使用方法
        # 本题使用双指针法
        # 1. 确定双指针为同向还是异向 - 同向
        # 2. 确定双指针的用途
        # 本题的双指针为快慢指针
        # 快指针走到对应位置后
        # 慢指针移动可以删除对应倒数N个结点
        # 确定是否具有特殊的边界情况
        # 如果链表为空直接返回空
        
        if not head:
            return None
        
        aummy_head = ListNode(0, head)
        # 快结点
        fast = aummy_head
        # 慢结点
        slow = aummy_head
        # 索引
        count = 0
        # 链表不为空
        while fast:
            # 如果满足条件则移动慢结点
            if count > n: slow = slow.next
            # 遍历快结点
            fast = fast.next
            count += 1
        # 删除结点
        slow.next = slow.next.next
        # 返回头结点
        return aummy_head.next


def main():
    s = Solution()
    # case 1
    head = [1,2,3,4,5]
    n = 2
    head_list = create_linklist(head)
    handled_list = s.removeNthFromEnd(head_list, n)
    print(print_linked_list(handled_list))
    # case 2
    head = [1]
    n = 1
    head_list = create_linklist(head)
    handled_list = s.removeNthFromEnd(head_list, n)
    print(print_linked_list(handled_list))
    # case 3
    head = [1,2]
    n = 1
    head_list = create_linklist(head)
    handled_list = s.removeNthFromEnd(head_list, n)
    print(print_linked_list(handled_list))

if __name__ == '__main__':
    main()