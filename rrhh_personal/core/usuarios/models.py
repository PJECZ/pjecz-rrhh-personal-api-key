"""
Usuarios, modelos
"""
from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.orm import relationship

from lib.database import Base
from lib.universal_mixin import UniversalMixin

from ..permisos.models import Permiso


class Usuario(Base, UniversalMixin):
    """Usuario"""

    # Nombre de la tabla
    __tablename__ = "usuarios"

    # Clave primaria
    id = Column(Integer, primary_key=True)

    # Columnas
    email = Column(String(256), nullable=False, unique=True, index=True)
    nombres = Column(String(256), nullable=False)
    apellido_primero = Column(String(256), nullable=False)
    apellido_segundo = Column(String(256))
    curp = Column(String(18))
    puesto = Column(String(256))
    telefono = Column(String(48), nullable=False)
    extension = Column(String(24), nullable=False)

    # Columnas que no deben ser expuestas
    api_key = Column(String(128), nullable=False)
    api_key_expiracion = Column(DateTime(), nullable=False)
    contrasena = Column(String(256), nullable=False)

    # Hijos
    bitacoras = relationship("Bitacora", back_populates="usuario")
    entradas_salidas = relationship("EntradaSalida", back_populates="usuario")
    usuarios_acciones = relationship("UsuarioAccion", back_populates="usuario")
    usuarios_roles = relationship("UsuarioRol", back_populates="usuario")

    # Propiedades
    permisos_consultados = {}

    @property
    def nombre(self):
        """Junta nombres, apellido_paterno y apellido materno"""
        return self.nombres + " " + self.apellido_paterno + " " + self.apellido_materno

    @property
    def permissions(self):
        """Entrega un diccionario con todos los permisos"""
        if len(self.permisos_consultados) > 0:
            return self.permisos_consultados
        self.permisos_consultados = {}
        for usuario_rol in self.usuarios_roles:
            if usuario_rol.estatus == "A":
                for permiso in usuario_rol.rol.permisos:
                    if permiso.estatus == "A":
                        etiqueta = permiso.modulo.nombre
                        if etiqueta not in self.permisos_consultados or permiso.nivel > self.permisos_consultados[etiqueta]:
                            self.permisos_consultados[etiqueta] = permiso.nivel
        return self.permisos_consultados

    def can(self, modulo_nombre: str, permission: int):
        """¿Tiene permiso?"""
        if modulo_nombre in self.permisos:
            return self.permisos[modulo_nombre] >= permission
        return False

    def can_view(self, modulo_nombre: str):
        """¿Tiene permiso para ver?"""
        return self.can(modulo_nombre, Permiso.VER)

    def can_edit(self, modulo_nombre: str):
        """¿Tiene permiso para editar?"""
        return self.can(modulo_nombre, Permiso.MODIFICAR)

    def can_insert(self, modulo_nombre: str):
        """¿Tiene permiso para agregar?"""
        return self.can(modulo_nombre, Permiso.CREAR)

    def can_admin(self, modulo_nombre: str):
        """¿Tiene permiso para administrar?"""
        return self.can(modulo_nombre, Permiso.ADMINISTRAR)

    def __repr__(self):
        """Representación"""
        return f"<Usuario {self.email}>"
