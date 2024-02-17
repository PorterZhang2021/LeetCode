"""
225.用队列实现栈
请你仅使用两个队列实现一个后入先出（LIFO）的栈，
并支持普通栈的全部四种操作（push、top、pop 和 empty）。

实现 MyStack 类：

void push(int x) 将元素 x 压入栈顶。
int pop() 移除并返回栈顶元素。
int top() 返回栈顶元素。
boolean empty() 如果栈是空的，返回 true ；否则，返回 false 。
 

注意：

你只能使用队列的基本操作 —— 
也就是 push to back、peek/pop from front、size 和 is empty 这些操作。
你所使用的语言也许不支持队列。 
你可以使用 list （列表）或者 deque（双端队列）来模拟一个队列 , 只要是标准的队列操作即可。

利用两个队列实现此操作
队列的特性为先进先出
栈的特性为后进先出
"""

class MyStack:

    def __init__(self):
        # 输入队列
        self._in = []
        # 输出队列
        self._out = []


    def push(self, x: int) -> None:
        # 将元素放入输入队列
        self._in.append(x)

    def pop(self) -> int:
        # 如果为空返回None
        if self.empty():
            return None
        
        # 将队列中的元素移除
        for _ in range(len(self._in) - 1):
            self._out.append(self._in.pop(0))
        
        return self._in.pop(0)
        

    def top(self) -> int:
        # 获取头部输出的元素
        x = self._in.pop(0)
        return x

    def empty(self) -> bool:
        if len(self._in) > 0:
            return False
        else:
            return True


def main():
    myStack = MyStack();
    myStack.push(1)
    myStack.push(2)
    print(str(myStack.top()))
    print(str(myStack.pop()))
    print(myStack.empty())


if __name__ == '__main__':
    main()
