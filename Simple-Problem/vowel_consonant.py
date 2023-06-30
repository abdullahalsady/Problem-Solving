def vowel_consonant(char):
    if char == 'a' or char == 'e' or char == 'i' or char == 'u' or char == 'A' or char == 'E' or char == 'I' or char == 'O' or char == 'U':
        print(f"{char} is Vowel.")
    else:
        print(f"{char} is Consonant.")

char = input("Entet a char: ")
vowel_consonant(char)