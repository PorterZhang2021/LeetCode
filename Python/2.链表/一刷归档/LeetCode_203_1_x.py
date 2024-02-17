"""
移除链表的元素

给你一个链表的头节点 head 和一个整数 val ，
请你删除链表中所有满足 Node.val == val 的节点，
并返回 新的头节点 。

快慢指针的办法
快指针与慢指针差一格
初始化
快指针为第一个元素
慢指针为头元素
当快指针不为None就一直循环
如果快指针的值等于val
那么慢指针的next改为快指针的next
否则就对快指针和慢指针同时后移 -> 这种情况会出现指针的指向错误

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 导入typing模块
from typing import Optional


# 链表的定义
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # 移除元素
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # 本身来说第一个头节点就带有值
        # 所以我们需要设置一个虚拟头结点
        dummy_head = ListNode(next=head)

        # 快指针
        fast = dummy_head.next
        # 慢指针
        slow = dummy_head

        # 如果快指针不为None就继续 PEP 8 守则
        while fast is not None:
            # 如果快指针的值和val相等
            if fast.val == val:
                # 慢指针的next改为快指针的next
                slow.next = fast.next
            # 快指针与慢指针每次往前走一次
            fast = fast.next
            slow = slow.next

        # 返回head
        return head
