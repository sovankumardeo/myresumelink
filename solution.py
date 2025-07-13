import sys

def calc(N, M, K, dx, dy, X, Y):
    MOD = 998244353
    
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
    return result

def main():
    N = int(sys.stdin.readline().strip())
    M = int(sys.stdin.readline().strip())
    K = int(sys.stdin.readline().strip())
    dx = []
    for _ in range(K):
        dx.append(int(sys.stdin.readline().strip()))
    dy = []
    for _ in range(K):
        dy.append(int(sys.stdin.readline().strip()))
    X = []
    for _ in range(M):
        X.append(int(sys.stdin.readline().strip()))
    Y = []
    for _ in range(M):
        Y.append(int(sys.stdin.readline().strip()))
    result = calc(N, M, K, dx, dy, X, Y)
    print(result)

if __name__ == "__main__":
    main()