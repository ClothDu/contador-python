import customtkinter as ctk
from customtkinter import ThemeManager as ctktm
from utils import Contador
from data_handler import Data
from tkinter import filedialog
import os

class Gui:
    def __init__(self, root : ctk.CTk, contador : Contador):
        self.root = root
        self.contador = contador
        self.mainframe = ctk.CTkFrame(self.root)
        self.mainframe.pack(fill="both", expand="true")
        
        self.frmMenu = ctk.CTkFrame(self.mainframe, fg_color=["#B9B9B9", "#242424"], corner_radius=0)
        self.frmMenu.grid(row=0, column=0, sticky="ew")
        self.mainframe.grid_columnconfigure(0, weight=1)
        
        self.frmMain = ctk.CTkFrame(self.mainframe)
        self.frmMain.grid(row=1, column=0, sticky="nsew")
        self.mainframe.grid_rowconfigure(1, weight=1)
        
        self.deveAbrirFile = False
        self.frmMenuFile : ctk.CTkFrame
        
        self.deveAbrirConfig = False
        self.frmMenuConfig : ctk.CTkFrame
        
    def trowErr(self, errType : str):
        popup = ctk.CTkToplevel(self.root)
        popup.title("Error")
        frame = ctk.CTkFrame()
        frame.pack(fill="both", expand=True)
        
        label = ctk.CTkLabel(frame, textvariable=f"Erro: {errType}")
        label.grid(row=0, column=0, sticky="nsew")
        
        button = ctk.CTkButton(frame, text="Fechar", command=popup.destroy)
        button.grid(row=1, column=0)
        
    def adicionar(self, pos):
        self.contador.adicionarPonto(pos, int(self.valor.get()))
        self.numeroLabelCtkString[pos].set(self.contador.getContador(pos))
    
    def remover(self, pos):
        self.contador.removerPonto(pos, int(self.valor.get()))
        self.numeroLabelCtkString[pos].set(self.contador.getContador(pos))
        
    def salvarArquivo(self):
        for i in range(len(contador.pontoContadores)):
            self.contador.modificarNome(i, self.NomesCTkString[i].get())
        arquivo = filedialog.asksaveasfilename(
            title="Selecione um arquivo",
            defaultextension=".json",
            filetypes=[("JSON files", "*.json"), ("Todos os arquivos", "*.*")],
        )

        if arquivo:
            Data.salvarFile(self.contador.__dict__, arquivo)
        else:
            self.trowErr("processo cancelado")
            
    def abrirArquivo(self):
        arquivo = filedialog.askopenfilename(
            title="Selecione um arquivo",
            filetypes=[("JSON files", "*.json"), ("Todos os arquivos", "*.*")],
        )

        if arquivo:
            try:
                data = Data.abrirFile(arquivo)
                self.contador = Contador(**data)
                for i in range(len(self.contador.pontoContadores)):
                    self.numeroLabelCtkString[i].set(self.contador.pontoContadores[i])
                for i in range(len(self.contador.nomeContador)):
                    self.NomesCTkString[i].set(self.contador.nomeContador[i])
            except Exception as e:
                self.trowErr(f"Erro ao abrir arquivo: {e}")
        else:
            self.trowErr("Erro ao abrir arquivo: arquivo inexistente")
        
    def botarFrameFile(self):
        if self.deveAbrirConfig:
            self.deveAbrirConfig = not self.deveAbrirConfig
            self.frmMenuConfig.place_forget()
        if self.deveAbrirFile:
            self.frmMenuFile.place(x=0, y=28)
        else:
            self.frmMenuFile.place_forget()
    
    def botarFrameConfig(self):
        if self.deveAbrirFile:
            self.deveAbrirFile = not self.deveAbrirFile
            self.frmMenuFile.place_forget()
        if self.deveAbrirConfig:
            self.frmMenuConfig.place(x=35, y=28)
        else:
            self.frmMenuConfig.place_forget()
        
    def qualDevoAbrir(self, opção : str):
        match opção: #type: ignore
            case "file":
                self.deveAbrirFile = not self.deveAbrirFile
                self.botarFrameFile()
            case "config":
                self.deveAbrirConfig = not self.deveAbrirConfig
                self.botarFrameConfig()
            case _:
                self.trowErr("sem passagens validas")
    
    def temas(self):
        self.frmMenuConfig.place_forget()
        def listaDeTemas():
            pasta = os.path.abspath("./Temas")
            lista = os.listdir(pasta)
            return lista

        def definirTema(path):
            ctk.set_default_color_theme(path)
            self.gui()
        
        def retornarAOrigem(path):
            ctk.set_default_color_theme(path)
            self.gui()
            popup.destroy()
            
        
        popup = ctk.CTkToplevel(self.mainframe)
        popup.title("Selecionar temas")
        
        temaAtual = ctk.ThemeManager._currently_loaded_theme
        
        frame = ctk.CTkFrame(popup)
        frame.grid(row=0, column=0, sticky="nsew")
        frame.grid_columnconfigure(0, weight=1)
        
        endframe = ctk.CTkFrame(popup)
        endframe.grid(row=1, column=0, sticky="nsew")
        endframe.grid_columnconfigure(0, weight=1)

        listTemas = listaDeTemas()
        
        listPaths = []
        for i in listTemas:
            listPaths.append(os.path.abspath("./Temas") + "/" + i)
        for idx, nome in enumerate(listTemas):
            btn = ctk.CTkButton(frame, text=nome.removesuffix(".json"), command=lambda nome=listPaths[idx]:definirTema(nome))
            btn.grid(row=idx, column=0)
        
        confirmar = ctk.CTkButton(endframe, text="Confirmar", command=popup.destroy)
        cancelar = ctk.CTkButton(endframe, text="Cancelar", command=lambda ta=temaAtual:retornarAOrigem(ta))
        confirmar.grid(row=0, column=1)
        cancelar.grid(row=0, column=0)
        
        
    def menu(self):
        self.frmMenuFile = ctk.CTkFrame(self.root, width=35, height=56)
        botaoSalvar = ctk.CTkButton(self.frmMenuFile, text="Salvar", command=self.salvarArquivo, width=90, height=28, corner_radius=0)
        botaoCarregar = ctk.CTkButton(self.frmMenuFile, text="Abrir", command=self.abrirArquivo, width=90, height=28, corner_radius=0)
        botaoSalvar.grid(row=0, column=0, sticky="we")
        botaoCarregar.grid(row=1, column=0, sticky="we")
        self.menuFileButton = ctk.CTkButton(self.frmMenu, text="File", fg_color="transparent", width=35,command=lambda: self.qualDevoAbrir("file"), corner_radius=0)
        self.menuFileButton.grid(row=0, column=0, sticky="nw")
        
        self.frmMenuConfig = ctk.CTkFrame(self.root, width=35, height=28)
        botaotemas = ctk.CTkButton(self.frmMenuConfig, text="Temas", command=self.temas, width=140, height=28, corner_radius=0)
        botaotemas.grid(row=0, column=0)
        self.menuConfigButton = ctk.CTkButton(self.frmMenu, text="Configurações", fg_color="transparent", width=35, command=lambda: self.qualDevoAbrir("config"), corner_radius=0)
        self.menuConfigButton.grid(row=0, column=1, sticky="nw")

    def colocarCoisas(self):
        self.root.grid_rowconfigure(0, weight=1)
        self.frmMain.grid_rowconfigure(0, weight=1)
        
        self.NomesCTkString = []
        self.nomeLabelCtk = []
        
        self.numeroLabelCtkString = []
        self.numeroLabelCtk = []
        
        self.framesDosBotoes = []
        
        self.valor = ctk.StringVar(value=1)
        
        for i in range(len(self.contador.pontoContadores)):
            #frame grandão que as coisas ficam dentro
            
            frm = ctk.CTkFrame(self.frmMain, corner_radius=6)
            frm.grid(row=0, column=i, sticky="nsew")
            self.frmMain.grid_columnconfigure(i, weight=1)
            
            # frame que as coisas de cima ficam
            
            frmtop = ctk.CTkFrame(frm)
            frmtop.grid(row=0, column=0)
            
                # label de nomes que ficam nas entry
            
            labelDosNomesCTkVar = ctk.StringVar()
            labelDosNomesCTkVar.set(self.contador.nomeContador[i])
            self.NomesCTkString.append(labelDosNomesCTkVar)
            
                    # entry com o nome dos jogadores (editavel pra poder mudar)
            
            label = ctk.CTkEntry(frmtop, placeholder_text=self.NomesCTkString[i], textvariable=self.NomesCTkString[i], width=400, fg_color="transparent", font=("Roboto", 30), justify="center")
            frm.grid_columnconfigure(i, weight=1)
            label.grid(row=1, column=1, sticky="nwe")
            self.nomeLabelCtk.append(label)
            
                # numeros que ficam nas labels
            
            numeroLabelCtkStringVar = ctk.StringVar()
            numeroLabelCtkStringVar.set(self.contador.pontoContadores[i])
            self.numeroLabelCtkString.append(numeroLabelCtkStringVar)
            
                    # labels dentro do programa
            
            labelNum = ctk.CTkLabel(frmtop, textvariable=self.numeroLabelCtkString[i], width=400, height=350, fg_color="transparent", font=("Roboto", 75))
            labelNum.grid(row=2, column=1, sticky="we")
            self.numeroLabelCtk.append(labelNum)
            
            # frame de baixo que ficam os botões e tals
            
            frm.grid_rowconfigure(1, weight=1)
            frmbottom = ctk.CTkFrame(frm, corner_radius=0)
            frmbottom.grid(row=1, column=0, sticky="nswe")
            frmbottom.grid_columnconfigure(0, weight=1)
            frmbottom.grid_columnconfigure(4, weight=1)
            frmbottom.grid_rowconfigure(0, weight=1)
            
                # entry que definem quantos valores seram acrescentados ou diminuidos nos botões + botões de mais e menos
            
            entryValor = ctk.CTkEntry(frmbottom, placeholder_text="1", textvariable=self.valor, width=75)
            entryValor.grid(row=0, column=1, sticky="nwe")
            botãoMenos = ctk.CTkButton(frmbottom, text="-", command=lambda n=i: self.remover(n),width=30)
            botãoMenos.grid(row=0, column=2, sticky="nwe")
            botãoMais = ctk.CTkButton(frmbottom, text="+", command=lambda n=i: self.adicionar(n),width=30)
            botãoMais.grid(row=0, column=3, sticky="nwe")
            self.framesDosBotoes.append(frm)

    def gui(self):
        # criar coisas de menu
        self.menu()
        
        # cria coisas no frmMain
        self.colocarCoisas()
        
        
contador = Contador()
ctk.set_appearance_mode("system")
ondeEstou = os.path.abspath("./")
ondeEstou += "/Temas/cherry.json"
ctk.set_default_color_theme(ondeEstou)
root = ctk.CTk()
root.option_add('*tearOff', False)
root.title("Contador")
root.geometry("800x500")

gui = Gui(root, contador)
gui.gui()

root.mainloop()