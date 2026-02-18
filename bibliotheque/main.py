bibliotheque = [
    {
        "titre": "1984",
        "auteur": "George Orwell",                              
        "annee": 1949,
        "disponible": True
    },
    {
        "titre": "L'Étranger",
        "auteur": "Albert Camus",
        "annee": 1942,
        "disponible": False
    }
]

def addBook(bibliotheque) :
    title =  input("entrez un titre pour votre livre :")
    author = input("entrez l'auteur de votre livre : ")
    year =  int(input("entrez l'annee de votre livre : "))
    avaible = input("ce livre est il disponible? oui ou non")

    isavaible = False
    if avaible == "oui":
        isavaible = True

    bibliotheque.append({"titre":title,"auteur":author,"annee":year,"disponible":isavaible ,})

    return "votre livre a bien ete ajouter"

def seachbook(bibliotheque, recherche) :
    i = 0
    while(i < len(bibliotheque) and bibliotheque[i]["titre"].lower() != recherche.lower() ) :
        i += 1
    return i

def delBOOK (bibliotheque,ilivre) :
    del bibliotheque[ilivre]

    return "votre livre a bien ete supprimer"



def main():
    while True :
        choice = int(input("choisir une action :\n " \
                            "1. ajouter un livre\n" \
                            "2. rechercher un livre\n" \
                            "3. supprimer un livre\n" \
                            "4. afficher la bibliotheque\n" \
                            "5. fermer\n" \
                            "entrez : "
        ))

        if choice == 1 :
            message = addBook(bibliotheque)
            print(message)
        elif choice == 2 :
            title = input("entrez le titre du libre que vous souhaitez rechercher")
            ilivre = seachbook(bibliotheque,title)
            if ilivre == len(bibliotheque):
                print("votre livre n'hesite pas")
            else:
                print(f"{bibliotheque[ilivre]}")
        elif choice == 3 : 
            livre = input("entrez le titre du livre que vous souhaitez supprimer")
            isearch = seachbook(bibliotheque, livre)
            if isearch == len(bibliotheque):
                print("votre livre n'est pas dans la bibliotheque")
            else:
                message = delBOOK(bibliotheque,isearch)
                print(message)
        elif choice == 4 :
            for livre in bibliotheque:
                print(livre)
        else :
            break

main()  