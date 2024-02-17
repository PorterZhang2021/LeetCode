# 确定本题的使用方法
# 本题使用迭代法 直接使用栈
# 后序遍历 后序遍历的方式为左右中
# 因此左节点先出栈 然后右边节点出栈
# 这里直接参考前序遍历可知
# 前序遍历为中左右 那么如果我们改成中右左
# 然后将中右左的方式逆序就能够获得 左右中的结果
# 确定本题是否具有特殊边界
# 本题具有特殊边界 如果节点为空就直接返回
def traversal(root):
    # 结果集
    result = []
    # 处理栈
    handle_stack = [root]
    
    # 特殊边界情况
    if not root:
        return result

    while handle_stack:
        # 将元素值进栈
        aux_node = handle_stack.pop()
        # 值进栈
        result.append(aux_node.val)
        # 如果左节点存在
        if aux_node.left:
            handle_stack.append(aux_node.left)
        # 如果右节点存在
        if aux_node.right:
            handle_stack.append(aux_node.right)
    
    # 最终的值逆序
    result = result[::-1]
    return result


