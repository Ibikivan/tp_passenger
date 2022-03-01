import copy
# nous allons créer un système qui crée des bus, des passagers et gère les associations
# Premièrement nous allons créer un modèle de bus et un model de passagers que les programmes utiliserons pour le procésus de création

modelBus = {
    "immatriculation" : "",
    "placesMax" : 0,
    "passengers" : []
}

modelPassenger = {
    "id" : "",
    "name" : "",
    "luggageWeight" : 0
}

# créons maintenant une fonction qui va créer un bus à partir du model de bus
def busAdd(matricule, places):
    # plus tard on va donner la possibilité à l'utilisateur de selection un nombre de places par défaut
    # et un système de vérification des entrés

    currentBus = copy.deepcopy(modelBus)
    currentBus["immatriculation"] = matricule
    currentBus["placesMax"] = places
    return currentBus

# Créons une fonction créer un utilisateur à partir du model
def passengerAdd(id, name, luggageWeight):
    # ajouter un système de vérification
    currentPassenger = copy.deepcopy(modelPassenger)
    currentPassenger["id"] = id
    currentPassenger["name"] = name
    currentPassenger["luggageWeight"] = luggageWeight
    return currentPassenger

# Créons une fonction qui va ajouter un passagers à un bus
def addPassengerToBus(passenger, bus):
    # il faudra l'associer à une fonction qui vérifie la presence du passager avant de l'ajouter
    # il faudra aussi vérifier qu'il y a de la place dans le bus en question
    bus["passengers"].append(passenger)

# On va créer une fonction pour connaître le nombre de places disponibes dans un bus
def isPlacesAvailable(bus):
    # On compare le nombre de places max du bus avec la longueur du tableau des passagers du bus, le resultat est la solution
    if bus["placesMax"] > len(bus["passengers"]):
        return True

# On va compter le nombre de places disponible en faisant une soustraction entre les places max et le nombre de passagers dans le tableau
def numberOfPlacesAvailable(bus):
    places = bus["placesMax"] - len(bus["passengers"])
    return places

# On va caluler le poids total des bagages des utilisateurs dans un bus
def luggageWeight(bus):
    totalWeight = 0
    for i in bus["passengers"]:
        totalWeight += i["luggageWeight"]
    return totalWeight

# Créons une fonction pour retirer un passager d'un bus
def removePassengerToBus(passenger, bus):
    # on va plus tard commencer par vérifier grâce à une fonction si l'utilisateur existe dans le bus
    bus["passengers"].remove(passenger)

# on vérifie la possibilité de tranferer les passagers d'un bus à un autre
def isBusTransfertIsPossible(incommingBus, recievingBus):
    if numberOfPlacesAvailable(recievingBus) >= len(incommingBus["passengers"]):
        return True

# Création d'une fonction qui va transférer les passagers d'un bus à un autre après avoir vérifié que sa soit possible
def TransferPasssengers(incommingBus, recievingBus):
    if isBusTransfertIsPossible(incommingBus, recievingBus):
        for i in incommingBus["passengers"]:
            recievingBus["passengers"].append(i)
            incommingBus["passengers"].remove(i) # on retire le passager après le transfert (sa ne marche pas bien)
    else:
        print("il n'y a pas suffisamment de place sur ce bus")

# Ecrivons une fonction pour afficher la liste des passagers d'un bus dans la console
def showPassengersList(bus):
    passengerNumber = 1 # un compteur à incrémenter pour afficher les numéros devant les noms
    print("Liste des passager :")
    for i in bus["passengers"]:
        print("{}. Nom : {} -> identifiant : '{}' ; poids des bagages : {} kg" . format(passengerNumber, i["name"], i["id"], i["luggageWeight"]))
        passengerNumber += 1

# Nous allons écrire une fonction qui va afficher tous les passagers de la flotte de bus
def allPassengersList(busTable):
    passengerNumber = 1  # un compteur à incrémenter pour afficher les numéros devant les noms
    print("Liste des passager :")
    for bus in busTable: # on lit le contenu de tous les bus regroupés dans un tableau
        for i in bus["passengers"]: # puis lit le contenu du tableau passagers contenu dans chaque bus
            print("{}. Nom : {} -> identifiant : '{}' ; poids des bagages : {} kg" . format(passengerNumber, i["name"], i["id"], i["luggageWeight"]))
            passengerNumber += 1

# Enfin nous allons vérifier la presence d'un passager sur un bus
# nous allons rechercher dans les tableaux de tous les bus pour vérifier si le passager est sur un bus
def isPassengerIsOnBoard(passenger, busTable):
    existence = False
    for bus in busTable:
        for i in bus["passengers"]:
            if passenger["id"] == i["id"]:
                return bus

# On affiche les détails du bus dans lequel se trouve le passager recherché
def busDetails(passenger, busTable):
    if isPassengerIsOnBoard(passenger, busTable):
        return isPassengerIsOnBoard(passenger, busTable)
    else:
        print("le passager n'existe pas")


bus1 = (busAdd("LT-530", 70))
bus2 = (busAdd("LT-540", 4))

hawa = (passengerAdd("175", "Nadia", 110))
disney = (passengerAdd("176", "Rock", 70))
maya = (passengerAdd("177", "L'abeille", 89))
van = (passengerAdd("178", "Ibiki", 15))
drey = (passengerAdd("179", "Aude", 210))

addPassengerToBus(hawa, bus2)
addPassengerToBus(van, bus1)
addPassengerToBus(disney, bus1)
addPassengerToBus(drey, bus1)

busTable = [bus1, bus2]

print(busDetails(drey, busTable))