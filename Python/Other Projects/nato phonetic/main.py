import pandas

with open('./nato phonetic/nato_phonetic_alphabet.csv') as file:
    data = pandas.read_csv(file)

#print(nato)
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}

word = input("Enter a word: ").upper()

try:
    output_list = [phonetic_dict[letter] for letter in word]
except KeyError as error_msg:
    print(error_msg)

print(output_list)

# for element in nato:
#     element.replace(",",":")

# print(nato)
