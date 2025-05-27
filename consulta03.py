from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import func

# se importan las clases del 
# archivo clases.py
from clases import *

# se importa información del archivo configuracion
from config import cadena_base_datos

# se genera enlace al gestor de base de datos
# para el ejemplo se usa la base de datos sqlite
engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()

# Consulta03
# Obtener todas las tareas asignadas a los siguientes estudiantes 
# Jennifer Bolton 
# Elaine Perez
# Heather Henderson
# Charles Harris
# En función de cada tarea, presentar el número de entregas que tiene

# Se crea una lista nombres_estudiantes para que pueda ser iterable para el in_ 
# Y asi filtrar los nombres de los estudiantes

nombres_estudiantes = [
    'Jennifer Bolton',
    'Elaine Perez',
    'Heather Henderson',
    'Charles Harris'
]

tareas = session.query(
    Tarea.titulo,
    func.count(Entrega.id).label("num_entregas")
).join(Tarea.entregas)\
 .join(Entrega.estudiante)\
 .filter(Estudiante.nombre.in_(nombres_estudiantes))\
 .group_by(Tarea.id)\
 .all()

for titulo, num_entregas in tareas:
    print(f"Tarea: {titulo}, Numero de entregas: {num_entregas}")
