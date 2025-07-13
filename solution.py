def solve():
    MOD = 10**9 + 7
    
    # Read input
    n = int(input())
    input()  # Skip the "3"
    
    portals = []
    for _ in range(n):
        r, b, w = map(int, input().split())
        portals.append([r, b, w])
    
    q = int(input())
    input()  # Skip the "4"
    
    queries = []
    for _ in range(q):
        query = list(map(int, input().split()))
        queries.append(query)
    
    xor_result = 0
    
    for query in queries:
        if query[0] == 0:
            # Type 0 query: count paths
            u, v, c = query[1], query[2], query[3]
            
            # DP approach
            # dp[i][color] = number of ways to reach room i with card color
            # color: 0 = red, 1 = blue
            dp = [[0, 0] for _ in range(n + 1)]
            dp[u][c] = 1
            
            for i in range(u, v):
                red_portals, blue_portals, white_portals = portals[i - 1]
                
                # From room i with red card
                if dp[i][0] > 0:
                    # Use red portals (stay red)
                    dp[i + 1][0] = (dp[i + 1][0] + dp[i][0] * red_portals) % MOD
                    # Use white portals (switch to blue)
                    dp[i + 1][1] = (dp[i + 1][1] + dp[i][0] * white_portals) % MOD
                
                # From room i with blue card
                if dp[i][1] > 0:
                    # Use blue portals (stay blue)
                    dp[i + 1][1] = (dp[i + 1][1] + dp[i][1] * blue_portals) % MOD
                    # Use white portals (switch to red)
                    dp[i + 1][0] = (dp[i + 1][0] + dp[i][1] * white_portals) % MOD
            
            # Answer is number of ways to reach room v with the same color we started with
            answer = dp[v][c]
            xor_result ^= answer
            
        else:
            # Type 1 query: update portals
            i, r, b, w = query[0], query[1], query[2], query[3]
            portals[i - 1] = [r, b, w]
    
    return xor_result

print(solve())