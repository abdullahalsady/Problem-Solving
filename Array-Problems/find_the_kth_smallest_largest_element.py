arr = [10, 103, 70, 93, 1, 24, 5]
length = len(arr)
kth = 3

# Sorting the array in ascending order to find the kth smallest element
for i in range(length - 1):
    for j in range(length - i - 1):
        if arr[j] > arr[j + 1]:
            # Swap elements if they are in the wrong order
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Print the kth smallest element
print(f"Kth smallest element is: {arr[kth - 1]}")

# Sorting the array in descending order to find the kth largest element
for i in range(length - 1):
    for j in range(length - i - 1):
        if arr[j] < arr[j + 1]:
            # Swap elements if they are in the wrong order
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Print the kth largest element
print(f"Kth largest element is: {arr[kth - 1]}")
