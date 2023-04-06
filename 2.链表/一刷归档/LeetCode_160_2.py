"""
160.链表相交
先获取两个链表的长度
获取两个链表的差值
先移动较长的那个链表
移动到正确位置之后，两者同时移动
结点相同则退出
结束则返回None
"""


# 链表结点
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        # 获取A链表的长度
        len_A = 0
        cur_A = headA
        while cur_A is not None:
            cur_A = cur_A.next
            len_A += 1
        # 获取B链表的长度
        len_B = 0
        cur_B = headB
        while cur_B is not None:
            cur_B = cur_B.next
            len_B += 1

        # 计算哪个链表长
        # 长的为curA
        # 短的为curB
        # 获取差值
        if len_A > len_B:
            cur_A = headA
            cur_B = headB
            length = len_A - len_B
        else:
            cur_A = headB
            cur_B = headA
            length = len_B - len_A

        # 计数
        count = 0

        # 如果cur_A不等于None就继续
        while cur_A is not None:
            # 如果count大于length就开始移动B
            if count > length:
                cur_B = cur_B.next
            # 如果curA与cur_B相等就返回
            if cur_A == cur_B:
                return cur_A
            # 移动cur_A
            cur_A = cur_A.next
            # 计数
            count += 1

        # 结束没有找到一样的返回None
        return None
