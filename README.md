<img align="left" width="100" src="http://departement-math.univ-tlse3.fr/medias/photo/logosidbigdata_1518444334675-png?ID_FICHE=301126">
<img align="left" width="100" src="https://upload.wikimedia.org/wikipedia/fr/a/a4/Logo_UT3.jpg">
<img align="right" width="100" src="https://www.senscritique.com/senscritique.png">
<br />
<br />
<br />
<h2>G2_Filtrage_Collaboratif</h2>
<h4>Dans le cadre du Projet/Challenge inter-promo de la formation SID (Statistique et Informatique Décisionnelle), en partenariat avec le site Sens Critique, nous avons pu participer à l'amélioration de leur système de recommandation afin de proposer aux utilisateurs de meilleures suggestions de produits.
<br />
<br />
Sens Critique est un site internet permettant à ses utilisateurs de noter et commenter des films, séries, jeux vidéos, livres, bandes dessinées et musiques.
<br />
<br />
Le principal objectif de notre groupe "filtrage collaboratif" est de pouvoir prédire la note d'un utilisateur à partir des notes des utilisateurs qui lui sont similaires.
<br />
<br />
Pour mener à bien notre projet, nous avons tout d'abord créé le répertoire "Src" qui se divise en 2 sous-répertoires : "Matrices" et "Prédiction" contenant les fichiers avec nos codes python. Ces fichiers sont composés des différentes fonctions nous permettant de réaliser les étapes allant de la lecture des données à la création de la matrice avec les notes prédites.
<br />
Pour atteindre nos objectifs, nous avons tout d'abord utilisé les données fournies par Sens Critique et plus précisément les tables Products (contenant les données sur les films, séries, livres...) et Ratings (contenant les différentes notes attribuées par un utilisateur sur un produit). Nous avons ensuite réalisé une jointure entre ces tables pour extraire uniquement les notes correspondant à des films, afin d'effectuer une analyse monomodale (sur un seul produit) dans un premier temps. Nous avons ensuite transformé la table obtenue en matrice Users/Items contenant la note attribuée pour chaque utilisateur (en ligne) et film (en colonne). L'objectif des prochaines étapes est donc de remplacer les nombreuses valeurs manquantes (nan), contenues dans cette matrice, par des notes prédites. Pour ce faire, nous avons tout d'abord débiaisé les notes en centrant et réduisant cette matrice. Cette étape a permis mettre à la même échelle les systèmes de notation des utilisateurs, afin de pourvoir par la suite comparer les notes entre elles. Nous avons ensuite utilisé la similarité cosinus sur la matrice Users/Users pour calculer la distance/similarité entre les utilisateurs et ainsi pouvoir déterminer les k plus proches utilisateurs grâce à la méthode KNN (K-Nearest Neighbors). L'étape suivante consiste à remplacer les nan de la première matrice Users/Items par les notes prédites. Ainsi, chaque valeur manquante est calculée grâce à la moyenne des notes des k plus proches voisins ayant vu ce film. Enfin, la dernière étape consiste à réintroduire le biais pour obtenir une matrice Users/Items avec les notes prédites comprises entre 1 et 10.
<br />
<br />
De plus, nous disposons également du répertoire "Biblios" comportant notamment des documents/aides sur le langage python et sur les systèmes de recommandation.
<br />
Nous avons aussi créé le répertoire "Rapport" qui contient le diagramme de Gantt de notre projet, ainsi que les 2 rapports à rendre : l'un pour Sens Critique et l'autre pour les enseignants.
<br />
Enfin, le dernier répertoire "Qualité" contient la charte de codage à respecter dans nos programmes.
</h4>
