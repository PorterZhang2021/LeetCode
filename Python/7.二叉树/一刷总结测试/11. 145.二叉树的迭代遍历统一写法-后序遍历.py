def traversal(root):
    # 结果集
    result = []
    # 处理栈
    handle_satck = [root]
    
    # 如果为空节点
    if not root:
        return result
    
    # 栈不为空
    while handle_satck:
        # 节点出栈
        cur = handle_satck.pop()
        # 如果节点不为空
        if cur:
            # 使用后序遍历
            # 后序遍历为左右中
            # 因此入栈顺序为中右左
            
            handle_satck.append(cur)
            # 标记节点
            handle_satck.append(None)

            # 如果是右节点
            if cur.right:
                handle_satck.append(cur.right)

            # 如果是左节点
            if cur.left:
                handle_satck.append(cur.left)

        else:
            # 节点出栈
            cur = handle_satck.pop()
            # 保存结果值
            result.append(cur.val)
    
    # 返回结果集
    return result