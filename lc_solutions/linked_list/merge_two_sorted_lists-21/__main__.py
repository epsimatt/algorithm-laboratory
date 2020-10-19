class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# runtime: 87.51%, memory usage: 6.61%
def mergeTwoLists_v1(l1: ListNode, l2: ListNode) -> ListNode:
    result = ListNode(-1)
    current = result

    while l1 and l2:
        if l1.val <= l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next

        current = current.next
        current.next = result

    if l1 or l2:
        current.next = l1 if l1 else l2

    return result.next


# runtime: 87.51%, memory usage: 6.61%
def mergeTwoLists_v2(l1: ListNode, l2: ListNode) -> ListNode:
    result = ListNode(-1)
    current = result

    while l1 and l2:
        if l1.val <= l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next

        current = current.next

    current.next = l1 or l2

    return result.next


if __name__ == '__main__':
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(4)

    l2 = ListNode(1)
    l2.next = ListNode(3)
    l2.next.next = ListNode(4)

    result = mergeTwoLists_v2(l1, l2)

    print(result.val)
    print(result.next.val)
    print(result.next.next.val)
    print(result.next.next.next.val)
    print(result.next.next.next.next.val)
    print(result.next.next.next.next.next.val)
