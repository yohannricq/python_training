def ask_firstname():
    prenomOK = False
    prenom = ""
    
    while not prenomOK:
        prenom = input("Prénom : ")
    
        if prenom.strip() == "":
            print("Erreur : Le prénom ne doit pas être vide")
        else:
            prenomOK = True
            
    return prenom

def ask_age(firstname):
    ageOK = False
    age = 0
    
    while not ageOK:
        age_str = input(f"Age de {firstname} : ")

        try:
            age = int(age_str)
        except ValueError:
            print("Erreur : Vous devez saisir un nombre")
        else:
            ageOK = True
            
    return age

def ask_size(firstname):
    sizeOK = False
    size = 0.0

    while not sizeOK:
        size_str = input(f"Taille de {firstname} : ")

        # Remplace la virgule par un point si nécessaire AVANT conversion
        size_str = size_str.replace(',', '.')

        try:
            size = float(size_str)
        except ValueError:
            print("Erreur : Saisie invalide")
        else:
            # Vérifie qu'il y avait bien un séparateur décimal dans la saisie d'origine
            if '.' not in size_str:
                print("Erreur : Vous devez saisir un nombre à virgule")
            else:
                sizeOK = True

    return size

def showPersonInfos(firstname, age, size=0):
    print(f"Hello {firstname}, tu as {age} ans !")
    
    # if age == 17:
    #     print("Tu es presque majeur")
    # elif 12 <= age < 18:
    #     print("Tu es adolescent")
    # elif age == 1 or age == 2:
    #     print("Tu es un bébé")
    # elif age == 18:
    #     print("Tu es tout juste majeur")
    # elif age > 60:
    #     print("Tu es un sénior")
    # elif age < 10:
    #     print("Tu es un enfant")
    # elif age >= 18:
    #     print("Tu es majeur")
    # else:
    #     print("Tu es mineur")
    
    if age == 1 or age == 2:
        print("Tu es un bébé")
    elif age < 10:
        print("Tu es un enfant")
    elif 12 <= age < 18:
        print("Tu es adolescent")
    elif age == 17:
        print("Tu es presque majeur")
    elif age == 18:
        print("Tu es tout juste majeur")
    elif age > 18:
        print("Tu es majeur")
    elif age > 60:
        print("Tu es un sénior")
    else:
        print("Tu es mineur")
        
    if not size == 0:
        print(f"Ta taille est : {size} mètres")

prenom1 = ask_firstname()
# prenom2 = ask_firstname()
# prenom3 = ask_firstname()
# prenom4 = ask_firstname()

age1 = ask_age(prenom1)
# age2 = ask_age(prenom2)
# age3 = ask_age(prenom3)
# age4 = ask_age(prenom4)

size1 = ask_size(prenom1)
        
showPersonInfos(prenom1, age1, size1)
# showPersonInfos(prenom2, age2)
# showPersonInfos(prenom3, age3)
# showPersonInfos(prenom4, age4)

# PERSONS_NUMBER = 4

# for i in range(0, PERSONS_NUMBER):
#     prenom = "prenom" + str(i + 1)
#     age = ask_age(prenom)
#     showPersonInfos(prenom, age)

