"""
analizar_sondeo_sesion02.py
Procesa el archivo Excel descargado de Microsoft Forms para la Sesión EB 2.
Identifica los sesgos de cada alumno y genera un reporte resumen del aula.

Uso:
    python analizar_sondeo_sesion02.py [archivo_respuestas.xlsx]
"""

import sys
import os
import pandas as pd

def analizar_sondeo(excel_path=None):
    if not excel_path:
        # Buscar el archivo Excel más reciente en la carpeta de la sesión
        current_dir = os.path.dirname(os.path.abspath(__file__))
        excels = [f for f in os.listdir(current_dir) if f.endswith('.xlsx') and not f.startswith('~$') and not f.startswith('Sesion')]
        if not excels:
            print("❌ No se encontró ningún archivo Excel de respuestas de Forms en esta carpeta.")
            print("👉 Guarda el Excel descargado de Forms aquí y vuelve a ejecutar:")
            print("   python analizar_sondeo_sesion02.py NombreDelArchivo.xlsx")
            return
        excel_path = os.path.join(current_dir, excels[0])

    print(f"📊 Leyendo respuestas desde: {os.path.basename(excel_path)}")
    df = pd.read_excel(excel_path)

    # Identificar columnas
    col_nombre = [c for c in df.columns if 'nombre' in c.lower() or 'name' in c.lower()][0]
    col_email = [c for c in df.columns if 'correo' in c.lower() or 'email' in c.lower()][0]
    col_pregunta = [c for c in df.columns if 'pactáramos' in c.lower() or 'salarios' in c.lower() or '15%' in c.lower()][-1]

    # Clasificar respuestas
    def clasificar_sesgo(resp):
        if pd.isna(resp):
            return "Sin responder"
        r = str(resp).lower()
        if "convergeríamos" in r or "consumo" in r or "reactivaría" in r:
            return "Sesgo 1: Demanda (Consumo/Alemania)"
        elif "no podrían asumir" in r or "coste unitario" in r or "subirían precios" in r:
            return "Acierto: Equilibrio CLU / Empleo"
        elif "motivados" in r or "productividad porque" in r:
            return "Sesgo 2: Voluntarismo / Motivación"
        return "Otra"

    df['Diagnostico_Sesgo'] = df[col_pregunta].apply(clasificar_sesgo)

    total_respuestas = len(df)
    conteo = df['Diagnostico_Sesgo'].value_counts()
    porcentajes = (conteo / total_respuestas * 100).round(1)

    print("\n" + "="*60)
    print("📈 RESULTADOS AGREGADOS DEL AULA (SESIÓN EB 2)")
    print("="*60)
    print(f"Total de alumnos participantes: {total_respuestas}\n")
    
    for sesgo, cant in conteo.items():
        pct = porcentajes[sesgo]
        barra = "█" * int(pct / 5)
        print(f" • {sesgo:<35}: {cant:>3} alumnos ({pct:>5.1f}%)  {barra}")

    # Guardar reporte limpio individual
    out_csv = os.path.join(os.path.dirname(excel_path), "registro_nominal_sesgos_sesion02.csv")
    df_nominal = df[[col_nombre, col_email, col_pregunta, 'Diagnostico_Sesgo']].copy()
    df_nominal.columns = ['Nombre_Alumno', 'Email_UPO', 'Respuesta_Elegida', 'Diagnostico_Sesgo']
    df_nominal.to_csv(out_csv, index=False, encoding='utf-8-sig')

    print("\n" + "="*60)
    print(f"💾 Registro nominal guardado con éxito en:")
    print(f"   {out_csv}")
    print("="*60)

if __name__ == "__main__":
    archivo = sys.argv[1] if len(sys.argv) > 1 else None
    analizar_sondeo(archivo)
