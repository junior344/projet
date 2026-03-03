# Matrice avec les lettres de l'alphabet et les chiffres
# Première ligne : lettres a-z et chiffres 0-9
# Deuxième ligne : zéros correspondants

tabLetter = [
    ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
     'à','á','â','ä','ç','è','é','ê','ë','ì','í','î','ï','ñ','ò','ó','ô','ö','ù','ú','û','ü','ý','ÿ',
     '0','1','2','3','4','5','6','7','8','9'],
    [0] * 49 
]

def load_file():
    """
        charge le fichier directement du repertoire courant
    """
    fichier = open('texte.txt','r')
    texte = fichier.read()

    return list(texte)
    

def count_letter(tabLetter):
    """compte le nombre de fois une lettre reviens dans un texte fourni dans le fichier charger dans la fonction load_file
        input:
            tabLetter (list) : matrice reprenant tout les lettres et les chiffres
        output:
             tabLetter (list) : la meme matrice completer par le nombre de fois que les lettres reviennent
    """
    texte = load_file()

    for i in range(len(texte)) :
       letter = texte[i]
       for j in range(len(tabLetter[0])) :
           if letter == tabLetter[0][j] :
               tabLetter[1][j] += 1
               break
    
    return tabLetter


def main():

    letters = count_letter(tabLetter)

    for i  in range(len(letters[1])): 
        if letters[1][i] != 0 :
            print(f"{letters[0][i]} = {letters[1][i]}")


main()




