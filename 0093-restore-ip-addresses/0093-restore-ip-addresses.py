class Solution:
    def restoreIpAddresses(self, s):
        res = []

        def backtrack(index, parts, path):
            # Found 4 parts
            if parts == 4:
                if index == len(s):
                    res.append(".".join(path))
                return

            # Try segments of length 1, 2, and 3
            for length in range(1, 4):
                if index + length > len(s):
                    break

                segment = s[index:index + length]

                # Leading zero is not allowed
                if len(segment) > 1 and segment[0] == '0':
                    continue

                # Must be <= 255
                if int(segment) > 255:
                    continue

                path.append(segment)
                backtrack(index + length, parts + 1, path)
                path.pop()

        backtrack(0, 0, [])
        return res