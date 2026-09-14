"""
figure_generator.py - Generador de figuras y gráficos académicos en alta resolución (300 DPI)
utilizando la identidad visual oficial de PSLL (BRAND.md) con matplotlib.
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import os

# Paleta oficial para gráficos (secuencia BRAND.md)
PALETTE = {
    "verde_pino": "#113927",
    "verde_profundo": "#113927",
    "salvia": "#76927A",
    "coral": "#E98F71",
    "melocoton": "#EDB090",
    "verde_tinta": "#2F3A30",
    "menta": "#F4F8F5",
    "crema": "#F4F8F5",
    "fondo_grafico": "#FFFFFF",
    "gris_ejes": "#A0B0A4",
    "border_slate": "#E2E8F0",
    "upo_navy": "#0B1C36",
}

def setup_academic_style():
    """Configura parámetros globales de estilo en matplotlib."""
    plt.rcParams['font.sans-serif'] = ['Calibri', 'Arial', 'DejaVu Sans']
    plt.rcParams['font.family'] = 'sans-serif'
    plt.rcParams['text.color'] = PALETTE['verde_tinta']
    plt.rcParams['axes.labelcolor'] = PALETTE['verde_tinta']
    plt.rcParams['xtick.color'] = PALETTE['verde_tinta']
    plt.rcParams['ytick.color'] = PALETTE['verde_tinta']
    plt.rcParams['axes.edgecolor'] = PALETTE['gris_ejes']
    plt.rcParams['axes.linewidth'] = 0.8
    plt.rcParams['grid.color'] = '#E6EBE7'
    plt.rcParams['grid.linestyle'] = '--'
    plt.rcParams['grid.alpha'] = 0.7

def generate_beveridge_figure(output_path: str):
    """
    Genera el gráfico canónico de la Curva de Beveridge:
    - Movimientos cíclicos a lo largo de la curva (A -> B)
    - Desplazamientos estructurales hacia fuera (A -> C) por ineficiencia o mismatch
    """
    setup_academic_style()
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    fig, ax = plt.subplots(figsize=(7.5, 4.8), dpi=300)
    fig.patch.set_facecolor(PALETTE['fondo_grafico'])
    ax.set_facecolor(PALETTE['fondo_grafico'])
    
    # Rango de desempleo
    u = np.linspace(3.5, 22.0, 300)
    
    # Curva 1: Eficiencia alta (BC1)
    v1 = 18.0 / (u - 1.5) + 0.3
    # Curva 2: Menor eficiencia / desajuste estructural (BC2)
    v2 = 28.0 / (u - 1.5) + 0.8
    
    # Trazar curvas
    ax.plot(u, v1, color=PALETTE['salvia'], linewidth=2.8, label=r'Curva de Beveridge inicial ($BC_1$)')
    ax.plot(u, v2, color=PALETTE['coral'], linewidth=2.8, linestyle='--', label=r'Desplazamiento estructural ($BC_2$ · Desajuste / Histéresis)')
    
    # Puntos de análisis
    u_A, v_A = 7.5, 18.0 / (7.5 - 1.5) + 0.3
    u_B, v_B = 14.5, 18.0 / (14.5 - 1.5) + 0.3
    u_C, v_C = 14.5, 28.0 / (14.5 - 1.5) + 0.8
    
    # Dibujar puntos
    ax.scatter([u_A], [v_A], color=PALETTE['verde_profundo'], s=70, zorder=5)
    ax.scatter([u_B], [v_B], color=PALETTE['salvia'], s=70, zorder=5)
    ax.scatter([u_C], [v_C], color=PALETTE['coral'], s=80, zorder=5)
    
    # Etiquetas de puntos
    ax.annotate('Punto A\n(Expansión cíclica)', xy=(u_A, v_A), xytext=(u_A - 0.5, v_A + 0.7),
                fontsize=9.5, fontweight='bold', color=PALETTE['verde_profundo'])
    ax.annotate('Punto B\n(Recesión cíclica)', xy=(u_B, v_B), xytext=(u_B - 1.0, v_B + 0.6),
                fontsize=9.5, fontweight='bold', color=PALETTE['salvia'])
    ax.annotate('Punto C\n(Desajuste estructural / PLD)', xy=(u_C, v_C), xytext=(u_C + 0.4, v_C + 0.2),
                fontsize=9.5, fontweight='bold', color=PALETTE['coral'])
    
    # Flecha movimiento cíclico A -> B
    ax.annotate('', xy=(u_B - 0.5, v_B + 0.1), xytext=(u_A + 1.0, v_A - 0.5),
                arrowprops=dict(arrowstyle="->", color=PALETTE['salvia'], lw=1.6, connectionstyle="arc3,rad=-0.15"))
    ax.text(9.8, 1.8, 'Movimiento cíclico a lo largo\n(Shock de Demanda Agregada)', 
            fontsize=8.5, color=PALETTE['salvia'], style='italic')
    
    # Flecha desplazamiento estructural B -> C
    ax.annotate('', xy=(u_C, v_C - 0.1), xytext=(u_B, v_B + 0.2),
                arrowprops=dict(arrowstyle="->", color=PALETTE['coral'], lw=1.8, linestyle=':'))
    ax.text(14.8, 2.0, 'Desplazamiento hacia fuera\n(Pérdida de eficiencia / Mismatch)', 
            fontsize=8.5, color=PALETTE['coral'], style='italic')
    
    # Configuración de ejes
    ax.set_xlim(2, 23)
    ax.set_ylim(0, 5.0)
    ax.set_xlabel('Tasa de Desempleo, $u$ (%)', fontsize=11, labelpad=8, fontweight='bold')
    ax.set_ylabel('Tasa de Vacantes, $v$ (%)', fontsize=11, labelpad=8, fontweight='bold')
    ax.set_title('La Curva de Beveridge: Dinámica Cíclica vs. Desajuste Estructural', 
                 fontsize=13, fontweight='bold', pad=14, color=PALETTE['verde_profundo'])
    
    ax.grid(True)
    ax.legend(frameon=True, facecolor='#F7FAF8', edgecolor=PALETTE['gris_ejes'], fontsize=9.5, loc='upper right')
    
    # Pie de autoría reglamentario (BRAND.md)
    plt.figtext(0.12, 0.02, 'Fuente: Elaboración propia para Políticas Sociolaborales y de Empleo (UPO). Marco Diamond-Mortensen-Pissarides.', 
                fontsize=8, color='#6F8073', style='italic')
    
    plt.tight_layout(rect=[0, 0.05, 1, 1])
    plt.savefig(output_path, dpi=300, facecolor=fig.get_facecolor(), edgecolor='none')
    plt.close()
    return output_path

def generate_epa_taxonomy_figure(output_path: str):
    """
    Genera el esquema analítico de la clasificación de la población según la EPA (INE/OIT).
    """
    setup_academic_style()
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    fig, ax = plt.subplots(figsize=(7.5, 3.8), dpi=300)
    fig.patch.set_facecolor(PALETTE['fondo_grafico'])
    ax.set_facecolor(PALETTE['fondo_grafico'])
    
    # Ocultar ejes para hacer un diagrama conceptual limpio
    ax.axis('off')
    
    # Definir cajas (x, y, ancho, alto, color, texto_ppal, subtexto)
    boxes = [
        # Nivel 1: Población Total
        (0.32, 0.82, 0.36, 0.14, PALETTE['menta'], PALETTE['verde_profundo'], 'POBLACIÓN TOTAL', 'España ~48,5 millones'),
        # Nivel 2: Menores vs PET
        (0.08, 0.58, 0.28, 0.14, '#F3F4F3', '#667066', '< 16 AÑOS', 'Población no activa legalmente'),
        (0.44, 0.58, 0.48, 0.14, PALETTE['menta'], PALETTE['verde_profundo'], 'POBLACIÓN EN EDAD DE TRABAJAR (PET)', 'Población de 16 y más años (~40,2 M)'),
        # Nivel 3: Activos vs Inactivos
        (0.38, 0.34, 0.26, 0.14, '#FDFBF7', '#768074', 'INACTIVOS', 'Estudiantes, jubilados, desánimo (~16,3 M)'),
        (0.68, 0.34, 0.28, 0.14, PALETTE['salvia'], '#FFFFFF', 'POBLACIÓN ACTIVA', 'Ocupados + Parados (~23,9 M)'),
        # Nivel 4: Ocupados vs Parados
        (0.56, 0.08, 0.20, 0.15, PALETTE['verde_profundo'], '#FFFFFF', 'OCUPADOS', 'Con empleo\n(~21,3 M)'),
        (0.79, 0.08, 0.18, 0.15, PALETTE['coral'], '#FFFFFF', 'PARADOS', 'Búsqueda activa\n(~2,6 M)'),
    ]
    
    for x, y, w, h, bg_color, text_color, title, sub in boxes:
        rect = plt.Rectangle((x, y), w, h, facecolor=bg_color, edgecolor=PALETTE['verde_profundo'],
                             linewidth=1.2, transform=ax.transAxes, clip_on=False)
        ax.add_patch(rect)
        ax.text(x + w/2, y + h*0.62, title, transform=ax.transAxes, ha='center', va='center',
                fontsize=8.5, fontweight='bold', color=text_color)
        ax.text(x + w/2, y + h*0.28, sub, transform=ax.transAxes, ha='center', va='center',
                fontsize=7.2, color=text_color)
        
    # Conectores / flechas tenues
    ax.annotate('', xy=(0.22, 0.72), xytext=(0.42, 0.82), arrowprops=dict(arrowstyle="->", color=PALETTE['gris_ejes'], lw=1.2))
    ax.annotate('', xy=(0.68, 0.72), xytext=(0.58, 0.82), arrowprops=dict(arrowstyle="->", color=PALETTE['gris_ejes'], lw=1.2))
    ax.annotate('', xy=(0.51, 0.48), xytext=(0.62, 0.58), arrowprops=dict(arrowstyle="->", color=PALETTE['gris_ejes'], lw=1.2))
    ax.annotate('', xy=(0.82, 0.48), xytext=(0.74, 0.58), arrowprops=dict(arrowstyle="->", color=PALETTE['gris_ejes'], lw=1.2))
    ax.annotate('', xy=(0.66, 0.23), xytext=(0.78, 0.34), arrowprops=dict(arrowstyle="->", color=PALETTE['gris_ejes'], lw=1.2))
    ax.annotate('', xy=(0.88, 0.23), xytext=(0.84, 0.34), arrowprops=dict(arrowstyle="->", color=PALETTE['gris_ejes'], lw=1.2))
    
    ax.set_title('Taxonomía Oficial del Mercado de Trabajo (Encuesta de Población Activa - INE / OIT)',
                 fontsize=11.5, fontweight='bold', pad=10, color=PALETTE['verde_profundo'], ha='center')
    
    plt.figtext(0.12, 0.01, 'Fuente: Elaboración propia a partir de la metodología de la EPA (INE) y directrices de la OIT.',
                fontsize=7.5, color='#6F8073', style='italic')
    
    plt.tight_layout(rect=[0, 0.04, 1, 1])
    plt.savefig(output_path, dpi=300, facecolor=fig.get_facecolor(), edgecolor='none')
    plt.close()
    return output_path
