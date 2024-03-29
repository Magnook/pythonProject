import pygame


class Avatar(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = pygame.image.load("data/avatar.png")
        self.image = pygame.transform.scale(self.image, [100, 100])
        self.rect = pygame.Rect(100, 100, 100, 100)

    def update(self, *args, **kwargs):
        # Pegando a tecla selecionada do Teclado
        keys = pygame.key.get_pressed()
        # Teclas de Movimento Horizontal
        if keys[pygame.K_a]:
            self.rect.x -= 1
        elif keys[pygame.K_d]:
            self.rect.x += 1
