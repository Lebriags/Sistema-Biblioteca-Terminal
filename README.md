# Sistema de Biblioteca

## 🔗 Repositório

https://github.com/Lebriags/Sistema-Biblioteca-Terminal

> Projeto desenvolvido em Python com foco em lógica de programação, estruturas de dados e organização de código.

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Status](https://img.shields.io/badge/Status-Em%20Desenvolvimento-yellow?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

---

# 📖 Sobre o Projeto

O objetivo deste projeto é desenvolver um **Sistema de Gerenciamento de Biblioteca** totalmente em Python utilizando apenas o terminal.

O sistema simula o funcionamento de uma pequena biblioteca, permitindo cadastrar livros, realizar empréstimos, devoluções, pesquisas e visualizar estatísticas.

Todo o projeto foi desenvolvido **sem banco de dados**, mantendo todas as informações apenas em memória durante a execução do programa.

---

# 🎯 Objetivos de Aprendizagem

Durante o desenvolvimento deste projeto são praticados diversos conceitos fundamentais da programação em Python:

- Estruturas condicionais (`if`, `elif`, `else`)
- Estruturas de repetição (`for` e `while`)
- Manipulação de listas
- Listas aninhadas
- Manipulação de strings
- Validação de dados
- Organização de programas maiores
- Criação de menus interativos
- Controle de fluxo
- Boas práticas de programação

---

# 🖥️ Funcionalidades

## 📚 Cadastro de Livros

Cada livro cadastrado possui:

- Código (gerado automaticamente)
- Título
- Autor
- Ano de publicação
- Status

Status inicial:

```
Disponível
```

---

## 📋 Listagem de Livros

Exibe todos os livros cadastrados contendo:

- Código
- Título
- Autor
- Ano
- Status

Caso não exista nenhum livro:

```
Nenhum livro cadastrado.
```

---

## 🔍 Pesquisa de Livros

Permite pesquisar um livro pelo título.

A pesquisa **não diferencia letras maiúsculas e minúsculas**.

Exemplo:

```
Python
python
PYTHON
```

Todos retornam o mesmo resultado.

---

## 📖 Empréstimo de Livros

Permite realizar empréstimos utilizando o código do livro.

Regras:

- Livro disponível → empréstimo realizado.
- Livro já emprestado → mensagem de aviso.
- Código inexistente → livro não encontrado.

---

## 🔄 Devolução de Livros

Permite devolver livros emprestados.

Regras:

- Livro emprestado → devolução realizada.
- Livro já disponível → mensagem informativa.
- Código inexistente → livro não encontrado.

---

## 📊 Estatísticas

Exibe informações gerais da biblioteca:

- Total de livros cadastrados
- Livros disponíveis
- Livros emprestados

---

# 💡 Funcionalidades Extras

O projeto também implementa algumas melhorias para tornar a experiência mais agradável.

### ✅ Validação de entradas

Impedindo:

- Título vazio
- Autor vazio
- Ano inválido
- Entradas vazias

---

### 🔎 Pesquisa inteligente

A busca funciona independentemente do uso de letras maiúsculas ou minúsculas.

---

### 🎨 Interface organizada

O programa utiliza:

- Separadores
- Mensagens claras
- Menus organizados
- Navegação intuitiva

---

### ↩ Navegação

Em qualquer tela é possível retornar ao menu principal digitando:

```
retornar
```

---

# 🚫 Restrições do Projeto

Durante o desenvolvimento **não é permitido utilizar**:

- Banco de Dados
- Arquivos
- JSON
- CSV
- Bibliotecas externas
- Programação Orientada a Objetos (POO)

Todo o sistema funciona apenas utilizando estruturas básicas da linguagem Python.

---

# 🧠 Conceitos Praticados

- Listas
- Listas aninhadas
- Loops (`for` e `while`)
- Condicionais
- `append()`
- `split()`
- `strip()`
- `lower()`
- `isdigit()`
- `len()`
- Manipulação de Strings
- Validação de dados
- Organização de código

---

# 📁 Estrutura do Projeto

```
biblioteca-python/
│
├── README.md
└── main.py
```

---

# 🚀 Como Executar

Clone o repositório:

```bash
git clone https://github.com/Lebriags/Sistema-Biblioteca-Terminal.git
```

Entre na pasta:

```bash
cd Sistema-Biblioteca-Terminal
```

Execute:

```bash
python main.py
```

> **Observação:** Em alguns sistemas, pode ser necessário utilizar `python3 main.py`.

---

# 📸 Demonstração

Em breve serão adicionadas imagens e GIFs demonstrando o funcionamento do sistema.

---

# 🧪 Casos de Teste

O sistema deve funcionar corretamente nos seguintes cenários:

- Biblioteca vazia
- Apenas um livro
- Muitos livros cadastrados
- Livros com mesmo título
- Autores repetidos
- Livro já emprestado
- Livro inexistente
- Ano inválido
- Entrada vazia
- Opções inválidas
- Retorno ao menu principal

---

# 👨‍💻 Autor

Projeto desenvolvido por **Lebriag** durante os estudos de Python.

---

## ⭐ Objetivo

Este projeto faz parte da minha jornada de aprendizado em Python e tem como objetivo consolidar conhecimentos em lógica de programação através do desenvolvimento de aplicações completas utilizando apenas recursos básicos da linguagem.
