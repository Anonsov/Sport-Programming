k = 3
a = [1, 1, 2, 2, 2, 3, 4, 4, 4] 
series = []
start = 0

for i in range(1, len(a)):
    if a[i] != a[i - 1]:
        series.append((start, i))
        start = i
series.append((start, len(a) - 1)) 
print(series)

if len(series) >= k:
    f_start, f_end = series[0][0], series[0][1]
    k_start, k_end = series[k-1][0], series[k-1][1]
    first_series = a[f_start:f_end]
    k_series = a[k_start:k_end]
    a[f_start:f_end] = k_series
    a[k_start:k_end] = first_series
    print(a)    