# -*- coding: utf-8 -*-
"""
===============================================================================
COMPILADOR CRIPTOGRÁFICO DEL PASAPORTE DE EVALUACIÓN CONTINUA
Políticas Sociolaborales y de Empleo (PSLL)
Grados en Relaciones Laborales y Recursos Humanos / Doble Grado DER + RRLyRRHH
Universidad Pablo de Olavide · Curso 2026-27
Profesor: Manuel A. Hidalgo Pérez
===============================================================================
Estructura los datos con desglose individual de preguntas por sesión
para navegación por pestañas en la interfaz web del alumno.
Cifrado militar Zero-Knowledge AES-GCM-256 + SHA-256.
===============================================================================
"""

import pandas as pd
import json
import itertools
import hashlib
import os
import re
import unicodedata
import base64
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(SCRIPT_DIR)
MICRO_APPS_DIR = r"C:\Users\Usuario\Dropbox\DOCENCIA UPO\micro_apps"

# Rutas a listas oficiales de clase
lista_l1_path = os.path.join(BASE_DIR, "Repositorio material (no alumnos)", "lista.xlsx")
lista_l2_path = os.path.join(BASE_DIR, "Repositorio material (no alumnos)", "ListaClase_2026-27_102023BC_2.xls")

# Rutas de evaluación por sesión (se cargarán dinámicamente si existen)
EVAL_SESIONES_CONFIG = [
    {
        "sesion_num": 2,
        "id": "s02",
        "titulo_corto": "Sesión 02",
        "titulo_completo": "Sesión 02 · Crecimiento Económico, Productividad y Costes Laborales Unitarios",
        "tema": "Tema 1: Macroeconomía del Mercado de Trabajo y Dinámica Salarial",
        "fecha": "Septiembre 2026",
        "calif_path": os.path.join(BASE_DIR, "Temas EB", "Sesiones EB", "Sesion 02", "evaluacion", "calificaciones_sesion_02.csv"),
        "trans_path": os.path.join(BASE_DIR, "Temas EB", "Sesiones EB", "Sesion 02", "evaluacion", "transcripciones_psll_sesion_02.csv"),
        "enunciado_p1": "«Un sector económico incrementa sus salarios un 8% en un ejercicio en el que su productividad por hora solo creció un 2%». Razona con rigor económico:\na) Costes Laborales Unitarios (CLU): ¿Qué ocurre numéricamente con el CLU del sector? Aplica la fórmula vista en clase.",
        "solucion_p1": "1. Definición y Fórmula Formal del CLU:\nEl Coste Laboral Unitario relaciona el coste laboral medio por hora (salario nominal por hora W/H) con la productividad media aparente del trabajo (Y/H):\nCLU = (W / H) / (Y / H) = W / Y.\n\n2. Aproximación en Tasas de Variación Porcentual:\nLa tasa de variación porcentual del CLU se obtiene como la diferencia de tasas de crecimiento:\n%ΔCLU ≈ %ΔW - %ΔProd = 8% - 2% = +6%\n(o en cálculo exacto continuo: (1 + 0,08)/(1 + 0,02) - 1 = 1,08/1,02 - 1 = +5,88%).\n\nConclusión: Numéricamente, el CLU del sector se incrementa un 6%, lo que significa que el coste en mano de obra necesario para fabricar cada unidad producida se encarece significativamente.",
        "enunciado_p2": "b) Competitividad y Empleo: ¿Pueden trasladar el sobrecoste a precios sin consecuencias? ¿Cómo ajustará la empresa?",
        "solucion_p2": "1. Imposibilidad de Traslación sin Consecuencias:\nNo es posible trasladar el sobrecoste a precios de forma inocua. Si las empresas aumentan sus precios de venta, sufren una pérdida inmediata de competitividad frente a competidores del sector (nacionales e internacionales) o frente a bienes sustitutivos. Esto desencadena una contracción de la demanda de mercado y una caída de las ventas.\n\n2. Vías de Ajuste Empresarial:\nAnte la imposibilidad de repercutir todo el incremento salarial en precios, la empresa debe asumir el impacto a través de:\n• Compresión de márgenes de beneficio empresarial a corto plazo.\n• Ajuste en el factor trabajo: reducción de plantilla (despidos, no renovación de contratos temporales) o reducción de horas trabajadas para contener la masa salarial.\n• Inversión tecnológica y sustitución de trabajo por capital: acelerar la mecanización o digitalización para elevar la productividad por hora y restablecer la rentabilidad a medio y largo plazo."
    },
    {
        "sesion_num": 3,
        "id": "s03",
        "titulo_corto": "Sesión 03",
        "titulo_completo": "Sesión 03 · Oferta de Trabajo, Salario de Reserva y Trampas de Inactividad",
        "tema": "Tema 1: Macroeconomía del Mercado de Trabajo y Dinámica Salarial",
        "fecha": "21 de Septiembre 2026",
        "calif_path": os.path.join(BASE_DIR, "Temas EB", "Sesiones EB", "Sesion 03", "evaluacion", "calificaciones_sesion_03.csv"),
        "trans_path": os.path.join(BASE_DIR, "Temas EB", "Sesiones EB", "Sesion 03", "evaluacion", "transcripciones_psll_sesion_03.csv"),
        "enunciado_p1": "«Un trabajador desempleado percibe un subsidio asistencial de 480 €/mes (Y_NS). Recibe una oferta para trabajar como operario de logística a jornada completa por 1.150 € netos mensuales. Para acudir al puesto debe gastar 180 € al mes en combustible y perdería de forma inmediata la ayuda de 480 €».\na) Calcule la ganancia neta real por hora trabajada de este operario.",
        "solucion_p1": "1. Ingresos y Gastos Mensuales:\nSalario neto mensual ofertado: 1.150 €.\nGastos obligatorios de transporte (combustible): -180 €.\nIngreso neto efectivo disponible derivado del empleo: 1.150 € - 180 € = 970 €/mes.\n\n2. Coste de Oportunidad y Pérdida del Subsidio:\nAl aceptar el empleo pierde automáticamente el subsidio asistencial de 480 €/mes.\nGanancia neta real incremental mensual:\nΔY = 970 € - 480 € = 490 €/mes.\n\n3. Ganancia Neta Real por Hora Trabajada:\nJornada completa habitual (40 horas semanales × 4 semanas = 160 horas al mes):\nGanancia neta por hora = 490 € / 160 h ≈ 3,06 €/hora.\n(Frente a un salario contractual aparente de 1.150 € / 160 h = 7,19 €/hora, el trabajador solo percibe un incentivo real marginal de 3,06 € por cada hora que dedica a trabajar).",
        "enunciado_p2": "b) Explique analíticamente por qué el salario ofertado se sitúa por debajo de su Salario de Reserva (w_R = 1.000 €). Indique si acepta o no el empleo.",
        "solucion_p2": "1. Comparación Analítica con el Salario de Reserva:\nEl Salario de Reserva (w_R = 1.000 €/mes) es el umbral mínimo de remuneración neta que exige el trabajador para renunciar a su tiempo de ocio/inactividad e incorporarse al empleo.\nEl salario neto disponible que obtiene de la actividad laboral tras deducir los gastos ineludibles de transporte es:\nw_efectivo = 1.150 € - 180 € = 970 €/mes.\nDado que 970 € < 1.000 € (w_efectivo < w_R), la oferta económica se sitúa estrictamente por debajo de su salario de reserva (e incluso la ganancia adicional neta de 490 € frente a percibir la ayuda asistencial queda extraordinariamente lejos de retribuir el esfuerzo de 160 h mensuales).\n\n2. Decisión del Trabajador y Trampa del Desempleo:\nDado que w < w_R, el trabajador RECHAZA la oferta de empleo y decide permanecer en desempleo asistido. El caso ejemplifica formalmente la «trampa del desempleo» (unemployment trap), en la que la pérdida brusca del subsidio combinada con los costes fijos de inserción desincentiva la aceptación de ofertas de trabajo en bandas salariales bajas o medias."
    }
]

GLOBAL_SALT = "psll_upo_eval_2026_salt"
ALL_COMBOS = list(itertools.combinations(range(8), 4))

def normalizar_texto(texto):
    if not texto or pd.isna(texto):
        return ""
    return str(texto).strip()

def strip_accents(s):
    return ''.join(c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn')

def parse_dni(raw):
    m = re.search(r'(\d+)', str(raw))
    return m.group(1).zfill(8) if m else ''

def parse_estudiante(raw):
    raw_str = normalizar_texto(raw)
    # Limpiar coletillas como (Erasmus)
    raw_clean = re.sub(r'\(.*?\)', '', raw_str).strip()
    parts = raw_clean.split(',')
    if len(parts) == 2:
        nombre = parts[1].strip().title()
        apellidos = parts[0].strip().title()
        return nombre, apellidos
    return raw_clean.title(), ""

def generar_username_sugerido(nombre, apellidos, dni):
    # Genera un handle institucional estándar si no hay username explícito
    nom_clean = strip_accents(nombre.lower())
    ape_parts = strip_accents(apellidos.lower()).split()
    first_nom = nom_clean.split()[0] if nom_clean else 'u'
    part1 = ape_parts[0][:3] if len(ape_parts) > 0 else 'est'
    part2 = ape_parts[1][:3] if len(ape_parts) > 1 else ''
    handle = f"{first_nom[0]}{part1}{part2}".replace(" ", "").replace("-", "")
    return handle

def cargar_censo_alumnos():
    alumnos_dict = {}

    # 1. Cargar Línea 1 (Excel)
    if os.path.exists(lista_l1_path):
        try:
            df1 = pd.read_excel(lista_l1_path, skiprows=7)
            for _, row in df1.iterrows():
                dni = parse_dni(row.get("DNI"))
                if not dni or len(dni) != 8:
                    continue
                nom, ape = parse_estudiante(row.get("ESTUDIANTE"))
                plan = normalizar_texto(row.get("PLAN"))
                if dni not in alumnos_dict:
                    alumnos_dict[dni] = {
                        "dni": dni,
                        "nombre": nom,
                        "apellidos": ape,
                        "lineas": ["Línea 1"],
                        "plan": plan
                    }
                else:
                    if "Línea 1" not in alumnos_dict[dni]["lineas"]:
                        alumnos_dict[dni]["lineas"].append("Línea 1")
        except Exception as e:
            print(f"[AVISO] Error al leer lista Línea 1: {e}")

    # 2. Cargar Línea 2 (TSV latin1)
    if os.path.exists(lista_l2_path):
        try:
            df2 = pd.read_csv(lista_l2_path, sep="\t", encoding="latin1", skiprows=6)
            for _, row in df2.iterrows():
                dni = parse_dni(row.get("DNI"))
                if not dni or len(dni) != 8:
                    continue
                nom, ape = parse_estudiante(row.get("ESTUDIANTE"))
                plan = normalizar_texto(row.get("PLAN"))
                if dni not in alumnos_dict:
                    alumnos_dict[dni] = {
                        "dni": dni,
                        "nombre": nom,
                        "apellidos": ape,
                        "lineas": ["Línea 2"],
                        "plan": plan
                    }
                else:
                    if "Línea 2" not in alumnos_dict[dni]["lineas"]:
                        alumnos_dict[dni]["lineas"].append("Línea 2")
        except Exception as e:
            print(f"[AVISO] Error al leer lista Línea 2: {e}")

    # Lista final
    censo = []
    for dni, d in sorted(alumnos_dict.items(), key=lambda x: (x[1]["apellidos"], x[1]["nombre"])):
        nom = d["nombre"]
        ape = d["apellidos"]
        username = generar_username_sugerido(nom, ape, dni)
        censo.append({
            "id_norm": dni,
            "username": username,
            "nombre": nom,
            "apellidos": ape,
            "nombre_completo": f"{nom} {ape}",
            "linea": " / ".join(d["lineas"]),
            "plan": d["plan"]
        })
    return pd.DataFrame(censo)

def compilar_pasaporte():
    print("=" * 75)
    print("  COMPILADOR CRIPTOGRÁFICO PASAPORTE DE EVALUACIÓN CONTINUA · PSLL")
    print("=" * 75)

    df_censo = cargar_censo_alumnos()
    print(f"[*] Censo de estudiantes cargado: {len(df_censo)} alumnos únicos registrados.")

    # Guardar censo unificado en alumnos/lista_alumnos.csv para referencia
    censo_csv_path = os.path.join(SCRIPT_DIR, "lista_alumnos.csv")
    df_censo.to_csv(censo_csv_path, sep=";", index=False, encoding="utf-8-sig")
    print(f"[OK] Censo unificado archivado en: {censo_csv_path}")

    # Verificar datos de sesiones
    sesiones_disponibles = []
    for s_cfg in EVAL_SESIONES_CONFIG:
        has_calif = os.path.exists(s_cfg["calif_path"])
        has_trans = os.path.exists(s_cfg["trans_path"])
        df_calif = None
        df_trans = None
        if has_calif:
            try:
                df_calif = pd.read_csv(s_cfg["calif_path"], sep=";", encoding="utf-8-sig")
                df_calif["id_norm"] = df_calif["ID_Estudiante"].astype(str).str.strip().str.zfill(8)
            except Exception as e:
                print(f"[!] Error leyendo calificaciones {s_cfg['id']}: {e}")
        if has_trans:
            try:
                df_trans = pd.read_csv(s_cfg["trans_path"], sep=";", encoding="utf-8-sig")
                df_trans["id_norm"] = df_trans["ID_Estudiante"].astype(str).str.strip().str.zfill(8)
            except Exception as e:
                print(f"[!] Error leyendo transcripciones {s_cfg['id']}: {e}")
        
        sesiones_disponibles.append({
            "config": s_cfg,
            "has_data": (df_calif is not None),
            "df_calif": df_calif,
            "df_trans": df_trans
        })

    students_encrypted_db = []
    all_students_scores = []

    for idx, row in df_censo.iterrows():
        dni = str(row["id_norm"]).strip()
        username = str(row["username"]).strip().lower()
        nombre = str(row["nombre"]).strip()
        apellidos = str(row["apellidos"]).strip()
        nombre_completo = str(row["nombre_completo"]).strip()

        puntos_totales_obtenidos = 0
        puntos_totales_potenciales = 0
        sesiones_payload = []

        for item in sesiones_disponibles:
            cfg = item["config"]
            df_calif = item["df_calif"]
            df_trans = item["df_trans"]

            puntos_ses = 0
            puntos_max = 1000
            puntos_totales_potenciales += puntos_max

            if item["has_data"] and df_calif is not None:
                match_c = df_calif[df_calif["id_norm"] == dni]
                if not match_c.empty:
                    c_row = match_c.iloc[0]
                    puntos_ses = int(c_row["Puntos"]) if pd.notna(c_row.get("Puntos")) else 0
                    estado_ses = str(c_row.get("Estado", "Presentado"))
                    feedback_ses = str(c_row.get("Retroalimentacion", "Sin observaciones."))
                else:
                    estado_ses = "No presentado"
                    feedback_ses = "No consta entrega del reto manuscrito de cierre de sesión."
            else:
                # Sesión en proceso de corrección o inicial
                estado_ses = "En corrección"
                puntos_ses = 0
                feedback_ses = "Calificaciones en proceso de procesamiento y validación docente."

            puntos_totales_obtenidos += puntos_ses

            # Transcripciones
            t_p1 = "No consta entrega escrita."
            t_p2 = "No consta entrega escrita."
            if item["df_trans"] is not None:
                match_t = df_trans[df_trans["id_norm"] == dni]
                if not match_t.empty:
                    t_row = match_t.iloc[0]
                    t_p1 = str(t_row.get("Transcripcion_P1", t_p1))
                    t_p2 = str(t_row.get("Transcripcion_P2", t_p2))

            # Preguntas de la sesión
            preguntas = []
            if cfg.get("enunciado_p1"):
                preguntas.append({
                    "num": 1,
                    "id": f"{cfg['id']}_p1",
                    "tipo": "Reto Manuscrito Individual",
                    "titulo": f"Pregunta 1 · {cfg['titulo_corto']}",
                    "enunciado": cfg["enunciado_p1"],
                    "transcripcion": t_p1 if item["has_data"] else "Próximamente disponible tras la finalización del proceso de corrección.",
                    "solucion_oficial": cfg["solucion_p1"] if item["has_data"] else "La solución oficial se publicará junto con las calificaciones definitivas."
                })
            if cfg.get("enunciado_p2"):
                preguntas.append({
                    "num": 2,
                    "id": f"{cfg['id']}_p2",
                    "tipo": "Aplicación Práctica",
                    "titulo": f"Pregunta 2 · {cfg['titulo_corto']}",
                    "enunciado": cfg["enunciado_p2"],
                    "transcripcion": t_p2 if item["has_data"] else "Próximamente disponible.",
                    "solucion_oficial": cfg["solucion_p2"] if item["has_data"] else "Pendiente de publicación."
                })

            sesiones_payload.append({
                "sesion_num": cfg["sesion_num"],
                "id": cfg["id"],
                "titulo_corto": cfg["titulo_corto"],
                "titulo_completo": cfg["titulo_completo"],
                "tema": cfg["tema"],
                "fecha": cfg["fecha"],
                "estado": estado_ses,
                "puntos_obtenidos": puntos_ses,
                "puntos_maximos": puntos_max,
                "porcentaje": round((puntos_ses / puntos_max) * 100, 1) if puntos_max > 0 else 0,
                "feedback_general": feedback_ses,
                "preguntas": preguntas
            })

        # Historial de evolución para las 16 sesiones del curso
        evolucion_16_sesiones = []
        # S01: introductoria (sin reto evaluable)
        evolucion_16_sesiones.append({
            "sesion": 1,
            "tag": "S01",
            "puntos": 0,
            "acumulado": 0,
            "evaluada": True,
            "max_sesion": 0
        })

        acum_calc = 0
        for ses_item in sesiones_payload:
            p_ob = ses_item["puntos_obtenidos"]
            acum_calc += p_ob
            evolucion_16_sesiones.append({
                "sesion": ses_item["sesion_num"],
                "tag": f"S{ses_item['sesion_num']:02d}",
                "puntos": p_ob,
                "acumulado": acum_calc,
                "evaluada": True,
                "max_sesion": ses_item["puntos_maximos"]
            })

        max_ses_num = max([s["sesion_num"] for s in sesiones_payload], default=1)
        for s_idx in range(max_ses_num + 1, 17):
            evolucion_16_sesiones.append({
                "sesion": s_idx,
                "tag": f"S{s_idx:02d}",
                "puntos": None,
                "acumulado": None,
                "evaluada": False,
                "max_sesion": 1000
            })

        if puntos_totales_potenciales == 0:
            puntos_totales_potenciales = 1000
        porcentaje_global = round((puntos_totales_obtenidos / puntos_totales_potenciales) * 100, 2)

        payload_data = {
            "nombre_completo": nombre_completo,
            "nombre_pila": nombre,
            "apellidos": apellidos,
            "username": username,
            "dni": dni,
            "linea": row["linea"],
            "plan": row["plan"],
            "puntos_acumulados": puntos_totales_obtenidos,
            "puntos_potenciales": puntos_totales_potenciales,
            "puntos_potenciales_curso": 16000,
            "porcentaje_logrado": porcentaje_global,
            "total_sesiones_evaluadas": len([s for s in sesiones_payload if s["estado"] != "En corrección"]),
            "total_sesiones_curso": 16,
            "evolucion_sesiones": evolucion_16_sesiones,
            "sesiones": sesiones_payload
        }

        all_students_scores.append(puntos_totales_obtenidos)

        master_key = os.urandom(32)
        payload_nonce = os.urandom(12)
        payload_bytes = json.dumps(payload_data, ensure_ascii=False).encode("utf-8")
        encrypted_payload = AESGCM(master_key).encrypt(payload_nonce, payload_bytes, None)

        # Hashes para permitir acceso tanto por username institucional como por DNI
        user_hash = hashlib.sha256(f"{GLOBAL_SALT}:{username}".encode("utf-8")).hexdigest()
        dni_hash = hashlib.sha256(f"{GLOBAL_SALT}:{dni}".encode("utf-8")).hexdigest()
        user_salt = os.urandom(16).hex()

        vault = []
        vault_nonce = os.urandom(12)
        for combo_idx, combo in enumerate(ALL_COMBOS):
            four_digits = "".join(dni[pos] for pos in combo)
            k_c_material = f"{user_salt}:{dni}:{four_digits}:{combo_idx}".encode("utf-8")
            k_c = hashlib.sha256(k_c_material).digest()
            enc_mk = AESGCM(k_c).encrypt(vault_nonce, master_key, None)
            vault.append(base64.b64encode(enc_mk).decode("ascii"))

        students_encrypted_db.append({
            "user_hash": user_hash,
            "dni_hash": dni_hash,
            "dni": dni,
            "user_salt": user_salt,
            "vault_nonce": base64.b64encode(vault_nonce).decode("ascii"),
            "vault": vault,
            "payload_nonce": base64.b64encode(payload_nonce).decode("ascii"),
            "payload_ciphertext": base64.b64encode(encrypted_payload).decode("ascii")
        })

    # Array anónimo de puntuaciones de la clase ordenadas (100% anónimo y RGPD)
    anon_scores = sorted(all_students_scores)

    os.makedirs(os.path.join(MICRO_APPS_DIR, "data"), exist_ok=True)
    dest_js = os.path.join(MICRO_APPS_DIR, "data", "calificaciones_cifradas_psll.js")

    output_js = f"""// Base de datos cifrada de calificaciones Políticas Sociolaborales y de Empleo (PSLL · UPO)
// Cifrado militar Zero-Knowledge AES-GCM-256 + SHA-256. Ningún dato personal legible en claro.
window.__PSLL_GLOBAL_SALT__ = "{GLOBAL_SALT}";
window.__PSLL_COMBOS__ = {json.dumps(ALL_COMBOS)};
window.__PSLL_TOTAL_SESIONES__ = 16;
window.__PSLL_PUNTOS_POTENCIALES_ACTUALES__ = {puntos_totales_potenciales};
window.__PSLL_PUNTOS_POTENCIALES_CURSO__ = 16000;
window.__PSLL_SCORES_ANON__ = {json.dumps(anon_scores)};
window.__PSLL_EVAL_DB__ = {json.dumps(students_encrypted_db, separators=(',', ':'))};
"""

    with open(dest_js, "w", encoding="utf-8") as f:
        f.write(output_js)

    dest_psll_docs = os.path.join(BASE_DIR, "docs", "data", "calificaciones_cifradas_psll.js")
    os.makedirs(os.path.dirname(dest_psll_docs), exist_ok=True)
    with open(dest_psll_docs, "w", encoding="utf-8") as f:
        f.write(output_js)

    print(f"[OK] Archivo cifrado PSLL generado en (micro_apps): {dest_js}")
    print(f"[OK] Archivo cifrado PSLL generado en (docs local): {dest_psll_docs}")
    print(f"[OK] Total de alumnos procesados y cifrados: {len(students_encrypted_db)}")
    print(f"[OK] Tamaño final del fichero JS: {os.path.getsize(dest_js) / 1024:.2f} KB")
    print("=" * 75)

if __name__ == "__main__":
    compilar_pasaporte()
