class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows==1:
            return [[1]]
        sol = [[1],[1,1]]
        # j is the index for numRows>2
        for j in range(2,numRows):
            temp=[1]
            for i in range(j-1):
                temp.append(sol[j-1][i]+sol[j-1][i+1])
            temp.append(1)
            sol.append(temp)
        return sol


if __name__ == '__main__':
    sol = Solution()
    numRows = 4
    res = sol.generate(numRows)
    print(res)