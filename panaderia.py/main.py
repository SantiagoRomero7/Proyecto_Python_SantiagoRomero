import json
from productos import gestionar_productos
from pedidos import gestionar_pedidos
from archivo import cargar_datos, guardar_datos

def main():
    # Cargar datos iniciales
    productos, pedidos = cargar_datos()

    while True:
        print("\n--- Sistema de Gestión de Panadería ---")
        print("1. Gestionar Productos")
        print("2. Gestionar Pedidos")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            gestionar_productos(productos)
        elif opcion == '2':
            gestionar_pedidos(pedidos, productos)
        elif opcion == '3':
            guardar_datos(productos, pedidos)
            print("Datos guardados. Saliendo...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()