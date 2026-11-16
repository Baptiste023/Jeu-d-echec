import pygame
from Plateau import damier,init_plateau, dessiner_piece
from Constante import TAILLE_CELLUE, TAILLE_TABLEAU
from Assets import charger_assets
from Regles import regle_capture_et_case_vide,regle_pion, regle_tour, regle_fou, regle_dame, regle_cavalier, regle_roi, regle_promotion

pygame.init()
screen = pygame.display.set_mode((TAILLE_TABLEAU*TAILLE_CELLUE, TAILLE_TABLEAU*TAILLE_CELLUE))
pygame.display.set_caption('Jeu d échecs')
assets=charger_assets()
plateau=init_plateau()

#print(plateau)
#print(regle_capture_et_case_vide(plateau,(7,0),(6,0))) // capture de piece de meme couleur
#print(regle_capture_et_case_vide(plateau,(4,4),(3,3))) // case vide
#print(regle_capture_et_case_vide(plateau,(6,0),(4,0))) // deplacement valide
REGLES = {"pion": regle_pion, "tour": regle_tour,"fou": regle_fou,"dame": regle_dame,"cavalier": regle_cavalier,"roi": regle_roi}
conetnu_case_cliquer=None
case_clique=None
running = True
Tour="blanc"
damier(screen)
dessiner_piece(plateau,screen,assets)
pygame.display.flip()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x,y=event.pos
            collone=x//TAILLE_CELLUE
            ligne=y//TAILLE_CELLUE
            if case_clique==None:
                if not plateau[ligne][collone]==None  and plateau[ligne][collone].split("_")[1] == Tour:
                    case_clique = (ligne, collone)
                    conetnu_case_cliquer=plateau[ligne][collone]
                    print("contenu : ", conetnu_case_cliquer)
                    print("case depart : ", case_clique)
            else:
                case_arriver=(ligne, collone)
                case_arriver = (ligne, collone)
                print("case arriver : ", case_arriver)

                type_piece = plateau[case_clique[0]][case_clique[1]].split("_")[0]
                regle_piece = REGLES.get(type_piece)

                if regle_capture_et_case_vide(plateau, case_clique,case_arriver) and regle_piece is not None and regle_piece(plateau,case_clique,case_arriver):
                    promotion = regle_promotion(plateau, case_clique, case_arriver)
                    if promotion:
                        print(promotion)
                    plateau[ligne][collone] = plateau[case_clique[0]][case_clique[1]]
                    plateau[case_clique[0]][case_clique[1]] = None
                    if Tour == "blanc":
                        Tour = "noir"
                    else:
                        Tour = "blanc"
                case_clique = None



    damier(screen)
    dessiner_piece(plateau, screen, assets)
    pygame.display.flip()





