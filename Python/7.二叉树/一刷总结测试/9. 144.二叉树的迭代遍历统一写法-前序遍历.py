# 确定本题的使用方法
# 确定本题是否具有边界条件
# 本题的边界条件为二叉树是否为空

def traversal(root):
    # 结果集
    result = []
    # 处理栈
    handle_stack = [root]

    # 如果根节点为空
    if not root:
        return result
    
    # 此部分为模拟过程
    # 可以发现本题的模拟过程同递归类似
    while handle_stack:
        # 先将一个值出栈
        cur = handle_stack.pop()
        # 判断这个值的情况
        # 如果这个值不是None
        if cur:
            # 此部分为前序遍历
            # 前序遍历为中左右
            # 这里由于是栈，所以存放为中右左
            
            

            # 如果有右节点
            if cur.right:
                # 将右节点加入
                handle_stack.append(cur.right)

            # 如果有左节点
            if cur.left:
                # 将左节点加入
                handle_stack.append(cur.left)
            
            # 将节点存放
            handle_stack.append(cur)
            # 标记一个None
            handle_stack.append(None)
            
        else:
            # 遇到None标记的时候
            # 代表值需要出栈了
            cur = handle_stack.pop()
            # 将出栈的值存入
            result.append(cur.val)
    
    # 返回结果集
    return result