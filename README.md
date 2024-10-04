# Problématique : 

Une ruche d’abeilles est installée dans un champ où il y a 50 fleurs. Les 100 abeilles de cette ruche se demandent quel est le meilleur itinéraire à effectuer pour butiner les 50 fleurs le plus rapidement possible.

# Solution

Nous avons donc, en équipe de 2, créé un algorithme génétique afin de trouver l’un des meilleurs itinéraires pour butiner ces fleurs le plus rapidement possible. La première génération de 100 abeilles a testé chacun un itinéraire au hasard. Nous avons pris les 20 % d’abeilles les plus rapides pour les croiser ensemble et créer des mutations pour la prochaine génération afin que cette génération soit plus performante et ainsi de suite pour chaque nouvelle génération.On utilise donc la loi de darwin. 

Voici les paramètre que nous avons mis en place :

BEEHIVE_POS = (500, 500)  : position de la ruche 
MUTATE_RATE = 0.045  : pourcentage de mutation dans la liste d'itineraire
MUTATION_INTENSITY = 0.05  : pourcentage d'abeille dans la nouvelle génération qui subissent une mutation
POPULATION_SIZE = 100  : nombre d'abeille
POPULATION_RATE = 0.2  : pourcentage des meilleur abeilles prisent pour chaque génération

# Résultat 

Nos premières générations ont une distance totale d'environ 24000 . Avec 1000 générations nous avons pu atteindre 6500 de distance . 
voici quelque graphique pour illustrer . 

![Le menu](image/menu.png)

![apperçu des fleurs dans le champs](image/field.png)

![Le parcours effectué par l'abeille avec le meilleur itinéraire](image/parcours.png)

![graphique montrant la meilleure distance par génération](image/convergence.png)