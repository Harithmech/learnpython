arr = [12, 5, 4, 23, 7, 100, 1]  # 0-6

n = len(arr)  # 7

maxi, maxl, maxr = 0, 0, 0

p, q, r = 1, 2, 3

for i in range(1, n-1):  # 1-6
    maxl = 0
    for j in range(0, i):
        maxl = max(maxl, p*arr[j])
    maxr = 0
    for k in range(i+1, n):
        maxr = max(maxr, r*arr[k])
    maxi = max(maxi, (maxl + q*arr[i] + maxr))

print(maxi)
