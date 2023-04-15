# 本题使用迭代遍历的方式
# 前序的迭代遍历
# 前序遍历为中左右
# 由于最后要进行出栈
# 因此要研究好出栈的顺序
# 本身的情况下为中左右遍历顺序
# 但进栈后是先进后出
# 因此在这种情况下需要逆序进栈
# 也就是说右节点先进栈
# 左节点后进栈
# 最后中间节点在进栈

def traversal(root):
    # 结果集
    result = []
    # 处理栈
    handled_stack = [root]
    # 如果栈不为空就继续处理
    while handled_stack:
        # 提取出栈的元素
        aux_node = handled_stack.pop()
        result.append(aux_node.val)
        # 如果有右节点就先进栈
        if aux_node.right:
            handled_stack.append(aux_node.right)
        # 如果有左节点进栈
        if aux_node.left:
            handled_stack.append(aux_node.left)
    # 输出最后的结果集
    return result
