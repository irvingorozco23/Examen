from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel, EmailStr
from typing import Optional, List
from app.application.services.patient_service import PatientService
from app.application.services.doctor_service import DoctorService



class PatientRequest(BaseModel):
    nombre: str
    email: EmailStr


class PatientResponse(BaseModel):
    id: str
    nombre: str
    email: str
    fecha_creacion: Optional[str] = None

    class Config:
        from_attributes = True


class DoctorRequest(BaseModel):
    nombre: str
    especialidad: str
    email: Optional[EmailStr] = None


class DoctorResponse(BaseModel):
    id: str
    nombre: str
    especialidad: str
    email: Optional[str] = None
    
    fecha_creacion: Optional[str] = None

    class Config:
        from_attributes = True


class PatientController:
   

    def __init__(self, patient_service: PatientService):
        self.patient_service = patient_service
        self.router = APIRouter(prefix="/pacientes", tags=["Pacientes"])
        self._setup_routes()

    def _setup_routes(self):
        
        self.router.add_api_route("/", self.registrar_paciente, methods=["POST"])
        self.router.add_api_route("/{patient_id}", self.obtener_paciente, methods=["GET"])
        self.router.add_api_route("/", self.listar_pacientes, methods=["GET"])
        self.router.add_api_route("/{patient_id}", self.actualizar_paciente, methods=["PUT"])
        self.router.add_api_route("/{patient_id}", self.eliminar_paciente, methods=["DELETE"])

    async def registrar_paciente(self, patient_data: PatientRequest) -> PatientResponse:
        
        try:
            patient = self.patient_service.registrar_paciente(
                nombre=patient_data.nombre,
                email=patient_data.email
            )
            return PatientResponse(
                id=patient.id,
                nombre=patient.nombre,
                email=patient.email,
                fecha_creacion=patient.fecha_creacion.isoformat() if patient.fecha_creacion else None
            )
        except ValueError as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

    async def obtener_paciente(self, patient_id: str) -> PatientResponse:
        
        patient = self.patient_service.obtener_paciente(patient_id)
        if not patient:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Paciente no encontrado")
        
        return PatientResponse(
            id=patient.id,
            nombre=patient.nombre,
            email=patient.email,
            telefono=patient.telefono,
            fecha_creacion=patient.fecha_creacion.isoformat() if patient.fecha_creacion else None
        )

    async def listar_pacientes(self) -> List[PatientResponse]:
       
        patients = self.patient_service.listar_pacientes()
        return [
            PatientResponse(
                id=p.id,
                nombre=p.nombre,
                email=p.email,
                fecha_creacion=p.fecha_creacion.isoformat() if p.fecha_creacion else None
            )
            for p in patients
        ]

    async def actualizar_paciente(self, patient_id: str, patient_data: PatientRequest) -> PatientResponse:
       
        patient = self.patient_service.actualizar_paciente(
            patient_id=patient_id,
            nombre=patient_data.nombre,
            email=patient_data.email
        )
        if not patient:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Paciente no encontrado")
        
        return PatientResponse(
            id=patient.id,
            nombre=patient.nombre,
            email=patient.email,
            telefono=patient.telefono,
            fecha_creacion=patient.fecha_creacion.isoformat() if patient.fecha_creacion else None
        )

    async def eliminar_paciente(self, patient_id: str) -> dict:
        
        if not self.patient_service.eliminar_paciente(patient_id):
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Paciente no encontrado")
        return {"mensaje": "Paciente eliminado exitosamente"}


class DoctorController:
   

    def __init__(self, doctor_service: DoctorService):
        self.doctor_service = doctor_service
        self.router = APIRouter(prefix="/doctores", tags=["Doctores"])
        self._setup_routes()

    def _setup_routes(self):
        
        self.router.add_api_route("/", self.registrar_doctor, methods=["POST"])
        self.router.add_api_route("/{doctor_id}", self.obtener_doctor, methods=["GET"])
        self.router.add_api_route("/", self.listar_doctores, methods=["GET"])
        self.router.add_api_route("/especialidad/{especialidad}", self.buscar_por_especialidad, methods=["GET"])
        self.router.add_api_route("/{doctor_id}", self.actualizar_doctor, methods=["PUT"])
        self.router.add_api_route("/{doctor_id}", self.eliminar_doctor, methods=["DELETE"])

    async def registrar_doctor(self, doctor_data: DoctorRequest) -> DoctorResponse:
       
        try:
            doctor = self.doctor_service.registrar_doctor(
                nombre=doctor_data.nombre,
                especialidad=doctor_data.especialidad,
                email=doctor_data.email
            )
            return DoctorResponse(
                id=doctor.id,
                nombre=doctor.nombre,
                especialidad=doctor.especialidad,
                email=doctor.email,
                fecha_creacion=doctor.fecha_creacion.isoformat() if doctor.fecha_creacion else None
            )
        except ValueError as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

    async def obtener_doctor(self, doctor_id: str) -> DoctorResponse:
        
        doctor = self.doctor_service.obtener_doctor(doctor_id)
        if not doctor:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Doctor no encontrado")
        
        return DoctorResponse(
            id=doctor.id,
            nombre=doctor.nombre,
            especialidad=doctor.especialidad,
            email=doctor.email,
            fecha_creacion=doctor.fecha_creacion.isoformat() if doctor.fecha_creacion else None
        )

    async def listar_doctores(self) -> List[DoctorResponse]:
        
        doctors = self.doctor_service.listar_doctores()
        return [
            DoctorResponse(
                id=d.id,
                nombre=d.nombre,
                especialidad=d.especialidad,
                email=d.email,
                fecha_creacion=d.fecha_creacion.isoformat() if d.fecha_creacion else None
            )
            for d in doctors
        ]

    async def buscar_por_especialidad(self, especialidad: str) -> List[DoctorResponse]:
       
        doctors = self.doctor_service.buscar_por_especialidad(especialidad)
        return [
            DoctorResponse(
                id=d.id,
                nombre=d.nombre,
                especialidad=d.especialidad,
                email=d.email,
                fecha_creacion=d.fecha_creacion.isoformat() if d.fecha_creacion else None
            )
            for d in doctors
        ]

    async def actualizar_doctor(self, doctor_id: str, doctor_data: DoctorRequest) -> DoctorResponse:
        
        doctor = self.doctor_service.actualizar_doctor(
            doctor_id=doctor_id,
            nombre=doctor_data.nombre,
            especialidad=doctor_data.especialidad,
            email=doctor_data.email
        )
        if not doctor:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Doctor no encontrado")
        
        return DoctorResponse(
            id=doctor.id,
            nombre=doctor.nombre,
            especialidad=doctor.especialidad,
            email=doctor.email,
            fecha_creacion=doctor.fecha_creacion.isoformat() if doctor.fecha_creacion else None
        )

    async def eliminar_doctor(self, doctor_id: str) -> dict:
      
        if not self.doctor_service.eliminar_doctor(doctor_id):
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Doctor no encontrado")
        return {"mensaje": "Doctor eliminado exitosamente"}
