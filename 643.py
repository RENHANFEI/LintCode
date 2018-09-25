class Solution:
    """
    @param input: an abstract file system
    @return: return the length of the longest absolute path to file
    """
    def lengthLongestPath(self, input):
        if input == "":
            return 0
            
        paths = input.split('\n')
        dir_lens = [-1]
        max_len = 0
        for path in paths:
            if path[0] != '\t':
                depth = 0
            else:
                for i, ch in enumerate(path):
                    if ch != '\t':
                        break
                depth = i
            if '.' in path:
                if depth == 0:
                    max_len = max(max_len, len(path))
                else:
                    max_len = max(max_len, len(path) - depth + dir_lens[depth - 1])
            else:
                if depth == 0:
                    dir_lens[0] = len(path) + 1
                elif depth >= len(dir_lens):
                    dir_lens.append(len(path) + 1 - depth + dir_lens[depth - 1])
                else:
                    dir_lens[depth] = len(path) + 1 - depth + dir_lens[depth - 1]
                    
        return max_len

sol = Solution()
test = "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"
print(sol.lengthLongestPath(test))