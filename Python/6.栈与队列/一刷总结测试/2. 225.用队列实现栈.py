from typing import *

class MyStack:

    def __init__(self):
        # 利用列表来模拟队列操作
        # 这里由于先进先出 因此使用pop(0)
        # 进入队列
        self.push_queue = []
        # 出栈队列
        self.pop_queue = []

    def push(self, x: int) -> None:
        # 进入队列
        self.push_queue.append(x)

    def pop(self) -> int:
        # 队列元素出栈
        # 由于队列是先进先出
        # 而栈是先进后出
        # 这里出栈是要出队列的最后一个元素

        # 将队列的前n-1个元素出队后存放在pop_queue中
        # 获取push_queue队列的长度
        push_length = len(self.push_queue)
        for i in range(push_length - 1):
            # 从push_queue中出队列
            value = self.push_queue.pop(0)
            # 将这些元素存放在pop_queue中
            self.pop_queue.append(value)

        # 需要的值
        need_value = self.push_queue.pop(0)

        # 获取pop_queue队列的长度
        pop_length = len(self.pop_queue) 
        # 将pop_queue的元素重新存放进push_queue中
        for i in range(pop_length):
            # 从pop_queue中出队列
            value = self.pop_queue.pop(0)
            # 将这些元素存放在push_queue中
            self.push_queue.append(value)

        # 输出出队列的元素
        return need_value


    def top(self) -> int:
        # 这里是直接返回栈顶指针而不是移除
        # 解决这个问题的办法就是将所有的队列元素
        # 出队列后重新存放进去

        # 将队列的前n-1个元素出队后存放在pop_queue中
        # 获取push_queue队列的长度
        push_length = len(self.push_queue)
        for i in range(push_length - 1):
            # 从push_queue中出队列
            value = self.push_queue.pop(0)
            # 将这些元素存放在pop_queue中
            self.pop_queue.append(value)

        # 需要的值
        need_value = self.push_queue.pop(0)
        # 将这个值也存放在pop_que中
        self.pop_queue.append(need_value)

        # 重新整理push_queue队列
        # 获取pop_queue队列的长度
        pop_length = len(self.pop_queue) 
        # 将pop_queue的元素重新存放进push_queue中
        for i in range(pop_length):
            # 从pop_queue中出队列
            value = self.pop_queue.pop(0)
            # 将这些元素存放在push_queue中
            self.push_queue.append(value)
            
        # 输出出队列的元素
        return need_value

    def empty(self) -> bool:
        # 如果push_queue队列为空
        if len(self.push_queue) == 0:
            return True
        return False

def main():
    myStack = MyStack()
    myStack.push(1)
    myStack.push(2)
    print(myStack.top())
    print(myStack.pop())
    print(myStack.empty())

if __name__ == '__main__':
    main()