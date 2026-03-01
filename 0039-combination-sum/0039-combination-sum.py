class Solution:
    def combinationSum(self, candidates, target):
        result = []

        def backtrack(start, path, remaining):
            # Base Case
            if remaining == 0:
                result.append(path[:])
                return
            if remaining < 0:
                return

            # Try all possibilities
            for i in range(start, len(candidates)):
                path.append(candidates[i])  # choose
                backtrack(i, path, remaining - candidates[i])  # reuse allowed
                path.pop()  # undo (backtrack)

        backtrack(0, [], target)
        return result