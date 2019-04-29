# Hackerrankhttps://www.hackerrank.com/challenges/a-very-big-sum/problem


def calculateSum(arr):
    sum = 0

    for i in range(len(arr)):
        sum += arr[i]

    return arr


ar_count = int(input())
ar = list(map(int, input().strip().split()))
calculateSum(ar)
