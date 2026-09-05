---
name: marca_psll
description: Guía de identidad visual, estilo y maquetación de marca para la asignatura Políticas Sociolaborales y de Empleo (PSLL - UPO). Aplica OBLIGATORIAMENTE siempre que el usuario solicite crear, editar, actualizar o generar: documentos (.docx, apuntes, lecturas, guías), presentaciones (.pptx, diapositivas, slides) o figuras/gráficos analíticos (Python, Matplotlib, Seaborn). Garantiza la aplicación consistente de la paleta cálida crema/ladrillo/terracota, tipografías, jerarquías visuales y formatos de publicación.
---

# Habilidad: Identidad Visual y Marca PSLL (Docencia UPO)

> [!IMPORTANT]
> **Condición de Activación Obligatoria:**
> Esta habilidad debe activarse e implementarse de forma rigurosa **siempre** que se genere o modifique cualquier material para la asignatura:
> 1. **Documentos y Apuntes:** Archivos `.docx`, guías didácticas, lecturas complementarias y documentos en Markdown.
> 2. **Presentaciones:** Diapositivas en `.pptx` de cualquiera de los temas de la asignatura.
> 3. **Figuras y Gráficos:** Cualquier script o gráfico generado con Python (`matplotlib`, `seaborn`, etc.) para ilustrar datos del mercado de trabajo.

---

## 1. Paleta de Colores de Marca (Identidad Cálida Substack/Editorial)

Toda la identidad gráfica de la asignatura se fundamenta en una estética editorial cálida, elegante y reposada, inspirada en tonos crema, terracota, arcilla y rojo ladrillo.

### Tabla Maestra de Colores (HEX)

| Rol | Nombre | HEX | Aplicación Principal |
| :--- | :--- | :--- | :--- |
| **Lienzo Principal** | Crema suave | `#FDFBF7` | Fondos de página, fondo principal de figuras y diapositivas claras |
| **Lienzo Secundario** | Crema oscuro / Arena | `#FAF6F0` | Cajas destacadas, ejes de gráficos, tarjetas, fondos de leyenda |
| **Bordes / Líneas** | Marrón claro sutil | `#E3DCD2` | Rejillas de gráficos (*grids*), bordes de cajas, separadores de tablas |
| **Texto de Cuerpo** | Café / Marrón oscuro | `#4A3B32` | Todo el texto de lectura principal (sustituye al negro puro `#000000`) |
| **Texto de Título** | Tinta oscura profunda | `#2F241D` | Títulos principales (H1) en documentos y portadas |
| **Color Primario (Acento)**| Rojo ladrillo profundo | `#A33327` | Encabezados de sección (H2), línea principal de gráficos, llamadas de atención |
| **Color Secundario** | Terracota cálido | `#D47B5A` | Subtítulos (H3), segunda serie en gráficos, barras secundarias |
| **Color Terciario** | Ámbar / Arcilla | `#C68B59` | Tercera serie de datos, categorías intermedias, iconos |
| **Color Cuaternario** | Salmón / Rojo pastel | `#E3ACA1` | Cuarta serie de datos, zonas sombreadas o intervalos de confianza |
| **Contraste Intenso** | Marrón rojizo oscuro | `#5C2317` | Máximo resalte, puntos singulares, líneas de tendencia clave |
| **Atenuado / Muted** | Marrón grisáceo tenue | `#A49080` | Etiquetas secundarias, notas al pie, texto de fuentes, líneas base |

### Reglas Críticas de Color
- **PROHIBIDO el negro puro `#000000`:** En su lugar se utiliza `#4A3B32` para cuerpo y `#2F241D` para grandes titulares. Esto genera una lectura visualmente orgánica y descansada.
- **PROHIBIDO el blanco clínico `#FFFFFF` a sangre completa:** Los fondos son `#FDFBF7`. Solo se permite blanco puro como relleno de tarjetas aisladas si el fondo es `#FAF6F0`.
- **Uso estricto del Rojo Ladrillo `#A33327`:** Es el color de mayor peso visual; no saturar con él párrafos enteros. Úsalo en titulares, números clave o la serie de datos protagonista.

---

## 2. Tipografías Oficiales

La combinación tipográfica busca máxima legibilidad, modernidad y compatibilidad universal en equipos Windows / Office:

1. **Titulares y Encabezados (H1, H2, títulos de slides, títulos de gráficos):**
   - **Preferencia principal:** `Poppins` (Bold / SemiBold) o `Inter`.
   - **Alternativa universal Office (sin instalación previa):** `Century Gothic`, `Calibri` (Bold) o `Cambria` (Bold).
2. **Cuerpo de Texto y Datos (Párrafos, tablas, ejes de coordenadas, leyendas):**
   - **Preferencia principal:** `Calibri` o `Arial` (Regular, 10.5–11.5 pt para texto, 9–10 pt para tablas y gráficos).
   - **Alternativa formal académica:** `Century Schoolbook` o `Cambria`.
3. **PROHIBICIÓN:** Nunca utilizar la fuente `Aptos` por defecto si genera inconsistencias entre versiones de Office.

---

## 3. Generación de Gráficos y Figuras (Python / Matplotlib / Seaborn)

Cualquier gráfico generado para la asignatura (tasas de desempleo, curvas de Beveridge, salarios, pensiones, etc.) DEBE inyectar y aplicar estrictamente el siguiente bloque estándar:

```python
import matplotlib.pyplot as plt

# 1. Configuración de estilo global
plt.rcParams.update({
    'figure.facecolor': '#FDFBF7',  # Crema suave
    'axes.facecolor': '#FAF6F0',    # Crema más oscuro / cálido
    'axes.edgecolor': '#E3DCD2',    # Borde tenue
    'axes.linewidth': 0.8,
    'axes.labelcolor': '#4A3B32',   # Marrón café para etiquetas de ejes
    'axes.titlesize': 13,
    'axes.titleweight': 'bold',
    'axes.titlecolor': '#2F241D',   # Título del gráfico
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

# 2. Diccionario oficial de colores para series de datos
BRAND_COLORS = {
    'primary': '#A33327',     # 1ª Serie (Rojo ladrillo profundo)
    'secondary': '#D47B5A',   # 2ª Serie (Terracota cálido)
    'tertiary': '#C68B59',    # 3ª Serie (Ámbar / arcilla)
    'quaternary': '#E3ACA1',  # 4ª Serie (Rojo pastel)
    'highlight': '#5C2317',   # Énfasis especial / máximo
    'muted': '#A49080'        # Serie de fondo o comparación pasiva
}

# Secuencia ordenada para gráficos multidato:
COLOR_CYCLE = ['#A33327', '#D47B5A', '#C68B59', '#5C2317', '#E3ACA1', '#A49080']
```

### Reglas de Presentación de Figuras
1. **Pie de Autoría y Fuentes (OBLIGATORIO):**
   Toda figura debe incluir en la esquina inferior izquierda o derecha, en tamaño 8-8.5 pt y color `#A49080`:
   `Fuente: [INE / EPA / Eurostat / SEPE] · Políticas Sociolaborales (UPO) / Elaboración propia @manujhidalgo`
2. **Formato y Guardado:**
   - Exportar con `dpi=300`, `bbox_inches='tight'`.
   - Guardar en formato `.png`.

---

## 4. Estilo de Documentos de Texto (Word `.docx` / Markdown)

Al redactar o maquetar apuntes, lecturas o casos prácticos:

### Jerarquía Visual
- **Título del Documento (Title / H1):** 22–26 pt, Bold, color `#2F241D` (Tinta profunda).
- **Encabezado 1 (H2 - Apartados principales):** 15–17 pt, Bold, color `#A33327` (Rojo ladrillo). Con espacio anterior de 12 pt y posterior de 4 pt.
- **Encabezado 2 (H3 - Subapartados):** 12.5–13.5 pt, Bold, color `#D47B5A` (Terracota).
- **Cuerpo de texto:** 10.5–11 pt, interlineado 1.15, espacio posterior de 4–6 pt, color `#4A3B32`.
- **Cajas de texto destacadas (Callouts / Casos / Paradojas):**
  - Fondo: Crema oscuro `#FAF6F0`.
  - Borde izquierdo grueso: 3 pt en color `#A33327`.
  - Texto interior: `#4A3B32` con título en negrita `#A33327`.

### Tablas de Datos
- **Fila de cabecera:** Fondo `#A33327` con texto en blanco `#FFFFFF` (o fondo `#FAF6F0` con texto en negrita `#2F241D` y borde inferior marcado `#A33327`).
- **Filas alternas:** Fondo `#FDFBF7` y `#FAF6F0` (cebreado sutil).
- **Bordes interiores:** Líneas horizontales finas en color `#E3DCD2`. Sin líneas verticales pesadas.
- **Alineación:** Texto a la izquierda, números y porcentajes a la derecha.

---

## 5. Estilo de Presentaciones (`.pptx` / Diapositivas)

Al generar o modificar diapositivas para las clases (EB y EPD):

1. **Fondo de Diapositivas:**
   - **Diapositivas de contenido:** Fondo `#FDFBF7`.
   - **Portadas y Divisores de bloque:** Dos opciones elegantes:
     - *Opción A (Impacto cálido):* Fondo `#A33327` (Ladrillo profundo) con tipografía en `#FDFBF7` y `#FAF6F0`.
     - *Opción B (Lienzo claro):* Fondo `#FDFBF7` con tarjeta central `#FAF6F0` y tipografía `#A33327`.
2. **Estructura del Slide:**
   - **Título de la diapositiva:** 28–34 pt, color `#A33327` o `#2F241D`, alineado a la izquierda.
   - **Contenido:** Priorizar bloques visuales, esquemas, cifras de gran tamaño (36–48 pt en coral/ladrillo) y párrafos analíticos frente a listas interminables de viñetas.
   - **Tarjetas y contenedores:** Fondo `#FAF6F0` con esquinas ligeramente redondeadas y borde tenue `#E3DCD2`.
3. **Uso de Logos Institucionales:**
   - **Emblema PSLL:** En portada y contraportada.
   - **Logo UPO (`upo_logo.jpg`):** Discreto en esquina inferior o contraportada sobre fondo claro, respetando su área de protección sin deformación ni recoloreado.

---

## 6. Lista de Comprobación (QA de Marca)

Antes de entregar cualquier documento, presentación o figura, verifica:
- [ ] ¿Se ha utilizado la paleta cálida (fondo `#FDFBF7`, primario `#A33327`, secundario `#D47B5A`)?
- [ ] ¿Se ha evitado el negro puro (`#000000`) sustituyéndolo por café oscuro (`#4A3B32`)?
- [ ] ¿Las figuras de Matplotlib tienen los `rcParams` actualizados y la firma de fuente/autoría?
- [ ] ¿Las tablas tienen el formato editorial limpio con bordes `#E3DCD2`?
- [ ] ¿Las tipografías son coherentes con las directrices (Poppins / Century Gothic / Calibri)?
