# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: List[List[int]]
        """
        if not root:
            return []
        res = []
        sol = [root.val]
        def dfs(root, sol, res, targetSum):
            # 
            if not root.left and not root.right:
                if sum(sol)==targetSum:
                    res.append(sol[:])
                return
            if root.left:
                sol.append(root.left.val)
                dfs(root.left, sol, res, targetSum)
                # backtrack
                sol.pop()
            if root.right:
                sol.append(root.right.val)
                dfs(root.right, sol, res, targetSum)
                # backtrack
                sol.pop()
            return
        
        dfs(root, sol, res, targetSum)
        return res

if __name__ == '__main__':
    # r = TreeNode(5)
    # r.left = TreeNode(4)
    # r.right = TreeNode(8)

    # r.left.left = TreeNode(11)
    # r.left.left.left = TreeNode(7)
    # r.left.left.right = TreeNode(2)

    # r.right.left = TreeNode(13)
    # r.right.right = TreeNode(4)
    # r.right.right.left = TreeNode(5)
    # r.right.right.right = TreeNode(1)

    r = TreeNode(1)
    r.left = TreeNode(2)
    r.right = TreeNode(3)

    sol = Solution()
    res = sol.pathSum(r, 5)
    print(res)