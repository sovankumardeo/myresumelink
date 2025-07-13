def solve():
    MOD = 998244353
    
    # Read input
    N = int(input())
    M = int(input())
    K = int(input())
    
    # Read dx values
    dx = []
    for _ in range(K):
        dx.append(int(input()))
    
    # Read dy values
    dy = []
    for _ in range(K):
        dy.append(int(input()))
    
    # Read X coordinates of forbidden zones
    X = []
    for _ in range(M):
        X.append(int(input()))
    
    # Read Y coordinates of forbidden zones
    Y = []
    for _ in range(M):
        Y.append(int(input()))
    
    # Create set of forbidden zones
    forbidden = set()
    for i in range(M):
        forbidden.add((X[i], Y[i]))
    
    # DP: dp[step][(x,y)] = number of ways to reach (x,y) after exactly 'step' jumps
    dp = [{} for _ in range(N + 1)]
    dp[0][(0, 0)] = 1
    
    # Fill DP table
    for step in range(1, N + 1):
        for (x, y), ways in dp[step - 1].items():
            for i in range(K):
                # Try each movement pattern
                nx, ny = x + dx[i], y + dy[i]
                
                # Skip if this position is forbidden
                if (nx, ny) not in forbidden:
                    if (nx, ny) not in dp[step]:
                        dp[step][(nx, ny)] = 0
                    dp[step][(nx, ny)] = (dp[step][(nx, ny)] + ways) % MOD
    
    # Sum all valid positions after N jumps
    result = sum(dp[N].values()) % MOD
    print(result)

solve()