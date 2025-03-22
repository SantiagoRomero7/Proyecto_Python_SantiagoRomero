def gestionar_productos(productos):
    while True:
        print("\n--- Gestión de Productos ---")
        print("1. Agregar Producto")
        print("2. Editar Producto")
        print("3. Eliminar Producto")
        print("4. Listar Productos")
        print("5. Volver")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            agregar_producto(productos)
        elif opcion == '2':
            editar_producto(productos)
        elif opcion == '3':
            eliminar_producto(productos)
        elif opcion == '4':
            listar_productos(productos)
        elif opcion == '5':
            break
        else:
            print("Opción no válida. Intente de nuevo.")

def agregar_producto(productos):
    codigo = input("Ingrese el código del producto: ")
    if codigo in productos:
        print("El código de producto ya existe.")
        return
    nombre = input("Ingrese el nombre del producto: ")
    categoria = input("Ingrese la categoría: ")
    descripcion = input("Ingrese la descripción: ")
    proveedor = input("Ingrese el proveedor: ")
    cantidad = int(input("Ingrese la cantidad en stock: "))
    precio_venta = float(input("Ingrese el precio de venta: "))
    precio_compra = float(input("Ingrese el precio de compra: "))

    productos[codigo] = {
        'nombre': nombre,
        'categoria': categoria,
        'descripcion': descripcion,
        'proveedor': proveedor,
        'cantidad': cantidad,
        'precio_venta': precio_venta,
        'precio_compra': precio_compra
    }
    print("Producto agregado exitosamente.")

def editar_producto(productos):
    codigo = input("Ingrese el código del producto a editar: ")
    if codigo not in productos:
        print("El código de producto no existe.")
        return

    print("Ingrese los nuevos datos (deje en blanco para no cambiar):")
    nombre = input(f"Nombre ({productos[codigo]['nombre']}): ") or productos[codigo]['nombre']
    categoria = input(f"Categoría ({productos[codigo]['categoria']}): ") or productos[codigo]['categoria']
    descripcion = input(f"Descripción ({productos[codigo]['descripcion']}): ") or productos[codigo]['descripcion']
    proveedor = input(f"Proveedor ({productos[codigo]['proveedor']}): ") or productos[codigo]['proveedor']
    cantidad = input(f"Cantidad en stock ({productos[codigo]['cantidad']}): ")
    cantidad = int(cantidad) if cantidad else productos[codigo]['cantidad']
    precio_venta = input(f"Precio de venta ({productos[codigo]['precio_venta']}): ")
    precio_venta = float(precio_venta) if precio_venta else productos[codigo]['precio_venta']
    precio_compra = input(f"Precio de compra ({productos[codigo]['precio_compra']}): ")
    precio_compra = float(precio_compra) if precio_compra else productos[codigo]['precio_compra']

    productos[codigo] = {
        'nombre': nombre,
        'categoria': categoria,
        'descripcion': descripcion,
        'proveedor': proveedor,
        'cantidad': cantidad,
        'precio_venta': precio_venta,
        'precio_compra': precio_compra
    }
    print("Producto editado exitosamente.")

def eliminar_producto(productos):
    codigo = input("Ingrese el código del producto a eliminar: ")
    if codigo not in productos:
        print("El código de producto no existe.")
        return

    del productos[codigo]
    print("Producto eliminado exitosamente.")

def listar_productos(productos):
    if not productos:
        print("No hay productos registrados.")
        return

    print("\n--- Lista de Productos ---")
    for codigo, info in productos.items():
        print(f"Código: {codigo}, Nombre: {info['nombre']}, Categoría: {info['categoria']}, "
              f"Proveedor: {info['proveedor']}, Cantidad: {info['cantidad']}, "
              f"Precio de Venta: {info['precio_venta']}, Precio de Compra: {info['precio_compra']}")