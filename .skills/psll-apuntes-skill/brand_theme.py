"""
brand_theme.py - Design tokens y utilidades XML para la maquetación corporativa de PSLL.
Paleta oficial: Menta, Salvia, Verde Profundo, Verde Tinta, Coral, Melocotón.
"""

from docx.shared import Inches, Pt, RGBColor
from docx.oxml import parse_xml, OxmlElement
from docx.oxml.ns import nsdecls, qn

# Paleta cromática oficial de PSLL (BRAND.md)
HEX_COLORS = {
    "mint": "E1F6EA",         # Lienzo, fondos suaves
    "sage": "76927A",         # Estructura, H2, bordes concepto
    "deep_green": "566B56",   # Títulos principales, H1, cabeceras tablas
    "ink_green": "2F3A30",    # Texto de cuerpo (nunca negro puro)
    "coral": "E99073",        # Acentos, llamadas de atención, alertas
    "peach": "EDB090",        # Acentos secundarios
    "warm_cream": "F3EFDC",   # Fondo de tarjetas / neutro cálido
    "white": "FFFFFF",        # Fondos neutros y texto sobre oscuro
    "light_gray": "D0DCD2",   # Líneas divisorias y bordes sutiles
    "alert_bg": "FDF4F0",     # Fondo muy suave para alertas coral
}

RGB_COLORS = {
    "mint": RGBColor(225, 246, 234),
    "sage": RGBColor(118, 146, 122),
    "deep_green": RGBColor(86, 107, 86),
    "ink_green": RGBColor(47, 58, 48),
    "coral": RGBColor(233, 144, 115),
    "peach": RGBColor(237, 176, 144),
    "warm_cream": RGBColor(243, 239, 220),
    "white": RGBColor(255, 255, 255),
    "light_gray": RGBColor(208, 220, 210),
}

# Tipografías oficiales
FONT_HEADINGS = "Poppins"
FONT_BODY = "Calibri"
FONT_FALLBACK = "Century Schoolbook"

def set_cell_shading(cell, color_hex: str):
    """Aplica sombreado de fondo a una celda de tabla en Word."""
    tcPr = cell._tc.get_or_add_tcPr()
    # Eliminar sombreado anterior si existe
    for child in list(tcPr):
        if child.tag.endswith('shd'):
            tcPr.remove(child)
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:val="clear" w:color="auto" w:fill="{color_hex}"/>')
    tcPr.append(shd)

def set_cell_margins(cell, top_dpt=140, bottom_dpt=140, left_dpt=200, right_dpt=180):
    """Establece márgenes interiores (padding) de una celda en dxa (1 pt = 20 dxa)."""
    tcPr = cell._tc.get_or_add_tcPr()
    for child in list(tcPr):
        if child.tag.endswith('tcMar'):
            tcPr.remove(child)
    tcMar = parse_xml(
        f'<w:tcMar {nsdecls("w")}>'
        f'  <w:top w:w="{top_dpt}" w:type="dxa"/>'
        f'  <w:left w:w="{left_dpt}" w:type="dxa"/>'
        f'  <w:bottom w:w="{bottom_dpt}" w:type="dxa"/>'
        f'  <w:right w:w="{right_dpt}" w:type="dxa"/>'
        f'</w:tcMar>'
    )
    tcPr.append(tcMar)

def set_callout_borders(cell, border_color_hex: str, border_size_pt: int = 24):
    """Aplica un borde izquierdo grueso (estilo callout box) y elimina los demás."""
    tcPr = cell._tc.get_or_add_tcPr()
    for child in list(tcPr):
        if child.tag.endswith('tcBorders'):
            tcPr.remove(child)
    borders = parse_xml(
        f'<w:tcBorders {nsdecls("w")}>'
        f'  <w:top w:val="none"/>'
        f'  <w:left w:val="single" w:sz="{border_size_pt}" w:space="0" w:color="{border_color_hex}"/>'
        f'  <w:bottom w:val="none"/>'
        f'  <w:right w:val="none"/>'
        f'</w:tcBorders>'
    )
    tcPr.append(borders)

def set_table_borders(table, border_color_hex: str = "D0DCD2"):
    """Establece bordes limpios y discretos para una tabla académica."""
    tblPr = table._tbl.tblPr
    for child in list(tblPr):
        if child.tag.endswith('tblBorders'):
            tblPr.remove(child)
    borders = parse_xml(
        f'<w:tblBorders {nsdecls("w")}>'
        f'  <w:top w:val="single" w:sz="6" w:space="0" w:color="{HEX_COLORS["deep_green"]}"/>'
        f'  <w:bottom w:val="single" w:sz="6" w:space="0" w:color="{HEX_COLORS["deep_green"]}"/>'
        f'  <w:insideH w:val="single" w:sz="4" w:space="0" w:color="{border_color_hex}"/>'
        f'  <w:left w:val="none"/>'
        f'  <w:right w:val="none"/>'
        f'  <w:insideV w:val="none"/>'
        f'</w:tblBorders>'
    )
    tblPr.append(borders)
