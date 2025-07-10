# Sistema simples de cadastro de pessoas

cadastros = []

def menu():
    print("\n=== MENU DE CADASTRO ===")
    print("1. Cadastrar nova pessoa")
    print("2. Listar pessoas cadastradas")
    print("3. Sair")

def cadastrar_pessoa():
    nome = input("Nome: ")
    idade = input("Idade: ")
    email = input("Email: ")
    
    pessoa = {
        "nome": nome,
        "idade": idade,
        "email": email
    }
    
    cadastros.append(pessoa)
    print(f"\nPessoa {nome} cadastrada com sucesso!")

def listar_pessoas():
    if not cadastros:
        print("\nNenhuma pessoa cadastrada.")
    else:
        print("\n=== Lista de Pessoas Cadastradas ===")
        for i, pessoa in enumerate(cadastros, 1):
            print(f"{i}. Nome: {pessoa['nome']}, Idade: {pessoa['idade']}, Email: {pessoa['email']}")

def main():
    while True:
        menu()
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            cadastrar_pessoa()
        elif opcao == "2":
            listar_pessoas()
        elif opcao == "3":
            print("Saindo do sistema. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
