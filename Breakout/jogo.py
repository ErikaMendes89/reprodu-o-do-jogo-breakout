import pygame
import sys

# Inicializando o pygame
pygame.init()

# Definindo valores de altura, largura, cores
WIDTH = 400
HEIGHT = 400
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

# Definindo a posição e tamanho do botão
button_rect = pygame.Rect(150, 150, 100, 50)

# Definindo uma cor para o botão
button_color = (0, 255, 0)

# CRIANDO A TELA
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Breakout")

# Criando raquete
raquete = pygame.Rect(200, 380, 100, 20)

# Criando a bola
bola = pygame.Rect(200, 200, 20, 20)
bola_speed = [2, 3]

# Criando as caixas
caixas = []
for row in range(2):
    for col in range(8):
        caixa = pygame.Rect(col * 50, 100 + row * 50, 50, 50)
        if (row + col) % 2 == 0:
            caixa_color = RED
        else:
            caixa_color = BLACK
        caixas.append((caixa, caixa_color))
# Variável de pontuação
pontuacao = 0

# Definindo uma variável para controlar se o jogo está rodando
running = False
# Variável de controle para alternar as cores
color_switch = False

clock = pygame.time.Clock()

while True:
    screen.fill(WHITE)

    # Desenhar as caixas
    for caixa, cor in caixas:
        pygame.draw.rect(screen, cor, caixa)
    # Exibir pontuação
    font = pygame.font.Font(None, 36)
    score_text = font.render("Pontuação: " + str(pontuacao), True, (0, 0, 0))
    screen.blit(score_text, (10, 10))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # Verificar teclas pressionadas
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                raquete.x -= 5  # Mover a raquete para a esquerda
            if event.key == pygame.K_RIGHT:
                raquete.x += 5  # Mover a raquete para a direita

        # Verificar se o mouse foi clicado
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            # Verificar se o clique foi dentro do botão
            if button_rect.collidepoint(event.pos):
                running = True  # Iniciar o jogo

    if running:
        # Movimentar a bola
        bola.x += bola_speed[0]
        bola.y += bola_speed[1]

        # Colisão com as bordas
        if bola.left <= 0 or bola.right >= WIDTH:
            bola_speed[0] = -bola_speed[0]
        if bola.top <= 0:
            bola_speed[1] = -bola_speed[1]

        # Colisão com a raquete
        if bola.colliderect(raquete):
            bola_speed[1] = -bola_speed[1]

        # Colisão com as caixas
        for caixa, _ in caixas[:]:
            if bola.colliderect(caixa):
                caixas.remove((caixa, _))
                bola_speed[1] = -bola_speed[1]
                pontuacao += 1

        # Se o jogador perder
        if bola.bottom >= HEIGHT:
            font = pygame.font.Font(None, 50)
            lose_text = font.render("Você Perdeu!!", True, (0, 0, 0))
            screen.blit(lose_text, (50, 200))
            running = False  # Parar o jogo após perder
    else:
        # Desenhar o botão e o texto "Iniciar Jogo"
        pygame.draw.rect(screen, button_color, button_rect)
        font = pygame.font.Font(None, 36)
        text = font.render("Iniciar Jogo", True, (0, 0, 0))
        text_rect = text.get_rect(center=button_rect.center)
        screen.blit(text, text_rect)

    # Desenhar a raquete e a bola
    pygame.draw.rect(screen, BLUE, raquete)
    pygame.draw.ellipse(screen, RED, bola)

    # Atualizar a tela
    pygame.display.flip()

    clock.tick(60)
