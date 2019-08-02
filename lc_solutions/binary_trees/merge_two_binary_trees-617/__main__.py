class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# runtime: 11.42%, memory usage: 5.17%
def mergeTrees(t1: TreeNode, t2: TreeNode) -> TreeNode:
    if not t1 and not t2:
        return None
    else:
        t1_val, t2_val = t1.val if t1 else 0, t2.val if t2 else 0
        t1_left, t2_left = t1.left if t1 else None, t2.left if t2 else None
        t1_right, t2_right = t1.right if t1 else None, t2.right if t2 else None

        result = TreeNode(t1_val + t2_val)
        result.left = mergeTrees(t1_left, t2_left)
        result.right = mergeTrees(t1_right, t2_right)

        return result


if __name__ == '__main__':
    t1 = TreeNode(1)

    t1.left = TreeNode(3)
    t1.left.left = TreeNode(5)

    t1.right = TreeNode(2)

    t2 = TreeNode(2)

    t2.left = TreeNode(1)
    t2.left.right = TreeNode(4)

    t2.right = TreeNode(3)
    t2.right.right = TreeNode(7)

    result = mergeTrees(t1, t2)

    print(result.val)
    print(result.left.val, result.right.val)
    print(result.left.left.val, result.left.right.val, result.right.right.val)
