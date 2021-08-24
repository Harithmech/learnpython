# given array arr
# given integer k
# rotate the array by k units
# clockwise --> pick an element from end and place it upfront


# time complexity n2
# space complexity o(1)
""" arr = [1, 5, 2, 4, 3]

k = 6
for i in range(k % len(arr)):
    temp = arr[-1]
    for j in range(len(arr)-1, 0, -1):
        arr[j] = arr[j-1]
    arr[0] = temp

print(arr) """


# time complecity o(n)
# space complexity o(n)

arr = [1, 2, 3, 4, 5]

arr1 = [0 for i in range(len(arr))]

k = 3

N = len(arr)
for i in range(0, len(arr)):
    # if(i % 3 == 0):
    arr1[(i+k) % N] = arr[i]

print(arr1)
