import numpy as np
import time



# Nom : MOHAMED KAMALUDEEN
# Prénom : Syedha Memouna
# Numéro d'étudiant : 20006505



# Exercice 1 : Creating and Manipulating NumPy Arrays
print("Exercice 1 : Creating and Manipulating NumPy Arrays\n")


# Création d'un tableau NumPy 1D à partir de la arraye [5, 10, 15, 20, 25]
array_1 = np.array([5, 10, 15, 20, 25])
# Affichage du tableau 
print("Array 1 : " + str(array_1))
# Conversion du type du tableau en type float64
array_1_float64 = array_1.astype(np.float64)
# Affichage du tableau convertie
print("Numpy array with array 1 : " + str(array_1_float64))


# Création d'un tableau NumPy 2D à partir de la arraye imbriquée [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
array_2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# Affichage du tableau
print("\nArray 2 : " + str(array_2))
# Forme du tableau
array_2_shape = array_2.shape
# Affichage de la forme du tableau
print("Shape of the array 2 : " + str(array_2_shape))
# Taille du tableau 
array_2_size = np.size(array_2)
# Affichage de la taille du tableau
print("Size of the array 2 : " + str(array_2_size))


# Création d'un tableau NumPy 3D avec des valeurs aléatoires de forme (2, 3, 4)
array_3 = np.random.rand(2, 3, 4)
# Affichage du tableau
print("\nArray 3 : " + str(array_3))
# Dimension du tableau
array_3_dimension = array_3.ndim
# Affichage de la dimension du tableau
print("Dimension of the array 3 : " + str(array_3_dimension))
# Forme du tableau
array_3_shape = array_3.shape 
# Affichage de la forme du tableau
print("Shape of the array 3 : " + str(array_3_shape))


# -----------------------------------------------------------------------
# -----------------------------------------------------------------------


# Exercice 2 : Advanced Array Manipulations
print("\n\n\nExercice 2 : Advanced Array Manipulations\n")


# Création d'un tableau NumPy 1D de 0 à 9
array_4 = np.arange(10)
# Inversion du tableau
array_4_flipped = np.flip(array_4)
# Affichage du tableau inversé
print("Array 4 : " + str(array_4_flipped))


# Création d'un tableau NumPy 2D de 0 à 11 de forme (3, 4)
array_5 = np.arange(12).reshape(3, 4)
# Affichage du tableau 
print("\nArray 5 : " + str(array_5))
# Extraction du sous-tableau contenant les deux premières lignes et deux dernières colonnes du tableau
array_5_subarray = array_5[:2, -2:]
# Affichage du sous-tableau
print("Subarray of the array 5 : " + str(array_5_subarray))


# Création d'un tableau NumPy 2D avec des valeurs aléatoires entre 0 et 10 de forme (5, 5)
array_6 = np.random.randint(0, 11, (5, 5))
# Affichage du tableau
print("\nArray 6 : " + str(array_6))
# Remplacement des valeurs supérieures à 5 par 0
array_6[array_6 > 5] = 0
# Affichage du tableau modifiée
print("Array 6 only with greater than 5 : " + str(array_6))


# -----------------------------------------------------------------------
# -----------------------------------------------------------------------


# Exercice 3 : Array Initialization and Attributes
print("\n\n\nExercice 3 : Array Initialization and Attributes\n")


# Création d'un tableau identité NumPy 2D de forme (3, 3) avec des 1 sur la diagonale et des 0 ailleurs
array_7 = np.eye(3)
# Affichage du tableau 
print("Array 7 : " + str(array_7))
# Affichage de la dimension du tableau
print("Dimension of array 7 : " + str(array_7.ndim))
# Affichage de la forme du tableau
print("Shape of array 7 : " + str(array_7.shape))
# Affichage de la taille du tableau
print("Size of array 7 : " + str(array_7.size))
# Affichage de la taille en octets d'un élément du tableau
print("Itemsize of array 7 : " + str(array_7.itemsize))
# Afffichage de la taille en octets du tableau
print("Bytes of array 7 : " + str(array_7.nbytes))


# Création d'un tableau NumPy 1D de 10 valeurs espacées uniformément entre 0 et 5
array_8 = np.linspace(0, 5, 10)
# Affichage du tableau
print("\nArray 8 : " + str(array_8))
# Affichage du type du tableau
print("Type of array 8 : " + str(array_8.dtype))


# Création d'un tableau NumPy 3D avec des valeurs aléatoires suivant une distribution normale standard de forme (2, 3, 4)
array_9 = np.random.randn(2, 3, 4)
# Affichage du tableau
print("\nArray 9 : " + str(array_9))
# Calcul de la somme de tous les valeurs du tableau
sum_elements = np.sum(array_9)
# Affichage du résultat de la somme
print("Sum of array 9 : " + str(sum_elements))


# -----------------------------------------------------------------------
# -----------------------------------------------------------------------


#Exercice 4 : Fancy Indexing and Masking
print("\n\n\nExercice 4 : Fancy Indexing and Masking\n")


# Création d'un tableau NumPy 1D de 20 valeurs aléatoires entre 0 et 50
array_10 = np.random.randint(0, 51, 20)
# Affichage du tableau
print("Array 10 : " + str(array_10))
# Indexation pour extraire les valeurs aux [2, 5, 7, 10, 15]
indices = [2, 5, 7, 10, 15]
# Affichage des valeurs extraites en utilisant l'indexation
print("Array 10 with only specific indices : " + str(array_10[indices]))


# Création d'un tableau NumPy 2D avec des valeurs aléatoires entre 0 et 30 de forme (4, 5)
array_11 = np.random.randint(0, 31, (4, 5))
# Affichage du tableau
print("\nArray 11 : " + str(array_11))
# Création d'un masque booléen pour extraire les valeurs supérieures à 15
mask = array_11 > 15
# Affichage du masque
print("Mask : " + str(mask))
# Affichage des valeurs extraites en utilisant le masque booléen 
print("Array 11 with only greater than 15 : " + str(array_11[mask]))


# Création d'un tableau NumPy 1D de 10 valeurs aléatoires entre -10 et 10
array_12 = np.random.randint(-10, 10, 10)
# Affichage du tableau
print("\nArray 12 : " + str(array_12))
# Uilisation d'un masque booléen pour remplacer les valeurs négatives par 0
array_12[array_12 < 0] = 0
# Affichage du tableau modifié
print("Array 12 only with greater than 0 : " + str(array_12))


# -----------------------------------------------------------------------
# -----------------------------------------------------------------------


#Exercice 5 : Combining and Splitting Arrays
print("\n\n\nExercice 5 : Combining and Splitting Arrays\n")


# Création d'un premier tableau NumPy 1D de 5 valeurs aléatoires entre 0 et 10
array_13 = np.random.randint(0, 11, 5)
# Affichage du premier tableau
print("\nArray 13 : " + str(array_13))
# Création d'un deuxième tableau NumPy 1D de 5 valeurs aléatoires entre 0 et 10
array_14 = np.random.randint(0, 10, 5)
# Affichage du deuxième tableau
print("Array 14 : " + str(array_14))
# Création d'un troisième tableau en concaténant les deux tableaux
conc_array_13_14 = np.concatenate((array_13, array_14))
# Affichage du tableau concaténé
print("Array 13 and 14 concatenated : " +str(conc_array_13_14))


# Création d'un tableau NumPy 2D avec des valeurs aléatoires entre 0 et 10 de forme (6, 4)
array_15 = np.random.randint(0, 11, (6, 4))
# Affichage du tableau
print("\nArray 15 : " + str(array_15))
# Division du tableau en deux parties égales le long de l'axe des lignes
array_15_1, array_15_2 = np.split(array_15, 2, axis = 0)
# Affichage des deux parties 
print("Array 15 splitted in 2 : ")
print(array_15_1)
print(array_15_2)


# Création d'un tableau NumPy 2D avec des valeurs aléatoires entre 0 et 10 de forme (3, 6)
array_16 = np.random.randint(0, 11, (3, 6))
# Affichage du tableau
print("\nArray 16 : " +str(array_16))
# Division du tableau en trois parties égales le long de l'axe des colonnes
array_16_1, array_16_2, array_16_3 = np.split(array_16, 3, axis = 1)
# Affichage des trois parties
print("Array 16 splitted in 3 : ")
print(array_16_1)
print(array_16_2)
print(array_16_3)


# -----------------------------------------------------------------------
# -----------------------------------------------------------------------


#Exercice 6 : Mathematical Functions and Aggregations
print("\n\n\nExercice 6 : Mathematical Functions and Aggregations\n")


# Création d'un tableau NumPy 1D de 15 valeurs aléatoires entre 0 et 100
array_17 = np.random.randint(0, 101, 15)
# Afffichage du tableau
print("\nArray 17 : " + str(array_17))
# Moyenne du tableau
array_17_mean = np.mean(array_17)
# Affichage de la moyenne du tableau
print("Mean of array 17 : " + str(array_17_mean))
# Médiane du tableau
array_17_median = np.median(array_17)
# Affichage de la médiane du tableau
print("Median of array 17 : " + str(array_17_median))
# Ecart-type du tableau
array_17_std = np.std(array_17)
# Affichage d'écart-type du tableau
print("Std of array 17 : " + str(array_17_std))
# Variance du tableau
array_17_variance = np.var(array_17)
# Affichage de la variance du tableau
print("Variance of array 17 : " + str(array_17_variance))


# Création d'un tableau NumPy 2D avec des valeurs aléatoires entre 1 et 50 de forme (4, 4)
array_18 = np.random.randint(1, 51, (4, 4))
# Affichage du tableau
print("\nArray 18 : " + str(array_18))
# Somme de chaque ligne du tableau
array_18_sum_row = np.sum(array_18, axis = 1)
# Affichage du résultat de la somme de chaque ligne
print("Sum of row of array 18 : " + str(array_18_sum_row))
# Somme de chaque colonne du tableau
array_18_sum_column = np.sum(array_18, axis = 0)
# Affichage du résultat de la somme de chaque colonne
print("Sum of column of array 18 : " + str(array_18_sum_column))


# Création d'un tableau 3D avec des valeurs aléatoires entre 1 et 20 de forme (2, 3, 4)
lts_19 = np.random.randint(1, 21, (2, 3, 4))
# Affichage du tableau
print("\nArray 19 : " + str(lts_19))
# Valeur minimale sur chaque profondeur du tableau
array_19_depth_min = np.min(lts_19, axis = 0)
# Affichage de la valeur minimale de chaque profondeur
print(array_19_depth_min)
# Valeur maximale sur chaque profondeur du tableau
array_19_depth_max = np.max(lts_19, axis = 0)
# Affichage de la valeur maximale de chaque profondeur
print(array_19_depth_max)
# Valeur minimale sur chaque colonne du tableau
array_19_column_min = np.min(lts_19, axis = 1)
# Affichage de la valeur minimale de chaque colonne
print(array_19_column_min)
# Valeur maximale sur chaque colonne du tableau
array_19_column_max = np.max(lts_19, axis = 1)
# Affichage de la valeur maximale de chaque colonne
print(array_19_column_max)
# Valeur minimale sur chaque ligne du tableau
array_19_row_min = np.min(lts_19, axis = 2)
# Affichage de la valeur minimale de chaque ligne
print(array_19_row_min)
# Valeur maximale sur chaque ligne du tableau
array_19_row_max = np.max(lts_19, axis = 2)
# Affichage de la valeur maximale de chaque ligne
print(array_19_row_max)



# -----------------------------------------------------------------------
# -----------------------------------------------------------------------


#Exercice 7 : Reshaping and Transposing Arrays
print("\n\n\nExercice 7 : Reshaping and Transposing Arrays\n")


# Création d'un tableau NumPy 1D de 1 à 12
array_20 = np.arange(1, 13)
# Affichage du tableau
print("Array 20 : " + str(array_20))
# Redimensionnement du tableau en 2D de forme (3, 4)
array_20_reshaped = array_20.reshape(3, 4)
# Affichage du tableau redimensionné
print("Array 20 reshaped : " + str(array_20_reshaped))


# Création d'un tableau NumPy 2D avec des valeurs aléatoires entre 1 à 10 de forme (3, 4)
array_21 = np.random.randint(1, 11, (3, 4))
# Affichage du tableau
print("\nArray 21 : " + str(array_21))
# Transposition du tableau
array_21_transposed = array_21.transpose()
# Affichage du tableau transposé
print("Array 21 transposed : " + str(array_21_transposed))


# Création d'un tableau NumPy 2D avec des valeurs aléatoires entre 1 et 10 de forme (2, 3)
array_22 = np.random.randint(1, 11, (2, 3))
# Affichage du tableau 
print("\nArray 22 : " + str(array_22))
# Aplanissement du tableau 
array_22_flatten = array_22.flatten()
# Affichage du tableau aplati
print("Array 22 flatten : " + str(array_22_flatten))


# -----------------------------------------------------------------------
# -----------------------------------------------------------------------


#Exercice 8 : Broadcasting and Vectorized Operations
print("\n\n\nExercice 8 : Broadcasting and Vectorized Operations\n")


# Création d'un tableau NumPy 2D avec des valeurs aléatoires entre 1 et 10 de forme (3, 4)
array_23 = np.random.randint(1, 11, (3, 4))
# Affichage du tableau
print("Array 23 : " + str(array_23))
# Moyenne de chaque colonne du tableau
array_23_mean = np.mean(array_23, axis = 0)
# Affichage de la moyenne de chaque colonne
print("Mean of array 23 : " + str(array_23_mean))
# Soustraction de la moyenne de chaque colonne à chaque valeur de la même colonne
result = array_23 - array_23_mean
# Affichage du résultat de la soustraction
print("Result : " + str(result))


# Création d'un premier tableau NumPy 1D de 4 valeurs aléatoires entre 1 et 5
array_24 = np.random.randint(1, 6, 4)
# Affichage du premier tableau
print("\nArray 24 : " + str(array_24))
# Création d'un deuxième tableau NumPy 1D de 4 valeurs aléatoires entre 1 et 5
array_25 = np.random.randint(1, 6, 4)
# Affichage du deuxième tableau
print("Array 25 : " + str(array_25))
# Produit extérieur des deux tableaux
outer_product = np.outer(array_24, array_25)
# Affichage du résultat du produit extérieur
print("Outer product : " + str(outer_product))


# Création d'un tableau NumPy 2D avec des valeurs aléatoires entre 1 et 10 de forme (4, 5)
array_26 = np.random.randint(1, 11, (4, 5))
# Affichage du tableau
print("\nArray 26 : " + str(array_26))
# Ajout de 10 aux valeurs supérieures à 5
array_26[array_26 > 5] += 10
# Affichage du résultat de l'addition 
print("Array 26 only with greater 5 : " + str(array_26))


# -----------------------------------------------------------------------
# -----------------------------------------------------------------------


#Exercice 9 : Sorting and Searching Arrays
print("\n\n\nExercice 9 : Sorting and Searching Arrays\n")


# Création d'un tableau NumPy 1D de 10 valeurs aléatoires entre 1 et 20
array_27 = np.random.randint(1, 21, 10)
# Affichage du tableau
print("Array 27 : " + str(array_27))
# Tri du tableau par ordre croissant
array_27_sorted = np.sort(array_27)
# Affichage du tableau trié
print("Sorted array 27 : " + str(array_27_sorted))


# Création d'un tableau NumPy 2D avec des valeurs aléatoires entre 1 et 50 de forme (3, 5)
array_28 = np.random.randint(1, 51, (3, 5))
# Affichage du tableau
print("\nArray 28 : " + str(array_28))
# Tri du tableau selon la deuxième colonne
array_28_sorted = array_28[array_28[:, 1].argsort()]
# Affichage du tableau trié
print("Array 28 : " + str(array_28_sorted))


# Création d'un tableau NumPy 1D de 15 valeurs aléatoires entre 1 et 100
array_29 = np.random.randint(1, 101, 15)
# Affichage du tableau
print("\nArray 29 : " + str(array_29))
# Recherche des indices des valeurs supérieures à 50
indices = np.where(array_29 > 50)
# Affichage des indices
print("Indices of numbers greater than 50 : " + str(indices))


# -----------------------------------------------------------------------
# -----------------------------------------------------------------------


# Exercice 10 : Linear Algebra with Numpy
print("\n\n\nExercice 10 : Linear Algebra with Numpy\n")


# Création d'un tableau NumPy 2D avec des valeurs aléatoires entre 1 et 10 de forme (2, 2)
array_30 = np.random.randint(1, 11, (2, 2))
# Affichage du tableau
print("Array 30 : " + str(array_30))
# Déterminant du tableau
array_30_determinant = np.linalg.det(array_30)
# Affichage du déterminanant
print("Linalg of array 30 : " + str(array_30_determinant))


# Création d'un tableau NumPy 2D avec des valeurs aléatoires entre 1 et 5 de forme (3, 3)
array_31 = np.random.randint(1, 6, (3, 3))
# Affichage du tableau
print("\nArray 31 : " + str(array_31))
# Valeurs propres et vecteurs propres du tableau
eigenvalues, eigenvectors = np.linalg.eig(array_31)
# Affichage caleurs propres et vecteurs propres
print("Eigenvalues of array 31 : " + str(eigenvalues))
print("Eigenvectors of array 31 : " + str(eigenvectors))


# Création d'un premier tableau NumPy 2D avec des valeurs aléatoires entre 1 et 10 de forme (2, 3)
array_32 = np.random.randint(1, 11, (2, 3))
# Affichage du premier tableau
print("\nArray 32 : " + str(array_32))
# Création d'un deuxième tableau NumPy 2D avec des valeurs aléatoires entre 1 et 10 de forme (3, 2)
array_33 = np.random.randint(1, 11, (3, 2))
# Affichage du deuxième tableau
print("Array 33 : " + str(array_33))
# Produit matricielle entre les deux tableaux
matrix_product = np.matmul(array_32, array_33)
# Affichage du résultat du produit matricielle
print("Matrix product : " + str(matrix_product))


# -----------------------------------------------------------------------
# -----------------------------------------------------------------------


# Exercice 11 : Random Sampling and Distributions
print("\n\n\nExercice 11 : Random Sampling and Distributions\n")


# Création d'un tableau NumPy 1D de 10 valeurs aléatoires entre 0 et 1 suivant une distribution uniforme
array_34 = np.random.rand(10)
# Affichage du tableau
print("Array 34 : " + str(array_34))


#Création d'un tableau NumPy 2D avec des valeurs aléatoire suivant une distribution normale standard de forme (3, 3)
array_35 = np.random.randn(3, 3)
# Affichage du tableau
print("\nArray 35 : " + str(array_35))


# Création d'un tableau 1D de 20 valeurs aléatoires entre 1 et 100 
array_36 = np.random.randint(1, 101, 20)
# Affichage du tableau
print("\nArray 36 : " + str(array_36))
# Histogramme et 5 classes du tableau 
histogram, bins = np.histogram(array_36, bins = 5)
# Affichage d'histogramme et de classes
print("Histogram : " + str(histogram))
print("Bins" + str(bins))


# -----------------------------------------------------------------------
# -----------------------------------------------------------------------


#Exercice 12 : Advanced Indexing and Selection
print("\n\n\nExercice 12 : Advanced Indexing and Selection\n")


# Création d'un tableau NumPy 2D avec des valeurs aléatoires entre 1 et 20 de forme (5, 5)
array_37 = np.random.randint(1, 21, (5, 5))
# Affichage du tableau
print("Array 37 : " + str(array_37))
# Extraction des valeurs diagonaux du tableau
diagonal_elements = np.diag(array_37)
# Affichage des valeurs diagonaux
print("Diaogonal : " + str(diagonal_elements))


# Création d'un tableau NumPy 1D de 10 valeurs aléatoires entre 1 et 50
array_38 = np.random.randint(1, 51, 10)
# Affichage du tableau
print("\nArray 38 : " + str(array_38))
# La fonction prime_number permet de verifier si le nombre en question est premier ou pas. 
def prime_numbers(number):
    if number < 2:
        return False
    for i in range(2, int(number//2) + 1):
        if number % i == 0:
            return False
    return True
# Extraction des valeurs premiers du tableau 
prime_numbers_array = np.array([number for number in array_38 if prime_numbers(number)])
# Affichage des valeurs extraites 
print("Prime numbers of the array 38 : " + str(prime_numbers_array))


# Création d'un tableau NumPy 2D avec des valeurs aléatoires entre 1 et 10 de forme (4, 4)
array_39 = np.random.randint(1, 11, (4, 4))
# Affichage du tableau
print("\nArray 39 : " + str(array_39))
# Extraction des nombres pairs du tableau
even_numbers = array_39[array_39 % 2 == 0]
# Affichage des nombres pairs du tableau
print("Even numbers of the array 39 : " + str(even_numbers))


# -----------------------------------------------------------------------
# -----------------------------------------------------------------------


#Exercice 13 : Handling Missing Data
print("\n\n\nExercice 13 : Handling Missing Data\n")


# Création d'un tableau NumPy 1D de 10 valeurs aléatoires entre 1 et 10 de type float
array_40 = np.random.randint(1, 11, 10).astype('float')
# Affichage du tableau
print("Array 40 : " + str(array_40))
# Sélection de trois nombres aléatoirement pour définir les indices
random_positions = np.random.choice(10, size = 3, replace = False)
# Remplacement des valeurs aux indices sélectionnés aléatoirement par NaN
array_40[random_positions] = np.nan
# Affichage du tableau modifié
print("Array 40 with nan : " + str(array_40))


# Création d'un tableau NumPy 2D avec des valeurs aléatoires de forme (3, 4) de type float
array_41 = np.random.randint(1, 11, (3, 4)).astype('float')
# Affichage du tableau
print("\nArray 41 : " + str(array_41))
# Remplacement des valeurs inférieures à 5 par NaN
array_41[array_41 < 5] = np.nan
# Affichage du tableau modifié
print("Array 41 with nan for numbers less than 5 : " + str(array_41))


# Création d'un tableau NumPy de 15 valeurs aléatoires entre 1 et 20 de type float
array_42 = np.random.randint(1, 21, 15).astype('float')
# Affichage du tableau
print("L\narray 42 : " + str(array_42))
# Sélection de trois nombres aléatoirement pour définir les indices
random_positions = np.random.choice(15, size = 3, replace = False)
# Remplacement des valeurs aux index sélectionnés aléatoirement par NaN
array_42[random_positions] = np.nan
# Affichage du tableau modifié
print("Array 41 with nan : " + str(array_42))
# Recherche des indices contenant NaN
nan_indices = np.where(np.isnan(array_42))
# Affichage des indices
print("Indices of nan : " + str(nan_indices))


# -----------------------------------------------------------------------
# -----------------------------------------------------------------------


#Exercice 14 : Performance Optimization with Numpy
print("\n\n\nExercice 14 : Performance Optimization with Numpy\n")


# Démarrage du chronomètre
start_time = time.time()
# Création d'un tableau NumPy 1D de 1000000 valeurs aléatoires entre 1 et 100
array_43 = np.random.randint(1, 101, 1000000)
# Moyenne du tableau
array_43_mean = np.mean(array_43)
# Ecart-type du tableau
array_43_std = np.std(array_43)
# Fin du chronomètre
end_time = time.time()
# Calcul du temps d'exécution des opérations
total_time = end_time - start_time
# Affichage du tableau
print("Array 43 : " + str(array_43))
# Affichage de la moyenne
print("Mean od the array 43 : " + str(array_43_mean))
# Affichage d'écart-type
print("Std of the array 43 : " + str(array_43_std))
# Affichage du temps d'exécution
print("Total time : " + str(total_time))


# Démarrage du chronomètre
start_time = time.time()
# Création d'un premier tableau NumPy 2D avec des valeurs aléatoires entre 1 et 10 de forme (1000, 1000)
array_44 = np.random.randint(1, 11, (1000, 1000))
# Création d'un deuxième tableau NumPy 2D avec des valeurs aléatoires entre 1 et 10 de forme (1000, 1000)
array_45 = np.random.randint(1, 11, (1000, 1000))
# Addition valeur par valeur des deux tableaux
array_44_45_sum = np.add(array_44, array_45)
# Fin du chronomètre
end_time = time.time()
# Calcul du temps d'exécution des opérations
total_time = end_time - start_time
# Affichage du premier tableau
print("\nArray 44 : " + str(array_44))
# Affichage du deuxième tableau
print("Array 45 : " + str(array_45))
# Affichage du résultat de l'addition
print("Sum of array 44 and 45 : " + str(array_44_45_sum))
# Affichage du temps d'exécution
print("Total time : " + str(total_time))


# Démarrage du chronomètre
start_time = time.time()
# Création d'un tableau NumPy 3D avec des valeurs aléatoires entre 1 et 10 de forme (100, 100, 100)
array_46 = np.random.randint(1, 11, (100, 100, 100))
sum_axis_0 =  np.sum(array_46, axis = 0)
sum_axis_1 =  np.sum(array_46, axis = 1)
sum_axis_2 =  np.sum(array_46, axis = 2)
# Fin du chronomètre
end_time = time.time()
# # Calcul du temps d'exécution des opérations
total_time = end_time - start_time
# Affichage du tableau
print("\nArray 46 : " + str(array_46))
# Affichage des résultats des sommes
print(sum_axis_0)
print(sum_axis_1)
print(sum_axis_2)
# Affichage du temps d'exécution
print("Total time : " + str(total_time))


# -----------------------------------------------------------------------
# -----------------------------------------------------------------------


# Exercice 15 : Cumulative and Aggregate Functions
print("\n\n\nExercice 15 : Cumulative and Aggregate Functions\n")


# Création d'un tableau NumPy 1D de 1 à 10
array_47 = np.arange(1, 11)
# Affichage du tableau
print("Array 47 : " + str(array_47))
# Somme cumulative du tableau
array_47_cum_sum = np.cumsum(array_47)
# Affichage du résultat de la somme cumulative
print("Cum sum of the array 47 : " + str(array_47_cum_sum))
# Produit cumulatif du tableau
array_47_cum_pro = np.cumprod(array_47)
# Affichage du résultat du produit cumulatif
print("Cum prod of the array 47 : " + str(array_47_cum_pro))


# Création d'un tableau NumPy 2D avec des valeurs aléatoires entre 1 et 20 de forme (4, 4)
array_48 = np.random.randint(1, 21, (4, 4))
# Affichage du tableau
print("\nArray 48 : " + str(array_48))
# Somme cumulative le long des colonnes du tableau 
array_48_cum_sum_column = np.cumsum(array_48, axis = 0)
# Affichage de la somme cumulative
print("Cum sum of column of array 48 : " + str(array_48_cum_sum_column))
# Somme cumulative le long des lignes du tableau
array_48_cum_sum_row = np.cumsum(array_48, axis = 1)
# Affichage de la somme cumulative
print("Cum sum of row of array 48 : " + str(array_48_cum_sum_row))


# Création d'un tableau NumPy 1D de 10 valeurs aléatoires entre 1 et 50
array_49 = np.random.randint(1, 51, 10)
# Affichage du tableau
print("\nArray 49 : " + str(array_49))
# Valeur minimale du tableau 
array_49_min = np.min(array_49)
# Affichage de la valeur minimale
print("Minimum of the array 49 : " + str(array_49_min))
# Valeur maximale du tableau
array_49_max = np.max(array_49)
# Affichage de la valeur maximale
print("Maximum of the array 49 : " + str(array_49_max))
# Somme des valeurs du tableau
array_49_sum = np.sum(array_49)
# Affichage de la somme
print("Sum of the array 49 : " + str(array_49_sum))


# -----------------------------------------------------------------------
# -----------------------------------------------------------------------


#Exercice 16 : Working with Dates and Times
print("\n\n\nExercice 16 : Working with Dates and Times\n")


# Création d'un tableau NumPy 1D de 10 dates à partir d'aujourd'hui avec une fréquance quotidienne
dates_1 = np.datetime64('today', 'D') + np.arange(10)
# Affichage des dates
print("Dates : " + str(dates_1))


# Création d'un tableau NumPy 1D de 10 dates à partir du 1 Janvier 2022 avec une fréquence mensuelle
dates_2 = np.datetime64('2022-01-01', 'M') + np.arange(5)
# Affichage des dates
print("\nDates : " + str(dates_2))


# Date de départ 1 Janvier 2023
start_year = np.datetime64('2023-01-01')
# Date de fin 31 Décembre 2023
end_year = np.datetime64('2023-12-31')
# Création d'un tableau NumPy 1D de 10 valeurs aléatoires entre la date de départ et la date de fin représentant les jours de l'année 2023
random_dates = np.random.randint(0, (end_year - start_year + 1).astype(int), 10)
# Conversion des jours en dates réelles en ajoutant chaque nombre de jours alétoires à la date de départ
random_timestamps = start_year + random_dates
# Affichage des dates
print("\nDates : " + str(random_timestamps))


# -----------------------------------------------------------------------
# -----------------------------------------------------------------------


#Exercice 17 : Creating Arrays with Custom Data Types
print("\n\n\nExercice 17 : Creating Arrays with Custom Data Types\n")

# Définition d'un type de données personnalisé pour les entiers et leurs représentations binaires
datatype_1 = np.dtype([('number', np.int32), ('binary', 'U8')])
# Création d'un tableau NumPy 1D avec longueur 5 avec le type de données personnalisé
array_50 = np.array([(i, format(i, 'b')) for i in range (1, 6)], dtype = datatype_1)
# Affichage du tableau
print("Array 50 : " + str(array_50))


# Définition d'un type de données personnalisé pour les nombres complexes
datatype_2 = np.dtype([('real', np.float64), ('imag', np.float64)])
# Création d'un tableau NumPy 2D de nombres complexes en utilisant le type de données personnalisé de forme (3, 3)
array_51 = np.array([
    [(1, 2), (3, 4), (5, 6)], 
    [(7, 8), (9, 10), (11, 12)], 
    [(13, 14), (15, 16), (17, 18)]], 
    dtype = datatype_2)
# Affichage du tableau
print("\nArray 51 : " + str(array_51))


# Définition d'un type de données structuré pour les livres
datatype_3 = np.dtype([('title', 'U50'), ('author', 'U50'), ('pages', np.int32)])
# Création d'un tableau avec des informations sur les trois livres en utilisant le type de données personnalisé
array_52 = np.array([
    ('Les misérables', 'Victor Hugo', 1664),
    ('Le Cri de la mouette', 'Emmanuelle Laborit', 206),
    ('Les Trois mousquetaires', 'Alexandre Dumas', 888)],
    dtype = datatype_3)
# Affichage du tableau
print("\nArray 52 : " + str(array_52))