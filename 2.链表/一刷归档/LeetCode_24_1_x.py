"""
24.两两交换链表中的节点
给你一个链表，两两交换其中相邻的节点，
并返回交换后链表的头节点。
你必须在不修改节点内部的值的情况下完成本题（即，只能进行节点交换）。

本题错误的原因是自己在模拟时出现了差错

"""

from typing import Optional


# 设置结点
class ListNode:
    # 初始化
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 方法
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head

        # 慢指针
        low = head
        # 快指针
        fast = head.next
        # 如果快指针不为None的情况
        while fast is not None:
            # 保存快指针要去的下一个结点
            tmp_node = fast.next
            # 快指针与慢指针交换
            low.next = fast.next
            fast.next = low
            # 快指针重置归位-移动一次
            fast = tmp_node.next if tmp_node is not None else None
            # 慢指针重置归位-不移动
            low = tmp_node
        return head
