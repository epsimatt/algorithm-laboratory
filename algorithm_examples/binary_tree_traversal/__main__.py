from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def preorderTraversal_recursive(root: TreeNode) -> List[int]:
    result = []

    def preorderTraverse(root: TreeNode, result: List[int]):
        if root:
            result.append(root.val)

            preorderTraverse(root.left, result)
            preorderTraverse(root.right, result)

    preorderTraverse(root, result)

    return result


def inorderTraversal_recursive(root: TreeNode) -> List[int]:
    result = []

    def inorderTraverse(root: TreeNode, result: List[int]):
        if root:
            inorderTraverse(root.left, result)
            result.append(root.val)
            inorderTraverse(root.right, result)

    inorderTraverse(root, result)

    return result


def postorderTraversal_recursive(root: TreeNode) -> List[int]:
    result = []

    def postorderTraverse(root: TreeNode, result: List[int]):
        if root:
            postorderTraverse(root.left, result)
            postorderTraverse(root.right, result)

            result.append(root.val)

    postorderTraverse(root, result)

    return result


def preorderTraversal_iterative(root: TreeNode) -> List[int]:
    # TODO: ...
    pass


def inorderTraversal_iterative(root: TreeNode) -> List[int]:
    # TODO: ...
    pass


def postorderTraversal_iterative(root: TreeNode) -> List[int]:
    # TODO: ...
    pass


def levelOrderTraversal(root: TreeNode) -> List[List[int]]:
    if not root:
        return []
    else:
        result, queue = [], [[root, 0]]

        while queue:
            current = queue.pop(0)
            node, distance = current[0], current[1]

            if not node:
                continue

            if len(result) < distance + 1:
                result.append([])

            result[distance].append(node.val)

            queue.append([node.left, distance + 1])
            queue.append([node.right, distance + 1])

        return result


if __name__ == '__main__':
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)

    print(preorderTraversal_recursive(root))  # [1, 2, 3]
    print(inorderTraversal_recursive(root))  # [1, 3, 2]
    print(postorderTraversal_recursive(root))  # [3, 2, 1]
    print(levelOrderTraversal(root))  # [[1], [2], [3]]
