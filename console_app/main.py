prenomOK = False
ageOK = False

while not prenomOK:
    prenom = input("Prénom : ")
    
    if prenom.strip() == "":
        print("Erreur : Le prénom ne doit pas être vide")
    else:
        prenomOK = True
        
while not ageOK:
    age = input("Age : ")

    try:
        age_prochain = int(age) + 1
    except ValueError:
        print("Erreur : Vous devez saisir un nombre pour l'age")
    else:
        ageOK = True
        
# print(type(prenom))
# print(type(age))
        
# print("Hello " + prenom + ", tu as " + age + " ans !")
print(f"Hello {prenom}, tu as {age} ans !")
print("L'an prochain tu auras " + str(age_prochain) + " ans !")
