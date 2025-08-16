# def minimumSensors(n: int, m: int, k: int) -> int:
#     return ((n + 2*k+1 - 1) // (2*k+1)) * ((m + 2*k+1 - 1) // (2*k+1))


def countPerfectPairs(nums):
    n = len(nums)
    cnt = 0
    
    for i in range(n):
        for j in range(i+1, n):
            a, b = nums[i], nums[j]
            abs_a, abs_b = abs(a), abs(b)
            abs_diff = abs(a - b)
            abs_sum = abs(a + b)
            
            min_abs = min(abs_a, abs_b)
            max_abs = max(abs_a, abs_b)
            min_expr = min(abs_diff, abs_sum)
            max_expr = max(abs_diff, abs_sum)
            if min_expr <= min_abs and max_expr >= max_abs:
                cnt += 1
                
    return cnt

print(countPerfectPairs([-3,2,-1,4]))