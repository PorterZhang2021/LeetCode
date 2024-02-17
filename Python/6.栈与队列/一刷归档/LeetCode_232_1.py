"""
232.用栈实现队列
请你仅使用两个栈实现先入先出队列。
队列应当支持一般队列支持的所有操作（push、pop、peek、empty）：

实现 MyQueue 类：

void push(int x) 将元素 x 推到队列的末尾
int pop() 从队列的开头移除并返回元素
int peek() 返回队列开头的元素
boolean empty() 如果队列为空，返回 true ；否则，返回 false
说明：
你 只能 使用标准的栈操作 —— 
也就是只有 push to top, peek/pop from top, size, 和 is empty 操作是合法的。
你所使用的语言也许不支持栈。
你可以使用 list 或者 deque（双端队列）来模拟一个栈，只要是标准的栈操作即可。

队列的特性：先入先出
用栈进行模拟
两个栈
输入栈
输出栈
"""
class MyQueue:

    def __init__(self):
        # 输入栈 先进入的是栈底
        self._push_list = []
        # 输出栈 
        self._pop_list = []

    def push(self, x: int) -> None:
        # 将其入栈 这里直接进入输入栈即可，不需要过多操作
        self._push_list.append(x)

    def pop(self) -> int:
        # 元素出栈
        # 将输入栈翻转
        self._pop_list = self._push_list[::-1]
        # 进行元素的输出
        x = self._pop_list.pop()
        # 将输入栈重新翻转回来
        self._push_list = self._pop_list[::-1]
        return x

    def peek(self) -> int:
        # 返回开头元素
        # 提取出元素
        x = self._push_list[0]
        # 返回元素值
        return x
    
    def empty(self) -> bool:
        # 栈是否为空
        if len(self._push_list) > 0:
            return False
        else:
            return True

def main():
    myqueue = MyQueue()
    myqueue.push(1)
    myqueue.push(2)
    print(str(myqueue.peek()))
    print(str(myqueue.pop()))
    print(myqueue.empty())


if __name__ == '__main__':
    main()
