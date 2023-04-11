from typing import *
from LinkList import ListNode
from LinkList import create_linklist
from LinkList import print_linked_list

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 确定本题的使用方法
        # 本题使用的方法为双指针+数学推理法
        # 确定双指针为同向还是异向 - 同向
        # 确定双指针的用途 - 快指针与慢指针
        # 快指针一次走两步
        # 慢指针一次走一步
        # 两个指针如果出现一致的情况了，那么代表具有环
        # 本题需要解决的问题有两个部分组成
        # 首先需要能够判断是否有环
        # 有环的基础上找到开始入环的第一个结点
        # 确定是否有特殊的边界情况
        # 如果为空节点，那么直接返回None
        # 如果只有一个结点，那么直接返回None
        if not head:
            return None
        if not head.next:
            return None
        
        # 快指针
        fast = head
        # 慢指针
        slow = head

        # 如果快指针为空了，那么就说明没有环
        while fast and fast.next and fast.next.next:
            # 此部分要放置到前面，具体问题暂时不明白
            # 快指针一次走两步
            fast = fast.next.next
            # 慢指针一次走一步
            slow = slow.next
            # 如果快指针与慢指针相等了
            if fast is slow:
                # 寻找环的入口
                index1 = fast
                index2 = head
                while index1 is not index2:
                    # 进行索引的遍历
                    index1 = index1.next
                    index2 = index2.next
                return index1
        # 返回空
        return None

