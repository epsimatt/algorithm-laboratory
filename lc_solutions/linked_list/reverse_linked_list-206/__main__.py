class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# runtime: 81.48%, memory usage: 9.95%
def reverseList_recursive(head: ListNode) -> ListNode:
    if not head or not head.next:
        return head
    else:
        result = reverseList_recursive(head.next)

        head.next.next = head
        head.next = None

        return result


# runtime: 95.06%, memory usage: 28.40%
def reverseList_iterative(head: ListNode) -> ListNode:
    result = ListNode(-1)
    current = head

    while current:
        temp = current.next

        current.next = result.next
        result.next = current
        current = temp

    return result.next


if __name__ == '__main__':
    list_node = ListNode(1)
    list_node.next = ListNode(2)
    list_node.next.next = ListNode(3)

    list_node = reverseList_recursive(list_node)
    print(list_node.val, list_node.next.val, list_node.next.next.val)

    list_node = reverseList_iterative(list_node)
    print(list_node.val, list_node.next.val, list_node.next.next.val)
