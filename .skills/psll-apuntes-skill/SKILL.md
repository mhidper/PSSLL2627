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
| **Tipografía Cuerpo** | Calibri | 10.5 pt, interlineado 1.15, espacio posterior 4 pt |
| **Márgenes de página** | Estándar institucional | Superior/Inferior 2.5 cm, Izquierdo/Derecho 2.5 cm |

---

## 🧩 Componentes Modulares Soportados

1. **Jerarquía Tipográfica Homogénea:**
   - Detección y normalización automática de epígrafes (`1.`, `1.1.`, `1.2.1.`).
   - Aplicación estricta de `Heading 1`, `Heading 2` y `Heading 3` para navegación en Word.

2. **Cajas Destacadas (*Callout Boxes*):**
   - Tabla unificada de 1 celda con fondo `#E1F6EA` (o `#FDF4F0` para alertas), borde izquierdo grueso de 3 pt en Salvia (`#76927A`) o Coral (`#E99073`), padding interior calibrado y título en negrita con icono temático.
   - Tipos:
     - 💡 *Concepto Clave*: Fundamentos micro/macroeconómicos y definiciones.
     - ⚠️ *Alerta / Trampa Habitual*: Errores conceptuales típicos en exámenes.
     - 📊 *Dato Empírico / Noticia*: Casos reales de la EPA, SEPE o Banco de España.

3. **Tablas Estilizadas:**
   - Fila de cabecera con fondo Verde Profundo (`#566B56`) o Salvia (`#76927A`), texto en blanco y negrita.
   - Filas de datos con texto en Verde Tinta (`#2F3A30`), bordes horizontales limpios (`#D0DCD2`) y sombreado alterno sutil.

4. **Figuras Oficiales Generadas en Python (`matplotlib`):**
   - Gráficos generados a 300 DPI respetando la paleta de la marca.
   - Ancladas centradas con pie reglamentario:  
     *«Figura X.X: Título descriptivo. Fuente: Elaboración propia para Políticas Sociolaborales (UPO)...»*.

5. **Encabezado y Pie de Página Corporativo:**
   - Cabecera con logo horizontal o emblema oficial.
   - Pie con paginación automática ("Página X de Y") y código de asignatura (`PSLL · 102023`).

---

## 🛠️ Ejecución y Reproducibilidad

El script motor se invoca desde la raíz del proyecto:
```powershell
py -3 .skills/psll-apuntes-skill/apply_style.py --input "Temas EB/Tema X/Apuntes/Tema X.docx" --output "Temas EB/Tema X/Apuntes/Tema X_maquetado.docx"
```
