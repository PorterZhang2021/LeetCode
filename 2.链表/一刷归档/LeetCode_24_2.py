"""
24.两两交换链表中的结点
给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。
你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
第一步
cur指向了cur.next
第二步
cur指向了cur.next.next
第三步
两者进行交换
第四步
cur放到正确的位置
"""

from typing import Optional


# 链表结点
class ListNode:
    # 初始化
    def __init__(self, val=0, next=None):
        # 值
        self.val = val
        # 下一个值
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 虚拟结点
        dummy_head = ListNode(0)
        # 将虚拟头结点指向head
        dummy_head.next = head
        # 遍历结点
        cur = dummy_head

        # 如果cur的下一个结点以及下下个结点不为空
        while cur.next is not None and cur.next.next is not None:
            # 记录临时结点
            tmp = cur.next
            # 记录临时结点
            tmp1 = cur.next.next.next

            # 进行交换操作
            # cur的下一个结点指向cur的下一个结点的下一个结点
            cur.next = cur.next.next
            # cur的下一个结点的下一个结点指向cur的下一个结点 即临时结点
            cur.next.next = tmp
            # cur的下一个结点的下一个结点的下一个结点指向原来的地方
            cur.next.next.next = tmp1

            # cur移动两位，准备下一轮交换
            cur = cur.next.next

        # 返回头节点
        return dummy_head.next
