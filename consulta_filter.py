from configuracion import session
from crear_base_entidades import Carrera

print("--- CARRERAS QUE SE LLAMEN 'Ingeniería de Software' ---")
carreras = session.query(Carrera).filter(Carrera.nombre == "Ingeniería de Software").all()
for c in carreras:
    print(f"Carrera: {c.nombre} | Código: {c.codigo_interno}")