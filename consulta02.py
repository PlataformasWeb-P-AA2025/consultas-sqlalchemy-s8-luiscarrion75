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

# Consulta02
# Todos los departamentos que tengan notas de entregas menores o iguales a 0.3 .
# En función de los departamentos, presentar el nombre del departamento
# y el número de cursos que tiene cada departamento

departamentos = session.query(
    Departamento.nombre,
    func.count(Curso.id).label("num_cursos") # 'func' permite usar funciones SQL como COUNT, AVG, SUM, etc
).join(Departamento.cursos)\
 .join(Curso.tareas)\
 .join(Tarea.entregas)\
 .filter(Entrega.calificacion <= 0.3)\
 .group_by(Departamento.id)\
 .all()

 # Se usa el group_by para agrupar por departamento para que COUNT funcione correctamente

for nombre, num_cursos in departamentos:
    print(f"Departamento: {nombre}, Cursos: {num_cursos}")

