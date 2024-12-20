class Solution(object):
    def letterCasePermutation(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []
        def dfs(word, s, depth):
            if len(word)==len(s):
                res.append(word[:])
                return
            if depth>=len(s):
                return
            c = s[depth]
            # check if string is from alphabet
            if c.isalpha():
                if c.islower():
                    word+=c
                    dfs(word, s, depth+1)
                    # backtrack
                    word=word[:-1]
                    word+=c.upper()
                    dfs(word, s, depth+1)
                    # backtrack
                    word=word[:-1]
                else:
                    word+=c.lower()
                    dfs(word, s, depth+1)
                    word=word[:-1]
                    word+=c
                    dfs(word, s, depth+1)
                    word=word[:-1]
            # check if string is a number
            elif c.isnumeric():
                word+=c
                dfs(word, s, depth+1)
                word=word[:-1]
            else:
                return
        
        dfs('', s, 0)
        return res



if __name__ == '__main__':
    sol = Solution()
    # s="a1b2"
    s="TB"
    res = sol.letterCasePermutation(s)
    print(res)