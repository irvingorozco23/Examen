

import uvicorn
import threading
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.infraestructure.adapters.database import (
    InMemoryPatientRepository,
    InMemoryDoctorRepository
)
from app.application.services.patient_service import PatientService
from app.application.services.doctor_service import DoctorService
from app.infraestructure.api.controller import PatientController, DoctorController


# Aplicación de Pacientes
app_patients = FastAPI(
    title="Sistema de Gestión Clínico- Unach (Pacientes)",
    description="API para gestionar pacientes de una clínica el mejor de chiapas ",
    version="unica"
)

app_patients.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

patient_repository = InMemoryPatientRepository()
patient_service = PatientService(patient_repository)
patient_controller = PatientController(patient_service)

app_patients.include_router(patient_controller.router)

@app_patients.get("/", tags=["Root"])
async def read_root_patients():
    """Endpoint raíz con información de la API"""
    return {
        "mensaje": "Bienvenido al Sistema de Gestión de Pacientes",
        "versión": "1.0.0",
        "puerto": 8001,
        "endpoints": {
            "pacientes": "/pacientes",
            "documentación": "/docs"
        }
    }

@app_patients.get("/health", tags=["Health"])
async def health_check_patients():
    """Verificar estado de la API"""
    return {
        "estado": "activo",
        "servicio": "Sistema de Gestión de Pacientes"
    }


# Aplicación de Doctores
app_doctors = FastAPI(
    title="Sistema de Gestión Clínico- Unach (Doctores)",
    description="API para gestionar doctores de una clínica el mejor de chiapas ",
    version="unica"
)

app_doctors.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

doctor_repository = InMemoryDoctorRepository()
doctor_service = DoctorService(doctor_repository)
doctor_controller = DoctorController(doctor_service)

app_doctors.include_router(doctor_controller.router)

@app_doctors.get("/", tags=["Root"])
async def read_root_doctors():
    """Endpoint raíz con información de la API"""
    return {
        "mensaje": "Bienvenido al Sistema de Gestión de Doctores",
        "versión": "1.0.0",
        "puerto": 8002,
        "endpoints": {
            "doctores": "/doctores",
            "documentación": "/docs"
        }
    }

@app_doctors.get("/health", tags=["Health"])
async def health_check_doctors():
    """Verificar estado de la API"""
    return {
        "estado": "activo",
        "servicio": "Sistema de Gestión de Doctores"
    }


if __name__ == "__main__":
    # Ejecutar ambas aplicaciones en paralelo
    def run_patients():
        uvicorn.run(app_patients, host="0.0.0.0", port=8001, log_level="info")
    
    def run_doctors():
        uvicorn.run(app_doctors, host="0.0.0.0", port=8002, log_level="info")
    
    thread_patients = threading.Thread(target=run_patients, daemon=True)
    thread_doctors = threading.Thread(target=run_doctors, daemon=True)
    
    thread_patients.start()
    thread_doctors.start()
    
    thread_patients.join()
    thread_doctors.join()
