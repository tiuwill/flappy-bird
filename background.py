import pygame


class Background(pygame.sprite.Sprite):
    
    def __init__(self):
        super().__init__()

        self.image = pygame.image.load("assets/sprites/background-day.png").convert_alpha()
        self.rect = self.image.get_rect()