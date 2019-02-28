# A string is an array of characters and they are used to name variables, and pass information within a paython program
my_first_string = "hello world"
# capitalize the first letter of the string
print(my_first_string.capitalize())
# ctrl+D- Duplicate a line

# make every letter of the string capital
print(my_first_string.upper())

# make every letter of the string lower
print(my_first_string.lower())

# counting the number of o's or rather any specified letter
print(my_first_string.count("o"))

# joining strings- multiple assignment
first_name, second_name = "Jacque","Chemutai"

# concatenating two strings
full_name = first_name+ " "  + second_name
print(full_name)

first_letter = full_name[0]
print(first_letter)
# determining the length of a  string
# length of_my_full_name = len(full_name)
last_letter = full_name [-1]
last_letter = full_name[len(full_name)-1]
print(last_letter)


