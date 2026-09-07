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
    ├── beveridge.png
    └── ...
```

---

## 🛠️ Ejecución y Catálogo

Para generar o regenerar las figuras oficiales de un tema:
```powershell
py -3 .skills/psll-figuras-skill/generate_topic_figures.py --tema 1
```

Esto generará automáticamente los archivos `.png` en alta resolución dentro de `Temas EB/Tema 1/figuras/remasterizadas/`.
La skill de maquetación (`psll-apuntes-skill`) detectará automáticamente estos archivos y los integrará en el documento Word maquetado sustituyendo a las versiones originales.
