import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from database import getDatabaseConnection
from model.estudiante import Estudiante, EstudianteDao

@pytest.fixture
def db_connection():
    """Fixture para manejar la conexión a la base de datos."""
    conexion = getDatabaseConnection()
    cursor = conexion.cursor()
    yield cursor  # Devuelve el cursor para usarlo en la prueba
    conexion.rollback()  # Deshace los cambios después de la prueba
    cursor.close()
    conexion.close()

def test_create_estudiante(db_connection):
    estudiante = Estudiante(None, "Lucia", "Caceres", "1991-12-04", "F", "lucia.caceres@example.com", "3152234560", "Carrera 90 # 102-34")

    # Intentar crear el estudiante
    try:
        EstudianteDao.create(estudiante)
    except Exception as e:
        pytest.fail(f"Error al crear estudiante: {e}")

    # Verificar que el estudiante fue insertado
    db_connection.execute("SELECT * FROM estudiantes WHERE nombre = 'Lucia'")
    result = db_connection.fetchone()
    assert result is not None, "El estudiante no fue encontrado en la base de datos"