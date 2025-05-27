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

# Consulta05
# 5.1 Obtener todos los cursos

cursos = session.query(Curso).all()

# 5.2 Realizar un ciclo repetitivo para obtener en cada iteración las entregas por cada curso (con otra consulta)
# y presentar el promedio de calificaciones de las entregas

for curso in cursos:
    promedio = session.query(func.avg(Entrega.calificacion))\
    .join(Tarea, Entrega.tarea_id == Tarea.id)\
    .filter(Tarea.curso_id == curso.id)\
    .scalar()

    print(f"Curso: {curso.titulo}, Promedio de calificaciones: {promedio}")
