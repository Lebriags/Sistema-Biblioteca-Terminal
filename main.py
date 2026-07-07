livros = [] # Lista que recebe os livros

# Função para limpar o terminal, deixando mais digerivel as coisas.
def limpar():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

def cadastrar_livro():
    
    while True:
        
        print("Para retornar ao menu inicial, digite '0' no campo do título do livro.")
        
        titulo = input("Digite o título do livro: ")
        
        if titulo == "0":
            break
        
        autor = input("Digite o autor do livro: ")
        ano = input("Digite o ano de publicação do livro: ")
        status = "disponível"
        codigo = len(livros) + 1
    
        livro = {
            "codigo": codigo,
            "titulo": titulo,
            "autor": autor,
            "ano": ano,
            "status": status    
        }
    
        livros.append(livro)
        print(f"\nLivro '{titulo}' cadastrado com sucesso!\n")

def listar_livro():
    
    while True:
        
        print("Livros cadastrados:\n")
        
        for livro in livros:
            print(f"Código: {livro['codigo']}, \nTitulo: {livro['titulo']}, \nAutor: {livro['autor']}, \nAno: {livro['ano']}, \nStatus: {livro['status']}\n ")

        sair = input("Digite '0' para retornar ao menu inicial: ")
        if sair == "0":
            break

def buscar_livro():
    
    while True:
        
        print("Pesquisar Livros:")
        
        pesquisa = input("Digite o código do livro que deseja buscar:\nPara retornar ao menu inicial, digite '0': ")
        
        if pesquisa == "0":
            break
        elif pesquisa == "":
            print("Por favor, digite um código válido.")
        elif not pesquisa.isdigit():
            print("Por favor, digite um código válido.")
        else:
            
            codigo = int(pesquisa)
            livro_encontrado = None
            
            for livro in livros:
                if livro['codigo'] == codigo:
                    livro_encontrado = livro
                    break
            
            if livro_encontrado:
                print(f"\nLivro encontrado! \nCódigo: {livro_encontrado['codigo']}, \nTitulo: {livro_encontrado['titulo']}, \nAutor: {livro_encontrado['autor']}, \nAno: {livro_encontrado['ano']}, \nStatus: {livro_encontrado['status']}\n")
            else:
                print("Livro não encontrado.")    
            
def emprestar_livro():
    
    while True:
        
        print("Emprestar Livro:")
        
        pesquisa = input("Digite o código do livro que deseja emprestar:\nPara retornar ao menu inicial, digite '0': ")
        
        if pesquisa == "0":
            break
        elif pesquisa == "":
            print("Por favor, digite um código válido.")
        elif not pesquisa.isdigit():
            print("Por favor, digite um código válido.")
        else:
            
            codigo = int(pesquisa)
            livro_encontrado = None
            
            for livro in livros:
                if livro['codigo'] == codigo:
                    livro_encontrado = livro
                    break
            
            if livro_encontrado:
                if livro_encontrado['status'] == "disponível":
                    livro_encontrado['status'] = "emprestado"
                    print(f"\nLivro '{livro_encontrado['titulo']}' emprestado com sucesso!\n")
                else:
                    print(f"\nLivro '{livro_encontrado['titulo']}' não está disponível para empréstimo.\n")
            else:
                print("Livro não encontrado.")

def devolver_livro():

    while True:
        
        print("Devolver um livro:\n")
            
        pesquisa = input("Digite o código do livro que deseja devolver:\nPara retornar ao menu inicial, digite '0': ")
        
        if pesquisa == "0":
            break
        elif pesquisa == "":
            print("Por favor, digite um código válido.")
        elif not pesquisa.isdigit():
            print("Por favor, digite um código válido.")
        else:
            
            codigo = int(pesquisa)
            livro_encontrado = None
            
            for livro in livros:
                if livro['codigo'] == codigo:
                    livro_encontrado = livro
                    break
            
            if livro_encontrado:
                if livro_encontrado['status'] == "emprestado":
                    livro_encontrado['status'] = "disponível"
                    print(f"\nLivro '{livro_encontrado['titulo']}' devolvido com sucesso!\n")
                else:
                    print(f"\nLivro '{livro_encontrado['titulo']}' não está emprestado.\n")
            else:
                print("Livro não encontrado.")

def estatisticas():
    
    while True:
        
        print("Estatísticas da Biblioteca:\n")
        
        total_livros = len(livros)
        livros_disponiveis = sum(1 for livro in livros if livro['status'] == "disponível")
        livros_emprestados = sum(1 for livro in livros if livro['status'] == "emprestado")
        
        print(f"Total de livros cadastrados: {total_livros}")
        print(f"Livros disponíveis para empréstimo: {livros_disponiveis}")
        print(f"Livros emprestados: {livros_emprestados}\n")
        
        sair = input("Digite '0' para retornar ao menu inicial: ")
        if sair == "0":
            break

def menu():
    
    while True:
        
        limpar()
        
        print("Bem vindo a BibliotecaPy2!")
        print("[1] - Cadastrar Livro")
        print("[2] - Listar Livros")
        print("[3] - Buscar Livros")
        print("[4] - Emprestar Livro")
        print("[5] - Devolver Livro")
        print("[6] - Estatisticas")
        print("[0] - Encerrar Programa")
        
        escolha = input("Por favor, digite o numero da opção desejada: ")
        
        if escolha == "1":
            limpar()
            cadastrar_livro()
        
        elif escolha == "2":
            limpar()
            listar_livro()
        
        elif escolha == "3":
            limpar()
            buscar_livro()
        
        elif escolha == "4":
            limpar()
            emprestar_livro()
        
        elif escolha == "5":
            limpar()
            devolver_livro()
        
        elif escolha == "6":
            limpar()
            estatisticas()
            
        elif escolha == "0":
            limpar()
            print("Encerrando......")
            print("Obrigado por usar!")            
            exit()
        
        else:
            limpar()
            print("Por favor, selecione uma opção valida...")

limpar()            
menu()
                     