class ListNode:
    """
    链表节点
    """
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def create_linklist(arr):
    """
    创建链表，返回一个链表
    """
    # 如果为空直接返回
    if not len(arr):
        return None
    # 头节点
    head = ListNode(arr[0])
    # 遍历节点
    cur = head
    for i in range(1, len(arr)):
        cur.next = ListNode(arr[i])
        cur = cur.next
    # 返回链表节点
    return head

def print_linked_list(head):
    """
    以链表的形式打印
    """
    cur = head
    res = []
    while cur:
        res.append(cur.val)
        cur = cur.next
    return res

