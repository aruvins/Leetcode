# Given the root of a binary tree and an integer targetSum, return the number of paths where the sum of the values along the path equals targetSum.

# The path does not need to start or end at the root or a leaf, but it must go downwards (i.e., traveling only from parent nodes to child nodes).

 

# Example 1:


# Input: root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
# Output: 3
# Explanation: The paths that sum to 8 are shown.
# Example 2:

# Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
# Output: 3
 

# Constraints:

# The number of nodes in the tree is in the range [0, 1000].
# -109 <= Node.val <= 109
# -1000 <= targetSum <= 1000


from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def dfs(root, ps):
            if not root:
                return
            
            cs = ps + root.val
            x = cs - targetSum
            if x in freq:
                self.count += freq[x]
            if cs in freq:
                freq[cs] += 1
            else:
                freq[cs] = 1

            dfs(root.left, cs)
            dfs(root.right, cs)
            freq[cs] -= 1
        
        self.count = 0
        freq = {0:1}
        dfs(root, 0)
        return self.count
    













# ChatGPT explanation:
# Certainly! This code finds the number of paths in a binary tree where the sum of nodes along the path equals a specified targetSum. Importantly, these paths don’t need to start at the root or end at a leaf, and they can begin and end at any nodes in the tree as long as they form a continuous sequence.

# The code is based on prefix sum theory. Here’s a step-by-step explanation of the theory, followed by examples.

# Theory
# 1. Prefix Sum in Trees:
# A prefix sum in this context is the cumulative sum of values from the root down to any node. By calculating prefix sums, we can determine if there exists a subpath between any two nodes that adds up to the targetSum.

# 2. Finding Subpaths with Target Sum:
# The main idea is to use the prefix sum to check for any path sum that matches the targetSum. Specifically, at each node with cumulative sum cs, we want to check if there exists an earlier cumulative sum ps such that:

# 𝑐
# 𝑠
# −
# 𝑝
# 𝑠
# =
# targetSum
# cs−ps=targetSum
# This equation means that the nodes between the two sums (from the node where ps was first calculated to the current node) form a path that sums up to targetSum.

# 3. Using a HashMap (freq) to Store Prefix Sums:
# We use a dictionary freq to store the counts of each prefix sum we encounter as we traverse the tree. This allows us to efficiently check if there exists a ps that satisfies cs - ps = \text{targetSum}:

# If cs - targetSum exists in freq, it implies there’s a path ending at the current node with a sum equal to targetSum.
# After we check for paths, we update freq[cs] to include the current node’s cumulative sum before moving deeper into the tree.
# 4. Backtracking:
# After exploring all paths from the current node, we decrement the count of cs in freq as we backtrack, ensuring each path calculation is only relevant for the current traversal context.

# Example
# Let's go through an example with a small binary tree:

# markdown
# Copy code
#       10
#      /   \
#     5    -3
#    / \     \
#   3   2     11
#  / \   \
# 3  -2   1
# Suppose targetSum = 8. We want to find all paths in this tree where the sum of the nodes in the path equals 8.

# Step-by-Step Execution
# Starting at the root (10):

# Cumulative Sum (cs) at node 10 = 10.
# cs - targetSum = 10 - 8 = 2 is not in freq, so no path found yet.
# Update freq to {0: 1, 10: 1}.
# Move to node 5 (left child of 10):

# Cumulative Sum at node 5 = 10 + 5 = 15.
# cs - targetSum = 15 - 8 = 7 is not in freq, so no path found yet.
# Update freq to {0: 1, 10: 1, 15: 1}.
# Move to node 3 (left child of 5):

# Cumulative Sum at node 3 = 15 + 3 = 18.
# cs - targetSum = 18 - 8 = 10, which is in freq with a count of 1.
# This means there’s one path (from node 10 to node 3) that sums up to 8. Increment self.count to 1.
# Update freq to {0: 1, 10: 1, 15: 1, 18: 1}.
# Move to node 3 (left child of 3):

# Cumulative Sum at node 3 = 18 + 3 = 21.
# cs - targetSum = 21 - 8 = 13 is not in freq, so no path found yet.
# Update freq to {0: 1, 10: 1, 15: 1, 18: 1, 21: 1}.
# Since this node has no children, we backtrack. Decrement freq[21] by 1.
# Move to node -2 (right child of 3):

# Cumulative Sum at node -2 = 18 - 2 = 16.
# cs - targetSum = 16 - 8 = 8 is not in freq, so no path found.
# Update freq to {0: 1, 10: 1, 15: 1, 18: 1, 16: 1}.
# Backtrack from this node, decrement freq[16].
# Move to node 2 (right child of 5):

# Cumulative Sum at node 2 = 15 + 2 = 17.
# cs - targetSum = 17 - 8 = 9 is not in freq, so no path found.
# Update freq to {0: 1, 10: 1, 15: 1, 17: 1}.
# Move to node 1 (right child of 2):

# Cumulative Sum at node 1 = 17 + 1 = 18.
# cs - targetSum = 18 - 8 = 10, which is in freq with a count of 1.
# This means there’s another path (from node 10 to node 1) that sums up to 8. Increment self.count to 2.
# Backtrack, decrement freq[18], then freq[17], freq[15], and freq[10] as we return to the root and then explore the right subtree.
# Move to node -3 (right child of 10):

# Cumulative Sum at node -3 = 10 - 3 = 7.
# cs - targetSum = 7 - 8 = -1 is not in freq.
# Update freq to {0: 1, 10: 1, 7: 1}.
# Move to node 11 (right child of -3):

# Cumulative Sum at node 11 = 7 + 11 = 18.
# cs - targetSum = 18 - 8 = 10, which is in freq with a count of 1.
# This means there’s a third path (from node 10 to node 11) that sums up to 8. Increment self.count to 3.
# Final Result
# After traversing all nodes, self.count equals 3, which is the number of paths that sum to targetSum = 8.

# Summary
# This approach leverages prefix sums and a dictionary to track potential paths, allowing it to detect valid paths with a time complexity of 
# 𝑂
# (
# 𝑁
# )
# O(N).
# It backtracks correctly by decrementing prefix sum counts after exploring each subtree, ensuring no over-counting.
# This efficient method enables finding all paths with a specific sum without revisiting nodes or recalculating sums multiple times.