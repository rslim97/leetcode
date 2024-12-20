# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """
        if not root:
            return False
        def dfs(root, sum, targetSum):
            if not root.left and not root.right:  # detect leaf
                return sum==targetSum
            if root.left:
                if dfs(root.left,sum+root.left.val,targetSum):
                    return True  # immediately return True if True
            if root.right:
                if dfs(root.right,sum+root.right.val,targetSum):
                    return True
            return False  # default value return False
        return dfs(root, root.val, targetSum)


if __name__ == '__main__':
    r = TreeNode(5)
    r.left = TreeNode(4)
    r.right = TreeNode(8)
    r.left.left = TreeNode(11)
    r.right.left = TreeNode(13)
    r.right.right = TreeNode(4)
    r.left.left.left = TreeNode(7)
    r.left.left.right = TreeNode(2)

    sol = Solution()
    res = sol.hasPathSum(r, 17)
    print(res)