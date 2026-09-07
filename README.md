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
├── README.md                                 # Este documento de bienvenida y mapa de navegación
├── GEMINI.md                                 # Contexto del proyecto, reglas de IA, conexión a NotebookLM y marca
├── Guía Docente 102023-1.pdf                 # Guía docente oficial UPO Línea 1 (Mañana)
├── Guía Docente 102023-2.pdf                 # Guía docente oficial UPO Línea 2 (Tarde)
├── horarios L1.pdf                           # Calendario oficial de clases Línea 1 (Grado y Doble Grado)
├── horarios L2.pdf                           # Calendario oficial de clases Línea 2 (Grado y Doble Grado)
│
├── cronograma/                               # Planificación temporal coordinada día a día
│   └── cronograma_psll_2026_27.md            # Cronograma semanal en paralelo (L1 vs. L2), aulas y vinculación EB-EPD
│
├── innovación_docente/                       # Marco metodológico e innovación pedagógica
│   └── propuesta_innovacion_docente.md       # Estrategias Flipped Classroom, dinámicas activas y gamificación
│
├── Temas EB/                                 # Materiales teóricos de Enseñanzas Básicas (EB)
│   ├── Recursos generales/                   # Código de gráficos (matplotlib) y plantillas
│   ├── Tema 0/                               # Presentación, metodología y conceptos introductorios
│   ├── Tema 1/                               # Flujos/stocks del mercado laboral, Beveridge y desajuste (mismatch)
│   ├── Tema 2/                               # Políticas Activas de Empleo (PAE), tipologías y evaluación de impacto
│   ├── Tema 3/                               # Políticas Pasivas, protección por desempleo y rentas mínimas (IMV)
│   ├── Tema 4/                               # Flexibilidad, costes de despido (EPL) y dualidad contractual
│   ├── Tema 5/                               # Negociación colectiva, modelos de fijación salarial y salarios de eficiencia
│   ├── Tema 6/                               # Estructura salarial, Salario Mínimo Interprofesional (SMI) y pobreza laboral
│   └── Tema 7/                               # Sostenibilidad del sistema de pensiones, demografía y reparto
│
├── EPD/                                      # Enseñanzas Prácticas y de Desarrollo (Casos Prácticos)
│   ├── PSLL_EPD_2026-27_propuesta.docx       # Memoria y propuesta operativa de las prácticas
│   └── Material para definir contenido/      # Órdenes reguladoras (Emplea-T), presentaciones y datos
│
├── Logos y skills/                           # Identidad de marca, paleta oficial y estilos
│   ├── BRAND.md                              # Guía de estilo visual de PSLL (paleta menta/salvia/coral)
│   ├── psll_icon.svg / psll_lockup.png       # Emblemas oficiales de la asignatura
│   └── psll-presentaciones-skill/            # Skill para generación automatizada de diapositivas y figuras
│
├── Repositorio material (no alumnos)/        # Literatura científica de apoyo docente (Mortensen, Pissarides, etc.)
└── .claude/skills/marca-psll/                # Skill de marca oficial para asistentes de código
```

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

- 📅 [Cronograma Oficial Coordinado (L1 y L2)](file:///c:/Users/Usuario/Dropbox/DOCENCIA%20UPO/CURSO%2026-27/PSLL/cronograma/cronograma_psll_2026_27.md)
- 💡 [Propuesta de Innovación Docente y Dinámicas de Aula](file:///c:/Users/Usuario/Dropbox/DOCENCIA%20UPO/CURSO%2026-27/PSLL/innovación_docente/propuesta_innovacion_docente.md)
- 🎨 [Guía de Estilo y Marca Visual (BRAND.md)](file:///c:/Users/Usuario/Dropbox/DOCENCIA%20UPO/CURSO%2026-27/PSLL/Logos%20y%20skills/BRAND.md)
- 🛠️ [Instrucciones de Contexto y Conexión de IA (GEMINI.md)](file:///c:/Users/Usuario/Dropbox/DOCENCIA%20UPO/CURSO%2026-27/PSLL/GEMINI.md)
