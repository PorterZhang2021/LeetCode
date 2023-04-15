def traversal(root, result):
    # 确定参数与返回值
    # 参数为节点 返回值无
    # 确定边界条件 - 如果节点为空就结束
    # 确定单层逻辑 - 保存遍历后的节点值
    if not root:
        return None
    
    # 左遍历
    traversal(root.left, result)
    # 中层逻辑
    result.append(root.val)
    # 右遍历
    traversal(root.right, result)