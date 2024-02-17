"""
删除链表的倒数第N个结点
给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 移除倒数第n个结点
        # 设置虚拟头结点
        dummy_head = ListNode(0)
        dummy_head.next = head
        # 快指针
        fast = dummy_head
        # 慢指针
        low = dummy_head.next
        # 慢指针的前一个指针
        pre_low = dummy_head
        # 计数
        count = 0
        # 如果快指针不为None就继续
        while fast is not None:
            # 如果计数值没有达到就不移动慢指针与慢指针的前一个指针
            # 这里要大于n 原因应该是因为low指针提前指向了一次
            if count > n:
                low = low.next
                pre_low = pre_low.next
            # 移动快指针
            fast = fast.next
            count += 1

        # 进行删除操作
        # 慢指针的前一个指针的下一个指针指向慢指针的下一个指针
        if low is not None:
            pre_low.next = low.next

        # 返回头结点 这里是next
        return dummy_head.next
