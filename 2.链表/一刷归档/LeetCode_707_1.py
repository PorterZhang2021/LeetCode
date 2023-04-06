"""
707.设计链表
设计链表实现。您可以选择使用单链表或双链表。
单链表中的节点应该具有两个属性：val 和 next。
val 是当前节点的值，next 是指向下一个节点的指针/引用。
如果要使用双向链表，则还需要一个属性 prev 以指示链表中的上一个节点。
假设链表中的所有节点都是 0-index 的。

在链表类中实现这些功能：

get(index)：获取链表中第 index 个节点的值。如果索引无效，则返回-1。

addAtHead(val)：在链表的第一个元素之前添加一个值为 val 的节点。
插入后，新节点将成为链表的第一个节点。

addAtTail(val)：将值为 val 的节点追加到链表的最后一个元素。

addAtIndex(index,val)：在链表中的第 index 个节点之前添加值为 val  的节点。
如果 index 等于链表的长度，则该节点将附加到链表的末尾。
如果 index 大于链表长度，则不会插入节点。如果index小于0，则在头部插入节点。

deleteAtIndex(index)：如果索引 index 有效，则删除链表中的第 index 个节点。
"""


# 单链表
# 构建一个结点
class ListNode:
    def __init__(self, val=0):
        # 存放值
        self.val = val
        # 下一个指针
        self.next = None


class MyLinkedList:

    # 初始化链表
    # 一个是头结点，一个是数组的长度属性
    def __init__(self):
        # 头节点
        self.head = ListNode(0)
        # 长度
        self.size = 0

    # get(index)：获取链表中第 index 个节点的值。如果索引无效，则返回-1。
    def get(self, index: int) -> int:
        # 如果索引小于0 或者 索引大于长度
        if index < 0 or index >= self.size:
            return -1
        # 找出头结点
        cur = self.head.next
        # 寻找索引值 这里索引值加1是要循环到索引的位置
        # 这里是从0开始循环的 因为本身具有一个头结点
        while index:
            cur = cur.next
            index -= 1
        # 返回值的情况
        return cur.val

    # addAtHead(val)：在链表的第一个元素之前添加一个值为 val 的节点。
    # 插入后，新节点将成为链表的第一个节点。
    def addAtHead(self, val: int) -> None:
        # 构建一个新结点
        new_node = ListNode(val)
        # 新节点的下一个结点同头节点的下一个结点连接
        new_node.next = self.head.next
        # 头节点的下一个结点为新结点
        self.head.next = new_node
        # 长度自增1
        self.size += 1

    def addAtTail(self, val: int) -> None:
        # 新结点
        new_node = ListNode(val)
        # 遍历
        cur = self.head
        # 进行循环遍历
        while cur.next:
            # 进行遍历
            cur = cur.next
        # 新结点
        cur.next = new_node
        # 长度自增1
        self.size += 1

    # addAtIndex(index,val)：在链表中的第 index 个节点之前添加值为 val  的节点。
    # 如果 index 等于链表的长度，则该节点将附加到链表的末尾。
    # 如果 index 大于链表长度，则不会插入节点。如果index小于0，则在头部插入节点。
    def addAtIndex(self, index: int, val: int) -> None:
        # 如果索引小于0
        if index < 0:
            # 增加头结点
            self.addAtHead(val)
            return
        # 如果索引与长度一致
        elif index == self.size:
            # 增加尾结点
            self.addAtTail(val)
            return
        # 如果索引大于长度
        elif index > self.size:
            return

        # 其他情况
        # 新节点
        node = ListNode(val)
        # 前一个结点
        pre = self.head
        while index:
            pre = pre.next
            index -= 1
        # 新结点的下一个结点指向前一个的下一个结点
        node.next = pre.next
        # 前一个结点的下一个结点 指向 新结点
        pre.next = node
        # 长度加1
        self.size += 1

    # deleteAtIndex(index)：如果索引 index 有效，则删除链表中的第 index 个节点。
    def deleteAtIndex(self, index: int) -> None:
        # 如果索引小于0或者索引大于等于长度
        if index < 0 or index >= self.size:
            # 返回
            return
        # 前一个结点
        pre = self.head
        # 循环索引
        while index:
            # 前一个结点的下一个结点
            pre = pre.next
            index -= 1
        # 前一个结点的下一个结点 指向 前一个结点的下一个结点的下一个结点
        pre.next = pre.next.next
        # 长度减少1
        self.size -= 1

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
