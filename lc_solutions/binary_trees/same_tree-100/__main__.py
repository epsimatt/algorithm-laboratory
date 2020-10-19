class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# runtime: 97.40%, memory usage: 5.35%
def isSameTree(p: TreeNode, q: TreeNode) -> bool:
    if (p is None and q is not None) or (p is not None and q is None):
        return False
    elif p is None and q is None:
        return True
    else:
        if p.val != q.val:
            return False

        return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)


if __name__ == '__main__':
    t1 = TreeNode(1)
    t1.left = TreeNode(2)
    t1.right = TreeNode(3)

    t2 = TreeNode(1)
    t2.left = TreeNode(2)
    t2.right = TreeNode(3)

    t3 = TreeNode(1)
    t3.left = TreeNode(2)

    t4 = TreeNode(1)
    t4.right = TreeNode(2)

    t5 = TreeNode(1)
    t5.left = TreeNode(2)
    t5.right = TreeNode(1)

    t6 = TreeNode(1)
    t6.left = TreeNode(1)
    t6.right = TreeNode(2)

    print(isSameTree(t1, t2))  # True
    print(isSameTree(t3, t4))  # False
    print(isSameTree(t5, t6))  # False
