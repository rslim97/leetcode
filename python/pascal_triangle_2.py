class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        # use caching like solving fibonacci number
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1,1]
        prev = [1,1]
        for j in range(2,rowIndex+1):
            temp=[1]
            for i in range(j-1):
                temp.append(prev[i]+prev[i+1])
            temp.append(1)
            prev=temp
        return prev




if __name__ == '__main__':
    sol = Solution()
    rowIndex = 0
    res = sol.getRow(rowIndex)
    print(res)