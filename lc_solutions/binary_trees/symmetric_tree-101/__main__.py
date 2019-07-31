class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# runtime: 76.10%, memory usage: 5.10%
def isSymmetric(root: TreeNode) -> bool:
    if not root:
        return True
    else:
        def isSymmetric_helper(left: TreeNode, right: TreeNode) -> bool:
            if not left and not right:
                return True
            elif not left or not right:
                return False
            else:
                return left.val == right.val \
                       and isSymmetric_helper(left.left, right.right) \
                       and isSymmetric_helper(left.right, right.left)

        return isSymmetric_helper(root.left, root.right)


if __name__ == '__main__':
    root = TreeNode(1)

    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)

    root.right = TreeNode(2)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(3)

    print(isSymmetric(root))
