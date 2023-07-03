array = [10, 130, 53, 30, 100]
length = len(array)

for i in range(length - 1):
    for j in range(length-i-1):
        if array[j] > array[j+1]:
            array[j], array[j+1] = array[j+1], array[j]

minimum = array[0]
maximum = array[length - 1]

print(f"The maximum value of the array is {maximum} and the minimum value is {minimum}.")
