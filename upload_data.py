import json
import os
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()
url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)

def transformar_dato(item):
    """
    Función de mapeo: convierte el JSON del frontend al esquema SQL.
    Es como un conversor de niveles lógicos.
    """
    return {
        # El ID lo dejamos fuera para que Supabase genere el UUID automático
        "empresa": item.get("empresa"),
        "puesto": item.get("puesto"),
        "plataforma": "Computrabajo", # O podrías extraerlo de la URL
        "estado": item.get("estado", "Enviada"),
        "enlace_oferta": item.get("url_vacante"),
        # Aquí empaquetamos todo lo extra en el campo 'notas'
        "notas": f"Proyecto: {item.get('proyecto_detalle')}\n" \
                 f"Stack: {', '.join(item.get('stack_tecnico', []))}\n" \
                 f"Notas: {' '.join(item.get('notas_adicionales', []))}"
    }

def upload_postulaciones():
    try:
        with open('data/postulaciones.json', 'r', encoding='utf-8') as f:
            raw_data = json.load(f)
        
        # Si raw_data es un solo objeto, lo metemos en una lista
        if isinstance(raw_data, dict):
            raw_data = [raw_data]

        # 4. Transformación de la data (Alineación de registros)
        cleaned_data = [transformar_dato(item) for item in raw_data]
        
        print(f"📡 Enviando {len(cleaned_data)} registros mapeados a Supabase...")
        
        # 5. Envío al puerto de salida
        supabase.table("postulaciones").insert(cleaned_data).execute()
        
        print("✅ ¡Éxito! Postulaciones cargadas. Ya puedes verlas en el Dashboard de Supabase.")
        
    except Exception as e:
        print(f"❌ Error en la transmisión: {e}")

if __name__ == "__main__":
    upload_postulaciones()