# 确定本题使用的方法
# 确定本题是否具有特殊边界
# 本题具有特殊边界 
# 当树节点为空的时候那么此时就可返回空结果集

# 中序遍历的遍历的遍历方式为左中右
# 本题使用的方法为栈因此在这种情况下
# 需要一直遍历到最左边
# 如果有左节点就一直存入
# 否则的情况下 先将节点的值输入
# 然后将右节点入栈
# 本题与其他题目不同的地方就是需要对节点进行检测

def traversal(root):
    # 结果集
    result = []
    # 处理栈
    handle_stack = []
    # 遍历节点
    cur = root
    # 进行处理
    while handle_stack or cur:
        # 如果栈没有到最底层
        if cur:
            # 将访问的节点放入
            handle_stack.append(cur)
            # 继续往左访问
            cur = cur.left
            # 否则
        else:
            # 栈内先弹出数据
            cur = handle_stack.pop()
            # 输出结果
            result.append(cur.val)
            # 往右边走
            cur = cur.right
    return result