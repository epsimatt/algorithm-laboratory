class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# runtime: 92.78%, memory usage: 5.07%
def maxDepth(root: TreeNode) -> int:
    if not root:
        return 0

    def maxDepth_helper(root: TreeNode, depth: int) -> int:
        if not root:
            return depth - 1
        else:
            return max(maxDepth_helper(root.left, depth + 1), maxDepth_helper(root.right, depth + 1))

    return maxDepth_helper(root, 1)


if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(9)

    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    print(maxDepth(root))