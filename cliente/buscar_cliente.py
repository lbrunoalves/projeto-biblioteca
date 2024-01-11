from cliente.cliente_repositorio import clientes


def buscarCliente(id) -> dict or None:
    for cliente in clientes:
        if cliente['id'] == id:
            return cliente

if __name__ == "__main__":
    buscarCliente(1)