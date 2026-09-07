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

1. **Jerarquía Tipográfica y Alineación Justificada:**
   - Detección y normalización automática de epígrafes (`1.`, `1.1.`, `1.2.1.`).
   - Aplicación estricta de `Heading 1` (15 pt en verde profundo), `Heading 2` (12.5 pt en salvia) y `Heading 3` (11 pt en verde profundo) alineados a la izquierda para navegación en Word.
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
     - ⚠️ **Alerta de Examen / Trampa Habitual (*Warning Box*):** Fondo suave de alerta (`#FDF4F0`), borde en Coral (`#E99073`). Errores analíticos frecuentes en pruebas de evaluación.
     - 💡 **Concepto Clave (*Concept Box*):** Fondo verde menta (`#E1F6EA`), borde en Verde Salvia (`#76927A`). Fundamentos teóricos e intuiciones microeconómicas.
     - 📊 **Dato Empírico / Noticia (*Case Box*):** Fondo crema cálido (`#F3EFDC`), borde en Verde Profundo (`#566B56`). Aplicaciones reales de la EPA, SEPE o Banco de España.

4. **Tablas Estilizadas:**
   - Fila de cabecera con fondo Verde Profundo (`#566B56`) o Salvia (`#76927A`), texto en blanco y negrita.
   - Filas de datos con texto en Verde Tinta (`#2F3A30`), bordes horizontales limpios (`#D0DCD2`) y sombreado alterno sutil.

5. **Figuras Oficiales Generadas en Python (`matplotlib`):**
   - Gráficos generados a 300 DPI respetando la paleta de la marca (`figure_generator.py`).
   - Ancladas centradas con pie reglamentario:  
     *«Figura X.X: Título descriptivo. Fuente: Elaboración propia para Políticas Sociolaborales (UPO)...»*.

6. **Encabezado y Pie de Página Corporativo:**
   - Cabecera con título del tema en verde salvia.
   - Pie con paginación automática ("Página X de Y") y código de asignatura (`PSLL · 102023`).

---

## 🛠️ Ejecución y Reproducibilidad

El script motor se invoca desde la raíz del proyecto:
```powershell
py -3 .skills/psll-apuntes-skill/apply_style.py --input "Temas EB/Tema X/Apuntes/Tema X.docx" --output "Temas EB/Tema X/Apuntes/Tema X_maquetado.docx"
```
