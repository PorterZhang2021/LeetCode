"""
206.反转链表
给你单链表的头节点head, 请你反转链表，并返回反转后的链表
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 慢指针
        cur = None
        # 快指针
        pre = head

        # 如果pre不为None
        while pre is not None:
            # 临时保存pre后一个结点
            tmp = pre.next
            # pre的下一个结点指向cur
            pre.next = cur
            # 移动cur
            cur = pre
            # 移动pre
            pre = tmp

        # pre的下一个结点指向cur
        pre.next = cur

        # 返回pre
        return pre
