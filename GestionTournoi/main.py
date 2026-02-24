import random
tabPlayers =[] 

def addplayer():
    id = len(tabPlayers) + 1
    name = input("entrez votre nom").lower()
    score = 0
    victoire = 0
    defaite = 0
    match_joues = 0

    checkDoubleName = searchPlayer(tabPlayers,name)

    if checkDoubleName == len(tabPlayers) :
        tabPlayers.append({"id":id,"name":name,"score":score,"victoire":victoire,"defaite":defaite,"match_joues":match_joues})
        return "le joueur a bien été ajouter"
    else :
        return "ce joueur existe deja veuillez choisir un autre nom"


def searchPlayer (tabPlayers, recherche) :
    iRecherche = 0

    while iRecherche < len(tabPlayers) and tabPlayers[iRecherche]["name"] != recherche:
        iRecherche += 1
    return iRecherche

def findplayers (tabPlayers) : 
    p1 = random.choice(tabPlayers)
    p2 = random.choice(tabPlayers)

    while p1["name"] == p2["name"]:
        p2 = random.choice(tabPlayers)
    
    return p1,p2

def findWinner(p1,p2) :
    winner = random.choice([p1,p2])

    updateWinner(winner)

    if winner["name"] != p1["name"] :
        lostPlayer(p1)
    else:
        lostPlayer(p2)
    
    return f"Felicitation a {winner["name"]} pour sa victoire"

    
def updateWinner (winner) :
    winner["score"] += 5
    winner["victoire"] += 1
    winner["match_joues"] += 1

def lostPlayer (loser) : 
    loser["defaite"] += 1
    loser["match_joues"] += 1

def showplayer (tabPlayers,iplayer) :
    return f"nom : {tabPlayers[iplayer]["name"]}\n \
             score : {tabPlayers[iplayer]["score"]}\n \
             victoire : {tabPlayers[iplayer]["victoire"]}\n \
             defaite : {tabPlayers[iplayer]["defaite"]}\n \
             match_joues : {tabPlayers[iplayer]["match_joues"]}\n"

def tri (tabPlayers) : 
    for i in range (len(tabPlayers)-1) :
        value = tabPlayers[i]
        for j in range(len(tabPlayers)) :
            if value["score"] < tabPlayers[i +1]["score"] : 
                tabPlayers[i] = tabPlayers[j]
                tabPlayers[j] = value

def showAll (tabPlayers) :
    tri(tabPlayers)
    result = []
    for iplayer in range(len(tabPlayers)) :
        result.append(  f"\n\
             id : {tabPlayers[iplayer]["id"]} \n \
             nom : {tabPlayers[iplayer]["name"]}\n \
             score : {tabPlayers[iplayer]["score"]}\n \
             victoire : {tabPlayers[iplayer]["victoire"]}\n \
             defaite : {tabPlayers[iplayer]["defaite"]}\n \
             match_joues : {tabPlayers[iplayer]["match_joues"]}\n")
    return result

def main ():
    while True : 
        try :
            choice = int(input("pour lancer le jeu choisir une action : \n" \
                            "1. lancer le jeu avec les donnés interne\n" \
                            "2. entrez votre donnés de jeu\n" \
                            "3. voir vos stats\n" \
                            "4. voir le classement des meilleurs de joueur\n" \
                            "5. quitter\n" \
                            "ecrivez : "
                       ))
            
            if choice == 1 :
                if len(tabPlayers)<1:
                    print("nous n'avons pas assez de donnés interne que pour vous lancer le jeu") 
                else :
                    p1,p2 = findplayers(tabPlayers)
                    winner = findWinner(p1,p2)
                    print(winner)
            elif choice == 2 :
                p1 =  addplayer()
                p2 = addplayer()
                winner = findWinner(p1,p2)
                print(winner)
            elif choice == 3 :
                nameplayer = input("entrez votre nom").lower()
                iplayer = searchPlayer(tabPlayers,nameplayer)
                if iplayer == len(tabPlayers) :
                    print("ce joueur n'hesite pas dans nos donnés")
                else :
                    print (showplayer)
            elif choice == 4 :
                result = (showAll(tabPlayers))
                for iplayer in range(len(result)) :
                    print(  f"\n\
                        id : {result[iplayer]["id"]} \n \
                        nom : {result[iplayer]["name"]}\n \
                        score : {result[iplayer]["score"]}\n \
                        victoire : {result[iplayer]["victoire"]}\n \
                        defaite : {result[iplayer]["defaite"]}\n \
                        match_joues : {result[iplayer]["match_joues"]}\n")
            elif choice == 5 :
                print("merci pour cette parti")
            break

        except ValueError :
            print("veuillez entrez des valeurs correct")

main()