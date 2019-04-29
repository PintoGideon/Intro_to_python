# Take an array of numbers
# Have a flag
# Sort the array
# Loop through the elements in the array
# Skipping the first element will give you the max
# Skipping the last element will you the min


def minMaxSum(arr):
    sum = 0

    for i in range(len(arr)):
        sum += arr[i]
    print(sum-max(arr), sum-min(arr))
