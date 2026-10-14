
import pygame
import pgzrun
import random
import math

WIDTH = 800
HEIGHT = 600
TITLE = "O Pedro é bobo"

heroi = Actor("heroi")
heroi.pos = (200, 100)

moeda = Actor("moeda")
moeda.pos = (400, 300)

inimigo = Actor("inimigo")
inimigo.pos = (600, 400)

pontos = 0
vidas = 4
contador_inimigo = 0
estado_jogo = "JOGANDO"
pontos_vitoria = 10


estado_inimigo = "PATRULHA"


pontos_patrulha = [
    (100, 100),
    (700, 100),
    (700, 500),
    (100, 500)
]

ponto_atual = 0


def draw():
    screen.fill((255, 0, 0))

    heroi.draw()
    moeda.draw()


    screen.draw.circle(inimigo.pos, 100, "yellow", 2)

    inimigo.draw()

    screen.draw.text(
        f"pontos: {pontos}",
        (20, 20),
        fontsize=36,
        color="white"
    )

    screen.draw.text(
        f"vidas: {vidas}",
        (20, 60),
        fontsize=36,
        color="white"
    )

    if estado_jogo == "VITORIA":
        screen.draw.filled_rect(
            Rect((0, 0), (WIDTH, HEIGHT)),
            (0, 0, 255)
        )

        screen.draw.text(
            "JÁ BORA!",
            center=(WIDTH // 2, 220),
            fontsize=70,
            color="white"
        )

        screen.draw.text(
            "VIIIIIIIIIIIIIIIIIIIIIIIIILLLLLLAAAAAAAAAAA",
            center=(WIDTH // 2, 300),
            fontsize=25,
            color="white"
        )

        screen.draw.text(
            "perta espaço ai so",
            center=(WIDTH // 2, 400),
            fontsize=30,
            color="white"
        )

    if estado_jogo == "PERDIDO":
        screen.draw.filled_rect(
            Rect((0, 0), (WIDTH, HEIGHT)),
            (0, 0, 0)
        )

        screen.draw.text(
            "PERDESTE!",
            center=(WIDTH // 2, 220),
            fontsize=70,
            color="red"
        )

        screen.draw.text(
            "Tens o que é necessário pra continuar?",
            center=(WIDTH // 2, 300),
            fontsize=30,
            color="white"
        )

        screen.draw.text(
            "perta ispaço ai ze",
            center=(WIDTH // 2, 380),
            fontsize=30,
            color="white"
        )


def update():
    global pontos
    global vidas
    global contador_inimigo
    global estado_jogo
    global estado_inimigo
    global ponto_atual

    if estado_jogo == "PERDIDO":
        if keyboard.space:
            reiniciar_jogo()
        return

    if estado_jogo == "VITORIA":
        if keyboard.space:
            reiniciar_jogo()
        return

    if keyboard.right:
        heroi.x += 1
    if keyboard.left:
        heroi.x -= 1
    if keyboard.up:
        heroi.y -= 1
    if keyboard.down:
        heroi.y += 1

    if keyboard.d:
        heroi.x += 1
    if keyboard.a:
        heroi.x -= 1
    if keyboard.w:
        heroi.y -= 1
    if keyboard.s:
        heroi.y += 1

    if heroi.colliderect(moeda):
        pontos += 1
        moeda.x = random.randint(50, WIDTH - 50)
        moeda.y = random.randint(50, HEIGHT - 50)

    if pontos >= pontos_vitoria:
        estado_jogo = "VITORIA"
        return

    
    distancia = math.sqrt(
        (inimigo.x - heroi.x) ** 2 +
        (inimigo.y - heroi.y) ** 2
    )

    
    if distancia <= 100:
        estado_inimigo = "PERSEGUICAO"
    else:
        estado_inimigo = "PATRULHA"

    contador_inimigo += 1

    if contador_inimigo >= 2:
        contador_inimigo = 0

        if estado_inimigo == "PATRULHA":
            alvo_x = pontos_patrulha[ponto_atual][0]
            alvo_y = pontos_patrulha[ponto_atual][1]

            if inimigo.x > alvo_x:
                inimigo.x -= 1
            if inimigo.x < alvo_x:
                inimigo.x += 1
            if inimigo.y > alvo_y:
                inimigo.y -= 1
            if inimigo.y < alvo_y:
                inimigo.y += 1

            
            if abs(inimigo.x - alvo_x) <= 1 and abs(inimigo.y - alvo_y) <= 1:
                ponto_atual += 1

                if ponto_atual >= 4:
                    ponto_atual = 0

        if estado_inimigo == "PERSEGUICAO":
            if inimigo.x > heroi.x:
                inimigo.x -= 1
            if inimigo.x < heroi.x:
                inimigo.x += 1
            if inimigo.y > heroi.y:
                inimigo.y -= 1
            if inimigo.y < heroi.y:
                inimigo.y += 1

        if inimigo.colliderect(heroi):
            vidas -= 1
            pontos -= 1

            inimigo.x = random.randint(50, WIDTH - 50)
            inimigo.y = random.randint(50, HEIGHT - 50)

            estado_inimigo = "PATRULHA"

            if pontos < 0:
                pontos = 0

            if vidas <= 0:
                vidas = 0
                estado_jogo = "PERDIDO"


def reiniciar_jogo():
    global pontos
    global vidas
    global estado_jogo
    global contador_inimigo
    global estado_inimigo
    global ponto_atual

    pontos = 0
    vidas = 4
    contador_inimigo = 0

    heroi.pos = (100, 100)
    moeda.pos = (400, 300)
    inimigo.pos = (650, 450)

    estado_inimigo = "PATRULHA"
    ponto_atual = 0
    estado_jogo = "JOGANDO"


pgzrun.go()
