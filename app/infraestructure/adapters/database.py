import uuid
from typing import List, Optional
from datetime import datetime
from app.domain.core.models import paciente, Doctor
from app.application.ports.patient_repository import PatientRepository
from app.application.ports.doctor_repository import DoctorRepository


class InMemoryPatientRepository(PatientRepository):
    

    def __init__(self):
        self.patients: dict[str, paciente] = {}

    def guardar(self, patient: paciente) -> paciente:
        
        if not patient.id:
            patient.id = str(uuid.uuid4())
        patient.fecha_creacion = datetime.now()
        self.patients[patient.id] = patient
        return patient

    def buscar_por_id(self, patient_id: str) -> Optional[paciente]:
        
        return self.patients.get(patient_id)

    def buscar_todos(self) -> List[paciente]:
       
        return list(self.patients.values())

    def actualizar(self, patient: paciente) -> paciente:
       
        if patient.id and patient.id in self.patients:
            self.patients[patient.id] = patient
            return patient
        return None

    def borrar(self, patient_id: str) -> bool:
        if patient_id in self.patients:
            del self.patients[patient_id]
            return True
        return False


class InMemoryDoctorRepository(DoctorRepository):
    

    def __init__(self):
        self.doctors: dict[str, Doctor] = {}

    def guardar(self, doctor: Doctor) -> Doctor:
        
        if not doctor.id:
            doctor.id = str(uuid.uuid4())
        doctor.fecha_creacion = datetime.now()
        self.doctors[doctor.id] = doctor
        return doctor

    def buscar_por_id(self, doctor_id: str) -> Optional[Doctor]:
        
        return self.doctors.get(doctor_id)

    def buscar_todos(self) -> List[Doctor]:
       
        return list(self.doctors.values())

    def buscar_por_especialidad(self, especialidad: str) -> List[Doctor]:
    
        return [doc for doc in self.doctors.values() 
                if doc.especialidad.lower() == especialidad.lower()]

    def actualizar(self, doctor: Doctor) -> Doctor:
        
        if doctor.id and doctor.id in self.doctors:
            self.doctors[doctor.id] = doctor
            return doctor
        return None

    def borrar(self, doctor_id: str) -> bool:
        
        if doctor_id in self.doctors:
            del self.doctors[doctor_id]
            return True
        return False
