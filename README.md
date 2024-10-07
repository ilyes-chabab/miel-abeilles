# Simulation d'Abeilles

## Description
Ce projet est une simulation d'abeilles qui utilise un algorithme génétique pour optimiser le chemin de recherche de nectar dans un champ de fleurs. Les abeilles simulent un comportement de recherche de nourriture, cherchant le chemin le plus court à travers un ensemble de fleurs disposées dans un espace donné.

## Technologies utilisées
- **Python** : Langage de programmation principal.
- **Tkinter** : Bibliothèque pour la création d'interfaces graphiques.
- **Matplotlib** : Bibliothèque pour la visualisation des résultats.
- **NumPy** : Pour les opérations mathématiques (si nécessaire).

# Problématique : 

Une ruche d’abeilles est installée dans un champ où il y a 50 fleurs. Les 100 abeilles de cette ruche se demandent quel est le meilleur itinéraire à effectuer pour butiner les 50 fleurs le plus rapidement possible.

# Solution

Nous avons donc, en équipe de 2, créé un algorithme génétique afin de trouver l’un des meilleurs itinéraires pour butiner ces fleurs le plus rapidement possible. La première génération de 100 abeilles a testé chacun un itinéraire au hasard et en fonction des paramètres choisis des générations meilleures sont créés. 

Voici les paramètre que nous avons mis en place :

Population Rate 10/100 : Le nombre de meilleurs abbeilles sélectionnées pour les générations suivantes

Mutate rate 4/100 : Nombre d'abbeilles subissant une mutation

Crossover Rate 96/100 : Nombre d'abbeilles subissant un croisement 

Mutation intensity : 2/500 : Nombre de positions modifiées dans le génome

Génération 1500 


# Résultat 

Nos premières générations ont une distance totale d'environ 24000 . Avec plus de 1000 générations nous avons pu atteindre 7460 de distance . 
voici quelque graphique pour illustrer . 

![Le menu](image/menu.png)

![apperçu des fleurs dans le champs](image/field.png)

![Le parcours effectué par l'abeille avec le meilleur itinéraire](image/parcours.png)

![graphique montrant la meilleure distance par génération](image/convergence.png)

# Analyse complémentaire 


