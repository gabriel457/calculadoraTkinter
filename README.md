# 🧮 Calculadora Tkinter

Uma calculadora com interface gráfica desenvolvida em **Python** utilizando **Tkinter**. Este projeto foi criado para praticar os fundamentos de Python, a criação de interfaces gráficas e o tratamento de eventos.

## 🚀 Funcionalidades

- Visor para exibir expressões matemáticas e resultados
- Botões numéricos de 0 a 9
- Operações básicas: adição (`+`), subtração (`-`), multiplicação (`*`) e divisão (`/`)
- Respeito à precedência das operações matemáticas
- Botão `=` e tecla Enter para calcular
- Botão `C` e tecla Esc para limpar o visor
- Botão `⌫` e tecla Backspace para apagar o último caractere
- Suporte à digitação de números e operadores pelo teclado
- Histórico de operações realizadas
- Botão para limpar o histórico sem apagar o conteúdo do visor
- Tratamento de expressões inválidas e divisão por zero
- Avaliação restrita de expressões matemáticas utilizando `ast`

## 🛠️ Tecnologias utilizadas

- Python 3
- Tkinter
- `ast` e `operator`, módulos da biblioteca padrão do Python
- Git e GitHub para versionamento

## 📋 Pré-requisitos

- Python instalado
- Tkinter disponível na instalação do Python
- Git instalado para clonar o repositório

## 💻 Instalação do Tkinter no Windows

Nas instalações convencionais do Python para Windows, o Tkinter geralmente já está incluído e não precisa ser instalado separadamente pelo `pip`.

1. Instale o Python pelo [site oficial](https://www.python.org/downloads/windows/), caso ainda não esteja instalado.
2. Abra o PowerShell ou o terminal do VS Code.
3. Verifique se o Tkinter está funcionando:

   ```powershell
   py -m tkinter
   ```

   Caso o comando `py` não esteja disponível, tente:

   ```powershell
   python -m tkinter
   ```

4. Se uma janela de teste for exibida, o Tkinter está funcionando.

Se ocorrer um erro, verifique a instalação do Python e o suporte ao Tcl/Tk. Se necessário, repare ou reinstale o Python com os componentes correspondentes habilitados.

## 🐧 Instalação do Tkinter no Linux

Em distribuições baseadas no Ubuntu ou Debian, pode ser necessário instalar o Tkinter separadamente:

```bash
sudo apt update
sudo apt install python3-tk
```

Para verificar se a instalação está funcionando, execute:

```bash
python3 -m tkinter
```

Se uma janela de teste for exibida, o Tkinter está funcionando.

## 📦 Como executar

### 1. Clone o repositório

Copie a URL HTTPS do repositório pelo botão **Code** no GitHub e execute:

```bash
git clone URL_DO_SEU_REPOSITORIO
```

Substitua `URL_DO_SEU_REPOSITORIO` pelo endereço real do repositório.

### 2. Entre na pasta do projeto

```bash
cd calculadora-tkinter
```

### 3. Execute a calculadora

**No Windows:**

```powershell
py calculadora.py
```

Caso o comando `py` não esteja disponível:

```powershell
python calculadora.py
```

**No Linux:**

```bash
python3 calculadora.py
```

O projeto não exige a instalação de dependências adicionais pelo `pip`. No Linux, entretanto, o pacote do Tkinter pode precisar ser instalado pelo gerenciador de pacotes da distribuição.

## 🔮 Possíveis melhorias futuras

- Salvar o histórico para mantê-lo disponível após fechar a aplicação
- Adicionar operações como porcentagem e potenciação
- Aprimorar o design e a adaptação da interface a diferentes tamanhos de janela

---

Desenvolvido por **Gabriel Fernandes** como projeto de aprendizado em Python.