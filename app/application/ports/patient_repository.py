from abc import ABC, abstractmethod
from typing import List, Optional
from app.domain.core.models import paciente


class PatientRepository(ABC):
    

    @abstractmethod
    def guardar(self, patient: paciente) -> paciente:
        
        pass

    @abstractmethod
    def buscar_por_id(self, patient_id: str) -> Optional[paciente]:
        
        pass

    @abstractmethod
    def buscar_todos(self) -> List[paciente]:
        
        pass

    @abstractmethod
    def actualizar(self, patient: paciente) -> paciente:
        pass

    @abstractmethod
    def borrar(self, patient_id: str) -> bool:
        pass
