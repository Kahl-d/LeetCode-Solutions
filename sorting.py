# Name: Khalid Mehtab Khan
# Date: 01/09/2024
# Description: This is a python program to sort an array using bubble sort algorithm.

arr = [64, 34, 25, 12, 22, 11, 90]

def bubbleSort (arr):

    didSwap = True
    n = len(arr)
    while didSwap:
        didSwap = False

        for i in range(0, n-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                didSwap = True

        n -= 1

    return arr


print("Original array: ", arr)
print("Sorted array: ", bubbleSort(arr))