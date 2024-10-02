# Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

# A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.

 

# Example 1:


# Input: root = [3,4,5,1,2], subRoot = [4,1,2]
# Output: true
# Example 2:


# Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
# Output: false
 

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False  # If root is None, it can't contain subRoot
        if not subRoot:
            return True   # If subRoot is None, it's a subtree of any tree

        # Check if current trees are identical, or if subRoot is a subtree of either child
        if self.isSameTree(root, subRoot):
            return True
        
        return (self.isSubtree(root.left, subRoot) or 
                self.isSubtree(root.right, subRoot))  # Recursively check both left and right subtrees
    
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True  # Both trees are empty, so they are the same
        if not p or not q:
            return False  # One tree is empty and the other is not, so they are not the same

        # Check if current nodes are the same and recurse on both children
        if p.val == q.val:
            return (self.isSameTree(p.left, q.left) and 
                    self.isSameTree(p.right, q.right))
            
        return False

        
        
        