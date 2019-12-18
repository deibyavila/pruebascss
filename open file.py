# -*- coding: utf-8 -*-
def writefile():
    """ escribir archivo """
    with open('./Documents/proyecto1/archivoxxxzz.txt', 'w') as f:
        for i in range(10):
            f.write(str(i))

def readfile():
    """leer archivo"""
    counter=0
    with open('C:/Users/Deiby Johany Avila/Documents/proyecto1/alepg.txt', 'r', encoding="utf8") as f:
        for lines in f:
            counter += lines.count('Beatriz')
        print('Beatriz se encuantra {} veces en el texto'.format(counter))


if __name__ == "__main__":
    readfile()