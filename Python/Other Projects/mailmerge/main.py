# This program loops through a template letter file and inserts
# a name from a list of names, thus creating a unique letter for each name

PLACEHOLDER = "[name]"

with open("./mailmerge/Names.txt") as names_file:
    names = names_file.readlines()

with open("./mailmerge/Letter.txt") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER,stripped_name)
        with open(f"./mailmerge/{stripped_name}.txt", "w") as completed_letter:
            completed_letter.write(new_letter)






