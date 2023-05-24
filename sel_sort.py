def selection_sort(arr):
    n = len(arr)
    for i in range(n-1):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]


# Get input from the user
n = int(input("Enter the number of elements: "))
arr = []
for i in range(n):
    element = int(input("Enter element {}: ".format(i+1)))
    arr.append(element)

# Perform selection sort
selection_sort(arr)

# Print the sorted array
print("Sorted array:", arr)
