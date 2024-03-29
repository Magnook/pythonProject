import pygame


class Enemy(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = pygame.image.load("data/enemy.png")
        self.image = pygame.transform.scale(self.image, [100, 100])
        self.rect = pygame.Rect(100, 100, 100, 100)