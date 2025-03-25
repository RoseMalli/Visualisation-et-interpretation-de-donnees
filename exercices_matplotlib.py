import numpy as np
import matplotlib
import matplotlib.pyplot as plt



# Nom : MOHAMED KAMALUDEEN
# Prénom : Syedha Memouna
# Numéro d'étudiant : 20006505



# Exercice 1 : Simple Polynomial Plot
print("Exercice 1 : Simple Polynomial Plot\n")


# Création d'un tableau x avec 100 valeurs espacées uniformément entre -10 et 10
x = np.linspace(-10, 10, 100)
# Création d'un tableau y pour la fonction polynomiale : y = 2x^3 - 5x^2 + 3x - 7
y = 2 * x ** 3 - 5 * x ** 2 + 3 * x - 7
# Création d'une figure avec la taille 10x6
plt.figure(figsize = (10, 6))
# Tracé y en fonction de x avec une ligne bleue
plt.plot(x, y, color = "blue", label = "$y = 2x^3 - 5x^2 + 3x - 7$")
# Ajout des étiquettes aux axes x et y
plt.xlabel("x")
plt.ylabel("y")
# Ajout d'un titre au graphique
plt.title("Simple Polynomial Plot")
# Ajout de la légende
plt.legend()
# Affichage du graphique
plt.show()


# -----------------------------------------------------------------------
# -----------------------------------------------------------------------


# Exercice 2 : Exponential and Logarithmic Plot
print("Exercice 2 : Exponential and Logarithmic Plot\n")


# Création d'un tableau x avec 500 valeurs espacées uniformément entre 0.1 et 10
x = np.linspace(0.1, 10, 500)
# Calcul y1 = exp(x)
y1 = np.exp(x)
# Calcul y2 = log(x)
y2 = np.log(x)
# Création d'une figure
plt.figure()
# Tracé des deux fonctions sur le même graphique avec des couleurs et styles de lignes différents
plt.plot(x, y1, color = "blue", label = "$exp(x)$", linestyle = ":")
plt.plot(x, y2, color = "green", label = "$log(x)$", linestyle = "-")
# Ajout d'une grille 
plt.grid()
# Ajout des étiquettes aux axes x et y
plt.xlabel("x")
plt.ylabel("y")
# Ajout d'un titre au graphique 
plt.title("Exponential and Logarithmic Plot")
# Ajout de la légende
plt.legend()
# Enregistrement du graphique sous forme de fichier PDF avec une résolution de 100 DPI
plt.savefig("./exponential_logarithmic_plot.png", format = "png", dpi = 100)
# Affichage du graphique
plt.show()


# -----------------------------------------------------------------------
# -----------------------------------------------------------------------


# Exercice 3 : Figure and Subplots
print("Exercice 3 : Figure and Subplots\n")


# Création d'un tableau x1 avec 500 valeurs espacées uniformément entre -2pi et 2pi
x1 = np.linspace(-2 * np.pi, 2 * np.pi, 500)
# Création d'un tableau x2 avec 500 valeurs espacées uniformément entre -2 et 2
x2 = np.linspace(-2, 2, 500)
# Calcul de y_tan = tan(x1)
y_tan = np.tan(x1)
# Calcul de y_arctan = arctan(x1)
y_arctan = np.arctan(x1)
# Calcul de y_sinh = sinh(x2)
y_sinh = np.sinh(x2)
# Calcul de y_cosh = cosh(x2)
y_cosh = np.cosh(x2)
# Création d'une figure avec 2 sous-graphiques disposés en une seule ligne
fig, axes = plt.subplots(1, 2, figsize = (8, 4))
# Tracé de y_tan et y_arctan sur le même premier sous-graphique avec des couleurs différentes
axes[0].plot(x1, y_tan, color = "blue", label = "$tan(x)$")
axes[0].plot(x1, y_arctan, color = "green", label = "$arctan(x)$")
# Ajout des étiquettes aux axes
axes[0].set_xlabel("x")
axes[0].set_ylabel("y")
# Ajout d'un titre pour le premier sous graphique
axes[0].set_title(r'Plot of y = tan(x) and y = arctan(x)')
# Ajout d'une légende pour le premier sous-graphique
axes[0].legend()
# Tracé de y_sinh et y_cosh sur le même deuxième sous-graphique avec des couleurs différentes
axes[1].plot(x2, y_cosh, color = "red", label = "$sinh(x)$")
axes[1].plot(x2, y_sinh, color = "orange", label = "$cosh(x)$")
# Ajout des étiquettes aux axes
axes[1].set_xlabel("x")
axes[1].set_ylabel("y")
# Ajout d'un titre pour le deuxième sous graphique
axes[1].set_title("Plot of $y = sinh(x)$ and $y = cosh(x)$")
# Ajout d'une légende pour le deuxième sous-graphique
axes[1].legend()
# Ajustement de la mise en page
fig.tight_layout()
# Affichage du graphique
plt.show()


# -----------------------------------------------------------------------
# -----------------------------------------------------------------------


# Exercice 4 : Histogram
print("Exercice 4 : Histogram\n")


# Création d'un tableau n avec 1000 valeurs aléatoires suivant une distribution normale standard
n = np.random.randn(1000)
# Tracé d'un histogramme de ces valeurs avec 30 bins en bleue ciel
plt.hist(n, bins = 30, color = "skyblue")
# Ajoute d'un titre
plt.title("Histogram of Random Values")
# Définition de la limite de l'axe des x pour couvrir toute la plage de n
plt.xlim(np.min(n), np.max(n))
# Affichage du graphique
plt.show()


# -----------------------------------------------------------------------
# -----------------------------------------------------------------------


# Exercice 5 : Scatter Plot
print("Exercice 5 : Scatter Plot\n")


# Création d'un tableau x avec 500 valeurs uniformément réparti entre 0 et 1
x = np.random.uniform(0, 1, 500)
# Création d'un tableau y = sin(x) + un bruit aléatoire avec 500 valeurs aléatoires 
# suivant une distribution normale standard
y = np.sin(x) + np.random.randn(500)
# Variation de la taille en fonction des valeurs de y
sizes = 20 + 100 * (y - np.min(y)) / (np.max(y) - np.min(y))
# Tracé d'un nuage de points de y en fonction de x en faisant varier la taille 
# et la couleur des marqueurs en fonction des valeurs de y
plt.scatter(x, y, c = y, s = sizes)
# Ajout d'une grille
plt.grid()
# Masque des graduations des axes
plt.axis("off")
# Ajout d'un titre pour le graphique
plt.title("Scatter plot")
# Enregistrement du graphique au format PDF
plt.savefig("scatter_plot.pdf", format = "PDF")
# Affichage du graphique
plt.show()


# -----------------------------------------------------------------------
# -----------------------------------------------------------------------


# Exercice 6 : Contour Plot
print("Exercice 6 : Contour Plot\n")


# Création d'un tableau x avec 200 valeurs espacées uniformément entre -5 et 5
x = np.linspace(-5, 5, 200)
# Création d'un tableau y avec 200 valeurs espacées uniformément entre -5 et 5
y = np.linspace(-5, 5, 200)
# Création d'une grille 2D avec numpy.meshgrid
X, Y = np.meshgrid(x, y)
# Defintion de la fonction f(x, y) = sin(sqrt(x^2 + y^2))
def f(x, y):
    return np.sin(np.sqrt(X ** 2 + Y ** 2))
# Tracé d'une courbe de niveau de cette fonction en utilisant une palette de couleurs 
# différente
plt.contour(X, Y, f(X, Y), cmap = "plasma")
# Ajout des étiquettes aux axes
plt.xlabel("X")
plt.ylabel("Y")
# Ajout d'un titre pour le graphique
plt.title("Contour Plot")
# Affichage du graphique
plt.show()


# -----------------------------------------------------------------------
# -----------------------------------------------------------------------


# Exercice 7 : 3D Surface Plot
print("Exercice 7 : 3D Surface Plot\n")


# Création d'un X avec des valeurs entre -5 et 5 avec un pas de 0.25
X = np.arange(-5, 5, 0.25)
# Création d'un Y avec des valeurs entre -5 et 5 avec un pas de 0.25
Y = np.arange(-5, 5, 0.25)
# Création d'une grille 2D avec numpy.meshgrid
X, Y = np.meshgrid(X, Y)
# Calcul Z = cos(sqrt(X^2 + Y^2))
Z = np.cos(np.sqrt(X ** 2 + Y ** 2))
# Création d'une figure et du graphique 3D
fig = plt.figure(figsize = (10, 8), dpi = 80)
axe = fig.add_subplot(111, projection = "3d")
# Tracé d'un graphique de surface 3D de Z en changeant la palettre de couleurs
surf = axe.plot_surface(X, Y, Z, cmap = "viridis")
# Ajout d'une barre de couleur
fig.colorbar(surf)
# Ajout des étiquettes aux axes
axe.set_xlabel("X")
axe.set_ylabel("Y")
axe.set_zlabel("Z")
# Ajoout d'un titre pour le graphique
axe.set_title("3D Surface Plot of $Z = cos(sqrt(X^2 + Y^2))$")
# Modification de l'angle de vue du graphique
axe.view_init(elev = 30, azim = 45)
# Affichage du graphique
plt.show()


# -----------------------------------------------------------------------
# -----------------------------------------------------------------------


# Exercice 8 : Line and Marker Styles
print("Exercice 8 : Line and Marker Styles\n")


# Création d'un tableau x avec 10 valeurs espacées uniformément entre -2 et 2
x = np.linspace(-2, 2, 10)
# Calcul de y1 = x^2
y1 = x**2
# Calcul de y2 = x^3
y2 = x**3 
# Calcul de y3 = x^4
y3 = x**4
# Création d'une figure
plt.figure()
# Tracé des trois fonctions sur le même graphique en utilisant différentes couleurs, 
# styles de lignes et marqueurs
plt.plot(x, y1, color = "blue", label = "$y1 = x^2$", linestyle = ":")
plt.plot(x, y2, color = "green", label = "$y2 = $x^3$", linestyle = "-")
plt.plot(x, y3, color = "red", label = "$y3 = x^4$", linestyle = "--")
# Ajout des étiquettes aux axes
plt.xlabel("x")
plt.ylabel("y")
# Ajout d'un titre
plt.title("Plot of $y1$, $y2$ and $y3$")
plt.legend()
# Affichage du graphique
plt.show()


# -----------------------------------------------------------------------
# -----------------------------------------------------------------------


# Exercice 9 : Logarithmic Scale
print("Exercice 9 : Logarithmic Scale\n")


# Création d'un tableau x avec 50 valeurs espacées uniformément entre 1 et 100
x = np.linspace(1, 100, 50)
# Calcul de y1 = 2^x
y1 = 2 ** x
# Calcul de y2 = log2(x)
y2 = np.log2(x)
# Création de la figure avec la taille 12x6
plt.figure(figsize = (12, 6))
# Tracé de y1 et y2 avec échelle logarithmique pour l'axe y
plt.plot(x, y1, color = "blue", label = "$y1 = 2^x$")
plt.plot(x, y2, color = "violet", label = "$y2 log2(x)$")
plt.yscale("log")
# Ajout des étiquettes aux axes
plt.xlabel("x")
plt.ylabel("y")
# Ajout d'un titre pour le graphique
plt.title("Logarithmic Scale for y-axis")
# Ajout d'une grille
plt.grid()
# Affichage du graphique
plt.show()


# -----------------------------------------------------------------------
# -----------------------------------------------------------------------


# Exercice 10 : Changing Viewing Angle
print("Exercice 10 : Changing Viewing Angle\n")


# Création d'un X avec des valeurs entre -5 et 5 avec un pas de 0.25
X = np.arange(-5, 5, 0.25)
# Création d'un Y avec des valeurs entre -5 et 5 avec un pas de 0.25
Y = np.arange(-5, 5, 0.25)
# Création d'une grille 2D avec numpy.meshgrid
X, Y = np.meshgrid(X, Y)
# Calcul Z = cos(sqrt(X^2 + Y^2))
Z = np.cos(np.sqrt(X ** 2 + Y ** 2))
# Création d'une figure
fig = plt.figure(figsize = (30, 12))
# Création du premier sous-graphique avec un angle de vue différent en 
# ajoutant un titre et utilisant view_init
axe1 = fig.add_subplot(121, projection = "3d")
axe1.plot_surface(X, Y, Z, cmap = "viridis")
axe1.view_init(elev = 30, azim = 45)
axe1.set_title("Viewing Angle (30, 45)")
# Création du deuxième sous-graphique avec un angle de vue différent en 
# ajoutant un titre et utilisant view_init
axe2 = fig.add_subplot(1, 2, 2, projection = "3d")
axe2.plot_surface(X, Y, Z, cmap = "viridis")
axe2.view_init(elev = 60, azim = 90)
axe2.set_title("Viewing Angle (60, 90)")
# Affichage du graphique
plt.show()


# -----------------------------------------------------------------------
# -----------------------------------------------------------------------


# Exercice 11 : 3D Wireframe Plot
print("Exercice 11 : 3D Wireframe Plot\n")


# Création d'un X avec des valeurs entre -5 et 5 avec un pas de 0.25
X = np.arange(-5, 5, 0.25)
# Création d'un Y avec des valeurs entre -5 et 5 avec un pas de 0.25
Y = np.arange(-5, 5, 0.25)
# Création d'une grille 2D avec numpy.meshgrid
X, Y = np.meshgrid(X, Y)
# Calcul Z = sin(X) * cos(Y)
Z = np.sin(X) * np.cos(Y)
# Création d'une figure
fig = plt.figure(figsize = (25, 10))
# Tracé du graphique 3D en maillage de Z
axe = fig.add_subplot(111, projection = "3d")
axe.plot_wireframe(X, Y, Z, color = "indigo")
# Changement de l'angle de vue 
axe.view_init(elev = 35, azim = 50)
# Ajout d'un titre pour le graphique
axe.set_title("3D Wireframe Plot of $Z = \sin(X) * \cos(Y)$")
# Afichage du graphique
plt.show()


# -----------------------------------------------------------------------
# -----------------------------------------------------------------------


# Exercice 12 : 3D Contour Plot
print("Exercice 12 : 3D Contour Plot\n")


# Création d'un X avec des valeurs entre -5 et 5 avec un pas de 0.25
X = np.arange(-5, 5, 0.25)
# Création d'un Y avec des valeurs entre -5 et 5 avec un pas de 0.25
Y = np.arange(-5, 5, 0.25)
# Création d'une grille 2D avec numpy.meshgrid
X, Y = np.meshgrid(X, Y)
# Calcul Z = exp(-0.1 * (X^2 + Y^2))
Z = np.exp(-0.1 * (X ** 2 + Y ** 2))
# Création d'une figure
fig = plt.figure()
# Tracé du graphique de contour 3D de Z en utilisant contour3D et changeant 
# la palette de couleurs
ax = fig.add_subplot(111, projection = "3d")
contour = ax.contour3D(X, Y, Z, cmap = "inferno")
# Ajout des étiquettes aux axes
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
# Ajout d'un titre pour le graphique
ax.set_title("3D Contour Plot of $Z = exp(-0.1 * (X^2 + Y^2))$")
# Affichage du graphique
plt.show()


# -----------------------------------------------------------------------
# -----------------------------------------------------------------------


# Exercice 13 : 3D Parametric Plot
print("Exercice 13 : 3D Parametric Plot\n")


# Création d'un tableau t avec 100 valeurs espacées uniformément entre 0 et 2pi
t = np.linspace(0, 2 * np.pi, 100)
# Calul X = sin(t)
X = np.sin(t)
# Calcul Y = cos(t)
Y = np.cos(t)
# Calcul Z = t
Z = t
# Création d'une figure 
fig = plt.figure()
# Tracé d'un graphique paramétrique 3D de X, Y et Z en changeant la couleur
ax = fig.add_subplot(111, projection = "3d")
ax.plot(X, Y, Z, color = "magenta")
# Ajout d'un titre pour le graphique
ax.set_title("3D Parametric Plot of $X = sin(t)$, $Y = cos(t)$ and $Z = t$")
# Ajout des étiquettes aux axes
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
# Affichage du graphique
plt.show()


# -----------------------------------------------------------------------
# -----------------------------------------------------------------------


# Exercice 14 : 3D Bar Plot
print("Exercice 14 : 3D Bar Plot\n")


# Création d'un tableau x avec 10 valeurs espacées uniformément entre -5 et 5
x = np.linspace(-5, 5, 10)
# Création d'un tableau y avec 10 valeurs espacées uniformément entre -5 et 5
y = np.linspace(-5, 5, 10)
# Création d'une grille 2D avec numpy.meshgrid
X, Y = np.meshgrid(x, y)
# Calcul Z = exp(-0.1 * (X^2 + Y^2))
Z = np.exp(-0.1 * (X**2 + Y**2))
# Création d'une figure
fig = plt.figure()
# Tracé d'un graphique en barres 3D des valeurs de Z
ax = fig.add_subplot(111, projection = "3d")
bar = ax.bar3d(X.flatten(), Y.flatten(), np.zeros_like(Z.flatten()), 1, 1, Z.flatten(), shade = True)
# Ajout d'une barre de couleur 
fig.colorbar(bar)
# Ajout des étiquettes aux axes
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
# Ajout d'un titre pour le graphique
ax.set_title("3D Bar Plot of $Z = exp(-0.1 * (X^2 + Y^2))$")
# Changement de l'angle de vue
ax.view_init(elev = 30, azim = 45)
# Affichage du graphique 
plt.show()


# -----------------------------------------------------------------------
# -----------------------------------------------------------------------


# Exercice 15 : 3D Vector Field
print("Exercice 15 : 3D Vector Field\n")


# Création d'un tableau x avec 10 valeurs espacées uniformément entre -5 et 5
x = np.linspace(-5, 5, 10)
# Création d'un tableau y avec 10 valeurs espacées uniformément entre -5 et 5
y = np.linspace(-5, 5, 10)
# Création d'un tableau z avec 10 valeurs espacées uniformément entre -5 et 5
z = np.linspace(-5, 5, 10)
# Création d'une grille 2D avec numpy.meshgrid
X, Y, Z = np.meshgrid(x, y, z)
# Calcul = U = -Y
U = -Y
# Calcul V = X
V = X
# Calcul W = Z
W = Z
# Création d'une figure
fig = plt.figure()
# Tracé d'un champ de vecteurs 3D en utilisant quiver3D
ax = fig.add_subplot(111, projection = "3d")
ax.quiver(X, Y, Z, U, V, W, length = 0.5, color = "blue", normalize = True)
# Ajout d'un titre pour le graphique
ax.set_title("3D Vector Field")
# Ajout des étiquettes aux axes
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
# Affichage du graphique
plt.show()


# -----------------------------------------------------------------------
# -----------------------------------------------------------------------


# Exercice 16 : 3D Scatter Plot
print("Exercice 16 : 3D Scatter Plot\n")


# Création d'un tableau x avec 100 valeurs aléatoires suivant une distribution normale standard
x = np.random.randn(100)
# Création d'un tableau y avec 100 valeurs aléatoires suivant une distribution normale standard
y = np.random.randn(100)
# Création d'un tableau z avec 100 valeurs aléatoires suivant une distribution normale standard
z = np.random.randn(100)
# Création d'une figure
fig = plt.figure()
# Tracé d'un graphique de dispersion 3D de ces points coloriés en fonction de z
ax = fig.add_subplot(111, projection = "3d")
scat = ax.scatter(x, y, z, c = z, cmap = "viridis")
# Ajout d'une barre de couleur
fig.colorbar(scat)
# Ajout des étiquettes aux axes
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
# Ajout d'un titre pour le graphique
ax.set_title("3D Scatter Plot")
# Affichage du graphique
plt.show()


# -----------------------------------------------------------------------
# -----------------------------------------------------------------------


# Exercice 17 : 3D Line Plot
print("Exercice 17 : 3D Line Plot\n")


# Création d'un tableau t avec 100 valeurs espacées uniformément entre 0 et 4pi 
t = np.linspace(0, 4 * np.pi, 100)
# Calcul X = sin(t)
X = np.sin(t)
# Calcul Y = cos(t)
Y = np.cos(t)
# Calcul Z = t
Z = t
# Création d'une figure
fig = plt.figure()
# Tracé d'un graphique de ligne 3D de X, Y, et Z
ax = fig.add_subplot(111, projection = "3d")
ax.plot(X, Y, Z, color = "magenta", linewidth = 2)
# Ajout des étiquettes aux axes
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
# Ajout d'un titre pour le graphique
ax.set_title("3D Line Plot of $X = sin(t)$, $Y = cos(t)$ and $Z = t$")
# Affichage du graphique
plt.show()


# -----------------------------------------------------------------------
# -----------------------------------------------------------------------


# Exercice 18 : 3D Filled Contour Plot
print("Exercice 18 : 3D Filled Contour Plot\n")


# Création d'un tableau X avec des valeurs entre -5 et 5 avec un pas de 0.1
X = np.arange(-5, 5.1, 0.1)
# Création d'un tableau Y avec des valeurs entre -5 et 5 avec un pas de 0.1
Y = np.arange(-5, 5.1, 0.1)
# Création d'une grille 2D avec numpy.meshgrid
X, Y = np.meshgrid(X, Y)
# Calcul Z = sin(sqrt(X^2 + Y^2))
Z = np.sin(np.sqrt(X**2 + Y**2))
# Création d'une figure
fig = plt.figure()
# Tracé d'un graphique de contours remplis en 3D de Z en changeant la colormap
ax = fig.add_subplot(111, projection = "3d")
contour = ax.contourf(X, Y, Z, 50, cmap = "plasma") 
# Ajout d'une barre de couleur
fig.colorbar(contour)
# Ajout des étiquettes aux axes
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
# Ajout d'un titre pour le graphique
ax.set_title("3D Filled Contour Plot of $Z = sin(sqrt(X^2 + Y^2))$")
# Affichage du graphique
plt.show()


# -----------------------------------------------------------------------
# -----------------------------------------------------------------------


# Exercice 19 : 3D Heatmap
print("Exercice 19 : 3D Heatmap\n")


# Création d'un tableau x avec 50 valeurs espacées uniformément entre -5 et 5 
x = np.linspace(-5, 5, 50)
# Création d'un tableau y avec 50 valeurs espacées uniformément entre -5 et 5 
y = np.linspace(-5, 5, 50)
# Création d'une grille 2D avec numpy.meshgrid
X, Y = np.meshgrid(x, y)
# Calcul Z = sin(sqrt(X^2 + Y^2)) 
Z = np.sin(np.sqrt(X**2 + Y**2))
# Création d'une figure
fig = plt.figure()
# Tracé d'une carte thermique de Z
axe = fig.add_subplot(111, projection = "3d")
surf = axe.plot_surface(X, Y, Z, cmap = "viridis")
# Ajout d'une barre de couleur
fig.colorbar(surf)
# Ajout des étiquettes aux axes
axe.set_xlabel("X")
axe.set_ylabel("Y")
axe.set_zlabel("Z")
# Ajout d'un titre pour le graphique
axe.set_title("3D Heatmap of $Z = sin(sqrt(X^2 + Y^2))$")
# Affichage du graphique
plt.show()


# -----------------------------------------------------------------------
# -----------------------------------------------------------------------


# Exercice 20 : 3D Density Plot
print("Exercice 20 : 3D Density Plot\n")


# Création d'un tableau x avec 1000 valeurs aléatoires suivant une distribution normale standard
x = np.random.randn(1000)
# Création d'un tableau y avec 1000 valeurs aléatoires suivant une distribution normale standard
y = np.random.randn(1000)
# Création d'un tableau z avec 1000 valeurs aléatoires suivant une distribution normale standard
z = np.random.randn(1000)
# Calcule de la distance de chaque point par rapport à l'origine
distance = np.sqrt(x**2 + y**2 + z**2)
# Création d'une figure
fig = plt.figure()
# Tracé d'un graphique de densité en 3D pour montrer où les points sont concentrés
axe = fig.add_subplot(111, projection = "3d")
surf = axe.scatter(x, y, z, c = distance, cmap = "viridis", alpha = 0.5)
# Ajout d'une barre de couleur
fig.colorbar(surf)
# Ajout des étiquettes aux axes
axe.set_xlabel("X")
axe.set_ylabel("Y")
axe.set_zlabel("Z")
# Ajout d'un titre
axe.set_title("3D Density Plot")
# Affichage du graphique
plt.show()