"""
Módulo de Estilo y Marca PSLL para Gráficos en Python (Matplotlib / Seaborn)
Uso:
    from estilo_graficos import aplicar_estilo_psll, BRAND_COLORS, COLOR_CYCLE, anadir_firma

    aplicar_estilo_psll()
    fig, ax = plt.subplots(figsize=(8, 4.5))
    ax.plot(x, y, color=BRAND_COLORS['primary'], label='Tasa de Paro')
    anadir_firma(ax, fuente="EPA, INE")
"""

import matplotlib.pyplot as plt

BRAND_COLORS = {
    'primary': '#A33327',     # Rojo ladrillo profundo
    'secondary': '#D47B5A',   # Terracota cálido
    'tertiary': '#C68B59',    # Ámbar / arcilla
    'quaternary': '#E3ACA1',  # Rojo pastel apagado
    'highlight': '#5C2317',   # Marrón rojizo oscuro
    'muted': '#A49080'        # Marrón grisáceo tenue
}

COLOR_CYCLE = ['#A33327', '#D47B5A', '#C68B59', '#5C2317', '#E3ACA1', '#A49080']

def aplicar_estilo_psll():
    """Aplica la configuración de rcParams oficial para gráficos PSLL."""
    plt.rcParams.update({
        'figure.facecolor': '#FDFBF7',
        'axes.facecolor': '#FAF6F0',
        'axes.edgecolor': '#E3DCD2',
        'axes.linewidth': 0.8,
        'axes.labelcolor': '#4A3B32',
        'axes.titlesize': 13,
        'axes.titleweight': 'bold',
        'axes.titlecolor': '#2F241D',
        'text.color': '#4A3B32',
        'xtick.color': '#4A3B32',
        'ytick.color': '#4A3B32',
        'xtick.labelsize': 9.5,
        'ytick.labelsize': 9.5,
        'grid.color': '#E3DCD2',
        'grid.linestyle': '--',
        'grid.linewidth': 0.6,
        'grid.alpha': 0.7,
        'legend.facecolor': '#FAF6F0',
        'legend.edgecolor': '#E3DCD2',
        'legend.fontsize': 9,
        'font.family': 'sans-serif',
        'font.sans-serif': ['Calibri', 'Arial', 'DejaVu Sans']
    })

def anadir_firma(ax, fuente="EPA, INE", autor="Políticas Sociolaborales (UPO) / @manujhidalgo"):
    """Añade la firma institucional de fuentes y autoría al pie del gráfico."""
    texto = f"Fuente: {fuente} · {autor}"
    ax.figure.text(
        0.01, 0.01, texto,
        ha='left', va='bottom',
        fontsize=8, color='#A49080',
        style='italic'
    )
