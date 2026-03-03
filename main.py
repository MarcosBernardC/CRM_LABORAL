import os
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from supabase import create_client, Client
from dotenv import load_dotenv

# Cargar variables de entorno del archivo .env
load_dotenv()

app = FastAPI(title="CRM Laboral API")

# Configurar CORS para que tu GitHub Pages pueda acceder
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # En producción, cámbialo por tu URL de GitHub Pages
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Conexión a Supabase
url: str = os.getenv("SUPABASE_URL")
key: str = os.getenv("SUPABASE_KEY")

if not url or not key:
    raise RuntimeError("Faltan las credenciales de Supabase en el archivo .env")

supabase: Client = create_client(url, key)

# Modelo de datos para las postulaciones
class Postulacion(BaseModel):
    empresa: str
    puesto: str
    plataforma: str  # Computrabajo, LinkedIn, etc.
    estado: str = "Pendiente"

@app.get("/")
def read_root():
    return {"message": "API del CRM Laboral de Marcos funcionando"}

@app.get("/postulaciones")
def listar_postulaciones():
    try:
        # Consulta a la tabla 'postulaciones' (asegúrate que se llame así en Supabase)
        response = supabase.table("postulaciones").select("*").execute()
        return response.data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/postulaciones")
def crear_postulacion(item: Postulacion):
    try:
        response = supabase.table("postulaciones").insert(item.dict()).execute()
        return response.data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))