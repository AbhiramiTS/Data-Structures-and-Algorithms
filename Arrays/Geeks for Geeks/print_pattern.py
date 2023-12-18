class Solution:
    def pattern(self, N):
        pattern_list = []
        pattern_list.append(N)
        print(N, end="")
        if len(pattern_list) > 1 and pattern_list[-1] == pattern_list[0]:
            return 

        if N > 0:
            # new_n = N - 5
            return
        else:
            new_n = N + 5

        return pattern_list.append(self.pattern(new_n))


solution = Solution()
result = solution.pattern(9)
print(result)
