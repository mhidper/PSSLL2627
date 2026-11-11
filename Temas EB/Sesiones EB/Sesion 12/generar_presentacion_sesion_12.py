# -*- coding: utf-8 -*-
"""
Generador oficial de la presentación en Formato 1 (.pptx + .pdf) para la Sesión EB 12:
«Flexibilidad externa, protección del empleo (EPL) y dualidad laboral»
Asignatura: Políticas Sociolaborales y de Empleo (UPO)
Profesor: Manuel A. Hidalgo Pérez
"""

import os
import subprocess
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE

# 1. Rutas
BASE_DIR = r"c:\Users\Usuario\Documents\Dropbox\DOCENCIA UPO\CURSO 26-27\PSLL"
SESION_DIR = os.path.join(BASE_DIR, r"Temas EB\Sesiones EB\Sesion 12")
LOGOS_DIR = os.path.join(BASE_DIR, "Logos y skills")
SKILL_ASSETS_DIR = os.path.join(LOGOS_DIR, "psll-presentaciones-skill", "assets")

LOGO_PSLL = os.path.join(LOGOS_DIR, "logo_psll_upo.png")
LOGO_UPO = os.path.join(SKILL_ASSETS_DIR, "upo_logo.jpg")
LOCKUP_PSLL = os.path.join(LOGOS_DIR, "psll_lockup.png")

FIG_4_1 = os.path.join(SESION_DIR, "figura_4_1_flexiseguridad_vs_dualidad.png")
FIG_4_2 = os.path.join(SESION_DIR, "figura_4_2_epl_ocde_comparativa.png")
FIG_4_3 = os.path.join(SESION_DIR, "figura_4_3_temporalidad_reformas_espana.png")
FIG_4_4 = os.path.join(SESION_DIR, "figura_4_4_coste_despido_antiguedad.png")

QR_SONDEO = os.path.join(SESION_DIR, "qr_sondeo_sesion12.png")
QR_APP = os.path.join(SESION_DIR, "qr_app_sesion12.png")
QR_RETO = os.path.join(SESION_DIR, "qr_reto_sesion12.png")
QR_PASAPORTE = os.path.join(SESION_DIR, "qr_pasaporte_psll.png")

OUTPUT_PPTX = os.path.join(SESION_DIR, "Sesion 12 - Flexibilidad externa, proteccion del empleo y dualidad laboral.pptx")
OUTPUT_PDF = os.path.join(SESION_DIR, "Sesion 12 - Flexibilidad externa, proteccion del empleo y dualidad laboral.pdf")

# 2. Paleta Oficial de Marca PSLL
PINO = RGBColor(17, 57, 39)          # #113927 (Primario)
PINO_DARK = RGBColor(11, 36, 25)     # #0B2419
SALVIA = RGBColor(118, 146, 122)     # #76927A (Estructura/Subtítulos)
CORAL = RGBColor(233, 143, 113)      # #E98F71 (Acento dinámico)
MENTA = RGBColor(244, 248, 245)      # #F4F8F5 (Fondo de tarjetas)
PAPEL_PRENSA = RGBColor(250, 248, 244) # #FAF8F4 (Fondo recorte de prensa)
TINTA = RGBColor(47, 58, 48)         # #2F3A30 (Texto lectura)
MELOCOTON = RGBColor(237, 176, 144)  # #EDB090
BLANCO = RGBColor(255, 255, 255)     # #FFFFFF
BORDE_MENTA = RGBColor(194, 216, 201) # #C2D8C9
BORDE_CORAL = RGBColor(233, 143, 113)

# 3. Inicializar Presentación Widescreen 16:9
prs = Presentation()
prs.slide_width = Inches(13.333)
prs.slide_height = Inches(7.500)
blank_layout = prs.slide_layouts[6]

TOTAL_SLIDES = 25

def set_slide_background(slide, color):
    background = slide.background
    fill = background.fill
    fill.solid()
    fill.fore_color.rgb = color

def add_header(slide, categoria, titulo, slide_num):
    tx_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.4), Inches(10.5), Inches(0.35))
    tf = tx_box.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = categoria.upper()
    p.font.name = "Outfit"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = SALVIA

    tx_box2 = slide.shapes.add_textbox(Inches(0.8), Inches(0.72), Inches(10.8), Inches(0.55))
    tf2 = tx_box2.text_frame
    tf2.word_wrap = True
    p2 = tf2.paragraphs[0]
    p2.text = titulo
    p2.font.name = "Outfit"
    p2.font.size = Pt(20)
    p2.font.bold = True
    p2.font.color.rgb = PINO

    if os.path.exists(LOCKUP_PSLL):
        slide.shapes.add_picture(LOCKUP_PSLL, Inches(11.8), Inches(0.42), width=Inches(1.013), height=Inches(0.320))

    tx_page = slide.shapes.add_textbox(Inches(11.5), Inches(6.95), Inches(1.3), Inches(0.3))
    tf_page = tx_page.text_frame
    p_page = tf_page.paragraphs[0]
    p_page.text = f"{slide_num} / {TOTAL_SLIDES}"
    p_page.alignment = PP_ALIGN.RIGHT
    p_page.font.name = "Outfit"
    p_page.font.size = Pt(10)
    p_page.font.color.rgb = SALVIA

def add_card(slide, left, top, width, height, bg_color=MENTA, border_color=BORDE_MENTA, border_width=Pt(1)):
    shape = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
    shape.fill.solid()
    shape.fill.fore_color.rgb = bg_color
    if border_color:
        shape.line.color.rgb = border_color
        shape.line.width = border_width
    else:
        shape.line.fill.background()
    return shape

# ==============================================================================
# SLIDE 1: PORTADA OFICIAL CANÓNICA (Ratio exacto 1.833 y 0.707)
# ==============================================================================
s1 = prs.slides.add_slide(blank_layout)
set_slide_background(s1, PINO)

if os.path.exists(LOGO_PSLL):
    s1.shapes.add_picture(LOGO_PSLL, Inches(4.267), Inches(0.550), width=Inches(4.800), height=Inches(2.618))

tb_s1 = s1.shapes.add_textbox(Inches(1.000), Inches(3.350), Inches(11.333), Inches(0.600))
p_over = tb_s1.text_frame.paragraphs[0]
p_over.alignment = PP_ALIGN.CENTER
p_over.text = "POLÍTICAS SOCIOLABORALES Y DE EMPLEO"
p_over.font.name = "Outfit"
p_over.font.size = Pt(25)
p_over.font.bold = True
p_over.font.color.rgb = BLANCO

tb_s1_sub = s1.shapes.add_textbox(Inches(0.800), Inches(4.000), Inches(11.733), Inches(0.550))
p_tit = tb_s1_sub.text_frame.paragraphs[0]
p_tit.alignment = PP_ALIGN.CENTER
p_tit.text = "Sesión 12 – Flexibilidad Externa, Protección del Empleo (EPL) y Dualidad"
p_tit.font.name = "Outfit"
p_tit.font.size = Pt(18)
p_tit.font.bold = True
p_tit.font.color.rgb = CORAL

tb_s1_meta = s1.shapes.add_textbox(Inches(1.000), Inches(4.600), Inches(11.333), Inches(0.400))
p_meta = tb_s1_meta.text_frame.paragraphs[0]
p_meta.alignment = PP_ALIGN.CENTER
p_meta.text = "Semana 9  ·  Tema 4 (I)  ·  Código 102023  ·  Manuel A. Hidalgo Pérez"
p_meta.font.name = "Calibri"
p_meta.font.size = Pt(13)
p_meta.font.color.rgb = RGBColor(244, 248, 245)

s1_footer = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.0), Inches(6.600), Inches(13.333), Inches(0.900))
s1_footer.fill.solid()
s1_footer.fill.fore_color.rgb = BLANCO
s1_footer.line.fill.background()

if os.path.exists(LOGO_UPO):
    s1.shapes.add_picture(LOGO_UPO, Inches(0.500), Inches(6.700), width=Inches(0.495), height=Inches(0.700))

tb_s1_inst = s1.shapes.add_textbox(Inches(1.300), Inches(6.850), Inches(11.300), Inches(0.400))
p_inst = tb_s1_inst.text_frame.paragraphs[0]
p_inst.text = "Grado en Relaciones Laborales y Recursos Humanos · Doble Grado en Derecho y RRLL-RRHH · Universidad Pablo de Olavide"
p_inst.font.name = "Calibri"
p_inst.font.size = Pt(11)
p_inst.font.color.rgb = TINTA

# ==============================================================================
# SLIDE 2: HOJA DE RUTA PEDAGÓGICA (120 MINUTOS)
# ==============================================================================
s2 = prs.slides.add_slide(blank_layout)
set_slide_background(s2, BLANCO)
add_header(s2, "Metodología de Aula · Curso 2026-27", "Hoja de Ruta · Arquitectura en 5 Fases de la Sesión 12 (120 min)", 2)

fases_data = [
    ("Fase 1 · 00–20 min", "Apertura con Recorte de Prensa y Sondeo", "Recorte de Cinco Días / El País sobre el desplome de la temporalidad privada (12,4%), el bloqueo público (>30%) y el fijo discontinuo. Sondeo Forms y choque empírico.", PINO),
    ("Fase 2 · 20–45 min", "Mini-Lección I: Flexibilidad, Dualidad y EPL", "Taxonomía de Atkinson (externa vs. interna). El Triángulo de Oro de la flexiseguridad danesa frente a la dualidad española. Indicador EPL de la OCDE y brecha ΔEPL.", SALVIA),
    ("Fase 3 · 45–70 min", "Mini-Lección II: Despido y RDL 32/2021", "Costes de despido en España (12, 20, 33 y doble tramo 45/33 días; ERE art. 51 ET y despido nulo). La Reforma Laboral (RDL 32/2021) y el fijo discontinuo (DENO vs. EPA).", PINO),
    ("Fase 4 · 70–85 min", "Laboratorio con Micro-App", "Móviles activos (15 min): simulación de indemnizaciones de despido, brecha de dualidad ΔEPL y auditoría estadística SEPE/EPA en simulador_epl_dualidad.html.", CORAL),
    ("Fase 5 · 85–120 min", "Reto Manuscrito y Evaluación", "Síntesis en pizarra (10 min), reto individual en papel sin pantallas (10 min), subida con QR a Forms y feedback formativo inmediato con rúbrica (0–1.000 pts).", PINO)
]

y_pos = Inches(1.45)
for f_tag, f_tit, f_desc, f_col in fases_data:
    add_card(s2, Inches(0.8), y_pos, Inches(11.733), Inches(0.95), MENTA, BORDE_MENTA)
    pill = s2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.95), y_pos + Inches(0.18), Inches(2.2), Inches(0.58))
    pill.fill.solid()
    pill.fill.fore_color.rgb = f_col
    pill.line.fill.background()
    p_pill = pill.text_frame.paragraphs[0]
    p_pill.text = f_tag
    p_pill.alignment = PP_ALIGN.CENTER
    p_pill.font.name = "Outfit"
    p_pill.font.size = Pt(11)
    p_pill.font.bold = True
    p_pill.font.color.rgb = BLANCO

    tb = s2.shapes.add_textbox(Inches(3.3), y_pos + Inches(0.08), Inches(9.0), Inches(0.8))
    tf = tb.text_frame
    tf.word_wrap = True
    p1 = tf.paragraphs[0]
    p1.text = f_tit
    p1.font.name = "Outfit"
    p1.font.size = Pt(13)
    p1.font.bold = True
    p1.font.color.rgb = PINO

    p2 = tf.add_paragraph()
    p2.text = f_desc
    p2.font.name = "Calibri"
    p2.font.size = Pt(11.5)
    p2.font.color.rgb = TINTA
    y_pos += Inches(1.05)

# ==============================================================================
# SLIDE 3: FASE 1 · APERTURA CON GANCHO (RECORTE DE PRENSA FUNDAMENTAL)
# ==============================================================================
s3 = prs.slides.add_slide(blank_layout)
set_slide_background(s3, BLANCO)
add_header(s3, "Fase 1 (00–20 min) · Apertura y Recorte de Prensa Disparador", "El Debate Público: «El milagro de los indefinidos y el enigma del fijo discontinuo»", 3)

# Tarjeta Recorte de Prensa (Estilo periódico económico)
add_card(s3, Inches(0.8), Inches(1.45), Inches(7.55), Inches(5.3), PAPEL_PRENSA, PINO, Pt(1.5))
mast_line = s3.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(1.05), Inches(1.86), Inches(7.05), Inches(0.025))
mast_line.fill.solid()
mast_line.fill.fore_color.rgb = PINO
mast_line.line.fill.background()

tb_s3 = s3.shapes.add_textbox(Inches(1.05), Inches(1.52), Inches(7.05), Inches(5.05))
tf_s3 = tb_s3.text_frame
tf_s3.word_wrap = True

p_art_tag = tf_s3.paragraphs[0]
p_art_tag.text = "📰 CINCO DÍAS / EL PAÍS ECONOMÍA · ANÁLISIS DEL MERCADO DE TRABAJO"
p_art_tag.font.name = "Outfit"
p_art_tag.font.size = Pt(10.5)
p_art_tag.font.bold = True
p_art_tag.font.color.rgb = CORAL

p_art_tit = tf_s3.add_paragraph()
p_art_tit.text = "«La temporalidad privada cae al mínimo histórico del 12,4% tras el RDL 32/2021, pero el sector público supera el 30% y los fijos discontinuos abren la batalla estadística»"
p_art_tit.font.name = "Georgia"
p_art_tit.font.size = Pt(14)
p_art_tit.font.bold = True
p_art_tit.space_before = Pt(15)
p_art_tit.font.color.rgb = PINO

bullets_s3 = [
    ("1. El vuelco en la contratación privada:", " La supresión del contrato por obra o servicio ha elevado la cuota de nuevos indefinidos del 10% histórico a más del 44%, hundiendo la temporalidad privada del 29,2% al 12,4% (en línea con el 13,5% de la UE)."),
    ("2. La paradoja del Estado empleador:", " Mientras se sanciona a las empresas privadas por abusar de contratos cortos, las Administraciones Públicas mantienen un 31% de interinos y temporales en sanidad, educación y justicia."),
    ("3. El boom del fijo discontinuo y el limbo estadístico:", " Su firma se ha multiplicado por diez. En los meses de inactividad, el trabajador cobra el paro pero el SEPE lo registra como DENO (Demandante No Ocupado) y no aparece en la lista del Paro Registrado».")
]
for b_tit, b_desc in bullets_s3:
    p_b = tf_s3.add_paragraph()
    p_b.font.name = "Calibri"
    p_b.font.size = Pt(12.2)
    p_b.space_before = Pt(7)
    r1 = p_b.add_run()
    r1.text = "• " + b_tit
    r1.font.bold = True
    r1.font.color.rgb = PINO
    r2 = p_b.add_run()
    r2.text = b_desc
    r2.font.color.rgb = TINTA

# Tarjeta lateral de reflexión / Cliffhanger
add_card(s3, Inches(8.55), Inches(1.45), Inches(3.98), Inches(5.3), BLANCO, BORDE_CORAL, Pt(1.5))
tb_s3_lat = s3.shapes.add_textbox(Inches(8.8), Inches(1.65), Inches(3.5), Inches(4.9))
tf_s3_lat = tb_s3_lat.text_frame
tf_s3_lat.word_wrap = True

p_lat_h = tf_s3_lat.paragraphs[0]
p_lat_h.text = "Dilemas para el Aula"
p_lat_h.font.name = "Outfit"
p_lat_h.font.size = Pt(15)
p_lat_h.font.bold = True
p_lat_h.font.color.rgb = CORAL

p_lat_body = tf_s3_lat.add_paragraph()
p_lat_body.font.name = "Calibri"
p_lat_body.font.size = Pt(13)
p_lat_body.space_before = Pt(10)
p_lat_body.text = "1. ¿Por qué durante 35 años (1984–2021) el 90% de los contratos firmados cada mes en España eran temporales?\n\n2. ¿Hemos acabado realmente con la precariedad o una parte de la rotación temporal se ha trasladado hacia contratos fijos discontinuos e indefinidos que duran pocos meses?\n\n3. ¿Dónde cuenta un fijo discontinuo cuando su hotel cierra en invierno?"
p_lat_body.font.color.rgb = TINTA

# ==============================================================================
# SLIDE 4: FASE 1 · LOS DOS ENIGMAS DE AULA
# ==============================================================================
s4 = prs.slides.add_slide(blank_layout)
set_slide_background(s4, BLANCO)
add_header(s4, "Fase 1 (00–20 min) · Planteamiento del Enigma Económico y Jurídico", "¿Por Qué España Fue la Campeona Europea de la Temporalidad y Qué Ha Cambiado?", 4)

add_card(s4, Inches(0.8), Inches(1.45), Inches(5.7), Inches(5.3), MENTA, BORDE_MENTA)
tb_s4_1 = s4.shapes.add_textbox(Inches(1.05), Inches(1.65), Inches(5.2), Inches(4.9))
tf_s4_1 = tb_s4_1.text_frame
tf_s4_1.word_wrap = True

p_e1 = tf_s4_1.paragraphs[0]
p_e1.text = "Enigma 1 · El Abismo de la Dualidad (ΔEPL)"
p_e1.font.name = "Outfit"
p_e1.font.size = Pt(15)
p_e1.font.bold = True
p_e1.font.color.rgb = PINO

p_e1_b = tf_s4_1.add_paragraph()
p_e1_b.font.name = "Calibri"
p_e1_b.font.size = Pt(13)
p_e1_b.space_before = Pt(10)
p_e1_b.text = "Imagina que diriges el departamento de RRHH de una empresa:\n\n• Extinguir un contrato temporal al vencer su plazo cuesta 12 días de salario por año y no tiene litigiosidad judicial.\n• Despedir a un trabajador indefinido cuya causa económica sea tumbada por un juez (improcedente) cuesta 33 días por año (o 45 días antes de 2012).\n• Además, existía una figura ('obra o servicio') que permitía contratar temporalmente para casi cualquier actividad rutinaria.\n\nResultado racional: La empresa usa a los temporales como colchón de ajuste y los despide el día antes de cumplir el límite legal para no hacerlos fijos."
p_e1_b.font.color.rgb = TINTA

add_card(s4, Inches(6.8), Inches(1.45), Inches(5.733), Inches(5.3), MENTA, BORDE_MENTA)
tb_s4_2 = s4.shapes.add_textbox(Inches(7.05), Inches(1.65), Inches(5.2), Inches(4.9))
tf_s4_2 = tb_s4_2.text_frame
tf_s4_2.word_wrap = True

p_e2 = tf_s4_2.paragraphs[0]
p_e2.text = "Enigma 2 · El Misterio del Fijo Discontinuo"
p_e2.font.name = "Outfit"
p_e2.font.size = Pt(15)
p_e2.font.bold = True
p_e2.font.color.rgb = PINO

p_e2_b = tf_s4_2.add_paragraph()
p_e2_b.font.name = "Calibri"
p_e2_b.font.size = Pt(13)
p_e2_b.space_before = Pt(10)
p_e2_b.text = "Una trabajadora con contrato fijo discontinuo en un hotel de la Costa del Sol termina la temporada el 31 de octubre:\n\n• Durante noviembre, diciembre, enero y febrero no trabaja ni cobra sueldo de la empresa.\n• Acude al SEPE y cobra su prestación contributiva por desempleo.\n• Sin embargo, su contrato no se ha extinguido: sigue vigente pero en periodo de inactividad a la espera del llamamiento de marzo.\n\nPregunta clave: ¿Cuenta esta trabajadora como parada en la cifra oficial de Paro Registrado del SEPE? ¿Y cómo la clasifica la EPA del INE?"
p_e2_b.font.color.rgb = TINTA

# ==============================================================================
# SLIDE 5: FASE 1 · SONDEO EN DIRECTO CON FORMS (MÓVILES ACTIVOS)
# ==============================================================================
s5 = prs.slides.add_slide(blank_layout)
set_slide_background(s5, BLANCO)
add_header(s5, "Fase 1 (00–20 min) · Participación en Directo (Móviles Activos)", "Sondeo de Aula: ¿Cómo Cuenta un Fijo Discontinuo en Periodo de Inactividad?", 5)

add_card(s5, Inches(0.8), Inches(1.45), Inches(7.5), Inches(5.3), MENTA, BORDE_MENTA)
tb_s5_p = s5.shapes.add_textbox(Inches(1.1), Inches(1.7), Inches(6.9), Inches(4.8))
tf_s5_p = tb_s5_p.text_frame
tf_s5_p.word_wrap = True

p_s5_h = tf_s5_p.paragraphs[0]
p_s5_h.text = "Pregunta del Sondeo Previo (1 minuto):"
p_s5_h.font.name = "Outfit"
p_s5_h.font.size = Pt(16)
p_s5_h.font.bold = True
p_s5_h.font.color.rgb = PINO

p_s5_sub = tf_s5_p.add_paragraph()
p_s5_sub.text = "Cuando un trabajador fijo discontinuo termina su campaña anual, pasa a la inactividad sin sueldo y cobra el paro en el SEPE, ¿cómo se contabiliza en las estadísticas oficiales?"
p_s5_sub.font.name = "Calibri"
p_s5_sub.font.size = Pt(13.5)
p_s5_sub.space_before = Pt(8)
p_s5_sub.font.color.rgb = TINTA

opts = [
    ("[Opción A]", "Suma como un parado más tanto en el Paro Registrado del SEPE como en la Encuesta de Población Activa (EPA)."),
    ("[Opción B]", "NO cuenta como Paro Registrado en el SEPE (figura como Demandante No Ocupado - DENO), pero SÍ cuenta como parado en la EPA si busca otro empleo."),
    ("[Opción C]", "Sigue contando como ocupado en activo en la EPA durante los meses que está en su casa porque su contrato es indefinido.")
]
for o_tag, o_txt in opts:
    p_opt = tf_s5_p.add_paragraph()
    p_opt.space_before = Pt(10)
    p_opt.font.name = "Calibri"
    p_opt.font.size = Pt(13)
    r_tag = p_opt.add_run()
    r_tag.text = o_tag + " "
    r_tag.font.bold = True
    r_tag.font.color.rgb = CORAL
    r_txt = p_opt.add_run()
    r_txt.text = o_txt
    r_txt.font.color.rgb = TINTA

add_card(s5, Inches(8.55), Inches(1.45), Inches(3.98), Inches(5.3), BLANCO, BORDE_CORAL, Pt(1.5))
tb_s5_qr = s5.shapes.add_textbox(Inches(8.75), Inches(1.65), Inches(3.6), Inches(1.0))
tf_s5_qr = tb_s5_qr.text_frame
tf_s5_qr.word_wrap = True
p_qr_h = tf_s5_qr.paragraphs[0]
p_qr_h.text = "¡Escanea y Vota!"
p_qr_h.alignment = PP_ALIGN.CENTER
p_qr_h.font.name = "Outfit"
p_qr_h.font.size = Pt(16)
p_qr_h.font.bold = True
p_qr_h.font.color.rgb = PINO

p_qr_sub = tf_s5_qr.add_paragraph()
p_qr_sub.text = "Microsoft Forms UPO\n(Votación anónima en vivo)"
p_qr_sub.alignment = PP_ALIGN.CENTER
p_qr_sub.font.name = "Calibri"
p_qr_sub.font.size = Pt(11)
p_qr_sub.font.color.rgb = SALVIA

if os.path.exists(QR_SONDEO):
    s5.shapes.add_picture(QR_SONDEO, Inches(9.2), Inches(2.75), width=Inches(2.7), height=Inches(2.7))

tb_s5_url = s5.shapes.add_textbox(Inches(8.75), Inches(5.75), Inches(3.6), Inches(0.8))
p_url = tb_s5_url.text_frame.paragraphs[0]
p_url.alignment = PP_ALIGN.CENTER
p_url.text = "forms.office.com/e/PSLL-Sondeo-Sesion12\nSolo dispositivos autorizados para el sondeo"
p_url.font.name = "Calibri"
p_url.font.size = Pt(9.5)
p_url.font.color.rgb = SALVIA

# ==============================================================================
# SLIDE 6: FASE 1 · CHOQUE EMPÍRICO I (FIGURA 4.3 TEMPORALIDAD Y REFORMAS)
# ==============================================================================
s6 = prs.slides.add_slide(blank_layout)
set_slide_background(s6, BLANCO)
add_header(s6, "Fase 1 (00–20 min) · Choque Empírico con Datos Oficiales (EPA / INE)", "Figura 4.3 · El Desplome de la Temporalidad Privada (12,4%) frente al Sector Público (>30%)", 6)

if os.path.exists(FIG_4_3):
    s6.shapes.add_picture(FIG_4_3, Inches(0.8), Inches(1.40), width=Inches(11.733), height=Inches(3.90))

add_card(s6, Inches(0.8), Inches(5.42), Inches(11.733), Inches(1.40), MENTA, BORDE_MENTA)
tb_s6_inf = s6.shapes.add_textbox(Inches(1.0), Inches(5.48), Inches(11.3), Inches(1.25))
tf_s6_inf = tb_s6_inf.text_frame
tf_s6_inf.word_wrap = True

b_s6 = [
    ("1. Convergencia privada histórica: ", "Tras el RDL 32/2021, la temporalidad en el sector privado cayó del 29,2% (2018) al 12,4% (2024–2025), situando la tasa agregada en el 15,8% (mínimo desde 1987).", PINO),
    ("2. La anomalía del sector público: ", "Las Administraciones Públicas mantienen un 31,2% de temporalidad (sanidad, educación y administración local) por la lentitud en estabilizar plazas interinas (Ley 20/2021).", CORAL),
    ("3. Sustitución de modalidades: ", "La eliminación del contrato de obra o servicio trasladó el flujo de entrada hacia indefinidos ordinarios y fijos discontinuos.", PINO)
]
for idx, (bt, bd, bc) in enumerate(b_s6):
    p = tf_s6_inf.paragraphs[0] if idx == 0 else tf_s6_inf.add_paragraph()
    p.font.name = "Calibri"
    p.font.size = Pt(11.8)
    r1 = p.add_run()
    r1.text = bt
    r1.font.bold = True
    r1.font.color.rgb = bc
    r2 = p.add_run()
    r2.text = bd
    r2.font.color.rgb = TINTA

# ==============================================================================
# SLIDE 7: FASE 1 · CHOQUE EMPÍRICO II (RESOLUCIÓN DEL SONDEO: SEPE VS EPA)
# ==============================================================================
s7 = prs.slides.add_slide(blank_layout)
set_slide_background(s7, BLANCO)
add_header(s7, "Fase 1 (00–20 min) · Resolución del Enigma Estadístico", "¿Dónde Están los Fijos Discontinuos Inactivos? Registro SEPE (DENO) vs. EPA (INE)", 7)

cols_s7 = [
    ("EN PERIODO DE ACTIVIDAD", "Trabajando en Campaña", [
        "Relación laboral: Contrato indefinido fijo discontinuo en ejecución activa.",
        "Seguridad Social (TGSS): Afiliado en situación de ALTA y cotizando.",
        "Registro SEPE: No figura como demandante de empleo.",
        "Encuesta EPA (INE): Contabilizado como OCUPADO (trabajó ≥ 1 hora en la semana de referencia).",
        "Veredicto: Plena coincidencia entre registros administrativos y encuesta EPA."
    ], PINO),
    ("EN INACTIVIDAD · REGISTRO SEPE", "Excluido del Paro Registrado", [
        "Relación laboral: El contrato NO se extingue, queda SUSPENDIDO hasta el próximo llamamiento.",
        "Clasificación SEPE: Se inscribe como DENO (Demandante de Empleo No Ocupado con relación laboral).",
        "Norma histórica: La Orden Ministerial de 11/03/1985 excluye a los fijos discontinuos del Paro Registrado.",
        "Cobro de ayuda: Sí puede cobrar prestación o subsidio por desempleo.",
        "Efecto óptico: Reduce el Paro Registrado oficial respecto a los antiguos temporales."
    ], CORAL),
    ("EN INACTIVIDAD · ENCUESTA EPA", "Criterio Puro de la OIT (INE)", [
        "Al entrevistar al hogar, la EPA no mira la etiqueta del contrato sino la actividad real de esa semana.",
        "¿Trabajó al menos 1 hora?: NO → Jamás cuenta como ocupado en la EPA durante la inactividad.",
        "Caso 1 (Busca otro trabajo y está disponible): La EPA lo clasifica como PARADO.",
        "Caso 2 (Espera en casa el llamamiento sin buscar): La EPA lo clasifica como INACTIVO.",
        "Veredicto: La EPA captura con total transparencia la falta de trabajo efectivo."
    ], SALVIA)
]

x_pos = Inches(0.8)
for c_tag, c_tit, c_items, c_col in cols_s7:
    add_card(s7, x_pos, Inches(1.45), Inches(3.75), Inches(5.3), MENTA, BORDE_MENTA)
    tb_t = s7.shapes.add_textbox(x_pos + Inches(0.15), Inches(1.6), Inches(3.45), Inches(0.4))
    p_t = tb_t.text_frame.paragraphs[0]
    p_t.text = c_tag
    p_t.font.name = "Outfit"
    p_t.font.size = Pt(11)
    p_t.font.bold = True
    p_t.font.color.rgb = c_col

    tb_tit = s7.shapes.add_textbox(x_pos + Inches(0.15), Inches(1.95), Inches(3.45), Inches(0.55))
    p_h = tb_tit.text_frame.paragraphs[0]
    p_h.text = c_tit
    p_h.font.name = "Outfit"
    p_h.font.size = Pt(13)
    p_h.font.bold = True
    p_h.font.color.rgb = PINO

    tb_b = s7.shapes.add_textbox(x_pos + Inches(0.15), Inches(2.55), Inches(3.45), Inches(4.05))
    tf_b = tb_b.text_frame
    tf_b.word_wrap = True
    for idx, item in enumerate(c_items):
        p_it = tf_b.paragraphs[0] if idx == 0 else tf_b.add_paragraph()
        p_it.font.name = "Calibri"
        p_it.font.size = Pt(11.8)
        p_it.space_before = Pt(7)
        p_it.text = "• " + item
        p_it.font.color.rgb = TINTA
    x_pos += Inches(3.99)

# ==============================================================================
# SLIDE 8: FASE 2 · MINI-LECCIÓN I: TAXONOMÍA DE LA FLEXIBILIDAD (ATKINSON)
# ==============================================================================
s8 = prs.slides.add_slide(blank_layout)
set_slide_background(s8, BLANCO)
add_header(s8, "Fase 2 (20–45 min) · Mini-Lección Quirúrgica I (Sin Pantallas · Solo Papel)", "Epígrafe 4.1 · ¿A Qué Llamamos Flexibilidad Laboral? La Taxonomía de Atkinson", 8)

add_card(s8, Inches(0.8), Inches(1.45), Inches(5.7), Inches(5.3), MENTA, BORDE_MENTA)
tb_s8_1 = s8.shapes.add_textbox(Inches(1.05), Inches(1.65), Inches(5.2), Inches(4.9))
tf_s8_1 = tb_s8_1.text_frame
tf_s8_1.word_wrap = True

p_s8_1 = tf_s8_1.paragraphs[0]
p_s8_1.text = "1. Flexibilidad Externa (Ajuste vía Empleo · N)"
p_s8_1.font.name = "Outfit"
p_s8_1.font.size = Pt(15)
p_s8_1.font.bold = True
p_s8_1.font.color.rgb = CORAL

bullets_s8_1 = [
    ("Definición:", " Capacidad de la empresa para adaptar el volumen de su plantilla (número de trabajadores N) contratando en fases expansivas o rescindiendo contratos en recesión."),
    ("A. Flexibilidad Externa de Entrada:", " Regulación de las modalidades contractuales (indefinidos, temporales causales, fijos discontinuos, formativos) y Empresas de Trabajo Temporal (ETT)."),
    ("B. Flexibilidad Externa de Salida:", " Costes, requisitos causales, plazos de preaviso y control judicial para extinguir contratos (despido individual objetivo/improcedente y despido colectivo ERE)."),
    ("Riesgo económico:", " Si toda la flexibilidad descansa en la vía externa, el empleo destruido en cada crisis es masivo (patrón histórico español).")
]
for b_t, b_d in bullets_s8_1:
    p = tf_s8_1.add_paragraph()
    p.font.name = "Calibri"
    p.font.size = Pt(12.2)
    p.space_before = Pt(8)
    r1 = p.add_run()
    r1.text = "• " + b_t
    r1.font.bold = True
    r1.font.color.rgb = PINO
    r2 = p.add_run()
    r2.text = b_d
    r2.font.color.rgb = TINTA

add_card(s8, Inches(6.8), Inches(1.45), Inches(5.733), Inches(5.3), MENTA, BORDE_MENTA)
tb_s8_2 = s8.shapes.add_textbox(Inches(7.05), Inches(1.65), Inches(5.2), Inches(4.9))
tf_s8_2 = tb_s8_2.text_frame
tf_s8_2.word_wrap = True

p_s8_2 = tf_s8_2.paragraphs[0]
p_s8_2.text = "2. Flexibilidad Interna (Ajuste sin Destruir Empleo)"
p_s8_2.font.name = "Outfit"
p_s8_2.font.size = Pt(15)
p_s8_2.font.bold = True
p_s8_2.font.color.rgb = PINO

bullets_s8_2 = [
    ("Definición:", " Capacidad de reorganizar el trabajo dentro de la empresa manteniendo intacto el vínculo contractual y el capital humano específico."),
    ("A. Interna Cuantitativa (Horas · H):", " Distribución irregular de jornada (hasta 10% anual, art. 34.2 ET), horas extraordinarias, ERTE ETOP/Fuerza Mayor (art. 47 ET) y Mecanismo RED (art. 47 bis ET)."),
    ("B. Interna Funcional (Tareas):", " Movilidad funcional horizontal y vertical dentro de grupos profesionales (art. 39 ET), polivalencia y teletrabajo."),
    ("C. Interna Salarial (Costes):", " Retribución variable ligada a productividad y cláusulas de inaplicación o descuelgue salarial de convenio (art. 82.3 ET).")
]
for b_t, b_d in bullets_s8_2:
    p = tf_s8_2.add_paragraph()
    p.font.name = "Calibri"
    p.font.size = Pt(12.2)
    p.space_before = Pt(8)
    r1 = p.add_run()
    r1.text = "• " + b_t
    r1.font.bold = True
    r1.font.color.rgb = PINO
    r2 = p.add_run()
    r2.text = b_d
    r2.font.color.rgb = TINTA

# ==============================================================================
# SLIDE 9: FASE 2 · FLEXISEGURIDAD DANESA VS DUALIDAD ESPAÑOLA (FIGURA 4.1)
# ==============================================================================
s9 = prs.slides.add_slide(blank_layout)
set_slide_background(s9, BLANCO)
add_header(s9, "Fase 2 (20–45 min) · Dos Modelos Institucionales Opuestos en Europa", "Figura 4.1 · El Triángulo de Oro de la Flexiseguridad Danesa vs. la Dualidad Española", 9)

if os.path.exists(FIG_4_1):
    s9.shapes.add_picture(FIG_4_1, Inches(0.8), Inches(1.38), width=Inches(11.733), height=Inches(3.92))

add_card(s9, Inches(0.8), Inches(5.40), Inches(11.733), Inches(1.42), MENTA, BORDE_MENTA)
tb_s9_inf = s9.shapes.add_textbox(Inches(1.0), Inches(5.46), Inches(11.3), Inches(1.30))
tf_s9_inf = tb_s9_inf.text_frame
tf_s9_inf.word_wrap = True

b_s9 = [
    ("1. El Triángulo de Oro Danés (Proteger al trabajador, no al puesto): ", "Combina despido libre/barato + seguro de paro muy generoso (80–90% del salario) + Políticas Activas (PAE) obligatorias y eficaces que recolocan rápidamente al parado.", PINO),
    ("2. La Dualidad Española (Insiders vs. Outsiders, 1984–2021): ", "Trató de compensar un despido indefinido rígido y caro liberalizando en 1984 los contratos temporales sin causa. Creó dos castas laborales: fijos blindados y temporales precarios que absorbían el 85% de los despidos en cada crisis.", CORAL)
]
for idx, (bt, bd, bc) in enumerate(b_s9):
    p = tf_s9_inf.paragraphs[0] if idx == 0 else tf_s9_inf.add_paragraph()
    p.font.name = "Calibri"
    p.font.size = Pt(12)
    p.space_before = Pt(4)
    r1 = p.add_run()
    r1.text = bt
    r1.font.bold = True
    r1.font.color.rgb = bc
    r2 = p.add_run()
    r2.text = bd
    r2.font.color.rgb = TINTA

# ==============================================================================
# SLIDE 10: FASE 2 · EL INDICADOR EPL DE LA OCDE Y LA BRECHA ΔEPL
# ==============================================================================
s10 = prs.slides.add_slide(blank_layout)
set_slide_background(s10, BLANCO)
add_header(s10, "Fase 2 (20–45 min) · Medición Comparada de la Rigidez Normativa", "Epígrafe 4.2.1 · La Legislación de Protección del Empleo (EPL) y la Brecha Regulatoria", 10)

add_card(s10, Inches(0.8), Inches(1.45), Inches(11.733), Inches(1.15), MENTA, BORDE_MENTA)
tb_f10 = s10.shapes.add_textbox(Inches(1.0), Inches(1.50), Inches(11.3), Inches(1.0))
tf_f10 = tb_f10.text_frame
tf_f10.word_wrap = True
p_f10 = tf_f10.paragraphs[0]
p_f10.alignment = PP_ALIGN.CENTER
p_f10.text = "Definición de la Brecha Regulatoria de Dualidad (OCDE Employment Outlook)"
p_f10.font.name = "Outfit"
p_f10.font.size = Pt(13)
p_f10.font.bold = True
p_f10.font.color.rgb = PINO

p_f10_eq = tf_f10.add_paragraph()
p_f10_eq.alignment = PP_ALIGN.CENTER
p_f10_eq.font.name = "Calibri"
p_f10_eq.font.size = Pt(16)
p_f10_eq.font.bold = True
p_f10_eq.space_before = Pt(4)
r1 = p_f10_eq.add_run()
r1.text = "Brecha de Dualidad (ΔEPL) = EPL"
r1.font.color.rgb = PINO
r2 = p_f10_eq.add_run()
r2.text = "indefinidos"
r2.font.subscript = True
r2.font.color.rgb = PINO
r3 = p_f10_eq.add_run()
r3.text = " − Coste Efectivo de Salida Temporal (EPL"
r3.font.color.rgb = CORAL
r4 = p_f10_eq.add_run()
r4.text = "temporal"
r4.font.subscript = True
r4.font.color.rgb = CORAL
r5 = p_f10_eq.add_run()
r5.text = ")"
r5.font.color.rgb = CORAL

pilares_epl = [
    ("Pilar 1 · Despido Individual (Indefinidos)", "Mide en escala de 0 a 6: requisitos de notificación y preaviso, cuantía de la indemnización según antigüedad, definición legal de causa justa vs. improcedente y posibilidad de readmisión forzosa.", PINO),
    ("Pilar 2 · Despidos Colectivos (ERE)", "Evalúa los costes y trámites adicionales cuando la empresa supera los umbrales de despido masivo: plazos de consulta sindical obligatoria, planes de recolocación e intervención administrativa.", SALVIA),
    ("Pilar 3 · Regulación Temporal y Efecto Umbral", "Evalúa las causas válidas, duración máxima e indemnización de fin de contrato temporal. Cuando ΔEPL es alto, las empresas no convierten temporales en fijos: los rotan sistemáticamente (efecto umbral).", CORAL)
]

x_p10 = Inches(0.8)
for p_tit, p_desc, p_col in pilares_epl:
    add_card(s10, x_p10, Inches(2.80), Inches(3.75), Inches(3.95), BLANCO, BORDE_MENTA)
    tb = s10.shapes.add_textbox(x_p10 + Inches(0.15), Inches(2.95), Inches(3.45), Inches(3.65))
    tf = tb.text_frame
    tf.word_wrap = True
    p1 = tf.paragraphs[0]
    p1.text = p_tit
    p1.font.name = "Outfit"
    p1.font.size = Pt(13.5)
    p1.font.bold = True
    p1.font.color.rgb = p_col

    p2 = tf.add_paragraph()
    p2.text = p_desc
    p2.font.name = "Calibri"
    p2.font.size = Pt(12.5)
    p2.space_before = Pt(10)
    p2.font.color.rgb = TINTA
    x_p10 += Inches(3.99)

# ==============================================================================
# SLIDE 11: FASE 2 · COMPARATIVA INTERNACIONAL OCDE DE EPL (FIGURA 4.2)
# ==============================================================================
s11 = prs.slides.add_slide(blank_layout)
set_slide_background(s11, BLANCO)
add_header(s11, "Fase 2 (20–45 min) · Evidencia Comparada en la OCDE", "Figura 4.2 · Rigidez de Protección del Empleo (EPL) en Indefinidos vs. Temporales (OCDE)", 11)

if os.path.exists(FIG_4_2):
    s11.shapes.add_picture(FIG_4_2, Inches(0.8), Inches(1.38), width=Inches(11.733), height=Inches(3.92))

add_card(s11, Inches(0.8), Inches(5.40), Inches(11.733), Inches(1.42), MENTA, BORDE_MENTA)
tb_s11_inf = s11.shapes.add_textbox(Inches(1.0), Inches(5.46), Inches(11.3), Inches(1.30))
tf_s11_inf = tb_s11_inf.text_frame
tf_s11_inf.word_wrap = True

b_s11 = [
    ("1. Modelo Anglosajón (EE.UU. 0,09 · R. Unido 1,35): ", "Doctrina del employment-at-will: mínima protección tanto en fijos como en temporales. Desempleo de corta duración pero alta desigualdad salarial.", SALVIA),
    ("2. Flexiseguridad Nórdica (Dinamarca 1,53): ", "Baja rigidez en indefinidos (1,53) combinada con generosa protección por desempleo.", PINO),
    ("3. Modelo Continental y Mediterráneo (España 2,46 en fijos / 2,67 en temporales): ", "Alta protección legal en indefinidos y, tras el RDL 32/2021, endurecimiento severo de las restricciones legales para contratar temporalmente.", CORAL)
]
for idx, (bt, bd, bc) in enumerate(b_s11):
    p = tf_s11_inf.paragraphs[0] if idx == 0 else tf_s11_inf.add_paragraph()
    p.font.name = "Calibri"
    p.font.size = Pt(11.8)
    p.space_before = Pt(3)
    r1 = p.add_run()
    r1.text = bt
    r1.font.bold = True
    r1.font.color.rgb = bc
    r2 = p.add_run()
    r2.text = bd
    r2.font.color.rgb = TINTA

# ==============================================================================
# SLIDE 12: FASE 3 · MINI-LECCIÓN II: CUADRO NORMATIVO DEL DESPIDO EN ESPAÑA
# ==============================================================================
s12 = prs.slides.add_slide(blank_layout)
set_slide_background(s12, BLANCO)
add_header(s12, "Fase 3 (45–70 min) · Mini-Lección Quirúrgica II (Marco Jurídico-Económico)", "Epígrafe 4.2.2 · Tipología y Costes de Extinción del Contrato en España (ET)", 12)

tipos_despido = [
    ("1. Fin de Contrato Temporal (Art. 49.1.c ET)", "12 días de salario por año de servicio (prorrateándose por meses los periodos inferiores al año). Excepción: los contratos de sustitución y los contratos formativos no generan indemnización (0 días) a su vencimiento.", SALVIA),
    ("2. Despido Objetivo Procedente (Arts. 52–53 ET) y Colectivo ERE (Art. 51 ET)", "Por causas Económicas, Técnicas, Organizativas o de Producción (ETOP) o ineptitud sobrevenida. Indemnización: 20 días/año (tope de 12 mensualidades) + 15 días de preaviso. El ERE aplica cuando en 90 días afecta a ≥10 trabajadores (empresas <100), ≥10% (empresas 100–300) o ≥30 (empresas >300).", PINO),
    ("3. Despido Improcedente (Art. 56 ET · Reforma RDL 3/2012 y DT 11.ª ET)", "Cuando no se acredita la causa legal o disciplinaria. Indemnización desde el 12/02/2012: 33 días/año (tope de 24 mensualidades = 720 días), sin salarios de tramitación salvo readmisión o representante sindical. Para contratos anteriores al 12/02/2012: doble tramo de 45 días/año (previo) + 33 días/año (posterior).", CORAL),
    ("4. Despido Nulo (Art. 55.5 ET · Tutela de Derechos Fundamentales)", "Móvil discriminatorio, vulneración de derechos fundamentales, embarazo, permisos de nacimiento/cuidado o fraude en ERE. Efecto: Readmisión obligatoria inmediata + pago íntegro de salarios de tramitación.", PINO_DARK)
]

y_d12 = Inches(1.42)
for d_tit, d_txt, d_col in tipos_despido:
    add_card(s12, Inches(0.8), y_d12, Inches(11.733), Inches(1.22), MENTA, BORDE_MENTA)
    m_box = s12.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), y_d12, Inches(0.18), Inches(1.22))
    m_box.fill.solid()
    m_box.fill.fore_color.rgb = d_col
    m_box.line.fill.background()

    tb = s12.shapes.add_textbox(Inches(1.15), y_d12 + Inches(0.06), Inches(11.2), Inches(1.10))
    tf = tb.text_frame
    tf.word_wrap = True
    p1 = tf.paragraphs[0]
    p1.text = d_tit
    p1.font.name = "Outfit"
    p1.font.size = Pt(13.5)
    p1.font.bold = True
    p1.font.color.rgb = d_col

    p2 = tf.add_paragraph()
    p2.text = d_txt
    p2.font.name = "Calibri"
    p2.font.size = Pt(11.5)
    p2.space_before = Pt(3)
    p2.font.color.rgb = TINTA
    y_d12 += Inches(1.33)

# ==============================================================================
# SLIDE 13: FASE 3 · FUNCIÓN DE COSTE DE DESPIDO SEGÚN ANTIGÜEDAD (FIGURA 4.4)
# ==============================================================================
s13 = prs.slides.add_slide(blank_layout)
set_slide_background(s13, BLANCO)
add_header(s13, "Fase 3 (45–70 min) · Análisis Gráfico de las Curvas de Indemnización", "Figura 4.4 · Indemnización Acumulada según Antigüedad y Prima de Litigiosidad", 13)

if os.path.exists(FIG_4_4):
    s13.shapes.add_picture(FIG_4_4, Inches(0.8), Inches(1.32), width=Inches(11.733), height=Inches(3.88))

guia_fig44 = [
    ("1. Rebaja del RDL 3/2012", "De 45 d (42 m) a 33 d (24 m)", CORAL, RGBColor(255, 245, 242), CORAL,
     "El RDL 3/2012 redujo la pendiente del despido improcedente de 1,5 meses/año (45 d) a 1,1 meses/año (33 d) y recortó el tope máximo de 42 a 24 mensualidades (que se alcanza a los 21,8 años)."),
    ("2. Brecha 33 vs. 20 días", "Incertidumbre Judicial", PINO, MENTA, PINO,
     "La franja sombreada mide el sobrecoste (+65%) si un juez rechaza la causa objetiva (20 d) y declara el despido improcedente (33 d). A los 15 años supone pasar de 25.000 € a 41.250 €."),
    ("3. El Abismo Temporal", "12 días vs. 33 días", SALVIA, BLANCO, BORDE_MENTA,
     "Extinguir un contrato temporal al año cuesta 1.000 € (12 días) sin juicio. Esa asimetría frente al indefinido explicaba la rotación masiva antes de 2022.")
]

x_g13 = Inches(0.8)
for g_tit, g_sub, g_col, g_bg, g_bor, g_txt in guia_fig44:
    add_card(s13, x_g13, Inches(5.28), Inches(3.75), Inches(1.55), g_bg, g_bor)
    tb_g = s13.shapes.add_textbox(x_g13 + Inches(0.12), Inches(5.33), Inches(3.51), Inches(1.45))
    tf_g = tb_g.text_frame
    tf_g.word_wrap = True
    p1 = tf_g.paragraphs[0]
    p1.text = g_tit + " · " + g_sub
    p1.font.name = "Outfit"
    p1.font.size = Pt(11)
    p1.font.bold = True
    p1.font.color.rgb = g_col

    p2 = tf_g.add_paragraph()
    p2.text = g_txt
    p2.font.name = "Calibri"
    p2.font.size = Pt(10)
    p2.space_before = Pt(4)
    p2.font.color.rgb = TINTA
    x_g13 += Inches(3.99)

# ==============================================================================
# SLIDE 14: FASE 3 · TRES CASOS NUMÉRICOS APLICADOS DE DESPIDO
# ==============================================================================
s14 = prs.slides.add_slide(blank_layout)
set_slide_background(s14, BLANCO)
add_header(s14, "Fase 3 (45–70 min) · Práctica Cuantitativa para Graduados en RRLL", "Cálculo Aplicado de Indemnizaciones: Tres Escenarios Reales (Salario = 2.400 €/mes)", 14)

casos_despido = [
    {
        "tit": "CASO 1 · Objetivo Procedente",
        "sub": "Art. 52 ET · 20 días/año (Tope 12 meses)",
        "col": SALVIA,
        "lineas": [
            ("Trabajador:", "Contratado en 2016 (10 años exactos)."),
            ("Salario regulador:", "2.400 €/mes → Salario diario = 80 €/día."),
            ("Devengo legal:", "10 años × 20 días/año = 200 días."),
            ("Verificación tope:", "200 días < 360 días (12 mensualidades)."),
            ("Cálculo formal:", "200 días × 80 €/día = 16.000 €."),
            ("Veredicto RRLL:", "Indemnización tasada de 16.000 € + 15 días de preaviso.")
        ]
    },
    {
        "tit": "CASO 2 · Improcedente Post-2012",
        "sub": "Art. 56 ET · 33 días/año (Tope 24 meses)",
        "col": CORAL,
        "lineas": [
            ("Trabajador:", "Mismo empleado (10 años, 80 €/día)."),
            ("Sentencia judicial:", "El juzgado rechaza la causa organizativa."),
            ("Devengo legal:", "10 años × 33 días/año = 330 días."),
            ("Verificación tope:", "330 días < 720 días (24 mensualidades)."),
            ("Cálculo formal:", "330 días × 80 €/día = 26.400 €."),
            ("Veredicto RRLL:", "Sobrecoste de +10.400 € (+65%) respecto al despido objetivo.")
        ]
    },
    {
        "tit": "CASO 3 · Doble Tramo Pre-2012",
        "sub": "DT 11.ª ET · 45 d (pre-2012) + 33 d (post)",
        "col": PINO,
        "lineas": [
            ("Trabajador:", "4 años pre-12/02/2012 + 12 años post-2012."),
            ("Tramo 1 (45 d/año):", "4 años × 45 días = 180 días."),
            ("Tramo 2 (33 d/año):", "12 años × 33 días = 396 días."),
            ("Suma total días:", "180 + 396 = 576 días (< tope 720 días)."),
            ("Cálculo formal:", "576 días × 80 €/día = 46.080 €."),
            ("Veredicto RRLL:", "Protección reforzada de derechos adquiridos antes de 2012.")
        ]
    }
]

x_c14 = Inches(0.8)
for case in casos_despido:
    add_card(s14, x_c14, Inches(1.45), Inches(3.75), Inches(5.3), MENTA, BORDE_MENTA)
    tb = s14.shapes.add_textbox(x_c14 + Inches(0.15), Inches(1.60), Inches(3.45), Inches(5.0))
    tf = tb.text_frame
    tf.word_wrap = True
    p1 = tf.paragraphs[0]
    p1.text = case["tit"]
    p1.font.name = "Outfit"
    p1.font.size = Pt(14.5)
    p1.font.bold = True
    p1.font.color.rgb = case["col"]

    p2 = tf.add_paragraph()
    p2.text = case["sub"]
    p2.font.name = "Outfit"
    p2.font.size = Pt(11)
    p2.font.bold = True
    p2.font.color.rgb = PINO
    p2.space_before = Pt(3)

    for etiq, det in case["lineas"]:
        p_l = tf.add_paragraph()
        p_l.font.name = "Calibri"
        p_l.font.size = Pt(11.8)
        p_l.space_before = Pt(8)
        r1 = p_l.add_run()
        r1.text = "• " + etiq + " "
        r1.font.bold = True
        r1.font.color.rgb = PINO
        r2 = p_l.add_run()
        r2.text = det
        if "Cálculo" in etiq or "Veredicto" in etiq:
            r2.font.bold = True
            r2.font.color.rgb = case["col"]
        else:
            r2.font.color.rgb = TINTA
    x_c14 += Inches(3.99)

# ==============================================================================
# SLIDE 15: FASE 3 · LA REFORMA LABORAL DE 2021 (RDL 32/2021)
# ==============================================================================
s15 = prs.slides.add_slide(blank_layout)
set_slide_background(s15, BLANCO)
add_header(s15, "Fase 3 (45–70 min) · El Cambio de Paradigma en la Flexibilidad de Entrada", "Epígrafe 4.2.3 · Los Cuatro Pilares de la Reforma Laboral (RDL 32/2021)", 15)

pilares_rdl = [
    ("1. Presunción Indefinida y Supresión del Contrato por Obra o Servicio (Art. 15 ET)",
     "El contrato de trabajo se presume concertado por tiempo indefinido. Se deroga definitivamente el contrato por obra o servicio determinado (principal foco histórico de fraude y rotación en España desde 1984).", PINO),
    ("2. Redefinición Estricta de los Contratos Temporales Estructurales (Art. 15 ET)",
     "Solo quedan dos modalidades causales: a) Circunstancias de la producción IMPREVISIBLES (máx. 6 meses, ampliable a 12 por convenio sectorial) y PREVISIBLES (máx. 90 días/año por empresa, no continuados); b) Sustitución de trabajador con reserva de puesto.", SALVIA),
    ("3. Límite al Encadenamiento (Art. 15.5 ET) y Penalización a Micro-Contratos (<30 días)",
     "Adquiere condición de fijo quien encadene >18 meses en un periodo de 24 meses (antes 24 en 30). Además, cada baja de un contrato temporal inferior a 30 días paga una cotización adicional fija de 31,40 € a la Seguridad Social (art. 151 LGSS).", CORAL),
    ("4. Nuevos Contratos Formativos (Art. 11 ET): Alternancia y Práctica Profesional",
     "Sustituyen a los antiguos contratos de aprendizaje y prácticas: Formación en alternancia (compatibilizar empleo con estudios, de 3 meses a 2 años) y Obtención de práctica profesional para titulados (de 6 meses a 1 año).", PINO_DARK)
]

y_p15 = Inches(1.42)
for p_tit, p_txt, p_col in pilares_rdl:
    add_card(s15, Inches(0.8), y_p15, Inches(11.733), Inches(1.22), MENTA, BORDE_MENTA)
    m_box = s15.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), y_p15, Inches(0.18), Inches(1.22))
    m_box.fill.solid()
    m_box.fill.fore_color.rgb = p_col
    m_box.line.fill.background()

    tb = s15.shapes.add_textbox(Inches(1.15), y_p15 + Inches(0.06), Inches(11.2), Inches(1.10))
    tf = tb.text_frame
    tf.word_wrap = True
    p1 = tf.paragraphs[0]
    p1.text = p_tit
    p1.font.name = "Outfit"
    p1.font.size = Pt(13.5)
    p1.font.bold = True
    p1.font.color.rgb = p_col

    p2 = tf.add_paragraph()
    p2.text = p_txt
    p2.font.name = "Calibri"
    p2.font.size = Pt(11.5)
    p2.space_before = Pt(3)
    p2.font.color.rgb = TINTA
    y_p15 += Inches(1.33)

# ==============================================================================
# SLIDE 16: FASE 3 · RADIOGRAFÍA DEL CONTRATO FIJO DISCONTINUO (ART. 16 ET)
# ==============================================================================
s16 = prs.slides.add_slide(blank_layout)
set_slide_background(s16, BLANCO)
add_header(s16, "Fase 3 (45–70 min) · La Figura Estrella de la Reforma Laboral", "El Contrato Fijo Discontinuo (Art. 16 ET): Naturaleza Jurídica y Derechos", 16)

add_card(s16, Inches(0.8), Inches(1.45), Inches(5.7), Inches(5.3), MENTA, BORDE_MENTA)
tb_s16_1 = s16.shapes.add_textbox(Inches(1.05), Inches(1.65), Inches(5.2), Inches(4.9))
tf_s16_1 = tb_s16_1.text_frame
tf_s16_1.word_wrap = True

p_s16_1 = tf_s16_1.paragraphs[0]
p_s16_1.text = "¿Cuándo se Utiliza y Qué Derechos Otorga?"
p_s16_1.font.name = "Outfit"
p_s16_1.font.size = Pt(15)
p_s16_1.font.bold = True
p_s16_1.font.color.rgb = PINO

b_s16_1 = [
    "Objeto legal (Art. 16.1 ET): Trabajos de naturaleza estacional (turismo, agricultura, educación), actividades de prestación intermitente con periodos ciertos o inciertos, y ejecución de contratas mercantiles o concesiones administrativas.",
    "Derecho de llamamiento: La empresa está obligada a llamar al trabajador al inicio de cada campaña según criterios objetivos y formales fijados en convenio. La falta de llamamiento equivale a un despido improcedente.",
    "Cómputo de antigüedad (Jurisprudencia TS y TJUE): A efectos de promoción económica y social (trienios), computa todo el tiempo de duración de la relación laboral, incluyendo los periodos de inactividad (a efectos indemnizatorios por despido computan los periodos efectivamente trabajados)."
]
for b in b_s16_1:
    p = tf_s16_1.add_paragraph()
    p.font.name = "Calibri"
    p.font.size = Pt(12.2)
    p.space_before = Pt(8)
    p.text = "• " + b
    p.font.color.rgb = TINTA

add_card(s16, Inches(6.8), Inches(1.45), Inches(5.733), Inches(5.3), BLANCO, BORDE_CORAL, Pt(1.5))
tb_s16_2 = s16.shapes.add_textbox(Inches(7.05), Inches(1.65), Inches(5.2), Inches(4.9))
tf_s16_2 = tb_s16_2.text_frame
tf_s16_2.word_wrap = True

p_s16_2 = tf_s16_2.paragraphs[0]
p_s16_2.text = "El Debate Económico: ¿Estabilidad Real o Nominal?"
p_s16_2.font.name = "Outfit"
p_s16_2.font.size = Pt(15)
p_s16_2.font.bold = True
p_s16_2.font.color.rgb = CORAL

b_s16_2 = [
    "Avance innegable en derechos: El trabajador gana vínculo indefinido, protección de 33 días frente a la no llamada y menor incertidumbre que el antiguo temporal de obra.",
    "Sombra 1 · Inestabilidad de rentas anuales: Tener un contrato indefinido fijo discontinuo o a tiempo parcial no garantiza trabajar 12 meses al año ni salir de la pobreza laboral.",
    "Sombra 2 · Reparto del empleo en trozos más pequeños: El número de contratos indefinidos firmados por persona al año ha subido (pluriempleo y mayor rotación dentro de los indefinidos).",
    "Sombra 3 · Opacidad en el Paro Registrado: Cientos de miles de fijos discontinuos inactivos figuran como DENO sin desglosarse en la cifra de cabecera del paro mensual."
]
for b in b_s16_2:
    p = tf_s16_2.add_paragraph()
    p.font.name = "Calibri"
    p.font.size = Pt(12.2)
    p.space_before = Pt(8)
    p.text = "• " + b
    p.font.color.rgb = TINTA

# ==============================================================================
# SLIDE 17: FASE 3 · BALANCE EMPÍRICO DEL RDL 32/2021 (FEDEA / BANCO DE ESPAÑA)
# ==============================================================================
s17 = prs.slides.add_slide(blank_layout)
set_slide_background(s17, BLANCO)
add_header(s17, "Fase 3 (45–70 min) · Evaluación Empírica de la Reforma Laboral", "Balance del RDL 32/2021: Tres Éxitos Estructurales y Tres Retos Pendientes", 17)

balance_rdl = [
    ("ÉXITO 1 · Hundimiento de la Temporalidad Privada (29,2% → 12,4%)",
     "España ha dejado de ser la anomalía europea en contratación temporal privada, reduciendo la brecha en más de 16 puntos porcentuales sin destruir empleo agregado y mejorando la estabilidad percibida por los hogares jóvenes.", PINO),
    ("RETOS Y SOMBRAS 2 · Aumento de Bajas en Periodo de Prueba y Despidos de Corta Antigüedad",
     "Al cerrarse la válvula del contrato temporal sin modificar los costes del despido indefinido, ha aumentado la tasa de extinción de contratos indefinidos durante los primeros meses (no superación del periodo de prueba y despidos de baja antigüedad).", CORAL),
    ("RETOS Y SOMBRAS 3 · El Enquistamiento de la Temporalidad Pública (>30%)",
     "Las Administraciones Públicas siguen registrando tasas de temporalidad superiores al 30%, lo que exige culminar los procesos de estabilización y reformar el acceso a la función pública para cumplir con la Directiva 1999/70/CE y la doctrina del TJUE.", SALVIA)
]

y_b17 = Inches(1.45)
for r_tit, r_txt, r_col in balance_rdl:
    add_card(s17, Inches(0.8), y_b17, Inches(11.733), Inches(1.65), MENTA, BORDE_MENTA)
    m_box = s17.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), y_b17, Inches(0.2), Inches(1.65))
    m_box.fill.solid()
    m_box.fill.fore_color.rgb = r_col
    m_box.line.fill.background()

    tb = s17.shapes.add_textbox(Inches(1.2), y_b17 + Inches(0.12), Inches(11.0), Inches(1.4))
    tf = tb.text_frame
    tf.word_wrap = True
    p1 = tf.paragraphs[0]
    p1.text = r_tit
    p1.font.name = "Outfit"
    p1.font.size = Pt(15)
    p1.font.bold = True
    p1.font.color.rgb = r_col

    p2 = tf.add_paragraph()
    p2.text = r_txt
    p2.font.name = "Calibri"
    p2.font.size = Pt(13)
    p2.space_before = Pt(6)
    p2.font.color.rgb = TINTA
    y_b17 += Inches(1.8)

# ==============================================================================
# SLIDE 18: FASE 4 · LABORATORIO ACTIVO CON MICRO-APP (15 MIN)
# ==============================================================================
s18 = prs.slides.add_slide(blank_layout)
set_slide_background(s18, BLANCO)
add_header(s18, "Fase 4 (70–85 min · 15 min) · Laboratorio Activo desde el Móvil", "Taller Práctico: «Calculadora de Despido, Brecha ΔEPL y Auditoría SEPE/EPA»", 18)

add_card(s18, Inches(0.8), Inches(1.45), Inches(7.5), Inches(5.3), MENTA, BORDE_MENTA)
tb_s18_m = s18.shapes.add_textbox(Inches(1.05), Inches(1.60), Inches(6.9), Inches(5.0))
tf_s18_m = tb_s18_m.text_frame
tf_s18_m.word_wrap = True

p_m_h = tf_s18_m.paragraphs[0]
p_m_h.text = "🎯 Misión en el Simulador Móvil (3 Escenarios en 15 minutos)"
p_m_h.font.name = "Outfit"
p_m_h.font.size = Pt(15)
p_m_h.font.bold = True
p_m_h.font.color.rgb = PINO

p_sub_ch = tf_s18_m.add_paragraph()
p_sub_ch.text = "Desbloquead el teléfono móvil, escanead el código QR de la derecha y resolved las tres pestañas del laboratorio interactivo:"
p_sub_ch.font.name = "Calibri"
p_sub_ch.font.size = Pt(12)
p_sub_ch.space_before = Pt(6)
p_sub_ch.font.color.rgb = TINTA

metas18 = [
    ("Misión 1 · Calculadora de Indemnización (Pestaña 1):", " Introduce un salario de 2.400 €/mes (80 €/día) y 10 años de antigüedad. Comprueba el salto de 16.000 € (objetivo 20 d) a 26.400 € (improcedente 33 d) y simula el doble tramo pre-2012 (45/33 d).", PINO),
    ("Misión 2 · Simulador de Dualidad ΔEPL (Pestaña 2):", " Pulsa el botón 'Aplicar Reforma RDL 32/2021' y analiza cómo la supresión de obra o servicio y el recargo de 31,40 € hunden la temporalidad privada al 12,4%.", SALVIA),
    ("Misión 3 · Auditoría del Fijo Discontinuo (Pestaña 3):", " Simula el paso a inactividad de 1.000 trabajadores de hostelería y contrasta el registro SEPE (+1.000 DENO, +0 Paro Registrado) frente a la EPA del INE.", CORAL)
]
for m_tit, m_desc, m_col in metas18:
    p = tf_s18_m.add_paragraph()
    p.space_before = Pt(8)
    p.font.name = "Calibri"
    p.font.size = Pt(12)
    r1 = p.add_run()
    r1.text = "• " + m_tit
    r1.font.bold = True
    r1.font.color.rgb = m_col
    r2 = p.add_run()
    r2.text = m_desc
    r2.font.color.rgb = TINTA

add_card(s18, Inches(8.55), Inches(1.45), Inches(3.98), Inches(5.3), BLANCO, BORDE_CORAL, Pt(1.5))
tb_s18_qr = s18.shapes.add_textbox(Inches(8.75), Inches(1.65), Inches(3.6), Inches(1.0))
tf_s18_qr = tb_s18_qr.text_frame
tf_s18_qr.word_wrap = True

p_qr_app_h = tf_s18_qr.paragraphs[0]
p_qr_app_h.text = "¡Abre la Micro-App!"
p_qr_app_h.alignment = PP_ALIGN.CENTER
p_qr_app_h.font.name = "Outfit"
p_qr_app_h.font.size = Pt(16)
p_qr_app_h.font.bold = True
p_qr_app_h.font.color.rgb = PINO

p_qr_app_sub = tf_s18_qr.add_paragraph()
p_qr_app_sub.text = "Simulador de EPL, Despido y Dualidad"
p_qr_app_sub.alignment = PP_ALIGN.CENTER
p_qr_app_sub.font.name = "Calibri"
p_qr_app_sub.font.size = Pt(11)
p_qr_app_sub.font.bold = True
p_qr_app_sub.font.color.rgb = CORAL

if os.path.exists(QR_APP):
    s18.shapes.add_picture(QR_APP, Inches(9.2), Inches(2.75), width=Inches(2.7), height=Inches(2.7))

tb_s18_url = s18.shapes.add_textbox(Inches(8.75), Inches(5.75), Inches(3.6), Inches(0.8))
p_u18 = tb_s18_url.text_frame.paragraphs[0]
p_u18.alignment = PP_ALIGN.CENTER
p_u18.text = "mhidper.github.io/micro_apps/\nsimulador_epl_dualidad.html"
p_u18.font.name = "Calibri"
p_u18.font.size = Pt(10)
p_u18.font.bold = True
p_u18.font.color.rgb = PINO

# ==============================================================================
# SLIDE 19: FASE 5A · SÍNTESIS INSTITUCIONAL Y DEBATE DE AULA
# ==============================================================================
s19 = prs.slides.add_slide(blank_layout)
set_slide_background(s19, BLANCO)
add_header(s19, "Fase 5a (85–95 min) · Síntesis Institucional y Debate de Aula", "Claves Estratégicas para un Graduado en Relaciones Laborales y RRHH", 19)

add_card(s19, Inches(0.8), Inches(1.45), Inches(5.7), Inches(5.3), MENTA, BORDE_MENTA)
tb_s19_1 = s19.shapes.add_textbox(Inches(1.05), Inches(1.65), Inches(5.2), Inches(4.9))
tf_s19_1 = tb_s19_1.text_frame
tf_s19_1.word_wrap = True

p_s19_h1 = tf_s19_1.paragraphs[0]
p_s19_h1.text = "De la Flexibilidad Externa a la Flexibilidad Interna"
p_s19_h1.font.name = "Outfit"
p_s19_h1.font.size = Pt(15)
p_s19_h1.font.bold = True
p_s19_h1.font.color.rgb = PINO

p_s19_b1 = tf_s19_1.add_paragraph()
p_s19_b1.font.name = "Calibri"
p_s19_b1.font.size = Pt(13)
p_s19_b1.space_before = Pt(8)
p_s19_b1.text = "1. El fin del atajo temporal en España:\nDurante 37 años (1984–2021), las empresas españolas ajustaron sus costes despidiendo masivamente a temporales. El RDL 32/2021 ha cerrado esa vía al suprimir el contrato de obra o servicio.\n\n2. La brecha ΔEPL sigue siendo determinante:\nMientras exista un salto brusco de costes e incertidumbre judicial entre modalidades, el diseño institucional debe vigilar que la rotación no se traslade a despidos en periodo de prueba.\n\n3. El papel del director de RRHH:\nGestionar picos de demanda hoy exige dominar los 90 días previsibles, el contrato fijo discontinuo y los mecanismos de flexibilidad interna (ERTE)."
p_s19_b1.font.color.rgb = TINTA

add_card(s19, Inches(6.8), Inches(1.45), Inches(5.733), Inches(5.3), MENTA, BORDE_MENTA)
tb_s19_2 = s19.shapes.add_textbox(Inches(7.05), Inches(1.65), Inches(5.2), Inches(4.9))
tf_s19_2 = tb_s19_2.text_frame
tf_s19_2.word_wrap = True

p_s19_h2 = tf_s19_2.paragraphs[0]
p_s19_h2.text = "Rigor Estadístico y Preparación del Reto"
p_s19_h2.font.name = "Outfit"
p_s19_h2.font.size = Pt(15)
p_s19_h2.font.bold = True
p_s19_h2.font.color.rgb = PINO

p_s19_b2 = tf_s19_2.add_paragraph()
p_s19_b2.font.name = "Calibri"
p_s19_b2.font.size = Pt(13)
p_s19_b2.space_before = Pt(8)
p_s19_b2.text = "1. Leer las estadísticas sin caer en trampas políticas:\nUn graduado en RRLL sabe distinguir por qué el SEPE clasifica al fijo discontinuo inactivo como DENO (vínculo suspendido, no extinguido) mientras la EPA lo mide como parado o inactivo según criterios OIT.\n\n2. El reto pendiente de las Administraciones Públicas:\nNo se puede exigir estabilidad al sector privado (12,4% de temporalidad) manteniendo a más del 30% de los empleados públicos en interinidad estructural.\n\n3. Transición al Reto Manuscrito (Fase 5b):\nGuardamos todos los teléfonos móviles. Solo cuartilla oficial y bolígrafo (10 minutos)."
p_s19_b2.font.color.rgb = TINTA

# ==============================================================================
# SLIDE 20: FASE 5B · RETO MANUSCRITO TURNO MARTES (LÍNEA 1)
# ==============================================================================
s20 = prs.slides.add_slide(blank_layout)
set_slide_background(s20, BLANCO)
add_header(s20, "Fase 5b (95–105 min) · Reto Manuscrito Individual (10 min · Solo Papel)", "Turno Martes · Línea 1 (10 de Noviembre de 2026)", 20)

add_card(s20, Inches(0.8), Inches(1.45), Inches(11.733), Inches(5.3), MENTA, BORDE_MENTA)
tb_s20 = s20.shapes.add_textbox(Inches(1.1), Inches(1.65), Inches(11.1), Inches(4.9))
tf_s20 = tb_s20.text_frame
tf_s20.word_wrap = True

p_r1 = tf_s20.paragraphs[0]
p_r1.text = "RETO DE EVALUACIÓN CONTINUA · TURNO MARTES (LÍNEA 1) · 1.000 PTS"
p_r1.font.name = "Outfit"
p_r1.font.size = Pt(16)
p_r1.font.bold = True
p_r1.font.color.rgb = PINO

p_warn1 = tf_s20.add_paragraph()
p_warn1.text = "Entorno libre de pantallas. Redacta a mano en tu cuartilla oficial (máximo 1 cara por alumno):"
p_warn1.font.name = "Calibri"
p_warn1.font.size = Pt(12.5)
p_warn1.font.color.rgb = CORAL
p_warn1.space_before = Pt(4)

p_q1 = tf_s20.add_paragraph()
p_q1.font.name = "Calibri"
p_q1.font.size = Pt(13.5)
p_q1.space_before = Pt(14)
r_q1_t = p_q1.add_run()
r_q1_t.text = "1. (500 pts) Flexiseguridad Danesa vs. Dualidad Española y Brecha de EPL:\n"
r_q1_t.font.bold = True
r_q1_t.font.color.rgb = PINO
r_q1_d = p_q1.add_run()
r_q1_d.text = "Explica los tres vértices que integran el «Triángulo de Oro» de la flexiseguridad danesa y contrástalo con el modelo histórico de dualidad laboral español (insiders vs. outsiders). ¿Por qué una elevada brecha en la legislación de protección del empleo (ΔEPL) entre contratos indefinidos y temporales desincentiva la conversión en fijos y dispara la volatilidad del empleo en las recesiones?"
r_q1_d.font.color.rgb = TINTA

p_q2 = tf_s20.add_paragraph()
p_q2.font.name = "Calibri"
p_q2.font.size = Pt(13.5)
p_q2.space_before = Pt(14)
r_q2_t = p_q2.add_run()
r_q2_t.text = "2. (500 pts) Caso Aplicado de Costes de Despido (Objetivo, Improcedente y Nulo):\n"
r_q2_t.font.bold = True
r_q2_t.font.color.rgb = PINO
r_q2_d = p_q2.add_run()
r_q2_d.text = "Una empresa extingue el contrato indefinido de una trabajadora contratada en 2016 (10 años exactos de antigüedad) cuyo salario bruto es de 2.400 €/mes con pagas extras prorrateadas (salario diario = 80 €/día), alegando causas organizativas. a) Calcula la indemnización legal si el despido es declarado Objetivo Procedente (20 días/año) y si un juzgado lo declara Improcedente (33 días/año), indicando el sobrecoste en euros. b) ¿Qué ocurriría si la trabajadora estuviera embarazada y el despido careciera de causa real?"
r_q2_d.font.color.rgb = TINTA

# ==============================================================================
# SLIDE 21: FASE 5B · RETO MANUSCRITO TURNO VIERNES (LÍNEA 2)
# ==============================================================================
s21 = prs.slides.add_slide(blank_layout)
set_slide_background(s21, BLANCO)
add_header(s21, "Fase 5b (95–105 min) · Reto Manuscrito Individual (10 min · Solo Papel)", "Turno Viernes · Línea 2 (13 de Noviembre de 2026)", 21)

add_card(s21, Inches(0.8), Inches(1.45), Inches(11.733), Inches(5.3), MENTA, BORDE_MENTA)
tb_s21 = s21.shapes.add_textbox(Inches(1.1), Inches(1.65), Inches(11.1), Inches(4.9))
tf_s21 = tb_s21.text_frame
tf_s21.word_wrap = True

p_r2 = tf_s21.paragraphs[0]
p_r2.text = "RETO DE EVALUACIÓN CONTINUA · TURNO VIERNES (LÍNEA 2) · 1.000 PTS"
p_r2.font.name = "Outfit"
p_r2.font.size = Pt(16)
p_r2.font.bold = True
p_r2.font.color.rgb = PINO

p_warn2 = tf_s21.add_paragraph()
p_warn2.text = "Entorno libre de pantallas. Redacta a mano en tu cuartilla oficial (máximo 1 cara por alumno):"
p_warn2.font.name = "Calibri"
p_warn2.font.size = Pt(12.5)
p_warn2.font.color.rgb = CORAL
p_warn2.space_before = Pt(4)

p_q2_1 = tf_s21.add_paragraph()
p_q2_1.font.name = "Calibri"
p_q2_1.font.size = Pt(13.5)
p_q2_1.space_before = Pt(14)
r_q2_1_t = p_q2_1.add_run()
r_q2_1_t.text = "1. (500 pts) La Reforma Laboral (RDL 32/2021) y la Brecha Público-Privada:\n"
r_q2_1_t.font.bold = True
r_q2_1_t.font.color.rgb = PINO
r_q2_1_d = p_q2_1.add_run()
r_q2_1_d.text = "Expón las principales medidas introducidas por el Real Decreto-ley 32/2021 para reducir la temporalidad en España (supresión de modalidad contractual, nuevas causas del art. 15 ET y penalización a contratos muy cortos). ¿Qué impacto ha tenido sobre la tasa de temporalidad del sector privado y por qué persiste una brecha tan acusada frente al sector público (>30%)?"
r_q2_1_d.font.color.rgb = TINTA

p_q2_2 = tf_s21.add_paragraph()
p_q2_2.font.name = "Calibri"
p_q2_2.font.size = Pt(13.5)
p_q2_2.space_before = Pt(14)
r_q2_2_t = p_q2_2.add_run()
r_q2_2_t.text = "2. (500 pts) La Paradoja Estadística y Laboral del Contrato Fijo Discontinuo:\n"
r_q2_2_t.font.bold = True
r_q2_2_t.font.color.rgb = PINO
r_q2_2_d = p_q2_2.add_run()
r_q2_2_d.text = "Un trabajador de hostelería con contrato fijo discontinuo finaliza la campaña de verano y pasa a situación de inactividad durante 4 meses, solicitando su prestación por desempleo. a) Explica con precisión cómo se contabiliza a este trabajador durante esos 4 meses en el Paro Registrado del SEPE (y por qué) frente a cómo lo clasifica la EPA del INE. b) Señala una ventaja y una limitación real del auge de esta figura contractual tras 2022."
r_q2_2_d.font.color.rgb = TINTA

# ==============================================================================
# SLIDE 22: FASE 5C · SUBIDA FOTOGRÁFICA INSTANTÁNEA (QR FORMS)
# ==============================================================================
s22 = prs.slides.add_slide(blank_layout)
set_slide_background(s22, BLANCO)
add_header(s22, "Fase 5c (105–107 min · 2 min) · Subida Fotográfica Instantánea", "Escanea y Sube la Fotografía de tu Cuartilla a Microsoft Forms", 22)

add_card(s22, Inches(0.8), Inches(1.45), Inches(7.5), Inches(5.3), MENTA, BORDE_MENTA)
tb_s22_t = s22.shapes.add_textbox(Inches(1.1), Inches(1.7), Inches(6.9), Inches(4.8))
tf_s22_t = tb_s22_t.text_frame
tf_s22_t.word_wrap = True

p_s22_h = tf_s22_t.paragraphs[0]
p_s22_h.text = "Instrucciones de Subida (2 minutos exactos):"
p_s22_h.font.name = "Outfit"
p_s22_h.font.size = Pt(16)
p_s22_h.font.bold = True
p_s22_h.font.color.rgb = PINO

steps_s22 = [
    ("Paso 1 · Cámara:", " Desbloquea tu teléfono móvil y abre la cámara fotográfica."),
    ("Paso 2 · Foto Nítida:", " Toma una fotografía cenital nítida y bien iluminada de la cara redactada de tu cuartilla oficial."),
    ("Paso 3 · Subida Forms:", " Escanea el código QR de la derecha o entra en el enlace institucional de Microsoft Forms."),
    ("Paso 4 · Anonimización:", " Tu entrega quedará vinculada a tu cuenta institucional UPO. El sistema anonimiza automáticamente la cuartilla para la evaluación ciega."),
    ("Recompensa:", " Cada entrega válida suma en tu Pasaporte de Evaluación Continua para bonificaciones del examen final (70%).")
]
for s_tit, s_desc in steps_s22:
    p = tf_s22_t.add_paragraph()
    p.space_before = Pt(8)
    p.font.name = "Calibri"
    p.font.size = Pt(13)
    r1 = p.add_run()
    r1.text = s_tit + " "
    r1.font.bold = True
    r1.font.color.rgb = PINO
    r2 = p.add_run()
    r2.text = s_desc
    r2.font.color.rgb = TINTA

add_card(s22, Inches(8.55), Inches(1.45), Inches(3.98), Inches(5.3), BLANCO, BORDE_CORAL, Pt(1.5))
tb_s22_qr = s22.shapes.add_textbox(Inches(8.75), Inches(1.65), Inches(3.6), Inches(1.0))
tf_s22_qr = tb_s22_qr.text_frame
tf_s22_qr.word_wrap = True

p_qr_r_h = tf_s22_qr.paragraphs[0]
p_qr_r_h.text = "Subida de Cuartilla"
p_qr_r_h.alignment = PP_ALIGN.CENTER
p_qr_r_h.font.name = "Outfit"
p_qr_r_h.font.size = Pt(16)
p_qr_r_h.font.bold = True
p_qr_r_h.font.color.rgb = PINO

p_qr_r_sub = tf_s22_qr.add_paragraph()
p_qr_r_sub.text = "Microsoft Forms Institucional UPO"
p_qr_r_sub.alignment = PP_ALIGN.CENTER
p_qr_r_sub.font.name = "Calibri"
p_qr_r_sub.font.size = Pt(11)
p_qr_r_sub.font.color.rgb = SALVIA

if os.path.exists(QR_RETO):
    s22.shapes.add_picture(QR_RETO, Inches(9.2), Inches(2.75), width=Inches(2.7), height=Inches(2.7))

tb_s22_url = s22.shapes.add_textbox(Inches(8.75), Inches(5.75), Inches(3.6), Inches(0.8))
p_u_r = tb_s22_url.text_frame.paragraphs[0]
p_u_r.alignment = PP_ALIGN.CENTER
p_u_r.text = "forms.office.com/e/PSLL-Reto-Sesion12\nCierre automático a los 2 minutos"
p_u_r.font.name = "Calibri"
p_u_r.font.size = Pt(9.5)
p_u_r.font.color.rgb = SALVIA

# ==============================================================================
# SLIDE 23: FASE 5D · RÚBRICA Y SOLUCIÓN TURNO MARTES (LÍNEA 1)
# ==============================================================================
s23 = prs.slides.add_slide(blank_layout)
set_slide_background(s23, BLANCO)
add_header(s23, "Fase 5d (107–120 min) · Feedback Formativo Inmediato", "Solución Modelo y Rúbrica Oficial (0–1.000 pts) · Turno Martes (L1)", 23)

add_card(s23, Inches(0.8), Inches(1.45), Inches(5.7), Inches(5.3), MENTA, BORDE_MENTA)
tb_s23_1 = s23.shapes.add_textbox(Inches(1.05), Inches(1.65), Inches(5.2), Inches(4.9))
tf_s23_1 = tb_s23_1.text_frame
tf_s23_1.word_wrap = True

p_sol1_h = tf_s23_1.paragraphs[0]
p_sol1_h.text = "Cuestión 1 · Flexiseguridad vs. Dualidad (500 pts)"
p_sol1_h.font.name = "Outfit"
p_sol1_h.font.size = Pt(14)
p_sol1_h.font.bold = True
p_sol1_h.font.color.rgb = PINO

bullets_sol1 = [
    ("Triángulo de Oro Danés (200 pts):", " Combina: 1) Baja protección del puesto fijo (despido flexible); 2) Seguro de desempleo muy generoso; y 3) Políticas Activas de Empleo (PAE) eficaces que recualifican y recolocan al trabajador."),
    ("Dualidad Española (150 pts):", " Segmentación entre insiders (indefinidos con alta protección) y outsiders (temporales precarios sin tutela judicial)."),
    ("Efecto de la Brecha ΔEPL (150 pts):", " Una gran diferencia entre el coste de despedir a un fijo y a un temporal genera un 'efecto umbral': las empresas rotan a los temporales antes del límite legal, no invierten en su formación y destruyen empleo masivamente en las crisis.")
]
for b_t, b_d in bullets_sol1:
    p = tf_s23_1.add_paragraph()
    p.font.name = "Calibri"
    p.font.size = Pt(12)
    p.space_before = Pt(8)
    r1 = p.add_run()
    r1.text = "• " + b_t
    r1.font.bold = True
    r1.font.color.rgb = PINO
    r2 = p.add_run()
    r2.text = b_d
    r2.font.color.rgb = TINTA

add_card(s23, Inches(6.8), Inches(1.45), Inches(5.733), Inches(5.3), MENTA, BORDE_MENTA)
tb_s23_2 = s23.shapes.add_textbox(Inches(7.05), Inches(1.65), Inches(5.2), Inches(4.9))
tf_s23_2 = tb_s23_2.text_frame
tf_s23_2.word_wrap = True

p_sol2_h = tf_s23_2.paragraphs[0]
p_sol2_h.text = "Cuestión 2 · Caso Aplicado de Despido (500 pts)"
p_sol2_h.font.name = "Outfit"
p_sol2_h.font.size = Pt(14)
p_sol2_h.font.bold = True
p_sol2_h.font.color.rgb = PINO

bullets_sol2 = [
    ("a.1) Objetivo Procedente (150 pts):", " 20 días/año (tope 12 meses): 10 años × 20 días × 80 €/día = 16.000 € (200 días < tope de 360 días)."),
    ("a.2) Improcedente y Sobrecoste (200 pts):", " 33 días/año (tope 24 meses): 10 años × 33 días × 80 €/día = 26.400 €. El sobrecoste por improcedencia es de +10.400 € (+65%)."),
    ("b) Despido de Trabajadora Embarazada (150 pts):", " Conforme al art. 55.5 ET, es un Despido Nulo por tutela objetiva de la maternidad: conlleva la readmisión obligatoria inmediata en su puesto y el abono íntegro de los salarios de tramitación.")
]
for b_t, b_d in bullets_sol2:
    p = tf_s23_2.add_paragraph()
    p.font.name = "Calibri"
    p.font.size = Pt(12)
    p.space_before = Pt(8)
    r1 = p.add_run()
    r1.text = "• " + b_t
    r1.font.bold = True
    r1.font.color.rgb = CORAL
    r2 = p.add_run()
    r2.text = b_d
    r2.font.color.rgb = TINTA

# ==============================================================================
# SLIDE 24: FASE 5D · RÚBRICA Y SOLUCIÓN TURNO VIERNES (LÍNEA 2)
# ==============================================================================
s24 = prs.slides.add_slide(blank_layout)
set_slide_background(s24, BLANCO)
add_header(s24, "Fase 5d (107–120 min) · Feedback Formativo Inmediato", "Solución Modelo y Rúbrica Oficial (0–1.000 pts) · Turno Viernes (L2)", 24)

add_card(s24, Inches(0.8), Inches(1.45), Inches(5.7), Inches(5.3), MENTA, BORDE_MENTA)
tb_s24_1 = s24.shapes.add_textbox(Inches(1.05), Inches(1.65), Inches(5.2), Inches(4.9))
tf_s24_1 = tb_s24_1.text_frame
tf_s24_1.word_wrap = True

p_sol3_h = tf_s24_1.paragraphs[0]
p_sol3_h.text = "Cuestión 1 · RDL 32/2021 y Brecha Pública (500 pts)"
p_sol3_h.font.name = "Outfit"
p_sol3_h.font.size = Pt(14)
p_sol3_h.font.bold = True
p_sol3_h.font.color.rgb = PINO

bullets_sol3 = [
    ("Medidas del RDL 32/2021 (300 pts):", " 1) Supresión del contrato por obra o servicio y presunción indefinida; 2) Temporales causales restringidos a circunstancias imprevisibles (máx. 6–12 meses), previsibles (90 días/año) y sustitución; 3) Límite de encadenamiento de 18 meses en 24 y penalización de 31,40 € a contratos <30 días."),
    ("Brecha Privada vs. Pública (200 pts):", " La temporalidad privada ha caído del 29,2% al 12,4% (convergiendo con la UE), mientras la pública supera el 30% por el abuso histórico de interinidades en sanidad y educación y el retraso en estabilizar plazas (Ley 20/2021).")
]
for b_t, b_d in bullets_sol3:
    p = tf_s24_1.add_paragraph()
    p.font.name = "Calibri"
    p.font.size = Pt(12)
    p.space_before = Pt(8)
    r1 = p.add_run()
    r1.text = "• " + b_t
    r1.font.bold = True
    r1.font.color.rgb = PINO
    r2 = p.add_run()
    r2.text = b_d
    r2.font.color.rgb = TINTA

add_card(s24, Inches(6.8), Inches(1.45), Inches(5.733), Inches(5.3), MENTA, BORDE_MENTA)
tb_s24_2 = s24.shapes.add_textbox(Inches(7.05), Inches(1.65), Inches(5.2), Inches(4.9))
tf_s24_2 = tb_s24_2.text_frame
tf_s24_2.word_wrap = True

p_sol4_h = tf_s24_2.paragraphs[0]
p_sol4_h.text = "Cuestión 2 · Fijo Discontinuo SEPE vs. EPA (500 pts)"
p_sol4_h.font.name = "Outfit"
p_sol4_h.font.size = Pt(14)
p_sol4_h.font.bold = True
p_sol4_h.font.color.rgb = PINO

bullets_sol4 = [
    ("a) Contabilización en Inactividad (300 pts):", " Al estar el contrato suspendido y no extinguido, en el SEPE figura como DENO (Demandante No Ocupado con relación laboral) y NO suma en el Paro Registrado (Orden de 1985). En cambio, la EPA (INE) aplica criterios OIT: al no trabajar esa semana no es ocupado; si busca otro empleo es Parado EPA y si espera el llamamiento sin buscar es Inactivo EPA."),
    ("b) Ventaja y Limitación (200 pts):", " Ventaja: estabilidad jurídica indefinida, derecho de llamamiento y cómputo de antigüedad. Limitación: intermitencia salarial anual y mayor rotación de contratos indefinidos.")
]
for b_t, b_d in bullets_sol4:
    p = tf_s24_2.add_paragraph()
    p.font.name = "Calibri"
    p.font.size = Pt(12)
    p.space_before = Pt(8)
    r1 = p.add_run()
    r1.text = "• " + b_t
    r1.font.bold = True
    r1.font.color.rgb = CORAL
    r2 = p.add_run()
    r2.text = b_d
    r2.font.color.rgb = TINTA

# ==============================================================================
# SLIDE 25: CIERRE INSTITUCIONAL Y PASAPORTE DIGITAL
# ==============================================================================
s25 = prs.slides.add_slide(blank_layout)
set_slide_background(s25, BLANCO)
add_header(s25, "Cierre de Sesión y Pasaporte Digital", "Síntesis de la Sesión 12 y Avance de la Sesión 13 · Tema 4 (II)", 25)

add_card(s25, Inches(0.8), Inches(1.45), Inches(7.5), Inches(5.3), MENTA, BORDE_MENTA)
tb_s25 = s25.shapes.add_textbox(Inches(1.05), Inches(1.65), Inches(6.9), Inches(4.9))
tf_s25 = tb_s25.text_frame
tf_s25.word_wrap = True

p_c_h = tf_s25.paragraphs[0]
p_c_h.text = "Conclusiones de la Sesión 12 y Próxima Clase"
p_c_h.font.name = "Outfit"
p_c_h.font.size = Pt(16)
p_c_h.font.bold = True
p_c_h.font.color.rgb = PINO

concl_items = [
    ("De la Dualidad a la Estabilidad Contractual:", " La restricción del contrato temporal (RDL 32/2021) ha reducido la temporalidad privada al 12,4%, desplazando el reto hacia la duración efectiva de los empleos y el sector público."),
    ("Dominio Técnico del Despido y EPL:", " La diferencia entre 12, 20 y 33 días de salario determina la gestión estratégica de plantillas y los incentivos empresariales."),
    ("Próxima Clase · Sesión 13 (Tema 4 · Parte II):", " Analizaremos la Flexibilidad Interna (ERTE y Mecanismo RED, el cambio estructural en la pandemia) y las Políticas de Reparto del Trabajo y Reducción de Jornada a 37,5 horas."),
    ("Pasaporte Digital:", " Las calificaciones anonimizadas de esta sesión se actualizarán en el Pasaporte de Evaluación Continua.")
]
for c_t, c_d in concl_items:
    p = tf_s25.add_paragraph()
    p.space_before = Pt(8)
    p.font.name = "Calibri"
    p.font.size = Pt(13)
    r1 = p.add_run()
    r1.text = c_t + " "
    r1.font.bold = True
    r1.font.color.rgb = PINO
    r2 = p.add_run()
    r2.text = c_d
    r2.font.color.rgb = TINTA

add_card(s25, Inches(8.55), Inches(1.45), Inches(3.98), Inches(5.3), BLANCO, BORDE_CORAL, Pt(1.5))
tb_s25_qr = s25.shapes.add_textbox(Inches(8.75), Inches(1.65), Inches(3.6), Inches(1.0))
tf_s25_qr = tb_s25_qr.text_frame
tf_s25_qr.word_wrap = True

p_pas_h = tf_s25_qr.paragraphs[0]
p_pas_h.text = "Pasaporte PSLL"
p_pas_h.alignment = PP_ALIGN.CENTER
p_pas_h.font.name = "Outfit"
p_pas_h.font.size = Pt(16)
p_pas_h.font.bold = True
p_pas_h.font.color.rgb = PINO

p_pas_sub = tf_s25_qr.add_paragraph()
p_pas_sub.text = "Consulta tu saldo de puntos acumulados"
p_pas_sub.alignment = PP_ALIGN.CENTER
p_pas_sub.font.name = "Calibri"
p_pas_sub.font.size = Pt(11)
p_pas_sub.font.color.rgb = SALVIA

if os.path.exists(QR_PASAPORTE):
    s25.shapes.add_picture(QR_PASAPORTE, Inches(9.2), Inches(2.75), width=Inches(2.7), height=Inches(2.7))

tb_s25_url = s25.shapes.add_textbox(Inches(8.75), Inches(5.75), Inches(3.6), Inches(0.8))
p_u_p = tb_s25_url.text_frame.paragraphs[0]
p_u_p.alignment = PP_ALIGN.CENTER
p_u_p.text = "mhidper.github.io/micro_apps/\npasaporte_psll.html"
p_u_p.font.name = "Calibri"
p_u_p.font.size = Pt(10)
p_u_p.font.bold = True
p_u_p.font.color.rgb = PINO

# Guardar PPTX
prs.save(OUTPUT_PPTX)
print("¡Presentación PPTX generada con éxito en:", OUTPUT_PPTX)

# Exportar a PDF mediante COM PowerPoint vía PowerShell
try:
    ps_cmd = (
        f'$pp = New-Object -ComObject PowerPoint.Application; '
        f'$pres = $pp.Presentations.Open("{OUTPUT_PPTX}", $true, $false, $false); '
        f'$pres.SaveAs("{OUTPUT_PDF}", 32); '
        f'$pres.Close(); '
        f'$pp.Quit()'
    )
    subprocess.run(["powershell", "-NoProfile", "-Command", ps_cmd], check=True)
    print("¡Exportación PDF generada con éxito en:", OUTPUT_PDF)
except Exception as e:
    print("Aviso al exportar PDF:", e)
