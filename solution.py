import sys

def solve(N, M, H):
    # Binary search on the answer
    left, right = 1, 10**9
    
    def can_form_team(x):
        # Create bitmasks for each hero
        mask_count = {}
        for i in range(N):
            mask = 0
            for k in range(M):
                if H[i][k] >= x:
                    mask |= (1 << k)
            mask_count[mask] = mask_count.get(mask, 0) + 1
        
        # Check if any two masks can combine to form the target
        target = (1 << M) - 1  # All skills must be >= x
        for mask1 in mask_count:
            for mask2 in mask_count:
                if (mask1 | mask2) == target:
                    return True
        return False
    
    while left < right:
        mid = (left + right + 1) // 2
        if can_form_team(mid):
            left = mid
        else:
            right = mid - 1
    
    return left

def main():
    N = int(sys.stdin.readline().strip())
    M = int(sys.stdin.readline().strip())
    H = []
    for _ in range(N):
        H.append(list(map(lambda x: int(x), sys.stdin.readline().strip().split(" "))))
    result = solve(N, M, H)
    print(result)

if __name__ == "__main__":
    main()