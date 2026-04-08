from pygame import *
import sys

init()

cachorro_imagem = image.load('cachorro.png')
cachorro_imagem = transform.scale(cachorro_imagem, (150,150))

cachorro_font = font.Font('Somelist.ttf', 50)

mixer.music.load('Fluffing-a-Duck(chosic.com).mp3')
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
    draw.rect(window, (50, 168, 70), (0, 550, 1280, 300))

    draw.circle(window, (255,255,0), (70,70), 50)

    draw.rect(window, (227, 195, 132), (200,350,300,200))
    draw.polygon(window, (196, 103, 49), ((200,350), (350,150), (500,350)))
    draw.rect(window, (148, 219, 227),(225,400,55,80) )
    draw.rect(window, (128, 85, 1), (350,400,90,150))
    draw.circle(window, (0,0,0), (360,470), 5)

    draw.rect(window, (128, 85, 1), (900,400,30,150))
    draw.circle(window, (20, 107, 2), (915,350), 100)

    draw.circle(window, (255,255,255), (900,75), 40)
    draw.circle(window, (255,255,255), (940,75), 40)
    draw.circle(window, (255,255,255), (980,75), 40)
    draw.circle(window, (255,255,255), (1020,75), 40)

    draw.line(window, (255,255,0),(70, 70),(150,70), 5)
    draw.line(window, (255,255,0),(70, 70),(70,150), 5)
    draw.line(window, (255,255,0),(70, 70),(140,140), 5)
    draw.line(window, (255,255,0),(70, 70),(140,30), 5)   
    
    
    #Desenhar imagens 
    window.blit(cachorro_imagem, (500,420))

    # Desenhar texto
    cachorro_text = cachorro_font.render('mais um dia calmo', True, (0, 0, 0))
    window.blit(cachorro_text, (400,100))

    display.update()
