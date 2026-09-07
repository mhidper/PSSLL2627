---
name: psll-figuras-skill
description: Motor especializado de generación y remasterización gráfica de figuras, curvas económicas y diagramas para Políticas Sociolaborales (PSLL). Aplica la paleta corporativa oficial (menta, salvia, coral), tipografías Poppins/Calibri, calidad 300 DPI y pies institucionales UPO.
---

# Skill: Remasterización y Generación Gráfica (PSLL)

Esta skill gobierna la creación, vectorización y rediseño de figuras, esquemas conceptuales y curvas analíticas para la asignatura **Políticas Sociolaborales y de Empleo (PSLL · Código 102023)** en la Universidad Pablo de Olavide (UPO).

---

## 🎨 Especificaciones de Identidad Gráfica

Basado estrictamente en [Logos y skills/BRAND.md](file:///c:/Users/Usuario/Dropbox/DOCENCIA%20UPO/CURSO%2026-27/PSLL/Logos%20y%20skills/BRAND.md):

| Elemento | Código HEX | Rol en Gráficos |
| :--- | :--- | :--- |
| **Verde Salvia** | `#76927A` | Serie de datos principal, curvas canónicas iniciales (ej. $BC_1$, $S_L$), cajas estructurales |
| **Verde Profundo** | `#566B56` | Títulos de gráficos, etiquetas de equilibrio, contrastes fuertes, bordes principales |
| **Verde Tinta** | `#2F3A30` | Texto de ejes, números y etiquetas secundarias |
| **Coral** | `#E99073` | Serie de contraste, desplazamientos estructurales (ej. $BC_2$), alertas, choques adversos |
| **Melocotón** | `#EDB090` | Serie complementaria suave, áreas de dispersión, escenarios intermedios |
| **Verde Menta** | `#E1F6EA` | Sombras, áreas bajo la curva, cajas de conceptos, fondos suaves |
| **Crema Cálido** | `#F3EFDC` | Fondos de diagramas de bloques, cuadros de metodología |
| **Gris Ejes** | `#A0B0A4` | Líneas de ejes cartesianos y cuadrícula discontinua tenue |

### Parámetros Técnicos Obligatorios:
- **Resolución:** 300 DPI (`dpi=300`), ideal para impresión y maquetación editorial en Word y proyección en diapositivas PPTX.
- **Tipografía:** `Calibri` / `Arial` para ejes y etiquetas numéricas; `Poppins` / sans-serif negrita para títulos.
- **Pie de figura:** Siempre debe incluir autoría y fuente:  
  *«Fuente: Elaboración propia para Políticas Sociolaborales (UPO)...»*

---

## 📁 Convención de Rutas Relativas por Tema

Las figuras se gestionan siempre en la carpeta relativa de cada tema dentro de `Temas EB/`:

```text
Temas EB/Tema X/figuras/
├── originales/        <- Extraídas automáticamente del .docx original por psll-apuntes-skill
│   ├── image1.png
│   ├── image2.png
│   └── ...
└── remasterizadas/    <- Generadas a 300 DPI con marca PSLL por psll-figuras-skill
    ├── epa_taxonomy.png
    ├── epa_decision_tree.png
    ├── vab_pan.png
    ├── pib_interanual.png
    ├── productividad_salarios.png
    ├── modelo_desempleo_neoclasico.png
    ├── tasa_natural_nairu.png
    ├── curva_phillips_dual.png
    └── curva_beveridge_dual.png
```

---

## 🛠️ Ejecución y Catálogo Oficial de Figuras (Tema 1)

Para generar o regenerar las figuras oficiales de un tema:
```powershell
py -3 .skills/psll-figuras-skill/generate_topic_figures.py --tema 1
```

### Catálogo de Figuras Oficiales de Tema 1 (100% Remasterizadas a 300 DPI):
1. **Figura 1.1 (`epa_taxonomy.png`):** Taxonomía oficial y articulación de la población según la EPA (INE / OIT).
2. **Figura 1.2 (`epa_decision_tree.png`):** Algoritmo metodológico y árbol de decisión de clasificación laboral (OIT / EPA).
3. **Figura 1.3 (`vab_pan.png`):** Cadena de Valor Añadido Bruto (VAB) y proceso productivo del pan (cálculo del PIB por la vía de la producción y eliminación de la doble contabilización).
4. **Figura 1.4 (`pib_interanual.png`):** Evolución trimestral del PIB en España: tasas de variación interanual en volumen encadenado (2022T1 - 2026T2, Contabilidad Nacional Trimestral de España, INE).
5. **Figura 1.5 (`productividad_salarios.png`):** Relación empírica entre productividad laboral por hora y salario medio en la OCDE (2024): panel dual con tabla de clasificación y dispersión con regresión MCO ($R^2 = 0,7309$).
6. **Figura 1.6 (`modelo_desempleo_neoclasico.png`):** El desempleo en el modelo neoclásico de mercado de trabajo: oferta backward-bending, demanda, equilibrio competitivo, rigidez salarial y exceso de oferta involuntario.
7. **Figura 1.7 (`tasa_natural_nairu.png`):** Tasa de desempleo observada vs. Tasa natural (NAIRU) en España y la Zona Euro (1980–2024, base AMECO) con sombreado de brechas cíclicas y análisis del suelo estructural.
8. **Figura 1.8 (`curva_phillips_dual.png`):** Panel Dual de la Curva de Phillips:
   - **Panel A (Teórico):** Modelo aceleracionista de Friedman-Phelps (estímulo coyuntural $A \to B$ en $CP_1$, ajuste de expectativas en $CP_2$ y curva vertical de largo plazo $LP$ en la NAIRU $C$).
   - **Panel B (Empírico):** Evidencia en España (2002–2024, datos oficiales INE de EPA y ETCL) categorizada en 4 fases macroeconómicas (burbuja, devaluación salarial de 2012, recuperación y shock inflacionista post-COVID).
9. **Figura 1.9 (`curva_beveridge_dual.png`):** Panel Dual de la Curva de Beveridge:
   - **Panel A (Teórico):** Modelo Diamond-Mortensen-Pissarides (DMP): movimientos a lo largo de la curva (ciclo económico) vs. desplazamientos estructurales de emparejamiento ($E_1 \to E_2$).
   - **Panel B (Empírico):** Serie temporal armonizada de 45 años en España (1980–2024, FEDEA, Nada es Gratis e INE): fase pre-crisis con ancla en punto $A$, Gran Recesión con desplazamiento al punto $B$ (+5 p.p. de paro estructural) y recuperación récord de vacantes (0,70%–0,73%) con paro al 11,3%.

La skill de maquetación (`psll-apuntes-skill`) detecta automáticamente estos archivos y los integra en el documento Word maquetado sustituyendo a las versiones originales.
