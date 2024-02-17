"""
移除链表元素
"""

from typing import Optional


# 定义链表
class ListNode:
    def __init__(self, val=0, next=None):
        # 值
        self.val = val
        # 下一个结点
        self.next = next


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        # 构建一个虚拟的头节点
        dummy_head = ListNode(next=head)
        # 构建一个遍历结点的工具
        cur = dummy_head
        # 后续结点不为空继续运行
        while cur.next is not None:
            # 如果此结点的下一个结点val值与cur的值相同
            if cur.next.val == val:
                # 删除结点
                cur.next = cur.next.next
            # 否则
            else:
                # 移动一次
                cur = cur.next
        # 返回头结点
        return dummy_head.next
