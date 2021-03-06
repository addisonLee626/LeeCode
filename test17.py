#definition for singly-linked list.
#class listnode:
 #   def init(self,x):
  #      self.val = x
   #     self.next = None


def mergeTwoLists(l1, l2):
    if l1 is None:
        return l2
    if l2 is None:
        return l1
    if l1.val <= l2.val:
        l1.next = mergeTwoLists(l1.next, l2)
        return l1
    if l1.val > l2.val:
        l2.next = mergeTwoLists(l2.next, l1)
        return l2


array1 = [1, 3, 5]
array2 = [2, 4, 6]
print(mergeTwoLists(array1, array2))
