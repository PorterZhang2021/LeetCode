from typing import *
from LinkList import ListNode
from LinkList import create_linklist
from LinkList import print_linked_list

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        # 确定本题的解题方法
        # 本题使用的方法为双指针法
        # 双指针是同向还是异向 - 同向
        # 双指针的用途
        # curA 用于遍历A结点
        # curB 用于遍历B结点
        # 确定本题是否具有特殊边界的情况 - 暂无

        # 首先获取到两个链表的长度
        # 获取A链表的长度
        lenA = 0
        curA = headA
        while curA:
            curA = curA.next
            lenA += 1
        lenB = 0
        # 获取B链表的长度
        curB = headB
        while curB:
            curB = curB.next
            lenB += 1
        
        # 计算两个链表之间的差值
        if lenA > lenB:
            distance = lenA - lenB
            # 长的为A
            curA = headA
            # 短的为B
            curB = headB
        else:
            distance = lenB - lenA
            # 长的为B
            curA = headB
            # 短的为A
            curB = headA
        
        # 对长链表进行移动
        index = 0
        while distance > index:
            curA = curA.next
            index += 1
        
        # 同时移动直到两者相等
        # 这个情况下我并没有验证None
        # is not 的细节还得在看一下
        while curA is not curB:
            curA = curA.next
            curB = curB.next
        
        # 返回结点
        return curA

def main():
    pass

if __name__ == '__main__':
    main()