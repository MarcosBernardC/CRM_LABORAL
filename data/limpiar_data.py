import json
import os
from datetime import datetime

# Diccionario para traducir meses de español a número
MESES = {
    "enero": "01", "febrero": "02", "marzo": "03", "abril": "04",
    "mayo": "05", "junio": "06", "julio": "07", "agosto": "08",
    "septiembre": "09", "octubre": "10", "noviembre": "11", "diciembre": "12"
}

def limpiar_fecha(fecha_str):
    # Convierte "02 de marzo de 2026" -> "2026-03-02"
    partes = fecha_str.lower().split(" de ")
    dia = partes[0].zfill(2)
    mes = MESES[partes[1]]
    anio = partes[2]
    return f"{anio}-{mes}-{dia}"

def transformar_data(archivo_json):
    with open(archivo_json, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    data_limpia = []
    
    for item in data:
        nuevo_item = {
            "empresa": item.get("empresa"),
            "puesto": item.get("puesto"),
            "modalidad": item.get("modalidad"),
            "url_vacante": item.get("url_vacante"), # Si hiciste el RENAME en SQL
            "fecha_postulacion": limpiar_fecha(item.get("fecha")),
            "proyecto_detalle": item.get("proyecto_detalle"),
            "stack_tecnico": item.get("stack_tecnico"),
            "estrategia_completa": item.get("estrategia_completa"),
            "notas_adicionales": item.get("notas_adicionales"),
            "prioridad": item.get("prioridad"),
            "cliente_sector": item.get("cliente_sector"),
            "verificado": item.get("verificado")
        }
        data_limpia.append(nuevo_item)
    
    return data_limpia

# Uso:
# postulaciones_listas = transformar_data("postulaciones.json")import json
from datetime import datetime

# Diccionario para traducir meses de español a número
MESES = {
    "enero": "01", "febrero": "02", "marzo": "03", "abril": "04",
    "mayo": "05", "junio": "06", "julio": "07", "agosto": "08",
    "septiembre": "09", "octubre": "10", "noviembre": "11", "diciembre": "12"
}

def limpiar_fecha(fecha_str):
    # Convierte "02 de marzo de 2026" -> "2026-03-02"
    partes = fecha_str.lower().split(" de ")
    dia = partes[0].zfill(2)
    mes = MESES[partes[1]]
    anio = partes[2]
    return f"{anio}-{mes}-{dia}"

def transformar_data(archivo_json):
    with open(archivo_json, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    data_limpia = []
    
    for item in data:
        nuevo_item = {
            "empresa": item.get("empresa"),
            "puesto": item.get("puesto"),
            "modalidad": item.get("modalidad"),
            "url_vacante": item.get("url_vacante"), # Si hiciste el RENAME en SQL
            "fecha_postulacion": limpiar_fecha(item.get("fecha")),
            "proyecto_detalle": item.get("proyecto_detalle"),
            "stack_tecnico": item.get("stack_tecnico"),
            "estrategia_completa": item.get("estrategia_completa"),
            "notas_adicionales": item.get("notas_adicionales"),
            "prioridad": item.get("prioridad"),
            "cliente_sector": item.get("cliente_sector"),
            "verificado": item.get("verificado")
        }
        data_limpia.append(nuevo_item)
    
    return data_limpia

def guardar_data_limpia(data, nombre_archivo="data_limpia.json"):
    try:
        with open(nombre_archivo, 'w', encoding='utf-8') as f:
            # indent=4 para que el JSON sea legible, ensure_ascii=False para las tildes
            json.dump(data, f, indent=4, ensure_ascii=False)
        print(f"✅ Proceso terminado. Archivo guardado como: {nombre_archivo}")
    except Exception as e:
        print(f"❌ Error al guardar: {e}")

# --- EJECUCIÓN DEL FLUJO ---
if __name__ == "__main__":
    # 1. Transformamos la data en memoria
    postulaciones_listas = transformar_data("postulaciones.json")
    
    # 2. La guardamos en un nuevo archivo físico
    guardar_data_limpia(postulaciones_listas)
# Uso:
# postulaciones_listas = transformar_data("postulaciones.json")