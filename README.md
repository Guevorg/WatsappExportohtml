# WatsappExportohtml


Instruction pour le programme de génération de page HTML depuis une archive WhatsApp
Description :
Ce programme permet de :

Désarchiver un fichier ZIP contenant une conversation WhatsApp et ses médias.
Renommer et déplacer le fichier de discussion texte à la racine du projet.
Cloner un projet GitHub pour la génération de pages HTML et l'utiliser pour convertir la conversation en fichier HTML.
Générer une page HTML interactive avec la conversation, incluant les liens pour les fichiers multimédias (images, vidéos, audio, etc.).
Ouvrir automatiquement le fichier HTML généré dans un navigateur web.
Pré-requis :
Python 3.x doit être installé sur votre machine.
Git doit être installé pour pouvoir cloner le dépôt GitHub.
Les dépendances du projet GitHub seront automatiquement prises en charge par le script.
Structure du projet attendu après exécution :
bash
Copier le code
/chemin_vers_votre_projet/
│
├── media/                       # Dossier contenant les fichiers multimédias (extrait du fichier ZIP)
│
├── pics/                        # Dossier contenant des images pour les icônes de lecture de médias
│
├── Discussion.txt               # Fichier contenant la discussion WhatsApp
│
├── genhtml.py                   # Script pour générer le fichier HTML de la conversation
│
├── whatsapp_conversation.html    # Fichier HTML généré, contenant la conversation formatée
│
└── run.py                       # Script principal à exécuter
Étapes pour exécuter le programme :
Télécharger le fichier ZIP de la conversation WhatsApp :

Exportez une conversation WhatsApp depuis l'application en choisissant l'option "Exporter" avec ou sans médias. Cela génère un fichier ZIP contenant un fichier texte de la discussion et un dossier contenant les fichiers multimédias (images, vidéos, etc.).
Placez le fichier ZIP dans le même dossier que le script :

Le fichier ZIP doit commencer par "Discussion WhatsApp" et être placé dans le même dossier que le script run.py.
Exécuter le programme :

Ouvrez une console ou un terminal.
Naviguez jusqu'au dossier où se trouvent run.py et le fichier ZIP.
Exécutez la commande suivante :
bash
Copier le code
python run.py
Résultats attendus :

Le fichier ZIP sera automatiquement décompressé dans un dossier media/.
Le fichier de discussion texte sera renommé en Discussion.txt et déplacé à la racine du projet.
Le projet GitHub sera cloné, et les fichiers nécessaires seront extraits.
Le script genhtml.py sera exécuté pour générer un fichier HTML de la conversation dans le fichier whatsapp_conversation.html.
Le fichier HTML sera ouvert automatiquement dans votre navigateur web.
Consulter la conversation :

Une fois le script exécuté, la page whatsapp_conversation.html s'ouvre dans votre navigateur avec la conversation formatée, incluant les liens vers les médias (images, vidéos, audio).
Problèmes fréquents et solutions :
Erreur d'accès refusé (PermissionError) : Si vous rencontrez des erreurs de permission (en particulier sous Windows), assurez-vous d'exécuter le programme avec les droits administrateur.
Le fichier ZIP n'est pas trouvé : Vérifiez que le nom du fichier ZIP commence bien par "Discussion WhatsApp" et qu'il est bien placé dans le même dossier que le script.
Git non installé : Assurez-vous d'avoir installé Git pour pouvoir cloner le projet GitHub. Vous pouvez télécharger Git depuis ce lien.
En résumé, ce programme automatisera le processus de conversion de vos discussions WhatsApp en un fichier HTML facilement lisible et partageable, avec les fichiers multimédias intégrés !



Explication du code :
Désarchivage du fichier ZIP : La fonction unzip_file() extrait tout le contenu du fichier ZIP dans un dossier appelé media/.
Renommage du fichier de discussion : La fonction rename_discussion_file() recherche le fichier texte contenant la discussion et le renomme en Discussion.txt.
Téléchargement du projet GitHub : La fonction clone_github_repo() télécharge le projet depuis le dépôt GitHub WatsappExportohtml.
Copie du dossier pics : La fonction copy_pics_to_base() copie le dossier pics dans le même niveau que media et Discussion.txt.
Exécution du script genhtml.py : La fonction run_genhtml_script() exécute le script Python genhtml.py qui va générer le fichier HTML.
Ouverture du fichier HTML dans un navigateur : Enfin, la fonction open_html_in_browser() ouvre le fichier généré whatsapp_conversation.html dans le navigateur par défaut.
Pré-requis :
Python doit être installé sur votre système (avec le module GitPython).
Installez GitPython en exécutant la commande : pip install GitPython.
Vous devez avoir un fichier ZIP nommé Discussion WhatsApp.zip et contenant la discussion WhatsApp et les médias.
L'accès à internet est requis pour télécharger le projet GitHub.
Exécution :
Ce script va automatiquement gérer toutes les étapes : extraction du ZIP, renommage du fichier, téléchargement et exécution du projet, puis affichage de la page HTML dans un navigateur.
