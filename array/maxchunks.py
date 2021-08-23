# Maximum number of chunk that array can be split into
# problem : Array with n elements, with arr[permutations till 0, n-1]
# split the array into chunks(partitions)
# no shuffling of chunks
# concateniate and the result is sorted array
# most number of chunks that can be made

# Clue: chaining technique is used to make chunks

arr = [1, 0, 2, 3, 4]
a = 0
count = 1
for i in range(1, len(arr)):
    if arr[a] < arr[i]:
        count += 1
        a = i
print(count)


# count starts from 1, if the array is in decreasing order chunk is 1
