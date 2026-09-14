"""
brand_figures.py - Utilidades de estilo y paleta oficial de PSLL para gráficos matplotlib.
"""

import os
import sys
import io
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

try:
    if hasattr(sys.stdout, 'encoding') and sys.stdout.encoding.lower() != 'utf-8':
        if hasattr(sys.stdout, 'buffer'):
            sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
except Exception:
    pass

PALETTE = {
    "verde_pino": "#113927",
    "verde_profundo": "#113927",
    "salvia": "#76927A",
    "coral": "#E98F71",
    "melocoton": "#EDB090",
    "verde_tinta": "#2F3A30",
    "menta": "#F4F8F5",
    "crema": "#F4F8F5",
    "blanco": "#FFFFFF",
    "gris_ejes": "#A0B0A4",
    "grid_color": "#E6EBE7",
    "border_slate": "#E2E8F0",
    "upo_navy": "#0B1C36",
}

def setup_academic_style():
    """Configura parámetros globales de estilo en matplotlib según la marca oficial PSLL."""
    plt.rcParams['font.sans-serif'] = ['Calibri', 'Arial', 'DejaVu Sans']
    plt.rcParams['font.family'] = 'sans-serif'
    plt.rcParams['text.color'] = PALETTE['verde_tinta']
    plt.rcParams['axes.labelcolor'] = PALETTE['verde_tinta']
    plt.rcParams['xtick.color'] = PALETTE['verde_tinta']
    plt.rcParams['ytick.color'] = PALETTE['verde_tinta']
    plt.rcParams['axes.edgecolor'] = PALETTE['gris_ejes']
    plt.rcParams['axes.linewidth'] = 0.8
    plt.rcParams['grid.color'] = PALETTE['grid_color']
    plt.rcParams['grid.linestyle'] = '--'
    plt.rcParams['grid.alpha'] = 0.7

def save_figure(fig, output_path: str, dpi=300):
    """Guarda una figura en disco asegurando la creación de directorios y calidad 300 DPI."""
    os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
    fig.savefig(output_path, dpi=dpi, bbox_inches='tight', facecolor=fig.get_facecolor(), edgecolor='none')
    plt.close(fig)
    print(f"📊 Figura guardada en: {output_path}")
