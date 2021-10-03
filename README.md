# Projet 1 - Préparez vos placements financiers

<!--- Changer la date de remise en modifiant le URL--->
#### :alarm_clock: [Date de remise le dimanche 3 octobre à 23h59](https://www.timeanddate.com/countdown/generic?iso=20200928T2359&p0=165&msg=Remise&font=cursive&csz=1#)

## Objectif
Concevoir et implémenter un programme permettant de calculer le rendement de différents investissements selon différentes situations. 

## Partie 1 : Interet simple /5 pts
À faire : compléter le fichier `partie_1.py` 

on place un capital de 8 000 $ pendant 72 jours au taux annuel de 6.5%. Calculer l’intérêt et la valeur acquise à l’issue du placement. On utilise la formule suivante:
<img src="https://render.githubusercontent.com/render/math?math=I=Ctn">.

- ***I*** : intérêt
- ***C*** : capital placé
- ***t*** : taux journalier (**taux annuel / 365**)
- ***n*** : nombre de jours

Enfin:  **Valeur acquise = Capital + Intérêts**


Exemple d'affichage : 

![Formules de section](data/affichage_partie1.png)

## Partie 2 :  Comparer deux placements à intérêts simples /8 pts
À faire : compléter le fichier `partie_2.py`

On possède un capital de 2600$. Votre banquier vous propose deux types de placement :
<img src="https://render.githubusercontent.com/render/math?math=I=Ctn">

- Pas de frais avec un taux annuel à 4,5 %
- 60$ de frais fixe qui sont prélevés du capital mais avec un taux annuel de 10%

i) Calculez le montant de votre capital avec le premier placement au 100ème jour de l'année

ii) Calculez le montant de votre capital avec le deuxième placement au 300ème jour de l'année 

iii) Au bout de combien de jours le deuxième placement vous rapportera plus que le premier ? (Question à faire avec une boucle)

Remarque : La formule pour calculer la valeur de votre capital est :

<strong>C = capital_initial + capital_initial*(taux/365)*nb_jours</strong>


Exemple d'affichage : 

![Formules de section](data/affichage_partie2.png)



## Partie 3 :  intérêts composé /7 pts
À faire : compléter le fichier `partie_3.py`

Soit le capital initial **C<sub>0</sub>** = 300 000$ et le capital placé récupéré au bout de n années <strong>C<sub>n</sub> = C<sub>n-1</sub>+C<sub>n-1</sub> * taux_interet</strong>

Calculer  **C<sub>20</sub>** le capital placé pendant 20 années avec un taux d'intérêt de 8%.


Exemple d'affichage : 

![Formules de section](data/affichage_partie3.png)


