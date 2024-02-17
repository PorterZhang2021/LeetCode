from typing import *
from LinkList import ListNode
from LinkList import create_linklist
from LinkList import print_linked_list

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 确定本题的使用方法
        # 本题使用双指针法
        # 双指针是同向还是异向 - 同向
        # 双指针的用途是什么
        # fast快指针 - 一次走两步，其一次走两步会出现相交的情况
        # slow慢指针 - 一次走一步
        # 确定是否具有边界条件
        # 如果头节点为空或者只有一个结点那么直接返回None
        if not head:
            return None
        if not head.next:
            return None
        # 快指针
        fast = head
        # 慢指针
        slow = head
        while fast and fast.next and fast.next.next:
            # 快指针走两步
            fast = fast.next.next
            # 慢指针走一步
            slow = slow.next
            # 如果出现两者相等
            if fast is slow:
                # 相等索引位置
                index1 = fast
                # 头结点
                index2 = head
                while index1 is not index2:
                    index1 = index1.next
                    index2 = index2.next
                return index1

        return None


def main():
    pass

if __name__ == '__main__':
    main()
