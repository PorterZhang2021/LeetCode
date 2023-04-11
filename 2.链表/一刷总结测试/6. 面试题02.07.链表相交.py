from typing import *
from LinkList import ListNode
from LinkList import create_linklist
from LinkList import print_linked_list

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        # 确定解决方法
        # 本题使用只需要将两者对其后
        # 同时进行遍历，直到出现结点相等
        # 此时即为我们所能获得的结点情况
        # 是否有边界性的特殊情况
        # 无需考虑
        
        # 计算出两个的长度
        lenA = 0
        lenB = 0
        # 遍历结点
        curA = headA
        curB = headB
        # 进行循环遍历
        while curA:
            lenA += 1
            curA = curA.next
        while curB:
            lenB += 1
            curB = curB.next
        
        # 进行大小的比较
        if lenA > lenB:
            # 存放差额
            sub_len = lenA - lenB
            # 结点置换
            curA = headA
            curB = headB
        else:
            sub_len = lenB - lenA
            curA = headB
            curB = headA
        
        # 进行结点的前置移动
        while sub_len:
            curA = curA.next
            sub_len -= 1
        
        # 两者同时进行移动
        while curA is not curB:
            curA = curA.next
            curB = curB.next
        
        # 输出交点情况
        return curA


def main():
    s = Solution()
    intersectVal = 8
    listA = [4,1,8,4,5]
    listB = [5,0,1,8,4,5]

if __name__ == '__main__':
    main()