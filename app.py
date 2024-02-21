from tkinter import *

valor          = 0  # Valor a ser exibido no label
dif            = 0  # Valor a ser usado nas operações

#variaveis pa o programa saber quando fazer a operação
soma           = False 
subtracao      = False
multiplicacao  = False
divisao        = False

# Funções das operações que darão serviço aos botões
def click(num):
    entrada.delete(0,END)
    entrada.insert(END, num)

def somar():
    global valor, soma
    soma = True
    valor = entrada.get()

def subtrair(): 
    global valor, subtracao
    subtracao = True
    valor = entrada.get()

def multiplicar():
    global valor, multiplicacao
    multiplicacao = True
    valor = entrada.get()

def dividir():
    global valor, divisao
    divisao = True
    valor = entrada.get()

def igual():
    global soma, subtracao, multiplicacao, divisao, dif
    dif = entrada.get()
    entrada.delete(0, END)
    if soma:
        entrada.insert(0, int(valor) + int(dif))
        soma = False

    if subtracao:
        entrada.insert(0, int(valor) - int(dif))
        subtracao = False

    if multiplicacao:
        entrada.insert(0, int(valor) * int(dif))
        multiplicacao = False

    if divisao:
        try:
            entrada.insert(0, int(valor) / int(dif))
        except ZeroDivisionError:
            entrada.insert(0,"Erro")
        divisao = False

def limpar():
    entrada.delete(0, END)

#Funções para condigurar os botões de uma maneira mais pratica:
def botaoNun(text, x, y, width=5, height=2):
    botao = Button(janela, text=text, font=("Arial", 20), command=lambda: click(text))
    botao.config(width=width, height=height)
    botao.place(x=x, y=y)

def botaoOperacao(text, x, y, operacao):
    botao = Button(janela, text=text, font=("Arial", 20), command=operacao)
    botao.config(width=5, height=2)
    botao.place(x=x, y=y)

def botaoIgual(text, x, y, operacao):
    botao = Button(janela, text=text, font=("Arial", 20), command=operacao)
    botao.config(width=5, height=2)
    botao.place(x=x, y=y)

def botaoLimpar(text, x, y):
    botao = Button(janela, text=text, font=("Arial", 20), command=limpar)
    botao.config(width=5, height=2)
    botao.place(x=x, y=y)


# Abrindo e configurando a janela
janela = Tk()
janela.title("Calculadora")
janela.configure(background="white")
janela.maxsize(420,512)
janela.minsize(420,512)


entrada = Entry(janela, width=10, relief=FLAT, font=("Arial", 45), justify=RIGHT)
entrada.grid(row=0, column=0, columnspan=4, pady=1)

# Posicionando os botões:
botaoNun(1, 0, 93)
botaoNun(2, 105, 93)
botaoNun(3, 210, 93)
botaoNun(4, 0, 198)
botaoNun(5, 105, 198)
botaoNun(6, 210, 198)
botaoNun(7, 0, 303)
botaoNun(8, 105, 303)
botaoNun(9, 210, 303)
botaoNun(0, 0, 408)

botaoOperacao("+", 315, 93, somar)
botaoOperacao("-", 315, 198, subtrair)
botaoOperacao("*", 315, 303, multiplicar)
botaoOperacao("/", 315, 408, dividir)
botaoIgual('=', 210, 408, igual)
botaoLimpar("<", 105, 408)

mainloop()
