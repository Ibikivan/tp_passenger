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
    
    if choixPlaces:
        nombreDeplaces = int(choixPlaces)
    else:
        nombreDeplaces = 50
        
    bus = "bus" + str(id)
    bus = {"busId" : id,
           "placesMax" : nombreDeplaces,
           "passagers" : passagers}
    
    idBus += 1
    
    return bus

idBus = 1

print(ajoutBus(idBus))
print(idBus)