#从尾到头打印链表

def from_tail_to_the_head(listNode):
    if not listNode:
        return []
    # temp = []
    result = []
    length = len(listNode)
    while length > 0:
        result.append(listNode[length-1])
        length -= 1
    # while listNode:
    #     temp.append(listNode)
    #     listNode = listNode.next
    # while temp:
    #     result.append(temp.pop())
    return result


Arraylist=[12,34,56,78]
print(from_tail_to_the_head(Arraylist))




