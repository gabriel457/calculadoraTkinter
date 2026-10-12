import tkinter as tk
import ast
import operator

janela = tk.Tk()
janela.title("Calculadora")
janela.geometry("300x560")

entrada_texto = tk.StringVar()

entrada = tk.Entry(
    janela,
    textvariable=entrada_texto,
    font=("Arial", 20),
    bd=10,
    relief="sunken",
    justify="right"
)

entrada.pack(fill="both", ipadx=8, ipady=8, padx=10)

OPERACOES_BINARIAS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv
}

OPERACOES_UNARIAS = {
    ast.UAdd: operator.pos,
    ast.USub: operator.neg
}

resultado_exibido = False

def avaliar_no(no):
    if isinstance(no, ast.Constant) and type(no.value) in (int, float):
        return no.value

    if isinstance(no, ast.BinOp) and type(no.op) in OPERACOES_BINARIAS:
        esquerda = avaliar_no(no.left)
        direita = avaliar_no(no.right)

        operacao = OPERACOES_BINARIAS[type(no.op)]
        return operacao(esquerda, direita)

    if isinstance(no, ast.UnaryOp) and type(no.op) in OPERACOES_UNARIAS:
        valor = avaliar_no(no.operand)

        operacao = OPERACOES_UNARIAS[type(no.op)]
        return operacao(valor)

    raise ValueError("Expressão matemática não permitida")


def avaliar_expressao(expressao):
    arvore = ast.parse(expressao, mode="eval")
    return avaliar_no(arvore.body)

def click(valor):
    global resultado_exibido

    if entrada_texto.get() == "Erro":
        entrada_texto.set("")
        resultado_exibido = False

    if resultado_exibido:
        if valor not in ("+", "-", "*", "/"):
            entrada_texto.set("")

        resultado_exibido = False

    entrada_texto.set(entrada_texto.get() + str(valor))
    entrada.icursor(tk.END)

def calcular():
    global resultado_exibido
    expressao = entrada_texto.get()

    try:
        resultado = avaliar_expressao(expressao)
        resultado_exibido = True

        entrada_texto.set(str(resultado))

        lista_historico.insert(
            tk.END,
            f"{expressao} = {resultado}"
        )

    except Exception:
        entrada_texto.set("Erro")
        resultado_exibido = False

def limpar():
    global resultado_exibido

    resultado_exibido = False
    entrada_texto.set("")
    entrada.icursor(tk.END)

def apagar_ultimo():
    global resultado_exibido

    resultado_exibido = False
    texto = entrada_texto.get()

    if texto == "Erro":
        entrada_texto.set("")
    else:
        entrada_texto.set(texto[:-1])

    entrada.icursor(tk.END)

def limpar_historico():
    lista_historico.delete(0, tk.END)

def tratar_tecla(evento):
    tecla = evento.keysym
    caractere = evento.char

    if caractere and caractere in "0123456789+-*/.":
        click(caractere)

    elif caractere == "=" or tecla in ("Return", "KP_Enter"):
        calcular()

    elif tecla == "BackSpace":
        apagar_ultimo()

    elif tecla == "Escape":
        limpar()

    return "break"

operadores = [
    ("/", 1, 3),
    ("*", 2, 3),
    ("-", 3, 3),
    ("+", 4, 3),
    ("=", 4, 2)
]

frame_botoes = tk.Frame(janela)
frame_botoes.pack()

numeros = [
    ("7", 1,0), ("8", 1,1), ("9", 1, 2),
    ("4", 2,0), ("5", 2,1), ("6", 2, 2),
    ("1", 3,0), ("2", 3,1), ("3", 3, 2),
    ("0", 4,0), (".", 4, 1)
]

for texto, linha, coluna in numeros:
    btn = tk.Button(
        frame_botoes,
        text=texto,
        width=5, height=2,
        command=lambda n=texto: click(n)
    )
    btn.grid(row=linha, column=coluna, padx=5, pady=5)

for texto, linha, coluna in operadores:
    if texto == "=":
        btn = tk.Button(frame_botoes, text=texto, width=5, height=2, command=calcular, bg="lightgreen")
    else:
        btn = tk.Button(frame_botoes, text=texto, width=5, height=2, command=lambda op=texto: click(op))
    btn.grid(row=linha, column=coluna, padx=5, pady=5)

frame_acoes = tk.Frame(janela)
frame_acoes.pack(pady=10)

btn_limpar = tk.Button(
    frame_acoes,
    text="C",
    width=8,
    height=2,
    command=limpar,
    bg="red",
    fg="white"
)
btn_limpar.pack(side="left", padx=5)

btn_apagar = tk.Button(
    frame_acoes,
    text="⌫",
    width=8,
    height=2,
    command=apagar_ultimo
)
btn_apagar.pack(side="left", padx=5)

entrada.bind("<Key>", tratar_tecla)

janela.bind_all("<Key>", tratar_tecla)

janela.bind_all(
    "<ButtonRelease-1>",
    lambda evento: entrada.focus_set()
)

entrada.focus_set()

frame_historico = tk.LabelFrame(
    janela,
    text="Histórico",
    padx=5,
    pady=5
)
frame_historico.pack(
    fill="both",
    expand=True,
    padx=10,
    pady=5
)

lista_historico = tk.Listbox(
    frame_historico,
    height=3,
    font=("Arial", 11)
)

lista_historico.pack(fill="both", expand=True)
btn_limpar_historico = tk.Button(
    frame_historico,
    text="Limpar histórico",
    command=limpar_historico
)

btn_limpar_historico.pack(pady=5)

janela.mainloop()