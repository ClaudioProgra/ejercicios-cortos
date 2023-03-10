import platform
import os
import time 


def animacion(so,palabra):
    if so == "Linux":
        limpiar = "clear"
    
    conta = 0
    while True:
        
        palabra =  " " + palabra
        time.sleep(0.2)
        os.system(limpiar)
        print(palabra)

        if conta == 40:
            break
        conta = conta + 1    


if __name__ == "__main__":
    so = platform.system()
    animacion(so,"Mayoneza")