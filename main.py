import pygame
from avatar import Avatar
from enemy import Enemy
# Inicializando o PYGAME e a Janela
pygame.init()

display = pygame.display.set_mode([1280, 720])
pygame.display.set_caption("Meu Jogo")

# Objetos

objectGroup = pygame.sprite.Group()

avatar = Avatar(objectGroup)
enemy = Enemy(objectGroup)
enemy.rect.center = [200, 400]


# Music
pygame.mixer.music.load("data/music.wav")
pygame.mixer.music.play(-1)
# Sounds
hit = pygame.mixer.Sound("data/hit.flac")


# Base da aplicação
gameLoop = True
clock = pygame.time.Clock()
if __name__ == "__main__":
    clock.tick(60)
    while gameLoop:
        # Mantendo a Janela aberta enquanto não apertar no Input pra fechar a Aba
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameLoop = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    hit.play()

        # Update Logic
        objectGroup.update()

        # Draw
        display.fill([46, 46, 46])
        objectGroup.draw(display)

        pygame.display.update()
