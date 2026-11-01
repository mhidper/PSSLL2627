# -*- coding: utf-8 -*-
"""
Generador oficial de la presentación para la Sesión EB 11:
«Garantía de rentas, trampa de la pobreza e Ingreso Mínimo Vital (IMV)»
Asignatura: Políticas Sociolaborales y de Empleo (UPO)
Profesor: Manuel A. Hidalgo Pérez
"""

import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE

# 1. Rutas
BASE_DIR = r"c:\Users\Usuario\Documents\Dropbox\DOCENCIA UPO\CURSO 26-27\PSLL"
SESION_DIR = os.path.join(BASE_DIR, r"Temas EB\Sesiones EB\Sesion 11")
LOGOS_DIR = os.path.join(BASE_DIR, "Logos y skills")
SKILL_ASSETS_DIR = os.path.join(LOGOS_DIR, "psll-presentaciones-skill", "assets")

LOGO_PSLL = os.path.join(LOGOS_DIR, "logo_psll_upo.png")
LOGO_UPO = os.path.join(SKILL_ASSETS_DIR, "upo_logo.jpg")
LOCKUP_PSLL = os.path.join(LOGOS_DIR, "psll_lockup.png")

FIG_3_4 = os.path.join(SESION_DIR, "figura_3_4_trampa_pobreza_emtr.png")
FIG_3_6 = os.path.join(SESION_DIR, "figura_3_6_nacionalidad_imv.png")
FIG_3_5 = os.path.join(SESION_DIR, "figura_3_5_cobertura_nontakeup_imv.png")

QR_SONDEO = os.path.join(SESION_DIR, "qr_sondeo_sesion11.png")
QR_APP = os.path.join(SESION_DIR, "qr_app_sesion11.png")
QR_RETO = os.path.join(SESION_DIR, "qr_reto_sesion11.png")
QR_PASAPORTE = os.path.join(SESION_DIR, "qr_pasaporte_psll.png")

OUTPUT_PPTX = os.path.join(SESION_DIR, "Sesion 11 - Garantia de rentas, trampa de la pobreza e Ingreso Minimo Vital.pptx")

# 2. Paleta Oficial de Marca PSLL
PINO = RGBColor(17, 57, 39)       # #113927 (Primario)
PINO_DARK = RGBColor(11, 36, 25)  # #0B2419
SALVIA = RGBColor(118, 146, 122)  # #76927A (Estructura/Subtítulos)
CORAL = RGBColor(233, 143, 113)   # #E98F71 (Acento dinámico)
MENTA = RGBColor(244, 248, 245)   # #F4F8F5 (Fondo de tarjetas)
TINTA = RGBColor(47, 58, 48)      # #2F3A30 (Texto lectura)
MELOCOTON = RGBColor(237, 176, 144) # #EDB090
BLANCO = RGBColor(255, 255, 255)  # #FFFFFF
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
    # Categoría
    tx_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.4), Inches(10.5), Inches(0.35))
    tf = tx_box.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = categoria.upper()
    p.font.name = "Outfit"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = SALVIA

    # Título
    tx_box2 = slide.shapes.add_textbox(Inches(0.8), Inches(0.72), Inches(10.8), Inches(0.55))
    tf2 = tx_box2.text_frame
    tf2.word_wrap = True
    p2 = tf2.paragraphs[0]
    p2.text = titulo
    p2.font.name = "Outfit"
    p2.font.size = Pt(20)
    p2.font.bold = True
    p2.font.color.rgb = PINO

    # Lockup esquina
    if os.path.exists(LOCKUP_PSLL):
        slide.shapes.add_picture(LOCKUP_PSLL, Inches(11.8), Inches(0.42), width=Inches(1.013), height=Inches(0.320))

    # Paginación
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

# Logo PSLL centrado
if os.path.exists(LOGO_PSLL):
    s1.shapes.add_picture(LOGO_PSLL, Inches(4.267), Inches(0.550), width=Inches(4.800), height=Inches(2.618))

# Bloque Textual Central
tb_s1 = s1.shapes.add_textbox(Inches(1.000), Inches(3.350), Inches(11.333), Inches(0.600))
p_over = tb_s1.text_frame.paragraphs[0]
p_over.alignment = PP_ALIGN.CENTER
p_over.text = "POLÍTICAS SOCIOLABORALES Y DE EMPLEO"
p_over.font.name = "Outfit"
p_over.font.size = Pt(25)
p_over.font.bold = True
p_over.font.color.rgb = BLANCO

tb_s1_sub = s1.shapes.add_textbox(Inches(1.000), Inches(4.000), Inches(11.333), Inches(0.550))
p_tit = tb_s1_sub.text_frame.paragraphs[0]
p_tit.alignment = PP_ALIGN.CENTER
p_tit.text = "Sesión 11 – Garantía de Rentas, Trampa de la Pobreza e IMV"
p_tit.font.name = "Outfit"
p_tit.font.size = Pt(18)
p_tit.font.bold = True
p_tit.font.color.rgb = CORAL

tb_s1_meta = s1.shapes.add_textbox(Inches(1.000), Inches(4.600), Inches(11.333), Inches(0.400))
p_meta = tb_s1_meta.text_frame.paragraphs[0]
p_meta.alignment = PP_ALIGN.CENTER
p_meta.text = "Semana 8  ·  Código 102023  ·  Manuel A. Hidalgo Pérez"
p_meta.font.name = "Calibri"
p_meta.font.size = Pt(13)
p_meta.font.color.rgb = RGBColor(244, 248, 245)

# Franja inferior blanca con Escudo UPO
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
add_header(s2, "Metodología de Aula · Curso 2026-27", "Hoja de Ruta · Arquitectura en 5 Fases de la Sesión 11 (120 min)", 2)

fases_data = [
    ("Fase 1 · 00–20 min", "Apertura y Sondeo Previo", "Noticia de Cinco Días (M. Hidalgo), los 3 estigmas del IMV, sondeo en directo con Forms y choque empírico de microdatos AIReF.", PINO),
    ("Fase 2 · 20–45 min", "Mini-Lección I: Garantía de Rentas", "De las 17 RMI autonómicas a la Ley 19/2021 del IMV. Diseño diferencial, escala de convivencia, CAPI y la barrera del non-take-up.", SALVIA),
    ("Fase 3 · 45–70 min", "Mini-Lección II: Trampa del EMTR", "Tipo marginal efectivo (EMTR = 100% y >100% con ayudas concurrentes). Evidencia AIReF (-3 pp). Incentivo RD 240/2026 y reformas.", PINO),
    ("Fase 4 · 70–85 min", "Laboratorio con Micro-App", "Móviles activos (15 min): simulación del caso María, la trampa de inactividad y el dilema macro del ministro en simulador_imv_trampa.html.", CORAL),
    ("Fase 5 · 85–120 min", "Reto Manuscrito y Evaluación", "Síntesis en pizarra (10 min), reto individual en papel sin pantallas (10 min), subida con QR a Forms y feedback formativo inmediato con rúbrica.", PINO)
]

y_pos = Inches(1.45)
for f_tag, f_tit, f_desc, f_col in fases_data:
    add_card(s2, Inches(0.8), y_pos, Inches(11.733), Inches(0.95), MENTA, BORDE_MENTA)
    
    # Pill color
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
    
    # Texto
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
# SLIDE 3: FASE 1 · APERTURA CON GANCHO (COLUMNA CINCO DÍAS)
# ==============================================================================
s3 = prs.slides.add_slide(blank_layout)
set_slide_background(s3, BLANCO)
add_header(s3, "Fase 1 (00–20 min) · Apertura y Gancho de Actualidad", "El Debate Público: «Un Ingreso Mínimo Vital mejor diseñado alcanzaría mejor sus objetivos»", 3)

add_card(s3, Inches(0.8), Inches(1.45), Inches(7.5), Inches(5.3), MENTA, BORDE_MENTA)
tb_s3 = s3.shapes.add_textbox(Inches(1.05), Inches(1.65), Inches(7.0), Inches(4.9))
tf_s3 = tb_s3.text_frame
tf_s3.word_wrap = True

p_art_tag = tf_s3.paragraphs[0]
p_art_tag.text = "CINCO DÍAS · TRIBUNA DE ECONOMÍA Y EMPLEO"
p_art_tag.font.name = "Outfit"
p_art_tag.font.size = Pt(11)
p_art_tag.font.bold = True
p_art_tag.font.color.rgb = CORAL

p_art_tit = tf_s3.add_paragraph()
p_art_tit.text = "«Tres estigmas han surgido desde el inicio de su implementación:"
p_art_tit.font.name = "Outfit"
p_art_tit.font.size = Pt(15)
p_art_tit.font.bold = True
p_art_tit.font.color.rgb = PINO

bullets_s3 = [
    ("1. Transferencia para no trabajar:", " Se argumenta que destruye la oferta laboral, cuando 2 de cada 3 hogares perceptores han tenido rentas del trabajo en el último año."),
    ("2. Prestación para adultos sin cargas:", " El 40% de los beneficiarios son menores de edad, el 70% de hogares tienen menores a cargo y el 68% de titulares son mujeres."),
    ("3. Fraude generalizado:", " Los informes de la AIReF documentan que el problema crítico es la exclusión (non-take-up), no la picaresca: el 55% de hogares con derecho no lo solicita, y el 72% no solicita el complemento por hijo».")
]
for b_tit, b_desc in bullets_s3:
    p_b = tf_s3.add_paragraph()
    p_b.font.name = "Calibri"
    p_b.font.size = Pt(13)
    p_b.space_before = Pt(8)
    r1 = p_b.add_run()
    r1.text = "• " + b_tit
    r1.font.bold = True
    r1.font.color.rgb = PINO
    r2 = p_b.add_run()
    r2.text = b_desc
    r2.font.color.rgb = TINTA

# Tarjeta lateral de reflexión
add_card(s3, Inches(8.55), Inches(1.45), Inches(3.98), Inches(5.3), BLANCO, BORDE_CORAL, Pt(1.5))
tb_s3_lat = s3.shapes.add_textbox(Inches(8.8), Inches(1.65), Inches(3.5), Inches(4.9))
tf_s3_lat = tb_s3_lat.text_frame
tf_s3_lat.word_wrap = True

p_lat_h = tf_s3_lat.paragraphs[0]
p_lat_h.text = "Dilema para el Aula"
p_lat_h.font.name = "Outfit"
p_lat_h.font.size = Pt(15)
p_lat_h.font.bold = True
p_lat_h.font.color.rgb = CORAL

p_lat_body = tf_s3_lat.add_paragraph()
p_lat_body.font.name = "Calibri"
p_lat_body.font.size = Pt(13.5)
p_lat_body.space_before = Pt(10)
p_lat_body.text = "Si la pobreza extrema supera los 2 millones de personas en España:\n\n¿Por qué más de la mitad de las familias que tienen derecho reconocido por ley no lo cobran?\n\n¿Y por qué trabajar a tiempo parcial puede costarle dinero a una madre sola perceptora de la ayuda?"
p_lat_body.font.color.rgb = TINTA

# ==============================================================================
# SLIDE 4: FASE 1 · EL ENIGMA DE AULA
# ==============================================================================
s4 = prs.slides.add_slide(blank_layout)
set_slide_background(s4, BLANCO)
add_header(s4, "Fase 1 (00–20 min) · Apertura y Planteamiento del Enigma", "¿Por Qué Cuesta Tanto Ayudar a Quien Más lo Necesita sin Desincentivar?", 4)

add_card(s4, Inches(0.8), Inches(1.45), Inches(5.7), Inches(5.3), MENTA, BORDE_MENTA)
tb_s4_1 = s4.shapes.add_textbox(Inches(1.05), Inches(1.65), Inches(5.2), Inches(4.9))
tf_s4_1 = tb_s4_1.text_frame
tf_s4_1.word_wrap = True

p_e1 = tf_s4_1.paragraphs[0]
p_e1.text = "Enigma 1 · La Trampa de la Inactividad"
p_e1.font.name = "Outfit"
p_e1.font.size = Pt(15)
p_e1.font.bold = True
p_e1.font.color.rgb = PINO

p_e1_b = tf_s4_1.add_paragraph()
p_e1_b.font.name = "Calibri"
p_e1_b.font.size = Pt(13)
p_e1_b.space_before = Pt(10)
p_e1_b.text = "Una persona sin ingresos cobra 734 €/mes de IMV. Si encuentra un empleo de 400 €:\n\n• Bajo el modelo diferencial tradicional, la ayuda baja exactamente en 400 € (pasa a 334 €).\n• La suma total sigue siendo 734 €.\n• Si acudir al trabajo le exige pagar 80 € de transporte y vestimenta, sus ingresos líquidos finales son 654 €.\n\nResultado paradójico: Trabajar le cuesta 80 € netos al mes frente a quedarse en casa."
p_e1_b.font.color.rgb = TINTA

add_card(s4, Inches(6.8), Inches(1.45), Inches(5.733), Inches(5.3), MENTA, BORDE_MENTA)
tb_s4_2 = s4.shapes.add_textbox(Inches(7.05), Inches(1.65), Inches(5.2), Inches(4.9))
tf_s4_2 = tb_s4_2.text_frame
tf_s4_2.word_wrap = True

p_e2 = tf_s4_2.paragraphs[0]
p_e2.text = "Enigma 2 · La Exclusión del Non-Take-Up"
p_e2.font.name = "Outfit"
p_e2.font.size = Pt(15)
p_e2.font.bold = True
p_e2.font.color.rgb = PINO

p_e2_b = tf_s4_2.add_paragraph()
p_e2_b.font.name = "Calibri"
p_e2_b.font.size = Pt(13)
p_e2_b.space_before = Pt(10)
p_e2_b.text = "La Seguridad Social presupuesta más de 4.000 M€ anuales para el IMV:\n\n• Sin embargo, el 55% de los hogares en extrema necesidad no lo solicita (y el 72% en el CAPI infantil).\n• Dos de cada tres denegaciones se deben a trabas probatorias con el padrón histórico o la unidad de convivencia.\n• Quienes lo cobran viven con miedo a revisiones anuales retroactivas que les reclamen miles de euros indebidos.\n\nResultado paradójico: El sistema teme tanto el fraude de inclusión que provoca una exclusión masiva de inocentes."
p_e2_b.font.color.rgb = TINTA

# ==============================================================================
# SLIDE 5: FASE 1 · SONDEO EN DIRECTO CON FORMS (MÓVILES ACTIVOS)
# ==============================================================================
s5 = prs.slides.add_slide(blank_layout)
set_slide_background(s5, BLANCO)
add_header(s5, "Fase 1 (00–20 min) · Participación en Directo (Móviles Activos)", "Sondeo de Aula: ¿Quién es el Beneficiario Típico del IMV en España?", 5)

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
p_s5_sub.text = "Conforme a tu intuición espontánea y lo que escuchas en el debate público, ¿cuál de estas tres afirmaciones describe con mayor precisión la realidad del IMV?"
p_s5_sub.font.name = "Calibri"
p_s5_sub.font.size = Pt(13.5)
p_s5_sub.space_before = Pt(8)
p_s5_sub.font.color.rgb = TINTA

opts = [
    ("[Opción A]", "La mayoría de los beneficiarios son adultos que deciden no trabajar y vivir permanentemente del subsidio público."),
    ("[Opción B]", "La mayoría de perceptores son familias con menores y trabajadores que tienen empleo pero con salarios de pobreza."),
    ("[Opción C]", "El principal problema del sistema es el fraude generalizado de personas que ocultan ingresos en la economía sumergida.")
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

# QR Box
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

# Enlace texto
tb_s5_url = s5.shapes.add_textbox(Inches(8.75), Inches(5.75), Inches(3.6), Inches(0.8))
p_url = tb_s5_url.text_frame.paragraphs[0]
p_url.alignment = PP_ALIGN.CENTER
p_url.text = "forms.office.com/e/PSLL-Sondeo-Sesion11\nSolo dispositivos autorizados para el sondeo"
p_url.font.name = "Calibri"
p_url.font.size = Pt(9.5)
p_url.font.color.rgb = SALVIA

# ==============================================================================
# SLIDE 6: FASE 1 · CHOQUE EMPÍRICO (FIGURA 3.5 AIREF)
# ==============================================================================
s6 = prs.slides.add_slide(blank_layout)
set_slide_background(s6, BLANCO)
add_header(s6, "Fase 1 (00–20 min) · Choque Empírico con Microdatos Oficiales", "Desmontando Prejuicios: Microdatos Oficiales de la AIReF y la Seguridad Social", 6)

if os.path.exists(FIG_3_5):
    s6.shapes.add_picture(FIG_3_5, Inches(0.8), Inches(1.45), width=Inches(11.733), height=Inches(3.85))

# Banner explicativo inferior
add_card(s6, Inches(0.8), Inches(5.45), Inches(11.733), Inches(1.35), MENTA, BORDE_MENTA)
tb_s6_inf = s6.shapes.add_textbox(Inches(1.0), Inches(5.5), Inches(11.3), Inches(1.2))
tf_s6_inf = tb_s6_inf.text_frame
tf_s6_inf.word_wrap = True

p_s6_b1 = tf_s6_inf.paragraphs[0]
p_s6_b1.font.name = "Calibri"
p_s6_b1.font.size = Pt(12)
r1 = p_s6_b1.add_run()
r1.text = "1. No es un subsidio para no trabajar: "
r1.font.bold = True
r1.font.color.rgb = PINO
r2 = p_s6_b1.add_run()
r2.text = "El 66,7% (2 de cada 3) ha tenido ingresos laborales en el último año. El IMV complementa salarios bajos y jornadas parciales."

p_s6_b2 = tf_s6_inf.add_paragraph()
p_s6_b2.font.name = "Calibri"
p_s6_b2.font.size = Pt(12)
r3 = p_s6_b2.add_run()
r3.text = "2. No es para adultos sin cargas: "
r3.font.bold = True
r3.font.color.rgb = PINO
r4 = p_s6_b2.add_run()
r4.text = "El 40,2% son menores de edad, el 70% de hogares tienen hijos y el 68,4% de titulares son mujeres (escudo de infancia)."

p_s6_b3 = tf_s6_inf.add_paragraph()
p_s6_b3.font.name = "Calibri"
p_s6_b3.font.size = Pt(12)
r5 = p_s6_b3.add_run()
r5.text = "3. El problema no es el fraude, sino la exclusión: "
r5.font.bold = True
r5.font.color.rgb = CORAL
r6 = p_s6_b3.add_run()
r6.text = "El 55% de hogares con derecho no pide el IMV y el 72% no pide el CAPI por trabas burocráticas de padrón y convivencia."


# ==============================================================================
# SLIDE 7: FASE 1 · DATOS POR NACIONALIDAD Y FILTRO DE RESIDENCIA LEGAL
# ==============================================================================
s6_bis = prs.slides.add_slide(blank_layout)
set_slide_background(s6_bis, BLANCO)
add_header(s6_bis, "Fase 1 (00–20 min) · Evidencia Empírica y Filtro Jurídico", "Figura 3.6 · ¿A Quién Llega el IMV? Nacionalidad, Residencia Legal y Dispersión", 7)

# Inserción de la Figura 3.6 (Gráfico Donut + Dispersión Provincial + Filtro Legal)
if os.path.exists(FIG_3_6):
    s6_bis.shapes.add_picture(FIG_3_6, Inches(0.8), Inches(1.40), width=Inches(11.733), height=Inches(3.85))

# Tarjeta analítica inferior de lectura guiada
add_card(s6_bis, Inches(0.8), Inches(5.38), Inches(11.733), Inches(1.45), MENTA, BORDE_MENTA)
tb_s6b_inf = s6_bis.shapes.add_textbox(Inches(1.0), Inches(5.45), Inches(11.3), Inches(1.3))
tf_s6b_inf = tb_s6b_inf.text_frame
tf_s6b_inf.word_wrap = True

p_s6b_1 = tf_s6b_inf.paragraphs[0]
p_s6b_1.font.name = "Calibri"
p_s6b_1.font.size = Pt(12)
r1 = p_s6b_1.add_run()
r1.text = "1. Mayoría Nacional y Proporcionalidad (Panel A): "
r1.font.bold = True
r1.font.color.rgb = PINO
r2 = p_s6b_1.add_run()
r2.text = "El 82,5% de los perceptores del IMV tienen nacionalidad española (más de 8 de cada 10). La población extranjera supone el 17,5%, en línea con su peso demográfico y laboral en los tramos de salarios bajos."

p_s6b_2 = tf_s6b_inf.add_paragraph()
p_s6b_2.font.name = "Calibri"
p_s6b_2.font.size = Pt(12)
r3 = p_s6b_2.add_run()
r3.text = "2. Dispersión Territorial Productiva (Panel B): "
r3.font.bold = True
r3.font.color.rgb = PINO
r4 = p_s6b_2.add_run()
r4.text = "El peso de extranjeros alcanza el 30%–38% en provincias con agricultura intensiva (Almería, Lleida) por la alta temporalidad, frente a menos del 10% en el sur peninsular (Sevilla 9,1%, Jaén 7,3%)."

p_s6b_3 = tf_s6b_inf.add_paragraph()
p_s6b_3.font.name = "Calibri"
p_s6b_3.font.size = Pt(12)
r5 = p_s6b_3.add_run()
r5.text = "3. El Filtro Legal Ineludible (Panel C): "
r5.font.bold = True
r5.font.color.rgb = CORAL
r6 = p_s6b_3.add_run()
r6.text = "El art. 10 de la Ley 19/2021 exige al menos 1 año ininterrumpido de residencia legal continuada previa. Las personas en situación administrativa irregular tienen cerrado el acceso por imperativo normativo."


# ==============================================================================
# SLIDE 8: FASE 2 · MINI-LECCIÓN I (EL TRÍPODE DE PROTECCIÓN)
# ==============================================================================
s7 = prs.slides.add_slide(blank_layout)
set_slide_background(s7, BLANCO)
add_header(s7, "Fase 2 (20–45 min) · Mini-Lección Quirúrgica I (Sin Pantallas · Solo Papel)", "El Trípode de la Red de Protección de Rentas en España", 8)

cols_s7 = [
    ("NIVEL 1 · CONTRIBUTIVO", "Prestación Contributiva (SEPE)", [
        "Naturaleza: Seguro social ligado a cotización previa.",
        "Requisito: Mínimo 360 días cotizados en 6 años.",
        "Finalidad: Sustituir salario perdido por cese involuntario.",
        "Duración: Tasada (de 4 a 24 meses según cotización).",
        "Cuantía: 70% base reguladora (180 d) y 60% resto."
    ], PINO),
    ("NIVEL 2 · ASISTENCIAL", "Subsidios por Desempleo (SEPE)", [
        "Naturaleza: Asistencial vinculado al mercado de trabajo.",
        "Requisito: Carencia de rentas (<75% SMI) + cargas o edad.",
        "Finalidad: Evitar desprotección tras agotar contributivo.",
        "Duración: Temporal sujeta a prórrogas periódicas.",
        "Cuantía: Fija referenciada al IPREM (80% = 480 €/mes)."
    ], SALVIA),
    ("NIVEL 3 · GARANTÍA RENTAS", "Ingreso Mínimo Vital (INSS)", [
        "Naturaleza: Prestación no contributiva de Seguridad Social.",
        "Requisito: Vulnerabilidad económica extrema del hogar.",
        "Finalidad: Suelo mínimo incondicional de ingresos vitales.",
        "Duración: Indefinida mientras persista la necesidad.",
        "Cuantía: Diferencial hasta renta garantizada (~8.800 €/año)."
    ], CORAL)
]

x_pos = Inches(0.8)
for c_tag, c_tit, c_items, c_col in cols_s7:
    add_card(s7, x_pos, Inches(1.45), Inches(3.75), Inches(5.3), MENTA, BORDE_MENTA)
    
    # Tag
    tb_t = s7.shapes.add_textbox(x_pos + Inches(0.15), Inches(1.6), Inches(3.45), Inches(0.4))
    p_t = tb_t.text_frame.paragraphs[0]
    p_t.text = c_tag
    p_t.font.name = "Outfit"
    p_t.font.size = Pt(11)
    p_t.font.bold = True
    p_t.font.color.rgb = c_col
    
    # Tit
    tb_tit = s7.shapes.add_textbox(x_pos + Inches(0.15), Inches(1.95), Inches(3.45), Inches(0.6))
    p_h = tb_tit.text_frame.paragraphs[0]
    p_h.text = c_tit
    p_h.font.name = "Outfit"
    p_h.font.size = Pt(13)
    p_h.font.bold = True
    p_h.font.color.rgb = PINO
    
    # Bullet text
    tb_b = s7.shapes.add_textbox(x_pos + Inches(0.15), Inches(2.6), Inches(3.45), Inches(4.0))
    tf_b = tb_b.text_frame
    tf_b.word_wrap = True
    for idx, item in enumerate(c_items):
        p_it = tf_b.paragraphs[0] if idx == 0 else tf_b.add_paragraph()
        p_it.font.name = "Calibri"
        p_it.font.size = Pt(12)
        p_it.space_before = Pt(8)
        p_it.text = "• " + item
        p_it.font.color.rgb = TINTA
        
    x_pos += Inches(3.99)

# ==============================================================================
# SLIDE 8: FASE 2 · DE LAS RMI AUTONÓMICAS A LA LEY 19/2021
# ==============================================================================
s8 = prs.slides.add_slide(blank_layout)
set_slide_background(s8, BLANCO)
add_header(s8, "Fase 2 (20–45 min) · Evolución Institucional", "De la Fragmentación Autonómica (1988–2020) al Suelo Común del IMV", 9)

add_card(s8, Inches(0.8), Inches(1.45), Inches(5.7), Inches(5.3), MENTA, BORDE_MENTA)
tb_s8_1 = s8.shapes.add_textbox(Inches(1.05), Inches(1.65), Inches(5.2), Inches(4.9))
tf_s8_1 = tb_s8_1.text_frame
tf_s8_1.word_wrap = True

p_s8_1 = tf_s8_1.paragraphs[0]
p_s8_1.text = "El Modelo Previo: 17 Rentas Mínimas Autonómicas"
p_s8_1.font.name = "Outfit"
p_s8_1.font.size = Pt(15)
p_s8_1.font.bold = True
p_s8_1.font.color.rgb = PINO

bullets_s8_1 = [
    "Surgidas a finales de los 80 como competencia exclusiva autonómica.",
    "Inequidad territorial extrema: el País Vasco (RGI) cubría a más del 60% de sus hogares pobres, mientras Andalucía, Madrid o Murcia no llegaban al 15%.",
    "Gasto condicionado a disponibilidad presupuestaria regional anual, provocando listas de espera y suspensiones de pagos.",
    "Barreras proteccionistas: exigencias de empadronamiento autonómico de hasta 3 y 5 años para frenar el supuesto 'turismo de rentas'."
]
for b in bullets_s8_1:
    p = tf_s8_1.add_paragraph()
    p.font.name = "Calibri"
    p.font.size = Pt(12.5)
    p.space_before = Pt(8)
    p.text = "• " + b
    p.font.color.rgb = TINTA

add_card(s8, Inches(6.8), Inches(1.45), Inches(5.733), Inches(5.3), MENTA, BORDE_MENTA)
tb_s8_2 = s8.shapes.add_textbox(Inches(7.05), Inches(1.65), Inches(5.2), Inches(4.9))
tf_s8_2 = tb_s8_2.text_frame
tf_s8_2.word_wrap = True

p_s8_2 = tf_s8_2.paragraphs[0]
p_s8_2.text = "El Suelo Común Estatal: RDL 20/2020 y Ley 19/2021"
p_s8_2.font.name = "Outfit"
p_s8_2.font.size = Pt(15)
p_s8_2.font.bold = True
p_s8_2.font.color.rgb = PINO

bullets_s8_2 = [
    "Aprobado en plena pandemia de Covid-19 como derecho subjetivo de la Seguridad Social financiado vía tributación general.",
    "Fija un suelo común estatal obligatorio para todos los ciudadanos independientemente de la comunidad donde residan.",
    "Las Rentas Mínimas Autonómicas no desaparecen: pasan a actuar como complementos de cuantía o para colectivos no cubiertos por el IMV.",
    "Problema residual: colapso inicial en el INSS y transferencia pendiente de la gestión a las autonomías (País Vasco y Navarra asumieron la gestión íntegra)."
]
for b in bullets_s8_2:
    p = tf_s8_2.add_paragraph()
    p.font.name = "Calibri"
    p.font.size = Pt(12.5)
    p.space_before = Pt(8)
    p.text = "• " + b
    p.font.color.rgb = TINTA

# ==============================================================================
# SLIDE 9: FASE 2 · DISEÑO DEL IMV Y CUANTÍAS 2026
# ==============================================================================
s9 = prs.slides.add_slide(blank_layout)
set_slide_background(s9, BLANCO)
add_header(s9, "Fase 2 (20–45 min) · Parámetros Legales del Sistema", "La Arquitectura de la Prestación: Renta Diferencial y Cuantías 2026", 10)

# Fórmula de la prestación diferencial
shape_f = add_card(s9, Inches(0.8), Inches(1.45), Inches(11.733), Inches(1.15), MENTA, BORDE_MENTA)
tb_f = s9.shapes.add_textbox(Inches(1.0), Inches(1.5), Inches(11.3), Inches(1.0))
tf_f = tb_f.text_frame
tf_f.word_wrap = True
p_f = tf_f.paragraphs[0]
p_f.alignment = PP_ALIGN.CENTER
p_f.text = "Fórmula Legal de la Prestación Diferencial (Art. 13 Ley 19/2021)"
p_f.font.name = "Outfit"
p_f.font.size = Pt(13)
p_f.font.bold = True
p_f.font.color.rgb = PINO

p_f_eq = tf_f.add_paragraph()
p_f_eq.alignment = PP_ALIGN.CENTER
p_f_eq.font.name = "Calibri"
p_f_eq.font.size = Pt(16)
p_f_eq.font.bold = True
p_f_eq.space_before = Pt(4)
r_eq1 = p_f_eq.add_run()
r_eq1.text = "Cuantía Mensual IMV = "
r_eq1.font.color.rgb = PINO
r_eq2 = p_f_eq.add_run()
r_eq2.text = "Renta Garantizada Hogar"
r_eq2.font.color.rgb = CORAL
r_eq3 = p_f_eq.add_run()
r_eq3.text = " − "
r_eq4 = p_f_eq.add_run()
r_eq4.text = "Ingresos Computables del Hogar"
r_eq4.font.color.rgb = SALVIA

# Dos tarjetas comparativas
add_card(s9, Inches(0.8), Inches(2.8), Inches(5.7), Inches(3.95), BLANCO, BORDE_MENTA)
tb_s9_1 = s9.shapes.add_textbox(Inches(1.05), Inches(2.95), Inches(5.2), Inches(3.6))
tf_s9_1 = tb_s9_1.text_frame
tf_s9_1.word_wrap = True
p_s9_1 = tf_s9_1.paragraphs[0]
p_s9_1.text = "1. Escalas de Convivencia y Renta Garantizada (2026)"
p_s9_1.font.name = "Outfit"
p_s9_1.font.size = Pt(14)
p_s9_1.font.bold = True
p_s9_1.font.color.rgb = PINO

cuantias_2026 = [
    "Adulto Solo (1 miembro): ~8.800 €/año (~734 €/mes).",
    "Escala de Equivalencia: cada adulto adicional suma un 30% hasta un tope del 220% de la renta individual (~1.615 €/mes).",
    "Familias Monoparentales: plus adicional del 22% sobre la cuantía base.",
    "Test de Medios: ingresos y patrimonio neto (excluida vivienda habitual hasta umbral tasado) del ejercicio fiscal previo."
]
for c in cuantias_2026:
    p = tf_s9_1.add_paragraph()
    p.font.name = "Calibri"
    p.font.size = Pt(12)
    p.space_before = Pt(6)
    p.text = "• " + c
    p.font.color.rgb = TINTA

add_card(s9, Inches(6.8), Inches(2.8), Inches(5.733), Inches(3.95), BLANCO, BORDE_CORAL, Pt(1.5))
tb_s9_2 = s9.shapes.add_textbox(Inches(7.05), Inches(2.95), Inches(5.2), Inches(3.6))
tf_s9_2 = tb_s9_2.text_frame
tf_s9_2.word_wrap = True
p_s9_2 = tf_s9_2.paragraphs[0]
p_s9_2.text = "2. Complemento de Ayuda para la Infancia (CAPI)"
p_s9_2.font.name = "Outfit"
p_s9_2.font.size = Pt(14)
p_s9_2.font.bold = True
p_s9_2.font.color.rgb = CORAL

capi_info = [
    "Creado por la Ley 19/2021 para atajar la severa pobreza infantil.",
    "Cuantías mensuales por menor según grupo de edad:\n  - Menores de 3 años: 115 €/mes por hijo.\n  - De 3 a 6 años: 80,50 €/mes por hijo.\n  - De 6 a 18 años: 57,50 €/mes por hijo.",
    "Umbral ampliado: pueden percibirlo hogares que superen el límite del IMV hasta en un 300% de la renta garantizada.",
    "¡Paradoja extrema!: El 72% de hogares pobres con derecho no lo cobra por desconocimiento y falta de automatización."
]
for c in capi_info:
    p = tf_s9_2.add_paragraph()
    p.font.name = "Calibri"
    p.font.size = Pt(12)
    p.space_before = Pt(6)
    p.text = "• " + c
    p.font.color.rgb = TINTA

# ==============================================================================
# SLIDE 10: FASE 2 · LA BRECHA DEL NON-TAKE-UP (BARRERAS)
# ==============================================================================
s10 = prs.slides.add_slide(blank_layout)
set_slide_background(s10, BLANCO)
add_header(s10, "Fase 2 (20–45 min) · La Paradoja de la Exclusión Administrativa", "La Brecha de Cobertura y Non-Take-Up: 55% en IMV y 72% en CAPI (AIReF)", 11)

barreras = [
    ("Traba Probatoria del Padrón y Convivencia", "El 68% de las denegaciones del INSS se deben a la imposibilidad de certificar documentalmente la 'unidad de convivencia' o carecer de empadronamiento histórico ininterrumpido (mínimo 1-2 años). Castiga a quienes viven en habitaciones subarrendadas o pisos compartidos.", CORAL),
    ("Brecha Digital y Complejidad Administrativa", "El diseño de solicitud telemática exige certificado digital, Cl@ve o firma biométrica avanzada. Familias en exclusión severa carecen de equipos, competencias digitales o conexión a internet, dependiendo de redes asistenciales colapsadas.", SALVIA),
    ("El Pánico a los Cobros Indebidos Retroactivos", "Al revisar los ingresos a año vencido con los datos del IRPF, la Seguridad Social detecta desfases temporales y exige devolver miles de euros cobrados de buena fe. Dos de cada tres beneficiarios sufrieron modificaciones y muchos renuncian por terror financiero.", PINO)
]

y_b = Inches(1.45)
for b_tit, b_txt, b_col in barreras:
    add_card(s10, Inches(0.8), y_b, Inches(11.733), Inches(1.65), MENTA, BORDE_MENTA)
    
    # Marcador
    m_box = s10.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), y_b, Inches(0.2), Inches(1.65))
    m_box.fill.solid()
    m_box.fill.fore_color.rgb = b_col
    m_box.line.fill.background()
    
    tb = s10.shapes.add_textbox(Inches(1.2), y_b + Inches(0.12), Inches(11.0), Inches(1.4))
    tf = tb.text_frame
    tf.word_wrap = True
    
    p1 = tf.paragraphs[0]
    p1.text = b_tit
    p1.font.name = "Outfit"
    p1.font.size = Pt(15)
    p1.font.bold = True
    p1.font.color.rgb = b_col
    
    p2 = tf.add_paragraph()
    p2.text = b_txt
    p2.font.name = "Calibri"
    p2.font.size = Pt(13)
    p2.space_before = Pt(6)
    p2.font.color.rgb = TINTA
    
    y_b += Inches(1.8)

# ==============================================================================
# SLIDE 11: FASE 3 · MINI-LECCIÓN II (EL CONCEPTO DE EMTR)
# ==============================================================================
s11 = prs.slides.add_slide(blank_layout)
set_slide_background(s11, BLANCO)
add_header(s11, "Fase 3 (45–70 min) · Mini-Lección Quirúrgica II (Análisis Analítico)", "El Tipo Marginal Efectivo sobre el Trabajo (EMTR) y el Salario de Reserva", 12)

add_card(s11, Inches(0.8), Inches(1.45), Inches(11.733), Inches(1.4), MENTA, BORDE_MENTA)
tb_emtr = s11.shapes.add_textbox(Inches(1.0), Inches(1.55), Inches(11.3), Inches(1.2))
tf_emtr = tb_emtr.text_frame
tf_emtr.word_wrap = True

p_emtr_h = tf_emtr.paragraphs[0]
p_emtr_h.text = "Definición Formal del Tipo Marginal Efectivo sobre el Trabajo (EMTR)"
p_emtr_h.font.name = "Outfit"
p_emtr_h.font.size = Pt(14)
p_emtr_h.font.bold = True
p_emtr_h.font.color.rgb = PINO

p_emtr_f = tf_emtr.add_paragraph()
p_emtr_f.font.name = "Calibri"
p_emtr_f.font.size = Pt(16)
p_emtr_f.font.bold = True
p_emtr_f.space_before = Pt(6)
r_f1 = p_emtr_f.add_run()
r_f1.text = "EMTR = 1 − "
r_f1.font.color.rgb = PINO
r_f2 = p_emtr_f.add_run()
r_f2.text = "(Δ Renta Disponible del Hogar / Δ Salario Bruto de Mercado)"
r_f2.font.color.rgb = CORAL

# Tarjetas comparativas de interpretación con tres ejemplos numéricos detallados
emtr_cases = [
    {
        "tit": "EMTR = 0%",
        "sub": "Incentivo Pleno (Exención al Empleo)",
        "col": SALVIA,
        "desc": "Cada euro ganado incrementa íntegramente la renta del hogar. Trabajar aporta máxima liquidez.",
        "ejemplo_tit": "EJEMPLO 1 · Exención 100% (RD 240/2026)",
        "lineas": [
            ("Situación inicial:", "Hogar percibe 650 €/mes de IMV."),
            ("Salario nuevo ganado:", "ΔYbruto = +400 €/mes."),
            ("Retirada de IMV:", "0 € (exención total del tramo inicial)."),
            ("Renta disponible final:", "650 € + 400 € = 1.050 € (ΔYdisp = +400 €)."),
            ("Cálculo formal:", "EMTR = 1 − (400 / 400) = 1 − 1 = 0%."),
            ("Veredicto alumno:", "El hogar retiene el 100% de lo ganado. ¡Incentivo laboral pleno!")
        ]
    },
    {
        "tit": "EMTR = 100%",
        "sub": "Trampa Clásica (Renta Diferencial)",
        "col": CORAL,
        "desc": "La ayuda se recorta euro a euro con el salario. Trabajar no aporta ni un solo céntimo adicional.",
        "ejemplo_tit": "EJEMPLO 2 · Deducción 1€ por 1€ ganado",
        "lineas": [
            ("Situación inicial:", "Hogar percibe 650 €/mes de IMV."),
            ("Salario nuevo ganado:", "ΔYbruto = +400 €/mes."),
            ("Retirada de IMV:", "−400 € (el IMV baja a 250 €/mes)."),
            ("Renta disponible final:", "250 € + 400 € = 650 € (ΔYdisp = 0 €)."),
            ("Cálculo formal:", "EMTR = 1 − (0 / 400) = 1 − 0 = 100%."),
            ("Veredicto alumno:", "Trabaja 20 h/semana por 0 € netos. Con transporte (−50 €), ¡pierde dinero!")
        ]
    },
    {
        "tit": "EMTR > 100%",
        "sub": "Trampa Agravada (Acantilado Social)",
        "col": PINO_DARK,
        "desc": "La pérdida de ayudas concurrentes supera al salario. ¡Aceptar el empleo empobrece a la familia!",
        "ejemplo_tit": "EJEMPLO 3 · Concurrencia de Subsidios",
        "lineas": [
            ("Situación inicial:", "IMV (650 €) + Bono luz (50 €) + Beca comedor (120 €) = 820 €."),
            ("Salario nuevo ganado:", "ΔYbruto = +400 €/mes."),
            ("Pérdidas acumuladas:", "IMV (−400 €) + Pérdida Bono luz (−50 €) + Beca (−120 €)."),
            ("Renta disponible final:", "250 € + 400 € = 650 € (ΔYdisp = −170 €)."),
            ("Cálculo formal:", "EMTR = 1 − (−170 / 400) = 1 − (−0,425) = 142,5%."),
            ("Veredicto alumno:", "Aceptar el empleo destruye 170 €/mes de liquidez. ¡Trampa confiscatoria!")
        ]
    }
]

# Ajuste ergonómico de dimensiones para que quepa holgado y legible
x_c = Inches(0.8)
for case in emtr_cases:
    # Tarjeta base
    add_card(s11, x_c, Inches(2.95), Inches(3.75), Inches(4.00), BLANCO, BORDE_MENTA)
    
    tb = s11.shapes.add_textbox(x_c + Inches(0.12), Inches(3.02), Inches(3.51), Inches(3.85))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.margin_left = Inches(0.05)
    tf.margin_right = Inches(0.05)
    tf.margin_top = Inches(0.05)
    tf.margin_bottom = Inches(0.05)
    
    # Titular EMTR
    p1 = tf.paragraphs[0]
    p1.text = case["tit"]
    p1.font.name = "Outfit"
    p1.font.size = Pt(16)
    p1.font.bold = True
    p1.font.color.rgb = case["col"]
    
    # Subtítulo conceptual
    p2 = tf.add_paragraph()
    p2.text = case["sub"]
    p2.font.name = "Outfit"
    p2.font.size = Pt(11)
    p2.font.bold = True
    p2.font.color.rgb = PINO
    p2.space_before = Pt(2)
    
    # Descripción
    p3 = tf.add_paragraph()
    p3.text = case["desc"]
    p3.font.name = "Calibri"
    p3.font.size = Pt(10)
    p3.font.color.rgb = TINTA
    p3.space_before = Pt(3)
    
    # Header del ejemplo numérico
    p_ej = tf.add_paragraph()
    p_ej.text = "▸ " + case["ejemplo_tit"]
    p_ej.font.name = "Outfit"
    p_ej.font.size = Pt(10.5)
    p_ej.font.bold = True
    p_ej.font.color.rgb = case["col"]
    p_ej.space_before = Pt(6)
    
    # Líneas del ejemplo numérico
    for etiqueta, detalle in case["lineas"]:
        p_l = tf.add_paragraph()
        p_l.font.name = "Calibri"
        p_l.font.size = Pt(9.5)
        p_l.space_before = Pt(1.5)
        
        r1 = p_l.add_run()
        r1.text = "• " + etiqueta + " "
        r1.font.bold = True
        r1.font.color.rgb = PINO
        
        r2 = p_l.add_run()
        r2.text = detalle
        if "EMTR =" in detalle or "Veredicto" in etiqueta:
            r2.font.bold = True
            if "142,5%" in detalle or "pierde dinero" in detalle or "confiscatoria" in detalle:
                r2.font.color.rgb = CORAL
            elif "0%" in detalle or "Incentivo" in detalle:
                r2.font.color.rgb = SALVIA
            else:
                r2.font.color.rgb = TINTA
        else:
            r2.font.color.rgb = TINTA
            
    x_c += Inches(3.99)

# ==============================================================================
# SLIDE 12: FASE 3 · LA TRAMPA DE LA POBREZA (FIGURA 3.4)
# ==============================================================================
s12 = prs.slides.add_slide(blank_layout)
set_slide_background(s12, BLANCO)
add_header(s12, "Fase 3 (45–70 min) · Análisis Microeconómico de Restricción Presupuestaria", "Figura 3.4 · Guía Analítica: Restricción Presupuestaria y Tipos Marginales (EMTR)", 13)

# Imagen gráfica enriquecida con callouts explicativos
if os.path.exists(FIG_3_4):
    s12.shapes.add_picture(FIG_3_4, Inches(0.8), Inches(1.30), width=Inches(11.733), height=Inches(3.85))

# 3 Tarjetas inferiores de Guía de Lectura para el Profesor y el Alumnado
guia_figura = [
    {
        "tit": "1. ¿Por qué el tramo coral es plano?",
        "sub": "Trampa del 100% (Renta Diferencial)",
        "col": CORAL,
        "bg": RGBColor(255, 245, 242),
        "borde": CORAL,
        "texto": "Si la curva es horizontal (pendiente 0), cada 1 € ganado en el empleo se recorta del IMV. El hogar cobra clavados 8.800 € trabaje 0 o 25 h/semana. ¡Ganancia líquida por trabajar = 0 €!"
    },
    {
        "tit": "2. ¿Por qué la curva verde sube?",
        "sub": "Incentivo al Empleo (RD 240/2026)",
        "col": PINO,
        "bg": MENTA,
        "borde": PINO,
        "texto": "Al eximir los primeros 6.000 € anuales de salario (EMTR = 0%), la curva tiene pendiente positiva. La familia suma su salario al IMV íntegro (alcanza 14.800 €). ¡Trabajar sí compensa!"
    },
    {
        "tit": "3. Clave Analítica para RRLL",
        "sub": "Pendiente = Incentivo al Trabajo",
        "col": SALVIA,
        "bg": BLANCO,
        "borde": BORDE_MENTA,
        "texto": "La inclinación de la curva mide el salario de reserva efectivo. Si la curva es plana, los gastos de transporte y conciliación hacen que trabajar cueste dinero y genere inactividad forzada."
    }
]

x_g = Inches(0.8)
for g in guia_figura:
    add_card(s12, x_g, Inches(5.25), Inches(3.75), Inches(1.60), g["bg"], g["borde"])
    tb_g = s12.shapes.add_textbox(x_g + Inches(0.12), Inches(5.30), Inches(3.51), Inches(1.50))
    tf_g = tb_g.text_frame
    tf_g.word_wrap = True
    tf_g.margin_left = Inches(0.04)
    tf_g.margin_right = Inches(0.04)
    tf_g.margin_top = Inches(0.04)
    tf_g.margin_bottom = Inches(0.04)
    
    p1 = tf_g.paragraphs[0]
    p1.text = g["tit"]
    p1.font.name = "Outfit"
    p1.font.size = Pt(11)
    p1.font.bold = True
    p1.font.color.rgb = g["col"]
    
    p2 = tf_g.add_paragraph()
    p2.text = g["sub"]
    p2.font.name = "Outfit"
    p2.font.size = Pt(9.5)
    p2.font.bold = True
    p2.font.color.rgb = PINO
    p2.space_before = Pt(1.5)
    
    p3 = tf_g.add_paragraph()
    p3.text = g["texto"]
    p3.font.name = "Calibri"
    p3.font.size = Pt(9.5)
    p3.font.color.rgb = TINTA
    p3.space_before = Pt(3)
    
    x_g += Inches(3.99)

# ==============================================================================
# SLIDE 13: FASE 3 · LA TRAMPA AGRAVADA (EMTR > 100%)
# ==============================================================================
s13 = prs.slides.add_slide(blank_layout)
set_slide_background(s13, BLANCO)
add_header(s13, "Fase 3 (45–70 min) · Concurrencia de Ayudas y Pérdida en Cascada", "La Trampa Agravada: Cuando el Tipo Marginal Supera el 100% (EMTR > 100%)", 14)

add_card(s13, Inches(0.8), Inches(1.45), Inches(6.8), Inches(5.3), MENTA, BORDE_MENTA)
tb_s13 = s13.shapes.add_textbox(Inches(1.05), Inches(1.65), Inches(6.3), Inches(4.9))
tf_s13 = tb_s13.text_frame
tf_s13.word_wrap = True

p_s13_h = tf_s13.paragraphs[0]
p_s13_h.text = "La Realidad de la Concurrencia (51% de Hogares)"
p_s13_h.font.name = "Outfit"
p_s13_h.font.size = Pt(15)
p_s13_h.font.bold = True
p_s13_h.font.color.rgb = PINO

p_s13_b = tf_s13.add_paragraph()
p_s13_b.font.name = "Calibri"
p_s13_b.font.size = Pt(13)
p_s13_b.space_before = Pt(8)
p_s13_b.text = "El 51% de los hogares que perciben el IMV tiene reconocida al menos otra ayuda pública condicionada a renta:\n\n1. Bono Social Eléctrico y Térmico (descuento del 40% al 80% en factura de luz y gas, valorado en unos 75–90 €/mes).\n2. Beca Municipal de Comedor Escolar (valorada en unos 120–140 €/mes por hijo).\n3. Tarjetas Sociales de Transporte y Ayuda de Emergencia Habitacional.\n\nEl Efecto Acantilado (Cliff Effect):\nAl aceptar un contrato de 600 €/mes, la familia supera el umbral de extrema vulnerabilidad. Pierde simultáneamente el subsidio y las ayudas en especie. ¡El saldo neto empeora en más de 200 € al mes!"
p_s13_b.font.color.rgb = TINTA

# Tarjeta ejemplo numérico
add_card(s13, Inches(7.85), Inches(1.45), Inches(4.68), Inches(5.3), BLANCO, BORDE_CORAL, Pt(1.5))
tb_s13_ex = s13.shapes.add_textbox(Inches(8.1), Inches(1.65), Inches(4.2), Inches(4.9))
tf_s13_ex = tb_s13_ex.text_frame
tf_s13_ex.word_wrap = True

p_ex_h = tf_s13_ex.paragraphs[0]
p_ex_h.text = "Simulación Numérica Real"
p_ex_h.font.name = "Outfit"
p_ex_h.font.size = Pt(15)
p_ex_h.font.bold = True
p_ex_h.font.color.rgb = CORAL

p_ex_b = tf_s13_ex.add_paragraph()
p_ex_b.font.name = "Calibri"
p_ex_b.font.size = Pt(12.5)
p_ex_b.space_before = Pt(8)
p_ex_b.text = "Situación A (Inactividad):\n• IMV Hogar: 1.100 €\n• Bono Eléctrico: 80 €\n• Beca Comedor: 140 €\n→ Total Disponible: 1.320 €/mes\n\nSituación B (Acepta Empleo 600 €):\n• Salario Bruto: +600 €\n• IMV recortado: 500 €\n• Bono Eléctrico: 0 € (perdido)\n• Beca Comedor: 0 € (perdida)\n→ Total Disponible: 1.100 €/mes\n\nCálculo del EMTR:\nEMTR = 1 − (-220 / 600) = 136,7%\n\n¡Trabajar le cuesta 220 €/mes a la familia!"
p_ex_b.font.color.rgb = TINTA

# ==============================================================================
# SLIDE 14: FASE 3 · EVIDENCIA EMPÍRICA AIREF (-3 PP)
# ==============================================================================
s14 = prs.slides.add_slide(blank_layout)
set_slide_background(s14, BLANCO)
add_header(s14, "Fase 3 (45–70 min) · Evidencia Causal y Evaluación Empírica", "La Evidencia de la AIReF: El Impacto de -3 pp (-12%) en Participación Laboral", 15)

add_card(s14, Inches(0.8), Inches(1.45), Inches(5.7), Inches(5.3), MENTA, BORDE_MENTA)
tb_s14_1 = s14.shapes.add_textbox(Inches(1.05), Inches(1.65), Inches(5.2), Inches(4.9))
tf_s14_1 = tb_s14_1.text_frame
tf_s14_1.word_wrap = True

p_s14_h = tf_s14_1.paragraphs[0]
p_s14_h.text = "El Hallazgo Econométrico de la AIReF"
p_s14_h.font.name = "Outfit"
p_s14_h.font.size = Pt(15)
p_s14_h.font.bold = True
p_s14_h.font.color.rgb = PINO

p_s14_b = tf_s14_1.add_paragraph()
p_s14_b.font.name = "Calibri"
p_s14_b.font.size = Pt(13)
p_s14_b.space_before = Pt(8)
p_s14_b.text = "La AIReF comparó a hogares beneficiarios con hogares de perfil socioeconómico idéntico situados justo por encima del umbral de renta (diseño de regresión discontinua y emparejamiento):\n\n• Resultado: Percibir el IMV reduce en 3 puntos porcentuales la probabilidad de trabajar entre los adultos en edad laboral.\n• En términos relativos, supone una caída del 12% en la tasa de participación laboral de este colectivo.\n• ¿Refleja este dato una preferencia intrínseca por la holgazanería o un mal diseño de la ayuda?\n• Conclusión de la AIReF: Es contabilidad familiar racional provocada por el tipo marginal efectivo confiscatorio."
p_s14_b.font.color.rgb = TINTA

add_card(s14, Inches(6.8), Inches(1.45), Inches(5.733), Inches(5.3), MENTA, BORDE_MENTA)
tb_s14_2 = s14.shapes.add_textbox(Inches(7.05), Inches(1.65), Inches(5.2), Inches(4.9))
tf_s14_2 = tb_s14_2.text_frame
tf_s14_2.word_wrap = True

p_s14_h2 = tf_s14_2.paragraphs[0]
p_s14_h2.text = "Literatura Internacional de Referencia"
p_s14_h2.font.name = "Outfit"
p_s14_h2.font.size = Pt(15)
p_s14_h2.font.bold = True
p_s14_h2.font.color.rgb = PINO

p_s14_b2 = tf_s14_2.add_paragraph()
p_s14_b2.font.name = "Calibri"
p_s14_b2.font.size = Pt(13)
p_s14_b2.space_before = Pt(8)
p_s14_b2.text = "La evidencia de la economía laboral en otros países avala esta conclusión:\n\n• Estados Unidos (Earned Income Tax Credit · EITC): Cuando el subsidio premia el empleo sumando renta por cada dólar ganado (subsidio salarial), la participación laboral femenina con hijos aumentó entre 2 y 4 puntos porcentuales.\n• Francia (RSA · Revenu de Solidarité Active): La sustitución del RMI diferencial por un modelo con complemento salarial permanente redujo la inactividad en un 8%.\n• Reino Unido (Universal Credit): Unificar las ayudas concurrentes en una ventanilla única eliminó los acantilados donde el EMTR superaba el 100%."
p_s14_b2.font.color.rgb = TINTA

# ==============================================================================
# SLIDE 15: FASE 3 · EL INCENTIVO DEL RD 240/2026 Y SUS LÍMITES
# ==============================================================================
s15 = prs.slides.add_slide(blank_layout)
set_slide_background(s15, BLANCO)
add_header(s15, "Fase 3 (45–70 min) · La Respuesta Normativa Reciente", "El Mecanismo de Incentivos al Empleo del RD 240/2026 y sus Limitaciones", 16)

add_card(s15, Inches(0.8), Inches(1.45), Inches(5.7), Inches(5.3), MENTA, BORDE_MENTA)
tb_s15_1 = s15.shapes.add_textbox(Inches(1.05), Inches(1.65), Inches(5.2), Inches(4.9))
tf_s15_1 = tb_s15_1.text_frame
tf_s15_1.word_wrap = True

p_s15_1 = tf_s15_1.paragraphs[0]
p_s15_1.text = "El Avance Positivo del RD 240/2026"
p_s15_1.font.name = "Outfit"
p_s15_1.font.size = Pt(15)
p_s15_1.font.bold = True
p_s15_1.font.color.rgb = PINO

bullets_s15_1 = [
    "Modifica el cómputo de ingresos del IMV cuando el hogar incrementa sus rentas laborales respecto al año previo.",
    "Tramo exento inicial: los primeros 6.000 € de aumento salarial anual quedan completamente exentos de recorte en el IMV (EMTR = 0%).",
    "Tramo de retiro al 50%: por encima de los 6.000 € y hasta cierto umbral, solo computa la mitad del incremento salarial (EMTR = 50%).",
    "Supone un cambio notable frente a la regla de incompatibilidad diferencial pura del 100%."
]
for b in bullets_s15_1:
    p = tf_s15_1.add_paragraph()
    p.font.name = "Calibri"
    p.font.size = Pt(12.5)
    p.space_before = Pt(8)
    p.text = "• " + b
    p.font.color.rgb = TINTA

add_card(s15, Inches(6.8), Inches(1.45), Inches(5.733), Inches(5.3), BLANCO, BORDE_CORAL, Pt(1.5))
tb_s15_2 = s15.shapes.add_textbox(Inches(7.05), Inches(1.65), Inches(5.2), Inches(4.9))
tf_s15_2 = tb_s15_2.text_frame
tf_s15_2.word_wrap = True

p_s15_2 = tf_s15_2.paragraphs[0]
p_s15_2.text = "Las Limitaciones Críticas (M. Hidalgo, Cinco Días)"
p_s15_2.font.name = "Outfit"
p_s15_2.font.size = Pt(15)
p_s15_2.font.bold = True
p_s15_2.font.color.rgb = CORAL

bullets_s15_2 = [
    "Se calcula sobre el INCREMENTO respecto al año anterior, no sobre el NIVEL permanente de renta.",
    "Carácter transitorio: al cabo de 12 meses, cuando el salario se asimila en la declaración de IRPF, la exención se extingue y el IMV se recorta drásticamente.",
    "Desfase temporal: se liquida con la declaración del IRPF del ejercicio previo (hasta 18 meses de retraso) en lugar de en tiempo real.",
    "Riesgo de devolución: si el trabajador pierde el empleo tras consolidarse la rebaja, tarda meses en recuperar la ayuda completa."
]
for b in bullets_s15_2:
    p = tf_s15_2.add_paragraph()
    p.font.name = "Calibri"
    p.font.size = Pt(12.5)
    p.space_before = Pt(8)
    p.text = "• " + b
    p.font.color.rgb = TINTA

# ==============================================================================
# SLIDE 16: FASE 3 · PROPUESTAS DE REDISEÑO ESTRUCTURAL
# ==============================================================================
s16 = prs.slides.add_slide(blank_layout)
set_slide_background(s16, BLANCO)
add_header(s16, "Fase 3 (45–70 min) · Propuestas de Rediseño de Políticas Públicas", "Hacia un IMV Eficaz: Las Tres Reformas Estructurales Pendientes", 17)

reformas = [
    ("1. Retirada Gradual y Permanente sobre Nivel", "Sustituir la exención transitoria sobre incrementos por una retirada suave y permanente sobre el nivel de renta (Impuesto Negativo / in-work benefit), garantizando que trabajar siempre añada ingresos líquidos de forma indefinida.", PINO),
    ("2. Gestión Proactiva en Tiempo Real (Hacienda + TGSS)", "Invertir la carga de la prueba: la Administración ya conoce en tiempo real los datos de cotizaciones y salarios. Conceder de oficio y regularizar mes a mes en nómina, con reincorporación automática si se pierde el empleo.", SALVIA),
    ("3. Prestación Universal por Menor a Cargo en el IRPF", "Sacar el Complemento de Infancia (CAPI) de la prueba de medios estigmatizante del IMV. Una ayuda por hijo cuasi-universal tramitada por la Agencia Tributaria erradica de golpe el 72% de non-take-up y la pobreza infantil.", CORAL)
]

y_ref = Inches(1.45)
for r_tit, r_txt, r_col in reformas:
    add_card(s16, Inches(0.8), y_ref, Inches(11.733), Inches(1.65), MENTA, BORDE_MENTA)
    
    m_box = s16.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), y_ref, Inches(0.2), Inches(1.65))
    m_box.fill.solid()
    m_box.fill.fore_color.rgb = r_col
    m_box.line.fill.background()
    
    tb = s16.shapes.add_textbox(Inches(1.2), y_ref + Inches(0.12), Inches(11.0), Inches(1.4))
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
    
    y_ref += Inches(1.8)

# ==============================================================================
# SLIDE 17: FASE 4 · LABORATORIO ACTIVO Y COMPETICIÓN DE AULA (20 MIN)
# ==============================================================================
s17 = prs.slides.add_slide(blank_layout)
set_slide_background(s17, BLANCO)
add_header(s17, "Fase 4 (70–90 min · 20 min) · Laboratorio Activo y Competición en Parejas", "Competición de Aula: «El Reto del Ministro de Seguridad Social»", 18)

add_card(s17, Inches(0.8), Inches(1.45), Inches(7.5), Inches(5.3), MENTA, BORDE_MENTA)
tb_s17_m = s17.shapes.add_textbox(Inches(1.05), Inches(1.60), Inches(6.9), Inches(5.0))
tf_s17_m = tb_s17_m.text_frame
tf_s17_m.word_wrap = True

p_m_h = tf_s17_m.paragraphs[0]
p_m_h.text = "🎯 Misión en Parejas: Cuadrar el Triángulo del Estado del Bienestar"
p_m_h.font.name = "Outfit"
p_m_h.font.size = Pt(15)
p_m_h.font.bold = True
p_m_h.font.color.rgb = PINO

p_sub_ch = tf_s17_m.add_paragraph()
p_sub_ch.text = "Tenéis 8 minutos con el móvil para entrar en la Pestaña 3 ('El Dilema del Ministro') y encontrar la reforma que cumpla simultáneamente las 3 metas oficiales:"
p_sub_ch.font.name = "Calibri"
p_sub_ch.font.size = Pt(11.5)
p_sub_ch.space_before = Pt(4)
p_sub_ch.font.color.rgb = TINTA

metas = [
    ("META 1 · Cobertura Social:", " Cubrir al menos el 50% de hogares pobres (hundiendo el non-take-up por debajo del 30%). Requiere derribar trabas de padrón.", SALVIA),
    ("META 2 · Sostenibilidad Fiscal:", " Gasto público ≤ 0,55% del PIB (máx. 7.500 M€). No se puede quebrar el presupuesto del Estado.", PINO),
    ("META 3 · Incentivo al Empleo:", " Reducir el desincentivo laboral a menos de -1,5 pp (acabar con la trampa del 100% mediante retirada gradual continua).", CORAL)
]
for m_tit, m_desc, m_col in metas:
    p = tf_s17_m.add_paragraph()
    p.space_before = Pt(6)
    p.font.name = "Calibri"
    p.font.size = Pt(11.5)
    r1 = p.add_run()
    r1.text = "• " + m_tit
    r1.font.bold = True
    r1.font.color.rgb = m_col
    r2 = p.add_run()
    r2.text = m_desc
    r2.font.color.rgb = TINTA

# Caja de llamada a la acción / Premio
p_win = tf_s17_m.add_paragraph()
p_win.space_before = Pt(10)
p_win.font.name = "Outfit"
p_win.font.size = Pt(11)
p_win.font.bold = True
r_w = p_win.add_run()
r_w.text = "🏆 REGLA DE ORO: ¡La primera pareja que consiga el badge de 'MISIÓN CUMPLIDA' en su pantalla levanta la mano para defender su reforma en clase!"
r_w.font.color.rgb = CORAL

# Preguntas de debate posterior
p_deb = tf_s17_m.add_paragraph()
p_deb.space_before = Pt(6)
p_deb.font.name = "Calibri"
p_deb.font.size = Pt(10.5)
p_deb.font.italic = True
p_deb.font.color.rgb = SALVIA
p_deb.text = "Debate posterior: ¿Por qué gastar 10.000 M€ no sirve si no tocas el padrón? ¿Por qué la retirada gradual salva el empleo?"

# Tarjeta QR de la App
add_card(s17, Inches(8.55), Inches(1.45), Inches(3.98), Inches(5.3), BLANCO, BORDE_CORAL, Pt(1.5))
tb_s17_qr = s17.shapes.add_textbox(Inches(8.75), Inches(1.65), Inches(3.6), Inches(1.0))
tf_s17_qr = tb_s17_qr.text_frame
tf_s17_qr.word_wrap = True

p_qr_app_h = tf_s17_qr.paragraphs[0]
p_qr_app_h.text = "¡Abre la Micro-App!"
p_qr_app_h.alignment = PP_ALIGN.CENTER
p_qr_app_h.font.name = "Outfit"
p_qr_app_h.font.size = Pt(16)
p_qr_app_h.font.bold = True
p_qr_app_h.font.color.rgb = PINO

p_qr_app_sub = tf_s17_qr.add_paragraph()
p_qr_app_sub.text = "Pestaña 3: El Dilema del Ministro"
p_qr_app_sub.alignment = PP_ALIGN.CENTER
p_qr_app_sub.font.name = "Calibri"
p_qr_app_sub.font.size = Pt(11)
p_qr_app_sub.font.bold = True
p_qr_app_sub.font.color.rgb = CORAL

if os.path.exists(QR_APP):
    s17.shapes.add_picture(QR_APP, Inches(9.2), Inches(2.75), width=Inches(2.7), height=Inches(2.7))

tb_s17_url = s17.shapes.add_textbox(Inches(8.75), Inches(5.75), Inches(3.6), Inches(0.8))
p_u = tb_s17_url.text_frame.paragraphs[0]
p_u.alignment = PP_ALIGN.CENTER
p_u.text = "mhidper.github.io/micro_apps/\nsimulador_imv_trampa.html"
p_u.font.name = "Calibri"
p_u.font.size = Pt(10)
p_u.font.bold = True
p_u.font.color.rgb = PINO

# ==============================================================================
# SLIDE 18: FASE 5A · SÍNTESIS Y DEBATE DE AULA
# ==============================================================================
s18 = prs.slides.add_slide(blank_layout)
set_slide_background(s18, BLANCO)
add_header(s18, "Fase 5a (85–95 min) · Síntesis Institucional y Debate de Aula", "Lecciones para un Graduado en Relaciones Laborales y Recursos Humanos", 19)

add_card(s18, Inches(0.8), Inches(1.45), Inches(5.7), Inches(5.3), MENTA, BORDE_MENTA)
tb_s18_1 = s18.shapes.add_textbox(Inches(1.05), Inches(1.65), Inches(5.2), Inches(4.9))
tf_s18_1 = tb_s18_1.text_frame
tf_s18_1.word_wrap = True

p_s18_h1 = tf_s18_1.paragraphs[0]
p_s18_h1.text = "La Racionalidad Económica del Desempleado"
p_s18_h1.font.name = "Outfit"
p_s18_h1.font.size = Pt(15)
p_s18_h1.font.bold = True
p_s18_h1.font.color.rgb = PINO

p_s18_b1 = tf_s18_1.add_paragraph()
p_s18_b1.font.name = "Calibri"
p_s18_b1.font.size = Pt(13)
p_s18_b1.space_before = Pt(8)
p_s18_b1.text = "1. Rechazar un empleo no siempre es holgazanería moral:\nCuando el sistema impone un EMTR cercano o superior al 100%, trabajar destruye renta líquida y bienestar doméstico.\n\n2. Para las empresas y departamentos de RRLL:\nCubrir vacantes de salarios bajos o tiempos parciales exige que la ayuda pública opere como complemento salarial (in-work benefit) y no como castigo de exclusión.\n\n3. La pobreza española precedió a la ayuda:\nEl problema de fondo radica en el subempleo, la temporalidad y salarios que no permiten salir de la pobreza (trabajadores pobres)."
p_s18_b1.font.color.rgb = TINTA

add_card(s18, Inches(6.8), Inches(1.45), Inches(5.733), Inches(5.3), MENTA, BORDE_MENTA)
tb_s18_2 = s18.shapes.add_textbox(Inches(7.05), Inches(1.65), Inches(5.2), Inches(4.9))
tf_s18_2 = tb_s18_2.text_frame
tf_s18_2.word_wrap = True

p_s18_h2 = tf_s18_2.paragraphs[0]
p_s18_h2.text = "El Futuro del Sistema de Garantía de Rentas"
p_s18_h2.font.name = "Outfit"
p_s18_h2.font.size = Pt(15)
p_s18_h2.font.bold = True
p_s18_h2.font.color.rgb = PINO

p_s18_b2 = tf_s18_2.add_paragraph()
p_s18_b2.font.name = "Calibri"
p_s18_b2.font.size = Pt(13)
p_s18_b2.space_before = Pt(8)
p_s18_b2.text = "1. Reemplazar la desconfianza por la proactividad:\nLa Agencia Tributaria y la Seguridad Social disponen de datos cruzados para conceder ayudas de oficio sin obligar a los vulnerables a acreditar lo evidente.\n\n2. Universalizar la protección infantil:\nUn complemento por hijo universal en el IRPF elimina el non-take-up del 72% y el estigma social de las colas de asistencia social.\n\n3. Transición al Reto de Aula (Fase 5b):\nMóviles y ordenadores guardados. Pasamos a la cuartilla oficial manuscrita (10 minutos)."
p_s18_b2.font.color.rgb = TINTA

# ==============================================================================
# SLIDE 19: FASE 5B · RETO MANUSCRITO TURNO MARTES (LÍNEA 1)
# ==============================================================================
s19 = prs.slides.add_slide(blank_layout)
set_slide_background(s19, BLANCO)
add_header(s19, "Fase 5b (95–105 min) · Reto Manuscrito Individual (10 min · Solo Papel)", "Turno Martes · Línea 1 (03 de Noviembre de 2026)", 20)

add_card(s19, Inches(0.8), Inches(1.45), Inches(11.733), Inches(5.3), MENTA, BORDE_MENTA)
tb_s19 = s19.shapes.add_textbox(Inches(1.1), Inches(1.65), Inches(11.1), Inches(4.9))
tf_s19 = tb_s19.text_frame
tf_s19.word_wrap = True

p_r1 = tf_s19.paragraphs[0]
p_r1.text = "RETO DE EVALUACIÓN CONTINUA · TURNO MARTES (LÍNEA 1) · 1.000 PTS"
p_r1.font.name = "Outfit"
p_r1.font.size = Pt(16)
p_r1.font.bold = True
p_r1.font.color.rgb = PINO

p_warn1 = tf_s19.add_paragraph()
p_warn1.text = "Entorno libre de pantallas. Redacta a mano en tu cuartilla oficial (máximo 1 cara por alumno):"
p_warn1.font.name = "Calibri"
p_warn1.font.size = Pt(12.5)
p_warn1.font.color.rgb = CORAL
p_warn1.space_before = Pt(4)

p_q1 = tf_s19.add_paragraph()
p_q1.font.name = "Calibri"
p_q1.font.size = Pt(13.5)
p_q1.space_before = Pt(14)
r_q1_t = p_q1.add_run()
r_q1_t.text = "1. (500 pts) La Trampa de la Pobreza y el Tipo Marginal Efectivo (EMTR):\n"
r_q1_t.font.bold = True
r_q1_t.font.color.rgb = PINO
r_q1_d = p_q1.add_run()
r_q1_d.text = "Define con precisión técnica qué es el Tipo Marginal Efectivo sobre el Trabajo (EMTR) y explica por qué el diseño original de una renta mínima diferencial pura (donde la ayuda cubre exactamente la distancia entre los ingresos del hogar y la renta garantizada) genera un EMTR del 100%. ¿Cómo altera esta situación los incentivos para aceptar un empleo a tiempo parcial de un perceptor del IMV y qué solución provisional aportó el RD 240/2026?"
r_q1_d.font.color.rgb = TINTA

p_q2 = tf_s19.add_paragraph()
p_q2.font.name = "Calibri"
p_q2.font.size = Pt(13.5)
p_q2.space_before = Pt(14)
r_q2_t = p_q2.add_run()
r_q2_t.text = "2. (500 pts) Los Tres Estigmas del IMV y la Evidencia Empírica de la AIReF:\n"
r_q2_t.font.bold = True
r_q2_t.font.color.rgb = PINO
r_q2_d = p_q2.add_run()
r_q2_d.text = "En el debate público suelen atribuirse al Ingreso Mínimo Vital tres estigmas: que desincentiva el trabajo porque financia la inactividad voluntaria, que es una ayuda para adultos sin cargas y que padece un fraude generalizado. Apoyándote en los datos oficiales de la AIReF y la Seguridad Social analizados en clase, desmonta razonadamente cada uno de estos tres mitos."
r_q2_d.font.color.rgb = TINTA

# ==============================================================================
# SLIDE 20: FASE 5B · RETO MANUSCRITO TURNO VIERNES (LÍNEA 2)
# ==============================================================================
s20 = prs.slides.add_slide(blank_layout)
set_slide_background(s20, BLANCO)
add_header(s20, "Fase 5b (95–105 min) · Reto Manuscrito Individual (10 min · Solo Papel)", "Turno Viernes · Línea 2 (06 de Noviembre de 2026)", 21)

add_card(s20, Inches(0.8), Inches(1.45), Inches(11.733), Inches(5.3), MENTA, BORDE_MENTA)
tb_s20 = s20.shapes.add_textbox(Inches(1.1), Inches(1.65), Inches(11.1), Inches(4.9))
tf_s20 = tb_s20.text_frame
tf_s20.word_wrap = True

p_r2 = tf_s20.paragraphs[0]
p_r2.text = "RETO DE EVALUACIÓN CONTINUA · TURNO VIERNES (LÍNEA 2) · 1.000 PTS"
p_r2.font.name = "Outfit"
p_r2.font.size = Pt(16)
p_r2.font.bold = True
p_r2.font.color.rgb = PINO

p_warn2 = tf_s20.add_paragraph()
p_warn2.text = "Entorno libre de pantallas. Redacta a mano en tu cuartilla oficial (máximo 1 cara por alumno):"
p_warn2.font.name = "Calibri"
p_warn2.font.size = Pt(12.5)
p_warn2.font.color.rgb = CORAL
p_warn2.space_before = Pt(4)

p_q2_1 = tf_s20.add_paragraph()
p_q2_1.font.name = "Calibri"
p_q2_1.font.size = Pt(13.5)
p_q2_1.space_before = Pt(14)
r_q2_1_t = p_q2_1.add_run()
r_q2_1_t.text = "1. (500 pts) La Trampa del EMTR Acumulado (>100%) y la Retirada Gradual:\n"
r_q2_1_t.font.bold = True
r_q2_1_t.font.color.rgb = PINO
r_q2_1_d = p_q2_1.add_run()
r_q2_1_d.text = "El 51% de los hogares perceptores del IMV recibe al menos otra ayuda pública condicionada a renta (bono social eléctrico/térmico, becas comedor, tarifas reducidas). Explica cómo la interacción entre estas ayudas puede provocar un tipo marginal efectivo acumulado superior al 100% (EMTR > 100%). ¿Por qué los economistas laborales proponen sustituir las exenciones transitorias por una retirada gradual permanente sobre el nivel de renta (Impuesto Negativo / in-work benefit)?"
r_q2_1_d.font.color.rgb = TINTA

p_q2_2 = tf_s20.add_paragraph()
p_q2_2.font.name = "Calibri"
p_q2_2.font.size = Pt(13.5)
p_q2_2.space_before = Pt(14)
r_q2_2_t = p_q2_2.add_run()
r_q2_2_t.text = "2. (500 pts) La Paradoja del Non-Take-Up y el Rediseño de la Protección a la Infancia:\n"
r_q2_2_t.font.bold = True
r_q2_2_t.font.color.rgb = PINO
r_q2_2_d = p_q2_2.add_run()
r_q2_2_d.text = "Según la AIReF, el 55% de los hogares elegibles no solicita el IMV, y el 72% no solicita el Complemento de Ayuda para la Infancia (CAPI). Explica cuáles son las principales barreras administrativas e institucionales que explican esta exclusión masiva y qué ventajas tendría transformar el complemento infantil en una prestación cuasi-universal integrada en el IRPF."
r_q2_2_d.font.color.rgb = TINTA

# ==============================================================================
# SLIDE 21: FASE 5C · SUBIDA FOTOGRÁFICA INSTANTÁNEA (QR FORMS)
# ==============================================================================
s21 = prs.slides.add_slide(blank_layout)
set_slide_background(s21, BLANCO)
add_header(s21, "Fase 5c (105–107 min · 2 min) · Subida Fotográfica Instantánea", "Escanea y Sube la Fotografía de tu Cuartilla a Microsoft Forms", 22)

add_card(s21, Inches(0.8), Inches(1.45), Inches(7.5), Inches(5.3), MENTA, BORDE_MENTA)
tb_s21_t = s21.shapes.add_textbox(Inches(1.1), Inches(1.7), Inches(6.9), Inches(4.8))
tf_s21_t = tb_s21_t.text_frame
tf_s21_t.word_wrap = True

p_s21_h = tf_s21_t.paragraphs[0]
p_s21_h.text = "Instrucciones de Subida (2 minutos exactos):"
p_s21_h.font.name = "Outfit"
p_s21_h.font.size = Pt(16)
p_s21_h.font.bold = True
p_s21_h.font.color.rgb = PINO

steps_s21 = [
    ("Paso 1 · Cámara:", " Desbloquea tu teléfono móvil y abre la cámara fotográfica."),
    ("Paso 2 · Foto Nítida:", " Toma una fotografía cenital nítida y bien iluminada de la cara redactada de tu cuartilla oficial."),
    ("Paso 3 · Subida Forms:", " Escanea el código QR de la derecha o entra en el enlace institucional de Microsoft Forms."),
    ("Paso 4 · Anonimización:", " Tu entrega quedará vinculada a tu cuenta institucional UPO. El sistema anonimiza automáticamente la cuartilla para la evaluación ciega."),
    ("Recompensa:", " Cada entrega válida suma en tu Pasaporte de Evaluación Continua para bonificaciones del examen final (70%).")
]
for s_tit, s_desc in steps_s21:
    p = tf_s21_t.add_paragraph()
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

# QR Box
add_card(s21, Inches(8.55), Inches(1.45), Inches(3.98), Inches(5.3), BLANCO, BORDE_CORAL, Pt(1.5))
tb_s21_qr = s21.shapes.add_textbox(Inches(8.75), Inches(1.65), Inches(3.6), Inches(1.0))
tf_s21_qr = tb_s21_qr.text_frame
tf_s21_qr.word_wrap = True

p_qr_r_h = tf_s21_qr.paragraphs[0]
p_qr_r_h.text = "Subida de Cuartilla"
p_qr_r_h.alignment = PP_ALIGN.CENTER
p_qr_r_h.font.name = "Outfit"
p_qr_r_h.font.size = Pt(16)
p_qr_r_h.font.bold = True
p_qr_r_h.font.color.rgb = PINO

p_qr_r_sub = tf_s21_qr.add_paragraph()
p_qr_r_sub.text = "Microsoft Forms Institucional UPO"
p_qr_r_sub.alignment = PP_ALIGN.CENTER
p_qr_r_sub.font.name = "Calibri"
p_qr_r_sub.font.size = Pt(11)
p_qr_r_sub.font.color.rgb = SALVIA

if os.path.exists(QR_RETO):
    s21.shapes.add_picture(QR_RETO, Inches(9.2), Inches(2.75), width=Inches(2.7), height=Inches(2.7))

tb_s21_url = s21.shapes.add_textbox(Inches(8.75), Inches(5.75), Inches(3.6), Inches(0.8))
p_u_r = tb_s21_url.text_frame.paragraphs[0]
p_u_r.alignment = PP_ALIGN.CENTER
p_u_r.text = "forms.office.com/e/PSLL-Reto-Sesion11\nCierre automático a los 2 minutos"
p_u_r.font.name = "Calibri"
p_u_r.font.size = Pt(9.5)
p_u_r.font.color.rgb = SALVIA

# ==============================================================================
# SLIDE 22: FASE 5D · RÚBRICA Y SOLUCIÓN TURNO MARTES (LÍNEA 1)
# ==============================================================================
s22 = prs.slides.add_slide(blank_layout)
set_slide_background(s22, BLANCO)
add_header(s22, "Fase 5d (107–120 min) · Feedback Formativo Inmediato", "Solución Modelo y Rúbrica Oficial (0–1.000 pts) · Turno Martes (L1)", 23)

add_card(s22, Inches(0.8), Inches(1.45), Inches(5.7), Inches(5.3), MENTA, BORDE_MENTA)
tb_s22_1 = s22.shapes.add_textbox(Inches(1.05), Inches(1.65), Inches(5.2), Inches(4.9))
tf_s22_1 = tb_s22_1.text_frame
tf_s22_1.word_wrap = True

p_sol1_h = tf_s22_1.paragraphs[0]
p_sol1_h.text = "Cuestión 1 · EMTR y Trampa de Pobreza (500 pts)"
p_sol1_h.font.name = "Outfit"
p_sol1_h.font.size = Pt(14)
p_sol1_h.font.bold = True
p_sol1_h.font.color.rgb = PINO

bullets_sol1 = [
    ("Definición EMTR (150 pts):", " Proporción de ingresos brutos perdida por impuestos, cotizaciones y pérdida de ayuda: EMTR = 1 - (Δ Ydisp / Δ Ybruto)."),
    ("Trampa del 100% (200 pts):", " En renta diferencial pura, cada euro ganado reduce 1 euro de ayuda (Δ Ydisp = 0). Trabajar acarrea costes directos (transporte, ropa, guardería) que hacen la ganancia neta negativa."),
    ("Incentivo RD 240/2026 (150 pts):", " Exención de los primeros 6.000 € anuales de aumento y cómputo al 50% de lo restante. Alivia temporalmente la trampa, pero caduca a los 12 meses al consolidarse en el IRPF.")
]
for b_t, b_d in bullets_sol1:
    p = tf_s22_1.add_paragraph()
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

add_card(s22, Inches(6.8), Inches(1.45), Inches(5.733), Inches(5.3), MENTA, BORDE_MENTA)
tb_s22_2 = s22.shapes.add_textbox(Inches(7.05), Inches(1.65), Inches(5.2), Inches(4.9))
tf_s22_2 = tb_s22_2.text_frame
tf_s22_2.word_wrap = True

p_sol2_h = tf_s22_2.paragraphs[0]
p_sol2_h.text = "Cuestión 2 · Refutación de los 3 Estigmas (500 pts)"
p_sol2_h.font.name = "Outfit"
p_sol2_h.font.size = Pt(14)
p_sol2_h.font.bold = True
p_sol2_h.font.color.rgb = PINO

bullets_sol2 = [
    ("Estigma 1: 'Paguita para no trabajar' (175 pts):", " El 66,7% (2 de cada 3) de perceptores ha tenido empleo en el último año. El IMV opera como complemento de salarios bajos y jornadas parciales."),
    ("Estigma 2: 'Adultos sin cargas' (150 pts):", " El 40,2% son menores de edad, el 70% de hogares tienen menores a cargo y el 68,4% de titulares son mujeres (política de infancia encubierta)."),
    ("Estigma 3: 'Fraude masivo' (175 pts):", " El problema real documentado por AIReF es el non-take-up: el 55% de hogares con derecho no lo pide y el 72% no pide el CAPI. El sistema excluye al vulnerable en vez de integrarlo.")
]
for b_t, b_d in bullets_sol2:
    p = tf_s22_2.add_paragraph()
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
# SLIDE 23: FASE 5D · RÚBRICA Y SOLUCIÓN TURNO VIERNES (LÍNEA 2)
# ==============================================================================
s23 = prs.slides.add_slide(blank_layout)
set_slide_background(s23, BLANCO)
add_header(s23, "Fase 5d (107–120 min) · Feedback Formativo Inmediato", "Solución Modelo y Rúbrica Oficial (0–1.000 pts) · Turno Viernes (L2)", 24)

add_card(s23, Inches(0.8), Inches(1.45), Inches(5.7), Inches(5.3), MENTA, BORDE_MENTA)
tb_s23_1 = s23.shapes.add_textbox(Inches(1.05), Inches(1.65), Inches(5.2), Inches(4.9))
tf_s23_1 = tb_s23_1.text_frame
tf_s23_1.word_wrap = True

p_sol3_h = tf_s23_1.paragraphs[0]
p_sol3_h.text = "Cuestión 1 · EMTR Acumulado >100% (500 pts)"
p_sol3_h.font.name = "Outfit"
p_sol3_h.font.size = Pt(14)
p_sol3_h.font.bold = True
p_sol3_h.font.color.rgb = PINO

bullets_sol3 = [
    ("Mecanismo del EMTR > 100% (250 pts):", " El 51% de hogares con IMV cobra ayudas concurrentes (bono social 80 €/m, beca comedor 120 €/m). Al aceptar un empleo que aporta 500 €, superar el umbral de vulnerabilidad provoca la pérdida simultánea de la prestación y de las ayudas en especie. La ganancia bruta es menor que la pérdida de subsidios: el hogar se empobrece trabajando."),
    ("Retirada Gradual Continua (250 pts):", " Retirada suave permanente sobre el nivel de renta (t = 40%, modelo Impuesto Negativo) con datos de TGSS/Hacienda en tiempo real, garantizando que el trabajador retenga siempre un porcentaje significativo de cada euro ganado.")
]
for b_t, b_d in bullets_sol3:
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

p_sol4_h = tf_s23_2.paragraphs[0]
p_sol4_h.text = "Cuestión 2 · Non-Take-Up y Ayuda por Hijo (500 pts)"
p_sol4_h.font.name = "Outfit"
p_sol4_h.font.size = Pt(14)
p_sol4_h.font.bold = True
p_sol4_h.font.color.rgb = PINO

bullets_sol4 = [
    ("Barreras del Non-Take-Up (250 pts):", " El 55% de hogares elegibles no solicita el IMV y el 72% no solicita el CAPI por: a) Trabas de acreditación de unidad de convivencia y padrón histórico (68% de denegaciones); b) Brecha digital de colectivos excluidos; c) Pánico a revisiones retroactivas que exigen devolver miles de euros indebidos."),
    ("Ventajas de la Ayuda Universal (250 pts):", " Transformar el complemento infantil en una prestación por menor cuasi-universal en el IRPF elimina totalmente el non-take-up, erradica el estigma social y recupera el coste en las rentas altas vía IRPF progresivo.")
]
for b_t, b_d in bullets_sol4:
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
# SLIDE 24: CIERRE INSTITUCIONAL Y PASAPORTE DIGITAL
# ==============================================================================
s24 = prs.slides.add_slide(blank_layout)
set_slide_background(s24, BLANCO)
add_header(s24, "Cierre de Sesión y Pasaporte Digital", "Balance del Tema 3 y Pasaporte de Evaluación Continua", 25)

add_card(s24, Inches(0.8), Inches(1.45), Inches(7.5), Inches(5.3), MENTA, BORDE_MENTA)
tb_s24 = s24.shapes.add_textbox(Inches(1.05), Inches(1.65), Inches(6.9), Inches(4.9))
tf_s24 = tb_s24.text_frame
tf_s24.word_wrap = True

p_c_h = tf_s24.paragraphs[0]
p_c_h.text = "Balance del Tema 3: Políticas Pasivas y Garantía de Rentas"
p_c_h.font.name = "Outfit"
p_c_h.font.size = Pt(16)
p_c_h.font.bold = True
p_c_h.font.color.rgb = PINO

concl_items = [
    ("El Trípode Consolidado:", " España cuenta hoy con tres niveles de protección: seguro contributivo, asistencia por desempleo y garantía de rentas vitales."),
    ("El Reto de la Activación:", " Ni la protección por desempleo ni el IMV pueden concebirse como trampas de inactividad: exigen complementos al empleo (CAE e incentivos al IMV) y retirada gradual continua."),
    ("Siguiente Bloque · Tema 4:", " Pasamos de la protección pasiva a la protección activa: Políticas Activas de Empleo (PAE), formación, intermediación laboral y el papel de las ETTs."),
    ("Pasaporte Digital:", " Las calificaciones anonimizadas de esta sesión quedarán publicadas en 48 horas en el Pasaporte de Evaluación Continua.")
]
for c_t, c_d in concl_items:
    p = tf_s24.add_paragraph()
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

# QR Box Pasaporte
add_card(s24, Inches(8.55), Inches(1.45), Inches(3.98), Inches(5.3), BLANCO, BORDE_CORAL, Pt(1.5))
tb_s24_qr = s24.shapes.add_textbox(Inches(8.75), Inches(1.65), Inches(3.6), Inches(1.0))
tf_s24_qr = tb_s24_qr.text_frame
tf_s24_qr.word_wrap = True

p_pas_h = tf_s24_qr.paragraphs[0]
p_pas_h.text = "Pasaporte PSLL"
p_pas_h.alignment = PP_ALIGN.CENTER
p_pas_h.font.name = "Outfit"
p_pas_h.font.size = Pt(16)
p_pas_h.font.bold = True
p_pas_h.font.color.rgb = PINO

p_pas_sub = tf_s24_qr.add_paragraph()
p_pas_sub.text = "Consulta tu saldo de puntos acumulados"
p_pas_sub.alignment = PP_ALIGN.CENTER
p_pas_sub.font.name = "Calibri"
p_pas_sub.font.size = Pt(11)
p_pas_sub.font.color.rgb = SALVIA

if os.path.exists(QR_PASAPORTE):
    s24.shapes.add_picture(QR_PASAPORTE, Inches(9.2), Inches(2.75), width=Inches(2.7), height=Inches(2.7))

tb_s24_url = s24.shapes.add_textbox(Inches(8.75), Inches(5.75), Inches(3.6), Inches(0.8))
p_u_p = tb_s24_url.text_frame.paragraphs[0]
p_u_p.alignment = PP_ALIGN.CENTER
p_u_p.text = "mhidper.github.io/micro_apps/\npasaporte_psll.html"
p_u_p.font.name = "Calibri"
p_u_p.font.size = Pt(10)
p_u_p.font.bold = True
p_u_p.font.color.rgb = PINO

# Guardar la presentación
prs.save(OUTPUT_PPTX)
print("¡Presentación generada con éxito en:", OUTPUT_PPTX)
