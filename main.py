
import pandas as pd
import matplotlib.pyplot as plt



def generate_field():
    # Charger le fichier Excel
    fichier_excel = 'Champ de pissenlits et de sauge des pres.xlsx'
    df = pd.read_excel(fichier_excel)

    # Visualiser les premières lignes du fichier pour savoir quelles colonnes utiliser
    print(df.head())

    # Générer un graphique simple, par exemple un graphique en courbes entre deux colonnes
    plt.plot(df['x'], df['y'])

    # Ajouter des titres et des labels
    plt.title('Titre du graphique')
    plt.xlabel('Nom de la colonne X')
    plt.ylabel('Nom de la colonne Y')

    # Afficher le graphique
    plt.show()


if __name__ == '__main__':
    generate_field()