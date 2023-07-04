arr = [10, 90, 102, 134, 90]
rev_arr = []

# Iterate over the indices of the original array in reverse order
for i in range(len(arr) - 1, -1, -1):
    # Append the element at index i to the reversed array
    rev_arr.append(arr[i])

# Update the original array with the reversed array
arr = rev_arr

# Print the reversed array
print(f"The reversed array is {arr}.")
