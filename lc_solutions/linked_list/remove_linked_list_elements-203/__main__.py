class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# runtime: 86.28%, memory usage: 5.55%
def removeElements(head: ListNode, val: int) -> ListNode:
    if not head:
        return head
    else:
        result = ListNode(-1)

        current = result
        current.next = head

        while current.next:
            while current.next and current.next.val != val:
                current = current.next

            if current.next:
                current.next = current.next.next

        return result.next


if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(6)
    head.next.next.next = ListNode(3)
    head.next.next.next.next = ListNode(4)
    head.next.next.next.next.next = ListNode(5)
    head.next.next.next.next.next.next = ListNode(6)

    result = removeElements(head, 6)

    print(result.val)
    print(result.next.val)
    print(result.next.next.val)
    print(result.next.next.next.val)
    print(result.next.next.next.next.val)
