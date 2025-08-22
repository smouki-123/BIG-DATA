import csv
import random
from datetime import datetime, timedelta

productos = ['Auriculares', 'Camisa', 'Lámpara', 'Teclado', 'Pantalón', 'TV', 'Silla', 'Mouse', 'Zapatos', 'Celular']
categorias = {'Auriculares': 'Electrónica', 'Teclado': 'Electrónica', 'Mouse': 'Electrónica', 'TV': 'Electrónica',
              'Camisa': 'Ropa', 'Pantalón': 'Ropa', 'Zapatos': 'Ropa',
              'Lámpara': 'Hogar', 'Silla': 'Hogar', 'Celular': 'Electrónica'}

with open('ventas.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['id', 'fecha', 'producto', 'categoria', 'precio', 'cantidad', 'total'])

    start_date = datetime(2022, 1, 1)
    for i in range(1, 100001):
        producto = random.choice(productos)
        categoria = categorias[producto]
        fecha = (start_date + timedelta(days=random.randint(0, 730))).strftime('%Y-%m-%d')
        precio = round(random.uniform(10, 500), 2)
        cantidad = random.randint(1, 5)
        total = round(precio * cantidad, 2)
        writer.writerow([i, fecha, producto, categoria, precio, cantidad, total])
