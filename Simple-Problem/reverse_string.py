def reverse_string(string):
    new_str = ""
    length = len(string) - 1
    for i in range(length, -1, -1):
        new_str += string[i]
    return new_str

string = input("Enter a string: ")
print(reverse_string(string))
