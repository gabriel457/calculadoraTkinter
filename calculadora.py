import tkinter as tk

janela = tk.Tk()
janela.title("Calculadora")
janela.geometry("300x400")

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

def click(valor):
    entrada_texto.set(entrada_texto.get() + str(valor))
    entrada.icursor(tk.END)

def calcular():
    try:
        resultado = eval(entrada_texto.get())
        entrada_texto.set(str(resultado))
    except:
        entrada_texto.set("Erro")

def limpar():
    entrada_texto.set("")

def apagar_ultimo():
    texto = entrada_texto.get()

    if texto == "Erro":
        entrada_texto.set("")
    else:
        entrada_texto.set(texto[:-1])

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

btn_limpar.pack(pady=10)

entrada.bind("<Key>", tratar_tecla)

janela.bind_all("<Key>", tratar_tecla)

janela.bind_all(
    "<ButtonRelease-1>",
    lambda evento: entrada.focus_set()
)

entrada.focus_set()

janela.mainloop()