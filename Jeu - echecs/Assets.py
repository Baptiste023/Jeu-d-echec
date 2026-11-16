import os
import pygame

from Constante import TAILLE_CELLUE

def charger_assets():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    assets_dir = os.path.join(current_dir,"assets")

    assets={}

    image_pion_noir= pygame.image.load(os.path.join(assets_dir, "pion_noir.png")).convert_alpha()
    assets["pion_noir"]=pygame.transform.scale(image_pion_noir, (TAILLE_CELLUE, TAILLE_CELLUE))

    image_pion_blanc=pygame.image.load(os.path.join(assets_dir, "pion_blanc.png")).convert_alpha()
    assets["pion_blanc"]=pygame.transform.scale(image_pion_blanc,(TAILLE_CELLUE,TAILLE_CELLUE))

    image_tour_noir= pygame.image.load(os.path.join(assets_dir, "tour_noir.png")).convert_alpha()
    assets["tour_noir"]=pygame.transform.scale(image_tour_noir,(TAILLE_CELLUE,TAILLE_CELLUE))

    image_tour_blanc = pygame.image.load(os.path.join(assets_dir, "tour_blanc.png")).convert_alpha()
    assets["tour_blanc"] = pygame.transform.scale(image_tour_blanc, (TAILLE_CELLUE, TAILLE_CELLUE))

    image_cavalier_noir= pygame.image.load(os.path.join(assets_dir, "cavalier_noir.png")).convert_alpha()
    assets["cavalier_noir"] = pygame.transform.scale(image_cavalier_noir, (TAILLE_CELLUE, TAILLE_CELLUE))

    image_cavalier_blanc = pygame.image.load(os.path.join(assets_dir, "cavalier_blanc.png")).convert_alpha()
    assets["cavalier_blanc"] = pygame.transform.scale(image_cavalier_blanc, (TAILLE_CELLUE, TAILLE_CELLUE))

    image_fou_noir= pygame.image.load(os.path.join(assets_dir, "fou_noir.png")).convert_alpha()
    assets["fou_noir"]=pygame.transform.scale(image_fou_noir, (TAILLE_CELLUE, TAILLE_CELLUE))

    image_fou_blanc=pygame.image.load(os.path.join(assets_dir, "fou_blanc.png")).convert_alpha()
    assets["fou_blanc"]=pygame.transform.scale(image_fou_blanc, (TAILLE_CELLUE, TAILLE_CELLUE))

    image_dame_blanc= pygame.image.load(os.path.join(assets_dir, "dame_blanc.png")).convert_alpha()
    assets["dame_blanc"]=pygame.transform.scale(image_dame_blanc, (TAILLE_CELLUE, TAILLE_CELLUE))

    image_dame_noir= pygame.image.load(os.path.join(assets_dir, "dame_noir.png")).convert_alpha()
    assets["dame_noir"]=pygame.transform.scale(image_dame_noir, (TAILLE_CELLUE, TAILLE_CELLUE))

    image_roi_noir= pygame.image.load(os.path.join(assets_dir, "roi_noir.png")).convert_alpha()
    assets["roi_noir"]=pygame.transform.scale(image_roi_noir, (TAILLE_CELLUE, TAILLE_CELLUE))

    image_roi_blanc=pygame.image.load(os.path.join(assets_dir, "roi_blanc.png")).convert_alpha()
    assets["roi_blanc"]=pygame.transform.scale(image_roi_blanc, (TAILLE_CELLUE, TAILLE_CELLUE))

    return assets