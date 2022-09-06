def get_node_by_index(node, index):
    while index:
        node = node.next_item
        index -= 1
    return node


def solution(head, idx):
    if idx == 0:
        return head.next_item

    prev = get_node_by_index(head, idx - 1)
    prev.next_item = prev.next_item.next_item

    return head
