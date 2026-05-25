from configuracion import session
from crear_base_entidades import Facultad, Carrera, Profesor, RecursoAcademico

def poblar_datos():
    print("Insertando datos de ejemplo...")

    # 1. Creamos las Facultades
    fac_sistemas = Facultad(nombre="Facultad de Sistemas", ubicacion="Bloque Alfa - Piso 2", decano="Ing. Carlos Mendoza")
    fac_medicina = Facultad(nombre="Facultad de Medicina", ubicacion="Bloque Beta - Piso 1", decano="Dra. María Espinoza")
    
    session.add_all([fac_sistemas, fac_medicina])
    session.commit() # Guardamos para generar sus IDs

    # 2. Creamos las Carreras conectadas a sus respectivas facultades
    carrera_tic = Carrera(nombre="Tecnologías de la Información", codigo_interno="TIC-001", facultad_id=fac_sistemas.id)
    carrera_soft = Carrera(nombre="Ingeniería de Software", codigo_interno="SOFT-002", facultad_id=fac_sistemas.id)
    carrera_enfermeria = Carrera(nombre="Enfermería", codigo_interno="ENF-003", facultad_id=fac_medicina.id)
    
    session.add_all([carrera_tic, carrera_soft, carrera_enfermeria])
    session.commit()

    # 3. Creamos los Profesores asignados a una carrera
    prof_shirley = Profesor(nombres_apellidos="Shirley Pilapanta", correo="shirley.pila@utpl.edu.ec", especialidad="Bases de Datos NoSQL", carrera_id=carrera_tic.id)
    prof_ramiro = Profesor(nombres_apellidos="Ramiro Morocho", correo="ramiro.morocho@utpl.edu.ec", especialidad="Desarrollo Web Back-End", carrera_id=carrera_soft.id)
    
    session.add_all([prof_shirley, prof_ramiro])
    session.commit()

    # 4. Creamos los Recursos Académicos subidos por los profesores
    recurso_1 = RecursoAcademico(titulo="Guía práctica de Modelado de Datos", fecha_publicacion="2026-05-15", tipo="PDF", url="https://utpl.edu/recursos/guia-modelado", profesor_id=prof_shirley.id)
    recurso_2 = RecursoAcademico(titulo="Video: Introducción a SQLAlchemy y SQLite", fecha_publicacion="2026-05-20", tipo="Video", url="https://utpl.edu/recursos/video-sqlalchemy", profesor_id=prof_ramiro.id)
    
    session.add_all([recurso_1, recurso_2])
    session.commit()

    print("¡Todos los datos han sido insertados con éxito en la base de datos!")

if __name__ == '__main__':
    poblar_datos()