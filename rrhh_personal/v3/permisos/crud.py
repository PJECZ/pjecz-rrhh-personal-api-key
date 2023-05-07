"""
Permisos v3, CRUD (create, read, update, and delete)
"""
from typing import Any

from sqlalchemy.orm import Session

from lib.exceptions import MyIsDeletedError, MyNotExistsError

from ...core.permisos.models import Permiso
from ..modulos.crud import get_modulo, get_modulo_by_nombre
from ..roles.crud import get_rol, get_rol_by_nombre


def get_permisos(
    db: Session,
    modulo_id: int = None,
    modulo_nombre: str = None,
    rol_id: int = None,
    rol_nombre: str = None,
) -> Any:
    """Consultar los permisos activos"""
    consulta = db.query(Permiso)
    if modulo_id is not None:
        modulo = get_modulo(db, modulo_id)
        consulta = consulta.filter(modulo == modulo)
    elif modulo_nombre is not None:
        modulo = get_modulo_by_nombre(db, modulo_nombre)
        consulta = consulta.filter(modulo == modulo)
    if rol_id is not None:
        rol = get_rol(db, rol_id)
        consulta = consulta.filter(rol == rol)
    elif rol_nombre is not None:
        rol = get_rol_by_nombre(db, rol_nombre)
        consulta = consulta.filter(rol == rol)
    return consulta.filter_by(estatus="A").order_by(Permiso.id)


def get_permiso(db: Session, permiso_id: int) -> Permiso:
    """Consultar un permiso por su id"""
    permiso = db.query(Permiso).get(permiso_id)
    if permiso is None:
        raise MyNotExistsError("No existe ese permiso")
    if permiso.estatus != "A":
        raise MyIsDeletedError("No es activo ese permiso, está eliminado")
    return permiso
