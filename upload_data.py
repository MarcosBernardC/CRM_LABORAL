import os
import json
from dotenv import load_dotenv
from supabase import create_client, Client

# 1. Cargar credenciales desde el .env
load_dotenv()
url: str = os.getenv("SUPABASE_URL")
key: str = os.getenv("SUPABASE_KEY")

if not url or not key:
    raise RuntimeError("Error: No se encontraron las credenciales de Supabase.")

supabase: Client = create_client(url, key)

def ejecutar_carga_masiva():
    # 2. Localizar el archivo data_limpia.json dinámicamente
    # Esto busca en la carpeta 'data' que está en el mismo directorio que este script
    directorio_actual = os.path.dirname(os.path.abspath(__file__))
    ruta_json = os.path.join(directorio_actual, "data", "data_limpia.json")

    if not os.path.exists(ruta_json):
        print(f"❌ Error: El archivo {ruta_json} no existe.")
        return

    # 3. Leer la data limpia
    with open(ruta_json, "r", encoding="utf-8") as f:
        data_para_subir = json.load(f)

    print(f"⚡ Conectando a Supabase para cargar {len(data_para_subir)} registros...")

    try:
        # 4. Inserción masiva (Bulk Insert)
        # Al estar la tabla vacía, simplemente insertamos la lista completa
        response = supabase.table("postulaciones").insert(data_para_subir).execute()
        
        if response.data:
            print(f"✅ ¡Misión cumplida! {len(response.data)} postulaciones subidas a la nube.")
            print(f"📊 Primer registro cargado: {response.data[0]['empresa']} - {response.data[0]['puesto']}")

    except Exception as e:
        print(f"❌ Error crítico durante la carga: {e}")

if __name__ == "__main__":
    ejecutar_carga_masiva()