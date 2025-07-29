# Définir une variable contenant le nom d'utilisateur du joueur
pseudo = "Link"

# Définir une variable contenant l'âge du joueur
age = 15

# Assigner la vie du joueur à 5
vie = 5

# Assigner le mana du joueur à 100
mana = 100

# Ajouter 15 points de vie au joueur
vie += 15

# Multiplier le mana par 2
mana *= 2

# Assigner une variable séparée contenant 10 tirets, afficher la barre de séparation à chaque print()
separateur = '-' * 10

# Afficher le pseudo tout en majuscules
print(f"PSEUDO : {pseudo.upper()}")
print(separateur)

# Afficher l'âge divisé par 2
print(f"Âge : {age / 2}")
print(separateur)

# Afficher la vie avec 2 points de vie en moins
print(f"Vie : {vie - 2}")
print(separateur)

# Afficher la moitié du mana
print(f"Mana : {mana / 2}")
print(separateur)
