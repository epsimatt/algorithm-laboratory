class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


# runtime: 79.81%, memory usage: 7.69%
def isPalindrome(head: ListNode) -> bool:
    array = []

    while head:
        array.append(head.val)
        head = head.next

    low, high = 0, len(array) - 1

    while low < high:
        if array[low] != array[high]:
            return False

        low += 1
        high -= 1

    return True


if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(2)
    head.next.next.next = ListNode(1)

    print(isPalindrome(head))
