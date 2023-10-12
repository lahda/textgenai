def count_words(text):
    # Supprimer les caractères de ponctuation
    text = text.replace(',', ' ').replace('.', ' ').replace('!', ' ').replace('?', ' ').replace(';', ' ').replace(':', ' ')
    # Diviser le texte en mots
    words = text.split()
    # Retourner le nombre de mots
    return len(words)
