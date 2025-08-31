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

def calcular():
    try:
        resultado = eval(entrada_texto.get())
        entrada_texto.set(str(resultado))
    except:
        entrada_texto.set("Erro")

def limpar():
    entrada_texto.set("")

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


btn_limpar = tk.Button(
    janela,
    text="C",
    width=20, height=2,
    command=limpar,
    bg="red", fg="white"
)

btn_limpar.pack(pady=10)

janela.mainloop()