class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# runtime: 91.27%, memory usage: 5.41%
def invertTree_recursive(root: TreeNode) -> TreeNode:
    if not root:
        return root
    elif not root.left and not root.right:
        return root
    else:
        result = root

        invertTree_recursive(result.left)
        invertTree_recursive(result.right)

        temp = result.left
        result.left = result.right
        result.right = temp

        return result


if __name__ == '__main__':
    root = TreeNode(4)

    root.left = TreeNode(2)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)

    root.right = TreeNode(7)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(9)

    result = invertTree_recursive(root)

    print(result.val)
    print(result.left.val, result.right.val)
    print(result.left.left.val, result.left.right.val, result.right.left.val, result.right.right.val)
