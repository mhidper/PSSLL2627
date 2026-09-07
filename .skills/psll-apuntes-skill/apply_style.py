"""
apply_style.py - Script principal de la skill psll-apuntes-skill.
Lee un documento de apuntes en .docx, aplica la maquetación corporativa completa,
inserta figuras de alta resolución, cajas callout y tablas estilizadas, y guarda el resultado.
"""

import os
import sys
import re
import io
import argparse
import docx

if hasattr(sys.stdout, 'buffer'):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
if hasattr(sys.stderr, 'buffer'):
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT

# Asegurar importación de módulos hermanos
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
if CURRENT_DIR not in sys.path:
    sys.path.insert(0, CURRENT_DIR)

from brand_theme import (
    HEX_COLORS, RGB_COLORS, FONT_HEADINGS, FONT_BODY,
    set_cell_shading, set_cell_margins, set_callout_borders, set_table_borders
)
from figure_generator import generate_beveridge_figure, generate_epa_taxonomy_figure
from docx_styler import (
    set_document_geometry, setup_document_styles, add_header_and_footer,
    insert_callout_box, insert_reflection_box, insert_key_concepts_box, insert_figure
)

def create_institutional_cover(doc, emblem_path: str, upo_logo_path: str):
    """Inserta la cabecera institucional en la primera página alineada a la izquierda."""
    tbl = doc.add_table(rows=1, cols=2)
    tbl.alignment = WD_TABLE_ALIGNMENT.LEFT
    tbl.autofit = False
    
    # Celda izquierda: Textos institucionales alineados a la izquierda
    cell_l = tbl.cell(0, 0)
    cell_l.width = Inches(4.8)
    
    # Párrafo 1: UNIVERSIDAD PABLO DE OLAVIDE
    p1 = cell_l.paragraphs[0]
    p1.alignment = WD_ALIGN_PARAGRAPH.LEFT
    p1.paragraph_format.space_before = Pt(0)
    p1.paragraph_format.space_after = Pt(1.5)
    run_univ = p1.add_run("UNIVERSIDAD PABLO DE OLAVIDE")
    run_univ.font.name = FONT_HEADINGS
    run_univ.font.size = Pt(9.0)
    run_univ.font.bold = True
    run_univ.font.color.rgb = RGB_COLORS["deep_green"]
    
    # Párrafo 2: Facultad de Ciencias del Trabajo...
    p2 = cell_l.add_paragraph()
    p2.alignment = WD_ALIGN_PARAGRAPH.LEFT
    p2.paragraph_format.space_before = Pt(0)
    p2.paragraph_format.space_after = Pt(1.5)
    run_fac = p2.add_run("Facultad de Ciencias del Trabajo · Grado en RRLL y Recursos Humanos")
    run_fac.font.name = FONT_BODY
    run_fac.font.size = Pt(8.5)
    run_fac.font.color.rgb = RGB_COLORS["sage"]
    
    # Párrafo 3: Políticas Sociolaborales y de Empleo...
    p3 = cell_l.add_paragraph()
    p3.alignment = WD_ALIGN_PARAGRAPH.LEFT
    p3.paragraph_format.space_before = Pt(0)
    p3.paragraph_format.space_after = Pt(1.5)
    run_asig = p3.add_run("Políticas Sociolaborales y de Empleo (Código 102023) | Curso 2026-2027")
    run_asig.font.name = FONT_BODY
    run_asig.font.size = Pt(8.5)
    run_asig.font.color.rgb = RGB_COLORS["ink_green"]
    
    # Párrafo 4: Prof. Manuel A. Hidalgo Pérez
    p4 = cell_l.add_paragraph()
    p4.alignment = WD_ALIGN_PARAGRAPH.LEFT
    p4.paragraph_format.space_before = Pt(0)
    p4.paragraph_format.space_after = Pt(0)
    run_prof = p4.add_run("Prof. Manuel A. Hidalgo Pérez")
    run_prof.font.name = FONT_BODY
    run_prof.font.size = Pt(8.5)
    run_prof.font.color.rgb = RGB_COLORS["ink_green"]
    
    # Celda derecha: Emblema oficial PSLL
    cell_r = tbl.cell(0, 1)
    cell_r.width = Inches(1.7)
    p_logo = cell_r.paragraphs[0]
    p_logo.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    p_logo.paragraph_format.space_before = Pt(0)
    p_logo.paragraph_format.space_after = Pt(0)
    
    if os.path.exists(emblem_path):
        p_logo.add_run().add_picture(emblem_path, width=Inches(1.2))
        
    # Línea separadora horizontal alineada a la izquierda
    p_div = doc.add_paragraph()
    p_div.alignment = WD_ALIGN_PARAGRAPH.LEFT
    p_div.paragraph_format.space_before = Pt(4)
    p_div.paragraph_format.space_after = Pt(16)
    run_div = p_div.add_run("―" * 48)
    run_div.font.name = FONT_HEADINGS
    run_div.font.size = Pt(10)
    run_div.font.color.rgb = RGB_COLORS["sage"]

def insert_epa_summary_table(doc):
    """Inserta una tabla estilizada con el resumen de las tasas fundamentales de la EPA."""
    table = doc.add_table(rows=4, cols=3)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = False
    
    headers = ["Indicador Laboral", "Fórmula Matemática Oficial", "Interpretación Económica"]
    widths = [Inches(1.8), Inches(2.2), Inches(2.5)]
    
    # Cabecera
    hdr_cells = table.rows[0].cells
    for i, title in enumerate(headers):
        hdr_cells[i].width = widths[i]
        set_cell_shading(hdr_cells[i], HEX_COLORS["deep_green"])
        set_cell_margins(hdr_cells[i], top_dpt=140, bottom_dpt=140, left_dpt=140, right_dpt=140)
        p = hdr_cells[i].paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.LEFT
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(0)
        run = p.add_run(title)
        run.font.name = FONT_HEADINGS
        run.font.size = Pt(9.5)
        run.font.bold = True
        run.font.color.rgb = RGB_COLORS["white"]
        
    data = [
        ("Tasa de Actividad", "Activos / Población ≥ 16 × 100", "Mide la propensión y disposición a participar en el mercado de trabajo."),
        ("Tasa de Desempleo (Paro)", "Parados / Población Activa × 100", "Proporción de personas que buscando activamente trabajo no lo encuentran."),
        ("Tasa de Empleo (Ocupación)", "Ocupados / Población ≥ 16 × 100", "Capacidad real de la economía de generar puestos para la población en edad laboral."),
    ]
    
    for row_idx, (col1, col2, col3) in enumerate(data, start=1):
        row_cells = table.rows[row_idx].cells
        bg_color = "F7FAF8" if row_idx % 2 == 1 else "FFFFFF"
        for i, val in enumerate([col1, col2, col3]):
            row_cells[i].width = widths[i]
            set_cell_shading(row_cells[i], bg_color)
            set_cell_margins(row_cells[i], top_dpt=120, bottom_dpt=120, left_dpt=140, right_dpt=140)
            p = row_cells[i].paragraphs[0]
            p.paragraph_format.space_before = Pt(0)
            p.paragraph_format.space_after = Pt(0)
            run = p.add_run(val)
            run.font.name = FONT_BODY
            run.font.size = Pt(9.0)
            if i == 0:
                run.font.bold = True
                run.font.color.rgb = RGB_COLORS["deep_green"]
            elif i == 1:
                run.font.color.rgb = RGB_COLORS["sage"]
                run.font.bold = True
            else:
                run.font.color.rgb = RGB_COLORS["ink_green"]
                
    set_table_borders(table)
    
    # Párrafo posterior
    p_post = doc.add_paragraph()
    p_post.paragraph_format.space_before = Pt(2)
    p_post.paragraph_format.space_after = Pt(6)

def style_topic_document(input_path: str, output_path: str):
    """Procesa el documento original y genera la versión maquetada con alta fidelidad."""
    print(f"Leyendo documento original: {input_path}")
    doc_orig = docx.Document(input_path)
    
    # Crear nuevo documento con estilos y geometría
    doc = docx.Document()
    set_document_geometry(doc)
    setup_document_styles(doc)
    
    # Generar figuras si no existen
    figures_dir = os.path.join(CURRENT_DIR, "figures")
    os.makedirs(figures_dir, exist_ok=True)
    epa_fig_path = os.path.join(figures_dir, "epa_taxonomy.png")
    beveridge_fig_path = os.path.join(figures_dir, "beveridge.png")
    
    print("Generando figuras oficiales con la paleta PSLL...")
    generate_epa_taxonomy_figure(epa_fig_path)
    generate_beveridge_figure(beveridge_fig_path)
    
    # Rutas de assets oficiales
    project_root = os.path.abspath(os.path.join(CURRENT_DIR, "..", ".."))
    emblem_path = os.path.join(project_root, "Logos y skills", "psll-presentaciones-skill", "assets", "psll_emblem.png")
    upo_logo_path = os.path.join(project_root, "Logos y skills", "psll-presentaciones-skill", "assets", "upo_logo.jpg")
    
    # 1. Cabecera Institucional
    create_institutional_cover(doc, emblem_path, upo_logo_path)
    
    # Identificar título del tema para encabezados dinámicos
    topic_title = "Tema 1: Fundamentos del Mercado Laboral"
    
    # Banderas para inserción controlada de figuras y cajas piloto
    epa_fig_inserted = False
    epa_callout_inserted = False
    beveridge_fig_inserted = False
    beveridge_callout_inserted = False
    skip_reflection_block = False
    collecting_key_concepts = False
    key_concepts = []
    key_concepts_title = "Conceptos Clave del Tema"
    
    print("Procesando y reclasificando párrafos...")
    for idx, p in enumerate(doc_orig.paragraphs):
        raw_text = p.text.strip()
        if not raw_text:
            continue
            
        # 0.0. RECOLECCIÓN Y VOLCADO DE CONCEPTOS CLAVE EN PÁGINA NUEVA
        if collecting_key_concepts:
            # Si encontramos un nuevo encabezado (capítulo, debate, referencias, etc.), cerramos la caja
            if re.match(r"^\d+\.", raw_text) or raw_text in ["PREGUNTAS PARA EL DEBATE", "REFERENCIAS BIBLIOGRÁFICAS"] or raw_text.startswith("TEMA"):
                if key_concepts:
                    insert_key_concepts_box(doc, title=key_concepts_title, concepts_list=key_concepts, page_break_before=True)
                collecting_key_concepts = False
                key_concepts = []
                # Se continúa la ejecución sin continue para que el párrafo actual se procese normalmente
            else:
                if ":" in raw_text:
                    parts = raw_text.split(":", 1)
                    key_concepts.append((parts[0].strip(), parts[1].strip()))
                elif raw_text:
                    key_concepts.append(("", raw_text.strip()))
                continue

        # Detección del inicio de Conceptos Clave
        if re.match(r"^Conceptos\s+clave", raw_text, re.IGNORECASE):
            collecting_key_concepts = True
            key_concepts_title = raw_text.rstrip(":")
            key_concepts = []
            continue

        # 0.1. PARADA REFLEXIVA AGRUPADA: RANGOS DE LA TASA DE ACTIVIDAD
        if "Reflexión sobre los rangos de la tasa de actividad" in raw_text:
            insert_reflection_box(
                doc,
                title="Límites y Rangos de Variación de la Tasa de Actividad",
                q_and_a_list=[
                    ("¿Puede ser negativa?", "Teóricamente, la tasa de actividad no puede asumir valores negativos, ya que una población activa negativa carece de sentido práctico."),
                    ("¿Es razonable que sea cero?", "Una tasa de actividad del 0% indicaría que ninguna persona en edad de trabajar está buscando empleo ni trabajando, lo cual sería un escenario extremadamente raro y poco realista en cualquier economía moderna."),
                    ("¿Es razonable que sea del 20%?", "Una tasa de actividad del 20% podría darse en países o regiones con una participación limitada en el mercado laboral, quizás debido a restricciones culturales, sociales o a altos niveles de desempleo estructural. No obstante, sigue siendo un valor relativamente bajo en comparación con economías desarrolladas, donde las tasas de actividad suelen oscilar entre el 60% y el 80%.")
                ]
            )
            skip_reflection_block = True
            continue
            
        if skip_reflection_block:
            if "Factores determinantes de la tasa de actividad" in raw_text:
                skip_reflection_block = False
            else:
                continue

        # 0.2. INDICACIÓN DE SESIÓN DOCENTE (CRONOGRAMA DE AULA)
        if "📍" in raw_text or (raw_text.startswith("SESIÓN") and any(k in raw_text for k in ["Semana", "min", "Lunes", "Martes", "Viernes"])):
            clean_session = raw_text.replace("📍", "").strip()
            parts = clean_session.split("—", 1)
            if len(parts) == 2:
                sess_title = parts[0].strip()
                sess_desc = parts[1].strip()
            else:
                sess_title = clean_session
                sess_desc = "Desarrollo presencial de los contenidos, debates y dinámicas activas correspondientes a este bloque según la planificación oficial de la asignatura."
            insert_callout_box(
                doc,
                callout_type="session",
                title=f"Encuadre Docente Presencial · {sess_title}",
                text=sess_desc
            )
            continue

        # 1. TÍTULO PRINCIPAL (TEMA X: ...)
        if re.match(r"^TEMA\s+\d+:", raw_text, re.IGNORECASE):
            topic_title = raw_text
            p_new = doc.add_paragraph()
            p_new.alignment = WD_ALIGN_PARAGRAPH.LEFT
            p_new.paragraph_format.space_before = Pt(8)
            p_new.paragraph_format.space_after = Pt(14)
            p_new.paragraph_format.keep_with_next = True
            run = p_new.add_run(raw_text)
            run.font.name = FONT_HEADINGS
            run.font.size = Pt(20.0)
            run.font.bold = True
            run.font.color.rgb = RGB_COLORS["deep_green"]
            continue
            
        # 2. CAPÍTULOS PRINCIPALES (1. FUNDAMENTOS..., 2. EL PIB..., 6. LA CURVA...)
        if re.match(r"^\d+\.\s+[A-ZÁÉÍÓÚÑ\s]{4,}", raw_text) or raw_text in ["EQUILIBRIO EN EL MERCADO DE TRABAJO", "PREGUNTAS PARA EL DEBATE", "REFERENCIAS BIBLIOGRÁFICAS"]:
            p_new = doc.add_paragraph(style='Heading 1')
            p_new.alignment = WD_ALIGN_PARAGRAPH.LEFT
            p_new.paragraph_format.space_before = Pt(26)
            p_new.paragraph_format.space_after = Pt(6)
            p_new.paragraph_format.keep_with_next = True
            run = p_new.add_run(raw_text)
            run.font.name = FONT_HEADINGS
            run.font.size = Pt(15.0)
            run.font.bold = True
            run.font.color.rgb = RGB_COLORS["deep_green"]
            continue
            
        # 3. SUBEPÍGRAFES NIVEL 2 (1.1., 1.2., 2.1., 6.1., etc.)
        if re.match(r"^\d+\.\d+\.\s+", raw_text):
            p_new = doc.add_paragraph(style='Heading 2')
            p_new.alignment = WD_ALIGN_PARAGRAPH.LEFT
            p_new.paragraph_format.space_before = Pt(18)
            p_new.paragraph_format.space_after = Pt(5)
            p_new.paragraph_format.keep_with_next = True
            run = p_new.add_run(raw_text)
            run.font.name = FONT_HEADINGS
            run.font.size = Pt(12.5)
            run.font.bold = True
            run.font.color.rgb = RGB_COLORS["sage"]
            
            # Si es el epígrafe de Indicadores EPA, insertar diagrama conceptual y tabla resumen
            if not epa_fig_inserted and "1.2. Indicadores básicos" in raw_text:
                insert_figure(
                    doc,
                    epa_fig_path,
                    caption_text="Figura 1.1: Taxonomía oficial y articulación de la población según la EPA (INE / OIT).",
                    source_text="Fuente: Elaboración propia a partir de la metodología de la Encuesta de Población Activa (INE)."
                )
                insert_epa_summary_table(doc)
                epa_fig_inserted = True
                
            # Si es el epígrafe de la Curva de Beveridge, insertar gráfico canónico
            if not beveridge_fig_inserted and ("6.1. Fundamentos" in raw_text or "6.0. Dinámica" in raw_text):
                insert_figure(
                    doc,
                    beveridge_fig_path,
                    caption_text="Figura 1.2: La Curva de Beveridge. Desplazamientos a lo largo de la curva vs. desplazamientos estructurales.",
                    source_text="Fuente: Elaboración propia para Políticas Sociolaborales (UPO). Modelo Diamond-Mortensen-Pissarides."
                )
                beveridge_fig_inserted = True
            continue
            
        # 4. SUBEPÍGRAFES NIVEL 3 (1.2.1., 1.2.2., 4.1.1., etc.)
        if re.match(r"^\d+\.\d+\.\d+\.\s+", raw_text):
            p_new = doc.add_paragraph(style='Heading 3')
            p_new.alignment = WD_ALIGN_PARAGRAPH.LEFT
            p_new.paragraph_format.space_before = Pt(12)
            p_new.paragraph_format.space_after = Pt(3)
            p_new.paragraph_format.keep_with_next = True
            run = p_new.add_run(raw_text)
            run.font.name = FONT_HEADINGS
            run.font.size = Pt(11.0)
            run.font.bold = True
            run.font.color.rgb = RGB_COLORS["deep_green"]
            continue

        # 5. LISTAS ITEMIZADAS CON VIÑETAS (BULLET POINTS)
        # Patrón A: Lista numerada con título en negrita (ej. "1. Heterogeneidad del factor trabajo: ...")
        m_num_item = re.match(r"^(\d+)\.\s+([A-ZÁÉÍÓÚÑ][^:]{2,55}):\s*(.*)$", raw_text)
        if m_num_item:
            p_new = doc.add_paragraph(style='Normal')
            p_new.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
            p_new.paragraph_format.left_indent = Inches(0.35)
            p_new.paragraph_format.first_line_indent = Inches(-0.18)
            p_new.paragraph_format.space_after = Pt(3.5)
            
            run_b = p_new.add_run("•  ")
            run_b.font.name = FONT_BODY
            run_b.font.bold = True
            run_b.font.color.rgb = RGB_COLORS["sage"]
            
            run_t = p_new.add_run(f"{m_num_item.group(2).strip()}: ")
            run_t.font.name = FONT_BODY
            run_t.font.bold = True
            run_t.font.color.rgb = RGB_COLORS["deep_green"]
            
            if m_num_item.group(3).strip():
                run_c = p_new.add_run(m_num_item.group(3).strip())
                run_c.font.name = FONT_BODY
                run_c.font.color.rgb = RGB_COLORS["ink_green"]
            continue

        # Patrón B: Elemento con etiqueta explicativa antes de dos puntos (ej. "Motor económico: El empleo...")
        m_lbl_item = re.match(r"^([A-ZÁÉÍÓÚÑ][^:]{2,40}):\s+(.+)$", raw_text)
        if m_lbl_item and not raw_text.startswith(("TEMA", "NOTA", "Figura", "Fuente", "Definición")):
            p_new = doc.add_paragraph(style='Normal')
            p_new.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
            p_new.paragraph_format.left_indent = Inches(0.35)
            p_new.paragraph_format.first_line_indent = Inches(-0.18)
            p_new.paragraph_format.space_after = Pt(3.5)
            
            run_b = p_new.add_run("•  ")
            run_b.font.name = FONT_BODY
            run_b.font.bold = True
            run_b.font.color.rgb = RGB_COLORS["sage"]
            
            run_t = p_new.add_run(f"{m_lbl_item.group(1).strip()}: ")
            run_t.font.name = FONT_BODY
            run_t.font.bold = True
            run_t.font.color.rgb = RGB_COLORS["deep_green"]
            
            run_c = p_new.add_run(m_lbl_item.group(2).strip())
            run_c.font.name = FONT_BODY
            run_c.font.color.rgb = RGB_COLORS["ink_green"]
            continue

        # Patrón C: Viñetas preexistentes o requisitos directos de una lista
        is_bullet_item = bool(re.match(r"^(\-|\•|\*)\s*(.+)$", raw_text)) or raw_text.startswith((
            "Estar sin empleo", "Haber tomado medidas concretas", "Estar disponible para trabajar"
        ))
        if is_bullet_item:
            clean_item = re.sub(r"^(\-|\•|\*)\s*", "", raw_text).strip()
            p_new = doc.add_paragraph(style='Normal')
            p_new.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
            p_new.paragraph_format.left_indent = Inches(0.35)
            p_new.paragraph_format.first_line_indent = Inches(-0.18)
            p_new.paragraph_format.space_after = Pt(3.5)
            
            run_b = p_new.add_run("•  ")
            run_b.font.name = FONT_BODY
            run_b.font.bold = True
            run_b.font.color.rgb = RGB_COLORS["sage"]
            
            run_c = p_new.add_run(clean_item)
            run_c.font.name = FONT_BODY
            run_c.font.color.rgb = RGB_COLORS["ink_green"]
            continue

        # 6. PÁRRAFO NORMAL (CUERPO DE TEXTO JUSTIFICADO)
        p_new = doc.add_paragraph(style='Normal')
        p_new.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        p_new.paragraph_format.left_indent = Inches(0)
        p_new.paragraph_format.first_line_indent = Inches(0)
        p_new.paragraph_format.space_after = Pt(4.5)
        p_new.paragraph_format.line_spacing = 1.15
        
        # Preservar negritas básicas si el primer run original era negrita o títulos internos cortos
        first_bold = False
        is_short_heading = len(raw_text) < 55 and not raw_text.endswith((".", ":", ";"))
        if (p.runs and p.runs[0].bold) or is_short_heading:
            first_bold = True
            
        # Si es un título o subtítulo corto interno, forzar alineación a la izquierda
        if is_short_heading:
            p_new.alignment = WD_ALIGN_PARAGRAPH.LEFT
            p_new.paragraph_format.space_before = Pt(8)
            p_new.paragraph_format.space_after = Pt(2)
            p_new.paragraph_format.keep_with_next = True
            
        # Copiar texto
        run = p_new.add_run(raw_text)
        run.font.name = FONT_BODY
        run.font.size = Pt(10.5)
        run.font.color.rgb = RGB_COLORS["ink_green"]
        if first_bold:
            run.font.bold = True
            if is_short_heading:
                run.font.color.rgb = RGB_COLORS["deep_green"]



    if collecting_key_concepts and key_concepts:
        insert_key_concepts_box(doc, title=key_concepts_title, concepts_list=key_concepts, page_break_before=True)

    # Agregar encabezados y pies de página
    add_header_and_footer(doc, topic_title)
    
    # Guardar documento con gestión de archivo abierto en Word
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    try:
        doc.save(output_path)
        print(f"\n✅ Documento maquetado generado con éxito en: {output_path}")
    except PermissionError:
        alt_output = output_path.replace(".docx", "_v2.docx")
        doc.save(alt_output)
        print(f"\n⚠️ El archivo '{output_path}' está abierto en Microsoft Word.")
        print(f"✅ Se ha guardado la versión actualizada en: {alt_output}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Aplica la maquetación corporativa oficial de PSLL a un archivo .docx.")
    parser.add_argument("--input", default=r"Temas EB\Tema 1\Apuntes\Tema 1 2627.docx", help="Ruta del documento de entrada")
    parser.add_argument("--output", default=r"Temas EB\Tema 1\Apuntes\Tema 1 2627_maquetado.docx", help="Ruta del documento de salida")
    args = parser.parse_args()
    
    style_topic_document(args.input, args.output)
