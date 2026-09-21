---
name: psll-evaluacion-ciega-skill
description: Protocolo estandarizado para la ingestión, anonimización visual, transcripción OCR única, corrección a ciegas (blind grading) y baremo continuo (0-1.000 pts) de los retos manuscritos individuales de cierre de sesión en Políticas Sociolaborales y de Empleo (PSLL · UPO).
---

# Skill: Evaluación Ciega de Retos Manuscritos · PSLL UPO

Este protocolo describe el procedimiento estandarizado y reproducible para evaluar las respuestas manuscritas de los alumnos a la pregunta/reto final de cada sesión de Enseñanzas Básicas (EB) en **Políticas Sociolaborales y de Empleo (PSLL)**, garantizando **100% de corrección a ciegas (blind grading)**, cumplimiento estricto del **RGPD / LOPDGDD** y máxima eficiencia de tokens.

---

## 1. Activación y Parámetros de Entrada

Se activa siempre que el profesor Manuel indique:  
*«Vamos a evaluar la pregunta final de la sesión [XX]»* o frases análogas.

**Entradas Requeridas:**
1. **Identificador de la Sesión:** Ej. `Sesion 01`, `Sesion 02`, `Sesion 03`.
2. **Directorio o Enlace de Entregas en Microsoft Forms (OneDrive):**  
   `C:\Users\Usuario\OneDrive - Universidad Pablo de Olavide de Sevilla\Aplicaciones\Microsoft Forms\[Nombre del Formulario]`
3. **Enunciado y Solución Canónica Oficial:** Rúbrica con conceptos clave, descomposiciones, tasas, efectos de políticas o desarrollos formales esperados.

---

## 2. Fase 1: Mapeo y Anonimización Visual en Local

Antes de que el asistente examine las imágenes, se ejecuta el script auxiliar en Python (alojado en `alumnos/anonimizar_entregas_forms.py` o en `scratch/`):

1. **Lectura de Datos Oficiales:**
   * Censo oficial de clase unificado (Línea 1 y Línea 2): `alumnos/lista_alumnos.csv` (`DNI / id_norm`, `Nombre`, `Apellidos`, `Linea`, `Plan`).
   * Archivo Excel de respuestas de Microsoft Forms: extrae el correo/nombre del estudiante y el fichero de imagen asociado en la subcarpeta de entregas.
2. **Generación del Token Ciego:**
   * Aplica la fórmula oficial sobre los 8 dígitos del DNI:  
     $$\text{Token} = \text{str}(\text{DNI})[-5:-1]$$
   * Produce un código de 4 caracteres alfanuméricos 100% único por alumno (verificado sin colisiones para los 85 estudiantes de las Líneas 1 y 2).
3. **Censura de la Cabecera Manuscrita:**
   * Dado que los alumnos suelen escribir su nombre y apellidos a mano arriba en la hoja, el script enmascara con una banda opaca o recorta el **primer 14% superior** de cada fotografía.
   * Guarda las imágenes anonimizadas en: `scratch/ciegas_sXX/{TOKEN}.jpg`.
4. **Archivo Secreto de Correspondencia:**
   * Guarda el mapeo local temporal en `scratch/mapeo_ciego_sesion_XX.json` (que el evaluador NO consulta durante la corrección).

---

## 3. Fase 2: Transcripción Única y Persistencia en CSV (Regla de Oro de Tokens)

Para evitar el consumo innecesario de tokens en sucesivos barridos o revisiones de baremo:
1. **Primer Barrido Multimodal Único:**
   * El asistente examina las imágenes anonimizadas `scratch/ciegas_sXX/{TOKEN}.jpg` una sola vez mediante visión multimodal (`view_file`).
   * Extrae la transcripción literal y estructurada de lo escrito por el alumno en cada pregunta, junto con observaciones técnicas.
2. **Generación del Dataset Oficial de Transcripciones:**
   * Se guarda inmediatamente el archivo persistente en el subdirectorio de evaluación:  
     `Temas EB/Sesiones EB/Sesion XX/evaluacion/transcripciones_psll_sesion_XX.csv` con columnas:  
     `ID_Estudiante;Nombre_Completo;Token_Ciego;Transcripcion_P1;Transcripcion_P2;Observaciones`
3. **Regla de Oro para Barridos Sucesivos o Reevaluaciones:**
   * **Queda estrictamente prohibido volver a leer o abrir las imágenes** en segundas o terceras vueltas.
   * Cualquier recalificación, aplicación de criterios más flexibles, baremos parciales o revisión de notas debe operar **exclusivamente sobre el texto transcrito en `transcripciones_psll_sesion_XX.csv`**.

---

## 4. Fase 3: Evaluación y Calificación Continua (Escala 0 a 1.000 Puntos)

La evaluación valora el desempeño del estudiante de forma **continua, gradual y proporcionada** (no escalones rígidos):

### A. Desglose Aditivo por Preguntas (Retos Bimodales)
En retos compuestos por dos partes (habitualmente **500 puntos para P1** y **500 puntos para P2**, o el peso explícito que fije la sesión):

1. **Pregunta Teórico-Conceptual / Institucional (0 – 500 pts):**
   * **450 – 500 pts:** Rigor impecable. Identifica el mecanismo causal, marco institucional o efecto de la política con precisión terminológica.
   * **350 – 440 pts:** Intuición económica/laboral correcta y conclusión válida, pero con alguna laguna menor en la argumentación secundaria.
   * **200 – 340 pts:** Comprensión parcial; identifica la dirección general del efecto pero confunde el canal de transmisión o deja el razonamiento incompleto.
   * **100 – 190 pts:** Argumentación muy débil; cita términos clave de la sesión pero sin hilvanar la causalidad.
   * **0 pts:** Afirmación contraria a los fundamentos de la materia, disparate conceptual o en blanco.

2. **Pregunta Cuantitativa / Aplicada (0 – 500 pts):**
   * **450 – 500 pts:** Planteamiento, formulación y cálculos exactos. Erratas menores de redondeo no penalizan más de 20-30 puntos.
   * **350 – 440 pts:** Planteamiento conceptual y fórmulas 100% correctos, con fallo estrictamente aritmético que arrastra a las cifras finales.
   * **200 – 340 pts:** Planteamiento bien enfocado, pero se atasca en la sustitución de parámetros o deja a medias el cálculo.
   * **100 – 190 pts:** Expresa la relación de partida o tasa adecuada pero no sabe cómo aplicarla a los datos.
   * **0 pts:** Confusión grave de variables de partida que invalida todo el planteamiento, o en blanco.

---

### B. Tabla de Estados y Gradación Global (Suma de 0 a 1.000 Puntos)

| Rango de Puntos | Estado Oficial | Descripción Pedagógica |
| :---: | :--- | :--- |
| **900 – 1.000 pts** | `Apto (Sobresaliente)` | Dominio excelente. Planteamiento impecable y resolución casi o totalmente perfecta. |
| **700 – 899 pts** | `Apto (Notable)` | Dominio sólido. Comprensión clara de los modelos; fallos menores de precisión o cálculo aritmético. |
| **500 – 699 pts** | `Apto (Aprobado)` | Nivel suficiente. Comprensión básica de los conceptos y mecanismos, aunque con desarrollos incompletos o errores numéricos combinados. |
| **250 – 499 pts** | `No Apto (Mejorable)` | Insuficiente pero con trabajo. Demuestra captar alguna intuición o fórmula aislada, pero no alcanza la resolución adecuada. |
| **50 – 249 pts** | `No Apto (Insuficiente)` | Errores conceptuales graves de base o desarrollo testimonial de apenas unas líneas. |
| **0 pts** | `No Apto (Sin contenido)` / `No presentado` | Hoja en blanco, todo completamente erróneo sin base económica/laboral o no entrega. |

---

### C. Redacción del Feedback Formativo Individualizado
* **Extensión:** Conciso, pedagógico y constructivo (**máximo 40–50 palabras**).
* **Estructura obligatoria:**
  1. *Qué ha hecho bien:* Validación explícita del punto fuerte del alumno.
  2. *Motivo exacto del descuento de puntos:* Señalamiento claro de la deducción (ej. *«descuento de 150 pts por omitir la justificación del efecto desánimo»*).
  3. *Recomendación o felicitación final.*

---

## 5. Fase 4: Consolidación, Exportación y Pasaporte Digital

1. **Generación del CSV Oficial de Calificaciones:**  
   `Temas EB/Sesiones EB/Sesion XX/evaluacion/calificaciones_sesion_XX.csv` con columnas:  
   `Apellidos;Nombre;ID_Estudiante;Token_Ciego;Estado;Puntos;Retroalimentacion`
2. **Actualización Automática del Pasaporte Web Cifrado:**
   Ejecutar el compilador oficial:
   ```powershell
   py -3.11 "alumnos/compilar_pasaporte_evaluacion.py"
   ```
   Esto actualiza al instante `micro_apps/data/calificaciones_cifradas_psll.js` y `docs/data/calificaciones_cifradas_psll.js`, permitiendo que los alumnos consulten su calificación, transcripción y solución canónica de forma privada y cifrada.
3. **Informe Ejecutivo:** Generar resumen estadístico de la sesión (presentados, aptos, notas medias y errores más comunes).

---

## 6. Protocolo de Ficheros Temporales (`scratch/`)

Los ficheros auxiliares (imágenes anonimizadas en `scratch/ciegas_sXX/` y mapeos temporales) se eliminan solicitando confirmación explícita a Manuel tras cerrar la sesión con éxito.
