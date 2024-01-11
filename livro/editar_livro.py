from livro.livro_repositorio import livros
from livro.buscar_livro import buscarlivro

def editarLivro(id: int, titulos: str, editora: str, disponivel: bool):
    livro = buscarlivro(id)
    if livro:
        livro['titulo'] = titulos
        livro['editora'] = editora
        livro['disponivel'] = disponivel
        print('Dados alterados com sucesso!')
        return
    print('Erro: Livro não encontrado!')

if __name__ == "__main__":
    editarLivro(1, "Harry potter III", "infinity", False)
    print(livros)