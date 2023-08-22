"""
Entradas-Salidas v4, esquemas de pydantic
"""
from datetime import datetime

from pydantic import BaseModel, ConfigDict

from lib.schemas_base import OneBaseOut


class EntradaSalidaOut(BaseModel):
    """Esquema para entregar entradas-salidas"""

    id: int | None = None
    usuario_id: int | None = None
    usuario_email: str | None = None
    usuario_nombre: str | None = None
    tipo: str | None = None
    direccion_ip: str | None = None
    creado: datetime | None = None
    model_config = ConfigDict(from_attributes=True)


class OneEntradaSalidaOut(EntradaSalidaOut, OneBaseOut):
    """Esquema para entregar un entrada-salida"""
