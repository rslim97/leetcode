class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        res = []
        def dfs(nums, sol, depth):
            if depth>=len(nums):
                res.append(sol[:])
                return
            dfs(nums, sol, depth+1)
            sol.append(nums[depth])
            dfs(nums, sol, depth+1)
            # backtrack
            sol.pop()

        dfs(nums,[],0)
        return res


if __name__ == '__main__':
    sol = Solution()
    nums = [1,2,2]  # unique numbers
    res = sol.subsets(nums)
    print(res)