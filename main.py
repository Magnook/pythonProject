import pygame

# Inicializando o PYGAME e a Janela

pygame.init()

# Fazendo a Janela se manter me Loop pra não fechar sozinha
display = pygame.display.set_mode([1280, 720])
pygame.display.set_caption("Meu Jogo")

# Agrupando os Sprites
drawGroup = pygame.sprite.Group()

# Importando a imagem do Avatar e adicionando ao Grupo de Sprites
avatar = pygame.sprite.Sprite(drawGroup)
avatar.image = pygame.image.load("data/avatar.png")
avatar.image = pygame.transform.scale(avatar.image, [100, 100])
avatar.rect = pygame.Rect(100, 100, 100, 100)


# Music
pygame.mixer.music.load("data/music.wav")
pygame.mixer.music.play(-1)

# Base da aplicação
gameLoop = True
if __name__ == "__main__":
    # Mantendo a Janela aberta enquanto não apertar no Input pra fechar a Aba
    while gameLoop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameLoop = False
        # Pegando a tecla selecionada do Teclado
        keys = pygame.key.get_pressed()

        # Teclas de Movimento Horizontal
        if keys[pygame.K_a]:
            avatar.rect.x -= 1
        elif keys[pygame.K_d]:
            avatar.rect.x += 1

        # Draw
        display.fill([46, 46, 46])

                        #     x,  y, width, heigth
        player = pygame.Rect(50, 50, 100, 100)
        pygame.draw.rect(display, [255, 255, 255, 255], player)

        drawGroup.draw(display)

        pygame.display.update()
