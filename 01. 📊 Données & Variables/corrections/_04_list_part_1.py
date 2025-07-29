# --- NIVEAU 1 ---

# La fonction str() sert à convertir un objet en chaîne de caractère.

# Définir une variable contenant une liste de chaînes de caractère pomme, épée, potion, pioche, pain ensuite affiche la liste
inventaire = ["pomme","épée","potion","pioche","pain"] # On utilise la syntaxe d'une liste [] et chaque objets séparées de ,
print("Inventaire : " + str(inventaire)) # On affiche la liste

# Changer la valeur du 3 élément dans la liste en parchemin
inventaire[2] = "parchemin" # On commence à compter à partir de 0 en programmation donc l'élément 3 est le 2
print("Inventaire : " + str(inventaire))

# Changer la valeur du dernière élément de la liste en chocolatine (Sans utiliser son ID)
inventaire[-1] = "chocolatine" # On récupère le premier des dernier élément avec un nombre négatif 😉
print("Inventaire : " + str(inventaire))

# Ajouter l'item sac à dos et sabre à l'inventaire 
inventaire += ["sac à dos","sabre"] # Pour ajouter un élément à une liste on l'additionne via une autre liste les 2 listes fusionne. J'ai utiliser l'opérateur d'assignation +=
print("Inventaire : " + str(inventaire))

# Définis un nombre et stocke-le dans une variable
i = 5
# Maintenant, utilise cette variable comme indice pour afficher un élément d’une liste
print("Objet : " + str(inventaire[i]))
# Change la valeur de i
i = 2
# Réaffiche la valeur avec la variable comme indice
print("Objet : " + str(inventaire[i]))

# Vide l'inventaire
inventaire = [] # On redéfini la l'inventaire en liste vide cela supprime tout les éléments
print("Inventaire : " + str(inventaire))

# Affiche le nombre d'items dans l'inventaire
print("Nombre d'objets : " + str(len(inventaire)))

# Crée une liste imbriquées contenant chaque item et une quantité à toi de choisir (Minimum 3 items)
inventaire = [
    ["épée", 5],
    ["potion", 3],
    ["pomme", 10]
]

# --- NIVEAU 2 ---

# Définis une nouvelle liste imbriquée contenant bois, fer, or, diamant, émeraude choisie une quantité pour chacun
ressources = [
    ["bois",81],
    ["fer",5],
    ["or",3],
    ["diamant",2],
    ["émeraude",8]
]
print("Ressources : " + str(ressources))

# Affiche le nom du premier et le dernier élément de la liste (utilise un indice positif et un négatif)
print("Premier : " + ressources[0][0]) # On récupère le premier élément de la liste qui est une liste et on récupère le premier élément de la liste qui est le nom de l'item
print("Dernier : " + ressources[-1][0]) # On récupère le dernier élément de la liste qui est une liste et on récupère le premier élément de la liste qui est le nom de l'item

# Crée une nouvelle liste imbriquée contenant 2 objets et leurs quantitées: une potion et un bouclier
loot = [["potion",3], ["bouclier",1]]

# Fusionne la liste ressources avec la liste loot dans une nouvelle liste appelée coffre
coffre = ressources + loot
print("Coffre : " + str(coffre))

# Affiche le nombre total d'objets dans le coffre
print("Nombre d'objets : " + str(len(coffre)))

# Modifie la quantité d'or ajoute en 4
coffre[2][1] = 4
print("Coffre : " + str(coffre))

# Supprime tous les éléments du coffre (vide la liste)
coffre = []
print("Coffre vidé : " + str(coffre))
print("Nombre d'objets : " + str(len(coffre)))
