from typing import *
from LinkList import ListNode
from LinkList import create_linklist
from LinkList import print_linked_list

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 确定使用方法
        # 使用双指针法
        # 1. 双指针是同向还是异向 - 同向
        # 2. 双指针的用途是什么？
        # 一个为快指针，一个为慢指针
        # 其中快指针用于遍历
        # 慢指针用于在后面进行调整
        # 是否有边界情况
        # 如果头节点为空直接返回
        if not head:
            return None
        fast = head
        slow = None
        while fast:
            # 辅助结点
            aux_cur = fast.next
            # 进行结点指向的逆转
            fast.next = slow
            # 重新构建遍历秩序
            slow = fast
            fast = aux_cur
        # 返回慢节点作为头结点
        return slow

def main():
    s = Solution()
    # case 1
    head = [1,2,3,4,5]
    head_list = create_linklist(head)
    handled_list = s.reverseList(head_list)
    print(print_linked_list(handled_list))
    # case 2
    head = [1,2]
    head_list = create_linklist(head)
    handled_list = s.reverseList(head_list)
    print(print_linked_list(handled_list))
    # case 3
    head = []
    head_list = create_linklist(head)
    handled_list = s.reverseList(head_list)
    print(print_linked_list(handled_list))

if __name__ == '__main__':
    main()