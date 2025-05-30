def ask_firstname():
    prenomOK = False
    while not prenomOK:
        prenom = input("Prénom : ")
    
        if prenom.strip() == "":
            print("Erreur : Le prénom ne doit pas être vide")
        else:
            prenomOK = True
            
    return prenom

def ask_age():
    ageOK = False
    while not ageOK:
        age_str = input("Age : ")

        try:
            age = int(age_str)
        except ValueError:
            print("Erreur : Vous devez saisir un nombre pour l'age")
        else:
            ageOK = True
            
    return age

prenom = ask_firstname()
age = ask_age()

age_prochain = int(age) + 1
        
print(f"Hello {prenom}, tu as {age} ans !")
print(f"L'an prochain tu auras {age_prochain} ans")
