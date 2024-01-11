from livro.livro_repositorio import livros
from livro.buscar_livro import buscarlivro

def deletarLivro(id: int):
    livro = buscarlivro(id)
    if livro:
        livros.remove(livro)
        print('Livro removido com sucesso!')
    else:
        print('Livro não encontrado!')

if __name__ == "__main__":
    print(livros)
    deletarLivro(1)
    print(livros)
