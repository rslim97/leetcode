# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root.left and not root.right:
            return 0
        sum=[0]
        def dfs(root, sum):
            if not root:
                return
            if not root.left and not root.right:
                return
            if root.left:
                # detect left leaf
                if not root.left.left and not root.left.right:
                    sum[0]+=root.left.val
            dfs(root.left, sum)
            dfs(root.right, sum)
        
        dfs(root,sum)
        return sum[0]
            



if __name__ == '__main__':
    # r = TreeNode(3)
    # r.left = TreeNode(9)
    # r.right = TreeNode(20)
    # r.right.left = TreeNode(15)
    # r.right.left.right = TreeNode(12)
    # r.right.left.right.left = TreeNode(14)
    # r.right.right = TreeNode(7)

    r = TreeNode(1)
    r.left = TreeNode(2)
    r.left.right = TreeNode(3)
    r.left.right.left = TreeNode(4)

    sol = Solution()
    res = sol.sumOfLeftLeaves(r)
    print(res)