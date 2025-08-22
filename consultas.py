import sqlite3
import pandas as pd
conn = sqlite3.connect('ventas.db')


print(pd.read_sql_query('''
SELECT categoria, SUM(total) AS total_ventas
FROM ventas
GROUP BY categoria
''', conn))


print(pd.read_sql_query('''
SELECT producto, SUM(cantidad) AS unidades_vendidas
FROM ventas
GROUP BY producto
ORDER BY unidades_vendidas DESC
LIMIT 5
''', conn))


print(pd.read_sql_query('''
SELECT strftime('%Y-%m', fecha) AS mes, SUM(total) AS facturacion
FROM ventas
GROUP BY mes
ORDER BY facturacion DESC
LIMIT 1
''', conn))

conn.close()
