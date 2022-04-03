student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

for (index, row) in student_data_frame.iterrows():
    pass

df = pandas.read_csv("nato_phonetic_alphabet.csv", header=0)
df = df.set_index('letter')

dictionary = {index:row[0] for (index, row) in df.iterrows()}
print(dictionary)



is_alphabet = True
while is_alphabet:
    word = input("Please enter a word:").upper()
    try:
        nato = [dictionary[letter] for letter in word]
        is_alphabet = False
    except KeyError as e:
        print("Sorry, only letters in the alphabet please. ")
    else:
        print(nato)