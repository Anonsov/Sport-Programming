n = 5

prev_max, prev_min = None, None
max, min = float('-inf'), float('inf')

for i in range(0, n-1):
    a = int(input())
    prev_max, prev_min = max, min  # Store previous values
    if a > max:
        max = a
    if a < min:
        min = a
    print(f"Previous max: {prev_max}, Current max: {max}")
    print(f"Previous min: {prev_min}, Current min: {min}")
print(min, max)    