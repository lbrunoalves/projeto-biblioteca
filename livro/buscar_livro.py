from livro.livro_repositorio import livros

def buscarlivro(id: int) -> dict or None:
    for livro in livros:
        if livro['id'] == id:
            return livro

if __name__ == "__main__":

    print(buscarlivro(1))
    print(buscarlivro(2))