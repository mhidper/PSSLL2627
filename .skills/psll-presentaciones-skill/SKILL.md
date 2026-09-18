---
name: psll-presentaciones
description: "Usar SIEMPRE que el usuario pida crear, editar o maquetar una presentación, deck, diapositivas o .pptx para la asignatura Políticas Sociolaborales (PSLL) de la UPO. Activar ante términos como 'presentación', 'diapositivas', 'slides', 'deck', 'transparencias', 'PowerPoint' en el contexto de PSLL, de cualquiera de sus temas (mercado de trabajo, políticas activas/pasivas de empleo, flexibilidad, pensiones, EPL, etc.), o cuando se mencione el emblema PSLL. Esta skill aplica la identidad visual PSLL (paleta, tipografías, logos, motivo) sobre la mecánica de generación de .pptx."
---

# PSLL · Presentaciones

Genera presentaciones de la asignatura **Políticas Sociolaborales (UPO)** con identidad de marca coherente. Esta skill **NO** sustituye a la skill `pptx`: aporta la capa de marca; la mecánica (crear, renderizar, QA) se ejecuta con `pptx`.

## Orden de trabajo (obligatorio)

1. **Leer la guía de marca** `assets/BRAND.md` (paleta, tipografías, logos, contraste). Es la fuente de verdad de colores.
2. **Leer la skill `pptx`** (`/mnt/skills/public/pptx/SKILL.md`) y, para crear desde cero, su `pptxgenjs.md`. Toda la generación, conversión a imagen y QA visual sigue esa skill.
3. Aplicar la marca PSLL descrita aquí.
4. **QA visual con subagente** (según la skill `pptx`) antes de entregar.

## Paleta oficial (resumen — detalle en BRAND.md y marca/guia_de_estilo.md)

- Fondos claros: blanco puro `#FFFFFF` y menta tenue `#F4F8F5` para tarjetas.
- Fondos oscuros / contraste: verde pino `#113927` o verde salvia `#76927A`, con texto blanco.
- Texto de cuerpo sobre claro: verde tinta `#2F3A30` (nunca salvia sobre blanco ni negro puro).
- Acento: coral dinámico `#E98F71`, solo para cifras clave, una palabra destacada o la onda de políticas.
- Series de datos, en orden: `#113927` (pino), `#76927A` (salvia), `#E98F71` (coral), `#EDB090` (melocotón), `#566B56` (verde intermedio).

## Tipografías

- Titulares: **Outfit** (Bold / Heavy), en sintonía directa con Macroeconomía UPO. Alternativa de respaldo: Inter o Segoe UI.
- Cuerpo: **16 pt Calibri obligatorio** (tamaño estándar fijado para proyección en aula; no usar tamaños inferiores en párrafos de contenido). Nunca Aptos.
- Tamaños en diapositivas (.pptx): título 36–44 pt · cabecera de sección 20–24 pt · **cuerpo: 16 pt Calibri** · pie/cita 10–12 pt.

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
>   - Tamaño estándar portada: Si ancho = $5.00"$, alto = $2.73"$ (o en portadas grandes: ancho $5.89" \times$ alto $3.20"$). ¡Nunca usar dimensiones cuadradas como 2.6" x 2.6"!
> - **Lockup de esquina (`psll_lockup.png`):**
>   - Ratio nativo: **3.167** ($760 \times 240$ px).
>   - Tamaño estándar en esquinas: Si alto = **0.32"**, ancho = **1.013"** (no 1.30").
> - **Isotipo / Sello (`isotipo_psll_upo.png` o `psll_icon_transparent.svg`):**
>   - Ratio nativo: **1.000** (cuadrado $1024 \times 1024$ px).
>   - Tamaño estándar: ancho = alto.

## Estructura Oficial Canónica de Portada (Modelo Sesión 1 · Obligatorio)

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

## Motivo y composición

- Repetir el **motivo de líneas orgánicas** muy tenues (un tono más oscuro que el fondo) como textura sutil en portada y divisores. Nunca sobre zonas de texto.
- Esquinas redondeadas en tarjetas y bloques (radio ~8–12 pt).
- Iconos en círculos de color de marca junto a cabeceras de sección.
- **Prohibido** (heredado de la skill pptx y reforzado aquí): líneas/subrayados bajo los títulos, barras o franjas de color decorativas en bordes, y diapositivas solo-texto. Cada diapositiva lleva un elemento visual.

## Estructura Oficial de un Deck PSLL (Sesiones EB · Metodología en 5 Fases)

Todas las presentaciones de la asignatura siguen la secuencia pedagógica de innovación docente en 5 bloques:

1. **Portada Oficial Unificada (Slide 1):** Lienzo Verde Pino (`#113927`), logotipo PSLL en ratio 1.833 centrado arriba, bloque tipográfico institucional (26 pt Blanco / 17 pt Melocotón / 12 pt Crema) y franja inferior blanca con escudo vertical UPO (0.707).
2. **Hoja de Ruta de la Sesión (Slide 2):** Bloques de la sesión con sus tiempos previstos (120 min).
3. **Bloque 1 · Apertura, Gancho y Sondeo Previo (00–20 min):**
   - Noticia real de prensa sociolaboral / económica reciente como disparador del choque intelectual.
   - Código QR de **Microsoft Forms** para votación diagnóstica en vivo desde el móvil.
   - Gráficos oficiales (EPA, Eurostat, OCDE) a 300 DPI (ej. PIB pc vs SMI en la UE) que desmienten el prejuicio popular.
4. **Bloques 2 y 3 · Mini-Lecciones Quirúrgicas Conceptuales (20–70 min):**
   - Desarrollo teórico con figuras oficiales numeradas, fórmulas clave y análisis institucional.
   - Párrafos desarrollados en **16 pt Calibri obligatorio** (prohibidas las slides solo-texto).
5. **Bloque 4 · Taller Práctico Individual con Micro-Apps (70–85 min · 15 min):**
   - Actividad interactiva **individual desde el teléfono móvil** (15 min) en rol de *Analista de Empleo*, guiada paso a paso por la propia app (`https://mhidper.github.io/micro_apps/`).
   - Slide con **código QR oficial en alta resolución (Verde Pino `#113927`) de acceso directo a la micro-app** específica de la sesión (ej. *Simulador CLU*, *PIB Real vs Nominal*, *Balanza de Protección Social*, etc.).
6. **Bloque 5 · Reto Individual de Cierre y Gamificación (85–120 min · Regla de Oro):**
   - **Slide de Reto (10 min):** Pregunta **100% basada en lo explicado en clase y el material previo**, redactada **a mano en papel** en entorno sin pantallas.
   - **Slide de Subida con QR (2 min):** Código QR de Microsoft Forms (cuenta UPO) para fotografiar y subir la hoja manuscrita. Las entregas acumulan puntos canjeables para el examen final (70%).
   - **Slide de Solución y Rúbrica (5 min):** Criterios de corrección proyectados para feedback formativo inmediato.
7. **Cierre:** Conclusiones clave + adelanto de la siguiente sesión (enlace al aula invertida / píldora previa).

## Comprobaciones antes de entregar

- Contraste de todo el texto (cuerpo en tinta/blanco, nunca salvia sobre menta).
- Logo UPO presente en material oficial y sin deformar.
- Coral usado solo como acento.
- QA visual con subagente (skill pptx). Corregir desbordes/solapes y entregar.

## Consolidación de Estilos y Estándares Avanzados (Actualización 2026-27)

### 1. Rigor Analítico y Formulación Matemática
- **Subíndices Reales Obligatorios:** Prohibido escribir subíndices como texto plano sin formato (ej. `wR`, `Y_NS`, `PMgL`, `w_neto`). En PowerPoint, activar siempre el atributo nativo de subíndice (`run.font.subscript = True`) para cada índice o etiqueta ($C = w(T-L) + Y_{\text{NS}}$, $PMg_L$, $w_R$).
- **Símbolos Tipográficos Homologados:** Utilizar caracteres matemáticos formales en lugar de aproximaciones ASCII: `≥` (`\u2265`), `≤` (`\u2264`), `τ` (`\u03C4`), `∂` (`\u2202`), `·` (`\u00B7`), `➔` (`\u2794`).

### 2. Checkpoints Interactivos con Códigos QR (Doble Columna)
- Además del QR del Laboratorio Activo (Bloque 4) y de Subida Forms (Bloque 5), pueden incluirse **puntos de control interactivo (*checkpoints*) con cuestionarios rápidos en mini-lecciones conceptuales** (ej. Cuestionario de Salario de Reserva en Bloque 2).
- **Estructura visual de 2 columnas:**
  - **Tarjeta Izquierda (`#F4F8F5`, borde `#76927A`):** Formalización analítica del concepto, condiciones matemáticas y papel de las políticas públicas.
  - **Tarjeta Derecha (`#F4F8F5`, borde `#E98F71`):** Llamada a la acción destacada en coral, instrucciones breves del reto (5 min), código QR oficial centrado en la mitad inferior y enlace web directo en el pie.
- **Aspect Ratio y Espaciado de Códigos QR:**
  - El QR debe ser estrictamente cuadrado (1:1, ej. $2.05" \times 2.05"$), generado en **Verde Pino PSLL (`#113927`)** sobre fondo blanco puro con nivel H de corrección.
  - Dejar espacio de respiración (*breathing room*) vertical entre el texto de instrucciones, la parte superior del QR y la caja de texto inferior de la URL para garantizar cero colisiones visuales.

### 3. Integración de Figuras Oficiales Numeradas
- Las figuras de los apuntes oficiales maquetados (ej. Figura 1.6 de apuntes) deben insertarse en alta resolución (300 DPI), con la paleta de marca y acompañadas de un panel analítico lateral con viñetas estructuradas que desglosen los equilibrios, desplazamientos y rigideces institucionales.

### 4. Gestión Técnica de Diapositivas OpenXML (.pptx)
- Al limpiar, editar o reconstruir diapositivas existentes con scripts Python (`python-pptx`), inspeccionar directamente los nodos hijos de `slide._element.spTree`.
- **Eliminación de formas fantasma:** `python-pptx` no siempre lista elementos envueltos en `mc:AlternateContent` o formas agrupadas en `slide.shapes`. Deben eliminarse explícitamente del árbol XML para evitar que capas previas queden renderizadas como marcas de agua o solapamientos no deseados tras las nuevas tarjetas.
