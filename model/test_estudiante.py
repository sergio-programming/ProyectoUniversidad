import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pytest
from database import getDatabaseConnection
from estudiante import Estudiante, EstudianteDao

def test_create_estudiante():
    estudiante = Estudiante(None, "Bryan", "Rodriguez", "1993-05-06", "M", "bryan.rodriguez@example.com", "3198806745", "Calle 75 # 83-24")
    EstudianteDao.create(estudiante)
    
    conexion = getDatabaseConnection()
    cursor = conexion.cursor()
    cursor.execute("SELECT *FROM estudiantes where nombre = 'Bryan'")
    result = cursor.fetchone()
    cursor.close()
    conexion.close()
    assert result is not None