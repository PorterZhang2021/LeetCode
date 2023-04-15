def traversal(root):
    # 确定本题的使用方法
    # 确定本题是否有特殊的边界条件
    # 如果节点为空则返回结果集
    
    # 结果集
    result = []
    # 处理队列
    handle_queue = [root]

    # 如果根节点为空
    if not root:
        return result
    
    # 如果处理队列不为空
    while handle_queue:
        # 本层长度
        length = len(handle_queue)
        # 构建本层结果集
        level_result = []
        # 遍历节点
        for i in range(length):
            # 将节点出队列
            node = handle_queue.pop(0)
            # 将节点值存入
            level_result.append(node.val)
            # 对节点筛查
            # 如果有左节点
            if node.left:
                # 左节点入队列
                handle_queue.append(node.left)
            # 如果有右节点
            if node.right:
                # 右节点入队列
                handle_queue.append(node.right)
        # 将本层结果放入
        result.append(level_result)
    
    # 输出结果集
    return result
