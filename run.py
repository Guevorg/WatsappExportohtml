import os
import zipfile
import shutil
import subprocess
import stat
import webbrowser
from git import Repo

# Chemins et variables globaux
media_dir = "media/"
discussion_txt = "Discussion.txt"
project_dir = "WatsappExportohtml"
html_output_file = "whatsapp_conversation.html"
repo_url = "https://github.com/Guevorg/WatsappExportohtml.git"

# Fonction pour trouver le fichier ZIP qui commence par "Discussion WhatsApp"
def find_whatsapp_zip():
    for file in os.listdir('.'):
        if file.startswith("Discussion WhatsApp") and file.endswith(".zip"):
            return file
    raise FileNotFoundError("Aucun fichier ZIP ne commence par 'Discussion WhatsApp' dans le répertoire courant.")

# Fonction pour désarchiver un fichier ZIP et extraire son contenu dans un dossier
def unzip_file(zip_file, extract_to):
    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        zip_ref.extractall(extract_to)
    print(f"Fichier {zip_file} désarchivé dans {extract_to}")

# Fonction pour renommer et déplacer le fichier de discussion à la racine
def move_and_rename_discussion_file(media_dir):
    for file_name in os.listdir(media_dir):
        if "discussion" in file_name.lower() and file_name.endswith(".txt"):
            old_path = os.path.join(media_dir, file_name)
            new_path = os.path.join(".", discussion_txt)  # Déplacement vers la racine
            os.rename(old_path, new_path)
            print(f"Fichier {file_name} déplacé et renommé en {discussion_txt} à la racine.")
            return new_path
    raise FileNotFoundError("Aucun fichier de discussion trouvé dans le dossier média.")

# Fonction pour modifier les permissions d'un fichier/dossier
def remove_readonly(func, path, excinfo):
    os.chmod(path, stat.S_IWRITE)
    func(path)

# Fonction pour télécharger le projet GitHub et l'extraire à la racine
def clone_github_repo_to_root(repo_url):
    if not os.path.exists(project_dir):
        Repo.clone_from(repo_url, project_dir)
        print(f"Répertoire {project_dir} cloné depuis GitHub.")

        # Copier tout le contenu du dossier Git vers la racine, sauf les dossiers qui existent déjà
        for item in os.listdir(project_dir):
            item_path = os.path.join(project_dir, item)
            destination_path = os.path.join(".", item)
            if not os.path.exists(destination_path):  # Si le fichier ou dossier n'existe pas déjà
                shutil.move(item_path, ".")
            else:
                print(f"Le chemin {destination_path} existe déjà, il ne sera pas déplacé.")
        
        # Supprimer le dossier WatsappExportohtml en modifiant les permissions
        shutil.rmtree(project_dir, onerror=remove_readonly)
        print(f"Le dossier {project_dir} a été supprimé.")
    else:
        print(f"Le projet {project_dir} existe déjà.")

# Fonction pour copier le dossier pics dans le même niveau que le dossier media et Discussion.txt
def ensure_pics_in_root():
    if not os.path.exists("pics"):
        raise FileNotFoundError("Le dossier pics est manquant après l'extraction.")
    print("Le dossier pics est déjà à la racine.")

# Fonction pour exécuter le script genhtml.py
def run_genhtml_script():
    script_path = os.path.join(".", "genhtml.py")
    subprocess.run(["python3", script_path], check=True)
    print(f"Le script {script_path} a été exécuté.")

# Fonction pour ouvrir le fichier HTML généré dans un navigateur
def open_html_in_browser(html_file):
    if os.path.exists(html_file):
        webbrowser.open(f"file://{os.path.realpath(html_file)}")
        print(f"Page HTML {html_file} ouverte dans le navigateur.")
    else:
        raise FileNotFoundError(f"Le fichier {html_file} n'existe pas.")

# Fonction principale pour tout le processus
def main():
    # 1. Trouver dynamiquement le fichier ZIP qui commence par "Discussion WhatsApp"
    zip_file = find_whatsapp_zip()

    # 2. Désarchiver le fichier ZIP
    unzip_file(zip_file, media_dir)

    # 3. Renommer et déplacer le fichier contenant la discussion à la racine
    move_and_rename_discussion_file(media_dir)

    # 4. Télécharger le projet depuis GitHub et l'extraire à la racine
    clone_github_repo_to_root(repo_url)

    # 5. S'assurer que le dossier pics est à la racine
    ensure_pics_in_root()

    # 6. Exécuter le script genhtml.py
    run_genhtml_script()

    # 7. Ouvrir la page HTML générée dans un navigateur
    open_html_in_browser(html_output_file)

# Exécuter le script principal
if __name__ == "__main__":
    main()
