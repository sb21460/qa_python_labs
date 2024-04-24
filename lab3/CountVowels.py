input_string = input("Please enter any string : ")
counter = 0
vowel_counter = 0
vowels =('a', 'e', 'i', 'o', 'u')
while counter < len(input_string):
    if input_string[counter].lower() in vowels:
        vowel_counter = vowel_counter + 1
    counter = counter + 1


print(f"There are {vowel_counter} vowels in {input_string}.")




