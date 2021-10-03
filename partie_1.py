# Initialisation des variables
capital = 8000
nb_jours = 72
taux_annuel = 0.065

# Calcul du taux périodique
taux_periodique = (taux_annuel/365)

# Calcul des intérêts
nb_jours = 72
interet = capital*taux_periodique*nb_jours

# Calcul de la valeur acquise
valeur_acquise = (capital + interet)

# Affichage des interets et de la valeur acquise
print("L'intérêt issue de ce placement est de " + str(interet) +"$.")
print("La valeur acquise de ce placement est estimé a " + str(round(valeur_acquise, 1)) +"$")
