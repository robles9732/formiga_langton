import tkinter as tk

janela = tk.Tk()
janela.geometry("800x800")
janela.title("Formiga de Langton")

cel_colors = ['#fff', '#000'] # define a cor da célula, 0 = branca, 1 = preta
cor = 0
x = 50 
y = 50  # índices de linha e coluna
matriz_labels = [] # cria a matriz a mudar de cor
contador = 1

frame = tk.Frame(janela)
frame.grid(row=0, column=0, padx=10, pady=10, stick = 'ew')
for i in range(98):
    linha = []
    for j in range(98):
        lbcelula = tk.Label(frame, width=2, height=1 , background=cel_colors[cor], font=("Arial", 1))
        lbcelula.grid(row=i, column=j)
        linha.append(lbcelula)
    matriz_labels.append(linha) #cria a matriz de linhas e colunas de labels

matriz_labels[x][y]
direcao = 'L' # direção em que se inicia o primeiro movimento
def caminho_formiga():
    global contador     
    global direcao
    global x
    global y
    global cor
            
    cel_color = matriz_labels[x][y].cget('bg') # Captura a cor de fundo e verfica se é preta ou branca
    x_out = x # Variáveis que guardam a posição da célula deixada
    y_out = y
    if cel_color == cel_colors[0]:   # sempre que for branca, se move para a direita, relativamente aos pontos cardeais
        if direcao == 'L':
            y += 1
            direcao = 'S'                                
        elif direcao == 'O':
            y -= 1
            direcao = 'N'
        elif direcao == 'N':
            x -= 1
            direcao = 'L'
        elif direcao == 'S':                
            x += 1
            direcao = 'O'
        cor = 1
    else:                   # sempre que for preta, se move para a esquerda, relativamente aos pontos cardeais
        if direcao == 'L':
            y -= 1
            direcao = 'N'
        elif direcao == 'O':
            y += 1
            direcao = 'S'
        elif direcao == 'N':
            x += 1
            direcao = 'O'
        elif direcao == 'S':
            x -= 1
            direcao = 'L'
        cor = 0
    matriz_labels[x],[y]        # Move de acordo com a direção ordenada no último movimento
    matriz_labels[x_out][y_out].configure(background = cel_colors[cor]) # Altera a cor da célula deixada
    
    janela.after(5, caminho_formiga) # Repete o loop a cada 50 milisegundos

caminho_formiga() # Repete o loop

janela.mainloop()