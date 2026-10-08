---
name: psll-examenes-skill
description: Protocolo y motor de diseño, maquetación y generación de exámenes oficiales y simulacros formativos de Políticas Sociolaborales y de Empleo (PSLL · UPO). Integra la cabecera institucional, la estructura de 6 preguntas cortas (<100 palabras) y 3 preguntas largas concisas y aplicadas (sin modelos analíticos ni matemáticas complejas), el sistema de comodines basado en la tasa de aciertos del Pasaporte de Evaluación Continua y la identidad visual de la asignatura.
---

# Skill: Diseño y Maquetación de Exámenes y Simulacros (PSLL)

Esta skill establece las directrices pedagógicas, formales y estéticas para generar los exámenes y simulacros de la asignatura **Políticas Sociolaborales y de Empleo (PSLL · Código 102023)** en la Universidad Pablo de Olavide (UPO).

---

## 🏛️ 1. Identidad Visual y Membrete Institucional

Todo examen o simulacro debe respetar escrupulosamente la identidad visual oficial del proyecto documentada en `BRAND.md` y `guia_de_estilo.md`:

| Atributo | Especificación | Detalle Técnico |
| :--- | :--- | :--- |
| **Logotipo PSLL + UPO** | `Logos y skills/marca/logo_psll_upo.png` | Ratio nativo 1.833 (ancho = alto × 1.833). Nunca deformar. |
| **Color Primario** | Verde Pino PSLL (`#113927`) | Cabeceras, títulos de sección, marcos destacados y divisores. |
| **Color Secundario** | Verde Salvia (`#76927A`) | Subtítulos, metadatos, bordes sutiles y tablas secundarias. |
| **Acento Dinámico** | Coral Active Wave (`#E98F71`) | Alertas, avisos de comodines y llamadas de atención. |
| **Fondo de Cajas** | Verde Menta Tenue (`#F4F8F5`) | Cuadros de datos de alumno, normas y áreas de respuesta. |
| **Texto de Lectura** | Verde Tinta (`#2F3A30`) | Enunciados, texto normativo y criterios de calificación. |
| **Tipografía Títulos** | Outfit (Bold / SemiBold) | `Logos y skills/fonts/Outfit-Bold.ttf`. |
| **Tipografía Cuerpo** | Calibri (Regular / Negrita / Cursiva) | Fuentes nativas del sistema (`C:\Windows\Fonts\calibri*.ttf`). |

### Elementos de Cabecera Obligatorios:
1. **Membrete Superior:** Logotipo oficial de PSLL y Universidad Pablo de Olavide.
2. **Identificación Académica:**
   - Asignatura: *Políticas Sociolaborales y de Empleo (Código 102023)*.
   - Titulación: Grados en Relaciones Laborales y Recursos Humanos / Doble Grado Derecho + RRLyRRHH.
   - Convocatoria / Tipo de Prueba: *Simulacro de Examen Parcial / Evaluación Continua Formativa (Sesión XX)*.
   - Curso Académico: *2026-27* · Docente: *Prof. Dr. Manuel A. Hidalgo Pérez*.
3. **Casillas de Filiación del Estudiante:**
   - Apellidos y Nombre.
   - DNI / NIE.
   - Grupo de Docencia (L1 / L2).
   - Firma del estudiante.

---

## 🎯 2. Sistema de Comodines de Evaluación Continua

El examen se articula con el **Pasaporte de Evaluación Continua**, en el cual los alumnos acumulan su desempeño en los retos manuscritos de Fase 5 de cada sesión presencial. La tasa individual de aciertos semanales desbloquea **comodines para descartar preguntas cortas**:

| Tasa de Aciertos en Pasaporte Semanal | Comodines (Preguntas Cortas Descartables) | Preguntas Cortas a Responder | Preguntas Largas a Responder | Total a Calificar |
| :---: | :---: | :---: | :---: | :---: |
| **$\ge 80\%$** | **4 preguntas descartables** | **2 cortas** (a elegir de 6) | 3 largas (obligatorias) | 5 preguntas |
| **$[60\%,\, 80\%)$** | **3 preguntas descartables** | **3 cortas** (a elegir de 6) | 3 largas (obligatorias) | 6 preguntas |
| **$[40\%,\, 60\%)$** | **2 preguntas descartables** | **4 cortas** (a elegir de 6) | 3 largas (obligatorias) | 7 preguntas |
| **$[20\%,\, 40\%)$** | **1 pregunta descartable** | **5 cortas** (a elegir de 6) | 3 largas (obligatorias) | 8 preguntas |
| **$< 20\%$** | **0 descartes (sin comodines)** | **6 cortas** (todas obligatorias) | 3 largas (obligatorias) | 9 preguntas |

### 📋 Cuadro de Declaración y Validación en Cabecera:
En la primera página del examen debe incluirse un recuadro formal con:
- Casilla visible para que el alumno consigne su **% de aciertos acreditado en su Pasaporte**.
- Selector/marcador de comodines disponibles.
- Casillas para que el alumno marque expresamente qué preguntas cortas descarta (ej. `[P1] [P2] [P3] [P4] [P5] [P6]`).
- Casilla de **Cotejo Docente**: Advertencia de que el profesor cotejará la tasa declarada con el registro central cifrado en la plataforma de evaluación.

---

## 📝 3. Directrices Pedagógicas y Criterios de Redacción

### 🚫 Regla de Oro: Sin Preguntas Analíticas ni Modelos Teóricos Formales
- **Prohibido preguntar modelos teóricos formales como tales:** Queda expresamente prohibido formular preguntas analíticas abstractas basadas en derivaciones matemáticas o representaciones geométricas formales de modelos teóricos (por ejemplo, la Curva de Beveridge, la Curva de Phillips o funciones algebraicas de emparejamiento con parámetros y exponentes tipo $M = A \cdot U^\alpha \cdot V^\beta$ **NO se preguntan como modelos formales**).
- **Enfoque Sociolaboral Aplicado (Perfil RRLyRRHH):** El alumnado pertenece a Relaciones Laborales y Recursos Humanos. Las preguntas deben evaluar el entendimiento intuitivo de la realidad sociolaboral, las instituciones del mercado de trabajo, los problemas de empleo de las empresas y el diseño e impacto de las políticas públicas.
- **Límite Cuantitativo Estricto:** Cero matemáticas complejas. Únicamente se admiten:
  1. Cálculos de ratios e indicadores básicos del mercado de trabajo (tasa de paro, tasa de empleo, tasa de actividad o aproximación simple del CLU).
  2. Cálculos directos y aplicados de evaluación de políticas de empleo: cálculo de porcentajes sencillos de **Efecto Peso Muerto (Deadweight)**, **Efecto Sustitución** y **Creación Neta Efectiva de Empleo**, así como el coste público por empleo neto.

### ✂️ Concisión en las Preguntas Largas (Evitar Textos Excesivos)
- **Enunciados breves y directos:** Se debe evitar redactar parrafadas densas o sobrecargadas que abrumen al estudiante. El contexto de cada caso práctico debe plantearse en 3 o 4 líneas claras y concisas.
- **Preguntas acotadas (2 o 3 apartados):** Cada pregunta larga debe dividirse en 2 o 3 apartados (a, b, c) muy específicos, evitando preguntas dobles o dispersas que pidan demasiadas cosas a la vez.

---

## 🧩 4. Estructura de las Dos Partes del Examen

### Parte I: Preguntas Cortas de Síntesis Conceptual (6 preguntas)
- **Extensión Máxima:** Menos de 100 palabras por pregunta (espacio pautado de 5 líneas).
- **Objetivo:** Definición rigurosa de términos sociolaborales, identificación de categorías estadísticas (EPA/SEPE), trampas de empleo o conceptos clave de políticas activas.
- **Régimen de Elección:** Es la **única parte sujeta al sistema de comodines** del pasaporte.

### Parte II: Preguntas Largas Aplicadas y Concisas (3 preguntas)
- **Obligatoriedad:** **100% obligatorias para todo el alumnado**, sin comodines.
- **Objetivo:** Resolución de un dilema empresarial o de gestión laboral, diagnóstico de un problema de desajuste en el empleo y evaluación cuantitativa directa de un programa de fomento de la contratación (peso muerto y coste por empleo neto).
- **Extensión y Espacio:** Desarrollo estructurado y conciso en una página pautada por pregunta.

---

## ⚙️ 5. Reglas de Generación y Automatización

1. **Ubicación de Salida:**
   - Los PDFs de exámenes y simulacros se guardan en: `examenes/`.
   - Nomenclatura oficial: `examenes/simulacro_sXX.pdf` (donde `XX` es la sesión hasta la cual se cubre la materia, por ejemplo `simulacro_s07.pdf`).
   - El documento explicativo de normas para el alumnado se guarda como `examenes/guia_procedimiento_examen_evaluacion_continua.pdf`.
   - **Carácter General y Atemporal de la Guía:** Este documento sirve para todo el curso escolar y para el examen final global. En su sección de formato de preguntas no deben mencionarse temas concretos ni ejemplos de sesiones específicas (nada de EPA, CLU, Beveridge, etc.), sino únicamente las directrices generales de formato (Parte I cortas <100 palabras y Parte II largas en 2-3 apartados prácticos, sin modelos analíticos abstractos ni matemáticas complejas).

2. **Alcance Temático Dinámico:**
   - Al solicitar un simulacro para una sesión $N$, se comprueban los conceptos vistos hasta dicha sesión, formulando siempre preguntas aplicadas y comprensibles para estudiantes de RRLyRRHH, sin formalismos matemáticos.

3. **Ciclo de Scripts y Scratch:**
   - Todo script intermedio de compilación o comprobación se aloja en `scratch/`.
   - Al finalizar con éxito, se solicita confirmación expresa a Manuel para su eliminación.
