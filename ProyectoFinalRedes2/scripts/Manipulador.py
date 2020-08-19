from pathlib import Path

NOMBRE_ARCHIVO = "mensaje.txt"
RUTA_ARCHIVO = (Path(__file__).parent / ("../archivos/"+NOMBRE_ARCHIVO)).resolve()

class MAnipulador():

    def __init__(self):
        pass

    def lecturaArchivo(self, ruta=None):
        if ruta is None:
            return open(RUTA_ARCHIVO, "r").read()
        else:
            return open(ruta, "r").read()

    def textoABinario(self, srt='', texto=""):
        return srt.join(format(ord(l), 'b') for l in texto)

    def contarCaracteres(self, texto=""):
        diccionario={}
        for l in texto:
            if l in diccionario:
                diccionario[l] = str(int(diccionario[l]) +1)
            else:
                diccionario[l] = str(1)
        caracteres = sorted(diccionario.items(), key=lambda t: t[1], reverse=True)
        return caracteres
    
    def caracteresABinario(self, texto=""):
        diccionario={}
        for l in texto:
            if l in diccionario:
                continue
            else:
                diccionario[l] = format(ord(l), 'b')
        return diccionario