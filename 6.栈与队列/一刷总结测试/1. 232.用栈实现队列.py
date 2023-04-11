from typing import *

class MyQueue:

    def __init__(self):
        # 栈为先进后出
        # 因此使用pop()方法可以用列表直接模拟栈
        # 进栈
        self.push_stack = []
        # 出栈
        self.pop_stack = []


    def push(self, x: int) -> None:
        # 元素进栈
        self.push_stack.append(x)

    def pop(self) -> int:
        # 元素出栈
        # 由于队列是先进先出，因此需要移动到出栈后
        # 在出队列
        # 获取现在栈的元素长度
        push_length = len(self.push_stack)
        for i in range(push_length):
            # 将值出栈后存放到出栈列表内
            value = self.push_stack.pop()
            self.pop_stack.append(value)
        # 将需要的值出栈
        need_value = self.pop_stack.pop()
        # 获取现在出栈列表的元素
        pop_length = len(self.pop_stack)
        for i in range(pop_length):
            value = self.pop_stack.pop()
            self.push_stack.append(value)
        # 输出值
        return need_value
        

    def peek(self) -> int:
        # 获取现在栈的元素长度
        push_length = len(self.push_stack)
        for i in range(push_length):
            # 将值出栈后存放到出栈列表内
            value = self.push_stack.pop()
            self.pop_stack.append(value)
        # 将需要的值出栈
        need_value = self.pop_stack.pop()
        # 将这个值重新入栈
        self.pop_stack.append(need_value)
        # 重置入栈队列
        # 获取现在出栈列表的元素
        pop_length = len(self.pop_stack)
        for i in range(pop_length):
            value = self.pop_stack.pop()
            self.push_stack.append(value)
        # 输出值
        return need_value

    def empty(self) -> bool:
        # 如果出栈的长度为0
        if len(self.push_stack) == 0:
            # 则说明为空
            return True
        return False

def main():
    # case 1
    myQueue = MyQueue()
    myQueue.push(1)
    myQueue.push(2)
    print(myQueue.peek())
    print(myQueue.pop())
    print(myQueue.empty())


if __name__ == '__main__':
    main()