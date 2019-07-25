class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# runtime: 100%, memory usage: 5.07%
def minDepth(root: TreeNode) -> int:
    if not root:
        return 0
    else:
        def minDepth_helper(root: TreeNode, depth: int) -> int:
            if not root:
                return depth - 1
            else:
                left_val = minDepth_helper(root.left, depth + 1)
                right_val = minDepth_helper(root.right, depth + 1)

                if not root.left:
                    return right_val
                elif not root.right:
                    return left_val
                else:
                    return min(left_val, right_val)

        return minDepth_helper(root, 1)


if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(9)

    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    print(minDepth(root))
    