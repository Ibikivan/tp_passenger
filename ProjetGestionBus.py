#On implémente la fonctionnalité de création des bus
def ajoutBus(idBus):
    #on commence par réunir les informations nécessaire à la création du dictionnaire bus
    #on commence par récupérer l'identifiant depuis une varible déclaré à l'avance puis on l'incrémentera après exécution de la fonction
    id = idBus
    
    #puis on initialise le tableau contenant le nom des passager
    passagers = []
    
    #et enfin on demande à l'utilisateur soit d'entrer un nombre de places max, soit d'utiliser le nombre de places par défaut
    print("Voulez-vous utiliser le nombre de places par défaut pour ce bus ?")
    print("")
    choixPlaces = input("si oui tapez 'Entrer', sinon entrez directement le NOMBRE DE PLACES pour ce bus : ")
    nombreDeplaces = 0
    
    #S'il n'entre rien on prend le nombre de places par défaut
    if choixPlaces:
        nombreDeplaces = int(choixPlaces)
    else:
        nombreDeplaces = 50
    
    #on crée le dictionnaire et on le retourne    
    bus = {"busId" : id,
           "placesMax" : nombreDeplaces,
           "placesDispo" : nombreDeplaces,
           "passagers" : passagers}
    
    return bus

#On implémente la fonctionnalité de création des passager
def ajoutPassagers(idPassager):
    #on commence par réunir les informations nécessaire à la création du dictionnaire passager
    #on commence par récupérer l'identifiant depuis une varible déclaré à l'avance puis on l'incrémentera après exécution de la fonction
    id = idPassager
    
    #puis on récurère dans une variable le nom du passager
    nomPassager = input("Veuillez entrer le nom de ce passage: ")
    
    #et enfin on recupère le poid des bagages du passager en question
    poidsBagages = input("Veuillez indiquer le poid des bagages de ce passager:  ")
    
    #on crée le dictionnaire passager et on le retourne    
    passager = {"idPassager" : id,
           "nomPassager" : nomPassager,
           "poidBagages" : poidsBagages}
    
    return passager

#On réalise la fonctionnalité d'ajout de passagers aux bus
#pour cela on va créer une fonction qui iras lire les tableaux contenant les utilisateurs et les bus et faire transiter les informations
def ajoutPassagersBus(numeroBus):
    busActuel = buss[numeroBus]
    print("Voulez-vous remplir le bus ?")
    nombreACharger = int(input("si oui tapez sur 'Entrer', sinon saisissez lz nombre de places à charger: "))

    if nombreACharger:
        for i in range(0, nombreACharger):
            busActuel["passagers"].append(passagers[i])
            buss[numeroBus] = busActuel
            busActuel["placesDispo"] -= 1
    else:
        for i in range(0, busActuel["placesMax"]):
            busActuel["passagers"].append(passagers[i])
            buss[numeroBus] = busActuel
            busActuel["placesDispo"] -= 1

    return numeroBus


idBus = 0
idPassager = 0
passagers = []
buss = []

for i in range(0, 3):
    buss.append(ajoutBus(idBus))
    passagers.append(ajoutPassagers(idPassager))
    idBus += 1
    idPassager += 1

numeroBus = int(input("Entrer le numero du bus à charger: "))    
ajoutPassagersBus(numeroBus)

print("")
print(buss[numeroBus])
print("")


print(passagers)
print(buss)