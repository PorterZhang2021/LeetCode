"""
142.环形链表Ⅱ
给定一个链表的头节点  head ，返回链表开始入环的第一个节点。
如果链表无环，则返回 null。
如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，则链表中存在环。
为了表示给定链表中的环，评测系统内部使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。
如果 pos 是 -1，则在该链表中没有环。
注意：pos 不作为参数进行传递，仅仅是为了标识链表的实际情况。
不允许修改 链表。

使用快慢指针操作
快慢指针操作的情况下
快指针走一圈，慢指针走一圈 迟早会遇到相撞的情况
这里循环的条件就是快指针为None
因为快指针为None的情况下其只可能为非循环链表

这题指判断了有环，没有解决环的入口问题

这题自己写的过程好像有冗余错误，超出时间限制

"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 相遇结点
        meet_index = None

        if head is None or head.next is None or head.next.next is None:
            return None

        # 快指针先走两步
        fast = head.next.next
        # 慢指针后走
        low = head

        # 是否有环
        is_circle = False

        # 快指针不为空就继续
        while fast.next.next is not None:
            # 快指针和慢指针相等
            if fast == low:
                # 这里说明其是环状的
                is_circle = True
                meet_index = fast

            # 快指针走一步
            fast = fast.next.next
            # 慢指针走一步
            low = low.next

        # 如果没有环直接返回None
        if not is_circle:
            return None
        # 否则进行如下的操作找环路口
        else:
            # 遍历结点
            cur = head
            # 遍历结点不等于相遇结点
            while cur != meet_index:
                # 遍历结点走一次
                cur = cur.next
                # 相遇结点走一次
                meet_index = meet_index.next
            return cur
