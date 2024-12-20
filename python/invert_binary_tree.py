from collections import deque
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# class Solution(object):
#     def invertTree(self, root):
#         """
#         :type root: Optional[TreeNode]
#         :rtype: Optional[TreeNode]
#         """
#         if not root:
#             return
        
#         queue=deque([root])
#         while queue:
#             current = queue.popleft()
#             current.left, current.right = current.right, current.left
#             if current.left:
#                 queue.append(current.left)
#             if current.right:
#                 queue.append(current.right)

#         return root
    
# recursive
class Solution(object):
    def invertTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        
        if not root:
            return None
        
        root.left, root.right = root.right, root.left

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root

if __name__ == '__main__':
    sol = Solution()
    r = TreeNode(2)
    r.left = TreeNode(1)
    r.right = TreeNode(3)
    r.left.right = TreeNode(4)
    r.right.right = TreeNode(5)
    res = sol.invertTree(r)
    print(res.left.left.val)
    print(res.right.left.val)