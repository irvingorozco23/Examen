from typing import List, Optional
from app.domain.core.models import paciente
from app.application.ports.patient_repository import PatientRepository


class PatientService:
   

    def __init__(self, patient_repository: PatientRepository):
        self.patient_repository = patient_repository

    def registrar_paciente(self, nombre: str, email: str) -> paciente:
       
        patient = paciente(nombre=nombre, email=email)
        return self.patient_repository.guardar(patient)

    def obtener_paciente(self, patient_id: str) -> Optional[paciente]:
      
        return self.patient_repository.buscar_por_id(patient_id)

    def listar_pacientes(self) -> List[paciente]:
      
        return self.patient_repository.buscar_todos()

    def actualizar_paciente(self, patient_id: str, nombre: Optional[str] = None, 
                           email: Optional[str] = None) -> Optional[paciente]:
        
        patient = self.patient_repository.buscar_por_id(patient_id)
        if not patient:
            return None

        if nombre:
            patient.nombre = nombre
        if email:
            patient.email = email
        return self.patient_repository.actualizar(patient)

    def eliminar_paciente(self, patient_id: str) -> bool:
        return self.patient_repository.borrar(patient_id)
