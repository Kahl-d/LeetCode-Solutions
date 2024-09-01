# Name: Khalid Mehtab Khan
# Date: 01/09/2024

# Description: This is a python program to sort an array using different sorting algorithms.

# Bubble Sort

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



# Selection Sort

def selectionSort(arr):
    n = len(arr)
    start = 0

    while start < n:
        minIndex = start
        for i in range(start + 1, n):
            if arr[i] < arr[minIndex]:
                minIndex = i

        arr[start], arr[minIndex] = arr[minIndex], arr[start]
        start += 1

    return arr

# print("original array: ", arr)
# print("Selection Sort: ", selectionSort(arr))




# Insertion sort

def insertionSort(arr):

    n = len(arr)

    current  = 1

    while current < n:
        i = current -1
        key = arr[current]
        while i >=0:
            if key < arr[i]:
                arr[i+1] = arr[i]
                i -= 1
            else:
                break
        
        arr[i+1] = key
        current += 1

    return arr

# print("original array: ", arr)
# print("Insertion Sort: ", insertionSort(arr))


