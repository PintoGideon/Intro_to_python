# Hackerrank:


# Take an array of inputs
# Check for positive , negative and fractions in the array
# Divide each count by the total number of elements in the array


def plusMinus(arr):
    positiveFrac = 0
    negativeFrac = 0
    zeroFrac = 0
    length = len(arr)

    for i in range(len(arr)):
        if(i > 0):
            positiveFrac += 1
        elif(i < 0):
            negativeFrac += 1
        else:
            zeroFrac += 1

    print(positiveFrac/length, negativeFrac/length, zeroFrac/length)


n = int(input())

arr = list(map(int, input().rstrip().split()))

plusMinus(arr)
