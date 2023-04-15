def traversal(root, result):
    # 确定参数与返回值
    # 参数 节点 返回值为空
    # 确定是否具有边界条件
    # 如果节点为空 返回None
    # 确定中层逻辑 - 存放中间节点值
    if not root:
        return None
    # 左右中
    # 左遍历
    traversal(root.left, result)
    # 右遍历
    traversal(root.right, result)
    # 中遍历
    result.append(root.val)