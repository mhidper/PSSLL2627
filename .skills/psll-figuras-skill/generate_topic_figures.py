"""
generate_topic_figures.py - Generador centralizado de figuras remasterizadas por tema.
Ejecución: py -3 .skills/psll-figuras-skill/generate_topic_figures.py --tema 1
"""

import os
import sys
import io
import argparse
import numpy as np

try:
    if hasattr(sys.stdout, 'encoding') and sys.stdout.encoding.lower() != 'utf-8':
        if hasattr(sys.stdout, 'buffer'):
            sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
except Exception:
    pass
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Importar paleta y estilos
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
if CURRENT_DIR not in sys.path:
    sys.path.insert(0, CURRENT_DIR)

from brand_figures import PALETTE, setup_academic_style, save_figure

def generate_epa_taxonomy(output_path: str):
    """Genera el esquema metodológico oficial de la EPA en alta resolución con la paleta PSLL."""
    setup_academic_style()
    fig, ax = plt.subplots(figsize=(8.5, 4.6), dpi=300)
    fig.patch.set_facecolor(PALETTE["blanco"])
    ax.set_facecolor(PALETTE["blanco"])
    
    # Coordenadas y dimensiones de cajas
    # Nivel 1: Población de 16 y más años
    box_total = patches.FancyBboxPatch((1.5, 3.2), 5.5, 0.9, boxstyle="round,pad=0.1",
                                       facecolor=PALETTE["menta"], edgecolor=PALETTE["verde_profundo"], linewidth=2.0)
    ax.add_patch(box_total)
    ax.text(4.25, 3.65, "POBLACIÓN EN EDAD DE TRABAJAR (≥ 16 AÑOS)\n(Marco poblacional de referencia de la EPA)",
            ha="center", va="center", fontsize=10.5, fontweight="bold", color=PALETTE["verde_profundo"])
    
    # Nivel 2: Activos e Inactivos
    box_act = patches.FancyBboxPatch((0.4, 1.8), 3.5, 0.8, boxstyle="round,pad=0.08",
                                     facecolor=PALETTE["crema"], edgecolor=PALETTE["salvia"], linewidth=1.8)
    box_inac = patches.FancyBboxPatch((4.6, 1.8), 3.5, 0.8, boxstyle="round,pad=0.08",
                                      facecolor="#F7F9F7", edgecolor=PALETTE["gris_ejes"], linewidth=1.5)
    ax.add_patch(box_act)
    ax.add_patch(box_inac)
    ax.text(2.15, 2.2, "POBLACIÓN ACTIVA\n(Ocupados + Parados que buscan trabajo)",
            ha="center", va="center", fontsize=9.5, fontweight="bold", color=PALETTE["verde_profundo"])
    ax.text(6.35, 2.2, "POBLACIÓN INACTIVA\n(Estudiantes, labores del hogar, jubilados, desanimados)",
            ha="center", va="center", fontsize=8.5, color=PALETTE["verde_tinta"])
    
    # Nivel 3: Ocupados y Parados (dentro de activos)
    box_ocup = patches.FancyBboxPatch((0.2, 0.4), 1.8, 0.8, boxstyle="round,pad=0.08",
                                      facecolor=PALETTE["menta"], edgecolor=PALETTE["salvia"], linewidth=1.5)
    box_par = patches.FancyBboxPatch((2.2, 0.4), 1.8, 0.8, boxstyle="round,pad=0.08",
                                     facecolor="#FDF4F0", edgecolor=PALETTE["coral"], linewidth=1.8)
    ax.add_patch(box_ocup)
    ax.add_patch(box_par)
    ax.text(1.1, 0.8, "OCUPADOS\n(≥ 1 h remunerada\nen ref.)",
            ha="center", va="center", fontsize=8.5, fontweight="bold", color=PALETTE["verde_profundo"])
    ax.text(3.1, 0.8, "PARADOS\n(Sin empleo, búsqueda\nactiva y disponibilidad)",
            ha="center", va="center", fontsize=8.5, fontweight="bold", color=PALETTE["coral"])
    
    # Flechas conectoras
    ax.annotate("", xy=(2.15, 2.65), xytext=(3.0, 3.15),
                arrowprops=dict(arrowstyle="->", color=PALETTE["salvia"], lw=1.8))
    ax.annotate("", xy=(6.35, 2.65), xytext=(5.5, 3.15),
                arrowprops=dict(arrowstyle="->", color=PALETTE["gris_ejes"], lw=1.5))
    ax.annotate("", xy=(1.1, 1.25), xytext=(1.6, 1.75),
                arrowprops=dict(arrowstyle="->", color=PALETTE["salvia"], lw=1.5))
    ax.annotate("", xy=(3.1, 1.25), xytext=(2.6, 1.75),
                arrowprops=dict(arrowstyle="->", color=PALETTE["coral"], lw=1.5))
    
    ax.set_xlim(0, 8.5)
    ax.set_ylim(0.2, 4.4)
    ax.axis("off")
    ax.set_title("Estructura Oficial de la Población según la Encuesta de Población Activa (INE)",
                 fontsize=11.5, fontweight="bold", color=PALETTE["verde_profundo"], pad=10)
    
    save_figure(fig, output_path)

def generate_epa_decision_tree(output_path: str):
    """
    Genera el diagrama de flujo oficial de decisión de la OIT y la EPA:
    - Clasificación en Ocupados, Parados e Inactivos según las preguntas filtro normativas.
    """
    setup_academic_style()
    fig, ax = plt.subplots(figsize=(9.6, 5.2), dpi=300)
    fig.patch.set_facecolor(PALETTE["blanco"])
    ax.set_facecolor(PALETTE["blanco"])
    
    # 1. Entrada: Población en edad de trabajar (16 o más años)
    box_start = patches.FancyBboxPatch((0.2, 2.4), 2.1, 1.2, boxstyle="round,pad=0.08",
                                       facecolor=PALETTE["menta"], edgecolor=PALETTE["verde_profundo"], linewidth=2.0)
    ax.add_patch(box_start)
    ax.text(1.25, 3.15, "POBLACIÓN EN EDAD\nDE TRABAJAR", ha="center", va="center",
            fontsize=9.5, fontweight="bold", color=PALETTE["verde_profundo"])
    ax.text(1.25, 2.65, "(16 o más años)", ha="center", va="center",
            fontsize=8.5, style="italic", color=PALETTE["verde_tinta"])
    
    # Flecha inicial hacia Filtro 1 (horizontal limpia)
    ax.annotate("", xy=(2.85, 3.0), xytext=(2.3, 3.0),
                arrowprops=dict(arrowstyle="->", color=PALETTE["verde_profundo"], lw=2.2))
    
    # 2. Filtro 1 (Empleo): ¿Trabajó al menos 1 hora?
    box_q1 = patches.FancyBboxPatch((2.85, 1.9), 2.5, 2.2, boxstyle="round,pad=0.1",
                                    facecolor=PALETTE["crema"], edgecolor=PALETTE["salvia"], linewidth=1.8)
    ax.add_patch(box_q1)
    ax.text(4.1, 3.75, "FILTRO 1: EMPLEO", ha="center", va="center",
            fontsize=8.5, fontweight="bold", color=PALETTE["salvia"])
    ax.text(4.1, 2.85, "¿Trabajó al menos 1 hora\nremunerada en la semana\nde referencia?",
            ha="center", va="center", fontsize=8.5, fontweight="bold", color=PALETTE["verde_profundo"], linespacing=1.3)
    
    # Rama SÍ de Filtro 1 -> OCUPADOS (sale de la esquina superior derecha x=5.35, y=3.7 hacia x=6.3, y=4.4)
    ax.annotate("", xy=(6.3, 4.4), xytext=(5.35, 3.7),
                arrowprops=dict(arrowstyle="->", color=PALETTE["salvia"], lw=2.2, connectionstyle="arc3,rad=-0.1"))
    # Badge SÍ
    ax.text(5.75, 4.25, "  SÍ  ", ha="center", va="center", fontsize=8.5, fontweight="bold",
            color="white", bbox=dict(boxstyle="round,pad=0.25", facecolor=PALETTE["salvia"], edgecolor="none"))
    
    # Caja OCUPADOS
    box_ocup = patches.FancyBboxPatch((6.3, 3.9), 2.8, 1.0, boxstyle="round,pad=0.08",
                                      facecolor=PALETTE["menta"], edgecolor=PALETTE["verde_profundo"], linewidth=2.0)
    ax.add_patch(box_ocup)
    ax.text(7.7, 4.45, "OCUPADOS", ha="center", va="center",
            fontsize=10.5, fontweight="bold", color=PALETTE["verde_profundo"])
    ax.text(7.7, 4.12, "(Asalariados y trabajadores por cuenta propia)", ha="center", va="center",
            fontsize=7.5, color=PALETTE["verde_tinta"])
    
    # Rama NO de Filtro 1 -> Filtro 2 (sale del borde derecho x=5.35, y=2.55 hacia x=6.1, y=2.55)
    ax.annotate("", xy=(6.1, 2.55), xytext=(5.35, 2.55),
                arrowprops=dict(arrowstyle="->", color=PALETTE["coral"], lw=2.2))
    # Badge NO
    ax.text(5.72, 2.85, "  NO  ", ha="center", va="center", fontsize=8.5, fontweight="bold",
            color="white", bbox=dict(boxstyle="round,pad=0.2", facecolor=PALETTE["coral"], edgecolor="none"))
    
    # 3. Filtro 2 (Doble requisito OIT de Paro)
    box_q2 = patches.FancyBboxPatch((6.1, 1.5), 3.2, 2.1, boxstyle="round,pad=0.1",
                                    facecolor=PALETTE["crema"], edgecolor=PALETTE["salvia"], linewidth=1.8)
    ax.add_patch(box_q2)
    ax.text(7.7, 3.35, "FILTRO 2: PARO (CONCURRENTE)", ha="center", va="center",
            fontsize=8.0, fontweight="bold", color=PALETTE["salvia"])
    ax.text(7.7, 2.85, "1. ¿Búsqueda activa de empleo\nen el mes precedente?",
            ha="center", va="center", fontsize=8.0, fontweight="bold", color=PALETTE["verde_tinta"])
    ax.text(7.7, 2.45, "Y (simultáneamente)", ha="center", va="center",
            fontsize=7.5, fontweight="bold", color=PALETTE["coral"], style="italic")
    ax.text(7.7, 2.05, "2. ¿Disponibilidad inmediata\npara trabajar en < 2 semanas?",
            ha="center", va="center", fontsize=8.0, fontweight="bold", color=PALETTE["verde_tinta"])
    
    # Rama SÍ de Filtro 2 -> PARADOS (sale de la esquina inferior izquierda x=6.1, y=1.7 hacia caja Parados x=5.2, y=1.1)
    ax.annotate("", xy=(5.2, 1.1), xytext=(6.1, 1.7),
                arrowprops=dict(arrowstyle="->", color=PALETTE["coral"], lw=2.2, connectionstyle="arc3,rad=0.08"))
    # Badge SÍ
    ax.text(5.8, 1.55, "  SÍ (Ambos)  ", ha="center", va="center", fontsize=7.5, fontweight="bold",
            color="white", bbox=dict(boxstyle="round,pad=0.25", facecolor=PALETTE["coral"], edgecolor="none"))
    
    # Caja PARADOS
    box_par = patches.FancyBboxPatch((3.4, 0.15), 2.6, 0.95, boxstyle="round,pad=0.08",
                                     facecolor="#FDF4F0", edgecolor=PALETTE["coral"], linewidth=2.0)
    ax.add_patch(box_par)
    ax.text(4.7, 0.72, "PARADOS", ha="center", va="center",
            fontsize=10.5, fontweight="bold", color=PALETTE["coral"])
    ax.text(4.7, 0.38, "(Desempleo genuino según norma OIT)", ha="center", va="center",
            fontsize=7.5, color=PALETTE["verde_tinta"])
    
    # Rama NO de Filtro 2 -> INACTIVOS (flecha vertical directa limpia hacia abajo x=8.0)
    ax.annotate("", xy=(8.0, 1.1), xytext=(8.0, 1.5),
                arrowprops=dict(arrowstyle="->", color=PALETTE["salvia"], lw=2.2))
    # Badge NO
    ax.text(8.0, 1.35, "  NO (Falla alguno)  ", ha="center", va="center", fontsize=7.5, fontweight="bold",
            color="white", bbox=dict(boxstyle="round,pad=0.25", facecolor=PALETTE["salvia"], edgecolor="none"))
    
    # Caja INACTIVOS
    box_inac = patches.FancyBboxPatch((6.7, 0.15), 2.6, 0.95, boxstyle="round,pad=0.08",
                                      facecolor="#F7FAF8", edgecolor=PALETTE["salvia"], linewidth=1.8)
    ax.add_patch(box_inac)
    ax.text(8.0, 0.72, "INACTIVOS", ha="center", va="center",
            fontsize=10.5, fontweight="bold", color=PALETTE["salvia"])
    ax.text(8.0, 0.38, "(Estudiantes, jubilados, desánimo, hogar)", ha="center", va="center",
            fontsize=7.5, color=PALETTE["verde_tinta"])
    
    ax.set_xlim(0, 9.6)
    ax.set_ylim(0.0, 5.2)
    ax.axis("off")
    ax.set_title("Algoritmo Oficial de Clasificación de la Población según la OIT y la EPA",
                 fontsize=12.5, fontweight="bold", color=PALETTE["verde_profundo"], pad=14)
    
    save_figure(fig, output_path)

def generate_beveridge_curve(output_path: str):
    """Genera la Curva de Beveridge teórica oficial en alta resolución."""
    setup_academic_style()
    fig, ax = plt.subplots(figsize=(7.5, 4.8), dpi=300)
    fig.patch.set_facecolor(PALETTE["blanco"])
    ax.set_facecolor(PALETTE["blanco"])
    
    u = np.linspace(3.5, 22.0, 300)
    v1 = 18.0 / (u - 1.5) + 0.3
    v2 = 28.0 / (u - 1.5) + 0.8
    
    ax.plot(u, v1, color=PALETTE["salvia"], linewidth=2.8, label=r'Curva de Beveridge inicial ($BC_1$)')
    ax.plot(u, v2, color=PALETTE["coral"], linewidth=2.8, linestyle="--", label=r'Desplazamiento estructural ($BC_2$ · Desajuste / Histéresis)')
    
    u_A, v_A = 7.5, 18.0 / (7.5 - 1.5) + 0.3
    u_B, v_B = 14.5, 18.0 / (14.5 - 1.5) + 0.3
    u_C, v_C = 14.5, 28.0 / (14.5 - 1.5) + 0.8
    
    ax.scatter([u_A], [v_A], color=PALETTE["verde_profundo"], s=70, zorder=5)
    ax.scatter([u_B], [v_B], color=PALETTE["salvia"], s=70, zorder=5)
    ax.scatter([u_C], [v_C], color=PALETTE["coral"], s=80, zorder=5)
    
    ax.annotate("Punto A\n(Expansión cíclica)", xy=(u_A, v_A), xytext=(u_A - 0.5, v_A + 0.7),
                fontsize=9.5, fontweight="bold", color=PALETTE["verde_profundo"])
    ax.annotate("Punto B\n(Recesión cíclica)", xy=(u_B, v_B), xytext=(u_B - 1.0, v_B + 0.6),
                fontsize=9.5, fontweight="bold", color=PALETTE["salvia"])
    ax.annotate("Punto C\n(Desajuste estructural / PLD)", xy=(u_C, v_C), xytext=(u_C + 0.4, v_C + 0.2),
                fontsize=9.5, fontweight="bold", color=PALETTE["coral"])
    
    ax.annotate("", xy=(u_B - 0.5, v_B + 0.1), xytext=(u_A + 1.0, v_A - 0.5),
                arrowprops=dict(arrowstyle="->", color=PALETTE["salvia"], lw=1.6, connectionstyle="arc3,rad=-0.15"))
    ax.text(9.8, 1.8, "Movimiento cíclico a lo largo\n(Shock de Demanda Agregada)", 
            fontsize=8.5, color=PALETTE["salvia"], style="italic")
    
    ax.annotate("", xy=(u_C, v_C - 0.1), xytext=(u_B, v_B + 0.2),
                arrowprops=dict(arrowstyle="->", color=PALETTE["coral"], lw=1.8, linestyle=":"))
    ax.text(14.8, 2.0, "Desplazamiento hacia fuera\n(Pérdida de eficiencia / Mismatch)", 
            fontsize=8.5, color=PALETTE["coral"], style="italic")
    
    ax.set_xlim(2, 23)
    ax.set_ylim(0, 5.0)
    ax.set_xlabel("Tasa de Desempleo, $u$ (%)", fontsize=11, labelpad=8, fontweight="bold")
    ax.set_ylabel("Tasa de Vacantes, $v$ (%)", fontsize=11, labelpad=8, fontweight="bold")
    ax.set_title("La Curva de Beveridge: Dinámica Cíclica vs. Desajuste Estructural", 
                 fontsize=12.5, fontweight="bold", pad=14, color=PALETTE["verde_profundo"])
    ax.legend(loc="upper right", framealpha=0.9, fontsize=9.5)
    ax.grid(True)
    
    save_figure(fig, output_path)

def generate_vab_pan(output_path: str):
    """
    Genera el diagrama metodológico oficial del Valor Añadido Bruto (VAB) 
    y el proceso de producción del pan en alta resolución (300 DPI) con paleta PSLL.
    """
    setup_academic_style()
    fig, ax = plt.subplots(figsize=(9.8, 5.5), dpi=300)
    fig.patch.set_facecolor(PALETTE["blanco"])
    ax.set_facecolor(PALETTE["blanco"])
    
    # 1. Título y Subtítulo
    ax.text(5.0, 5.18, "VALOR AÑADIDO BRUTO (VAB) · CADENA PRODUCTIVA DEL PAN",
            ha="center", va="center", fontsize=12.5, fontweight="bold", color=PALETTE["verde_profundo"])
    ax.text(5.0, 4.80, "Medición del PIB por la vía de la producción y eliminación del error de doble contabilización",
            ha="center", va="center", fontsize=9.0, style="italic", color=PALETTE["salvia"])
    
    # Dimensiones y posiciones horizontales refinadas (más espacio entre tarjetas)
    w_card = 2.30
    h_card = 2.65
    y_card = 1.88
    x1, x2, x3 = 0.55, 3.85, 7.15
    c1, c2, c3 = x1 + w_card/2, x2 + w_card/2, x3 + w_card/2
    
    # --- Tarjeta 1: Agricultor ---
    box_agri = patches.FancyBboxPatch((x1, y_card), w_card, h_card, boxstyle="round,pad=0.1",
                                      facecolor=PALETTE["menta"], edgecolor=PALETTE["verde_profundo"], linewidth=2.0)
    ax.add_patch(box_agri)
    
    # Pill de Fase 1
    pill1 = patches.FancyBboxPatch((c1 - 0.60, 4.22), 1.2, 0.32, boxstyle="round,pad=0.04",
                                   facecolor=PALETTE["verde_profundo"], edgecolor="none")
    ax.add_patch(pill1)
    ax.text(c1, 4.38, "FASE 1", ha="center", va="center", fontsize=7.5, fontweight="bold", color="white")
    
    ax.text(c1, 4.02, "AGRICULTOR", ha="center", va="center",
            fontsize=11.0, fontweight="bold", color=PALETTE["verde_profundo"])
    ax.text(c1, 3.75, "Sector primario · Cultivo", ha="center", va="center",
            fontsize=7.8, style="italic", color=PALETTE["verde_tinta"])
    
    ax.plot([x1 + 0.18, x1 + w_card - 0.18], [3.55, 3.55], color=PALETTE["salvia"], lw=0.8, alpha=0.5)
    ax.text(x1 + 0.18, 3.25, "Venta de trigo:", ha="left", va="center", fontsize=8.2, color=PALETTE["verde_tinta"])
    ax.text(x1 + w_card - 0.18, 3.25, "100 €", ha="right", va="center", fontsize=8.2, fontweight="bold", color=PALETTE["verde_profundo"])
    
    ax.text(x1 + 0.18, 2.90, "Consumo interm.:", ha="left", va="center", fontsize=8.2, color=PALETTE["verde_tinta"])
    ax.text(x1 + w_card - 0.18, 2.90, "0 €", ha="right", va="center", fontsize=8.2, color=PALETTE["gris_ejes"])
    
    # Badge VAB Fase 1
    badge_vab1 = patches.FancyBboxPatch((c1 - 0.90, 2.05), 1.8, 0.62, boxstyle="round,pad=0.06",
                                        facecolor=PALETTE["blanco"], edgecolor=PALETTE["verde_profundo"], linewidth=1.6)
    ax.add_patch(badge_vab1)
    ax.text(c1, 2.36, "VAB = 100 €", ha="center", va="center",
            fontsize=10.0, fontweight="bold", color=PALETTE["verde_profundo"])
    
    # --- Flecha 1 -> 2 ---
    ax.annotate("", xy=(x2 - 0.08, 3.15), xytext=(x1 + w_card + 0.08, 3.15),
                arrowprops=dict(arrowstyle="->", color=PALETTE["salvia"], lw=2.4))
    ax.text((x1 + w_card + x2)/2, 3.50, "Trigo\n100 €", ha="center", va="center",
            fontsize=7.8, fontweight="bold", color=PALETTE["salvia"], linespacing=1.2)
    
    # --- Tarjeta 2: Molino ---
    box_moli = patches.FancyBboxPatch((x2, y_card), w_card, h_card, boxstyle="round,pad=0.1",
                                      facecolor=PALETTE["crema"], edgecolor=PALETTE["salvia"], linewidth=1.8)
    ax.add_patch(box_moli)
    
    pill2 = patches.FancyBboxPatch((c2 - 0.60, 4.22), 1.2, 0.32, boxstyle="round,pad=0.04",
                                   facecolor=PALETTE["salvia"], edgecolor="none")
    ax.add_patch(pill2)
    ax.text(c2, 4.38, "FASE 2", ha="center", va="center", fontsize=7.5, fontweight="bold", color="white")
    
    ax.text(c2, 4.02, "MOLINO", ha="center", va="center",
            fontsize=11.0, fontweight="bold", color=PALETTE["verde_profundo"])
    ax.text(c2, 3.75, "Industria harinera", ha="center", va="center",
            fontsize=7.8, style="italic", color=PALETTE["verde_tinta"])
    
    ax.plot([x2 + 0.18, x2 + w_card - 0.18], [3.55, 3.55], color=PALETTE["salvia"], lw=0.8, alpha=0.5)
    ax.text(x2 + 0.18, 3.25, "Venta de harina:", ha="left", va="center", fontsize=8.2, color=PALETTE["verde_tinta"])
    ax.text(x2 + w_card - 0.18, 3.25, "150 €", ha="right", va="center", fontsize=8.2, fontweight="bold", color=PALETTE["verde_profundo"])
    
    ax.text(x2 + 0.18, 2.90, "Compra de trigo:", ha="left", va="center", fontsize=8.2, color=PALETTE["verde_tinta"])
    ax.text(x2 + w_card - 0.18, 2.90, "-100 €", ha="right", va="center", fontsize=8.2, color=PALETTE["coral"], fontweight="bold")
    
    # Badge VAB Fase 2
    badge_vab2 = patches.FancyBboxPatch((c2 - 0.90, 2.05), 1.8, 0.62, boxstyle="round,pad=0.06",
                                        facecolor=PALETTE["blanco"], edgecolor=PALETTE["salvia"], linewidth=1.6)
    ax.add_patch(badge_vab2)
    ax.text(c2, 2.36, "VAB = 50 €", ha="center", va="center",
            fontsize=10.0, fontweight="bold", color=PALETTE["verde_profundo"])
    
    # --- Flecha 2 -> 3 ---
    ax.annotate("", xy=(x3 - 0.08, 3.15), xytext=(x2 + w_card + 0.08, 3.15),
                arrowprops=dict(arrowstyle="->", color=PALETTE["salvia"], lw=2.4))
    ax.text((x2 + w_card + x3)/2, 3.50, "Harina\n150 €", ha="center", va="center",
            fontsize=7.8, fontweight="bold", color=PALETTE["salvia"], linespacing=1.2)
    
    # --- Tarjeta 3: Panadería ---
    box_pana = patches.FancyBboxPatch((x3, y_card), w_card, h_card, boxstyle="round,pad=0.1",
                                      facecolor="#FDF4F0", edgecolor=PALETTE["coral"], linewidth=2.0)
    ax.add_patch(box_pana)
    
    pill3 = patches.FancyBboxPatch((c3 - 0.60, 4.22), 1.2, 0.32, boxstyle="round,pad=0.04",
                                   facecolor=PALETTE["coral"], edgecolor="none")
    ax.add_patch(pill3)
    ax.text(c3, 4.38, "FASE 3", ha="center", va="center", fontsize=7.5, fontweight="bold", color="white")
    
    ax.text(c3, 4.02, "PANADERÍA", ha="center", va="center",
            fontsize=11.0, fontweight="bold", color=PALETTE["coral"])
    ax.text(c3, 3.75, "Transformación final · Pan", ha="center", va="center",
            fontsize=7.8, style="italic", color=PALETTE["verde_tinta"])
    
    ax.plot([x3 + 0.18, x3 + w_card - 0.18], [3.55, 3.55], color=PALETTE["coral"], lw=0.8, alpha=0.5)
    ax.text(x3 + 0.18, 3.25, "Venta al público:", ha="left", va="center", fontsize=8.2, color=PALETTE["verde_tinta"])
    ax.text(x3 + w_card - 0.18, 3.25, "250 €", ha="right", va="center", fontsize=8.2, fontweight="bold", color=PALETTE["coral"])
    
    ax.text(x3 + 0.18, 2.90, "Compra de harina:", ha="left", va="center", fontsize=8.2, color=PALETTE["verde_tinta"])
    ax.text(x3 + w_card - 0.18, 2.90, "-150 €", ha="right", va="center", fontsize=8.2, color=PALETTE["coral"], fontweight="bold")
    
    # Badge VAB Fase 3
    badge_vab3 = patches.FancyBboxPatch((c3 - 0.90, 2.05), 1.8, 0.62, boxstyle="round,pad=0.06",
                                        facecolor=PALETTE["blanco"], edgecolor=PALETTE["coral"], linewidth=1.6)
    ax.add_patch(badge_vab3)
    ax.text(c3, 2.36, "VAB = 100 €", ha="center", va="center",
            fontsize=10.0, fontweight="bold", color=PALETTE["coral"])
    
    # --- Banner Inferior de Síntesis Macroeconómica ---
    banner_box = patches.FancyBboxPatch((0.55, 0.32), 8.90, 1.28, boxstyle="round,pad=0.1",
                                        facecolor=PALETTE["verde_profundo"], edgecolor=PALETTE["salvia"], linewidth=1.8)
    ax.add_patch(banner_box)
    
    # Texto Banner Línea 1 (Fórmula agregada y PIB)
    ax.text(2.65, 1.15, "VAB TOTAL = 100 € + 50 € + 100 € = 250 €", ha="center", va="center",
            fontsize=10.5, fontweight="bold", color=PALETTE["menta"])
    ax.text(5.0, 1.15, "=", ha="center", va="center", fontsize=15.0, fontweight="bold", color="white")
    ax.text(7.35, 1.15, "PIB (VALOR DEL BIEN FINAL) = 250 €", ha="center", va="center",
            fontsize=10.5, fontweight="bold", color=PALETTE["melocoton"])
    
    # Texto Banner Línea 2 (Regla didáctica anti-doble contabilización)
    ax.text(5.0, 0.62, "Principio de Contabilidad Nacional: El PIB mide únicamente el valor añadido generado en cada fase o el valor de los bienes finales.\nSumar las ventas brutas de todos los agentes (100 € + 150 € + 250 € = 500 €) cometería un error grave de doble contabilización.",
            ha="center", va="center", fontsize=8.0, color="#FFFFFF", linespacing=1.35)
    
    ax.set_xlim(0, 10.0)
    ax.set_ylim(0.0, 5.6)
    ax.axis("off")
    
    save_figure(fig, output_path)

def generate_pib_interanual(output_path: str):
    """
    Genera el gráfico actualizado de evolución del PIB en España (2022T1 - 2026T2)
    con las tasas de variación interanual en volumen encadenado (INE / CNTR).
    """
    setup_academic_style()
    fig, ax = plt.subplots(figsize=(9.6, 4.8), dpi=300)
    fig.patch.set_facecolor(PALETTE["blanco"])
    ax.set_facecolor(PALETTE["blanco"])
    
    quarters = [
        "2022T1", "2022T2", "2022T3", "2022T4",
        "2023T1", "2023T2", "2023T3", "2023T4",
        "2024T1", "2024T2", "2024T3", "2024T4",
        "2025T1", "2025T2", "2025T3", "2025T4",
        "2026T1", "2026T2"
    ]
    rates = [
        7.1, 7.5, 6.3, 4.7,
        3.6, 2.0, 2.0, 2.2,
        2.9, 3.7, 3.6, 3.7,
        3.1, 2.9, 2.7, 2.7,
        2.7, 2.7
    ]
    
    x = np.arange(len(quarters))
    
    # Relleno suave bajo la curva (estilo editorial académico)
    ax.fill_between(x, rates, color=PALETTE["menta"], alpha=0.35, zorder=2)
    
    # Línea principal con paleta corporativa
    ax.plot(x, rates, color=PALETTE["verde_profundo"], linewidth=2.4, zorder=3,
            label="Variación interanual del PIB (%)")
    
    # Marcadores de rombo (diamante)
    ax.scatter(x, rates, color=PALETTE["salvia"], edgecolor=PALETTE["verde_profundo"],
               s=55, marker="D", linewidth=1.5, zorder=4)
    
    # Etiquetas numéricas sobre cada punto
    for xi, yi in zip(x, rates):
        label_text = f"{yi:.1f}".replace('.', ',')
        # Offset dinámico para evitar solapes
        y_offset = 6
        ax.annotate(label_text, (xi, yi), textcoords="offset points", xytext=(0, y_offset),
                    ha="center", va="bottom", fontsize=8.2, fontweight="bold",
                    color=PALETTE["verde_profundo"], zorder=5)
    
    # Configuración de ejes
    ax.set_xticks(x)
    ax.set_xticklabels(quarters, rotation=45, ha="right", fontsize=8.5, fontweight="500", color=PALETTE["verde_tinta"])
    
    y_ticks = np.arange(0, 9.0, 1.0)
    ax.set_yticks(y_ticks)
    ax.set_yticklabels([f"{val:.1f}".replace('.', ',') for val in y_ticks], fontsize=8.5, color=PALETTE["verde_tinta"])
    ax.set_ylim(0, 8.5)
    ax.set_xlim(-0.5, len(quarters) - 0.5)
    
    # Cuadrícula horizontal sutil
    ax.grid(True, axis="y", linestyle="--", alpha=0.5, color=PALETTE["gris_ejes"], zorder=1)
    
    # Estilo de spines
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_color(PALETTE["gris_ejes"])
    ax.spines['bottom'].set_color(PALETTE["gris_ejes"])
    
    # Título y Subtítulo corporativos
    plt.title("Producto Interior Bruto\n"
              r"$\mathregular{Volumen\ encadenado.\ Tasas\ de\ variación\ interanual\ (\%)}$",
              loc="left", fontsize=11.5, fontweight="bold", color=PALETTE["verde_profundo"], pad=14)
    
    # Pie de fuente y autoría en la propia figura
    ax.annotate("Fuente: Instituto Nacional de Estadística (INE). Contabilidad Nacional Trimestral de España (CNTR).",
                xy=(0, 0), xytext=(0, -46), xycoords="axes fraction", textcoords="offset points",
                ha="left", va="top", fontsize=8.0, style="italic", color=PALETTE["verde_tinta"])
    
    save_figure(fig, output_path)

def generate_productividad_salarios(output_path: str):
    """
    Genera el gráfico econométrico oficial de la relación entre Productividad por Hora
    Trabajada y Salario Medio en los 31 países de la OCDE (2024), con ranking salarial
    y España destacada en coral (R² = 0,7309).
    """
    setup_academic_style()
    
    data = [
        {"country": "Luxemburgo", "code": "LUX", "wage": 94.4, "prod": 124.0, "ha": "left", "va": "center", "ox": 7, "oy": 2},
        {"country": "Suiza", "code": "SUI", "wage": 87.5, "prod": 101.5, "ha": "left", "va": "center", "ox": 7, "oy": 3},
        {"country": "EE UU", "code": "USA", "wage": 82.9, "prod": 98.5, "ha": "right", "va": "bottom", "ox": -6, "oy": 5},
        {"country": "Bélgica", "code": "BEL", "wage": 76.1, "prod": 101.0, "ha": "left", "va": "center", "ox": 8, "oy": 3},
        {"country": "Austria", "code": "AUT", "wage": 75.8, "prod": 96.5, "ha": "right", "va": "bottom", "ox": -5, "oy": 6},
        {"country": "Países Bajos", "code": "HOL", "wage": 75.4, "prod": 97.0, "ha": "right", "va": "top", "ox": -6, "oy": -4},
        {"country": "Noruega", "code": "NOR", "wage": 74.9, "prod": 137.0, "ha": "left", "va": "center", "ox": 8, "oy": 0},
        {"country": "Dinamarca", "code": "DIN", "wage": 74.0, "prod": 100.5, "ha": "left", "va": "top", "ox": 7, "oy": -6},
        {"country": "Australia", "code": "AUS", "wage": 70.7, "prod": 85.0, "ha": "center", "va": "bottom", "ox": 0, "oy": 7},
        {"country": "Alemania", "code": "ALE", "wage": 69.4, "prod": 97.5, "ha": "center", "va": "top", "ox": 0, "oy": -9},
        {"country": "Canadá", "code": "CAN", "wage": 69.4, "prod": 74.5, "ha": "right", "va": "bottom", "ox": -5, "oy": 5},
        {"country": "Reino Unido", "code": "GBR", "wage": 63.7, "prod": 71.5, "ha": "right", "va": "bottom", "ox": -5, "oy": 5},
        {"country": "N. Zelanda", "code": "NZL", "wage": 62.4, "prod": 56.0, "ha": "right", "va": "bottom", "ox": -6, "oy": 4},
        {"country": "Eslovenia", "code": "SLV", "wage": 61.8, "prod": 66.0, "ha": "right", "va": "bottom", "ox": -5, "oy": 5},
        {"country": "Francia", "code": "FRA", "wage": 60.6, "prod": 91.0, "ha": "left", "va": "top", "ox": 6, "oy": -5},
        {"country": "Suecia", "code": "SUE", "wage": 60.4, "prod": 89.0, "ha": "center", "va": "top", "ox": 0, "oy": -9},
        {"country": "Finlandia", "code": "FIN", "wage": 59.6, "prod": 85.0, "ha": "right", "va": "top", "ox": -6, "oy": -4},
        {"country": "Israel", "code": "ISR", "wage": 54.7, "prod": 57.0, "ha": "right", "va": "bottom", "ox": -6, "oy": 4},
        {"country": "ESPAÑA", "code": "ESP", "wage": 54.6, "prod": 76.0, "ha": "left", "va": "center", "ox": 10, "oy": -2},
        {"country": "Lituania", "code": "LIT", "wage": 52.9, "prod": 64.0, "ha": "left", "va": "bottom", "ox": 6, "oy": 4},
        {"country": "Italia", "code": "ITA", "wage": 51.0, "prod": 79.0, "ha": "left", "va": "top", "ox": 6, "oy": -8},
        {"country": "Corea", "code": "COR", "wage": 50.9, "prod": 55.0, "ha": "right", "va": "bottom", "ox": -6, "oy": 3},
        {"country": "Japón", "code": "JAP", "wage": 49.4, "prod": 57.5, "ha": "left", "va": "top", "ox": 6, "oy": -5},
        {"country": "Letonia", "code": "LET", "wage": 45.6, "prod": 56.0, "ha": "left", "va": "top", "ox": 6, "oy": -3},
        {"country": "Polonia", "code": "POL", "wage": 44.2, "prod": 52.0, "ha": "right", "va": "center", "ox": -6, "oy": 0},
        {"country": "Portugal", "code": "POR", "wage": 40.0, "prod": 59.0, "ha": "left", "va": "center", "ox": 6, "oy": 1},
        {"country": "Estonia", "code": "EST", "wage": 39.0, "prod": 48.0, "ha": "right", "va": "center", "ox": -6, "oy": 0},
        {"country": "Chequia", "code": "CZE", "wage": 38.5, "prod": 58.0, "ha": "left", "va": "top", "ox": 6, "oy": -6},
        {"country": "Eslovaquia", "code": "SVQ", "wage": 36.1, "prod": 57.0, "ha": "left", "va": "top", "ox": 5, "oy": -7},
        {"country": "Hungría", "code": "HUN", "wage": 35.0, "prod": 55.0, "ha": "center", "va": "top", "ox": 0, "oy": -8},
        {"country": "Grecia", "code": "GRE", "wage": 32.3, "prod": 45.0, "ha": "center", "va": "top", "ox": 0, "oy": -8},
    ]
    
    fig = plt.figure(figsize=(12.0, 7.2), dpi=300)
    fig.patch.set_facecolor(PALETTE["blanco"])
    
    # Grid de subplots: panel izquierdo (ranking) y panel derecho (dispersión)
    gs = fig.add_gridspec(1, 2, width_ratios=[1.08, 2.7], wspace=0.18, left=0.04, right=0.96, top=0.88, bottom=0.10)
    
    ax_table = fig.add_subplot(gs[0, 0])
    ax_plot = fig.add_subplot(gs[0, 1])
    
    # --- PANEL IZQUIERDO: Ranking ---
    ax_table.axis("off")
    ax_table.set_xlim(0, 10)
    ax_table.set_ylim(0, 33)
    
    ax_table.text(5, 32.2, "SALARIO MEDIO ANUAL", ha="center", va="center",
                  fontsize=9.5, fontweight="bold", color=PALETTE["verde_profundo"])
    ax_table.text(5, 31.3, "(PPA en miles de $, año 2024)", ha="center", va="center",
                  fontsize=7.5, style="italic", color=PALETTE["verde_tinta"])
    
    ax_table.text(0.3, 30.2, "País", ha="left", va="center", fontsize=7.8, fontweight="bold", color=PALETTE["salvia"])
    ax_table.text(9.7, 30.2, "Salario", ha="right", va="center", fontsize=7.8, fontweight="bold", color=PALETTE["salvia"])
    ax_table.plot([0.2, 9.8], [29.7, 29.7], color=PALETTE["salvia"], lw=1.0)
    
    for i, d in enumerate(data):
        y_pos = 29.0 - i * 0.92
        is_esp = d["code"] == "ESP"
        
        if is_esp:
            esp_rect = patches.FancyBboxPatch((0.1, y_pos - 0.40), 9.8, 0.78, boxstyle="round,pad=0.03",
                                              facecolor="#FDF4F0", edgecolor=PALETTE["coral"], linewidth=1.3)
            ax_table.add_patch(esp_rect)
            ax_table.text(0.4, y_pos, f"19. {d['country']}", ha="left", va="center",
                          fontsize=7.8, fontweight="bold", color=PALETTE["coral"])
            ax_table.text(9.6, y_pos, f"{d['wage']:.1f}".replace('.', ','), ha="right", va="center",
                          fontsize=7.8, fontweight="bold", color=PALETTE["coral"])
        else:
            rank_num = f"{i+1}."
            color_text = PALETTE["verde_profundo"] if i < 8 else PALETTE["verde_tinta"]
            ax_table.text(0.4, y_pos, f"{rank_num} {d['country']}", ha="left", va="center",
                          fontsize=7.2, color=color_text)
            ax_table.text(9.6, y_pos, f"{d['wage']:.1f}".replace('.', ','), ha="right", va="center",
                          fontsize=7.2, color=color_text)
    
    # --- PANEL DERECHO: Dispersión y Regresión ---
    x_vals = np.array([d["prod"] for d in data])
    y_vals = np.array([d["wage"] for d in data])
    
    # Regresión MCO
    m, b = np.polyfit(x_vals, y_vals, 1)
    x_line = np.linspace(42, 130, 200)
    y_line = m * x_line + b
    
    ax_plot.plot(x_line, y_line, color=PALETTE["verde_profundo"], linestyle="--", linewidth=1.8,
                 label="Recta de regresión MCO ($R^2 = 0,7309$)", zorder=2)
    
    for d in data:
        xp, yp = d["prod"], d["wage"]
        is_esp = d["code"] == "ESP"
        
        if is_esp:
            ax_plot.scatter([xp], [yp], color=PALETTE["coral"], s=130, edgecolors=PALETTE["blanco"],
                            linewidth=2.0, zorder=6)
            ax_plot.scatter([xp], [yp], color="none", s=240, edgecolors=PALETTE["coral"],
                            linewidth=1.5, linestyle=":", zorder=5)
            
            ax_plot.annotate("ESPAÑA\n(54,6k$ · 76$/h)", xy=(xp, yp), xytext=(xp + 4, yp - 12),
                             fontsize=8.8, fontweight="bold", color=PALETTE["coral"],
                             arrowprops=dict(arrowstyle="->", color=PALETTE["coral"], lw=1.5),
                             bbox=dict(boxstyle="round,pad=0.25", facecolor="#FFF7F5", edgecolor=PALETTE["coral"], lw=1.0),
                             zorder=7)
        else:
            ax_plot.scatter([xp], [yp], color=PALETTE["salvia"], s=65, edgecolors=PALETTE["blanco"],
                            linewidth=1.0, zorder=3)
            ax_plot.annotate(d["code"], (xp, yp), xytext=(d["ox"], d["oy"]), textcoords="offset points",
                             fontsize=7.2, color=PALETTE["verde_tinta"], ha=d["ha"], va=d["va"],
                             fontweight="500", zorder=4)
    
    # Caja pedagógica interpretativa
    callout_bg = patches.FancyBboxPatch((97, 29), 47, 14.5, boxstyle="round,pad=0.5",
                                        facecolor=PALETTE["menta"], edgecolor=PALETTE["salvia"], linewidth=1.2)
    ax_plot.add_patch(callout_bg)
    ax_plot.text(120.5, 39.5, "POR DEBAJO DE LA RECTA", ha="center", va="center",
                 fontsize=8.5, fontweight="bold", color=PALETTE["verde_profundo"])
    ax_plot.text(120.5, 34.0, "España retribuye salarios medios\ninferiores a lo que le correspondería\npor su nivel de productividad por hora.",
                 ha="center", va="center", fontsize=7.8, color=PALETTE["verde_tinta"], linespacing=1.25)
    
    # Ejes y rejilla
    ax_plot.set_xlim(38, 146)
    ax_plot.set_ylim(25, 102)
    ax_plot.set_xlabel("Productividad por hora trabajada (PPA en dólares, 2024)", fontsize=9.5, fontweight="bold",
                       color=PALETTE["verde_profundo"], labelpad=8)
    ax_plot.set_ylabel("Salario medio anual (PPA en miles de dólares, 2024)", fontsize=9.5, fontweight="bold",
                       color=PALETTE["verde_profundo"], labelpad=8)
    
    ax_plot.grid(True, linestyle="--", alpha=0.5, color=PALETTE["gris_ejes"])
    ax_plot.spines['top'].set_visible(False)
    ax_plot.spines['right'].set_visible(False)
    ax_plot.spines['left'].set_color(PALETTE["gris_ejes"])
    ax_plot.spines['bottom'].set_color(PALETTE["gris_ejes"])
    
    ax_plot.legend(loc="upper left", framealpha=0.92, fontsize=8.5)
    
    # Título y Subtítulo corporativos superiores
    fig.text(0.50, 0.95, "Relación entre Productividad por Hora Trabajada y Salario Medio en la OCDE",
             ha="center", va="center", fontsize=12.5, fontweight="bold", color=PALETTE["verde_profundo"])
    fig.text(0.50, 0.915, "España presenta salarios medios bajos en relación a un nivel de productividad laboral intermedia",
             ha="center", va="center", fontsize=8.8, style="italic", color=PALETTE["salvia"])
    
    # Pie de fuente
    fig.text(0.04, 0.03, "Fuente: Elaboración propia a partir de datos oficiales de la OCDE (Productivity Statistics & Employment Outlook, 2024).",
             fontsize=7.8, style="italic", color=PALETTE["verde_tinta"])
    
    save_figure(fig, output_path)

def generate_modelo_desempleo_neoclasico(output_path: str):
    """
    Genera el gráfico del modelo neoclásico del mercado de trabajo:
    - Curva de demanda convexa decreciente D.
    - Curva de oferta con tramo backward-bending O.
    - Equilibrio competitivo E*(N*, S*).
    - Salario rígido S > S*, exceso de oferta (desempleo involuntario) y presión a la baja.
    """
    setup_academic_style()
    fig, ax = plt.subplots(figsize=(8.8, 5.8), dpi=300)
    fig.patch.set_facecolor(PALETTE["blanco"])
    ax.set_facecolor(PALETTE["blanco"])

    # 1. Curvas calibradas exactamente
    # Equilibrio en N*=5.0, S*=4.0
    N_d = np.linspace(1.3, 9.2, 200)
    S_d = 1.6 + 12.0 / N_d

    # Oferta O backward-bending: N_o(S) = 8.2 - a*(S - 7.5)^2 pasando por (5.0, 4.0)
    S_o = np.linspace(2.0, 9.2, 200)
    a_coeff = 3.2 / 12.25
    N_o = 8.2 - a_coeff * (S_o - 7.5)**2

    S_star = 4.0
    N_star = 5.0

    S_high = 6.80
    N_D_high = 12.0 / (S_high - 1.6)      # 2.3077
    N_O_high = 8.2 - a_coeff * (S_high - 7.5)**2 # 8.0720

    # 2. Trazado de Curvas
    ax.plot(N_d, S_d, color=PALETTE["verde_profundo"], linewidth=2.6, label="Demanda de trabajo ($D$)")
    ax.plot(N_o, S_o, color=PALETTE["salvia"], linewidth=2.6, label="Oferta de trabajo ($O$)")

    ax.text(N_d[-1] + 0.15, S_d[-1] + 0.1, "$D$", fontsize=12.5, fontweight="bold", color=PALETTE["verde_profundo"])
    ax.text(N_o[-1] - 0.45, S_o[-1] + 0.25, "$O$", fontsize=12.5, fontweight="bold", color=PALETTE["salvia"])

    # 3. Proyecciones del Equilibrio (N*, S*)
    ax.plot([0, N_star], [S_star, S_star], color=PALETTE["gris_ejes"], linestyle="--", lw=1.3)
    ax.plot([N_star, N_star], [0, S_star], color=PALETTE["gris_ejes"], linestyle="--", lw=1.3)
    ax.scatter([N_star], [S_star], color=PALETTE["verde_profundo"], s=75, zorder=5)

    ax.text(N_star + 0.22, S_star + 0.25, "$E^*$", fontsize=11.5, fontweight="bold", color=PALETTE["verde_profundo"])
    ax.text(N_star + 0.65, S_star + 0.25, "(Equilibrio)", fontsize=8.2, style="italic", color=PALETTE["verde_profundo"])

    # 4. Salario rígido S y Exceso de Oferta
    ax.plot([0, N_O_high], [S_high, S_high], color=PALETTE["coral"], linestyle="--", lw=1.3)
    ax.plot([N_D_high, N_D_high], [0, S_high], color=PALETTE["coral"], linestyle=":", lw=1.2)
    ax.plot([N_O_high, N_O_high], [0, S_high], color=PALETTE["coral"], linestyle=":", lw=1.2)

    ax.scatter([N_D_high], [S_high], color=PALETTE["verde_profundo"], s=65, zorder=5)
    ax.scatter([N_O_high], [S_high], color=PALETTE["salvia"], s=65, zorder=5)

    # Franja de Desempleo (flecha bidireccional)
    ax.annotate("", xy=(N_D_high, S_high), xytext=(N_O_high, S_high),
                arrowprops=dict(arrowstyle="<->", color=PALETTE["coral"], lw=2.2))
    ax.text((N_D_high + N_O_high) / 2, S_high + 0.40, "Exceso de oferta de trabajo (Desempleo)",
            ha="center", va="bottom", fontsize=9.0, fontweight="bold", color=PALETTE["coral"])

    # Flecha hacia abajo: presión bajista
    mid_x = (N_D_high + N_O_high) / 2
    ax.annotate("", xy=(mid_x, S_star + 0.45), xytext=(mid_x, S_high - 0.45),
                arrowprops=dict(arrowstyle="->", color=PALETTE["coral"], lw=2.0))
    ax.text(mid_x - 0.25, (S_high + S_star)/2, "Presión a la baja\n(si salarios son flexibles)",
            ha="right", va="center", fontsize=8.0, style="italic", color=PALETTE["coral"])

    # 5. Ejes limpios con puntas de flecha
    ax.set_xlim(0, 10.3)
    ax.set_ylim(0, 10.5)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_color(PALETTE["verde_tinta"])
    ax.spines['bottom'].set_color(PALETTE["verde_tinta"])
    ax.spines['left'].set_linewidth(1.4)
    ax.spines['bottom'].set_linewidth(1.4)

    ax.plot(0, 10.5, marker="^", markersize=7, color=PALETTE["verde_tinta"], clip_on=False)
    ax.plot(10.3, 0, marker=">", markersize=7, color=PALETTE["verde_tinta"], clip_on=False)

    ax.set_xticks([0, N_D_high, N_star, N_O_high])
    ax.set_xticklabels(["0", "$N_D$", "$N^*$", "$N_O$"], fontsize=10.0, fontweight="bold", color=PALETTE["verde_tinta"])
    ax.set_yticks([0, S_star, S_high])
    ax.set_yticklabels(["0", "$S^*$", "$S$"], fontsize=10.0, fontweight="bold", color=PALETTE["verde_tinta"])

    ax.set_xlabel("Nº Trabajadores / Nivel de Empleo ($N$)", fontsize=10.0, fontweight="bold",
                  color=PALETTE["verde_profundo"], labelpad=8)
    ax.set_ylabel("Salario real ($S$)", fontsize=10.0, fontweight="bold",
                  color=PALETTE["verde_profundo"], labelpad=8)

    # Título y Subtítulo corporativos
    fig.text(0.06, 0.95, "El Desempleo en el Modelo Neoclásico de Mercado de Trabajo",
             fontsize=12.0, fontweight="bold", color=PALETTE["verde_profundo"])
    fig.text(0.06, 0.915, "Rigidez salarial por encima del equilibrio, exceso de oferta y brecha de desempleo involuntario",
             fontsize=8.5, style="italic", color=PALETTE["salvia"])

    # Footer didáctico e institucional
    fig.text(0.08, 0.02, r"$\mathbf{Desempleo\ Involuntario} = N_O - N_D$ (a salario rígido $S > S^*$)",
             fontsize=9.0, fontweight="bold", color=PALETTE["coral"])
    fig.text(0.92, 0.02, "Fuente: Modelo neoclásico del mercado de trabajo (adaptado de M. Barneto).",
             ha="right", fontsize=7.8, style="italic", color=PALETTE["verde_tinta"])

    plt.tight_layout(rect=[0.02, 0.05, 0.98, 0.89])
    save_figure(fig, output_path)

def generate_tasa_natural_nairu(output_path: str):
    """
    Genera la comparativa pedagógica de Tasa de Desempleo Observada vs NAIRU (1980-2024)
    para España y la Zona Euro a partir de datos oficiales de AMECO (Comisión Europea).
    """
    setup_academic_style()
    years = np.arange(1980, 2025)

    esp_ur_data = {
        1980: 11.7, 1981: 14.6, 1982: 16.6, 1983: 14.7, 1984: 16.7, 1985: 17.8, 1986: 17.4, 1987: 19.7,
        1988: 18.7, 1989: 16.5, 1990: 15.5, 1991: 15.5, 1992: 17.0, 1993: 22.6, 1994: 24.1, 1995: 22.9,
        1996: 22.1, 1997: 20.6, 1998: 18.6, 1999: 15.7, 2000: 13.9, 2001: 10.6, 2002: 11.5, 2003: 11.5,
        2004: 11.0, 2005: 9.2, 2006: 8.5, 2007: 8.2, 2008: 11.3, 2009: 17.9, 2010: 19.9, 2011: 21.4,
        2012: 24.8, 2013: 26.1, 2014: 24.5, 2015: 22.1, 2016: 19.6, 2017: 17.2, 2018: 15.3, 2019: 14.1,
        2020: 15.5, 2021: 14.9, 2022: 13.0, 2023: 12.2, 2024: 11.4
    }

    esp_nawru_data = {
        1980: 10.38, 1981: 11.37, 1982: 12.38, 1983: 12.62, 1984: 13.7, 1985: 14.53, 1986: 14.99, 1987: 16.08,
        1988: 16.47, 1989: 16.66, 1990: 17.0, 1991: 17.22, 1992: 17.3, 1993: 18.03, 1994: 17.89, 1995: 17.41,
        1996: 17.11, 1997: 16.61, 1998: 16.05, 1999: 15.29, 2000: 14.82, 2001: 13.91, 2002: 13.9, 2003: 13.67,
        2004: 13.58, 2005: 13.39, 2006: 13.54, 2007: 13.63, 2008: 14.17, 2009: 15.36, 2010: 15.59, 2011: 15.84,
        2012: 16.52, 2013: 16.86, 2014: 16.77, 2015: 16.59, 2016: 16.31, 2017: 15.93, 2018: 15.52, 2019: 15.02,
        2020: 14.94, 2021: 14.32, 2022: 13.53, 2023: 13.07, 2024: 12.58
    }

    ea_ur_data = {
        1980: 6.0, 1981: 7.1, 1982: 8.1, 1983: 8.9, 1984: 9.4, 1985: 9.8, 1986: 9.9, 1987: 9.7,
        1988: 9.3, 1989: 8.4, 1990: 7.6, 1991: 7.9, 1992: 8.5, 1993: 10.2, 1994: 10.9, 1995: 10.7,
        1996: 10.9, 1997: 10.8, 1998: 10.3, 1999: 9.5, 2000: 8.5, 2001: 7.9, 2002: 8.3, 2003: 8.9,
        2004: 9.1, 2005: 9.0, 2006: 8.4, 2007: 7.5, 2008: 7.6, 2009: 9.6, 2010: 10.0, 2011: 10.1,
        2012: 11.4, 2013: 12.1, 2014: 11.6, 2015: 10.9, 2016: 10.2, 2017: 9.2, 2018: 8.3, 2019: 7.7,
        2020: 8.0, 2021: 7.8, 2022: 6.8, 2023: 6.6, 2024: 6.4
    }

    ea_nawru_data = {
        1980: 5.2, 1981: 5.8, 1982: 6.4, 1983: 7.0, 1984: 7.4, 1985: 7.8, 1986: 8.1, 1987: 8.3,
        1988: 8.5, 1989: 8.6, 1990: 8.7, 1991: 8.8, 1992: 8.9, 1993: 9.1, 1994: 9.2, 1995: 9.2,
        1996: 9.3, 1997: 9.3, 1998: 9.2, 1999: 9.1, 2000: 9.1, 2001: 8.9, 2002: 9.0, 2003: 9.0,
        2004: 9.1, 2005: 9.1, 2006: 9.1, 2007: 9.0, 2008: 9.0, 2009: 9.2, 2010: 9.1, 2011: 8.9,
        2012: 9.0, 2013: 8.9, 2014: 8.7, 2015: 8.4, 2016: 8.2, 2017: 8.0, 2018: 7.8, 2019: 7.5,
        2020: 7.3, 2021: 7.3, 2022: 7.0, 2023: 6.9, 2024: 6.8
    }

    u_esp = np.array([esp_ur_data[y] for y in years])
    n_esp = np.array([esp_nawru_data[y] for y in years])
    u_ea = np.array([ea_ur_data[y] for y in years])
    n_ea = np.array([ea_nawru_data[y] for y in years])

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10.0, 7.6), dpi=300, sharex=True)
    fig.patch.set_facecolor(PALETTE["blanco"])

    for ax in (ax1, ax2):
        ax.set_facecolor(PALETTE["blanco"])
        ax.grid(True, linestyle="--", alpha=0.5, color=PALETTE["gris_ejes"])
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['left'].set_color(PALETTE["verde_tinta"])
        ax.spines['bottom'].set_color(PALETTE["verde_tinta"])
        ax.spines['left'].set_linewidth(1.2)
        ax.spines['bottom'].set_linewidth(1.2)

    # --- PANEL 1: ZONA EURO ---
    ax1.plot(years, u_ea, color=PALETTE["verde_profundo"], lw=2.4, label="Tasa de desempleo observada ($u$)")
    ax1.plot(years, n_ea, color=PALETTE["salvia"], lw=2.2, linestyle="--", label="Tasa natural de desempleo / NAIRU ($u^*$)")

    ax1.fill_between(years, u_ea, n_ea, where=(u_ea >= n_ea), color="#FDF0EC", alpha=0.95, interpolate=True,
                     label="Desempleo cíclico ($u > u^*$, recesión / holgura laboral)")
    ax1.fill_between(years, u_ea, n_ea, where=(u_ea < n_ea), color="#EAF8F0", alpha=0.95, interpolate=True,
                     label="Sobrecalentamiento ($u < u^*$, presiones salariales)")

    ax1.set_ylim(3.5, 15.0)
    ax1.set_ylabel("Tasa de desempleo (%)", fontsize=9.2, fontweight="bold", color=PALETTE["verde_profundo"])
    ax1.text(0.02, 0.88, "PANEL A: ZONA DEL EURO (EA-20)", transform=ax1.transAxes,
             fontsize=10.0, fontweight="bold", color=PALETTE["verde_profundo"],
             bbox=dict(boxstyle="round,pad=0.25", facecolor=PALETTE["menta"], edgecolor="none", alpha=0.75))

    ax1.annotate("Pico crisis de deuda\n(2013: 12,1%)", xy=(2013, 12.1), xytext=(2014.2, 13.6),
                 arrowprops=dict(arrowstyle="->", color=PALETTE["coral"], lw=1.2),
                 fontsize=7.8, fontweight="bold", color=PALETTE["coral"])
    ax1.annotate("Mínimo histórico\n(2024: 6,4%)", xy=(2024, 6.4), xytext=(2019.5, 4.5),
                 arrowprops=dict(arrowstyle="->", color=PALETTE["verde_profundo"], lw=1.2),
                 fontsize=7.8, fontweight="bold", color=PALETTE["verde_profundo"])
    ax1.text(1987, 6.2, "NAIRU relativamente estable (~7% – 9%)", fontsize=8.0, style="italic", color=PALETTE["salvia"])

    # --- PANEL 2: ESPAÑA ---
    ax2.plot(years, u_esp, color=PALETTE["verde_profundo"], lw=2.6, label="Tasa de desempleo observada ($u$)")
    ax2.plot(years, n_esp, color=PALETTE["salvia"], lw=2.2, linestyle="--", label="Tasa natural de desempleo / NAIRU ($u^*$)")

    ax2.fill_between(years, u_esp, n_esp, where=(u_esp >= n_esp), color="#FDF0EC", alpha=0.95, interpolate=True)
    ax2.fill_between(years, u_esp, n_esp, where=(u_esp < n_esp), color="#EAF8F0", alpha=0.95, interpolate=True)

    ax2.set_ylim(6.0, 30.5)
    ax2.set_ylabel("Tasa de desempleo (%)", fontsize=9.2, fontweight="bold", color=PALETTE["verde_profundo"])
    ax2.set_xlabel("Año", fontsize=9.5, fontweight="bold", color=PALETTE["verde_profundo"], labelpad=6)
    ax2.text(0.02, 0.88, "PANEL B: ESPAÑA", transform=ax2.transAxes,
             fontsize=10.0, fontweight="bold", color=PALETTE["verde_profundo"],
             bbox=dict(boxstyle="round,pad=0.25", facecolor=PALETTE["menta"], edgecolor="none", alpha=0.75))

    ax2.annotate("Crisis 1993-94\n(24,1%)", xy=(1994, 24.1), xytext=(1991.5, 27.2),
                 arrowprops=dict(arrowstyle="->", color=PALETTE["coral"], lw=1.2),
                 fontsize=7.8, fontweight="bold", color=PALETTE["coral"])

    ax2.annotate("Burbuja / Expansión\n(2007: 8,2% < NAIRU 13,6%)", xy=(2007, 8.2), xytext=(2000.5, 7.3),
                 arrowprops=dict(arrowstyle="->", color=PALETTE["verde_profundo"], lw=1.2),
                 fontsize=7.8, fontweight="bold", color=PALETTE["verde_profundo"])

    ax2.annotate("Gran Recesión: pico 26,1%\nBrecha cíclica récord (+9,2 p.p.)", xy=(2013, 26.1), xytext=(2010.5, 28.5),
                 arrowprops=dict(arrowstyle="->", color=PALETTE["coral"], lw=1.3),
                 fontsize=8.0, fontweight="bold", color=PALETTE["coral"])

    ax2.annotate("Mínimo en 16 años\n(2024: 11,4%)", xy=(2024, 11.4), xytext=(2020.5, 9.2),
                 arrowprops=dict(arrowstyle="->", color=PALETTE["verde_profundo"], lw=1.2),
                 fontsize=7.8, fontweight="bold", color=PALETTE["verde_profundo"])

    callout_bg = patches.FancyBboxPatch((1999.0, 21.0), 7.8, 3.8, boxstyle="round,pad=0.25",
                                        facecolor=PALETTE["crema"], edgecolor=PALETTE["salvia"], lw=1.1, alpha=0.95)
    ax2.add_patch(callout_bg)
    ax2.text(2002.9, 22.9, "SUELO ESTRUCTURAL ELEVADO\nNAIRU media española: ~15,0%\n(duplica el promedio de la Eurozona)",
             ha="center", va="center", fontsize=7.6, fontweight="bold", color=PALETTE["verde_profundo"], linespacing=1.25)

    ax2.set_xticks(np.arange(1980, 2026, 5))
    ax2.set_xticklabels([str(y) for y in np.arange(1980, 2026, 5)], fontsize=9.0, color=PALETTE["verde_tinta"])

    handles, labels = ax1.get_legend_handles_labels()
    fig.legend(handles, labels, loc="upper center", bbox_to_anchor=(0.50, 0.935),
               ncol=2, frameon=True, facecolor="#FCFDFC", edgecolor=PALETTE["gris_ejes"], fontsize=7.9)

    fig.text(0.05, 0.98, "Tasa de Desempleo Observada y Tasa Natural (NAIRU): España vs. Zona Euro (1980–2024)",
             fontsize=11.5, fontweight="bold", color=PALETTE["verde_profundo"])
    fig.text(0.05, 0.952, "Descomposición entre el desempleo estructural (tendencia de fondo) y el desempleo cíclico (brecha de holgura)",
             fontsize=8.5, style="italic", color=PALETTE["salvia"])

    fig.text(0.05, 0.015, r"$\mathbf{Desempleo\ C\acute{\imath}clico} = u - u^*$ (recesión y holgura laboral si $u > u^*$)",
             fontsize=8.0, fontweight="bold", color=PALETTE["verde_profundo"])
    fig.text(0.95, 0.015, "Fuente: Elaboración propia a partir de datos oficiales de AMECO (Comisión Europea, DG ECFIN, 2024).",
             ha="right", fontsize=7.5, style="italic", color=PALETTE["verde_tinta"])

    plt.tight_layout(rect=[0.03, 0.04, 0.97, 0.91])
    save_figure(fig, output_path)

def generate_curva_phillips_dual(output_path: str):
    """
    Genera la Figura Dual de la Curva de Phillips:
    - Panel A: Modelo Teórico de Friedman-Phelps (Curvas CP1, CP2 y Largo Plazo vertical en la NAIRU).
    - Panel B: Evidencia Empírica en España (2002-2024) categorizada en 4 fases cíclicas con datos oficiales INE.
    """
    setup_academic_style()
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11.6, 5.8), dpi=300)
    fig.patch.set_facecolor(PALETTE["blanco"])

    for ax in (ax1, ax2):
        ax.set_facecolor(PALETTE["blanco"])
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['left'].set_color(PALETTE["verde_tinta"])
        ax.spines['bottom'].set_color(PALETTE["verde_tinta"])
        ax.spines['left'].set_linewidth(1.3)
        ax.spines['bottom'].set_linewidth(1.3)

    # ==========================================
    # PANEL A: EL MODELO TEÓRICO (FRIEDMAN-PHELPS)
    # ==========================================
    ax1.grid(True, linestyle="--", alpha=0.45, color=PALETTE["gris_ejes"])

    u_axis = np.linspace(2.0, 9.5, 200)
    u_star = 5.5  # NAIRU / Tasa natural de desempleo
    u_low = 3.2   # Paro reducido tras estímulo

    k_val = 3.0 / (1.0 / (u_low - 1.2) - 1.0 / (u_star - 1.2))
    cp1 = 2.0 + k_val * (1.0 / (u_axis - 1.2) - 1.0 / (u_star - 1.2))
    cp2 = 5.0 + k_val * (1.0 / (u_axis - 1.2) - 1.0 / (u_star - 1.2))

    ax1.plot(u_axis, cp1, color=PALETTE["salvia"], lw=2.5, label=r"$CP_1$ (Expectativas $\pi_1^e = 2\%$)")
    ax1.plot(u_axis, cp2, color="#9AB39E", lw=2.5, linestyle="-.", label=r"$CP_2$ (Expectativas $\pi_2^e = 5\%$)")
    ax1.axvline(x=u_star, color=PALETTE["verde_profundo"], lw=2.8, label=r"$LP$ (Largo Plazo vertical en NAIRU $u^*$)")

    # Puntos clave
    ax1.scatter([u_star], [2.0], color=PALETTE["verde_profundo"], s=85, zorder=5)
    ax1.text(u_star + 0.25, 1.85, r"$\mathbf{A}$", fontsize=11.5, fontweight="bold", color=PALETTE["verde_profundo"])
    ax1.text(u_star + 0.65, 1.85, r"$(\pi_1=2\%)$", fontsize=8.2, color=PALETTE["verde_profundo"])

    ax1.scatter([u_low], [5.0], color=PALETTE["coral"], s=85, zorder=5)
    ax1.text(u_low - 0.55, 5.15, r"$\mathbf{B}$", fontsize=11.5, fontweight="bold", color=PALETTE["coral"])
    ax1.text(u_low - 1.5, 4.7, r"$(\pi_2=5\%)$", fontsize=8.2, color=PALETTE["coral"])

    ax1.scatter([u_star], [5.0], color=PALETTE["verde_profundo"], s=85, zorder=5)
    ax1.text(u_star + 0.25, 5.15, r"$\mathbf{C}$", fontsize=11.5, fontweight="bold", color=PALETTE["verde_profundo"])
    ax1.text(u_star + 0.65, 5.15, r"$(\pi_2=5\%)$", fontsize=8.2, color=PALETTE["verde_profundo"])

    # Flechas dinámicas
    ax1.annotate("", xy=(u_low + 0.25, 4.6), xytext=(u_star - 0.3, 2.3),
                 arrowprops=dict(arrowstyle="->", color=PALETTE["coral"], lw=2.2, connectionstyle="arc3,rad=-0.18"))
    ax1.text(3.7, 3.1, "① Estímulo coyuntural\n(paro cae a $u_1$, inflación sube)",
             ha="right", fontsize=7.6, fontweight="bold", color=PALETTE["coral"])

    ax1.annotate("", xy=(u_star - 0.2, 5.0), xytext=(u_low + 0.3, 5.0),
                 arrowprops=dict(arrowstyle="->", color=PALETTE["verde_profundo"], lw=2.2))
    ax1.text((u_low + u_star)/2, 4.45, "② Ajuste a largo plazo ($\pi^e = 5\%$)\n(el desempleo retorna a la NAIRU)",
             ha="center", fontsize=7.4, fontweight="bold", color=PALETTE["verde_profundo"])

    # Proyecciones punteadas
    ax1.plot([u_star, u_star], [0, 2.0], color=PALETTE["gris_ejes"], linestyle=":", lw=1.2)
    ax1.plot([0, u_star], [2.0, 2.0], color=PALETTE["gris_ejes"], linestyle=":", lw=1.2)
    ax1.plot([u_low, u_low], [0, 5.0], color=PALETTE["gris_ejes"], linestyle=":", lw=1.2)
    ax1.plot([0, u_star], [5.0, 5.0], color=PALETTE["gris_ejes"], linestyle=":", lw=1.2)

    # Flechas ejes
    ax1.plot(0, 8.4, marker="^", markersize=6.5, color=PALETTE["verde_tinta"], clip_on=False)
    ax1.plot(10.0, 0, marker=">", markersize=6.5, color=PALETTE["verde_tinta"], clip_on=False)

    ax1.set_xlim(0, 10.0)
    ax1.set_ylim(0, 8.4)
    ax1.set_xticks([u_low, u_star])
    ax1.set_xticklabels([r"$u_1$", r"$u^*\ (\mathrm{NAIRU})$"], fontsize=9.2, fontweight="bold", color=PALETTE["verde_tinta"])
    ax1.set_yticks([2.0, 5.0])
    ax1.set_yticklabels([r"$\pi_1^e = 2\%$", r"$\pi_2^e = 5\%$"], fontsize=9.2, fontweight="bold", color=PALETTE["verde_tinta"])

    ax1.set_xlabel("Tasa de desempleo ($u$)", fontsize=9.5, fontweight="bold", color=PALETTE["verde_profundo"], labelpad=6)
    ax1.set_ylabel("Tasa de inflación ($\pi$)", fontsize=9.5, fontweight="bold", color=PALETTE["verde_profundo"], labelpad=6)

    ax1.set_title("PANEL A: Modelo de Expectativas (Friedman-Phelps)",
                  fontsize=9.8, fontweight="bold", color=PALETTE["verde_profundo"], pad=12)
    ax1.legend(loc="lower left", framealpha=0.92, fontsize=7.5, bbox_to_anchor=(0.02, 0.03))

    # ==========================================
    # PANEL B: EVIDENCIA EMPÍRICA EN ESPAÑA (2002–2024)
    # ==========================================
    ax2.grid(True, linestyle="--", alpha=0.45, color=PALETTE["gris_ejes"])

    p1_ur = [11.5, 11.4, 11.3, 11.5, 11.2, 11.3, 11.2, 11.0, 10.8, 10.6, 10.5, 10.2,
             10.2, 9.3, 8.7, 8.6, 8.5, 8.3, 8.2, 8.0, 8.2, 8.0, 8.2, 8.6]
    p1_w =  [3.6, 4.3, 3.9, 3.6, 4.0, 3.8, 3.9, 4.1, 4.2, 4.0, 3.5, 2.6,
             1.8, 2.4, 2.6, 3.7, 3.9, 5.1, 4.8, 3.7, 4.3, 4.1, 4.5, 4.7]

    p2_ur = [9.6, 10.4, 11.2, 13.8, 17.2, 17.8, 17.8, 18.7, 19.8, 19.9, 19.6, 20.1,
             21.1, 20.7, 21.3, 22.6, 24.2, 24.4, 24.8, 25.8, 26.9, 26.1, 25.7, 25.7]
    p2_w =  [5.2, 5.0, 5.3, 4.8, 2.9, 4.1, 3.1, 2.7, 1.9, 1.8, 0.1, 0.0,
             1.7, 1.2, 0.6, 1.4, -0.1, 0.3, -0.3, -3.6, -1.8, 0.0, -0.6, -0.2]

    p3_ur = [25.7, 24.3, 23.5, 23.7, 23.6, 22.2, 21.0, 20.8, 20.8, 19.8, 18.7, 18.6,
             18.6, 17.1, 16.3, 16.5, 16.6, 15.2, 14.4, 14.3, 14.6, 13.9, 13.8, 13.7]
    p3_w =  [0.0, 1.4, 1.2, -0.2, 0.6, 1.0, 1.2, 1.0, -0.2, -0.3, -0.8, -0.8,
             -0.1, 0.0, 0.4, 0.6, 0.7, 0.9, 1.1, 1.5, 2.2, 2.1, 1.9, 2.3]

    p4_ur = [14.4, 15.3, 16.3, 16.1, 16.0, 15.3, 14.6, 13.3, 13.6, 12.5, 12.7, 12.9,
             13.3, 11.6, 11.8, 11.8, 12.3, 11.3, 11.2, 11.4]
    p4_w =  [1.8, -1.4, 2.5, 2.8, 1.4, 3.1, 2.6, 2.8, 3.2, 4.3, 4.0, 3.8,
             4.3, 5.1, 4.2, 4.0, 3.9, 4.3, 4.1, 3.8]

    ax2.scatter(p1_ur, p1_w, color=PALETTE["verde_profundo"], s=42, alpha=0.85, label="2002–2007 (Expansión y Burbuja)", zorder=4)
    ax2.scatter(p2_ur, p2_w, color=PALETTE["coral"], s=42, alpha=0.85, label="2008–2013 (Gran Recesión)", zorder=4)
    ax2.scatter(p3_ur, p3_w, color=PALETTE["salvia"], s=42, alpha=0.85, label="2014–2019 (Recuperación y aplanamiento)", zorder=4)
    ax2.scatter(p4_ur, p4_w, color="#2F3A30", s=44, marker="s", alpha=0.90, label="2020–2024 (COVID y Shock Inflacionista)", zorder=4)

    all_ur = np.array(p1_ur + p2_ur + p3_ur + p4_ur)
    all_w = np.array(p1_w + p2_w + p3_w + p4_w)

    fit_u = np.linspace(7.8, 27.2, 200)
    poly = np.polyfit(1.0 / all_ur, all_w, deg=1)
    fit_w = poly[0] / fit_u + poly[1]
    ax2.plot(fit_u, fit_w, color=PALETTE["verde_profundo"], lw=1.9, linestyle="--", alpha=0.85, label="Tendencia inversa estimada")
    ax2.axhline(0, color=PALETTE["verde_tinta"], lw=0.9, linestyle="--", alpha=0.55)

    # Anotaciones didácticas
    ax2.annotate("2006T4: Paro 8,3%\nCoste sal. +5,1%", xy=(8.3, 5.1), xytext=(8.0, 6.2),
                 arrowprops=dict(arrowstyle="->", color=PALETTE["verde_profundo"], lw=1.0),
                 fontsize=7.2, fontweight="bold", color=PALETTE["verde_profundo"])

    ax2.annotate("2012T4: Devaluación salarial\nrécord (-3,6%)", xy=(25.8, -3.6), xytext=(18.8, -4.5),
                 arrowprops=dict(arrowstyle="->", color=PALETTE["coral"], lw=1.0),
                 fontsize=7.2, fontweight="bold", color=PALETTE["coral"])

    ax2.annotate("2013T1: Máximo paro (26,9%)", xy=(26.9, -1.8), xytext=(21.5, -1.0),
                 arrowprops=dict(arrowstyle="->", color=PALETTE["coral"], lw=1.0),
                 fontsize=7.2, color=PALETTE["coral"])

    ax2.annotate("2023T2: Repunte (+5,1%)\ncon paro al 11,6%", xy=(11.6, 5.05), xytext=(14.2, 6.0),
                 arrowprops=dict(arrowstyle="->", color="#2F3A30", lw=1.0),
                 fontsize=7.2, fontweight="bold", color="#2F3A30")

    ax2.set_xlim(6.0, 28.5)
    ax2.set_ylim(-5.5, 7.2)
    ax2.set_xlabel("Tasa de desempleo - EPA (%)", fontsize=9.5, fontweight="bold", color=PALETTE["verde_profundo"], labelpad=6)
    ax2.set_ylabel("Variación anual coste salarial - ETCL (%)", fontsize=9.5, fontweight="bold", color=PALETTE["verde_profundo"], labelpad=6)

    ax2.set_title("PANEL B: Evidencia Empírica en España (2002–2024)",
                  fontsize=9.8, fontweight="bold", color=PALETTE["verde_profundo"], pad=12)
    ax2.legend(loc="lower left", framealpha=0.92, fontsize=7.0, bbox_to_anchor=(0.02, 0.02))

    # Título y Subtítulo corporativos
    fig.text(0.05, 0.968, "La Curva de Phillips: Modelo Teórico y Evidencia Empírica en España (2002–2024)",
             fontsize=11.5, fontweight="bold", color=PALETTE["verde_profundo"])
    fig.text(0.05, 0.935, "De la relación inversa a corto plazo y la vertical a largo plazo (NAIRU) al comportamiento real de salarios y desempleo",
             fontsize=8.5, style="italic", color=PALETTE["salvia"])

    # Pie didáctico e institucional
    fig.text(0.05, 0.015, "Panel A: Modelo de expectativas de Friedman-Phelps. Panel B: Datos trimestrales armonizados de la EPA y ETCL.",
             fontsize=7.8, color=PALETTE["verde_profundo"])
    fig.text(0.95, 0.015, "Fuente: Elaboración propia a partir de datos oficiales del Instituto Nacional de Estadística (INE, 2024).",
             ha="right", fontsize=7.5, style="italic", color=PALETTE["verde_tinta"])

    plt.tight_layout(rect=[0.02, 0.04, 0.98, 0.91])
    save_figure(fig, output_path)

def generate_figures_for_topic(topic_num: int, project_root: str):
    """Genera las figuras remasterizadas para un tema específico en su carpeta relativa."""
    dest_dir = os.path.join(project_root, f"Temas EB/Tema {topic_num}/figuras/remasterizadas")
    os.makedirs(dest_dir, exist_ok=True)
    print(f"\n--- Generando figuras remasterizadas para Tema {topic_num} en: {dest_dir} ---")
    
    if topic_num == 1:
        epa_path = os.path.join(dest_dir, "epa_taxonomy.png")
        tree_path = os.path.join(dest_dir, "epa_decision_tree.png")
        vab_path = os.path.join(dest_dir, "vab_pan.png")
        pib_path = os.path.join(dest_dir, "pib_interanual.png")
        prod_path = os.path.join(dest_dir, "productividad_salarios.png")
        bev_path = os.path.join(dest_dir, "beveridge.png")
        neo_path = os.path.join(dest_dir, "modelo_desempleo_neoclasico.png")
        nairu_path = os.path.join(dest_dir, "tasa_natural_nairu.png")
        phil_path = os.path.join(dest_dir, "curva_phillips_dual.png")
        generate_epa_taxonomy(epa_path)
        generate_epa_decision_tree(tree_path)
        generate_vab_pan(vab_path)
        generate_pib_interanual(pib_path)
        generate_productividad_salarios(prod_path)
        generate_beveridge_curve(bev_path)
        generate_modelo_desempleo_neoclasico(neo_path)
        generate_tasa_natural_nairu(nairu_path)
        generate_curva_phillips_dual(phil_path)
    else:
        print(f"Aún no hay generadores registrados para el Tema {topic_num}.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Genera figuras oficiales en alta resolución para los temas de PSLL.")
    parser.add_argument("--tema", type=int, default=1, help="Número del tema (ej. 1)")
    args = parser.parse_args()
    
    project_root = os.path.abspath(os.path.join(CURRENT_DIR, "..", ".."))
    generate_figures_for_topic(args.tema, project_root)
