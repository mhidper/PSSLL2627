"""
docx_styler.py - Motor de transformación y formateo editorial de documentos docx para PSLL.
Aplica la identidad corporativa completa de forma automatizada y reproducible.
"""

import os
import re
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import parse_xml, OxmlElement
from docx.oxml.ns import nsdecls, qn

from brand_theme import (
    HEX_COLORS, RGB_COLORS, FONT_HEADINGS, FONT_BODY,
    set_cell_shading, set_cell_margins, set_callout_borders, set_table_borders
)

def set_document_geometry(doc):
    """Configura márgenes estándar institucionales de 2.5 cm."""
    for section in doc.sections:
        section.top_margin = Inches(0.98)     # ~2.5 cm
        section.bottom_margin = Inches(0.98)
        section.left_margin = Inches(0.98)
        section.right_margin = Inches(0.98)
        section.header_distance = Inches(0.5)
        section.footer_distance = Inches(0.5)

def setup_document_styles(doc):
    """Establece las tipografías y colores base en los estilos del documento."""
    styles = doc.styles
    
    # Normal (Cuerpo de texto)
    if 'Normal' in styles:
        normal = styles['Normal']
        normal.font.name = FONT_BODY
        normal.font.size = Pt(10.5)
        normal.font.color.rgb = RGB_COLORS['ink_green']
        normal.paragraph_format.line_spacing = 1.15
        normal.paragraph_format.space_after = Pt(4.5)
        normal.paragraph_format.space_before = Pt(0)
        normal.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    
    # Heading 1 (Capítulo / Bloque mayor)
    if 'Heading 1' in styles:
        h1 = styles['Heading 1']
        h1.font.name = FONT_HEADINGS
        h1.font.size = Pt(15.5)
        h1.font.bold = True
        h1.font.color.rgb = RGB_COLORS['deep_green']
        h1.paragraph_format.space_before = Pt(26)
        h1.paragraph_format.space_after = Pt(6)
        h1.paragraph_format.keep_with_next = True
        
    # Heading 2 (Subepígrafe nivel 2)
    if 'Heading 2' in styles:
        h2 = styles['Heading 2']
        h2.font.name = FONT_HEADINGS
        h2.font.size = Pt(12.5)
        h2.font.bold = True
        h2.font.color.rgb = RGB_COLORS['sage']
        h2.paragraph_format.space_before = Pt(18)
        h2.paragraph_format.space_after = Pt(5)
        h2.paragraph_format.keep_with_next = True

    # Heading 3 (Subepígrafe nivel 3)
    if 'Heading 3' in styles:
        h3 = styles['Heading 3']
        h3.font.name = FONT_HEADINGS
        h3.font.size = Pt(11.0)
        h3.font.bold = True
        h3.font.color.rgb = RGB_COLORS['deep_green']
        h3.paragraph_format.space_before = Pt(12)
        h3.paragraph_format.space_after = Pt(3)
        h3.paragraph_format.keep_with_next = True

def add_header_and_footer(doc, topic_title: str):
    """Agrega cabecera y pie de página dinámico con paginación en Word."""
    for section in doc.sections:
        # Encabezado (justificado a la izquierda según solicitud de marca)
        header = section.header
        header.is_linked_to_previous = False
        hp = header.paragraphs[0]
        hp.alignment = WD_ALIGN_PARAGRAPH.LEFT
        hp.text = f"POLÍTICAS SOCIOLABORALES Y DE EMPLEO · {topic_title.upper()}"
        hp.runs[0].font.name = FONT_HEADINGS
        hp.runs[0].font.size = Pt(8.0)
        hp.runs[0].font.color.rgb = RGB_COLORS['sage']
        
        # Pie de página
        footer = section.footer
        footer.is_linked_to_previous = False
        fp = footer.paragraphs[0]
        fp.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        
        # Texto izquierdo en pie
        run_l = fp.add_run("Universidad Pablo de Olavide (UPO) · Grado en RRLL y RRHH | ")
        run_l.font.name = FONT_BODY
        run_l.font.size = Pt(8.5)
        run_l.font.color.rgb = RGB_COLORS['sage']
        
        # Paginación dinámica XML: Página X de Y
        run_p = fp.add_run("Página ")
        run_p.font.name = FONT_BODY
        run_p.font.size = Pt(8.5)
        run_p.font.color.rgb = RGB_COLORS['ink_green']
        
        fld_page = parse_xml(r'<w:fldSimple %s w:instr="PAGE"/>' % nsdecls('w'))
        fp._p.append(fld_page)
        
        run_de = fp.add_run(" de ")
        run_de.font.name = FONT_BODY
        run_de.font.size = Pt(8.5)
        run_de.font.color.rgb = RGB_COLORS['ink_green']
        
        fld_numpages = parse_xml(r'<w:fldSimple %s w:instr="NUMPAGES"/>' % nsdecls('w'))
        fp._p.append(fld_numpages)

def insert_callout_box(doc, callout_type: str, title: str, text: str, page_break_before: bool = False):
    """
    Inserta una caja destacada (callout box) de 1 celda con sombreado y borde izquierdo grueso.
    Tipos: 'session', 'concept', 'warning', 'case'.
    Si page_break_before es True o callout_type == 'concept', inserta un salto de página antes.
    """
    if page_break_before or callout_type == "concept":
        doc.add_page_break()

    tbl = doc.add_table(rows=1, cols=1)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl.autofit = False
    cell = tbl.cell(0, 0)
    cell.width = Inches(6.5)
    
    if callout_type == "session":
        bg_hex = HEX_COLORS["mint"]          # Verde menta suave
        border_hex = HEX_COLORS["deep_green"] # Borde verde profundo distintivo
        icon = "🗓️"
        title_color = RGB_COLORS["deep_green"]
    elif callout_type == "reflection":
        bg_hex = HEX_COLORS["warm_cream"]     # Neutro cálido / crema suave
        border_hex = HEX_COLORS["sage"]       # Borde verde salvia
        icon = "💭"
        title_color = RGB_COLORS["deep_green"]
    elif callout_type == "concept":
        bg_hex = HEX_COLORS["mint"]
        border_hex = HEX_COLORS["sage"]
        icon = "💡"
        title_color = RGB_COLORS["deep_green"]
    elif callout_type == "warning":
        bg_hex = HEX_COLORS["alert_bg"]
        border_hex = HEX_COLORS["coral"]
        icon = "⚠️"
        title_color = RGB_COLORS["coral"]
    else: # case / empirical
        bg_hex = HEX_COLORS["warm_cream"]
        border_hex = HEX_COLORS["deep_green"]
        icon = "📊"
        title_color = RGB_COLORS["deep_green"]
        
    set_cell_shading(cell, bg_hex)
    set_cell_margins(cell, top_dpt=140, bottom_dpt=140, left_dpt=200, right_dpt=160)
    set_callout_borders(cell, border_hex, border_size_pt=26)
    
    # Párrafo del título
    p_title = cell.paragraphs[0]
    p_title.alignment = WD_ALIGN_PARAGRAPH.LEFT
    p_title.paragraph_format.space_before = Pt(0)
    p_title.paragraph_format.space_after = Pt(2)
    run_icon = p_title.add_run(f"{icon}  {title.upper()}")
    run_icon.font.name = FONT_HEADINGS
    run_icon.font.size = Pt(9.5)
    run_icon.font.bold = True
    run_icon.font.color.rgb = title_color
    
    # Texto interior (justificado)
    p_text = cell.add_paragraph()
    p_text.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p_text.paragraph_format.space_before = Pt(0)
    p_text.paragraph_format.space_after = Pt(0)
    p_text.paragraph_format.line_spacing = 1.15
    run_text = p_text.add_run(text)
    run_text.font.name = FONT_BODY
    run_text.font.size = Pt(9.5)
    run_text.font.color.rgb = RGB_COLORS["ink_green"]
    
    # Espacio tras la caja
    p_after = doc.add_paragraph()
    p_after.paragraph_format.space_before = Pt(0)
    p_after.paragraph_format.space_after = Pt(4)

def insert_reflection_box(doc, title: str, q_and_a_list: list):
    """
    Inserta una caja estructurada de Parada Reflexiva con preguntas encadenadas.
    q_and_a_list es una lista de tuplas: [ (pregunta, respuesta), ... ]
    Para evitar que Word estire las palabras justificando líneas cortas,
    la pregunta va en un párrafo alineado a la izquierda y la respuesta justificada debajo.
    """
    tbl = doc.add_table(rows=1, cols=1)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl.autofit = False
    cell = tbl.cell(0, 0)
    cell.width = Inches(6.5)
    
    bg_hex = HEX_COLORS["warm_cream"]
    border_hex = HEX_COLORS["sage"]
    
    set_cell_shading(cell, bg_hex)
    set_cell_margins(cell, top_dpt=140, bottom_dpt=140, left_dpt=200, right_dpt=160)
    set_callout_borders(cell, border_hex, border_size_pt=26)
    
    # Párrafo del título
    p_title = cell.paragraphs[0]
    p_title.alignment = WD_ALIGN_PARAGRAPH.LEFT
    p_title.paragraph_format.space_before = Pt(0)
    p_title.paragraph_format.space_after = Pt(5)
    run_icon = p_title.add_run(f"💭  PARADA REFLEXIVA: {title.upper()}")
    run_icon.font.name = FONT_HEADINGS
    run_icon.font.size = Pt(10.0)
    run_icon.font.bold = True
    run_icon.font.color.rgb = RGB_COLORS["deep_green"]
    
    # Preguntas y respuestas (pregunta alineada a la izquierda, respuesta justificada)
    for i, (q, a) in enumerate(q_and_a_list):
        # 1. Párrafo de la pregunta (siempre alineado a la izquierda, sin saltos de línea \n)
        p_q = cell.add_paragraph()
        p_q.alignment = WD_ALIGN_PARAGRAPH.LEFT
        p_q.paragraph_format.space_before = Pt(5 if i > 0 else 2)
        p_q.paragraph_format.space_after = Pt(1.5)
        p_q.paragraph_format.line_spacing = 1.15
        p_q.paragraph_format.keep_with_next = True
        
        run_bullet = p_q.add_run("•  ")
        run_bullet.font.name = FONT_BODY
        run_bullet.font.size = Pt(9.5)
        run_bullet.font.bold = True
        run_bullet.font.color.rgb = RGB_COLORS["sage"]
        
        run_q = p_q.add_run(q.strip())
        run_q.font.name = FONT_BODY
        run_q.font.size = Pt(9.5)
        run_q.font.bold = True
        run_q.font.color.rgb = RGB_COLORS["deep_green"]
        
        # 2. Párrafo de la respuesta (justificado, con sutil sangría izquierda para jerarquía visual)
        p_a = cell.add_paragraph()
        p_a.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        p_a.paragraph_format.left_indent = Inches(0.18)
        p_a.paragraph_format.space_before = Pt(0)
        p_a.paragraph_format.space_after = Pt(4)
        p_a.paragraph_format.line_spacing = 1.15
        
        run_a = p_a.add_run(a.strip())
        run_a.font.name = FONT_BODY
        run_a.font.size = Pt(9.5)
        run_a.font.color.rgb = RGB_COLORS["ink_green"]
        
    p_after = doc.add_paragraph()
    p_after.paragraph_format.space_before = Pt(0)
    p_after.paragraph_format.space_after = Pt(4)

def insert_key_concepts_box(doc, title: str, concepts_list: list, page_break_before: bool = True):
    """
    Inserta una caja destacada completa de Conceptos Clave en una página nueva.
    Por solicitud de diseño editorial, SIEMPRE va precedida de un salto de página.
    concepts_list es una lista de tuplas: [ (término, definición), ... ]
    """
    if page_break_before:
        doc.add_page_break()
        
    tbl = doc.add_table(rows=1, cols=1)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl.autofit = False
    cell = tbl.cell(0, 0)
    cell.width = Inches(6.5)
    
    bg_hex = HEX_COLORS["mint"]          # Verde menta corporativo
    border_hex = HEX_COLORS["sage"]      # Borde verde salvia distintivo
    
    set_cell_shading(cell, bg_hex)
    set_cell_margins(cell, top_dpt=160, bottom_dpt=160, left_dpt=200, right_dpt=160)
    set_callout_borders(cell, border_hex, border_size_pt=26)
    
    # Título de la caja
    p_title = cell.paragraphs[0]
    p_title.alignment = WD_ALIGN_PARAGRAPH.LEFT
    p_title.paragraph_format.space_before = Pt(0)
    p_title.paragraph_format.space_after = Pt(6)
    run_icon = p_title.add_run(f"💡  {title.upper()}")
    run_icon.font.name = FONT_HEADINGS
    run_icon.font.size = Pt(11.0)
    run_icon.font.bold = True
    run_icon.font.color.rgb = RGB_COLORS["deep_green"]
    
    # Lista de conceptos
    for i, (term, desc) in enumerate(concepts_list):
        p_item = cell.add_paragraph()
        p_item.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        p_item.paragraph_format.left_indent = Inches(0.25)
        p_item.paragraph_format.first_line_indent = Inches(-0.15)
        p_item.paragraph_format.space_before = Pt(3 if i > 0 else 0)
        p_item.paragraph_format.space_after = Pt(2)
        p_item.paragraph_format.line_spacing = 1.15
        
        run_b = p_item.add_run("• ")
        run_b.font.name = FONT_BODY
        run_b.font.bold = True
        run_b.font.color.rgb = RGB_COLORS["sage"]
        
        run_t = p_item.add_run(f"{term.strip()}: ")
        run_t.font.name = FONT_BODY
        run_t.font.bold = True
        run_t.font.color.rgb = RGB_COLORS["deep_green"]
        
        run_d = p_item.add_run(desc.strip())
        run_d.font.name = FONT_BODY
        run_d.font.size = Pt(9.5)
        run_d.font.color.rgb = RGB_COLORS["ink_green"]
        
    p_after = doc.add_paragraph()
    p_after.paragraph_format.space_before = Pt(0)
    p_after.paragraph_format.space_after = Pt(8)



def insert_figure(doc, image_path: str, caption_text: str, source_text: str, width_inches=6.2):
    """Inserta una figura centrada con pie y fuente reglamentarios."""
    if not os.path.exists(image_path):
        return
        
    p_img = doc.add_paragraph()
    p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_img.paragraph_format.space_before = Pt(8)
    p_img.paragraph_format.space_after = Pt(3)
    p_img.paragraph_format.keep_with_next = True
    run_img = p_img.add_run()
    run_img.add_picture(image_path, width=Inches(width_inches))
    
    # Pie de figura
    p_cap = doc.add_paragraph()
    p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_cap.paragraph_format.space_before = Pt(0)
    p_cap.paragraph_format.space_after = Pt(1)
    p_cap.paragraph_format.keep_with_next = True
    run_cap = p_cap.add_run(caption_text)
    run_cap.font.name = FONT_HEADINGS
    run_cap.font.size = Pt(9.0)
    run_cap.font.bold = True
    run_cap.font.color.rgb = RGB_COLORS["deep_green"]
    
    # Fuente
    p_src = doc.add_paragraph()
    p_src.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_src.paragraph_format.space_before = Pt(0)
    p_src.paragraph_format.space_after = Pt(8)
    run_src = p_src.add_run(source_text)
    run_src.font.name = FONT_BODY
    run_src.font.size = Pt(8.0)
    run_src.font.italic = True
    run_src.font.color.rgb = RGBColor(111, 128, 115)
