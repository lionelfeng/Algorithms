# Definition for a  binary tree node
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = []        

        if not root: return None
        cur = root

        while cur:
            self.stack.append(cur)
            cur = cur.left

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.stack) != 0
        

    def next(self):
        """
        :rtype: int
        """
        cur = self.stack.pop()
        val = cur.val

        cur = cur.right
        while cur:
            self.stack.append(cur)
            cur = cur.left

        return val


if __name__ == "__main__":
    a = TreeNode(7)
    b = TreeNode(6)
    c = TreeNode(5)
    b.left = a
    b.right = c
    bst = BSTIterator(b)
    print bst.next()

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())