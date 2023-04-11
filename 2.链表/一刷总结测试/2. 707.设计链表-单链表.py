from typing import *
from LinkList import ListNode
from LinkList import create_linklist
from LinkList import print_linked_list

# 构建链表节点类
class LinkNode:
    
    # 对其进行初始化
    def __init__(self, val=0, next=None):
        # 值
        self.val = val
        # 下一个节点
        self.next = next
        
class MyLinkedList:
	# 初始化
    def __init__(self):
        # 头节点
        self.head = LinkNode(0)
        # 长度
        self.size = 0


    def get(self, index: int) -> int:
        # 获取我们所需要的节点
        if 0 <= index < self.size:
            # 以头节点开始的遍历节点
            cur = self.head
            # 进行遍历，这里因为range是左闭右开，
            # 所以直接找到索引位置的话要单独加1
            for i in range(index + 1):
                # 进行遍历
                cur = cur.next
            # 返回遍历到的节点值
            return cur.val
        # 返回错误情况
        return -1

    def addAtHead(self, val: int) -> None:
        # 这里直接调用了索引插入
        self.addAtIndex(0 , val)

    def addAtTail(self, val: int) -> None:
        # 这里同样调用
        self.addAtIndex(self.size, val)


    def addAtIndex(self, index: int, val: int) -> None:
        # 如果索引值超过真实索引就返回
        if index > self.size:
            return
        # 如果索引值小于0
        if index < 0:
            index = 0
        # 这部分逻辑很重要
        if 0 <= index <= self.size:
            # 头节点
            cur = self.head
            # 进行遍历
            for i in range(index):
                cur = cur.next
            node = LinkNode(val, cur.next)
            cur.next = node
            self.size += 1
        
            

    def deleteAtIndex(self, index: int) -> None:
        if 0 <= index < self.size:
            cur = self.head
            for i in range(index):
                cur = cur.next
            cur.next = cur.next.next
            self.size -= 1
        else:
            return