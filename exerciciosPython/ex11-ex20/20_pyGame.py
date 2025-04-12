import pygame as pg 
pg.init()
try:
    pg.mixer.music.load('exerciciosPython/arquivo.mp3')
    pg.mixer.music.play()
    print("Está tocando?")
    while pg.mixer.music.get_busy():
        pg.time.Clock().tick(10)  # Manter o programa rodando enquanto a música toca
except pg.error as e:
    print(f"Erro ao carregar ou reproduzir a música: {e}")
finally:
    pg.quit()