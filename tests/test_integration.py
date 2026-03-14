import sqlite3 
from app import calcular_prioridad


def test_db_connection_and_ticket_creation():
    # configurar conexion  (integraion con la base de datos)
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()
    cursor.execute(
        'CREATE TABLE tickets (id INTEGER, ubicacion TEXT, prioridad TEXT)'
    )

    # logica de negocio + persistencia
    ubcacion = "laboratorio de redes"
    prioridad = calcular_prioridad(10)  # dos espacios antes del comentario

    cursor.execute(
        'INSERT INTO tickets (id, ubicacion, prioridad) VALUES (?, ? ,?)',
        (1, ubcacion, prioridad)
    )
    conn.commit()

    # verificacion (Assert)
    cursor.execute('SELECT priridad FROM tickets WHERE id=1')
    resultado = cursor.fetchone()

    assert resultado[0] == "prioridad alta"
    conn.close()
