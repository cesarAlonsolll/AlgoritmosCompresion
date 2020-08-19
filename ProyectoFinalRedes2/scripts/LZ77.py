class LZ77():

    SEARCH_BUFFER = 11
    LOOK_AHEAD_BUFFER = 5
    SIMBOL_SIZE = 8

    def codificar(self, sb = 11, lab = 5, ss = 8, texto = ""):

        ternas = []
        punteroTexto = 0
        finalTexto = len(texto)
        textoCodificado = ""
        if len(texto) > 0:
            textoCodificado += self.numeroABinario(sb, 4)+self.numeroABinario(lab, 4)+self.numeroABinario(ss, 4)

        while punteroTexto < finalTexto:
            punteroBufferS = [punteroTexto,0]
            creandoTerna = True
            textoTerna = ""
            terna = [0,0]
            while creandoTerna:
                punteroBufferS[1] = 0
                punteroBufferS[0] -= 1
                if punteroBufferS[0]<0 or (2**sb)-(punteroTexto-punteroBufferS[0])<0:
                    creandoTerna = False
                if creandoTerna:
                    aux = ""
                    aux1 = ""
                    while True:
                        if punteroBufferS[0]+punteroBufferS[1]<finalTexto-1 and punteroTexto+punteroBufferS[1]<finalTexto-1:
                            if punteroBufferS[0]+punteroBufferS[1]<punteroTexto:
                                if punteroBufferS[1]<(2**lab-1) and texto[punteroBufferS[0]+punteroBufferS[1]]==texto[punteroTexto+punteroBufferS[1]]:
                                    aux += texto[punteroTexto+punteroBufferS[1]]
                                    if aux>=textoTerna:
                                        textoTerna = aux
                                        terna = [punteroTexto-punteroBufferS[0], len(textoTerna)]
                                    punteroBufferS[1] += 1
                                else:
                                    if len(textoTerna)<=len(aux):
                                        textoTerna = aux
                                        terna = [terna[0], len(textoTerna)]
                                    break
                            else:
                                if punteroBufferS[1]<(2**lab)-1 and aux[punteroBufferS[1]%len(aux)]==texto[punteroTexto+punteroBufferS[1]]:
                                    aux1 += texto[punteroTexto+punteroBufferS[1]]
                                    terna = [punteroTexto-punteroBufferS[0], len(aux+aux1)]
                                    punteroBufferS[1] += 1
                                else:
                                    if len(textoTerna)<=len(aux +aux1):
                                        textoTerna = aux +aux1
                                    terna = [punteroTexto-punteroBufferS[0], len(textoTerna)]
                                    break
                        else:
                            break
                else:
                    #print([terna[0], terna[1], texto[punteroTexto+terna[1]]])
                    ternas.append([str(terna[0]), str(terna[1]), texto[punteroTexto+terna[1]]])
                    textoCodificado += self.numeroABinario(terna[0], sb)+self.numeroABinario(terna[1], lab)+self.carcaterABinario(texto[punteroTexto+terna[1]], ss)
                    punteroTexto += terna[1]+1
                    textoTerna = ""
        return [ternas, textoCodificado]
    
    def decodificar(self, textoBinario = ""):
        punteroTexto = 0
        finalTexto = len(textoBinario)
        textoDecodificado = ""
        if len(textoBinario) > 0:
            sb = self.binarioANumero(textoBinario[:4])
            lab = self.binarioANumero(textoBinario[4:8])
            ss = self.binarioANumero(textoBinario[8:12])
            punteroTexto += 12
        cantidadRecorrida = sb+lab+ss

        while punteroTexto < finalTexto:
            terna = [self.binarioANumero(textoBinario[punteroTexto:punteroTexto+sb]), self.binarioANumero(textoBinario[punteroTexto+sb:punteroTexto+sb+lab]),
                    self.binarioACaracter(textoBinario[punteroTexto+sb+lab:punteroTexto+sb+lab+ss])]
            print(terna)
            if terna[0]>=terna[1]:
                textoDecodificado += textoDecodificado[len(textoDecodificado)-terna[0]:len(textoDecodificado)-terna[0]+terna[1]]+terna[2]
            else:
                aux = textoDecodificado[len(textoDecodificado)-terna[0]:len(textoDecodificado)]
                for i in range(terna[1]):
                    textoDecodificado += aux[i%len(aux)]
                textoDecodificado += terna[2]
            punteroTexto += cantidadRecorrida
        return textoDecodificado

        
    def carcaterABinario(self, caracter = "", tamaño = 8):
        return format(ord(caracter), 'b').zfill(tamaño)

    def binarioACaracter(self, binario = ""):
        return chr(int(binario, 2))

    def numeroABinario(self, numero = 0, tamaño = 8):
        return bin(numero)[2:].zfill(tamaño)

    def binarioANumero(self, binario = ""):
        return int(binario, 2)