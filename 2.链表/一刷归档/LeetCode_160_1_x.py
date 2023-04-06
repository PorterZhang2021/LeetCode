"""
160. 链表相交
给你两个单链表的头节点 headA 和 headB ，
请你找出并返回两个单链表相交的起始节点。
如果两个链表没有交点，返回 null 。

将两个构成一个环状结构即可
如何实现？
两个链表同时走，
当走到链表末尾的时候继续走，
此时将它们下一个要走的部分拼接，
每个拼接到对面，继续走

循环如何结束？
尝试 先用两者不同时等于none作为不定量循环的条件

此方法并不太正确，后续研究

"""


# 链表结点
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        # 遍历结点A
        curA = headA
        # 遍历结点B
        curB = headB
        # 打标记
        flagA = True
        flagB = True

        # 如果A不为None且B不为None就继续
        while curA is not None and curB is not None:
            # 如果A为None 连接到 headB上
            if curA.next is None and flagA:
                curA.next = headB
                flagA = False
            # 如果B为None 连接到 headA上
            if curB.next is None and flagB:
                curB.next = headA
                flagB = False
            # 如果遍历结点A 等于 遍历结点B 那么就推出
            if curA == curB:
                return curA
            else:
                # 否则两者遍历
                curA = curA.next
                curB = curB.next

        # 如果有一个为None那么就可以返回NULL了
        return None

