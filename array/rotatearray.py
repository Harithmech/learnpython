# given array arr
# given integer k
# rotate the array by k units
# clockwise --> pick an element from end and place it upfront

arr = [1, 5, 2, 4, 3]

k = 3
for i in range(k):
    temp = arr[-1]
    for j in range(len(arr)-1, 0, -1):
        arr[j] = arr[j-1]
    arr[0] = temp

print(arr)
