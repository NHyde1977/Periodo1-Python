import json
import os

# Verifica se o arquivo JSON já existe e carrega os dados
if os.path.exists("E-Books.json"):
    with open("E-Books.json", "r") as arquivo:
        ebooks_dict = json.load(arquivo)
else:
    # Dados iniciais, caso o arquivo não exista
    ebooks_dict = {
        "ebooks": [
            {
                "id": 1,
                "título": "1984",
                "autor": "George Orwel",
                "editora": "Citadel",
                "gênero": "Ficção"
            },
            {
                "id": 2,
                "título": "Crime e castigo",
                "autor": "Fiódor Dostoiévski",
                "editora": "Principis",
                "gênero": "Ficção"
            }
        ]
    }
    # Cria o arquivo JSON inicial
    with open("E-Books.json", "w") as arquivo:
        json.dump(ebooks_dict, arquivo, indent=4, ensure_ascii=False)

# Função para adicionar livro
def adicionar_livro():
    print("Digite as informações do novo livro:")

    título = input("Título: ")
    autor = input("Autor: ")
    editora = input("Editora: ")
    gênero = input("Gênero: ")

    # Gerando novo ID
    novo_id = max([livro["id"] for livro in ebooks_dict["ebooks"]]) + 1

    novo_livro = {
        "id": novo_id,
        "título": título,
        "autor": autor,
        "editora": editora,
        "gênero": gênero
    }

    ebooks_dict["ebooks"].append(novo_livro)

    # Salvando o JSON no arquivo
    with open("E-Books.json", "w") as arquivo:
        json.dump(ebooks_dict, arquivo, indent=4, ensure_ascii=False)

    print("Livro adicionado com sucesso!")

# Função para buscar livros
def buscar_livros():
    print("\nComo você deseja procurar um livro?")
    print("1 - Por título")
    print("2 - Por autor")
    print("3 - Por gênero")
    escolha = input("Escolha uma opção (1/2/3): ")

    if escolha == '1':
        titulo_busca = input("Digite o título do livro: ").lower()
        resultados = [livro for livro in ebooks_dict["ebooks"] if titulo_busca in livro["título"].lower()]
    elif escolha == '2':
        autor_busca = input("Digite o autor do livro: ").lower()
        resultados = [livro for livro in ebooks_dict["ebooks"] if autor_busca in livro["autor"].lower()]
    elif escolha == '3':
        genero_busca = input("Digite o gênero do livro: ").lower()
        resultados = [livro for livro in ebooks_dict["ebooks"] if genero_busca in livro["gênero"].lower()]
    else:
        print("Opção inválida.")
        return

    if resultados:
        print("\nLivros encontrados:")
        for livro in resultados:
            print(
                f"ID: {livro['id']}, Título: {livro['título']}, Autor: {livro['autor']}, Editora: {livro['editora']}, Gênero: {livro['gênero']}")
    else:
        print("Nenhum livro encontrado com esse critério.")

# Função para remover livro
def remover_livro():
    try:
        livro_id = int(input("\nDigite o ID do livro que deseja remover: "))
        livro_removido = None

        # Procurando o livro pelo ID
        for livro in ebooks_dict["ebooks"]:
            if livro["id"] == livro_id:
                livro_removido = livro
                break

        if livro_removido:
            ebooks_dict["ebooks"].remove(livro_removido)
            print(f"\nLivro com ID {livro_id} removido com sucesso!")

            # Salvando as alterações no arquivo JSON
            with open("E-Books.json", "w") as arquivo:
                json.dump(ebooks_dict, arquivo, indent=4, ensure_ascii=False)
        else:
            print(f"Livro com ID {livro_id} não encontrado.")
    except ValueError:
        print("Por favor, insira um ID válido.")

# Menu principal
def menu():
    while True:
        print("\nMenu de opções:")
        print("1 - Adicionar livro")
        print("2 - Buscar livro")
        print("3 - Remover livro")
        print("4 - Sair")

        opcao = input("Escolha uma opção (1/2/3/4): ")

        if opcao == '1':
            adicionar_livro()
        elif opcao == '2':
            buscar_livros()
        elif opcao == '3':
            remover_livro()
        elif opcao == '4':
            print("Saindo...")
            break
        else:
            print("Opção inválida!")

# Executando o menu
menu()
