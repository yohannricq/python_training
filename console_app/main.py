def ask_firstname():
    prenomOK = False
    while not prenomOK:
        prenom = input("Prénom : ")
    
        if prenom.strip() == "":
            print("Erreur : Le prénom ne doit pas être vide")
        else:
            prenomOK = True
            
    return prenom

def ask_age(prenom):
    ageOK = False
    while not ageOK:
        age_str = input(f"Age de {prenom} : ")

        try:
            age = int(age_str)
        except ValueError:
            print("Erreur : Vous devez saisir un nombre pour l'age")
        else:
            ageOK = True
            
    return age

def showPersonInfos(prenom, age):
    print(f"Hello {prenom}, tu as {age} ans !")
    
    # infos_majeur = ""
    # infos_mineur = ""
    
    # if age == 17:
    #     print("Tu es presque majeur")
    # elif age == 18:
    #     print("Tu es tout juste majeur")
    # elif age > 18:
    #     infos_majeur = "Tu es majeur"
    #     if age > 60:
    #         infos_majeur += " et tu es un sénior"
    #     print(infos_majeur)
    # else:
    #     infos_mineur = "Tu es mineur"
    #     if age < 10:
    #         infos_mineur += " et tu es un enfant"
    #     print(infos_mineur)
        
    if age == 17:
        print("Tu es presque majeur")
    elif age == 18:
        print("Tu es tout juste majeur")
    elif age > 60:
        print("Tu es un sénior")
    elif age > 18:
        print("Tu es majeur")
    elif age < 10:
        print("Tu es un enfant")
    else:
        print("Tu es mineur")

prenom1 = ask_firstname()
prenom2 = ask_firstname()

age1 = ask_age(prenom1)
age2 = ask_age(prenom2)
        
showPersonInfos(prenom1, age1)
showPersonInfos(prenom2, age2)
