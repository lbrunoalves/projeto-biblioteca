from livro.livro_repositorio import livros

def listarLivros():
    print('--- Lista de livros ---')
    for livro in livros:
        print(f"Id: {livro['id']}")
        print(f"Titulo: {livro['titulo']}")
        print(f"Editora: {livro['editora']}")
        if livro['disponivel'] == True:
            print(f"Disponivel: Sim")
        else:
            print(f"Disponivel: Não")
        print("*"*50)

if __name__ == "__main__":
    listarLivros()