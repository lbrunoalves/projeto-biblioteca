from cliente.cliente_repositorio import clientes
from cliente.buscar_cliente import buscarCliente

def deletarCliente(id):
    cliente = buscarCliente(id)
    clientes.remove(cliente)
    print("Cliente removido com sucesso")

if __name__ == '__main__':
    print(clientes)
    deletarCliente(1)
    print(clientes)
