class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    
    def __str__(self) -> str:
        return 'val: %s' % str(self.val)
    
    def __repr__(self) -> str:
        return 'val: %s' % str(self.val)

def creatTree(nodes):
    if not nodes:
        return None
    
    from queue import Queue
    que = Queue()
    root = None
    is_left = True		# 是否生成左子树
    for val in nodes:
        node = TreeNode(val) if val else None
        if que.empty():
            root = node
            que.put(node)
        
        elif is_left:
            # 获取队首结点，同时出队
            cur = que.get()
            cur.left = node
            if node:
                que.put(node)
            is_left = not is_left
        
        else:
            # 到这里的话一定会有cur变量
            cur.right = node
            if node:
                que.put(node)
            
            is_left = not is_left
    
    return root