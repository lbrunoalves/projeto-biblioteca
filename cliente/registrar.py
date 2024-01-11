from cliente.cliente_repositorio import clientes

id_atual = 1

def gerarCliente(nome: str):
    global id_atual
    id_atual += 1
    cliente = {
        "id": id_atual,
        "nome": nome,
        "livros": []
    }
    return cliente

def registrarCliente(nome):
    cliente = gerarCliente(nome)
    clientes.append(cliente)
    print('Cliente adicionado com sucesso!')

if __name__ == "__main__":
    registrarCliente("Thiago")
    print(clientes)