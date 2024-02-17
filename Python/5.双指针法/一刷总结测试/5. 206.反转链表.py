from typing import *
from LinkList import ListNode
from LinkList import create_linklist
from LinkList import print_linked_list

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 确定本题的使用方法
        # 本题使用双指针法
        # 双指针法是同向还是异向 - 同向
        # 双指针的用途是什么？
        # 快慢指针，快指针fast用于进行遍历，并参与反转
        # 慢指针同样用于反转
        # 确定本题是否具有边界情况
        # 如果为头节点为空或者只有一个头节点直接返回头结点

        # 特殊边界情况
        if not head or not head.next:
            return head

        # 快指针
        fast = head
        # 慢指针
        slow = None

        # 快指针依然存在
        while fast:
            # 保存快指针的下一位
            aux_node = fast.next

            # 进行逆置
            # 快指针的下一位指向慢指针
            fast.next = slow
            
            # 慢指针等于快指针
            slow = fast
            # 快指针为之前的保存结点
            fast = aux_node
        
        # 返回慢指针-此时慢指针为头结点
        return slow


def main():
    sl = Solution()
    # case 1
    head = [1,2,3,4,5]
    head_list = create_linklist(head)
    handled_list = sl.reverseList(head_list)
    print(print_linked_list(handled_list))
    # case 2
    head = [1,2]
    head_list = create_linklist(head)
    handled_list = sl.reverseList(head_list)
    print(print_linked_list(handled_list))
    # case 3
    head = []
    head_list = create_linklist(head)
    handled_list = sl.reverseList(head_list)
    print(print_linked_list(handled_list))



if __name__ == '__main__':
    main()
