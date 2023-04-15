def traversal(root, result):
    # root用于存放节点
    # result用于存放结果集
    # 确定参数与返回值
    # 参数为根节点和结果集
    # 确定终止条件
    # 如果根节点为空了，那么就返回
    # 确定单层逻辑
    # 此部分为前序遍历
    # 每次对中层节点的逻辑进行处理
    # 因此这里 中左右的顺序

    # 边界条件
    if not root:
        return None
    
    # 中层逻辑
    result.append(root.value)
    # 左层逻辑
    traversal(root.left, result)
    # 右层逻辑
    traversal(root.right, result)