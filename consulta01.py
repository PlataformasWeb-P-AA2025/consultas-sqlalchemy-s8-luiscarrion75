from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_

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

# Consulta01
# Obtener las entregas de todos los estudiantes que pertenecen al departamento de Arte. 
# En función de la entrega, presentar, nombre del tarea, nombre del estudiante, 
# calificación, nombre de instructor y nombre del departamento

# Se hace session.query para poder acceder a la clase Entrega
# Se arma un camino para poder llegar hacia Departamento donde filtramos el valor de ARTE
entregas = session.query(Entrega)\
    .join(Entrega.tarea)\
    .join(Tarea.curso)\
    .join(Curso.departamento)\
    .join(Curso.instructor)\
    .join(Entrega.estudiante)\
    .filter(Departamento.nombre == 'Arte')\
    .all()

# Se recorre entregas para poder presentar los datos en la terminal
for entrega in entregas:
    print(f"Tarea: {entrega.tarea.titulo}, Estudiante: {entrega.estudiante.nombre}, "
          f"Calificación: {entrega.calificacion}, Instructor: {entrega.tarea.curso.instructor.nombre}, "
          f"Departamento: {entrega.tarea.curso.departamento.nombre}")

