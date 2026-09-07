---
name: psll-apuntes-skill
description: Motor de maquetación y diseño editorial de apuntes y documentos docentes (.docx) para Políticas Sociolaborales (PSLL 2026-27). Aplica la paleta oficial (menta/salvia/coral), tipografías Poppins/Calibri, cajas destacadas (callouts), tablas estilizadas y figuras de alta resolución en matplotlib.
---

# Skill: Maquetación y Formato de Apuntes (PSLL)

Esta skill define y automatiza los estándares visuales y editoriales para los documentos de apuntes (`.docx`) de la asignatura **Políticas Sociolaborales y de Empleo (PSLL · Código 102023)** en la Universidad Pablo de Olavide (UPO).

---

## 🎨 Principios de Diseño Editorial (Brand Identity)

Basado estrictamente en [Logos y skills/BRAND.md](file:///c:/Users/Usuario/Dropbox/DOCENCIA%20UPO/CURSO%2026-27/PSLL/Logos%20y%20skills/BRAND.md):

| Elemento | Configuración | Código / Valor |
| :--- | :--- | :--- |
| **Lienzo / Fondos destacados** | Verde menta | `#E1F6EA` |
| **Estructura y H2** | Verde salvia | `#76927A` |
| **Títulos principales y H1** | Verde profundo | `#566B56` |
| **Texto de lectura** | Verde tinta (nunca negro puro) | `#2F3A30` |
| **Acentos y alertas** | Coral | `#E99073` |
| **Acentos secundarios** | Melocotón | `#EDB090` |
| **Fondos alternativos cajas** | Neutro cálido / Crema | `#F3EFDC` |
| **Tipografía Titulares** | Poppins (alternativa: Century Schoolbook/Cambria) | 24 pt (Título), 16 pt (H1), 13 pt (H2), 11 pt (H3) |
| **Tipografía Cuerpo** | Calibri | 10.5 pt, interlineado 1.15, espacio posterior 4.5 pt, **texto justificado** |
| **Márgenes de página** | Estándar institucional | Superior/Inferior 2.5 cm, Izquierdo/Derecho 2.5 cm |

---

## 🧩 Componentes Modulares Soportados

1. **Jerarquía Tipográfica y Organización Visual de Secciones:**
   - Detección y normalización automática de epígrafes (`1.`, `1.1.`, `1.2.1.`).
   - Aplicación estricta de `Heading 1` (15.5 pt en verde profundo), `Heading 2` (12.5 pt en salvia) y `Heading 3` (11 pt en verde profundo) alineados a la izquierda para navegación en Word.
   - **Espaciado Generoso entre Secciones:** Para garantizar la respiración y una organización visual diáfana, se establecen márgenes previos amplios:
     - `Heading 1`: 26 pt antes / 6 pt después (`keep_with_next = True`).
     - `Heading 2`: 18 pt antes / 5 pt después (`keep_with_next = True`).
     - `Heading 3`: 12 pt antes / 3 pt después (`keep_with_next = True`).
   - **Alineación Justificada Obligatoria:** Todo el texto de cuerpo, listas y cajas destacadas debe estar justificado (`WD_ALIGN_PARAGRAPH.JUSTIFY`) para garantizar un acabado editorial limpio.

2. **Itemización Sistemática con Viñetas (Bullet Points):**
   - Detección automática y conversión de listas de factores, enumeraciones de características y requisitos en listas itemizadas con viñetas reales (`• `).
   - Formato de viñeta corporativo:
     - Símbolo `• ` en Verde Salvia (`#76927A`) negrita.
     - Sangría francesa / colgante: `left_indent = 0.35 pulgadas` (~0.9 cm), `first_line_indent = -0.18 pulgadas`.
     - Término o etiqueta clave en negrita Verde Profundo (`#566B56`) antes de dos puntos.
     - Texto explicativo justificado en Verde Tinta (`#2F3A30`).

3. **Cajas Destacadas (*Callout Boxes*):**
   - Tabla unificada de 1 celda con fondo temático, borde izquierdo grueso de 3 pt (26 dxa), padding interior calibrado y título en negrita con icono temático:
     - 🗓️ **Caja de Sesión Docente (*Session Box*):** Fondo verde menta suave (`#E1F6EA`), borde en Verde Profundo (`#566B56`). Sitúa al estudiante en el cronograma oficial de la asignatura (ej. *Sesión 1 · Semana 1*).
     - 💭 **Parada Reflexiva (*Reflection Box*):** Fondo neutro cálido/crema suave (`#F3EFDC`), borde en Verde Salvia (`#76927A`). Preguntas detonantes y dilemas intuitivos para que el estudiante auto-evalúe su comprensión antes de avanzar.
       - **Regla anti-estiramiento:** Las preguntas o enunciados breves van obligatoriamente en un **párrafo independiente alineado a la izquierda (`WD_ALIGN_PARAGRAPH.LEFT`)**, evitando que Word estire las palabras de margen a margen. La respuesta explicativa va en un párrafo inferior **justificado con sangría izquierda de 0.18 pulgadas**. Prohibido usar saltos de línea suaves (`\n`) en bloques justificados.
     - ⚠️ **Alerta de Examen / Trampa Habitual (*Warning Box*):** Fondo suave de alerta (`#FDF4F0`), borde en Coral (`#E99073`). Errores analíticos frecuentes en pruebas de evaluación.
     - 💡 **Concepto Clave / Conceptos Clave del Tema (*Concept Box*):**
       - **Regla Mandatoria:** Debe situarse **en una página nueva** (incorporando obligatoriamente un **salto de página previo**).
       - Fondo verde menta suave (`#E1F6EA`), borde en Verde Salvia (`#76927A`), icono `💡` y título en Verde Profundo (`#566B56`). Los conceptos se listan de forma itemizada y jerárquica con viñeta salvia y término en negrita.
     - 📊 **Dato Empírico / Noticia (*Case Box*):** Fondo crema cálido (`#F3EFDC`), borde en Verde Profundo (`#566B56`). Aplicaciones reales de la EPA, SEPE o Banco de España.

4. **Tablas Estilizadas:**
   - Fila de cabecera con fondo Verde Profundo (`#566B56`) o Salvia (`#76927A`), texto en blanco y negrita.
   - Filas de datos con texto en Verde Tinta (`#2F3A30`), bordes horizontales limpios (`#D0DCD2`) y sombreado alterno sutil.

5. **Gestión Integral y Remasterización de Figuras:**
   - **Extracción Automática de Originales:** El script extrae el 100% de las imágenes del `.docx` original a `Temas EB/Tema X/figuras/originales/` y mapea su ubicación contextual exacta.
   - **Precedencia Inteligente de Remasterizadas:** Si existe una versión rediseñada en `Temas EB/Tema X/figuras/remasterizadas/` (generada mediante `.skills/psll-figuras-skill/` a 300 DPI con la paleta oficial), se inserta prioritariamente.
   - **Conservación sin Pérdidas:** Si una figura aún no ha sido rediseñada, se inserta la versión original extraída para asegurar que el documento nunca carezca de sus imágenes.
   - **Exclusión Selectiva de Figuras Obsoletas / Redundantes:** Permite declarar metadatos con `"skip": True` (ej. antiguas figuras de baja resolución que han sido absorbidas por un panel dual más completo), evitando duplicidades o gráficos anticuados en el documento maquetado.
   - **Maquetación Reglamentaria:** Todas las figuras se insertan centradas (ancho estándar ~6.2 pulgadas), con pie descriptivo en 9 pt Poppins negrita Verde Profundo (`#566B56`) y fuente en 8 pt Calibri cursiva Verde Salvia (`#76927A`):  
     *«Figura X.X: Título descriptivo. Fuente: Elaboración propia para Políticas Sociolaborales (UPO)...»*.
   - **Párrafos de Interpretación Analítica:** En figuras de alta complejidad teórica y empírica (ej. Figuras Duales 1.8 de Phillips y 1.9 de Beveridge), se añade inmediatamente bajo la fuente un párrafo analítico en 9.8 pt Calibri cursiva Verde Tinta (`#2F3A30`) que guía al alumno en la interpretación conjunta del panel teórico y del panel empírico.

6. **Cabecera Institucional Inicial (Página 1):**
   - Tabla de 2 columnas flotante transparente alineada a la izquierda (`WD_TABLE_ALIGNMENT.LEFT`).
   - Todos los párrafos de metadatos académicos formateados como líneas independientes alineadas a la izquierda (`WD_ALIGN_PARAGRAPH.LEFT`):
     - `UNIVERSIDAD PABLO DE OLAVIDE` (9 pt Poppins negrita en Verde Profundo `#566B56`).
     - `Facultad de Ciencias del Trabajo · Grado en RRLL y Recursos Humanos` (8.5 pt Calibri en Verde Salvia `#76927A`).
     - `Políticas Sociolaborales y de Empleo (Código 102023) | Curso 2026-2027` (8.5 pt Calibri en Verde Tinta `#2F3A30`).
     - `Prof. Manuel A. Hidalgo Pérez` (8.5 pt Calibri en Verde Tinta `#2F3A30`).
   - Celda derecha con el emblema oficial de la asignatura (`psll_emblem.png`).
   - Línea separadora horizontal (`―` * 48) alineada a la izquierda en Verde Salvia.

7. **Encabezado y Pie de Página Corporativo:**
   - **Encabezado Justificado a la Izquierda:** Alineado a la izquierda (`WD_ALIGN_PARAGRAPH.LEFT`) con el título del tema en verde salvia (`#76927A`), 8 pt Poppins.
   - Pie con paginación automática dinámica ("Página X de Y") y referencia institucional UPO / Grado en RRLL y RRHH.

8. **Tratamiento Avanzado de Fórmulas Matemáticas (`m:oMath`):**
   - Extracción nativa desde el XML de Word de todos los nodos matemáticos (`m:oMath` y `m:t`), evitando que se pierdan símbolos griegos ($\pi, \lambda, \alpha$) o condiciones lógicas al procesar el texto.
   - Las ecuaciones principales se maquetan automáticamente **centradas, con margen vertical holgado (6 pt antes / 6 pt después) y en negrita Verde Profundo (`#566B56`, 11 pt)**.
   - Las definiciones de parámetros y condiciones de desviación se integran en la jerarquía visual con viñetas institucionales y negritas en verde profundo.

---

## 🛠️ Ejecución y Reproducibilidad

El script motor se invoca desde la raíz del proyecto:
```powershell
py -3 .skills/psll-apuntes-skill/apply_style.py --input "Temas EB/Tema X/Apuntes/Tema X.docx" --output "Temas EB/Tema X/Apuntes/Tema X_maquetado.docx"
```
