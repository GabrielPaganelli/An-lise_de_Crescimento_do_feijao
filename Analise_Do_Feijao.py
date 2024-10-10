import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import messagebox

class Feijao:
    def __init__(self, root):
        self.dias = 0
        self.altura = 0
        self.nroFolhas = 0
        self.estagio = "Semente"
        self.flor = 0
        self.sementes = 0

        # Janela principal
        self.root = root
        self.root.title("Análise do Crescimento do Feijão")

        # Layout
        tk.Label(self.root, text="Dias:").grid(row=0, column=0)
        self.dias_entry = tk.Entry(self.root)
        self.dias_entry.grid(row=0, column=1)

        tk.Label(self.root, text="Altura (cm):").grid(row=1, column=0)
        self.altura_entry = tk.Entry(self.root)
        self.altura_entry.grid(row=1, column=1)

        tk.Label(self.root, text="Número de folhas:").grid(row=2, column=0)
        self.nroFolhas_entry = tk.Entry(self.root)
        self.nroFolhas_entry.grid(row=2, column=1)

        tk.Label(self.root, text="Número de flores:").grid(row=3, column=0)
        self.flor_entry = tk.Entry(self.root)
        self.flor_entry.grid(row=3, column=1)

        tk.Button(self.root, text="Adicionar Registro", command=self.addRegistro).grid(row=4, column=0, pady=10)
        tk.Button(self.root, text="Exibir Gráfico", command=self.Grafico).grid(row=4, column=1, pady=10)


    def addRegistro(self):
        try:
            self.dias = int(self.dias_entry.get())
            self.altura = float(self.altura_entry.get())
            self.nroFolhas = int(self.nroFolhas_entry.get())
            self.flor = int(self.flor_entry.get()) if self.dias > 20 else 0

            with open('registro.txt', 'a') as arquivo:
            
                # Adiciona um cabeçalho para o registro no arquivo para controle do gráfico
                arquivo.write("# Inicio\n")

                # self.dias = int#(input("\nQual a contagem de dias? "))
                arquivo.write("Dia: " + str(self.dias) + "\n")

                # Verificação do estágio atual da planta baseado nos dias decorridos
                if self.dias <= 3:
                    self.estagio = "Germinacao"
                    arquivo.write("Estagio: " + self.estagio + "\n")
                elif 4 <= self.dias <= 10:
                    self.estagio = "Crescimento"
                    arquivo.write("Estagio: " + self.estagio + "\n")
                elif 11 <= self.dias <= 20:
                    self.estagio = "Folhas"
                    arquivo.write("Estagio: " + self.estagio + "\n")
                elif 21 <= self.dias <= 30:
                    self.estagio = "Flor"
                    arquivo.write("Estagio: " + self.estagio + "\n")
                    # self.flor = input("Quantas flores a sua planta apresenta? ")
                    arquivo.write("Numero de flores: " + self.flor + "\n")
                else:
                    self.estagio = "Semente"
                    arquivo.write("Estagio: " + self.estagio + "\n")
                    # self.flor = input("Quantas flores a sua planta apresenta? ")
                    arquivo.write("Numero de flores: " + self.flor + "\n")

                # self.altura = input("Qual a altura da sua planta (cm)? ")
                arquivo.write("Altura: " + str(self.altura) + "\n")

                # self.nroFolhas = input("Quantas folhas a sua planta apresenta? ")
                arquivo.write("Numero de folhas: " + str(self.nroFolhas) + "\n")
                arquivo.write("")

                # Adiciona rodapé ao registro no arquivo para controle do gráfico
                arquivo.write("# Fim\n")

                messagebox.showinfo("Sucesso", "Registro adicionado com sucesso!")

        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira valores válidos.")

    def Grafico(self):

        # Litas para guardar as informações de altura (x) e dias (y)
        x = []
        y = []

        dentro_dos_dados = False

        with open("registro.txt", "r") as arquivo:
            for linha in arquivo:
                if linha.strip() == "# Inicio":  # Ao detectar o cabeçalho "Inicio" o programa entende que está dentro do registro
                    dentro_dos_dados = True
                    continue
                elif linha.strip() == "# Fim":  # Ao detectar o rodapé "Fim" o programa entende o término do registro
                    dentro_dos_dados = False
                    continue

                if dentro_dos_dados:
                    # Ler a linha que começa com a palavra "Altura"
                    if linha.startswith('Altura:'):
                        # Quebra a string em uma lista, separando-a com base no delimitador ":"
                        valor1 = linha.strip().split(':')
                        try:
                            # Tenta a conversão do segundo elemento da lista "valor1" e adiciona ele à lista x
                            x.append(float(valor1[1]))

                        except ValueError:
                            print(f"Erro ao converter a linha: {linha}")

                    # Ler a linha que começa com a palavra "Dia"
                    if linha.startswith('Dia:'):
                        # Quebra a string em uma lista, separando-a com base no delimitador ":"
                        valor2 = linha.strip().split(':')
                        try:
                            # Tenta a conversão do segundo elemento da lista "valor2" e adiciona ele à lista y
                            y.append(float(valor2[1]))
                        except ValueError:
                            print(f"Erro ao converter a linha: {linha}")

        plt.scatter(x, y, color='blue', label='Dados')
        # Adiciona uma linha para conectar os pontos do gráfico
        plt.plot(x, y, color='green', linestyle='-', label='Crescimento')
        plt.xlabel('Altura')  # Rótulo do eixo X
        plt.ylabel('Dias')  # Rótulo do eixo Y
        plt.title("Crescimento da planta")
        plt.show()


# programa principal
if __name__ == "__main__":
    root = tk.Tk()
    app = Feijao(root)
    root.mainloop()
