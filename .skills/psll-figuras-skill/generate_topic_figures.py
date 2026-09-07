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
        bev_path = os.path.join(dest_dir, "beveridge.png")
        generate_epa_taxonomy(epa_path)
        generate_epa_decision_tree(tree_path)
        generate_vab_pan(vab_path)
        generate_pib_interanual(pib_path)
        generate_beveridge_curve(bev_path)
    else:
        print(f"Aún no hay generadores registrados para el Tema {topic_num}.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Genera figuras oficiales en alta resolución para los temas de PSLL.")
    parser.add_argument("--tema", type=int, default=1, help="Número del tema (ej. 1)")
    args = parser.parse_args()
    
    project_root = os.path.abspath(os.path.join(CURRENT_DIR, "..", ".."))
    generate_figures_for_topic(args.tema, project_root)
