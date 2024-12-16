# Clase base para manejo de datos (RegistroDatos)
class RegistroDatos:
    def __init__(self):
        self.datos = []

    def registrar(self, dato):
        self.datos.append(dato)
        print(f"Registrado: {dato}")

    def mostrar_datos(self):
        return self.datos

# Clase Cliente
class Cliente:
    def __init__(self, nombre, mesa):
        self.nombre = nombre
        self.mesa = mesa

    def __str__(self):
        return f"Cliente: {self.nombre}, Mesa: {self.mesa}"

# Clase Pedido (hereda RegistroDatos)
class Pedido(RegistroDatos):
    def __init__(self):
        super().__init__()

    def agregar_pedido(self, cliente, platillos):
        pedido = {
            "cliente": cliente,
            "platillos": platillos,
            "estado": "pendiente"
        }
        self.registrar(pedido)

# Clase Cocina
class Cocina:
    def __init__(self, pedidos):
        self.pedidos = pedidos

    def preparar_pedido(self, indice):
        try:
            pedido = self.pedidos[indice]
            if pedido['estado'] == 'pendiente':
                pedido['estado'] = 'preparado'
                print(f"\nPedido de {pedido['cliente']} ha sido PREPARADO.")
            else:
                print("\nEl pedido ya estaba preparado.")
        except IndexError:
            print("\n¡El índice del pedido no existe!")

# Clase Informe
class Informe:
    def __init__(self, pedidos):
        self.pedidos = pedidos

    def generar_informe(self):
        print("\n--- INFORME DE PEDIDOS ---")
        for i, pedido in enumerate(self.pedidos, start=1):
            print(f"{i}. Cliente: {pedido['cliente']}, Platillos: {pedido['platillos']}, Estado: {pedido['estado']}")

# Clase ControlPedidos (control de flujo)
class ControlPedidos:
    def __init__(self):
        self.pedidos = Pedido()

    def tomar_pedido(self, cliente, platillos):
        print(f"\nTomando pedido para {cliente}...")
        self.pedidos.agregar_pedido(cliente, platillos)

    def obtener_pedidos(self):
        return self.pedidos.mostrar_datos()

# Función principal
def main():
    # Crear sistema de pedidos
    control_pedidos = ControlPedidos()

    # Simulación de clientes y pedidos
    cliente1 = Cliente("Juan Pérez", 3)
    cliente2 = Cliente("María López", 5)

    control_pedidos.tomar_pedido(cliente1, ["Enchiladas", "Agua de Horchata"])
    control_pedidos.tomar_pedido(cliente2, ["Tacos al Pastor", "Refresco"])

    # Obtener lista de pedidos
    pedidos = control_pedidos.obtener_pedidos()

    # Cocina procesa los pedidos
    cocina = Cocina(pedidos)
    cocina.preparar_pedido(0)  # Preparar el primer pedido
    cocina.preparar_pedido(1)  # Preparar el segundo pedido

    # Generar informe final
    informe = Informe(pedidos)
    informe.generar_informe()

if __name__ == "__main__":
    main()
