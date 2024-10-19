# WatsappExportohtml

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
