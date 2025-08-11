inventario = []

# Agregar 5 productos manualmente
inventario.append({"nombre": "Manzanas", "categoria": "Frutas", "cantidad": 10, "precio_unitario": 0.5})
inventario.append({"nombre": "Leche", "categoria": "Lácteos", "cantidad": 3, "precio_unitario": 1.2})
inventario.append({"nombre": "Pan", "categoria": "Panadería", "cantidad": 8, "precio_unitario": 1.5})
inventario.append({"nombre": "Huevos", "categoria": "Lácteos", "cantidad": 4, "precio_unitario": 0.2})
inventario.append({"nombre": "Arroz", "categoria": "Granos", "cantidad": 6, "precio_unitario": 1.0})

# Mostrar información de cada producto
producto1 = inventario[0]
valor_total1 = producto1["cantidad"] * producto1["precio_unitario"]
print(f"Nombre: {producto1['nombre']}, Categoría: {producto1['categoria']}, "
      f"Cantidad: {producto1['cantidad']}, Precio Unitario: {producto1['precio_unitario']}, "
      f"Valor Total: {valor_total1}")

producto2 = inventario[1]
valor_total2 = producto2["cantidad"] * producto2["precio_unitario"]
print(f"Nombre: {producto2['nombre']}, Categoría: {producto2['categoria']}, "
      f"Cantidad: {producto2['cantidad']}, Precio Unitario: {producto2['precio_unitario']}, "
      f"Valor Total: {valor_total2}")

producto3 = inventario[2]
valor_total3 = producto3["cantidad"] * producto3["precio_unitario"]
print(f"Nombre: {producto3['nombre']}, Categoría: {producto3['categoria']}, "
      f"Cantidad: {producto3['cantidad']}, Precio Unitario: {producto3['precio_unitario']}, "
      f"Valor Total: {valor_total3}")

producto4 = inventario[3]
valor_total4 = producto4["cantidad"] * producto4["precio_unitario"]
print(f"Nombre: {producto4['nombre']}, Categoría: {producto4['categoria']}, "
      f"Cantidad: {producto4['cantidad']}, Precio Unitario: {producto4['precio_unitario']}, "
      f"Valor Total: {valor_total4}")

producto5 = inventario[4]
valor_total5 = producto5["cantidad"] * producto5["precio_unitario"]
print(f"Nombre: {producto5['nombre']}, Categoría: {producto5['categoria']}, "
      f"Cantidad: {producto5['cantidad']}, Precio Unitario: {producto5['precio_unitario']}, "
      f"Valor Total: {valor_total5}")

# Calcular el valor total general del inventario
valor_total_general = valor_total1 + valor_total2 + valor_total3 + valor_total4 + valor_total5
print(f"Valor Total General del Inventario: {valor_total_general}")

# Indicar productos que necesitan reposición

if producto1["cantidad"] < 5:
    print(f"Producto que necesita reposición: {producto1['nombre']} (Cantidad: {producto1['cantidad']})")
if producto2["cantidad"] < 5:
    print(f"Producto que necesita reposición: {producto2['nombre']} (Cantidad: {producto2['cantidad']})")
if producto3["cantidad"] < 5:
    print(f"Producto que necesita reposición: {producto3['nombre']} (Cantidad: {producto3['cantidad']})")
if producto4["cantidad"] < 5:
    print(f"Producto que necesita reposición: {producto4['nombre']} (Cantidad: {producto4['cantidad']})")
if producto5["cantidad"] < 5:
    print(f"Producto que necesita reposición: {producto5['nombre']} (Cantidad: {producto5['cantidad']})")