# total rain water trapped in histogram

arr = [3, 0, 6, 1, 5]  # output :  4

n = len(arr)  # 8

arr1 = [0 for i in range(len(arr))]
for i in range(1, n-1):
    ngl = 0
    for j in range(0, i):
        ngl = max(arr[i], arr[j])
    ngr = 0
    for k in range(i+1, n):
        ngr = max(arr[i], arr[k])
    arr1[i] = min(ngl, ngr) - arr[i]
print(sum(arr1))
