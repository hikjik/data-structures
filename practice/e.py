def solution(node):
    prev = None
    while node:
        next = node.next
        node.next = prev
        node.prev = next
        prev = node
        node = next
    return prev
