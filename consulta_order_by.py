from configuracion import session
from crear_base_entidades import Profesor

print("--- PROFESORES ORDENADOS POR NOMBRE (A-Z) ---")
profesores = session.query(Profesor).order_by(Profesor.nombres_apellidos).all()
for p in profesores:
    print(f"Profesor: {p.nombres_apellidos}")