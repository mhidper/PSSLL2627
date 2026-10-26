# -*- coding: utf-8 -*-
"""
convert_md_to_docx.py
Convierte los archivos Markdown de EPD 2 a documentos Word (.docx)
aplicando estrictamente el sistema de diseño y marca institucional de PSLL (UPO).
"""

import os
import sys
import re
import docx.opc.constants
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import parse_xml, OxmlElement
from docx.oxml.ns import nsdecls, qn

# Añadir .skills/psll-apuntes-skill al path para importar tokens oficiales
SKILL_DIR = r"c:\Users\Usuario\Dropbox\DOCENCIA UPO\CURSO 26-27\PSLL\.skills\psll-apuntes-skill"
if SKILL_DIR not in sys.path:
    sys.path.append(SKILL_DIR)

from brand_theme import (
    HEX_COLORS, RGB_COLORS, FONT_HEADINGS, FONT_BODY,
    set_cell_shading, set_cell_margins, set_callout_borders, set_table_borders
)
from docx_styler import set_document_geometry, setup_document_styles, add_header_and_footer

WORKSPACE_DIR = r"c:\Users\Usuario\Dropbox\DOCENCIA UPO\CURSO 26-27\PSLL"
LOGO_PATH = os.path.join(WORKSPACE_DIR, "Logos y skills", "psll-presentaciones-skill", "assets", "logo_psll_upo.png")

def add_institutional_cover_header(doc, doc_title: str, doc_subtitle: str):
    """Inserta la cabecera institucional oficial de PSLL en la primera página."""
    table = doc.add_table(rows=1, cols=2)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = False
    
    # Anchos: Columna izquierda 4.5", Columna derecha 2.0"
    table.columns[0].width = Inches(4.7)
    table.columns[1].width = Inches(1.8)
    
    cell_l = table.cell(0, 0)
    cell_r = table.cell(0, 1)
    
    # Quitar bordes a la tabla de cabecera
    for cell in (cell_l, cell_r):
        tcPr = cell._tc.get_or_add_tcPr()
        borders = parse_xml(
            f'<w:tcBorders {nsdecls("w")}>'
            f'  <w:top w:val="none"/>'
            f'  <w:left w:val="none"/>'
            f'  <w:bottom w:val="none"/>'
            f'  <w:right w:val="none"/>'
            f'</w:tcBorders>'
        )
        tcPr.append(borders)
        set_cell_margins(cell, top_dpt=0, bottom_dpt=80, left_dpt=0, right_dpt=0)

    # Texto institucional izquierda
    p1 = cell_l.paragraphs[0]
    p1.alignment = WD_ALIGN_PARAGRAPH.LEFT
    p1.paragraph_format.space_before = Pt(0)
    p1.paragraph_format.space_after = Pt(2)
    r1 = p1.add_run("UNIVERSIDAD PABLO DE OLAVIDE")
    r1.font.name = FONT_HEADINGS
    r1.font.size = Pt(9.5)
    r1.font.bold = True
    r1.font.color.rgb = RGB_COLORS["pine"]
    
    p2 = cell_l.add_paragraph()
    p2.alignment = WD_ALIGN_PARAGRAPH.LEFT
    p2.paragraph_format.space_before = Pt(0)
    p2.paragraph_format.space_after = Pt(2)
    r2 = p2.add_run("Facultad de Ciencias del Trabajo · Grado en RRLL y Recursos Humanos")
    r2.font.name = FONT_BODY
    r2.font.size = Pt(8.5)
    r2.font.color.rgb = RGB_COLORS["sage"]
    
    p3 = cell_l.add_paragraph()
    p3.alignment = WD_ALIGN_PARAGRAPH.LEFT
    p3.paragraph_format.space_before = Pt(0)
    p3.paragraph_format.space_after = Pt(2)
    r3 = p3.add_run("Políticas Sociolaborales y de Empleo (Código 102023) | Curso 2026-2027")
    r3.font.name = FONT_BODY
    r3.font.size = Pt(8.5)
    r3.font.color.rgb = RGB_COLORS["ink_green"]
    
    # Logo derecha
    if os.path.exists(LOGO_PATH):
        p_logo = cell_r.paragraphs[0]
        p_logo.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        p_logo.paragraph_format.space_before = Pt(0)
        p_logo.paragraph_format.space_after = Pt(0)
        p_logo.add_run().add_picture(LOGO_PATH, width=Inches(1.8))
        
    # Línea divisoria
    p_div = doc.add_paragraph()
    p_div.paragraph_format.space_before = Pt(6)
    p_div.paragraph_format.space_after = Pt(16)
    r_div = p_div.add_run("―" * 58)
    r_div.font.name = FONT_BODY
    r_div.font.size = Pt(8)
    r_div.font.color.rgb = RGB_COLORS["sage"]

def add_hyperlink(paragraph, url, text, color="113927", underline=True, font_name=FONT_BODY, font_size=10.5, bold=True):
    """Inserta un hipervínculo nativo de Word clicable en el párrafo."""
    try:
        part = paragraph.part
        r_id = part.relate_to(url, docx.opc.constants.RELATIONSHIP_TYPE.HYPERLINK, is_external=True)

        hyperlink = parse_xml(
            f'<w:hyperlink xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main" '
            f'xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships" '
            f'r:id="{r_id}"/>'
        )
        new_run = parse_xml(f'<w:r xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"/>')
        new_run_text = parse_xml(f'<w:t xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main" xml:space="preserve">{text}</w:t>')
        new_run.append(new_run_text)
        
        new_run_prop = parse_xml(f'<w:rPr xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"/>')
        c = parse_xml(f'<w:color xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main" w:val="{color}"/>')
        new_run_prop.append(c)
        f = parse_xml(f'<w:rFonts xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main" w:ascii="{font_name}" w:hAnsi="{font_name}"/>')
        new_run_prop.append(f)
        sz = parse_xml(f'<w:sz xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main" w:val="{int(font_size*2)}"/>')
        new_run_prop.append(sz)
        if underline:
            u = parse_xml(f'<w:u xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main" w:val="single"/>')
            new_run_prop.append(u)
        if bold:
            b = parse_xml(f'<w:b xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"/>')
            new_run_prop.append(b)
            
        new_run.insert(0, new_run_prop)
        hyperlink.append(new_run)
        paragraph._p.append(hyperlink)
        return hyperlink
    except Exception as e:
        # Fallback a texto normal si falla la inserción de hipervínculo
        r = paragraph.add_run(text)
        r.font.name = font_name
        r.font.size = Pt(font_size)
        r.font.underline = underline
        return r

def format_inline_runs(paragraph, text, base_font=FONT_BODY, base_size=10.5, base_color="ink_green"):
    """Procesa negritas (**texto**), cursivas (*texto*), código (`texto`) e hiperenlaces markdown [texto](url)."""
    # 1. Separar por enlaces Markdown: [texto](url)
    link_parts = re.split(r'(\[.*?\]\(https?://[^\s\)]+\))', text)
    for part in link_parts:
        if not part:
            continue
        link_match = re.match(r'\[(.*?)\]\((https?://[^\s\)]+)\)', part)
        if link_match:
            anchor_text = link_match.group(1).replace('`', '').strip()
            url = link_match.group(2).strip()
            add_hyperlink(paragraph, url, anchor_text, color="113927", underline=True, font_name=base_font, font_size=base_size, bold=True)
            continue

        # 2. Procesar tokens de formato inline (negritas, cursivas, tags código)
        tokens = re.split(r'(\*\*.*?\*\*|\*.*?\*|`.*?`)', part)
        for token in tokens:
            if not token:
                continue
            if token.startswith('**') and token.endswith('**') and len(token) >= 4:
                content = token[2:-2]
                run = paragraph.add_run(content)
                run.font.name = base_font
                run.font.size = Pt(base_size)
                run.font.bold = True
                run.font.color.rgb = RGB_COLORS.get("pine", RGB_COLORS[base_color])
            elif token.startswith('*') and token.endswith('*') and len(token) >= 2:
                content = token[1:-1]
                run = paragraph.add_run(content)
                run.font.name = base_font
                run.font.size = Pt(base_size)
                run.font.italic = True
                run.font.color.rgb = RGB_COLORS[base_color]
            elif token.startswith('`') and token.endswith('`') and len(token) >= 2:
                content = token[1:-1]
                run = paragraph.add_run(content)
                run.font.name = "Consolas"
                run.font.size = Pt(base_size - 1)
                run.font.color.rgb = RGB_COLORS["pine"]
            else:
                run = paragraph.add_run(token)
                run.font.name = base_font
                run.font.size = Pt(base_size)
                run.font.color.rgb = RGB_COLORS[base_color]

def add_callout_box(doc, text, title="NOTA DESTACADA", box_type="info"):
    """Crea una caja destacada (callout) de estilo PSLL."""
    table = doc.add_table(rows=1, cols=1)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = False
    table.columns[0].width = Inches(6.5)
    
    cell = table.cell(0, 0)
    bg_hex = HEX_COLORS["mint"]
    border_hex = HEX_COLORS["sage"]
    icon = "💡"
    
    if box_type == "alert" or "alerta" in title.lower() or "trampa" in title.lower():
        bg_hex = HEX_COLORS["alert_bg"]
        border_hex = HEX_COLORS["coral"]
        icon = "⚠️"
    elif "misión" in title.lower() or "objetivo" in title.lower():
        bg_hex = HEX_COLORS["mint"]
        border_hex = HEX_COLORS["pine"]
        icon = "🎯"
    elif "decisión" in title.lower():
        bg_hex = HEX_COLORS["mint"]
        border_hex = HEX_COLORS["pine"]
        icon = "📌"

    set_cell_shading(cell, bg_hex)
    set_callout_borders(cell, border_hex, border_size_pt=24)
    set_cell_margins(cell, top_dpt=140, bottom_dpt=140, left_dpt=200, right_dpt=180)
    
    p = cell.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.LEFT
    p.paragraph_format.space_before = Pt(2)
    p.paragraph_format.space_after = Pt(4)
    r_tit = p.add_run(f"{icon} {title}\n")
    r_tit.font.name = FONT_HEADINGS
    r_tit.font.size = Pt(11)
    r_tit.font.bold = True
    r_tit.font.color.rgb = RGB_COLORS["pine"] if border_hex != HEX_COLORS["coral"] else RGB_COLORS["coral"]
    
    p_body = cell.add_paragraph()
    p_body.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p_body.paragraph_format.space_before = Pt(2)
    p_body.paragraph_format.space_after = Pt(2)
    format_inline_runs(p_body, text, base_font=FONT_BODY, base_size=10, base_color="ink_green")
    
    # Párrafo de separación posterior
    p_sep = doc.add_paragraph()
    p_sep.paragraph_format.space_before = Pt(0)
    p_sep.paragraph_format.space_after = Pt(6)

def parse_markdown_table(lines):
    """Parsea líneas de tabla markdown y devuelve una matriz de celdas limpias."""
    rows = []
    for line in lines:
        line = line.strip()
        if not line or not line.startswith('|'):
            continue
        parts = [p.strip() for p in line.split('|')[1:-1]]
        # Si es la línea de separación (|---|---|), saltarla
        if parts and all(re.match(r'^:?-+:?$', p) for p in parts):
            continue
        rows.append(parts)
    return rows

def render_table_to_docx(doc, rows):
    """Crea una tabla en Word estilizada según los estándares PSLL."""
    if not rows:
        return
    num_rows = len(rows)
    num_cols = max(len(r) for r in rows)
    
    table = doc.add_table(rows=num_rows, cols=num_cols)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = True
    
    for r_idx, row in enumerate(rows):
        is_header = (r_idx == 0)
        for c_idx in range(num_cols):
            cell = table.cell(r_idx, c_idx)
            val = row[c_idx] if c_idx < len(row) else ""
            
            p = cell.paragraphs[0]
            p.paragraph_format.space_before = Pt(3)
            p.paragraph_format.space_after = Pt(3)
            
            if is_header:
                set_cell_shading(cell, HEX_COLORS["pine"])
                set_cell_margins(cell, top_dpt=120, bottom_dpt=120, left_dpt=140, right_dpt=140)
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                run = p.add_run(val)
                run.font.name = FONT_HEADINGS
                run.font.size = Pt(10)
                run.font.bold = True
                run.font.color.rgb = RGB_COLORS["white"]
            else:
                bg_col = HEX_COLORS["white"] if r_idx % 2 == 1 else HEX_COLORS["mint"]
                set_cell_shading(cell, bg_col)
                set_cell_margins(cell, top_dpt=100, bottom_dpt=100, left_dpt=140, right_dpt=140)
                p.alignment = WD_ALIGN_PARAGRAPH.LEFT
                format_inline_runs(p, val, base_font=FONT_BODY, base_size=9.5, base_color="ink_green")
                
    set_table_borders(table)
    
    p_sep = doc.add_paragraph()
    p_sep.paragraph_format.space_before = Pt(4)
    p_sep.paragraph_format.space_after = Pt(8)

def convert_md_file(md_path: str, docx_path: str, header_topic: str):
    """Convierte un archivo markdown completo a documento Word maquetado."""
    print(f"[CONVERT] Procesando: {os.path.basename(md_path)} -> {os.path.basename(docx_path)}")
    with open(md_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        
    doc = Document()
    set_document_geometry(doc)
    setup_document_styles(doc)
    add_header_and_footer(doc, header_topic)
    
    # Extraer título del documento
    doc_title = "Documento Docente · EPD 2"
    doc_subtitle = "Políticas Sociolaborales y de Empleo"
    for line in lines[:10]:
        if line.startswith("# "):
            doc_title = line[2:].strip()
            break
        elif line.startswith("## "):
            doc_subtitle = line[3:].strip()
            
    add_institutional_cover_header(doc, doc_title, doc_subtitle)
    
    in_table = False
    table_lines = []
    in_callout = False
    callout_lines = []
    callout_title = "NOTA TÉCNICA"
    callout_type = "info"
    
    i = 0
    n = len(lines)
    while i < n:
        raw_line = lines[i]
        line = raw_line.strip()
        
        # 1. Gestión de tablas Markdown
        if line.startswith('|'):
            in_table = True
            table_lines.append(line)
            i += 1
            continue
        elif in_table:
            # Fin de tabla
            render_table_to_docx(doc, parse_markdown_table(table_lines))
            table_lines = []
            in_table = False
            
        # 2. Gestión de bloques de cita (Callout Boxes)
        if line.startswith('>'):
            in_callout = True
            content = line.lstrip('>').strip()
            if "**Decisión" in content or "**Misión" in content or "**Alerta" in content or "**Nota" in content:
                # Extraer título
                m = re.match(r'\*\*(.*?)\*\*(.*)', content)
                if m:
                    callout_title = m.group(1).strip()
                    callout_lines.append(m.group(2).strip())
                else:
                    callout_lines.append(content)
            else:
                callout_lines.append(content)
            i += 1
            continue
        elif in_callout:
            # Fin de callout
            full_text = " ".join([cl for cl in callout_lines if cl])
            add_callout_box(doc, full_text, title=callout_title, box_type=callout_type)
            callout_lines = []
            in_callout = False
            callout_title = "NOTA TÉCNICA"
            
        # Líneas vacías
        if not line:
            i += 1
            continue
            
        # Reglas horizontales
        if line in ("---", "***", "___"):
            p_sep = doc.add_paragraph()
            p_sep.paragraph_format.space_before = Pt(6)
            p_sep.paragraph_format.space_after = Pt(6)
            r_s = p_sep.add_run("· " * 25)
            r_s.font.size = Pt(8)
            r_s.font.color.rgb = RGB_COLORS["sage"]
            i += 1
            continue
            
        # 3. Títulos y Encabezados
        if line.startswith('# ') and i < 5:
            # Título principal ya tratado en cabecera institucional
            p = doc.add_paragraph()
            p.alignment = WD_ALIGN_PARAGRAPH.LEFT
            p.paragraph_format.space_before = Pt(8)
            p.paragraph_format.space_after = Pt(4)
            r = p.add_run(line[2:].strip())
            r.font.name = FONT_HEADINGS
            r.font.size = Pt(17)
            r.font.bold = True
            r.font.color.rgb = RGB_COLORS["pine"]
            i += 1
            continue
            
        if line.startswith('## '):
            p = doc.add_paragraph(style='Heading 1')
            p.paragraph_format.space_before = Pt(20)
            p.paragraph_format.space_after = Pt(5)
            p.paragraph_format.keep_with_next = True
            r = p.add_run(line[3:].strip())
            r.font.name = FONT_HEADINGS
            r.font.size = Pt(14)
            r.font.bold = True
            r.font.color.rgb = RGB_COLORS["pine"]
            i += 1
            continue
            
        if line.startswith('### '):
            p = doc.add_paragraph(style='Heading 2')
            p.paragraph_format.space_before = Pt(14)
            p.paragraph_format.space_after = Pt(4)
            p.paragraph_format.keep_with_next = True
            r = p.add_run(line[4:].strip())
            r.font.name = FONT_HEADINGS
            r.font.size = Pt(12)
            r.font.bold = True
            r.font.color.rgb = RGB_COLORS["sage"]
            i += 1
            continue

        if line.startswith('#### '):
            p = doc.add_paragraph(style='Heading 3')
            p.paragraph_format.space_before = Pt(10)
            p.paragraph_format.space_after = Pt(3)
            p.paragraph_format.keep_with_next = True
            r = p.add_run(line[5:].strip())
            r.font.name = FONT_HEADINGS
            r.font.size = Pt(11)
            r.font.bold = True
            r.font.color.rgb = RGB_COLORS["pine"]
            i += 1
            continue

        # 4. Viñetas y Listas
        if line.startswith(('- ', '* ', '+ ')):
            bullet_text = line[2:].strip()
            p = doc.add_paragraph(style='List Bullet')
            p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
            p.paragraph_format.space_before = Pt(1.5)
            p.paragraph_format.space_after = Pt(2.5)
            format_inline_runs(p, bullet_text, base_font=FONT_BODY, base_size=10.5, base_color="ink_green")
            i += 1
            continue
            
        m_num = re.match(r'^(\d+)\.\s+(.*)', line)
        if m_num:
            num_str = m_num.group(1)
            num_text = m_num.group(2)
            p = doc.add_paragraph()
            p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
            p.paragraph_format.left_indent = Inches(0.25)
            p.paragraph_format.first_line_indent = Inches(-0.25)
            p.paragraph_format.space_before = Pt(2)
            p.paragraph_format.space_after = Pt(3)
            r_num = p.add_run(f"{num_str}. ")
            r_num.font.name = FONT_BODY
            r_num.font.bold = True
            r_num.font.color.rgb = RGB_COLORS["pine"]
            format_inline_runs(p, num_text, base_font=FONT_BODY, base_size=10.5, base_color="ink_green")
            i += 1
            continue

        # 5. Párrafos ordinarios
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(4.5)
        p.paragraph_format.line_spacing = 1.15
        format_inline_runs(p, line, base_font=FONT_BODY, base_size=10.5, base_color="ink_green")
        i += 1
        
    # Limpieza final de tablas o callouts si quedaron al final
    if in_table:
        render_table_to_docx(doc, parse_markdown_table(table_lines))
    if in_callout:
        full_text = " ".join([cl for cl in callout_lines if cl])
        add_callout_box(doc, full_text, title=callout_title, box_type=callout_type)
        
    doc.save(docx_path)
    print(f"[OK] Documento guardado con éxito: {docx_path}")

def main():
    target_dir = os.path.join(WORKSPACE_DIR, "EPD", "EPD 2")
    files_to_convert = [
        ("guion_docente_epd_02.md", "guion_docente_epd_02.docx", "GUÍA DOCENTE · EPD 2"),
        ("hoja_trabajo_estudiante_epd_02.md", "hoja_trabajo_estudiante_epd_02.docx", "LABORATORIO PRÁCTICO · EPD 2"),
        ("propuesta_coordinacion_juanma_pablo.md", "propuesta_coordinacion_juanma_pablo.docx", "COORDINACIÓN DOCENTE · EPD 2")
    ]
    
    for md_name, docx_name, topic in files_to_convert:
        md_file = os.path.join(target_dir, md_name)
        docx_file = os.path.join(target_dir, docx_name)
        if os.path.exists(md_file):
            convert_md_file(md_file, docx_file, topic)
        else:
            print(f"[WARN] No se encontró el archivo: {md_file}")

if __name__ == "__main__":
    main()
