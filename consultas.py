conn = sqlite3.connect('ventas.db')

# a. Total de ventas por categoría
print(pd.read_sql_query('''
SELECT categoria, SUM(total) AS total_ventas
FROM ventas
GROUP BY categoria
''', conn))

# b. Top 5 productos más vendidos
print(pd.read_sql_query('''
SELECT producto, SUM(cantidad) AS unidades_vendidas
FROM ventas
GROUP BY producto
ORDER BY unidades_vendidas DESC
LIMIT 5
''', conn))

# c. Mes con mayor facturación
print(pd.read_sql_query('''
SELECT strftime('%Y-%m', fecha) AS mes, SUM(total) AS facturacion
FROM ventas
GROUP BY mes
ORDER BY facturacion DESC
LIMIT 1
''', conn))

conn.close()
