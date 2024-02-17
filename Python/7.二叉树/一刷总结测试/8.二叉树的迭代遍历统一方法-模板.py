# 确定本题的使用方法
# 本题同样使用迭代法，需要使用栈
# 本题迭代法由于要实现统一
# 迭代法实现统一主要是因为有None的条件控制
# 这里的统一迭代本质上是一种标记法
# 确定是否具有特殊的边界条件
# 边界条件为如果节点为空那么就返回

def traversal(root):
    # 结果集
    result = []
    # 处理栈
    handle_stack = [root]

    # 如果为空节点直接
    if not root:
        # 返回结果集
        return result
    
    # 这里的遍历循环条件为
    # 栈不为空或者节点不为None
    # 这个是前序的情况
    while handle_stack:
        # 将节点出栈
        aux_node = handle_stack.pop()
        # 如果节点不为空
        if aux_node:
            # 此部分为变动位置
            pass
            # 变动部分为中间逻辑部分
            # 先添加右边节点
            if aux_node.right:
                handle_stack.append(aux_node.right)
            # 再添加左边节点
            elif aux_node.left:
                handle_stack.append(aux_node.left)
            # 最后添加中间节点
            handle_stack.append(aux_node)
            # 添加一个标记
            handle_stack.append(None)
        else:
            # 将节点出栈
            aux_node = handle_stack.pop()
            # 存放结果
            result.append(aux_node.val)
    return result
