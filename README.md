# - Título del Proyecto
**Sistema de Gestión para Panadería**

## - Descripción del Proyecto
Este proyecto implementa un sistema de gestión para una panadería, permitiendo un manejo eficiente de productos, pedidos y detalles asociados. Su objetivo es optimizar el control de inventario, mejorar la gestión de pedidos y garantizar un mejor servicio al cliente.

## - ¿Qué hace el proyecto?
El sistema permite:
- Registrar productos de panadería como panes, pasteles y postres.
- Administrar pedidos de clientes y gestionar detalles específicos de cada pedido.
- Automatizar la actualización del inventario con cada venta.
- Facilitar búsquedas y consultas de productos y pedidos.
- Almacenar datos de manera persistente mediante archivos JSON.

## - ¿Por qué este proyecto es útil?
Este sistema digitaliza la administración de una panadería, reduciendo errores humanos y optimizando el proceso de gestión de inventario y pedidos, lo que mejora la eficiencia operativa y la experiencia del cliente.

## - ¿Qué problema resuelve?
Resuelve la falta de un sistema centralizado para la gestión de productos y pedidos, evitando pérdidas de datos y dificultades en el seguimiento de los pedidos.

---

## - Instalación

### - Requisitos previos
- Tener Python instalado (versión 3.x recomendada).
- Librerías necesarias (pueden instalarse con `requirements.txt` si es necesario).

### - Pasos de instalación
```sh
# Clonar el repositorio
git clone https://github.com/SantiagoRomero7/gestion-panaderia.git
cd gestion-panaderia

# Crear un entorno virtual
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt
```

---

## - Uso

Para ejecutar el sistema, usa el siguiente comando:
```sh
python main.py
```

### - Funcionalidades principales
- **Gestión de Productos:** Registro y administración de productos con detalles como categoría, proveedor, stock y precios.
- **Gestión de Pedidos:** Creación, edición y eliminación de pedidos de clientes.
- **Inventario Automatizado:** Reducción automática de stock cuando se procesan pedidos y alertas cuando un producto está por agotarse.
- **Consultas y Búsquedas:** Búsqueda de productos por nombre, categoría o código, y filtrado de pedidos por distintos criterios.
- **Manejo de Archivos y Persistencia:** Almacenamiento de datos en archivos JSON para garantizar su persistencia.

---

## - ¿Qué aprendió el desarrollador?
Este proyecto permitió profundizar en:
- Manejo de estructuras de datos en JSON.
- Organización modular del código para gestión eficiente de productos y pedidos.
- Validaciones de datos y control de inventario automatizado.

---

## - Mantenimiento y Créditos
- **Santiago Romero** - [GitHub](https://github.com/SantiagoRomero7)

## - GitHub
Repositorio: [Sistema de Gestión para Panadería](https://github.com/SantiagoRomero7/gestion-panaderia)
