class MyQueue:
    
    def __init__(self):
        """
        in主要负责push，out主要负责pop
        """
        self.stack_in = []
        self.stack_out = []
    
    def push(self, x: int) -> None:
        """ 
        有新元素进来，就往in里面push
        """
        self.stack_in.append(x)
    
    def pop(self) -> int:
        """
        """
        # 如果没有元素
        if self.empty():
            return None

        # 如果输出栈有值
        if self.stack_out:
            # 输出元素
            return self.stack_out.pop()
        else:
            # 将输入栈的元素反转
            for i in range(len(self.stack_in)):
                self.stack_out.append(self.stack_in.pop())
            return self.stack_out.pop()
    
    def peek(self) -> int:
        """
        """
        ans = self.pop()
        self.stack_out.append(ans)
        return ans

    def empty(self) -> bool:
        """
        只要in或者out有元素，说明队列不为空
        """
        return not (self.stack_in or self.stack_out)