from typing import *
from LinkList import ListNode
from LinkList import create_linklist
from LinkList import print_linked_list

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # 1.确认使用什么方法
        # 直接对节点进行遍历
        # 2.确认是否有特殊的边界条件
        # 如果head节点为空的时候，那么就直接返回None
        if not head:
            return None
        # 构建一个虚拟头节点
        aummy_head = ListNode(0)
        # 进行连接
        aummy_head.next = head
        cur = aummy_head
        # 这里直接遍历前节点
        while cur.next:
            # 判断前一个结点的值
            if cur.next.val == val:
                # 进行结点的移除
                cur.next = cur.next.next
                # 直接继续验证
                continue
            # 进行下一个结点的遍历
            cur = cur.next
        # 返回删除之后的情况
        return aummy_head.next

def main():
    s = Solution()
    # case1
    head = [1,2,6,3,4,5,6]
    val = 6
    head_list = create_linklist(head)
    after_list = s.removeElements(head_list, val)
    print(print_linked_list(after_list))
    # case2
    head = []
    val = 1
    head_list = create_linklist(head)
    after_list = s.removeElements(head_list, val)
    print(print_linked_list(after_list))
    # case3
    head = [7,7,7,7]
    val = 7
    head_list = create_linklist(head)
    after_list = s.removeElements(head_list, val)
    print(print_linked_list(after_list))


if __name__ == '__main__':
    main()



