# We have n candles with varying heights
# Loop through the array
# Find the max
# Compare the values with Max and if the value is present, increament flag


def birthdayCakeCandles(arr):

    count = 0
    biggest = max(arr)

    for i in range(len(arr)):
        if(arr[i] == biggest):
            count += 1
        return count
