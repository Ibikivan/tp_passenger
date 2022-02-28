import copy
#nous alons créer un sytème qui crée des bus, des passagers et gère les associations
#Premièrement nous allons créer un modèle de bus et un model de passagers que les programmes utiliserons pour le procésus de création

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

#créons maintenant une fonction qui va créer un bus à partir du model de bus
def busAdd(matricule, places):
    #plus tard on va donner la possibilité à l'utilisateur de selection un nombre de places par défaut
    #et un système de vérification des entrés

    currentBus = copy.deepcopy(modelBus)
    currentBus["immatriculation"] = matricule
    currentBus["placesMax"] = places
    return currentBus

#Créons une fonction créer un utilisateur à partir du model
def passengerAdd(id, name, luggageWeight):
    #ajouter un système de vérification
    currentPassenger = copy.deepcopy(modelPassenger)
    currentPassenger["id"] = id
    currentPassenger["name"] = name
    currentPassenger["luggageWeight"] = luggageWeight
    return currentPassenger

#Créons une fonction qui va ajouter un utilisateur à un groupe
def addUserToBus(user, bus):
    #il faudra l'associer à une fonction qui vérifie la presence de l'utilisateur avant de l'ajouter
    bus["passengers"].append(user)


bus1 = (busAdd("LT-530", 70))
bus2 = (busAdd("LT-540", 50))

hawa = (passengerAdd("175", "Nadia", 110))
disney = (passengerAdd("176", "Rock", 70))
maya = (passengerAdd("175", "L'abeille", 89))
van = (passengerAdd("175", "Ibiki", 15))

addUserToBus(hawa, bus1)
addUserToBus(van, bus1)
addUserToBus(maya, bus2)

print(bus1)
print(bus2)