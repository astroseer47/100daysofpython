import pandas


data = pandas.read_csv("./nato_phonetic_alphabet.csv")

for index, row in data.iterrows():
    print(row.code)

new_object = {row.letter:row.code for (i, row) in data.iterrows()}
print(new_object)

while True:
    try:
        word = input("Enter word: ").upper()
        output_list = [new_object[letter] for letter in word]
        print(output_list)
    except KeyError:
        print("Please enter a valid word")