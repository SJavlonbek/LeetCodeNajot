def capitalizeTitle(title):
    words = title.split()  
    capitalized_words = []

    for word in words:
        if len(word) > 2:
            capitalized_words.append(word.capitalize())  
        else:
            capitalized_words.append(word.lower()) 

    return ' '.join(capitalized_words)