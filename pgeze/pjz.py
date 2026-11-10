
import pygame
import pgzrun
import random
import math

WIDTH = 800
HEIGHT = 600
TITLE = "O Pedro é bobo"

campo_visao = 200

heroi = Actor("heroi")
heroi.pos = (200, 100)

moeda = Actor("moeda")
moeda.pos = (400, 300)

inimigo = Actor("inimigo")
inimigo.pos = (600, 400)

tamanho_heroi = (25, 25)
tamanho_moeda = (20, 20)
tamanho_inimigo = (30, 30)

pontos = 0
vidas = 4
contador_inimigo = 0
estado_jogo = "JOGANDO"
pontos_vitoria = 10

estado_inimigo = "PATRULHA"

pontos_patrulha = [
    (100, 100),
    (220, 100),
    (220, 120),
    (220, 220),
    (300, 220),
    (380, 220),
    (580, 220),
    (600, 280),
    (600, 320),
    (380, 320),
    (380, 400),
    (350, 430),
    (320, 450),
    (320, 500),
    (700, 500),
    (700, 300),
    (700, 100),
    (580, 100),
    (580, 130),
    (580, 270),
    (500, 300),
    (350, 300),
    (300, 300),
    (300, 380),
    (300, 430),
    (100, 430),
    (100, 500)
]

ponto_atual = 0

paredes = [
    pygame.Rect(250, 150, 300, 30),
    pygame.Rect(250, 250, 30, 150),
    pygame.Rect(400, 350, 300, 30),
    pygame.Rect(550, 150, 30, 100),
    pygame.Rect(100, 400, 200, 30)
]


def Reescale(personagem, tamanho):
    imagem = personagem._surf
    imagem_menor = pygame.transform.scale(imagem, tamanho)

    screen.surface.blit(
        imagem_menor,
        (
            int(personagem.x - tamanho[0] / 2),
            int(personagem.y - tamanho[1] / 2)
        )
    )


def hitbox(personagem, tamanho):
    return pygame.Rect(
        int(personagem.x - tamanho[0] / 2),
        int(personagem.y - tamanho[1] / 2),
        tamanho[0],
        tamanho[1]
    )


def colisaogeral(personagem, dx, dy, tamanho):
    personagem.x = personagem.x + dx

    retangulo = hitbox(personagem, tamanho)

    for parede in paredes:
        if retangulo.colliderect(parede):
            personagem.x = personagem.x - dx
            break

    personagem.y = personagem.y + dy

    retangulo = hitbox(personagem, tamanho)

    for parede in paredes:
        if retangulo.colliderect(parede):
            personagem.y = personagem.y - dy
            break

    if personagem.x - tamanho[0] / 2 < 0:
        personagem.x = tamanho[0] / 2

    if personagem.x + tamanho[0] / 2 > WIDTH:
        personagem.x = WIDTH - tamanho[0] / 2

    if personagem.y - tamanho[1] / 2 < 0:
        personagem.y = tamanho[1] / 2

    if personagem.y + tamanho[1] / 2 > HEIGHT:
        personagem.y = HEIGHT - tamanho[1] / 2


def raycasting(origem, destino, paredes):
    dx = destino[0] - origem[0]
    dy = destino[1] - origem[1]

    distancia = math.sqrt(dx ** 2 + dy ** 2)

    if distancia == 0:
        return True

    passos = max(1, int(distancia))

    for i in range(passos + 1):
        x = origem[0] + (dx / passos) * i
        y = origem[1] + (dy / passos) * i

        ponto = (int(x), int(y))

        for parede in paredes:
            if parede.collidepoint(ponto):
                return False

    return True


def randomspawn(personagem, tamanho):
    while True:
        personagem.x = random.randint(
            tamanho[0],
            WIDTH - tamanho[0]
        )

        personagem.y = random.randint(
            tamanho[1],
            HEIGHT - tamanho[1]
        )

        retangulo = hitbox(personagem, tamanho)
        colidiu = False

        for parede in paredes:
            if retangulo.colliderect(parede):
                colidiu = True
                break

        if not colidiu:
            break


def draw():
    screen.fill((255, 0, 0))

    for parede in paredes:
        pygame.draw.rect(
            screen.surface,
            (100, 100, 100),
            parede
        )

    distancia = math.sqrt(
        (inimigo.x - heroi.x) ** 2 +
        (inimigo.y - heroi.y) ** 2
    )

    pygame.draw.circle(
        screen.surface,
        (255, 255, 0),
        (int(inimigo.x), int(inimigo.y)),
        campo_visao,
        2
    )

    if distancia <= campo_visao:
        if raycasting(inimigo.pos, heroi.pos, paredes):
            pygame.draw.line(
                screen.surface,
                (0, 255, 0),
                inimigo.pos,
                heroi.pos,
                2
            )

    Reescale(heroi, tamanho_heroi)
    Reescale(moeda, tamanho_moeda)
    Reescale(inimigo, tamanho_inimigo)

    screen.draw.text(
        "Pontos: " + str(pontos),
        (10, 10),
        color="white"
    )

    screen.draw.text(
        "Vidas: " + str(vidas),
        (10, 35),
        color="white"
    )

    if estado_jogo == "VITORIA":
        screen.draw.text(
            "VOCE VENCEU!",
            center=(WIDTH // 2, HEIGHT // 2),
            fontsize=60,
            color="white"
        )

    elif estado_jogo == "DERROTA":
        screen.draw.text(
            "VOCE PERDEU!",
            center=(WIDTH // 2, HEIGHT // 2),
            fontsize=60,
            color="white"
        )


def update():
    global pontos, vidas, estado_jogo
    global contador_inimigo, estado_inimigo, ponto_atual

    if estado_jogo != "JOGANDO":
        return

    dx = 0
    dy = 0

    if keyboard.left or keyboard.a:
        dx = -3
    if keyboard.right or keyboard.d:
        dx = 3
    if keyboard.up or keyboard.w:
        dy = -3
    if keyboard.down or keyboard.s:
        dy = 3

    colisaogeral(heroi, dx, dy, tamanho_heroi)

    if hitbox(heroi, tamanho_heroi).colliderect(
        hitbox(moeda, tamanho_moeda)
    ):
        pontos = pontos + 1
        randomspawn(moeda, tamanho_moeda)

    if pontos >= pontos_vitoria:
        estado_jogo = "VITORIA"
        return

    distancia = math.sqrt(
        (inimigo.x - heroi.x) ** 2 +
        (inimigo.y - heroi.y) ** 2
    )

    if distancia <= campo_visao and raycasting(
        inimigo.pos,
        heroi.pos,
        paredes
    ):
        estado_inimigo = "PERSEGUICAO"
    else:
        estado_inimigo = "PATRULHA"

    contador_inimigo = contador_inimigo + 1

    if contador_inimigo >= 2:
        contador_inimigo = 0

        if estado_inimigo == "PERSEGUICAO":
            dx_inimigo = 0
            dy_inimigo = 0

            if inimigo.x < heroi.x:
                dx_inimigo = 3
            elif inimigo.x > heroi.x:
                dx_inimigo = -3

            if inimigo.y < heroi.y:
                dy_inimigo = 3
            elif inimigo.y > heroi.y:
                dy_inimigo = -3

            colisaogeral(
                inimigo,
                dx_inimigo,
                dy_inimigo,
                tamanho_inimigo
            )

        else:
            alvo_x, alvo_y = pontos_patrulha[ponto_atual]

            dx_inimigo = 0
            dy_inimigo = 0

            if inimigo.x < alvo_x:
                dx_inimigo = 3
            elif inimigo.x > alvo_x:
                dx_inimigo = -3

            if inimigo.y < alvo_y:
                dy_inimigo = 3
            elif inimigo.y > alvo_y:
                dy_inimigo = -3

            colisaogeral(
                inimigo,
                dx_inimigo,
                dy_inimigo,
                tamanho_inimigo
            )

            if abs(inimigo.x - alvo_x) < 4 and abs(inimigo.y - alvo_y) < 4:
                ponto_atual = (ponto_atual + 1) % len(pontos_patrulha)

    if hitbox(heroi, tamanho_heroi).colliderect(
        hitbox(inimigo, tamanho_inimigo)
    ):
        vidas = vidas - 1
        pontos = max(0, pontos - 1)

        randomspawn(inimigo, tamanho_inimigo)

        if vidas <= 0:
            estado_jogo = "DERROTA"


def reiniciar_jogo():
    global pontos, vidas, contador_inimigo
    global estado_jogo, estado_inimigo, ponto_atual

    pontos = 0
    vidas = 4
    contador_inimigo = 0
    estado_jogo = "JOGANDO"
    estado_inimigo = "PATRULHA"
    ponto_atual = 0

    heroi.pos = (200, 100)
    inimigo.pos = (600, 400)

    randomspawn(moeda, tamanho_moeda)


def on_key_down(key):
    if key == keys.SPACE and estado_jogo != "JOGANDO":
        reiniciar_jogo()


pgzrun.go()
