ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def chiffre_cesar_carac(car, k):
    
    # on recupere la position du caractere passer en parametre
    i = ALPHABET.index(car)

    # on 
    j = (i+k)%26

    # on recupere l'élément à l'indice j
    op = ALPHABET[j]
    return op  # on retourne la valeur

# aff = chiffre_cesar_carac("E", 3)
# print(aff)

def chiffre_cesar_phrase(phrase, k):

    n = len(phrase)
    phrase_chiffre = ""

    for j in range(n):
        maj = phrase[j]
        if phrase[j] == str.upper(maj):
            phrase_chiffre = phrase_chiffre + chiffre_cesar_carac(phrase[j], k)
        else:
            phrase_chiffre = phrase_chiffre + phrase[j]
            j + 1

        return phrase_chiffre

p = 'ENIGMA'
b = chiffre_cesar_phrase(p, 4)

print(b)