from configuracion import session
from crear_base_entidades import RecursoAcademico
from sqlalchemy import and_

print("--- RECURSOS QUE SEAN PDF Y DEL AÑO 2026 ---")
recursos = session.query(RecursoAcademico).filter(
    and_(
        RecursoAcademico.tipo == 'PDF',
        RecursoAcademico.fecha_publicacion.like('2026%')
    )
).all()

for r in recursos:
    print(f"Recurso: {r.titulo} | Tipo: {r.tipo} | Fecha: {r.fecha_publicacion}")