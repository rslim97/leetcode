class Solution(object):
    def exist(self,matrix,input_word):
        if not matrix:
            return False
        
        directions = ((-1,0),(0,1),(1,0),(0,-1))
        rows, cols = len(matrix), len(matrix[0])
        # check for edge case
        unique_elements_set = set()
        for r in range(rows):
            for c in range(cols):
                unique_elements_set.add(matrix[r][c])
        input_word_set = set(input_word)
        if len(input_word_set)>len(unique_elements_set):
            return False
        
        def dfs(i,j,word,visited, depth):
            # base case
            print("word ", word)
            if word==input_word:
                print(word)
                return True
            if word[:depth]!=input_word[:depth]:
                return False
            if len(word)>len(input_word):
                return False
            for direction in directions:
                next_i, next_j = i+direction[0], j+direction[1]
                if 0<=next_i<rows and 0<=next_j<cols and (next_i, next_j) not in visited:
                    # visit children
                    visited.add((next_i, next_j))
                    word+=matrix[next_i][next_j]
                    if dfs(next_i, next_j, word, visited, depth+1):
                        return True
                    # backtrack
                    word=word[:-1]
                    visited.remove((next_i,next_j))

            return False

        for r in range(rows):
            for c in range(cols):
                visited = set(((r,c),))
                if dfs(r, c, matrix[r][c], visited, 1):
                    return True
        return False

if __name__ == '__main__':
    sol = Solution()
    matrix = [["a","a"]]
    matrix = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    # matrix=[["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"]]
    # matrix = [["A"]]
    # res=sol.exist(matrix,"AAAAAAAAAAAAABB")
    res=sol.exist(matrix,"ASADFC")
    # res=sol.exist(matrix,"aa")
    print(res)