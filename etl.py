import sqlite3
import pandas as pd

# Conexión a la base de datos SQLite
conn = sqlite3.connect('ventas.db')
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
conn.commit()

# Cargar datos en chunks de 10,000 filas con codificación compatible
chunk_size = 10000
for chunk in pd.read_csv('ventas.csv', chunksize=chunk_size, encoding='latin1'):
    chunk.to_sql('ventas', conn, if_exists='append', index=False)

conn.close()
print("✅ Datos cargados exitosamente en la base de datos.")

