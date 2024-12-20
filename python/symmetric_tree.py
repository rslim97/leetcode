from collections import deque
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __str__(self):
        return '{}'.format(self.val)
    def __repr__(self):
        return self.__str__()
    
# iterative (bfs)
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        # same like comparing two trees traversed using bfs 
        # with different child ordering left-right, right-left.
        queue_1 = deque([root])
        queue_2 = deque([root])
        while queue_1 and queue_2:
            print(queue_1)
            print(queue_2)
            current_1 = queue_1.popleft()
            current_2 = queue_2.popleft()
            # bfs add left child then right child
            if not current_1 and not current_2:
                continue
            elif not current_1 or not current_2:
                return False
            if current_1.val != current_2.val:
                return False
            # if current_1.left:
            queue_1.append(current_1.left)
            # if current_1.right:
            queue_1.append(current_1.right)

            # bfs add right child then left child
            # if current_2.right:
            queue_2.append(current_2.right)
            # if current_2.left:
            queue_2.append(current_2.left)

        return True

# recursive
# class Solution(object):
#     def isSymmetric(self, root):
#         """
#         :type root: Optional[TreeNode]
#         :rtype: bool
#         """

#         def helper(root1, root2):
#             if not root1 and not root2:
#                 return True
#             elif not root1 or not root2:
#                 return False
#             if root1.val!=root2.val:
#                 return False
#             if helper(root1.left,root2.right) and helper(root1.right,root2.left):
#                 return True
#             return False
        
#         return helper(root,root)
    


if __name__ == '__main__':
    sol = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    # root.left.left = TreeNode(4)
    root.left.right = TreeNode(3)
    # root.right.left = TreeNode(6)
    # root.right.right = TreeNode(3)
    # root.left.right = TreeNode(3)
    # root.right.right = TreeNode(2)
    # res=sol.isSymmetric(root)
    res=sol.isSymmetric(root)
    print(res)