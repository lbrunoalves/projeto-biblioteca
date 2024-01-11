from livro.livro_repositorio import livros
from livro.buscar_livro import buscarlivro
from livro.editar_livro import editarLivro
from livro.deletar_livro import deletarLivro
from livro.listar_livros import listarLivros
from livro.registrar import registrarLivro
from livro.emprestimo_devolucao_livro import *

def menuBiblioteca():
    while True:
        print('--- Menu Biblioteca ---')
        print('1 - Cadastrar livro')
        print('2 - Editar livro')
        print('3 - Removerlivro')
        print('4 - Buscar livro')
        print('5 - Listar todos os livros')
        print('6 - Sair')
        opcao = input('Selecione uma opção: ')
        if opcao == '1':
            livro = input("Digite o nome do livro: ")
            editora = input("Digite o nome da editora: ")
            registrarLivro(livro, editora)
        elif opcao == '2':
            id = int(input("Informe o ID do livro: "))
            titulo = input("Digite o novo Titulo: ")
            editora = input("Digite o nova Editora: ")
            disponivel = input("Qual a disponibilidade? "
                              "1 - True / 2 - False: ")
            if disponivel == "1":
                editarLivro(id, titulo, editora, True)
            else:
                editarLivro(id, titulo, editora, False)
        elif opcao == '3':
            id = int(input("Informe o ID do livro: "))
            deletarLivro(id)
        elif opcao == '4':
            id = int(input("Informe o ID do livro: "))
            print(buscarlivro(id))
        elif opcao == '5':
            listarLivros()
        elif opcao == '6':
            print('Programa finalizado')
            break
        else:
            print('Opção não é valida')


if __name__ == "__main__":
    menuBiblioteca()