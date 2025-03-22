def gestionar_pedidos(pedidos, productos):
    while True:
        print("\n--- Gestión de Pedidos ---")
        print("1. Crear Pedido")
        print("2. Editar Pedido")
        print("3. Eliminar Pedido")
        print("4. Listar Pedidos")
        print("5. Buscar Pedido")
        print("6. Volver")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            crear_pedido(pedidos, productos)
        elif opcion == '2':
            editar_pedido(pedidos, productos)
        elif opcion == '3':
            eliminar_pedido(pedidos)
        elif opcion == '4':
            listar_pedidos(pedidos)
        elif opcion == '5':
            buscar_pedido(pedidos)
        elif opcion == '6':
            break
        else:
            print("Opción no válida. Intente de nuevo.")

def crear_pedido(pedidos, productos):
    codigo_pedido = input("Ingrese el código del pedido: ")
    if codigo_pedido in pedidos:
        print("El código de pedido ya existe.")
        return

    codigo_cliente = input("Ingrese el código del cliente: ")
    fecha_pedido = input("Ingrese la fecha del pedido: ")
    detalles = []

    while True:
        codigo_producto = input("Ingrese el código del producto (o 'fin' para terminar): ")
        if codigo_producto.lower() == 'fin':
            break
        if codigo_producto not in productos:
            print("El código de producto no existe.")
            continue

        cantidad = int(input("Ingrese la cantidad: "))
        if cantidad > productos[codigo_producto]['cantidad']:
            print("No hay suficiente stock disponible.")
            continue

        precio_unitario = productos[codigo_producto]['precio_venta']
        detalles.append({
            'codigo_producto': codigo_producto,
            'cantidad': cantidad,
            'precio_unitario': precio_unitario,
            'linea': len(detalles) + 1
        })

        # Reducir el inventario
        productos[codigo_producto]['cantidad'] -= cantidad
        if productos[codigo_producto]['cantidad'] < 5:  # Umbral de alerta
            print(f"Alerta: El producto {codigo_producto} está por agotarse. Stock actual: {productos[codigo_producto]['cantidad']}")

    pedidos[codigo_pedido] = {
        'codigo_cliente': codigo_cliente,
        'fecha': fecha_pedido,
        'detalles': detalles
    }
    print("Pedido creado exitosamente.")

def editar_pedido(pedidos, productos):
    codigo_pedido = input("Ingrese el código del pedido a editar: ")
    if codigo_pedido not in pedidos:
        print("El código de pedido no existe.")
        return

    # Editar información del pedido
    print("Ingrese los nuevos datos (deje en blanco para no cambiar):")
    codigo_cliente = input(f"Código del cliente ({pedidos[codigo_pedido]['codigo_cliente']}): ") or pedidos[codigo_pedido]['codigo_cliente']
    fecha_pedido = input(f"Fecha del pedido ({pedidos[codigo_pedido]['fecha']}): ") or pedidos[codigo_pedido]['fecha']
    
    # Editar detalles del pedido
    detalles = pedidos[codigo_pedido]['detalles']
    nuevos_detalles = []

    while True:
        print("\nDetalles actuales del pedido:")
        for detalle in detalles:
            print(f"Línea: {detalle['linea']}, Producto: {detalle['codigo_producto']}, "
                  f"Cantidad: {detalle['cantidad']}, Precio Unitario: {detalle['precio_unitario']}")
        
        codigo_producto = input("Ingrese el código del producto a editar (o 'fin' para terminar): ")
        if codigo_producto.lower() == 'fin':
            break
        
        # Buscar el detalle correspondiente
        detalle_encontrado = next((d for d in detalles if d['codigo_producto'] == codigo_producto), None)
        if detalle_encontrado:
            nueva_cantidad = int(input(f"Cantidad actual ({detalle_encontrado['cantidad']}): ") or detalle_encontrado['cantidad'])
            if nueva_cantidad > productos[codigo_producto]['cantidad'] + detalle_encontrado['cantidad']:
                print("No hay suficiente stock disponible.")
                continue
            
            # Actualizar el detalle
            nuevos_detalles.append({
                'codigo_producto': codigo_producto,
                'cantidad': nueva_cantidad,
                'precio_unitario': detalle_encontrado['precio_unitario'],
                'linea': detalle_encontrado['linea']
            })
            # Ajustar el inventario
            productos[codigo_producto]['cantidad'] += detalle_encontrado['cantidad'] - nueva_cantidad
            if productos[codigo_producto]['cantidad'] < 5:
                print(f"Alerta: El producto {codigo_producto} está por agotarse. Stock actual: {productos[codigo_producto]['cantidad']}")
        else:
            print("El código de producto no está en el pedido.")

    # Actualizar el pedido con los nuevos detalles
    pedidos[codigo_pedido] = {
        'codigo_cliente': codigo_cliente,
        'fecha': fecha_pedido,
        'detalles': nuevos_detalles if nuevos_detalles else detalles  # Mantener detalles si no se editan
    }
    print("Pedido editado exitosamente.")

def eliminar_pedido(pedidos):
    codigo_pedido = input("Ingrese el código del pedido a eliminar: ")
    if codigo_pedido not in pedidos:
        print("El código de pedido no existe.")
        return

    del pedidos[codigo_pedido]
    print("Pedido eliminado exitosamente.")

def listar_pedidos(pedidos):
    if not pedidos:
        print("No hay pedidos registrados.")
        return

    print("\n--- Lista de Pedidos ---")
    for codigo, info in pedidos.items():
        print(f"Código: {codigo}, Cliente: {info['codigo_cliente']}, Fecha: {info['fecha']}")
        for detalle in info['detalles']:
            print(f"  Línea: {detalle['linea']}, Producto: {detalle['codigo_producto']}, "
                  f"Cantidad: {detalle['cantidad']}, Precio Unitario: {detalle['precio_unitario']}")

def buscar_pedido(pedidos):
    codigo_pedido = input("Ingrese el código del pedido a buscar: ")
    if codigo_pedido in pedidos:
        info = pedidos[codigo_pedido]
        print(f"Código: {codigo_pedido}, Cliente: {info['codigo_cliente']}, Fecha: {info['fecha']}")
        for detalle in info['detalles']:
            print(f"  Línea: {detalle['linea']}, Producto: {detalle['codigo_producto']}, "
                  f"Cantidad: {detalle['cantidad']}, Precio Unitario: {detalle['precio_unitario']}")
    else:
        print("El código de pedido no existe.")


# 
# Función para reducir el inventario
def reducir_inventario(productos, codigo_producto, cantidad):
    if codigo_producto in productos:
        productos[codigo_producto]['cantidad'] -= cantidad
        if productos[codigo_producto]['cantidad'] < 5:  # Umbral de alerta
            print(f"Alerta: El producto {codigo_producto} está por agotarse. Stock actual: {productos[codigo_producto]['cantidad']}")
    else:
        print("El código de producto no existe.")