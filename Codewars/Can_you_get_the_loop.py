def loop_size(node):
    i = 1
    a = {}
    b = set()
    while node not in b:
        a[node] = i
        b.add(node)
        i += 1
        node = node.next
    return i - a[node]
