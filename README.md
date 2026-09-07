# Políticas Sociolaborales y de Empleo (PSLL) — Curso 2026-2027
### Grado en Relaciones Laborales y Recursos Humanos / Doble Grado en Derecho y RRLL-RRHH
**Universidad Pablo de Olavide (UPO) — Código Asignatura: 102023**

---

## 📌 Descripción General del Proyecto

Este repositorio contiene la arquitectura docente integral, los materiales teóricos, las dinámicas prácticas, la identidad visual y la planificación coordinada para la asignatura **Políticas Sociolaborales y de Empleo (PSLL)** correspondiente al curso académico **2026-2027** (primer semestre: septiembre a diciembre de 2026).

El proyecto implementa un modelo de innovación pedagógica centrado en el **aula invertida (*Flipped Classroom*)** y el **Aprendizaje Basado en Proyectos/Problemas (ABP)**, donde:
- Las **Enseñanzas Básicas (EB)** proporcionan los mecanismos causales, la teoría macroeconómica y el instrumental empírico.
- Las **Enseñanzas Prácticas y de Desarrollo (EPD)** sitúan al estudiantado en el rol de analistas y diseñadores de políticas sociolaborales reales mediante **dos grandes casos de estudio**.

---

## 🗂️ Estructura del Repositorio

```text
PSLL/
├── README.md                                 # Este documento de bienvenida, mapa de navegación y estado
├── GEMINI.md                                 # Contexto del proyecto, reglas de IA, conexión a NotebookLM y marca
├── Guía Docente 102023-1.pdf                 # Guía docente oficial UPO Línea 1 (Mañana)
├── Guía Docente 102023-2.pdf                 # Guía docente oficial UPO Línea 2 (Tarde)
├── horarios L1.pdf                           # Calendario oficial de clases Línea 1 (Grado y Doble Grado)
├── horarios L2.pdf                           # Calendario oficial de clases Línea 2 (Grado y Doble Grado)
│
├── .skills/                                  # Motor editorial y gráfico automatizado (Skills del proyecto)
│   ├── psll-apuntes-skill/                   # Maquetación editorial de apuntes (.docx) con marca y jerarquía
│   │   ├── apply_style.py                    # Script motor principal de transformación de documentos
│   │   ├── docx_styler.py                    # Primitivas de estilo, callouts, tablas y cabeceras
│   │   ├── palette_utils.py                  # Utilidades de color y sombreado XML
│   │   └── SKILL.md                          # Guía y especificaciones completas de maquetación
│   └── psll-figuras-skill/                   # Generación y remasterización de figuras a 300 DPI
│       ├── brand_figures.py                  # Estilo matplotlib, paleta institucional y guardado en 300 DPI
│       ├── generate_topic_figures.py         # Generador modular de gráficos por tema (ej. --tema 1)
│       └── SKILL.md                          # Catálogo de figuras y parámetros técnicos
│
├── cronograma/                               # Planificación temporal coordinada día a día
│   ├── cronograma_psll_2026_27.md            # Cronograma semanal en paralelo (L1 vs. L2), aulas y vinculación EB-EPD
│   ├── guion_sesion_1409_lunes.md            # Guiones detallados sesión a sesión con retos y dinámicas
│   ├── guion_sesion_1409_martes.md
│   ├── guion_sesion_2109_lunes.md
│   └── guion_sesion_2109_martes.md
│
├── innovación_docente/                       # Marco metodológico e innovación pedagógica
│   └── propuesta_innovacion_docente.md       # Estrategias Flipped Classroom, dinámicas activas y gamificación
│
├── Temas EB/                                 # Materiales teóricos de Enseñanzas Básicas (EB)
│   ├── Recursos generales/                   # Código de gráficos (matplotlib) y plantillas
│   ├── Tema 0/                               # Presentación, metodología y conceptos introductorios
│   ├── Tema 1/                               # Fundamentos del mercado laboral, flujos, NAIRU, Phillips y Beveridge
│   │   ├── Apuntes/
│   │   │   └── Tema 1 2627_maquetado.docx    # VERSIÓN CANÓNICA OFICIAL maquetada con 9 figuras a 300 DPI
│   │   ├── Diapositivas/
│   │   │   └── Tema 1 2627.pptx              # Presentación oficial de aula
│   │   ├── figuras/
│   │   │   ├── originales/                   # Figuras extraídas del documento fuente
│   │   │   └── remasterizadas/               # Figuras 100% remasterizadas a 300 DPI con paleta PSLL
│   │   └── Versiones antiguas/               # Archivo histórico de versiones previas sin figuras
│   ├── Tema 2/                               # Políticas Activas de Empleo (PAE), tipologías y evaluación
│   ├── Tema 3/                               # Políticas Pasivas, protección por desempleo y rentas mínimas (IMV)
│   ├── Tema 4/                               # Flexibilidad, costes de despido (EPL) y dualidad contractual
│   ├── Tema 5/                               # Negociación colectiva, fijación salarial y salarios de eficiencia
│   ├── Tema 6/                               # Estructura salarial, SMI y pobreza laboral
│   └── Tema 7/                               # Sostenibilidad de pensiones, demografía y reparto
│
├── EPD/                                      # Enseñanzas Prácticas y de Desarrollo (Casos Prácticos)
│   ├── PSLL_EPD_2026-27_propuesta.docx       # Memoria y propuesta operativa de las prácticas
│   └── Material para definir contenido/      # Órdenes reguladoras (Emplea-T), presentaciones y datos
│
├── Logos y skills/                           # Identidad de marca, paleta oficial y assets
│   ├── BRAND.md                              # Guía de estilo visual de PSLL (paleta menta/salvia/coral)
│   ├── psll_icon.svg / psll_lockup.png       # Emblemas oficiales de la asignatura
│   └── psll-presentaciones-skill/            # Skill para diapositivas (.pptx) con identidad de marca
│
├── Repositorio material (no alumnos)/        # Literatura científica de apoyo docente (Mortensen, Pissarides, etc.)
└── .claude/skills/marca-psll/                # Skill de marca oficial para asistentes de código
```

---

## 🛠️ Motor Editorial y Remasterización Gráfica (Skills Oficiales)

El proyecto cuenta con un sistema modular automatizado para garantizar que todos los materiales docentes (apuntes `.docx`, gráficos Python y presentaciones `.pptx`) cumplan los más altos estándares visuales, pedagógicos y editoriales:

### 1. Skill de Maquetación de Apuntes: [`.skills/psll-apuntes-skill/`](file:///c:/Users/Usuario/Dropbox/DOCENCIA%20UPO/CURSO%2026-27/PSLL/.skills/psll-apuntes-skill/SKILL.md)
* **Motor:** [`apply_style.py`](file:///c:/Users/Usuario/Dropbox/DOCENCIA%20UPO/CURSO%2026-27/PSLL/.skills/psll-apuntes-skill/apply_style.py).
* **Jerarquía tipográfica:** Títulos en `Poppins` negrita Verde Profundo (`#566B56`), subtítulos en Verde Salvia (`#76927A`), cuerpo en `Calibri` 10.5 pt justificado en Verde Tinta (`#2F3A30`).
* **Cajas semánticas (*Callouts*):**
  - 🗓️ **Encuadre Docente Presencial:** Sitúa al estudiante en el cronograma semanal oficial.
  - 💭 **Parada Reflexiva:** Preguntas y respuestas estructuradas con formato anti-estiramiento.
  - ⚠️ **Alerta de Examen:** Puntos críticos y trampas habituales de evaluación.
  - 💡 **Conceptos Clave del Tema:** Caja capitular de síntesis en página dedicada con salto de página previo.
* **Tratamiento avanzado de fórmulas matemáticas (`m:oMath`):** Extracción nativa desde el XML de Word de fórmulas y símbolos griegos ($\pi, \lambda, \alpha$), maquetadas automáticamente **centradas, con holgura y en negrita verde profundo**.
* **Párrafos de interpretación analítica:** Explicación guiada bajo las figuras analíticas duales para maximizar la comprensión del alumnado.

### 2. Skill de Remasterización Gráfica: [`.skills/psll-figuras-skill/`](file:///c:/Users/Usuario/Dropbox/DOCENCIA%20UPO/CURSO%2026-27/PSLL/.skills/psll-figuras-skill/SKILL.md)
* **Motor:** [`brand_figures.py`](file:///c:/Users/Usuario/Dropbox/DOCENCIA%20UPO/CURSO%2026-27/PSLL/.skills/psll-figuras-skill/brand_figures.py) y [`generate_topic_figures.py`](file:///c:/Users/Usuario/Dropbox/DOCENCIA%20UPO/CURSO%2026-27/PSLL/.skills/psll-figuras-skill/generate_topic_figures.py).
* **Calidad institucional:** Gráficos generados a **300 DPI**, con paleta institucional de marca y pies de fuente oficiales.
* **Estado de Tema 1 (100% Remasterizado):**
  1. `epa_taxonomy.png`: Taxonomía metodológica oficial EPA / OIT.
  2. `epa_decision_tree.png`: Árbol de decisión de clasificación laboral.
  3. `vab_pan.png`: Cadena de Valor Añadido Bruto del pan y cálculo del PIB.
  4. `pib_interanual.png`: Evolución interanual del PIB trimestral (CNTR, INE).
  5. `productividad_salarios.png`: Relación productividad por hora vs. salarios en la OCDE 2024 (panel dual: ranking y regresión MCO).
  6. `modelo_desempleo_neoclasico.png`: Modelo neoclásico de mercado laboral (oferta backward-bending, rigidez salarial y desempleo involuntario).
  7. `tasa_natural_nairu.png`: Tasa de desempleo observada vs. NAIRU (España vs. Eurozona 1980–2024, AMECO) con sombreado cíclico.
  8. `curva_phillips_dual.png`: Panel Dual de la Curva de Phillips (Teoría Friedman-Phelps + Evidencia España 2002–2024 INE).
  9. `curva_beveridge_dual.png`: Panel Dual de la Curva de Beveridge (Modelo teórico DMP + Evidencia España 1980–2024 FEDEA/INE).

---

## 🧭 Pilares Metodológicos y Coordinación Docente

### 1. Sincronización Estricta entre Líneas (L1 y L2)
La asignatura se imparte simultáneamente en dos turnos con distinta configuración horaria y número de sesiones prácticas:
- **Línea 1 (Mañana):** EB los lunes (13:30–15:00, 1,5 h) y martes (09:30–11:30, 2,0 h) en el Aula E13A7. Dispone de **6 sesiones de EPD** en aula informática (lunes 13:30–15:00 o martes 11:30–13:00).
- **Línea 2 (Tarde):** EB los lunes (20:00–21:30, 1,5 h) y viernes (17:30–19:30, 2,0 h) en el Aula E10A3. Dispone de **7 sesiones de EPD** en aula informática (viernes 19:30–21:00).

> Para consultar el desglose exacto fecha a fecha, aula y contenido diario, véase [cronograma/cronograma_psll_2026_27.md](file:///c:/Users/Usuario/Dropbox/DOCENCIA%20UPO/CURSO%2026-27/PSLL/cronograma/cronograma_psll_2026_27.md).

### 2. Los Dos Casos de Estudio en EPD
El trabajo práctico se divide en dos bloques donde el alumnado asume el rol de asesor técnico:
1. **Caso 1 (Sesiones EPD 1, 2 y 3) · *Incentivos a la Contratación de Parados de Larga Duración (PLD)*:**
   - Inspirado en la Orden del *Programa Emplea-T* de la Junta de Andalucía.
   - Aplica los conceptos de la Curva de Beveridge, emparejamiento (*matching*), efecto peso muerto (*deadweight*) y efecto sustitución.
   - Culmina con la entrega del **Dossier Técnico 1** (Semana 9).
2. **Caso 2 (Sesiones EPD 4, 5 y 6) · *El Ingreso Mínimo Vital (IMV) y el Incentivo al Empleo*:**
   - Análisis empírico del *non-take-up* (hogares que teniendo derecho no lo perciben) a partir de los informes de la AIReF.
   - Diseño de la compatibilidad entre subsidio y salario eliminando el tipo marginal del 100% (esquema EITC).
   - Culmina con la entrega del **Dossier Técnico 2** (Semana 13).
3. **Sesión 7 de EPD (Exclusiva Línea 2):**
   - Configurada como sesión de **clínica práctica avanzada y preparación de la evaluación**, equilibrando el desfase administrativo entre ambos turnos sin alterar la igualdad curricular.

---

## 🎨 Identidad de Marca y Visual (Brand Identity)

Los documentos oficiales, diapositivas y figuras generadas con Python siguen la identidad corporativa documentada en [Logos y skills/BRAND.md](file:///c:/Users/Usuario/Dropbox/DOCENCIA%20UPO/CURSO%2026-27/PSLL/Logos%20y%20skills/BRAND.md):
- **Paleta oficial (basada en el emblema de la asignatura):**
  - Fondo/Lienzo menta: `#E1F6EA`
  - Verde salvia (estructura y serie principal): `#76927A`
  - Verde profundo (titulares y contraste): `#566B56`
  - Verde tinta (cuerpo de texto — nunca negro puro): `#2F3A30`
  - Coral (acento puntual enérgico): `#E99073`
  - Melocotón (acento suave y fondos de tarjeta): `#EDB090`
- **Tipografías:** `Poppins` para titulares y `Calibri` / `Arial` para textos extensos y tablas.

---

## 🤖 Integración con Cuaderno de Innovación en NotebookLM

El proyecto está permanentemente sincronizado con el cuaderno docente en Google NotebookLM:
- **Título del Cuaderno:** *Estrategias y Dinámicas para un Aprendizaje Significativo y Práctico*
- **Notebook ID:** `b94a743f-30fe-4b04-b7b4-d4da08e06d16`
- **Finalidad:** Consulta de dinámicas participativas, micro-evaluaciones formativas, rúbricas de debate y alineación de actividades activas para las sesiones de clase.

---

## 📊 Sistema de Evaluación

| Instrumento | Ponderación | Carácter | Vinculación |
| :--- | :---: | :---: | :--- |
| **Dossier Técnico 1 (Caso Emplea-T / PLD)** | **30%** | Grupal | EPD 1, 2 y 3. Entrega en Semana 9. |
| **Dossier Técnico 2 (Caso IMV / Incentivo Empleo)** | **30%** | Grupal | EPD 4, 5 y 6. Entrega en Semana 13. |
| **Participación y Retos de Clase Activa** | **10%** | Individual | Discusión guiada y micro-casos en EB. |
| **Examen Final Teórico-Práctico** | **30%** | Individual | Integración analítica y resolución de problemas. |

---

## 📚 Enlaces de Interés dentro del Proyecto

- 📖 [Apuntes Maquetados de Tema 1 (Versión Canónica)](file:///c:/Users/Usuario/Dropbox/DOCENCIA%20UPO/CURSO%2026-27/PSLL/Temas%20EB/Tema%201/Apuntes/Tema%201%202627_maquetado.docx)
- 📅 [Cronograma Oficial Coordinado (L1 y L2)](file:///c:/Users/Usuario/Dropbox/DOCENCIA%20UPO/CURSO%2026-27/PSLL/cronograma/cronograma_psll_2026_27.md)
- 💡 [Propuesta de Innovación Docente y Dinámicas de Aula](file:///c:/Users/Usuario/Dropbox/DOCENCIA%20UPO/CURSO%2026-27/PSLL/innovación_docente/propuesta_innovacion_docente.md)
- 🎨 [Guía de Estilo y Marca Visual (BRAND.md)](file:///c:/Users/Usuario/Dropbox/DOCENCIA%20UPO/CURSO%2026-27/PSLL/Logos%20y%20skills/BRAND.md)
- 🛠️ [Instrucciones de Contexto y Conexión de IA (GEMINI.md)](file:///c:/Users/Usuario/Dropbox/DOCENCIA%20UPO/CURSO%2026-27/PSLL/GEMINI.md)
