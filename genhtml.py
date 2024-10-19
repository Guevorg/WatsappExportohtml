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
        message_html = message
    
    sender_class = "sender-me" if "Bruno Cantone" in sender else "sender-other"
    
    bubble_html = f'''
    <div class="{sender_class}">
        <div class="timestamp">{timestamp}</div>
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
    
    # Parcourir chaque ligne de la discussion
    for line in lines:
        if " - " in line:
            # Extraire le timestamp, le nom de l'expéditeur et le message
            timestamp, remainder = line.split(" - ", 1)
            if ": " in remainder:
                sender, message = remainder.split(": ", 1)
                
                if "<Médias omis>" in message:
                    # Cas où le média est omis (pas de fichier précis)
                    message = "[Médias omis]"
                    is_media = False
                    media_file = None
                elif "fichier joint" in message:
                    # Identifier le nom du fichier joint et nettoyer les caractères invisibles
                    media_file = clean_filename(message.split(" ")[0].strip("()"))
                    media_file_path = os.path.join(media_dir, media_file)  # Chemin complet du média
                    is_media = True
                    message = f'{media_file}'  # On n'affiche que le nom du fichier dans le message
                else:
                    is_media = False
                    media_file = None
                
                # Générer le HTML pour la bulle de message
                html_content += generate_message_bubble(sender, message, timestamp, is_media, media_file_path if is_media else None)
    
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
