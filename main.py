from pygame import *
import sys

init()

cachorro_imagem = image.load('cachorro.png')
cachorro_imagem = transform.scale(cachorro_imagem, (500,500))

cachorro_font = font.Font('Somelist.ttf', 100)

mixer.music.load('batman_1966.mp3')
mixer.music.play(-1)

window = display.set_mode((1280,720))

window.fill((152, 209, 250))

while True:
    for ev in event.get():
        if ev.type == QUIT:
            quit()
            sys.exit()

    #Desenhar a partir daqui

    #Desenhar primitivas geometricas
    draw.rect(window, (255,0,0), (200, 300, 100, 50))
    draw.circle(window, (255,255,0), (500,600), 200)
    draw.polygon(window, (205,124,201), ((200,300), (250,150), (300,300)))
    draw.line(window, (255,0,255),(100, 100),(200,200), 5)

    #Desenhar imagens 
    window.blit(cachorro_imagem, (200,0))

    # Desenhar texto
    cachorro_text = cachorro_font.render('afqefnqoiof', True, (0, 0, 0))
    window.blit(cachorro_text, (600,400))

    display.update()