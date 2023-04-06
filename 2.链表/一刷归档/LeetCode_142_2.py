"""
142.环形链表Ⅱ
给定一个链表，返回链表开始入环的第一个节点。
如果链表无环，则返回 null。
为了表示给定链表中的环，
使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。
如果 pos 是 -1，则在该链表中没有环。
"""

from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 快指针
        fast = head
        # 慢指针
        slow = head

        # 如果快指针和快指针的下一个都不为None
        while fast is not None and fast.next is not None:
            # 慢指针走一次
            slow = slow.next
            # 快指针走两次
            fast = fast.next.next

            # 如果快慢指针相遇，此时从head和相遇点，同时查找直至相遇
            if slow == fast:
                # 相遇点
                index1 = fast
                # 头指针
                index2 = head
                # 如果两个指针不相遇
                while index1 is not index2:
                    # 相遇点索引位置走一次
                    index1 = index1.next
                    # 头指针走一次
                    index2 = index2.next
                # 返回环的入口
                return index2
        # 返回None
        return None
