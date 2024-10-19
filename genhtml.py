import os

# Fonction pour nettoyer les caractères invisibles du nom du fichier
def clean_filename(filename):
    # Retirer les espaces invisibles (comme U+200E) et autres caractères non imprimables
    return filename.strip().replace('\u200e', '').replace('\u202c', '').replace('\u202a', '')

# Fonction pour générer une bulle de message HTML
def generate_message_bubble(sender, message, timestamp, is_media=False, media_file=None):
    if is_media and media_file:
        # Nettoyer le nom du fichier pour éviter les caractères invisibles
        media_file = clean_filename(media_file)
        message_html = f'<img src="{media_file}" alt="Media" style="max-width: 200px;"/>'
    else:
        # Remplacer les sauts de ligne par des balises <br> pour le rendu HTML
        message_html = message.replace("\n", "<br>")
    me = "Agnès Cantone"
    sender_class = "sender-me" if me in sender else "sender-other"
    
    # Inclure le nom de l'expéditeur avec l'horodatage
    bubble_html = f'''
    <div class="{sender_class}">
        <div class="timestamp">{timestamp} - <strong>{sender}</strong></div>
        <div class="message">{message_html}</div>
    </div>
    '''
    return bubble_html

# Fonction pour analyser la discussion et générer l'HTML
def generate_html_from_whatsapp_chat(chat_file, media_dir, output_html_file):
    with open(chat_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # Créer le squelette du fichier HTML
    html_content = '''
    <html>
    <head>
        <style>
            body { font-family: Arial, sans-serif; background-color: #e5ddd5; padding: 10px; }
            .chat-container { max-width: 600px; margin: auto; background-color: #fff; padding: 20px; border-radius: 10px; }
            .sender-other { text-align: left; margin-bottom: 10px; }
            .sender-me { text-align: right; margin-bottom: 10px; }
            .message { padding: 10px; border-radius: 5px; display: inline-block; }
            .sender-other .message { background-color: #dcf8c6; }
            .sender-me .message { background-color: #34b7f1; color: white; }
            .timestamp { font-size: 10px; color: gray; }
        </style>
    </head>
    <body>
        <div class="chat-container">
    '''
    
    # Variables pour stocker le message en cours
    current_message = ""
    current_sender = ""
    current_timestamp = ""

    # Parcourir chaque ligne de la discussion
    for line in lines:
        if " - " in line:
            # Si on a un message en cours, on l'ajoute à l'HTML
            if current_message:
                html_content += generate_message_bubble(current_sender, current_message, current_timestamp)
            
            # Extraire le timestamp, le nom de l'expéditeur et le message
            timestamp, remainder = line.split(" - ", 1)
            if ": " in remainder:
                sender, message = remainder.split(": ", 1)
                
                if "<Médias omis>" in message:
                    # Cas où le média est omis (pas de fichier précis)
                    current_message = "[Médias omis]"
                    is_media = False
                    media_file = None
                elif "fichier joint" in message:
                    # Identifier le nom du fichier joint et nettoyer les caractères invisibles
                    media_file = clean_filename(message.split(" ")[0].strip("()"))
                    media_file_path = os.path.join(media_dir, media_file)  # Chemin complet du média
                    is_media = True
                    current_message = f'<a href="{media_file_path}"><img src="{media_file_path}" alt="Media" style="max-width: 200px;"/></a>'  # On prépare le chemin pour l'affichage d'image
                else:
                    is_media = False
                    media_file = None
                    current_message = message.strip()  # Nettoyer le message
                    
                # Mettre à jour le sender et le timestamp
                current_sender = sender.strip()
                current_timestamp = timestamp.strip()
        else:
            # Ajouter le texte de la ligne à current_message (multi-lignes)
            if current_message:
                current_message += "\n" + line.strip()

    # Ajouter le dernier message restant s'il existe
    if current_message:
        html_content += generate_message_bubble(current_sender, current_message, current_timestamp)

    # Clôturer le fichier HTML
    html_content += '''
        </div>
    </body>
    </html>
    '''
    
    # Enregistrer le fichier HTML
    with open(output_html_file, 'w', encoding='utf-8') as f:
        f.write(html_content)

# Variables du chemin
chat_file = 'discussion.txt'  # Nom du fichier texte de discussion
media_dir = 'media/'  # Dossier contenant les fichiers média
output_html_file = 'whatsapp_conversation.html'  # Nom du fichier de sortie HTML

# Exécuter la génération du HTML
generate_html_from_whatsapp_chat(chat_file, media_dir, output_html_file)

print(f"Fichier HTML généré: {output_html_file}")
