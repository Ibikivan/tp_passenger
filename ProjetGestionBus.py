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
           "passagers" : passagers}
    
    idBus += 1
    
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
    
    idPassager += 1
    
    return passager

idBus = 1
idPassager = 1

print(ajoutPassagers(idPassager))