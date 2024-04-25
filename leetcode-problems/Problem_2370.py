dp = [0] * 26
s = 'acfgbd'
k = 2
for c in s:
    cur = ord(c) - ord('a')
    longest = 1
    for prev in range(26):
        if abs(cur - prev) <= k:
            longest = max(longest, 1+dp[prev])
    dp[cur] = max(dp[cur], longest)

    print(max(dp))
