## Kaggle
Le TP a été réalisé sur Kaggle pour avoir la puissance des gpu pour le training.
Pour lancer le notebook sur kaggle il faut en créée un puis, choisir d'importé le notebook dans 'File', pour turn On les GPU il est nécessaire d'avoir validé son compte, qui demande désormais le numéro de téléphone.


## Cleaning et processing
Un certain nombre de duplicata son présent donc on les retir.
On convertie la valeur sentimental en bool, 0 ou 1.
Les reviews possèdant des balises html, il a été utilisé des regex pour les enlevés.
Remove des hastag et mention.
J'ai essayé de corrigé les erreures présente dans le text avec TextBlob qui est une librairie très connu pour, mais le réalisé sur tout le dataset prends trop de temps 1h+ donc je ne l'est pas utilisé.
De la ponctuation est présente ce qui est inutile pour l'apprentissage donc removed.
On map sur un dictionnaire cherchant a remplacé les mot utilisant un apostrophe dans la langue anglais par une version sans, exemple: "can't"-> "cannot"
Si des emoji ou des url sont présente on les enlèves.
La lemmatization est appliqué sur le texte.
Ils sont par la suite tokenizer et vectorizer.

J'ai essayer de trouvé une librairie pour les abréviations mais pas de résultat concluant (J'aurais pu le faire a la main mais y a beaucoup trop d'abréviation en anglais pour que j'en fasse un dictionnaire).

# Model

Une couche d'Embedding est nécessaire dans les modèle pour convertir les valeur numérique en un vecteur nécessaire.

J'ai réalisé un Lstm qui en 10 epoch arrive a 80 de acc et peut surement etre meilleur avec plus d'entainement.
Puis le Conv1D est celui qui arrive le plus vite a 99 d'accuracy en 3 epochs avec 88 de validation_acc.
Entrainement d'un TCN qui arrive 98 d'accuracy mais ou la validation_acc reste a 83.
J'ai fournie aussi le code d'un bilstm mais le bilstm prends ENORMEMENT de temps a etre entrainé, du coup je ne fournie pas de résultat.

Un modèle en .h5 a été fournit pour le lstm, TCN et Conv1d.

