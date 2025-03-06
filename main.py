from modelos import Usuario, Funcionario, Livro, Emprestimo
from biblioteca_db import BibliotecaDB

usuario_id = 1
funcionario_id = 1
livro_id = 1
emprestimo_id = 1

def usuario_crud():
    while True:
        print("\nSubmenu Usuário:")
        print("1 - Criar Usuário")
        print("2 - Buscar Usuário")
        print("3 - Atualizar Usuário")
        print("4 - Listar Usuários")
        print("5 - Voltar ao menu principal")

        choice = input("Escolha uma opção (1-5): ")

        if choice == '1':
            db = BibliotecaDB()

            try:
                global usuario_id
                nome = input("Digite o nome do usuário: ")
                cpf = input("Digite o CPF do usuário: ")
                email = input("Digite o email do usuário: ")
                numero_cartao = input("Digite o número do cartão do usuário: ")

                usuario = Usuario(usuario_id, nome, cpf, email, numero_cartao)
                db.salvar_usuario(usuario)
                usuario_id += 1
            finally:
                db.fechar()
                print(f"Usuário {usuario.nome} ({usuario.id}) salvo com sucesso!")
        elif choice == '2':
            db = BibliotecaDB()

            try:
                id_usuario = int(input("Digite o id do usuário: "))

                usuario = db.buscar_usuario(id_usuario)

                if usuario:
                    print(
                        f"Usuário: ID={usuario.id}, Nome={usuario.nome}, CPF={usuario.cpf}, Email={usuario.email}, Cartão={usuario.numero_cartao}")
                else:
                    print(f"Usuário com ID {id_usuario} não encontrado.")
            finally:
                db.fechar()
        elif choice == '3':
            db = BibliotecaDB()

            try:
                id_usuario = int(input("Digite o ID do usuário a ser atualizado: "))
                usuario = db.buscar_usuario(id_usuario)
                if usuario:
                    print(f"\nUsuário encontrado: {usuario.nome} (ID: {usuario.id})")
                    print("O que você gostaria de atualizar?")
                    print("1 - Nome")
                    print("2 - CPF")
                    print("3 - Email")
                    print("4 - Número do Cartão")
                    print("5 - Voltar")

                    update_choice = input("Escolha uma opção (1-5): ")

                    if update_choice == '1':
                        nome = input(f"Digite o novo nome (atual: {usuario.nome}): ")
                        usuario.nome = nome
                        db.salvar_usuario(usuario)
                        print(f"Nome atualizado para: {usuario.nome}")
                    elif update_choice == '2':
                        cpf = input(f"Digite o novo CPF (atual: {usuario.cpf}): ")
                        usuario.cpf = cpf
                        db.salvar_usuario(usuario)
                        print(f"CPF atualizado para: {usuario.cpf}")
                    elif update_choice == '3':
                        email = input(f"Digite o novo email (atual: {usuario.email}): ")
                        usuario.email = email
                        db.salvar_usuario(usuario)
                        print(f"Email atualizado para: {usuario.email}")
                    elif update_choice == '4':
                        numero_cartao = input(f"Digite o novo número do cartão (atual: {usuario.numero_cartao}): ")
                        usuario.numero_cartao = numero_cartao
                        db.salvar_usuario(usuario)
                        print(f"Número do cartão atualizado para: {usuario.numero_cartao}")
                    elif update_choice == '5':
                        print("Voltando ao menu...")
                        return  # This will exit the update process and go back to the previous menu
                    else:
                        print("Opção inválida.")
                else:
                    print(f"Usuário com ID {id_usuario} não encontrado.")
            finally:
                db.fechar()
        elif choice == '4':
            db = BibliotecaDB()

            try:
                usuarios = db.listar_usuarios()
                for usuario in usuarios:
                    print(
                        f"Usuário: ID={usuario.id}, Nome={usuario.nome}, CPF={usuario.cpf}, Email={usuario.email}, Cartão={usuario.numero_cartao}")
            finally:
                db.fechar()
        elif choice == '5':
            break
        else:
            print("Opção inválida. Tente novamente.")


def funcionario_crud():
    while True:
        print("\nSubmenu Funcionário:")
        print("1 - Criar Funcionário")
        print("2 - Buscar Funcionário Por ID")
        print("3 - Buscar Funcionário por Matrícula")
        print("4 - Voltar ao menu principal")

        choice = input("Escolha uma opção (1-4): ")

        if choice == '1':
            db = BibliotecaDB()

            try:
                global funcionario_id
                nome = input("Digite o nome do funcionário: ")
                cpf = input("Digite o CPF do funcionário: ")
                email = input("Digite o email do funcionário: ")
                matricula = input("Digite a matricula do funcionário: ")
                cargo = input("Digite o cargo do funcionário: ")

                func = Funcionario(funcionario_id, nome, cpf, email, matricula, cargo)
                db.salvar_funcionario(func)
                funcionario_id += 1
            finally:
                db.fechar()
                print(f"Funcionário {func.nome} (matrícula: {func.matricula}) salvo com sucesso!")
        elif choice == '2':
            db = BibliotecaDB()

            try:
                id = int(input("Digite o ID do funcionário: "))

                func = db.buscar_funcionario(id)
                print(f"Funcionário {func.nome}")

            finally:
                db.fechar()

        elif choice == '3':
            db = BibliotecaDB()
            try:
                matricula = input("Digite a matricula: ")

                func = db.buscar_funcionario_por_matricula(matricula)
                print(f"Funcionário {func.nome} Matricula {func.matricula}")
            finally:
                db.fechar()

        elif choice == '4':
            break
        else:
            print("Opção inválida. Tente novamente.")


def livro_crud():
    while True:
        print("\nSubmenu Livro:")
        print("1 - Criar Livro")
        print("2 - Buscar Livro por ID")
        print("3 - Buscar livro por ISBN")
        print("4 - Listar Livros Disponíveis")
        print("5 - Voltar ao menu principal")

        choice = input("Escolha uma opção (1-5): ")

        if choice == '1':
            db = BibliotecaDB()

            try:
                global livro_id
                titulo = input('Digite o titulo do livro: ')
                autor = input('Digite o nome do autor do livro: ')
                isbn = input('Digite o ISBN do livro: ')

                livro = Livro(livro_id, titulo, autor, isbn)
                db.salvar_livro(livro)
                livro_id += 1
                print (f"Livro {livro.titulo} cadastrado com sucesso")
            finally:
                db.fechar()
        elif choice == '2':
            db = BibliotecaDB()

            try:
                id = input('Digite o ID do livro')

                livro = db.buscar_livro(id)
                print(f'Livro {livro.titulo} encontrado')
            finally:
                db.fechar()

        elif choice == '3':
            db = BibliotecaDB()

            try:
                isbn = input('Digite o numero ISBN do livro: ')

                livro = db.buscar_livro_por_isbn(isbn)
                print(f"Livro {livro.titulo} encontrado")
            finally:
                db.fechar()
        elif choice == '4':
            db = BibliotecaDB()

            try:
                livros = db.listar_livros_disponiveis()
                for livro in livros:
                    print(
                        f"livros: ID={livro.id}, titulo={livro.titulo}, isbn={livro.isbn}, autor={livro.autor}")
            finally:
                db.fechar()
        elif choice == '5':
            break
        else:
            print("Opção inválida. Tente novamente.")


def emprestimo_crud():
    while True:
        print("\nSubmenu Empréstimo:")
        print("1 - Criar Empréstimo")
        print("2 - Buscar Empréstimo por ID")
        print("3 - Listar Empréstimos Ativos")
        print("4 - Voltar ao menu principal")

        choice = input("Escolha uma opção (1-5): ")

        if choice == '1':
            db = BibliotecaDB()

            try:
                global emprestimo_id
                id_usuario = int(input('Digite o ID do usuário: '))
                id_livro = int(input('Digite o ID do livro: '))

                usuario = db.buscar_usuario(id_usuario)
                livro = db.buscar_livro(id_livro)

                emprestimo = Emprestimo(emprestimo_id, usuario, livro)
                db.salvar_emprestimo(emprestimo)
                emprestimo_id += 1
                print(f"Empréstimo do livro {emprestimo.livro.titulo} ao usuário {emprestimo.usuario.nome} cadastrado com sucesso!")
            finally:
                db.fechar()
        elif choice == '2':
            db = BibliotecaDB()

            try:
                id = int(input("Digite o ID do empréstimo: "))
                emprestimo = db.buscar_emprestimo(id)

                print(f"Livro {emprestimo.livro.titulo} emprestado ao usuário {emprestimo.usuario.nome} na data {emprestimo.data_emprestimo}. Devolução presvista para {emprestimo.data_devolucao}.")
            finally:
                db.fechar()
        elif choice == '3':
            db = BibliotecaDB()

            try:
                emprestimos_ativos = db.listar_emprestimos_ativos()

                for emprestimo in emprestimos_ativos:
                    print(f"Livro {emprestimo.livro.titulo} emprestado ao usuário {emprestimo.usuario.nome} na data {emprestimo.data_emprestimo}. Devolução presvista para {emprestimo.data_devolucao}.")
            finally:
                db.fechar()
        elif choice == '4':
            break
        else:
            print("Opção inválida. Tente novamente.")

def main():
    while True:
        print("\nMenu:")
        print("1 - Usuário")
        print("2 - Funcionário")
        print("3 - Livro")
        print("4 - Empréstimo")
        print("5 - Sair")

        choice = input("Escolha uma opção (1-5): ")

        if choice == '1':
            usuario_crud()
        elif choice == '2':
            funcionario_crud()
        elif choice == '3':
            livro_crud()
        elif choice == '4':
            emprestimo_crud()
        elif choice == '5':
            print("Saindo... Até logo!")
            break  # Gracefully exit the loop and the program
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()