from idlelib.tree import TreeNode

class solution:
    def reConstructBinaryTree(self,pre,tin):
        if len(pre) == 1:
            head = TreeNode(pre[0])
            head.left = None
            head.right = None
            return head
        head = TreeNode(pre[0])
        temp1 = tin.index(pre[0])
        length = len(tin[:temp1])
        if temp1 == 0:
            head.left = None
        else:
            head.left = self.reConstructBinaryTree(pre[1:length + 1], tin[:temp1])
        if length + 1 < len(pre):
            head.right = self.reConstructBinaryTree(pre[length + 1:], tin[temp1 + 1:])
        else:
            head.right = None
        return head

        a = [1,2,3,4,5,6,7]
        b = [3,2,4,1,6,5,7]
        print(self.reConstructBinaryTree(a,b))

