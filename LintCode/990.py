import itertools

class Solution:
    """
    @param N: The number of integers
    @return: The number of beautiful arrangements you can construct
    """
    def countArrangement(self, N):
        self.count = 0

        for n in range(N):
            visited = [ False for n in range(N) ]    # i th = i + 1
            self.dfs(n, 1, visited[:])

        return self.count

    def dfs(self, v, i, visited):
        if (v+1) % i != 0 and i % (v+1) != 0:
            return

        visited[v] = True

        if not False in visited:
            self.count += 1

        for w, is_visited in enumerate(visited):
            if not is_visited:
                self.dfs(w, i+1, visited[:])


sol = Solution()
N = 5
print(sol.countArrangement((N)))

'''
# Brute-force
def countArrangement(self, N):
    numbers = [ i+1 for i in range(N)]
    all_arrangements = itertools.permutations(numbers, N)
    beautiful_num = 0
    
    for arrangement in all_arrangements:
        flag = True
        for position, num in enumerate(arrangement):
            if (position+1) % num != 0 and num % (position+1) != 0:
                flag = False
                break
        if flag == True:
            beautiful_num += 1
    
    return beautiful_num
'''