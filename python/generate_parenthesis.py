class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        def dfs(sol, n_open, n_close):
            if n_open+n_close==0:
                res.append(sol[:])
                return
            if n_open+n_close<0:
                return
            if n_open>0:
                sol+='('
                dfs(sol, n_open-1, n_close+1)
                # backtrack
                sol=sol[:-1]
            if n_close>0:
                sol+=')'
                dfs(sol, n_open, n_close-1)
                sol=sol[:-1]
            
        dfs('', n, 0)
        return res
    
if __name__ == '__main__':
    sol = Solution()
    n = 4
    res = sol.generateParenthesis(n)
    print(res)