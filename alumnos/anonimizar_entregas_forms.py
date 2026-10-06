# -*- coding: utf-8 -*-
"""
===============================================================================
PIPELINE DE ANONIMIZACIÓN Y CORRECCIÓN CIEGA DE RETOS MANUSCRITOS
Políticas Sociolaborales y de Empleo (PSLL) · Universidad Pablo de Olavide
Profesor: Manuel A. Hidalgo Pérez
===============================================================================
Fase 1: Mapeo y censura de cabeceras de exámenes manuscritos de Microsoft Forms.
- Asigna Token Ciego único (DNI[-5:-1]) para cada estudiante.
- Aplica enmascaramiento opaco del 14% superior de cada imagen.
- Guarda imágenes en scratch/ciegas_sXX/{TOKEN}.jpg para evaluación 100% ciega.
===============================================================================
"""

import os
import re
import json
import argparse
import pandas as pd
from PIL import Image, ImageDraw

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(SCRIPT_DIR)
SCRATCH_DIR = os.path.join(BASE_DIR, "scratch")

import unicodedata

def strip_accents(s):
    if not s:
        return ""
    return ''.join(c for c in unicodedata.normalize('NFD', str(s)) if unicodedata.category(c) != 'Mn')

def calcular_token_ciego(dni):
    dni_str = str(dni).strip().zfill(8)
    return dni_str[-5:-1]

def censurar_cabecera_imagen(input_path, output_path, crop_pct=0.14):
    """Aplica una banda opaca sobre el porcentaje superior de la imagen para tapar nombres."""
    with Image.open(input_path) as img:
        img_rgb = img.convert("RGB")
        w, h = img_rgb.size
        cut_h = int(h * crop_pct)

        # Dibujar un recuadro opaco neutro con texto de token
        draw = ImageDraw.Draw(img_rgb)
        draw.rectangle([(0, 0), (w, cut_h)], fill=(240, 240, 240))
        draw.line([(0, cut_h), (w, cut_h)], fill=(17, 57, 39), width=max(2, int(w * 0.003)))

        # Guardar imagen procesada en alta calidad
        img_rgb.save(output_path, "JPEG", quality=90)

def procesar_anonimizacion(forms_dir, sesion_num=1):
    sesion_id = f"s{int(sesion_num):02d}"
    print("=" * 75)
    print(f"  ANONIMIZACIÓN CIEGA DE ENTREGAS · PSLL · SESIÓN {sesion_num:02d}")
    print("=" * 75)

    if not os.path.exists(forms_dir):
        print(f"[ERROR] El directorio especificado no existe: {forms_dir}")
        return

    # 1. Cargar censo de estudiantes
    censo_path = os.path.join(SCRIPT_DIR, "lista_alumnos.csv")
    if not os.path.exists(censo_path):
        print(f"[ERROR] No se encuentra el censo oficial en: {censo_path}")
        return

    df_censo = pd.read_csv(censo_path, sep=";")
    df_censo["id_norm"] = df_censo["id_norm"].astype(str).str.strip().str.zfill(8)
    df_censo["token"] = df_censo["id_norm"].apply(calcular_token_ciego)

    # 2. Localizar archivos en el directorio de Forms
    output_dir = os.path.join(SCRATCH_DIR, f"ciegas_{sesion_id}")
    os.makedirs(output_dir, exist_ok=True)

    # Recoger todas las imágenes
    image_extensions = (".jpg", ".jpeg", ".png", ".webp", ".heic")
    imagenes_encontradas = []
    
    for root, _, files in os.walk(forms_dir):
        for f in files:
            if f.lower().endswith(image_extensions):
                # Si es HEIC y ya existe su versión JPG en la misma carpeta, omitir el HEIC
                if f.lower().endswith(".heic") and os.path.exists(os.path.join(root, f[:-5] + ".jpg")):
                    continue
                imagenes_encontradas.append(os.path.join(root, f))

    print(f"[*] Total de imágenes encontradas en Forms: {len(imagenes_encontradas)}")

    mapeo_secreto = {}
    tokens_usados = {}
    procesadas = 0

    for img_path in sorted(imagenes_encontradas):
        filename = os.path.basename(img_path)
        f_clean = strip_accents(filename)
        
        best_match = None
        best_score = 0
        
        for _, row in df_censo.iterrows():
            nom = strip_accents(row['nombre'])
            ape = strip_accents(row['apellidos'])
            nom_parts = [w for w in re.findall(r'[a-z]+', nom) if len(w) > 2]
            ape_parts = [w for w in re.findall(r'[a-z]+', ape) if len(w) > 2]
            
            score = 0
            # Primer apellido: peso 6
            if len(ape_parts) > 0:
                p1 = ape_parts[0]
                if p1 in f_clean or (len(p1) >= 4 and p1[:4] in f_clean):
                    score += 6
            # Segundo apellido: peso 4
            if len(ape_parts) > 1:
                p2 = ape_parts[1]
                if p2 in f_clean or (len(p2) >= 4 and p2[:4] in f_clean):
                    score += 4
            # Nombre: peso 3
            for np in nom_parts:
                if np in f_clean or (len(np) >= 4 and np[:4] in f_clean):
                    score += 3
                    
            usr = str(row['username']).lower()
            dni = str(row['id_norm'])
            if usr in f_clean or dni in f_clean:
                score += 20
                
            if score > best_score:
                best_score = score
                best_match = row

        if best_match is not None and best_score >= 6:
            token = best_match["token"]
            idx = tokens_usados.get(token, 0) + 1
            tokens_usados[token] = idx
            
            suffix = f"_{idx}" if idx > 1 else ""
            ciego_name = f"{token}{suffix}.jpg"
            dest_img = os.path.join(output_dir, ciego_name)
            censurar_cabecera_imagen(img_path, dest_img, crop_pct=0.14)
            
            map_key = f"{token}{suffix}"
            mapeo_secreto[map_key] = {
                "token": token,
                "dni": best_match["id_norm"],
                "nombre_completo": best_match["nombre_completo"],
                "archivo_origen": filename,
                "archivo_ciego": ciego_name
            }
            procesadas += 1
            print(f"  [+] {filename} -> {ciego_name} ({best_match['nombre_completo']}) [score:{best_score}]")
        else:
            token_temp = f"UNK_{procesadas+1:03d}"
            ciego_name = f"{token_temp}.jpg"
            dest_img = os.path.join(output_dir, ciego_name)
            censurar_cabecera_imagen(img_path, dest_img, crop_pct=0.14)
            mapeo_secreto[token_temp] = {
                "token": token_temp,
                "dni": "DESCONOCIDO",
                "nombre_completo": "Sin coincidencia automática",
                "archivo_origen": filename,
                "archivo_ciego": ciego_name
            }
            procesadas += 1
            print(f"  [?] {filename} -> {ciego_name} (DESCONOCIDO)")

    # Guardar mapeo secreto en scratch (para re-asociar en fase 4)
    mapeo_path = os.path.join(SCRATCH_DIR, f"mapeo_ciego_{sesion_id}.json")
    with open(mapeo_path, "w", encoding="utf-8") as f:
        json.dump(mapeo_secreto, f, ensure_ascii=False, indent=2)

    print(f"[OK] {procesadas} imágenes anonimizadas y guardadas en: {output_dir}")
    print(f"[OK] Mapeo secreto confidencial guardado en: {mapeo_path}")
    print("=" * 75)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Anonimizador de exámenes de Microsoft Forms")
    parser.add_argument("--forms_dir", type=str, required=True, help="Ruta al directorio de Forms en OneDrive")
    parser.add_argument("--sesion", type=int, default=1, help="Número de sesión (ej: 1)")
    args = parser.parse_args()

    procesar_anonimizacion(args.forms_dir, args.sesion)
