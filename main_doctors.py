from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.infraestructure.adapters.database import (
    InMemoryDoctorRepository
)
from app.application.services.doctor_service import DoctorService
from app.infraestructure.api.controller import DoctorController


app = FastAPI(
    title="Sistema de Gestión Clínico- Unach (Doctores)",
    description="API para gestionar doctores de una clínica el mejor de chiapas ",
    version="unica"
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


doctor_repository = InMemoryDoctorRepository()


doctor_service = DoctorService(doctor_repository)


doctor_controller = DoctorController(doctor_service)


app.include_router(doctor_controller.router)


@app.get("/", tags=["Root"])
async def read_root():
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


@app.get("/health", tags=["Health"])
async def health_check():
    """Verificar estado de la API"""
    return {
        "estado": "activo",
        "servicio": "Sistema de Gestión de Doctores"
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8002)
