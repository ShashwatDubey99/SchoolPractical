with open("txt_files/for7and8.txt") as f:
    data=f.read()
    n_vowels=0
    n_consonants=0
    n_uppercase=0
    n_lowercase=0
    for i in data:
        if i.lower() in "aeiou":
            n_vowels+=1
        elif i.lower() in "bcdfghjklmnpqrstvwxyz":
            n_consonants+=1
        if i.isupper():
            n_uppercase+=1
        elif i.islower():
            n_lowercase+=1
    print({"Vowels: ":n_vowels,
           "Consonants: ":n_consonants,
           "Uppercase: ":n_uppercase,
           "Lowercase: ":n_lowercase})