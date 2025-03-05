import pandas as pd
import numpy as np



# Nom : MOHAMED KAMALUDEEN
# Prénom : Syedha Memouna
# Numéro d'étudiant : 20006505



# Exerice 1 : Creating and Modifying Series
print("Exerice 1 : Creating and Modifying Series\n")


# Création d'un dictionnaire où les clés sont ['a', 'b', 'c'] et les valeurs 
# sont ['100', '200', '300']
dictionary = {'a' : 100, 'b' : 200, 'c' : 300}
# Création d'un Pandas Series à partir du dictionnaire
pd_series_dictonary = pd.Series(data = dictionary)
# Affichage du Pandas Series
print(pd_series_dictonary)


# -----------------------------------------------------------------------
# -----------------------------------------------------------------------


# Exercice 2 : Creating DataFrames
print("\n\n\nExercice 2 : Creating DataFrames\n")


# Création d'une data
data = {
    'A' : [1, 4, 7], 
    'B' : [2, 5, 8], 
    'C' : [3, 6, 9]
}
# Création d'un DataFrame à partir de la data
df = pd.DataFrame(data)
# Affiche du DataFrame
print(df)


# Ajout d'une nouvelle colonne D avec des valeurs [10, 11, 12]
df['D'] = [10, 11, 12] 
# Affichage du DataFrame
print(df)


# Suppression de la colonne B du DataFrame
df = df.drop('B', axis = 1)
# Affichage du DataFrame
print(df)


# -----------------------------------------------------------------------
# -----------------------------------------------------------------------


# Exercice 3 : DataFrame Indexing and Selection
print("\n\n\nExercice 3 : DataFrame Indexing and Selection\n")


# Création d'une data
data = {
    'A' : [1, 4, 7], 
    'B' : [2, 5, 8], 
    'C' : [3, 6, 9]
}
# Création d'un DataFrame à partir de la data
df = pd.DataFrame(data)


# Sélection et affichage de la colonne B du DataFrame
select_B = df[['B']]
print(select_B)


# Sélection et affichage des colonnes A et C du DataFrame
select_A_C = df[['A', 'C']]
print(select_A_C)


# Sélection et affichage de la ligne avec index qui égale à 1 en utilisant 
# .loc méthode 
select_row1 = df.loc[1]
print(select_row1)


# -----------------------------------------------------------------------
# -----------------------------------------------------------------------


# Exercice 4 : Adding and Removing DataFrame Elements
print("\n\n\nExercice 4 : Adding and Removing DataFrame Elements\n")


# Création d'une data
data = {
    'A' : [1, 4, 7], 
    'B' : [2, 5, 8], 
    'C' : [3, 6, 9]
}
# Création d'un DataFrame à partir de la data
df = pd.DataFrame(data)


# Ajout d'une nouvelle colonne Sum dans le DataFrame correspondant à la 
# somme des colonnes A, B et C
df['Sum'] = df['A'] + df['B'] + df['C']
# Affichage du DataFrame
print(df)


# Suppression de la colonne Sum du DataFrame
df = df.drop('Sum', axis = 1)
# Affichage du DataFrame
print(df)


# Ajout d'une nouvelle colonne Random avec des valeurs aléatoires en utilisant 
# NumPy
df['Random'] = np.random.randint(100, size = 3)
# Affichage du DataFrame
print(df)


# -----------------------------------------------------------------------
# -----------------------------------------------------------------------


# Exercice 5 : Merging DataFrames
print("\n\n\nExercice 5 : Merging DataFrames\n")


# Création d'une première data
left_data = {
    'key' : [1, 2, 3], 
    'A' : ['A1', 'A2', 'A3'], 
    'B' : ['B1', 'B2', 'B3']
}
# Création d'un premier DataFrame à partir de la première data
left = pd.DataFrame(left_data)
# Affichage du premier DataFrame
print(left)
# Création d'une deuxième data
right_data = {
    'key' : [1, 2, 3], 
    'C' : ['C1', 'C2', 'C3'], 
    'D' : ['D1', 'D2', 'D3']
}
# Création d'un deuxième DataFrame à partir de la deuxième data
right = pd.DataFrame(right_data)
# Affichage du deuxième DataFrame
print(right)


# Fusion des deux DataFrames suivant sur la colonne key
left_right_merging = pd.merge(left, right, on = 'key')
# Affichage du DataFrame fusionné
print(left_right_merging)


# Fusion des deux DataFrames en utilisant une jointure externe au 
# lieu d'une jointure interne
left_right_merging_outer = pd.merge(left, right, how = 'outer', on = 'key')
print(left_right_merging_outer)


# Ajout d'une nouvelle colonne E dans le DataFrame right
right['E'] = ['E1', 'E2', 'E3']
# Mise à jour du DataFrame fusionné pour inclure cette nouvelle 
# colonne E
left_right_merging['E'] = right['E']
# Affichage du DataFrame fusionné
print(left_right_merging)


# -----------------------------------------------------------------------
# -----------------------------------------------------------------------


# Exercice 6 : Data Cleaning
print("\n\n\nExercice 6 : Data Cleaning\n")


# Création d'une data
data = {
    'A' : [1.0, np.nan, 3.0], 
    'B' : [np.nan, 5.0, 6.0], 
    'C' : [7.0, 8.0, np.nan]
}
# CRéation d'un DataFrame à partir de la data
df = pd.DataFrame(data)


# Remplacement de toutes les valeurs NaN par 0 dans le DataFrame
df.fillna(value = 0)
# Affichage du DataFrame
print(df)

# Remplacement des 0 par NaN pour répondre à la question suivante
df.replace(0, np.nan, inplace = True)
# Remplacement des valeurs NaN par la moyenne de la colonne
df.fillna(value = df.mean(), inplace = True)
# Affichage du DataFrame
print(df)

# Remplacement d'une valeur dans une colonne pour répondre à la 
# question suivante
df.replace(3, np.nan, inplace = True)
# Suppression des lignes dont une valeur est NaN
df = df.dropna()
print(df)


# -----------------------------------------------------------------------
# -----------------------------------------------------------------------


# Exercice 7 : Grouping and Aggregation
print("\n\n\nExercice 7 : Grouping and Aggregation\n")


# Création d'une data
data = {
    'Category' : ['A', 'B', 'A', 'B', 'A', 'B'], 
    'Value' : [1, 2, 3, 4, 5, 6]
}
# Création d'un Dataframe à partir de la data
df = pd.DataFrame(data)


# Regroupement du DataFrame par la colonne Category et calcul de la 
# moyenne de la colonne Valeur
resultat_mean = df.groupby('Category')['Value'].mean()
# Affichge du résultat
print(resultat_mean)


# Regroupement du DataFrame par la colonne Category et calcul de la 
# somme de la colonne Valeur
resultat_sum = df.groupby('Category')['Value'].sum()
# Affichage du résultat
print(resultat_sum)


# Regroupement du DataFrame par la colonne Category et comptage de 
# nombre d'entrées dans chaque groupe
resultat_count_entries = df.groupby('Category').count()
# Affichage du résultat
print(resultat_count_entries)


# -----------------------------------------------------------------------
# -----------------------------------------------------------------------


# Exercice 8 : Pivot Tables
print("\n\n\nExercice 8 : Pivot Tables\n")


# Création d'une data
data = {
    'Category' : ['A', 'A', 'A', 'B', 'B', 'B'], 
    'Type' : ['X', 'Y', 'X', 'Y', 'X', 'Y'], 
    'Value' : [1, 2, 3, 4, 5, 6]
}
# Création d'un DataFrame à partir de la data
df = pd.DataFrame(data)


# Création d'un tableau croisé dynamique à partir du DataFrame en montrant 
# la valeur moyenne pour chaque catégorie et chaque type
table_mean = pd.pivot_table(df, values = 'Value', index = 'Category', columns = 'Type', aggfunc = 'mean')
# Affichage du tableau croisé
print(table_mean)


# Création d'un tableau croisé dynamique à partir du DataFrame en montrant 
# la somme des valeurs pour chaque catégorie et chaque type
table_sum = pd.pivot_table(df, values = 'Value', index = 'Category', columns = 'Type', aggfunc = 'sum')
# Affichage du tableau croisé
print(table_sum)


# Création d'un tableau croisé dynamique à partir du DataFrame en montrant 
# la somme des valeurs pour chaque catégorie et chaque type et ajoutant des 
# marges pour montrer les totaux
table_mean_margins = pd.pivot_table(df, values = 'Value', index = 'Category', columns = 'Type', aggfunc = 'mean', margins = True)
# Affichage du tableau croisé
print(table_mean_margins)


# -----------------------------------------------------------------------
# -----------------------------------------------------------------------


# Exercice 9 : Time Series Data
print("\n\n\nExercice 9 : Time Series Data\n")


# Création d'une data de type de série chronologique avec une plage de dates 
# commançant par '2023-01-01' pour 6 périodes et des valeurs alétoires
dates = pd.date_range(start = '2023-01-01', periods = 6, freq = 'D')
data = {
    'Date' : dates,
    'Value' : np.random.randint(1, 101, 6)
}
# Création d'un DataFrame à partir de la data
df = pd.DataFrame(data)
# Affichage du DataFrame
print(df)

# Définiton la colonne Data comme index
df.set_index('Date', inplace = True)
# Affichage du DataFrame
print(df)

# Regroupement des données par période de 2 jours afin de calculer la somme
df_resampled = df.resample('2D').sum()
print(df_resampled)


# -----------------------------------------------------------------------
# -----------------------------------------------------------------------


# Exercice 10 : Handling Missing Data
print("\n\n\nExercice 10 : Handling Missing Data\n")


# Création d'une data
data = {
    'A' : [1.0, np.nan, 3.0], 
    'B' : [2.0, 5.0, np.nan], 
    'C' : [np.nan, 8.0, 9.0]
}
# Création d'un DataFrame à partir de la data
df = pd.DataFrame(data)
# Affichage du DataFrame
print(df)

# Interpolation des valeurs manquantes dans le DataFrame
df = df.interpolate()
# Affichage du DataFrame
print(df)

# Suppression des lignes dont une valeur est NaN 
df = df.dropna()
# Affichage du DataFrame
print(df)


# -----------------------------------------------------------------------
# -----------------------------------------------------------------------


# Exercice 11 : DataFrame Operations
print("\n\n\nExercice 11 : DataFrame Operations\n")


# Création d'une data
data = {
    'A' : [1, 4, 7], 
    'B' : [2, 5, 8], 
    'C' : [3, 6, 9]
}
# Création d'un DataFrame à partir de la data
df = pd.DataFrame(data)
# Affichage du DataFrame
print(df)

# Calcul et affichage de la somme cumilative du DataFrame
sum_cum = df.cumsum()
print(sum_cum)


# Calcul et affichage du produit cumilatif du DataFrame
pro_cum = df.cumprod()
print(pro_cum)


# Soustraction de 1 à toutes les valeurs du DataFrame et affichage du résultat
sub_1 = df.sub(1)
print(sub_1)





