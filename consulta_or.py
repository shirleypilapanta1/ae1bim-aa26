from configuracion import session
from crear_base_entidades import Facultad
from sqlalchemy import or_

print("--- FACULTADES EN EL BLOQUE ALFA O BETA ---")
facultades = session.query(Facultad).filter(
    or_(
        Facultad.ubicacion.like('%Alfa%'),
        Facultad.ubicacion.like('%Beta%')
    )
).all()

for f in facultades:
    print(f"Facultad: {f.nombre} | Ubicación: {f.ubicacion}")