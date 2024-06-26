#SORTING:
def bubble_sort(arr):
    """
    Bubble Sort: Compare adjacent elements and swap them if they are in the wrong order.
    """
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1): 
            if arr[j] > arr[j+1]:   
                arr[j], arr[j+1] = arr[j+1], arr[j]

def selection_sort(arr):
    """
    Selection Sort: Find the minimum element from the unsorted portion and swap it with the first element.
    """
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]  

def insertion_sort(arr):
    """
    Insertion Sort: Build the sorted array one element at a time by repeatedly inserting the next element
    into the sorted portion of the array.
    """
    n = len(arr)
    for i in range(1, n):
        key = arr[i] 
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key  


def sort_switch(choice, arr):
    """
    Switch case to choose the sorting algorithm based on user input.
    """
    if choice == 1:
        bubble_sort(arr)
    elif choice == 2:
        selection_sort(arr)
    elif choice == 3:
        insertion_sort(arr)
    else:
        print("Invalid choice. Please choose between 1, 2, or 3.")

# Test the sorting algorithms
arr = [64, 34, 25, 12, 22, 11, 90]
print("Original Array:", arr)

# Prompt the user to choose a sorting algorithm
print("Choose a sorting algorithm:")
print("1. Bubble Sort")
print("2. Selection Sort")
print("3. Insertion Sort")

choice = int(input("Enter your choice (1, 2, or 3): "))

sort_switch(choice, arr)
print("Sorted Array:", arr)

# output:
# Original Array: [64, 34, 25, 12, 22, 11, 90]
# Choose a sorting algorithm:
# 1. Bubble Sort
# 2. Selection Sort
# 3. Insertion Sort
# Enter your choice (1, 2, or 3): 1
# Sorted Array: [11, 12, 22, 25, 34, 64, 90]

# Original Array: [64, 34, 25, 12, 22, 11, 90]
# Choose a sorting algorithm:
# 1. Bubble Sort
# 2. Selection Sort
# 3. Insertion Sort
# Enter your choice (1, 2, or 3): 2
# Sorted Array: [11, 12, 22, 25, 34, 64, 90]

# Original Array: [64, 34, 25, 12, 22, 11, 90]
# Choose a sorting algorithm:
# 1. Bubble Sort
# 2. Selection Sort
# 3. Insertion Sort
# Enter your choice (1, 2, or 3): 2
# Sorted Array: [11, 12, 22, 25, 34, 64, 90]

