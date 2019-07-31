class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# runtime: 25.71%, memory usage: 5.27%
def rangeSumBST_v1(root: TreeNode, L: int, R: int) -> int:
    if not root:
        return 0
    else:
        sum_of_children_nodes = rangeSumBST_v1(root.left, L, R) + rangeSumBST_v1(root.right, L, R)
        return sum_of_children_nodes + root.val * (L <= root.val <= R)


# runtime: 100%, memory usage: 5.27%
def rangeSumBST_v2(root: TreeNode, L: int, R: int) -> int:
    if not root:
        return 0
    else:
        if L <= root.val <= R:
            return root.val + rangeSumBST_v2(root.left, L, R) + rangeSumBST_v2(root.right, L, R)
        elif root.val < L:
            return rangeSumBST_v2(root.right, L, R)
        else:
            return rangeSumBST_v2(root.left, L, R)


if __name__ == '__main__':
    root = TreeNode(10)

    root.left = TreeNode(5)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(7)

    root.right = TreeNode(15)
    root.right.right = TreeNode(18)

    print(rangeSumBST_v2(root, 7, 15)) # 32