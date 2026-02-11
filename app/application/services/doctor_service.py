from typing import List, Optional
from app.domain.core.models import Doctor
from app.application.ports.doctor_repository import DoctorRepository


class DoctorService:
    

    def __init__(self, doctor_repository: DoctorRepository):
        self.doctor_repository = doctor_repository

    def registrar_doctor(self, nombre: str, especialidad: str, 
                        email: Optional[str] = None) -> Doctor:
        
        doctor = Doctor(nombre=nombre, especialidad=especialidad, email=email)
        return self.doctor_repository.guardar(doctor)

    def obtener_doctor(self, doctor_id: str) -> Optional[Doctor]:
       
        return self.doctor_repository.buscar_por_id(doctor_id)

    def listar_doctores(self) -> List[Doctor]:
        
        return self.doctor_repository.buscar_todos()

    def buscar_por_especialidad(self, especialidad: str) -> List[Doctor]:
        
        return self.doctor_repository.buscar_por_especialidad(especialidad)

    def actualizar_doctor(self, doctor_id: str, nombre: Optional[str] = None, 
                         especialidad: Optional[str] = None, email: Optional[str] = None) -> Optional[Doctor]:

        doctor = self.doctor_repository.buscar_por_id(doctor_id)
        if not doctor:
            return None

        if nombre:
            doctor.nombre = nombre
        if especialidad:
            doctor.especialidad = especialidad
        if email:
            doctor.email = email
        
        return self.doctor_repository.actualizar(doctor)

    def eliminar_doctor(self, doctor_id: str) -> bool:
    
        return self.doctor_repository.borrar(doctor_id)
