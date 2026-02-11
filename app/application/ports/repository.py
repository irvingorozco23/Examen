from abc import ABC, abstractmethod
from typing import List, Optional
from app.domain.core.models import paciente,Doctor


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
