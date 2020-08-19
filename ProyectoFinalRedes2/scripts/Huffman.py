class Huffman():

    def __init__(self):
        pass

    def generarTabla(self, lista=[]):
        arbol = self.generarArbol(lista)
        tabla = self.leerArbol(arbol)
        return tabla
    
    def leerArbol(self, arbol = None):
        valor = []
        def recursivo(nodo, bit):
            if type(nodo) is Nodo:
                recursivo(nodo.geNodoI(), bit+"1")
                recursivo(nodo.geNodoD(), bit+"0")
            elif type(nodo) is Hoja:
                valor.append((nodo.getCaracter(), bit))
        recursivo(arbol, "")
        return valor

    def generarArbol(self, lista=[]):
        nodos = [None]
        punterol = len(lista)-1

        def insertarEnNodoL(nodo):
            for i in range(len(nodos)):
                if nodos[i].getValor()<=nodo.getValor():
                    nodos.insert(i, nodo)
                    break
                elif i+1 == len(nodos):
                    nodos.insert(i+1, nodo)
                    break

        while punterol >= 0:
            if nodos[0] is None:
                nodos[0] = self.generarNuevaHoja(lista[punterol])
                punterol -= 1
            else:
                auxV = nodos[len(nodos)-1].getValor()
                insertarEnNodoL(self.generarNuevaHoja(lista[punterol]))
                if auxV<=lista[punterol][1]:
                    aux = self.generarNuevoNodo(nodos.pop(), nodos.pop())
                    if len(nodos) == 0:
                        nodos.append(aux)
                    else:
                        insertarEnNodoL(aux)
                elif punterol > 0:
                        punterol -= 1
                        insertarEnNodoL(self.generarNuevaHoja(lista[punterol]))
                        aux = self.generarNuevoNodo(nodos.pop(), nodos.pop())
                        insertarEnNodoL(aux)
                punterol -= 1

        max = len(nodos)-1
        for i in range(max):
            aux = self.generarNuevoNodo(nodos.pop(), nodos.pop())
            if len(nodos) == 0:
                nodos.append(aux)
            else:
                insertarEnNodoL(aux)
        return nodos[0]

    def generarNuevoNodo(self, hojaI = None, hojaD = None):
        return Nodo(hojaI, hojaD)
    
    def generarNuevaHoja(self, datos = []):
        return Hoja(datos[0], datos[1])

    def contarCaracteres(self, texto=""):
        diccionario={}
        for l in texto:
            if l in diccionario:
                diccionario[l] = diccionario[l] +1
            else:
                diccionario[l] = 1
        caracteres = sorted(diccionario.items(), key=lambda t: t[1], reverse=True)
        return caracteres

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

class Nodo():

    def __init__(self, nodoI = None, nodoD = None):
        self.nodoI = nodoI
        self.nodoD = nodoD

    def getValor(self):
        auxValor = 0
        if self.nodoD is not None:
            auxValor += self.nodoD.getValor()
        if self.nodoI is not None:
            auxValor += self.nodoI.getValor()
        return auxValor

    def geNodoI(self):
        return self.nodoI

    def geNodoD(self):
        return self.nodoD

class Hoja(Nodo):

    def __init__(self, caracter="", valor = 0):
        self.caracter = caracter
        self.valor = valor

    def getValor(self):
        return self.valor

    def getCaracter(self):
        return self.caracter