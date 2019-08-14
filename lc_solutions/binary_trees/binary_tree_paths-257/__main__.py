from typing import List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# runtime: 61.58%, memory usage: 9.52%
def binaryTreePaths(root: TreeNode) -> List[str]:
    result = []

    if not root:
        return result
    else:
        current = f"{root.val}"

        def binaryTreePaths_helper(root: TreeNode, current: str):
            if not root.left and not root.right:
                result.append(current)
            else:
                if root.left:
                    binaryTreePaths_helper(root.left, f"{current}->{root.left.val}")

                if root.right:
                    binaryTreePaths_helper(root.right, f"{current}->{root.right.val}")

        binaryTreePaths_helper(root, current)

        return result


if __name__ == '__main__':
    root = TreeNode(1)

    root.left = TreeNode(2)
    root.left.right = TreeNode(5)

    root.right = TreeNode(3)

    print(binaryTreePaths(root))
