"""
Personas, modelos
"""

from collections import OrderedDict

from sqlalchemy import Column, Date, Enum, Integer, String
from sqlalchemy.orm import relationship

from lib.database import Base
from lib.universal_mixin import UniversalMixin


class Persona(Base, UniversalMixin):
    """Persona"""

    SEXO = [
        ("H", "Hombre"),
        ("M", "Mujer"),
    ]

    ESTADO_CIVIL = [
        ("C", "C: Casado"),
        ("D", "D: Divorciado"),
        ("S", "S: Soltero"),
        ("UL", "UL: Unión Libre"),
        ("V", "V: Viudo"),
    ]

    SITUACION = [
        ("A.D.", "A.D: Alta Definitiva"),
        ("A.I.", "A.I: Alta Interina"),
        ("A.D.(B)", "A.D.(B): Alta Definitiva con Beneficiarios"),
        ("A.D.C.S.", "A.D.C.S: Alta Definitiva Comisionada al Sindicato"),
        ("A.D.SUS", "A.D.SUS: Alta Defininitiva Suspendida"),
        ("A.S.", "A.S: Asimilado"),
        ("B", "B: Baja"),
        ("C.E.", "C.E: Comisión Especial"),
        ("L.G.", "L.G: Licenia por Gravidez"),
        ("L.S.G.S.", "L.S.G.S: Licencia Sin Goce de Sueldo"),
        ("L.P.O.P.C.", "L.P.O.P.C: Licencia Para Ocupar Puesto de Confianza"),
        ("V", "V: Vacante"),
        ("P", "P: Pensionado"),
    ]

    # Nombre de la tabla
    __tablename__ = "personas"

    # Clave primaria
    id = Column(Integer, primary_key=True)

    # Columnas
    nombres = Column(String(128), nullable=False)
    apellido_primero = Column(String(128), nullable=False)
    apellido_segundo = Column(String(128))
    numero_empleado = Column(Integer(), nullable=True, unique=True)
    rfc = Column(String(13), nullable=False)
    curp = Column(String(18), nullable=False, unique=True)
    email = Column(String(64))
    email_secundario = Column(String(64))
    situacion = Column(Enum(*OrderedDict(SITUACION), name="tipo_situacion", native_enum=False), index=False, nullable=True)
    sexo = Column(Enum(*OrderedDict(SEXO), name="tipo_sexo", native_enum=False), index=False, nullable=True)
    estado_civil = Column(Enum(*OrderedDict(ESTADO_CIVIL), name="estado_civil", native_enum=False), index=False, nullable=True)
    fecha_ingreso_gobierno = Column(Date())
    fecha_ingreso_pj = Column(Date())

    @property
    def nombre(self):
        """Junta nombres, apellido primero y apellido segundo"""
        return self.nombres + " " + self.apellido_primero + " " + self.apellido_segundo

    def __repr__(self):
        """Representación"""
        return f"<Persona {self.id}>"
