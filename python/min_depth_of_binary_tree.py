from collections import deque
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
        def minDepth(self, root):
            """
            :type root: Optional[TreeNode]
            :rtype: int
            """
            if not root:
                return 0
            min_depth = [float('infinity')]  # pass integer by ref in python
            def dfs(root, depth, min_depth): 
                if not root.left and not root.right:
                    if depth<min_depth[0]:
                        min_depth[0] = depth
                    return
                if root.left:
                    dfs(root.left, depth+1, min_depth)
                if root.right:
                    dfs(root.right, depth+1, min_depth)  
                return
            dfs(root, 1, min_depth)
            return min_depth[0]



if __name__ == '__main__':
    sol = Solution()
    r = TreeNode(1)
    r.left = TreeNode(2)
    r.right = TreeNode(3)
    r.right.left = TreeNode(4)
    r.right.right = TreeNode(5)
    # r.right.right.right = TreeNode(7)

    res = sol.minDepth(r)
    print(res)