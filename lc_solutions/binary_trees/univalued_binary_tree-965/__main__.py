class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# runtime: 96.15%, memory usage: 5.82%
def isUnivalTree(root: TreeNode) -> bool:
    if not root or (not root.left and not root.right):
        return True
    else:
        v1 = root.val
        v2 = root.left.val if root.left else v1
        v3 = root.right.val if root.right else v1

        if not v1 == v2 == v3:
            return False
        else:
            return isUnivalTree(root.left) and isUnivalTree(root.right)


if __name__ == '__main__':
    root = TreeNode(1)

    root.left = TreeNode(1)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(1)

    root.right = TreeNode(1)
    root.right.right = TreeNode(1)

    print(isUnivalTree(root)) # True
