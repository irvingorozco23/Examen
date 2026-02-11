from abc import ABC, abstractmethod
from typing import List, Optional
from app.domain.core.models import Doctor


class DoctorRepository(ABC):
    

    @abstractmethod
    def guardar(self, doctor: Doctor) -> Doctor:
        
        pass

    @abstractmethod
    def buscar_por_id(self, doctor_id: str) -> Optional[Doctor]:
        
        pass

    @abstractmethod
    def buscar_todos(self) -> List[Doctor]:
        
        pass

    @abstractmethod
    def buscar_por_especialidad(self, especialidad: str) -> List[Doctor]:
        
        pass

    @abstractmethod
    def actualizar(self, doctor: Doctor) -> Doctor:
        
        pass

    @abstractmethod
    def borrar(self, doctor_id: str) -> bool:
        
        pass
