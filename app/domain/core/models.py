from dataclasses import dataclass
from typing import Optional
from datetime import datetime


@dataclass
class paciente:
    
    id: Optional[str] = None
    nombre: str = ""
    email: str = ""
    fecha_creacion: Optional[datetime] = None

    def __post_init__(self):
        if not self.nombre:
            raise ValueError("El nombre del paciente es requerido")
        if not self.email:
            raise ValueError("El email del paciente es requerido")


@dataclass
class Doctor:
    """Modelo de dominio para Doctor"""
    id: Optional[str] = None
    nombre: str = ""
    especialidad: str = ""
    email: Optional[str] = None
    fecha_creacion: Optional[datetime] = None

    def __post_init__(self):
        if not self.nombre:
            raise ValueError("El nombre del doctor es requerido")
        if not self.especialidad:
            raise ValueError("La especialidad del doctor es requerida")
