def decode_message( s: str, p: str) -> bool:

# write your code here
        m, n = len(s), len(p)

    # Create a DP table initialized to False
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True  # Empty pattern matches empty string

    # Handle patterns that start with '*' as they can match an empty string
        for j in range(1, n + 1):
                if p[j - 1] == '*':
                        dp[0][j] = dp[0][j - 1]

    # Fill the DP table
        for i in range(1, m + 1):
                for j in range(1, n + 1):
                        if p[j - 1] == s[i - 1] or p[j - 1] == '?':
                                dp[i][j] = dp[i - 1][j - 1]  # Character match or '?' matching one character
                        elif p[j - 1] == '*':
                                dp[i][j] = dp[i - 1][j] or dp[i][j - 1]  # '*' matching sequence or empty

    # Return True if the entire string matches the pattern
        if dp[m][n]:
                return True

    # Return False if the pattern doesn't match the string
        return False