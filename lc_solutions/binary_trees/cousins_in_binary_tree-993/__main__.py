class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# runtime: 96.97%, memory usage: 5.12%
def isCousins(root: TreeNode, x: int, y: int) -> bool:
    queue = [[root, 0]]
    x_cmp, y_cmp = [None, None, -1], [None, None, -1]

    while queue:
        front = queue.pop(0)

        node, distance = front[0], front[1]

        if not node:
            continue
        else:
            if node.left and node.left.val == x:
                x_cmp[0], x_cmp[1], x_cmp[2] = node, node.left, distance + 1

            if node.right and node.right.val == x:
                x_cmp[0], x_cmp[1], x_cmp[2] = node, node.right, distance + 1

            if node.left and node.left.val == y:
                y_cmp[0], y_cmp[1], y_cmp[2] = node, node.left, distance + 1

            if node.right and node.right.val == y:
                y_cmp[0], y_cmp[1], y_cmp[2] = node, node.right, distance + 1

            queue.append([node.left, distance + 1])
            queue.append([node.right, distance + 1])

    return x_cmp[0] != y_cmp[0] and x_cmp[2] == y_cmp[2]


if __name__ == '__main__':
    root = TreeNode(1)

    root.left = TreeNode(2)
    root.left.right = TreeNode(4)

    root.right = TreeNode(3)
    root.right.right = TreeNode(5)

    print(isCousins(root, 5, 4)) # True
