import pandas as pd
import sqlite3

# Parámetros
chunk_size = 10000
csv_file = 'ventas.csv'
db_file = 'ventas.db'

# Conexión a la base de datos
conn = sqlite3.connect(db_file)
cursor = conn.cursor()

# Crear tabla si no existe
cursor.execute('''
    CREATE TABLE IF NOT EXISTS ventas (
        id INTEGER PRIMARY KEY,
        fecha TEXT,
        producto TEXT,
        categoria TEXT,
        precio REAL,
        cantidad INTEGER,
        total REAL
    )
''')

# 🧹 Limpiar la tabla antes de insertar
cursor.execute('DELETE FROM ventas')
conn.commit()

# Cargar datos en chunks con codificación compatible
for chunk in pd.read_csv(csv_file, chunksize=chunk_size, encoding='latin1'):
    chunk.to_sql('ventas', conn, if_exists='append', index=False)

conn.close()
print("✅ Datos cargados exitosamente en la base de datos.")
