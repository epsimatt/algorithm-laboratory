from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# runtime: 85.07%, memory usage: 11.57%
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

        result.reverse()

        return result


if __name__ == '__main__':
    root = TreeNode(4)

    root.left = TreeNode(2)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)

    root.right = TreeNode(7)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(9)

    result = levelOrderTraversal(root)

    print(result)
