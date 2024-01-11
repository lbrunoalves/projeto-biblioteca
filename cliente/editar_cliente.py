from cliente.cliente_repositorio import clientes
from cliente.buscar_cliente import buscarCliente

def editarCliente(id, nome):
    cliente = buscarCliente(id)
    if cliente:
        cliente['nome'] = nome
        return cliente
    print('Cliente editado')

if __name__ == '__main__':
    print(clientes)
    editarCliente(1, "Thiago")
    print(clientes)
