# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root: return None
        big = max(p.val,q.val)
        small = min(p.val,q.val)

        if small <= root.val <= big:
            return root
        elif big < root.val:
            return self.lowestCommonAncestor(root.left, p , q)
        elif small > root.val:
	    return self.lowestCommonAncestor(root.right, p , q)
 	return None

