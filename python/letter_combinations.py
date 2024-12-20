class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        mapping = {"2":"abc","3":"def",
                   "4":"ghi","5":"jkl",
                   "6":"mno","7":"pqrs",
                   "8":"tuv","9":"wxyz"}
        
        if len(digits)<=0:
            return []
        res = []
        def dfs(digits,word,depth):
            if len(word)==len(digits):
                res.append(word[:])
            if depth>=len(digits):
                return
            for children in mapping[digits[depth]]:
                word+=children
                dfs(digits,word,depth+1)
                word=word[:-1]
        
        for c in mapping[digits[0]]:
            dfs(digits,c,1)
        return res

if __name__ == '__main__':
    sol=Solution()
    digits="23"
    res=sol.letterCombinations(digits)
    print(res)
            