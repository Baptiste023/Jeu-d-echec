import pygame
from Constante import TAILLE_CELLUE,TAILLE_TABLEAU

def damier(screen):
    for i in range(TAILLE_TABLEAU):
        for j in range(TAILLE_TABLEAU):
            if (i+j) % 2 != 0:
                pygame.draw.rect(screen,(0,0,0),(i*TAILLE_CELLUE,j*TAILLE_CELLUE,TAILLE_CELLUE,TAILLE_CELLUE))
            else :
                pygame.draw.rect(screen, (255,255,255),(i * TAILLE_CELLUE, j * TAILLE_CELLUE, TAILLE_CELLUE, TAILLE_CELLUE))

def init_plateau():
    ordre_piece=["tour","cavalier","fou","dame","roi","fou","cavalier","tour"]
    piece_noir=[]
    piece_blanc=[]
    pion_noir = ["pion_noir"] * 8
    pion_blanc = ["pion_blanc"] * 8

    for piece in ordre_piece:
        piece_noir.append(piece+"_noir")

    for piece in ordre_piece:
        piece_blanc.append(piece+"_blanc")

    plateau=[piece_noir,
             pion_noir,
             [None] * 8,
             [None] * 8,
             [None] * 8,
             [None] * 8,
             pion_blanc,
             piece_blanc
             ]
    return plateau

def dessiner_piece(plateau,screen,assets):

    for ligne in range(TAILLE_TABLEAU):
        for collone in range(TAILLE_TABLEAU):
            if plateau[ligne][collone]!= None :
                screen.blit(assets[plateau[ligne][collone]],(collone*TAILLE_CELLUE,ligne*TAILLE_CELLUE))


