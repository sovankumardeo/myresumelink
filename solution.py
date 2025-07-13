"""
Solution to the Quantum Jump Boots problem on planet Zyphora

Problem: Find the number of valid ways to complete exactly N jumps using K movement patterns
while avoiding M forbidden zones.

Algorithm: Dynamic Programming
- Use a dictionary to track the number of ways to reach each position after each jump
- For each jump, calculate all possible next positions from current positions
- Only count positions that are not in the forbidden zones
- Return the sum of all ways after N jumps

Time Complexity: O(N * K * |reachable_positions|)
Space Complexity: O(|reachable_positions|)
"""

def solve():
    MOD = 998244353
    
    # Read input
    N = int(input())  # Number of jumps
    M = int(input())  # Number of forbidden zones
    K = int(input())  # Number of movement patterns
    
    dx = []
    dy = []
    
    # Read movement patterns
    for _ in range(K):
        dx.append(int(input()))
    
    for _ in range(K):
        dy.append(int(input()))
    
    # Read forbidden zones coordinates
    X = []
    Y = []
    
    # Read all X coordinates first
    for i in range(M):
        X.append(int(input()))
    
    # Read all Y coordinates
    for i in range(M):
        Y.append(int(input()))
    
    # Create forbidden zones set for O(1) lookup
    forbidden = set()
    for i in range(M):
        forbidden.add((X[i], Y[i]))
    
    # DP: current_dp[pos] = number of ways to reach position pos
    current_dp = {(0, 0): 1}  # Start at origin with 1 way
    
    # Process each jump
    for jump in range(N):
        next_dp = {}
        
        # For each current position and its count
        for (x, y), count in current_dp.items():
            # Try all K movement patterns
            for i in range(K):
                new_x = x + dx[i]
                new_y = y + dy[i]
                new_pos = (new_x, new_y)
                
                # If new position is not forbidden, add to next_dp
                if new_pos not in forbidden:
                    if new_pos not in next_dp:
                        next_dp[new_pos] = 0
                    next_dp[new_pos] = (next_dp[new_pos] + count) % MOD
        
        current_dp = next_dp
    
    # Sum all ways after N jumps
    result = sum(current_dp.values()) % MOD
    print(result)

solve()