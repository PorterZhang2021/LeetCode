def traversal(root):
    # 结果集
    result = []
    # 处理栈
    handle_stack = []
    
    # 如果根节点为空
    if not root:
        return result

    # 如果栈不为空
    while handle_stack:
        # 取出栈内元素
        cur = handle_stack.pop()
        # 如果节点不为空
        if cur:
            # 左中右
            # 这里方式为右中左
            # 将左边的元素放入
            handle_stack.append(cur.left)
            # 将本身放入
            handle_stack.append(cur)
            # 放入标记节点
            handle_stack.append(None)
            # 将右边的元素放入
            handle_stack.append(cur.right)
        else:
            # 元素出栈
            cur = handle_stack.pop()
            # 将结果放入
            result.append(cur.val)
    
    # 返回结果集
    return result