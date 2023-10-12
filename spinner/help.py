def count_words(text):
    # Supprimer les caractères de ponctuation
    text = text.replace(',', ' ').replace('.', ' ').replace('!', ' ').replace('?', ' ').replace(';', ' ').replace(':', ' ')
    # Diviser le texte en mots
    words = text.split()
    # Retourner le nombre de mots
    return len(words)


import html

def convert_html_entities(text):
    decoded_text = html.unescape(text)
    return decoded_text