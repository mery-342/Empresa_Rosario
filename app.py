import sqlite3

conn = sqlite3.connect("Empresa_Rosario.db")

conn.execute(
    """
    CREATE TABLE IF NOT EXISTS clientes(
        id INTEGER PRIMARY KEY,
        nombre VARCHAR(100),
        apellido VARCHAR(100),
        telefono VARCHAR(100),
        direccion VARCHAR(100)
    )
    """
)

conn.execute("DROP TABLE IF EXISTS detalle_ventas;")

conn.execute(
    """
    INSERT INTO clientes (nombre, apellido, telefono, direccion)
    VALUES ('Anastaria', 'Sanchez', '3241321', 'Avenida Rosario 123')
"""
)

conn.execute(
    """
    CREATE TABLE IF NOT EXISTS productos(
        id INTEGER PRIMARY KEY,
        NOMBRE_PRODUCTO VARCHAR(100),
        PRECIO_UNITARIO DECIMAL(10,3),
        STOCK INTEGER
    )
    """
)

conn.execute(
   """
    INSERT INTO productos (NOMBRE_PRODUCTO, PRECIO_UNITARIO, STOCK)
    VALUES ('Hojas Bon', 100.00, 20)
    """
)

conn.execute(
    """
    CREATE TABLE IF NOT EXISTS ventas(
        id INTEGER PRIMARY KEY,
        fecha_venta DATE,
        cliente_id INTEGER,
        FOREIGN KEY (cliente_id) REFERENCES clientes(id)
    )
    """
)

conn.execute(
   """
  INSERT INTO ventas (fecha_venta, cliente_id)
 VALUES ('2026-05-25', 6)
"""
)

conn.commit()


print ("\nclientes")
cursor = conn.execute("SELECT * FROM clientes")
for fila in cursor:
    print(fila)

print ("\nproductos")
cursor = conn.execute("SELECT * FROM productos")
for fila in cursor:
    print(fila)

print ("\nventas")
cursor = conn.execute("SELECT * FROM ventas")
for fila in cursor:
    print(fila)