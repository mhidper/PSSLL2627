---
name: psll-presentaciones-skill
description: "Usar SIEMPRE que el usuario pida crear, editar o maquetar una presentación, deck, diapositivas (.pptx / .pdf y .html interactivo) para la asignatura Políticas Sociolaborales (PSLL) de la UPO. A partir de la Sesión 12, genera OBLIGATORIAMENTE las presentaciones en DOBLE FORMATO dentro de la carpeta de cada sesión: (1) Formato Clásico (.pptx + .pdf) como Plan B y (2) Formato Web Interactivo (.html) con la paleta PSLL, marca de agua de anillos entrelazados, recorte de prensa fundamental, las 5 fases docentes y gráficos SVG hiper-dinámicos animados por beats."
---

# PSLL · Presentaciones en Doble Formato (`.pptx`/`.pdf` + `.html` Interactivo)

Genera presentaciones de la asignatura **Políticas Sociolaborales y de Empleo (UPO)** con identidad de marca coherente.

> [!IMPORTANT]
> **REGLA DE ORO DEL DOBLE FORMATO OBLIGATORIO (A partir de la Sesión 12):**
> Toda sesión debe generarse simultáneamente en **dos formatos completos e independientes guardados en la carpeta de la sesión** (`Temas EB/Sesiones EB/Sesion XX/`), sin crear portal web externo (`index.html`):
> 1. **Formato 1 (Clásico / Plan B):** Presentación PowerPoint nativa (`Sesion XX - [Título].pptx`) + exportación sincronizada a PDF (`Sesion XX - [Título].pdf`), generada con `python-pptx` y figuras PNG a 300 DPI. No se sustituye nunca por el HTML; se mantiene siempre como Plan B operativo.
> 2. **Formato 2 (Interactivo Hiper-Dinámico):** Presentación web autocontenida en un único archivo (`Sesion XX - [Título].html`), inspirada en el motor técnico de *Economía Aplicada* pero **100% adaptada a la paleta oficial de PSLL**, con **marca de agua vectorial de los anillos entrelazados**, **recorte de prensa fundamental**, las **mismas 5 fases docentes** y **gráficos SVG 100% dinámicos y animados por *beats***.

## Orden de trabajo (obligatorio)

1. **Leer la guía de marca** `assets/BRAND.md` (paleta, tipografías, logos, contraste). Es la fuente de verdad de colores.
2. **Generar el Formato 1 (`.pptx` + `.pdf`)** aplicando la estructura canónica de PSLL y verificando visualmente el PDF.
3. **Generar el Formato 2 (`.html` interactivo)** en la misma carpeta de la sesión (`Temas EB/Sesiones EB/Sesion XX/`), programando todos los gráficos de la sesión como **SVG dinámicos animados por *beats***.

## Paleta oficial (resumen — detalle en BRAND.md y marca/guia_de_estilo.md · Aplica a PPTX, PDF y HTML)

- Fondos claros: blanco puro `#FFFFFF` y menta tenue `#F4F8F5` para tarjetas (borde `#C2D8C9`).
- Fondos oscuros / contraste: verde pino `#113927` o verde salvia `#76927A`, con texto blanco `#FFFFFF`.
- Texto de cuerpo sobre claro: verde tinta `#2F3A30` (nunca salvia sobre blanco ni negro puro).
- Acento: coral dinámico `#E98F71`, para cifras clave, llamadas de atención, bordes de recorte/QR o la onda de políticas.
- Series de datos, en orden: `#113927` (pino), `#76927A` (salvia), `#E98F71` (coral), `#EDB090` (melocotón), `#566B56` (verde intermedio).

## Tipografías

- Titulares: **Outfit** (Bold / Heavy), en sintonía directa con Macroeconomía UPO. Alternativa de respaldo: Inter o Segoe UI.
- Cuerpo: **16 pt Calibri obligatorio** en `.pptx` (tamaño estándar fijado para proyección en aula; no usar tamaños inferiores en párrafos de contenido). Nunca Aptos. En `.html`: `Calibri`, `Inter` o `Work Sans` a escala equivalente ($\ge 19\text{–}22\text{ px}$ sobre lienzo `1600×900`), `Newsreader` / `Georgia` para el recorte de prensa y `JetBrains Mono` / `IBM Plex Mono` para fórmulas y datos.
- Tamaños en diapositivas (.pptx): título 36–44 pt · cabecera de sección 20–24 pt · **cuerpo: 16 pt Calibri** · pie/cita 10–12 pt.

---

# PARTE I · FORMATO 1: PRESENTACIÓN POWERPOINT (`.pptx`) Y PDF (`.pdf`)

## Logos en las diapositivas (carpeta `assets/` y `marca/`)

> [!IMPORTANT]
> **Regla de Oro: Proporciones de Imágenes y Cero Distorsión (*Aspect Ratio Lock*)**
> Bajo ninguna circunstancia se debe estirar, encoger o deformar un logotipo o imagen insertada. Siempre debe preservarse su relación de aspecto (*aspect ratio*) nativa:
> $$\text{Ancho} = \text{Alto} \times \text{Ratio Nativo}$$
> 
> **Dimensiones canónicas y ratios exactos de la marca:**
> - **Escudo UPO (`upo_logo.jpg`):**
>   - Ratio nativo: **0.707** (vertical/alto: $159 \times 225$ px).
>   - Tamaño estándar: **Alto: 0.70"** ($1.78\text{ cm}$) $\times$ **Ancho: 0.495"** ($1.26\text{ cm}$). ¡Nunca fijar anchos arbitrarios como 1.5" que lo conviertan en apaisado!
> - **Logotipo Principal PSLL (`logo_psll_upo.png`):**
>   - Ratio nativo: **1.833** ($2816 \times 1536$ px).
>   - Tamaño estándar portada: Si ancho = $5.00"$, alto = $2.73"$ (o en portadas canónicas: ancho $4.800" \times$ alto $2.618"$). ¡Nunca usar dimensiones cuadradas como 2.6" x 2.6"!
> - **Lockup de esquina (`psll_lockup.png`):**
>   - Ratio nativo: **3.167** ($760 \times 240$ px).
>   - Tamaño estándar en esquinas: Si alto = **0.32"**, ancho = **1.013"** (no 1.30").
> - **Isotipo / Sello (`isotipo_psll_upo.png` o `psll_icon_transparent.svg`):**
>   - Ratio nativo: **1.000** (cuadrado $1024 \times 1024$ px).
>   - Tamaño estándar: ancho = alto.

## Estructura Oficial Canónica de Portada (Modelo Sesión 1 · Obligatorio en PPTX y HTML)

> [!IMPORTANT]
> **Formato Unificado de Portada para TODAS las Presentaciones:**
> A partir de la Sesión 1, todas las presentaciones de la asignatura siguen sin excepción la misma estructura visual, jerarquía y maquetación de portada:
> 
> 1. **Lienzo y Fondo:**
>    - Fondo oscuro corporativo en **Verde Pino PSLL (`#113927`)** sólido o degradado suave de marca.
> 2. **Logotipo Principal de la Asignatura (`logo_psll_upo.png`):**
>    - Protagonista superior centrado horizontalmente en la diapositiva (13.333" de ancho).
>    - Coordenadas: `left = 4.267"`, `top = 0.550"`, `width = 4.800"`, `height = 2.618"` (ratio exacto 1.833).
> 3. **Bloque Textual Central (Alineación Centrada):**
>    - **Línea 1 (Nombre de la Asignatura / Overline):**
>      - Texto: `POLÍTICAS SOCIOLABORALES Y DE EMPLEO`
>      - Posición: `left = 1.000"`, `top = 3.350"`, `width = 11.333"`, `height = 0.600"`.
>      - Estilo: 26 pt, Negrita, Color Blanco Puro `#FFFFFF`. Tipografía institucional (`Outfit` / titular).
>    - **Línea 2 (Título de la Sesión / Tema):**
>      - Texto: `Sesión X – [Título de la Sesión / Epígrafe]`
>      - Posición: `left = 1.000"`, `top = 4.000"`, `width = 11.333"`, `height = 0.500"`.
>      - Estilo: 17 pt, Color Melocotón / Coral Acento (`#EDB090` o `#E98F71`).
>    - **Línea 3 (Metadatos / Fecha / Docencia):**
>      - Texto: `[Día de la semana] [Fecha]  ·  Código 102023  ·  Manuel A. Hidalgo Pérez`
>      - Posición: `left = 1.000"`, `top = 4.550"`, `width = 11.333"`, `height = 0.400"`.
>      - Estilo: 12 pt, Color Blanco Hueso / Arena Tenue (`#F3EFDC` o `#F4F8F5`).
> 4. **Franja Inferior Institucional (Footer Band):**
>    - Rectángulo de fondo blanco puro (`#FFFFFF`): `left = 0.000"`, `top = 6.600"`, `width = 13.333"`, `height = 0.900"`.
>    - **Escudo UPO (`upo_logo.jpg`):** `left = 0.500"`, `top = 6.700"`, `width = 0.495"`, `height = 0.700"` (ratio vertical 0.707).
>    - **Texto Institucional del Título / Grado:**
>      - Texto: `Grado en Relaciones Laborales y Recursos Humanos · Doble Grado en Derecho y RRLL-RRHH`
>      - Posición: `left = 1.300"`, `top = 6.850"`, `width = 11.300"`, `height = 0.400"`.
>      - Estilo: 10 pt, Color Verde Tinta `#2F3A30`.

- **Divisores de sección:** fondo verde pino o salvia, número y título de bloque en blanco, `psll_icon_transparent.svg` pequeño como sello cuadrado.
- **Diapositivas de contenido:** `psll_lockup.png` (símbolo de anillos + "PSLL") pequeño en una esquina superior (alto = 0.32", ancho = 1.01"), discreto.
- **Cierre / contraportada:** síntesis + datos de contacto + logo **UPO** institucional vertical + logotipo PSLL en ratio 1.833.
- Respetar el área de protección de la UPO: no recolorear, no deformar, no integrarlo en el pastel.

## Estructura Oficial de un Deck PSLL (Sesiones EB · Metodología en 5 Fases · Común a PPTX y HTML)

Todas las presentaciones de la asignatura siguen la secuencia pedagógica de innovación docente en 5 bloques:

1. **Portada Oficial Unificada (Slide 1):** Lienzo Verde Pino (`#113927`), logotipo PSLL en ratio 1.833 centrado arriba, bloque tipográfico institucional (26 pt Blanco / 17 pt Melocotón / 12 pt Crema) y franja inferior blanca con escudo vertical UPO (0.707).
2. **Hoja de Ruta de la Sesión (Slide 2):** Bloques de la sesión con sus tiempos previstos (120 min).
3. **Bloque 1 · Apertura, Gancho con Recorte de Prensa y Sondeo Previo (00–20 min):**
   - **Recorte de prensa real fundamental** de actualidad sociolaboral / económica reciente como disparador del choque intelectual, acompañado del planteamiento de los 2 enigmas de la sesión.
   - Código QR de **Microsoft Forms** para votación diagnóstica en vivo desde el móvil.
   - Gráficos oficiales (EPA, Eurostat, OCDE, Seguridad Social, AIReF) que desmienten el prejuicio popular.
4. **Bloques 2 y 3 · Mini-Lecciones Quirúrgicas Conceptuales y Analíticas (20–70 min):**
   - Desarrollo teórico con figuras oficiales numeradas, fórmulas clave, ejemplos cuantitativos y análisis institucional.
   - Párrafos desarrollados en **16 pt Calibri obligatorio** (prohibidas las slides solo-texto).
5. **Bloque 4 · Taller Práctico Individual con Micro-Apps (70–85 min · 15 min):**
   - Actividad interactiva **individual desde el teléfono móvil** (15 min) en rol de *Analista de Empleo*, guiada paso a paso por la propia app (`https://mhidper.github.io/micro_apps/`).
   - Slide con **código QR oficial en alta resolución (Verde Pino `#113927`) de acceso directo a la micro-app** específica de la sesión.
6. **Bloque 5 · Reto Individual de Cierre y Gamificación (85–120 min · Regla de Oro):**
   - **Slide de Reto (10 min):** Pregunta **100% basada en lo explicado en clase y el material previo**, redactada **a mano en papel** en entorno sin pantallas.
   - **Slide de Subida con QR (2 min):** Código QR de Microsoft Forms (cuenta UPO) para fotografiar y subir la hoja manuscrita. Las entregas acumulan puntos en el **Pasaporte de Evaluación Continua** canjeables para el examen final (70%).
   - **Slide de Solución y Rúbrica (5 min):** Criterios de corrección proyectados para feedback formativo inmediato.
7. **Cierre:** Conclusiones clave + adelanto de la siguiente sesión.

## Consolidación de Estilos en `.pptx` (Actualización 2026-27)

### 1. Rigor Analítico y Formulación Matemática
- **Subíndices Reales Obligatorios:** Prohibido escribir subíndices como texto plano sin formato. En PowerPoint, activar siempre el atributo nativo de subíndice (`run.font.subscript = True`) para cada índice o etiqueta ($C = w(T-L) + Y_{\text{NS}}$, $PMg_L$, $w_R$).
- **Símbolos Tipográficos Homologados:** Utilizar caracteres matemáticos formales en lugar de aproximaciones ASCII: `≥` (`\u2265`), `≤` (`\u2264`), `τ` (`\u03C4`), `∂` (`\u2202`), `·` (`\u00B7`), `➔` (`\u2794`).

### 2. Checkpoints Interactivos con Códigos QR (Doble Columna)
- El QR debe ser estrictamente cuadrado (1:1, ej. $2.70" \times 2.70"$ o $2.05" \times 2.05"$), generado en **Verde Pino PSLL (`#113927`)** sobre fondo blanco puro con nivel H de corrección, dejando espacio de respiración vertical con la URL inferior.

### 3. Gestión Técnica de Diapositivas OpenXML (.pptx)
- Al limpiar, editar o reconstruir diapositivas existentes con scripts Python (`python-pptx`), inspeccionar directamente los nodos hijos de `slide._element.spTree` para eliminar cualquier nodo `mc:AlternateContent` o capa fantasma.

---

# PARTE II · FORMATO 2: PRESENTACIÓN WEB INTERACTIVA (`.html`) CON GRÁFICOS SVG HIPER-DINÁMICOS

Además del `.pptx` y `.pdf`, cada sesión incluye obligatoriamente un archivo `Sesion XX - [Título].html` en la misma carpeta `Temas EB/Sesiones EB/Sesion XX/`, construido bajo la arquitectura técnica de presentación web autocontenida:

## 1. Escenario 16:9 Fijo (`1600×900 px`), Paleta PSLL y Marca de Agua de Anillos Entrelazados

1. **Lienzo 16:9 Autoescalable (`#vp.viewport > #stage.stage`):**
   - El contenedor `#stage` tiene dimensiones fijas de `1600px × 900px` y se escala dinámicamente con `transform: scale(...)` mediante un listener `resize` para ajustarse a cualquier proyector o monitor manteniendo intactas todas las proporciones.
2. **Paleta Corporativa PSLL (Idéntica al `.pptx` y `.pdf`):**
   - Variables CSS en `:root`:
     - `--psll-bg: #FFFFFF` (lienzo base luminoso).
     - `--psll-mint: #F4F8F5` y `--psll-mint-border: #C2D8C9` (tarjetas de contenido con sombra suave y `backdrop-filter: blur(6px)`).
     - `--psll-pine: #113927` y `--psll-pine-dark: #0B2419` (portada, titulares, serie primaria y acentos de autoridad).
     - `--psll-sage: #76927A` (subtítulos, etiquetas de fase, serie estructural).
     - `--psll-coral: #E98F71` y `--psll-coral-dark: #C86D51` (acento dinámico, alertas, serie de choque/reforma, onda transversal).
     - `--psll-peach: #EDB090` (serie complementaria).
     - `--psll-ink: #2F3A30` (texto de lectura).
3. **Marca de Agua Vectorial Fija: Los Anillos Entrelazados de PSLL (`#stage > .watermark-layer`):**
   - Ubicada como hijo directo de `#stage` (`position: absolute; inset: 0; z-index: 1; pointer-events: none; overflow: hidden`).
   - Renderiza en SVG vectorial de alta precisión el **emblema oficial de los dos anillos entrelazados** (Anillo Izquierdo en Verde Pino `#113927` y Anillo Derecho en Verde Salvia `#76927A`) **atravesados por la onda aerodinámica transversal en Coral (`#E98F71`)**, junto con una retícula geométrica ultra-tenue (`opacity: 0.045–0.055`).
   - Las diapositivas de contenido (`section.slide`) tienen `z-index: 2` y `background: transparent` (mientras las tarjetas `.card` usan `rgba(244, 248, 245, 0.88)`), haciendo que los anillos entrelazados acompañen sutilmente toda la presentación.

## 2. Recorte de Prensa Fundamental (`.newspaper-card`) e Hilo Conductor

- En la **Fase 1 (Apertura con Gancho)**, la noticia real disparadora se maqueta como un **recorte de prensa económica auténtico (`.newspaper-card`)**:
  - Cabecera del periódico (`.news-masthead`) con nombre del medio (*Cinco Días · El País Economía · Expansión*), fecha, sección y firma.
  - Titular periodístico en tipografía serif editorial (`Newsreader` / `Georgia`), entradilla (`.news-subhead`), texto en columnas periodísticas (`.news-columns`) y tarjetas de datos clave (`.news-kpi-box`) con borde izquierdo en Coral `#E98F71`.
- En las diapositivas de las **Fases 2 y 3**, cuando un modelo teórico o gráfico empírico responde a los enigmas de la noticia inicial, se incluye la insignia `.news-thread-badge` (`📰 CONEXIÓN CON EL DEBATE DE APERTURA`).

## 3. Motor de *Beats* (Fragmentos Reversibles) y Controles de Aula

- **Navegación Reversible por *Beats*:**
  - Los elementos con clase `.frag` (tarjetas secuenciales, pasos de demostración, barras animadas `.frag-bar`, tramos de gráficos SVG, revelación del sondeo `.quiz-opt`) aparecen progresivamente al avanzar (`ArrowRight`, `Space`, `PageDown`, clic) con `nextFrag()` y se repliegan en orden inverso al retroceder (`ArrowLeft`, `PageUp`, `Backspace`) con `prevFrag()`.
- **Sondeo en Directo Dual (QR + Quiz Interactivo en Pantalla):**
  - La diapositiva del Sondeo Previo muestra simultáneamente el **Código QR cuadrado de Microsoft Forms** (para que los alumnos voten desde el móvil) y las **opciones interactivas `.quiz-opt`** en pantalla que, al avanzar el *beat* tras cerrar la votación, iluminan la respuesta correcta (`.revealed-right` en Verde Pino/Esmeralda) y desmienten los mitos (`.revealed-wrong` en Coral/Rojo).
- **HUD Docente y Notas del Orador (`N`):**
  - Barra de progreso inferior, contador de diapositivas, botones `‹` `›`, pantalla completa (`F`) y ventana flotante de **Notas del Orador** (`N`) alimentada por el atributo `data-notes` de cada `<section class="slide">`.

## 4. Gráficos SVG Hiper-Dinámicos y Animados al Máximo

> [!IMPORTANT]
> **Directriz de Máximo Dinamismo Gráfico en HTML:**
> En el archivo `.html`, todos los gráficos de la sesión deben construirse como **escenas SVG interactivas y animadas en vivo mediante JavaScript (`tween`, `requestAnimationFrame`, `stroke-dashoffset`, `cubic-bezier`)**:
> - **Curvas y series temporales multi-etapa:** Trazado progresivo de las series temporales (ej. caída histórica de la temporalidad tras el RDL 32/2021, evolución de indefinidos y fijos discontinuos, escalones de indemnización por despido de 12, 20, 33 y 45 días) con sombreado dinámico de zonas de reforma, puntos de choque con halo pulsante (`<circle>` animado) y etiquetas emergentes sincronizadas con cada *beat*.
> - **Comparativas internacionales OCDE/UE animadas:** Gráficos de barras / *lollipops* donde cada barra crece suavemente desde $0$ hasta su valor real (`tween` o transición CSS disparada por el *beat*), destacando a España en Coral `#E98F71` y Verde Pino `#113927` frente a la media OCDE/UE, con líneas de umbral animadas.
> - **Contadores numéricos animados (`.bignum[data-target]`):** Todas las grandes magnitudes macroeconómicas o sociolaborales cuentan dinámicamente desde $0$ hasta el dato final al entrar en la diapositiva o activar su *beat*.
> - **Esquemas institucionales y diagramas causales vivos:** Matrices comparativas (ej. *Triángulo de Oro de la Flexiseguridad Danesa* frente al *Círculo Vicioso de la Dualidad Española*) con conectores vectoriales animados (`stroke-dasharray` con flujo continuo) que se iluminan paso a paso conforme avanza la explicación.
