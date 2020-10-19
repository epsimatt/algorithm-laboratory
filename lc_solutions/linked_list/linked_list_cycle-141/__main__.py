class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


# runtime: 5.04%, memory usage: 75.16%
def hasCycle_v1(head: ListNode) -> bool:
    current = head
    visited_nodes = []

    while current:
        visited_nodes.append(current)
        current = current.next

        if current in visited_nodes:
            return True

    return False


# runtime: 65.44%, memory usage: 63.37%
def hasCycle_v2(head: ListNode) -> bool:
    slow = fast = head

    while fast and fast.next:
        slow = slow.next

        if not fast.next.next:
            break
        else:
            fast = fast.next.next

            if slow == fast:
                return True

    return False


if __name__ == '__main__':
    nodes = [ListNode(3), ListNode(2), ListNode(0), ListNode(-4)]

    nodes[0].next = nodes[1]
    nodes[1].next = nodes[2]
    nodes[2].next = nodes[3]
    nodes[3].next = nodes[1]

    print(hasCycle_v2(nodes[0]))