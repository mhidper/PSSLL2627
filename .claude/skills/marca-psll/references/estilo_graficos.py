"""
Módulo de Estilo y Marca PSLL para Gráficos en Python (Matplotlib / Seaborn)
Paleta oficial: menta / salvia / coral (la que coincide con el emblema PSLL real).

Uso:
    from estilo_graficos import aplicar_estilo_psll, BRAND_COLORS, COLOR_CYCLE, anadir_firma

    aplicar_estilo_psll()
    fig, ax = plt.subplots(figsize=(8, 4.5))
    ax.plot(x, y, color=BRAND_COLORS['primary'], label='Tasa de Paro')
    anadir_firma(ax, fuente="EPA, INE")
"""

import matplotlib.pyplot as plt

BRAND_COLORS = {
    'primary': '#76927A',     # Salvia (serie principal / estructura)
    'secondary': '#E99073',   # Coral (acento, serie destacada)
    'tertiary': '#EDB090',    # Melocotón (acento suave)
    'quaternary': '#566B56',  # Verde profundo (contraste fuerte)
    'support': '#9DBE8F',     # Verde claro de apoyo (5ª serie)
    'ink': '#2F3A30',         # Verde tinta (texto de cuerpo)
    'canvas': '#E1F6EA',      # Menta (lienzo)
    'cream': '#F3EFDC',       # Crema cálido (tarjetas, no fondo de figura completo)
}

# Secuencia ordenada para gráficos multidato (según BRAND.md):
COLOR_CYCLE = ['#76927A', '#E99073', '#EDB090', '#566B56', '#9DBE8F']


def aplicar_estilo_psll():
    """Aplica la configuración de rcParams oficial (paleta menta/salvia/coral) para gráficos PSLL."""
    plt.rcParams.update({
        'figure.facecolor': '#FFFFFF',
        'axes.facecolor': '#FFFFFF',
        'axes.edgecolor': '#C9DCC9',       # borde tenue derivado de la salvia
        'axes.linewidth': 0.8,
        'axes.labelcolor': '#2F3A30',      # verde tinta
        'axes.titlesize': 13,
        'axes.titleweight': 'bold',
        'axes.titlecolor': '#566B56',      # verde profundo
        'axes.prop_cycle': plt.cycler(color=COLOR_CYCLE),
        'text.color': '#2F3A30',
        'xtick.color': '#2F3A30',
        'ytick.color': '#2F3A30',
        'xtick.labelsize': 9.5,
        'ytick.labelsize': 9.5,
        'grid.color': '#C9DCC9',
        'grid.linestyle': '--',
        'grid.linewidth': 0.6,
        'grid.alpha': 0.6,
        'legend.facecolor': '#F3EFDC',     # crema
        'legend.edgecolor': '#C9DCC9',
        'legend.fontsize': 9,
        'font.family': 'sans-serif',
        'font.sans-serif': ['Calibri', 'Arial', 'DejaVu Sans']
    })


def anadir_firma(ax, fuente="EPA, INE", autor="Políticas Sociolaborales (UPO)"):
    """Añade la firma institucional de fuentes y autoría al pie del gráfico."""
    texto = f"Fuente: {fuente} · {autor}"
    ax.figure.text(
        0.01, 0.01, texto,
        ha='left', va='bottom',
        fontsize=8, color='#76927A',       # salvia, discreto
        style='italic'
    )
