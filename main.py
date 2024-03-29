import pygame
from avatar import Avatar
from enemy import Enemy
# Inicializando o PYGAME e a Janela
pygame.init()

# Fazendo a Janela se manter me Loop pra não fechar sozinha
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
if __name__ == "__main__":
    # Mantendo a Janela aberta enquanto não apertar no Input pra fechar a Aba
    while gameLoop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameLoop = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    hit.play()

        # Draw
        display.fill([46, 46, 46])

        objectGroup.update()
        objectGroup.draw(display)

        pygame.display.update()
