class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# runtime: 65.70%, memory usage: 7.69%
def sumOfLeftLeaves(root: TreeNode) -> int:
    if root is None:
        return 0
    else:
        val = root.left.val if root.left and (not root.left.left and not root.left.right) else 0

        return val + sumOfLeftLeaves(root.left) + sumOfLeftLeaves(root.right)


if __name__ == '__main__':
    root = TreeNode(3)

    root.left = TreeNode(9)

    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    print(sumOfLeftLeaves(root)) # 24
