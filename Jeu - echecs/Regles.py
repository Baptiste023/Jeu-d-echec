


def regle_capture_et_case_vide(plateau,case_depart,case_arrive):

    ligne_depart,colonne_depart=case_depart
    ligne_arrive,colonne_arrive=case_arrive

    if plateau[ligne_depart][colonne_depart]==None:
       return False

    piece_et_couleur_selectionner=plateau[ligne_depart][colonne_depart]
    piece_et_couleur_arriver = plateau[ligne_arrive][colonne_arrive]

    piece_selectionner, couleur_piece_selectionner = piece_et_couleur_selectionner.split("_")

    if piece_et_couleur_arriver != None:
        piece_presente_a_l_arrive, couleur_presente_a_l_arrive= piece_et_couleur_arriver.split("_")

        if couleur_presente_a_l_arrive == couleur_piece_selectionner:
            return False

    return True

def regle_pion(plateau,case_depart,case_arrive):
    ligne_depart,colonne_depart=case_depart
    ligne_arrive,colonne_arrive=case_arrive
    piece_et_couleur__selectionner = plateau[ligne_depart][colonne_depart]
    piece_selectionner, couleur_piece_selectionner = piece_et_couleur__selectionner.split("_")

    if couleur_piece_selectionner=="blanc":
        direction=1
        case_init=6
    else:
        direction=-1
        case_init=1

    if piece_selectionner=="pion":
        if ligne_depart - ligne_arrive == direction  and colonne_depart == colonne_arrive and plateau[ligne_arrive][colonne_arrive]==None:
            return True
        if ligne_depart - ligne_arrive == 2*direction  and colonne_depart == colonne_arrive and plateau[ligne_arrive][colonne_arrive]==None and ligne_depart == case_init and plateau[ligne_depart-direction][colonne_depart]==None:
            return True

        if ligne_depart - ligne_arrive == direction and abs(colonne_depart - colonne_arrive) == 1 and plateau[ligne_arrive][colonne_arrive] != None:
            return True
    else:
        return False

    return False

def regle_tour(plateau,case_depart,case_arrive):
    ligne_depart,colonne_depart=case_depart
    ligne_arrive,colonne_arrive=case_arrive

    if plateau[ligne_depart][colonne_depart]==None:
        return False

    if ligne_depart != ligne_arrive and colonne_depart == colonne_arrive :
        for i in range(min(ligne_depart,ligne_arrive)+1,max(ligne_depart,ligne_arrive)):
            if plateau[i][colonne_depart]!=None:
                return False
        return True

    if ligne_depart == ligne_arrive and colonne_depart != colonne_arrive :
        for i in range(min(colonne_depart,colonne_arrive)+1,max(colonne_depart,colonne_arrive)):
            if plateau[ligne_depart][i]!=None:
                return False
        return True

    return False

def regle_fou(plateau,case_depart,case_arrive):
    ligne_depart,colonne_depart=case_depart
    ligne_arrive,colonne_arrive=case_arrive

    if plateau[ligne_depart][colonne_depart]==None:
        return False

    if ligne_depart<ligne_arrive:
        pas_ligne=1
    else:
        pas_ligne=-1

    if colonne_depart < colonne_arrive:
        pas_colonne=1
    else:
        pas_colonne=-1

    if abs(ligne_depart-ligne_arrive)==abs(colonne_depart-colonne_arrive) and ligne_depart-ligne_arrive!=0:
        for i in range(1,abs(ligne_depart-ligne_arrive)):
            if plateau[ligne_depart+i*pas_ligne][colonne_depart+i*pas_colonne]!=None:
                return False
        return True
    return False

def regle_dame(plateau, case_depart, case_arrive):
    return regle_tour(plateau, case_depart, case_arrive) or regle_fou(plateau, case_depart, case_arrive)


def regle_cavalier(plateau, case_depart, case_arrive):
    ligne_depart, colonne_depart = case_depart
    ligne_arrive, colonne_arrive = case_arrive

    if plateau[ligne_depart][colonne_depart] == None:
        return False

    ecart_ligne = abs(ligne_depart - ligne_arrive)
    ecart_colonne = abs(colonne_depart - colonne_arrive)

    if (ecart_ligne==1 and ecart_colonne==2 ) or (ecart_ligne==2 and ecart_colonne==1):
        return True
    return False

def regle_roi(plateau, case_depart, case_arrive):
    ligne_depart, colonne_depart = case_depart
    ligne_arrive, colonne_arrive = case_arrive

    if plateau[ligne_depart][colonne_depart] == None:
        return False

    ecart_ligne = abs(ligne_depart - ligne_arrive)
    ecart_colonne = abs(colonne_depart - colonne_arrive)

    if (ecart_ligne==0 and ecart_colonne==1) or (ecart_ligne==1 and ecart_colonne==0) or (ecart_ligne==1 and ecart_colonne==1):
        return True
    return False

def regle_promotion (plateau,case_depart, case_arrive):

    ligne_depart, colonne_depart = case_depart
    ligne_arrive, colonne_arrive = case_arrive

    if plateau[ligne_depart][colonne_depart] == None:
        return False

    piece_et_couleur_selectionner = plateau[ligne_depart][colonne_depart]
    piece_selectionner = piece_et_couleur_selectionner.split("_")[0]

    if piece_selectionner=="pion" and (ligne_arrive ==0 or ligne_arrive==7 ):
        return True
    return False

