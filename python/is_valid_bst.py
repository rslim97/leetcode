# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """

        def dfs(root, min_val, max_val):
            if not root:
                return True
            if min_val>=root.val or root.val>=max_val:
                return False
            if dfs(root.left, min_val, root.val) and dfs(root.right, root.val, max_val):
                return True
            return False
        
        return dfs(root, -float("infinity"), float("infinity"))        


if __name__ == '__main__':
    sol = Solution()
    t = TreeNode(2)
    t.left = TreeNode(1)
    t.right = TreeNode(3)
    # t.right.left = TreeNode(3)
    # t.right.right = TreeNode(8)
    res = sol.isValidBST(t)
    print(res)