"""
brand_theme.py - Design tokens y utilidades XML para la maquetación corporativa de PSLL.
Paleta oficial: Verde Pino PSLL (#113927), Verde Salvia (#76927A), Coral Active Wave (#E98F71),
Verde Menta Tenue (#F4F8F5), Verde Tinta (#2F3A30), Azul Marino UPO (#0B1C36).
"""

from docx.shared import Inches, Pt, RGBColor
from docx.oxml import parse_xml, OxmlElement
from docx.oxml.ns import nsdecls, qn

# Paleta cromática oficial de PSLL (BRAND.md)
HEX_COLORS = {
    "pine": "113927",         # Color primario titular, Verde Pino PSLL
    "deep_green": "113927",   # Títulos principales, H1, cabeceras tablas (alias a pine)
    "sage": "76927A",         # Estructura, H2, bordes concepto, Verde Salvia
    "coral": "E98F71",        # Acento dinámico, alertas, llamadas de atención
    "mint": "F4F8F5",         # Fondos suaves, tarjetas y callouts (Mint Whisper)
    "ink_green": "2F3A30",    # Texto de cuerpo (Verde Tinta, nunca negro puro)
    "peach": "EDB090",        # Acentos secundarios
    "warm_cream": "F4F8F5",   # Fondo neutro tarjetas (Mint Whisper)
    "white": "FFFFFF",        # Fondos neutros y texto sobre oscuro
    "border_slate": "E2E8F0", # Retículas, bordes de tabla y separadores
    "light_gray": "E2E8F0",   # Líneas divisorias y bordes sutiles
    "alert_bg": "FDF4F0",     # Fondo muy suave para alertas coral
    "upo_navy": "0B1C36",     # Azul Marino UPO (presencia institucional)
}

RGB_COLORS = {
    "pine": RGBColor(17, 57, 39),
    "deep_green": RGBColor(17, 57, 39),
    "sage": RGBColor(118, 146, 122),
    "coral": RGBColor(233, 143, 113),
    "mint": RGBColor(244, 248, 245),
    "ink_green": RGBColor(47, 58, 48),
    "peach": RGBColor(237, 176, 144),
    "warm_cream": RGBColor(244, 248, 245),
    "white": RGBColor(255, 255, 255),
    "border_slate": RGBColor(226, 232, 240),
    "light_gray": RGBColor(226, 232, 240),
    "upo_navy": RGBColor(11, 28, 54),
}

# Tipografías oficiales
FONT_HEADINGS = "Outfit"
FONT_BODY = "Calibri"
FONT_FALLBACK = "Inter"

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
