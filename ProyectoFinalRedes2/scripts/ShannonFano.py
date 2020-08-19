from functools import reduce

class ShannonFano():

    def __init__(self):
        pass

    def tuplaALista(self, lista=[]):
        for i in range(len(lista)):
            lista[i] = list(lista[i])
            lista[i].append("")
    
    def contarCaracteres(self, texto=""):
        diccionario={}
        for l in texto:
            if l in diccionario:
                diccionario[l] = diccionario[l] +1
            else:
                diccionario[l] = 1
        caracteres = sorted(diccionario.items(), key=lambda t: t[1], reverse=True)
        return caracteres
    
    def generarTabla(self, lista=[]):
        self.tuplaALista(lista)
        tabla = self.generarTablaRecursivo(lista)
        list(map(lambda l: l.pop(1), tabla))
        tabla = list(map(lambda l: tuple(l), tabla))
        return tabla
    
    def generarTablaRecursivo(self, lista=[]):
        listaR = self.dividirLista(lista)
        result = []
        for i in range(len(listaR)):
            for l in listaR[i]:
                l[2]+=str(i)
            if len(listaR[i])>1:
                result.extend(self.generarTablaRecursivo(listaR[i]))
            else:
                result.extend(listaR[i])
        return result
                
    def dividirLista(self, lista=[]):
        suma = reduce(lambda x, y: x + y, [i[1] for i in lista])
        acumulado1 = 0
        acumulado2 = 0
        contador = 0
        for l in lista:
            acumulado2 += l[1]
            if abs(suma/2-acumulado2)<abs(suma/2-acumulado1):
                contador+=1
                acumulado1 = acumulado2
            else:
                break
        listaR = [lista[:contador], lista[contador:]]
        return listaR

    def codificar(self, texto=""):
        listaCaracteres = self.contarCaracteres(texto)
        tabla = self.generarTabla(listaCaracteres)
        textoCodificado = self.generarTextoCodificado(self.convertirADiccionario(tabla), texto)
        return [tabla, textoCodificado]

    def generarTextoCodificado(self, tabla={}, texto=""):
        result = ""
        for c in texto:
            result += ""+tabla[c]
        return result

    def convertirADiccionario(self, tabla=[]):
        result = {}
        for l in tabla:
            result[l[0]]=l[1]
        return result
    
    def decodificar(self, tabla=[], texto=""):
        puntero = 0
        decodificado = ""
        cadena = ""
        buscando = True
        for b in texto:
            cadena+=b
            buscando = True
            while buscando:
                if len(tabla[puntero][1])>len(cadena):
                    if cadena==tabla[puntero][1][0:len(cadena)]:
                        buscando = False
                    else:
                        puntero+=1
                else:
                    if cadena==tabla[puntero][1][0:len(cadena)]:
                        buscando = False
                        decodificado+=tabla[puntero][0]
                        puntero = 0
                        cadena = ""
                    else:
                        puntero+=1
        return decodificado