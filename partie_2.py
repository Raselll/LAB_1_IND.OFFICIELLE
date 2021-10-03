# Initialisation des variables 
capital = 2600
taux_journalier1 = (4.5/100)/365
taux_journalier2 = (10.0/100)/365
frais = 60

# Calcul du montant du capital avec le premier placement au 100ème jour de l'année 
nb_jours1 = 100
capital1 = capital+(capital*taux_journalier1*nb_jours1)

# Calcul du montant du capital avec le deuxième placement au 300ème jour de l'année 
nb_jours2 = 300
capital2 = ((capital-60)+((capital-60)*taux_journalier2*nb_jours2))

# /!\ AVEC UNE BOUCLE/!\ Calcul du jour à partir duquel le deuxième placement rapporte plus que le premier
# Premier placement = capital+(capital*taux_journalier1*nb_jours1)
# Deuxieme placement = ((capital-60)+((capital-60)*taux_journalier2*nb_jours2))

nb_jours = 0
capital01 = capital+(capital*taux_journalier1*nb_jours)
capital02 = ((capital-60)+((capital-60)*taux_journalier2*nb_jours))

while capital01 > capital02:
    nb_jours += 1
    capital01 = capital+(capital*taux_journalier1*nb_jours)
    capital02 =((capital-60)+((capital-60)*taux_journalier2*nb_jours))

# print(str(nb_jours+1))

# Affichage des valeurs calculées
print("Avec le premier placement, le montant obtenu apres 100 jours est de " + str(capital1) + "$.")
print("Avec le deuxième placement, le montant obtenu apres 300 jours est de " + str(capital2) +"$.")
print("Puisque le jour 0 n'est pas pris en compte, il faut manuellement ajouter 1 jour au 160 jours. Ceci fait donc " + str(nb_jours + 1) + " jours.")


