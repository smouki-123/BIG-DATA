import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

conn = sqlite3.connect('ventas.db')
df = pd.read_sql_query('''
SELECT categoria, SUM(total) AS total_ventas
FROM ventas
GROUP BY categoria
''', conn)

plt.bar(df['categoria'], df['total_ventas'], color='skyblue')
plt.title('Total de ventas por categoría')
plt.xlabel('Categoría')
plt.ylabel('Ventas ($)')
plt.tight_layout()
plt.savefig('grafico_ventas_categoria.png')
plt.show()
conn.close()
