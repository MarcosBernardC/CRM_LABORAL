import os
from typing import List, Optional, Dict
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from supabase import create_client, Client
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

app = FastAPI(title="CRM Laboral API - Marcos Bernard")

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Conexión a Supabase
url: str = os.getenv("SUPABASE_URL")
key: str = os.getenv("SUPABASE_KEY")

if not url or not key:
    raise RuntimeError("Faltan las credenciales de Supabase en las variables de entorno")

supabase: Client = create_client(url, key)

# --- MODELOS DE DATOS (Esquemático del Circuito) ---

class EstrategiaItem(BaseModel):
    titulo: str
    contenido: str

class Postulacion(BaseModel):
    id: Optional[str] = None
    fecha_postulacion: Optional[str] = None
    empresa: str
    puesto: str
    modalidad: Optional[str] = "Híbrido"
    prioridad: Optional[str] = "Media"
    enlace_oferta: Optional[str] = "#"
    plataforma: Optional[str] = "Computrabajo"
    estado: Optional[str] = "Postulado"
    proyecto_detalle: Optional[str] = None
    stack_tecnico: List[str] = []
    estrategia: List[EstrategiaItem] = []
    notas_adicionales: List[str] = []

# --- RUTAS (Endpoints) ---

@app.get("/")
def read_root():
    return {"status": "online", "message": "Bernard I+D Lab API funcionando"}

@app.get("/postulaciones")
def listar_postulaciones():
    try:
        # Seleccionamos todo de la tabla postulaciones
        response = supabase.table("postulaciones").select("*").order("created_at", desc=True).execute()
        return response.data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/postulaciones")
def crear_postulacion(item: Postulacion):
    try:
        # Convertimos el modelo a diccionario para insertarlo en Supabase
        data = item.dict(exclude_none=True)
        response = supabase.table("postulaciones").insert(data).execute()
        return response.data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))