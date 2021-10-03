# Initilisation des variables 
capital_initial = 300000
taux_interet = (8.0/100)
nb_annee = 20

# Calcul du capital au bout de 20 années 

capital_n19 = capital_initial*(1+taux_interet)**19
capital_n20 = capital_n19 + capital_n19*taux_interet

# Affichage du capital au bout de 20 années

print("Au bout de 20 ans, le capital placé sera de " + str(capital_n20) + "$.")
