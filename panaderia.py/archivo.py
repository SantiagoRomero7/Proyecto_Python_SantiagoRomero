import json

def cargar_datos():
    try:
        with open('data.json', 'r') as file:
            data = json.load(file)
            return data.get('productos', {}), data.get('pedidos', {})
    except FileNotFoundError:
        return {}, {}

def guardar_datos(productos, pedidos):
    data = {
        'productos': productos,
        'pedidos': pedidos
    }
    with open('data.json', 'w') as file:
        json.dump(data, file, indent=4)