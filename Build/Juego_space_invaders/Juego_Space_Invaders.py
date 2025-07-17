#JUEGO (INVASION ESPACIAL).
import pygame #Importamos la libreria para acceder a ella
import random
import math
from pygame import mixer #Para utilizar sonidos
import io

#1. INICIALIZAR PYGAME
pygame.init() #Inicializamos la libreria para tener las herramientas a utilizar.
#CREACION DE PANTALLA.
#pantalla es igual a display, establecer el modo que se muestra pygame.
#El tamaño de la pantalla va en una tupla dentro de set_mode
pantalla = pygame.display.set_mode((800,600))
#Todos lo que ocurra en una pantalla de pygame es un evento (click, presionar teclas, movimientos, etc)

#TITULO E ICONO
pygame.display.set_caption("Space Invaders Marlon") #Set caption es para el titulo de la ventana
icono = pygame.image.load("ovni_icon.png") #Cargar imagen del icono.
pygame.display.set_icon(icono) #Llamar al icono
fondo = pygame.image.load('fondo.jpg')

#Agregar musica
mixer.music.load('MusicaFondo.mp3') #Cargamos archivo de audio
mixer.music.set_volume(0.3) #Volumen
mixer.music.play(-1) #Para reproducir archivo, el menos 1 es para que se repita

#Variables del jugador
img_jugador = pygame.image.load("nave.png") #Cargar imagen de nave
jugador_x = 368 #Posicion x
jugador_y = 500 #Posicion y
jugador_x_cambio = 0

#Variables del enemigo
img_enemigo = []#Cargar imagen de nave
enemigo_x = []
enemigo_y = []
enemigo_x_cambio = []
enemigo_y_cambio = []
cantidad_enemigos = 8

for e in range (cantidad_enemigos):
    #Variables del enemigo
    img_enemigo.append(pygame.image.load("enemigo.png")) #Cargar imagen de nave
    enemigo_x.append(random.randint(0,736)) #Posicion x
    enemigo_y.append(random.randint(50, 200)) #Posicion y
    enemigo_x_cambio.append(0.2)
    enemigo_y_cambio.append(50)

#Variables de la bala
balas = []
img_bala = pygame.image.load("bala.png") #Cargar imagen de nave
bala_x = 0
bala_y = 500
bala_x_cambio = 0
bala_y_cambio = 3
bala_visible = False

#Funcion para convertir fuente a bytes
def fuente_bytes (fuente):
    #Abrir el archivo TTF en modo lectura binaria.
    with open (fuente, 'rb') as f:
        #Lee todos los bytes del archivo y los almacena en una variable.
        ttf_bytes = f.read()
    #Creamos un objeto BytesIO a partir de los bytes del archivo TTF
    return io.BytesIO(ttf_bytes)

#Puntaje
puntaje = 0
fuente_como_bytes = fuente_bytes("FreeSansBold.ttf")
fuente = pygame.font.Font(fuente_como_bytes, 32) #Almacena nombre de la fuente y tamaño
texto_x = 10
texto_y = 10

#Texto final del juego
fuente_final = pygame.font.Font(fuente_como_bytes, 40)

def texto_final():
    mi_fuente_final = fuente_final.render("GAME OVER", True, (255, 255, 255))
    pantalla.blit(mi_fuente_final, (60,200))

#Funcion mostrar puntaje
def mostrar_puntaje(x, y):
    texto = fuente.render(f"Puntaje: {puntaje}", True, (255,255,255)) #Render es para renderizar
    pantalla.blit(texto, (x,y))

#Funcion jugador
def jugador(x,y):  #X e Y se agregan porque cambian
    pantalla.blit(img_jugador, (x, y)) #Blit = arrojar, 2 datos (imagen y largo y ancho)

#Funcion enemigo
def enemigo(x, y, ene):
    pantalla.blit(img_enemigo[ene], (x, y))

#Funcion disparar bala
def disparar_bala(x, y):
    global bala_visible
    bala_visible = True
    pantalla.blit(img_bala, (x + 16, y + 10))


#Funcion detectar colisiones
def hay_colision(x_1, y_1, x_2, y_2):
    distancia = math.sqrt(math.pow(x_1 - x_2,2) + math.pow(y_2 - y_1,2))
    if distancia < 27:
        return True
    else:
        return False

#1. LOOP DEL JUEGO (PANTALLA)
#Lo siguiente es un ciclo, el cual funciona cuando se muestre la pantalla.
#lo que hace el ciclo es revisar cada uno de los eventos
#y si ese evento es del tipo quit (que es cuando un usuario presiona la equis en la esquina de cada programa)
#Y si ese quit es verdadero podemos salir del ciclo y desaparece la pantalla.
se_ejecuta = True
while se_ejecuta:

    #Imagen
    pantalla.blit(fondo, (0,0)) #Primero pide imagen (la tenemos en una variable) y despues coordenadas de ajuste.
    #pantalla.fill((205, 144, 228))  # Fill = relleno (en formato RGB)

    #Iterar eventos
    for evento in pygame.event.get():
        # Evento para cerrar el programa
        if evento.type == pygame.QUIT:
            se_ejecuta = False

        #Evento presionar teclas
        if evento.type == pygame.KEYDOWN: #Keydown es la presion del dedo sobre la tecla (evento)
            if evento.key == pygame.K_LEFT:  #Validacion de flechas
                jugador_x_cambio = -0.2 #Movemos al personaje
            if evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 0.2 #Movemos al personaje
            if evento.key == pygame.K_SPACE:
                sonido_bala = mixer.Sound('disparo.mp3') #Agregamos sonido de disparo
                sonido_bala.play()
                nueva_bala = {
                    "x":jugador_x,
                    "y":jugador_y,
                    "velocidad": 5
                }
                balas.append(nueva_bala)
                if not bala_visible:
                    bala_x = jugador_x
                    disparar_bala(bala_x, bala_y)

        #Evento soltar flechas
        if evento.type == pygame.KEYUP:  #Keyup es para cuando el usuario suelte la tecla (evento)
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 0

    #Modificar ubicacion del jugador
    jugador_x += jugador_x_cambio #Modifica la variable que almacena la pos x (jugador x)

    #Mantener al jugador dentro de bordes
    if jugador_x <= 0:
        jugador_x = 0  #No permite rebasar limite
    elif jugador_x >= 736:
        jugador_x = 736

    #Modificar ubicacion del enemigo
    for e in range (cantidad_enemigos):
        #Fin del juego
        if enemigo_y[e] > 500:
            for k in range(cantidad_enemigos):
                enemigo_y[k] = 1000
            texto_final()
            break

        enemigo_x[e] += enemigo_x_cambio[e]

        #Mantener al enemigo dentro de bordes
        if enemigo_x[e] <= 0:
            enemigo_x_cambio[e] = 0.2
            enemigo_y[e] += enemigo_y_cambio[e]
        elif enemigo_x[e] >= 736:
            enemigo_x_cambio[e] = -0.2
            enemigo_y[e] += enemigo_y_cambio[e]

        #Colision
        for bala in balas:
            colision_bala_enemigo = hay_colision(enemigo_x[e], enemigo_y[e], bala["x"], bala["y"])
            if colision_bala_enemigo:
                sonido_colision = mixer.Sound("Golpe.mp3")
                sonido_colision.play()
                balas.remove(bala)
                puntaje += 1
                enemigo_x[e] = random.randint(0,736)
                enemigo_y[e] = random.randint(20, 200)
                break
        enemigo(enemigo_x[e], enemigo_y[e], e)

        colision = hay_colision(enemigo_x[e], enemigo_y[e], bala_x, bala_y)
        if colision:
            sonido_colision = mixer.Sound('Golpe.mp3')
            sonido_colision.play()
            bala_y = 500
            bala_visible = False
            puntaje += 1
            enemigo_x[e] = random.randint(0, 736)  # Posicion x
            enemigo_y[e] = random.randint(50, 200)  # Posicion y

        enemigo(enemigo_x[e], enemigo_y[e], e)

    #Movimiento bala
    for bala in balas:
        bala["y"] += bala["velocidad"]
        pantalla.blit(img_bala, (bala["x"] + 16, bala["y"] + 10))
        if bala["y"] < 0:
            balas.remove(bala)

    if bala_y <= -64:
        bala_y = 500
        bala_visible = False

    if bala_visible:
        disparar_bala(bala_x, bala_y)
        bala_y -= bala_y_cambio

    jugador(jugador_x,jugador_y)
    mostrar_puntaje(texto_x, texto_y)

    #Actualizar todos
    pygame.display.update()
