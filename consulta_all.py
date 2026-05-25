from configuracion import session
from crear_base_entidades import Profesor

print("--- TODOS LOS PROFESORES ---")
profesores = session.query(Profesor).all()
for p in profesores:
    print(f"Profesor: {p.nombres_apellidos} | Correo: {p.correo} | Especialidad: {p.especialidad}")