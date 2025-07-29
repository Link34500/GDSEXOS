# --- NIVEAU 1 ---

# Afficher une chaîne de caractères contenant la phrase suivante : Bienvenue !
print("Bienvenue !")

# Afficher une chaîne de caractères contenant la phrase suivante : Mon frère m'a dit : "J'ai perdu mon stylo préféré dans l'herbe."
print("Mon frère m'a dit : \"J'ai perdu mon stylo préféré dans l'herbe.\"") 

# Afficher le mot : Menu entouré de 8 tirets devant et derrière, sans répéter les tirets
print("-"*8 + " Menu " + "-"*8) # On multiplie les chaînes et on les concatène
# ou
print(f'{"-"*8} Menu {"-"*8}') # Avec les f-strings

# Afficher la concaténation de la chaîne de caractères 'Pseudo : ' et 'MonPseudo'
print("Pseudo : " + "MonPseudo") # On concatène avec l'opérateur + et on n'oublie pas l'espace après les : sinon ça sera collé
# ou
print(f"Pseudo : {'MonPseudo'}") # Avec les f-strings

# Afficher la concaténation de la chaîne de caractères 'Endurance : ', du résultat de la division de 30 par 2 et de la chaîne de caractères '%'
print("Endurance : " + str(30/2) + "%") # On concatène la division de 30 par 2 en n'oubliant pas de convertir en chaîne de caractères avec la fonction str() 
# ou
print(f"Endurance : {30/2}%") # Avec les f-strings

# 📃 Tu as le droit de t'aider d'un moteur de recherche ou de chercher dans la documentation. IA : 🚫Interdit
# Mettre une majuscule à la première lettre de la chaîne de caractères
print("il disait que ce chien était trop mignon pour être vrai".capitalize())

# Mettre en majuscule la première lettre de la chaîne et vérifier si la chaîne de caractères finit par un .
print("cette chaîne contient uniquement des lettres minuscules.".capitalize().endswith('.'))

# Mettre tout le texte en majuscules
print("voici une phrase simple".upper())

# Vérifier si la chaîne commence par un mot spécifique
print("Bonjour tout le monde".startswith("Bonjour"))

# Compter le nombre de fois qu’un caractère apparaît dans une chaîne
print("Combien de a dans cette phrase ?".count("a"))

# Remplacer un mot par un autre dans une chaîne
print("J’aime les pommes".replace("pommes", "poires"))

# Supprimer les espaces au début et à la fin d’une chaîne
print("    trop d’espace autour    ".strip())

# Vérifier si la chaîne est composée uniquement de chiffres
print("12345".isdigit())

# Vérifier si la chaîne contient uniquement des lettres
print("JusteDesLettres".isalpha())

# Vérifier si la chaîne contient uniquement des lettres minuscules
print("toutpetit".islower())

# Vérifier si la chaîne contient uniquement des lettres majuscules
print("EN MAJUSCULE".isupper())

# --- NIVEAU 2 ---

# Mettre toute la chaîne en majuscule
print("bonjour tout le monde".upper())

# Mettre toute la chaîne en minuscules
print("HELLO WORLD".lower())

# Mettre la première lettre en majuscule
print("python est cool".capitalize())

# Remplacer un mot par un autre
print("mon chat dort".replace("chat", "chien"))

# Supprimer les espaces au début et à la fin
print("   beaucoup d'espaces   ".strip())

# Vérifier si la chaîne contient uniquement des chiffres
print("12345".isdigit())

# Vérifier si la chaîne contient uniquement des lettres
print("HelloWorld".isalpha())

# Vérifier si la chaîne est entièrement en minuscules
print("toutpetit".islower())

# Vérifier si la chaîne est entièrement en majuscules
print("EN MAJUSCULE".isupper())

# Vérifier si la chaîne commence par un mot spécifique
print("Bonjour tout le monde".startswith("Bonjour"))
