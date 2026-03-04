import os
from dotenv import load_dotenv
from supabase import create_client

# Carga las variables del .env
load_dotenv()

url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")

try:
    if not url or not key:
        print("❌ Error: No se encontraron las credenciales en el .env")
    else:
        supabase = create_client(url, key)
        print("🚀 ¡Conexión exitosa! Bernard I+D Lab está en la nube.")
except Exception as e:
    print(f"❌ Error de conexión: {e}")