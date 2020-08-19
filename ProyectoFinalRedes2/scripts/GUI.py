import ShannonFano as sf
import Huffman as hm
import LZ77 as lz
import Manipulador as fm

from tkinter import *
from tkinter import ttk

class Ventana():

    def __init__(self):
        self.objManipulador = fm.MAnipulador()
        self.raiz = Tk()
        self.iniciarInterfaz()
        self.raiz.mainloop()

    def iniciarInterfaz(self):
        self.raiz.title("Comparación Algoritmos de compresión")
        self.raiz.geometry('1000x800')
        self.raiz.resizable(width=False,height=False)
        self.raiz.configure(bg = 'beige')
        self.raiz.title('Aplicación')
        self.btnSF = ttk.Button(self.raiz, text='Codificar por Shanon-Fano', command=lambda: self.ejecutarCodificador(boton="SF"))
        self.btnSF.place(x=10, y=20, width=200, height=30)
        self.btnHM = ttk.Button(self.raiz, text='Codificar por Huffman', command=lambda: self.ejecutarCodificador(boton="HM"))
        self.btnHM.place(x=10, y=55, width=200, height=30)
        self.btnLZ = ttk.Button(self.raiz, text='Codificar por Lampel Ziv', command=lambda: self.ejecutarCodificador(boton="LZ"))
        self.btnLZ.place(x=10, y=90, width=200, height=30)
        self.lblSB = Label(self.raiz, text="SB")
        self.lblSB.place(x=10, y=125, width=25, height=30)
        self.textSB = Entry(self.raiz)
        self.textSB.place(x=40, y=125, width=25, height=30)
        self.lblLAB = Label(self.raiz, text="LAB")
        self.lblLAB.place(x=70, y=125, width=25, height=30)
        self.textLAB = Entry(self.raiz)
        self.textLAB.place(x=100, y=125, width=25, height=30)
        self.lblSS = Label(self.raiz, text="SS")
        self.lblSS.place(x=130, y=125, width=25, height=30)
        self.textSS = Entry(self.raiz)
        self.textSS.place(x=160, y=125, width=25, height=30)
        self.btnT = ttk.Button(self.raiz, text='Codificar Todos a la vez', command=self.ejecutarTodos)
        self.btnT.place(x=10, y=160, width=200, height=30)
        self.textG = Text(self.raiz)
        self.textG.place(x=220, y=20)
        self.textG.config(width=75, height=38, font=("Consolas",12), selectbackground="gray")
        self.textoR = Text(self.raiz)
        self.textoR.place(x=10, y=195, width=200, height=600)
        self.btnBorrarT = ttk.Button(self.raiz, text='Borrar Resultados', command=lambda : self.textoR.delete("1.0", END))
        self.btnBorrarT.place(x=220, y=765, width=200, height=30)
        self.btnBorrarT = ttk.Button(self.raiz, text='Borrar Texto', command=lambda : self.textG.delete("1.0", END))
        self.btnBorrarT.place(x=425, y=765, width=200, height=30)
        self.btnBorrarT = ttk.Button(self.raiz, text='Borrar Todo', command=self.borrarTextos)
        self.btnBorrarT.place(x=630, y=765, width=200, height=30)

    def borrarTextos(self):
        self.textoR.delete("1.0", END)
        self.textG.delete("1.0", END)

    def ejecutarTodos(self):
        texto = self.textG.get("1.0", END)
        texto = texto[:len(texto)-1]
        self.textoR.delete("1.0", END)
        if len(texto)==0:
            self.textoR.insert(INSERT,"Digite algo en el campo del texto.")
        else:
            sb = self.textSB.get()
            lab = self.textLAB.get()
            ss = self.textSS.get()
            aux = False
            if len(sb)>0 and len(lab)>0 and len(ss)>0:
                sb = int(sb)
                lab = int(lab)
                ss = int(ss)
                aux = True
            resultado = ""
            rSF = self.ejecutarSF(texto)
            rHM = self.ejecutarHM(texto)
            rLZ = None
            if aux:
                rLZ = self.ejecutarLZ(sb=sb, lab=lab, ss=ss, texto=texto)
            else:
                rLZ = self.ejecutarLZ(texto=texto)
            resultado += "LONGITUDES EN BITS:\n"
            resultado += "Tamaño original: "+str(len(self.objManipulador.textoABinario(texto=texto)))+"\n"
            resultado += "Shanon fano: "+str(len(rSF[1]))+"\n"
            resultado += "Huffman: "+str(len(rHM[1]))+"\n"
            resultado += "Lampel Ziv: "+str(len(rLZ[1]))+"\n\n"
            resultado += "DATOS CODIGOS:\n"
            resultado += "Codigos de Shanon-Fano:\n"
            resultado += self.listaACadena(rSF[0])
            resultado += "Codigos de Huffman:\n"
            resultado += self.listaACadena(rHM[0])
            resultado += "Ternas de Lampel-Ziv:\n"
            resultado += self.listaACadena(rLZ[0])
            self.textoR.insert(INSERT,resultado)

    def listaACadena(self, tabla=None):

        def internoACadena(t):
            return "["+", ".join(t)+"]\n"

        resultado = "".join(map(internoACadena, tabla))
        return resultado
    
    def ejecutarCodificador(self, boton=""):
        texto = self.textG.get(1.0, 'end')
        texto = texto[:len(texto)-1]
        self.textoR.delete("1.0", END)
        textSalida = ""
        resultado = None
        if len(texto)==0:
            self.textoR.insert(INSERT,"Digite algo en el campo del texto.")
        else:
            textSalida += "LONGITUDES EN BITS:\n"
            textSalida += "Tamaño original: "+str(len(self.objManipulador.textoABinario(texto=texto)))+"\n"
            if boton == "SF":
                tabla = self.objManipulador.contarCaracteres(texto)
                resultado = self.ejecutarSF(texto)
                textSalida += "Shanon fano: "+str(len(resultado[1]))+"\n\n"
                textSalida += "DATOS CODIGO:\n"
                textSalida += "Tabla de conteo:\n"
                textSalida += self.listaACadena(tabla)
                textSalida += "Codigos de Shanon-Fano:\n"
                textSalida += self.listaACadena(resultado[0])+"\n"
            elif boton == "HM":
                tabla = self.objManipulador.contarCaracteres(texto)
                resultado = self.ejecutarHM(texto)
                textSalida += "Huffman: "+str(len(resultado[1]))+"\n\n"
                textSalida += "DATOS CODIGO:\n"
                textSalida += "Tabla de conteo:\n"
                textSalida += self.listaACadena(tabla)
                textSalida += "Codigos de Huffman:\n"
                textSalida += self.listaACadena(resultado[0])+"\n"
            elif boton == "LZ":
                sb = self.textSB.get()
                lab = self.textLAB.get()
                ss = self.textSS.get()
                aux = False
                if len(sb)>0 and len(lab)>0 and len(ss)>0:
                    sb = int(sb)
                    lab = int(lab)
                    ss = int(ss)
                    aux = True
                if aux:
                    resultado = self.ejecutarLZ(sb=sb, lab=lab, ss=ss, texto=texto)
                else:
                    sb=11
                    lab=5
                    ss=8
                    resultado = self.ejecutarLZ(texto=texto)
                textSalida += "Lampel Ziv: "+str(len(resultado[1]))+"\n\n"
                textSalida += "DATOS CODIGO:\n"
                textSalida += "Valores de los buffers y el simbolo:\n"
                textSalida += "SB= "+str(sb)+"\nLAB= "+str(lab)+"\nSS= "+str(ss)+"\n"
                textSalida += "Ternas de Lampel-Ziv:\n"
                textSalida += self.listaACadena(resultado[0])+"\n"
            textSalida += "Codigo en binario:\n"
            textSalida += resultado[1]
            self.textoR.insert(INSERT,textSalida)

    def ejecutarSF(self, texto=""):
        codificador = sf.ShannonFano()
        resultado = codificador.codificar(texto)
        return resultado

    def ejecutarHM(self, texto=""):
        codificador = hm.Huffman()
        resultado = codificador.codificar(texto)
        return resultado

    def ejecutarLZ(self, sb=11, lab=5, ss=8, texto=""):
        codificador = lz.LZ77()
        resultado = codificador.codificar( sb=sb, lab=lab, ss=ss, texto=texto)
        self.textoR.insert(INSERT,self.listaACadena(resultado[0])+"\n")
        print(codificador.decodificar(resultado[1]))
        return resultado