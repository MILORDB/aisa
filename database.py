import os
import psycopg2
from psycopg2.extras import RealDictCursor
from datetime import datetime
import bcrypt
import json
import urllib.parse
import random
import string

DATABASE_URL = os.environ.get('DATABASE_URL', '')

def get_db():
    """Obtiene una conexión a PostgreSQL"""
    if not DATABASE_URL:
        raise Exception("DATABASE_URL no está configurada")
    
    url = DATABASE_URL.strip()
    if not url.startswith('postgresql://') and not url.startswith('postgres://'):
        url = 'postgresql://' + url
    
    parsed = urllib.parse.urlparse(url)
    
    try:
        conn = psycopg2.connect(
            host=parsed.hostname or 'localhost',
            port=parsed.port or 5432,
            database=parsed.path.lstrip('/') if parsed.path else '',
            user=parsed.username or '',
            password=parsed.password or '',
            sslmode='require'
        )
        return conn
    except Exception as e:
        print(f"❌ Error de conexión: {e}")
        raise

def init_db():
    """Inicializa la base de datos con PostgreSQL"""
    try:
        conn = get_db()
        cursor = conn.cursor()
        print("✅ Conectado a PostgreSQL")
    except Exception as e:
        print(f"❌ Error de conexión: {e}")
        return
    
    # Crear tablas aquí...
    # (Todas las tablas que ya tienes en tu database.py actual)
    
    conn.commit()
    conn.close()
    print("✅ Base de datos inicializada correctamente")

# El resto de las funciones de database.py van aquí...
# (Todas las funciones que ya tienes en tu database.py actual)
