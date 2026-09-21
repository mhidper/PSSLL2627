# Protocolo de Banco de Preguntas y Modelos de Examen (PSLL · UPO)

Este documento y directorio constituyen el repositorio oficial estructurado de reactivos, preguntas conceptuales, dilemas de políticas sociolaborales y análisis cuantitativos acumulados sesión a sesión para la asignatura **Políticas Sociolaborales y de Empleo (PSLL)** (Grados en Relaciones Laborales y Recursos Humanos / Doble Grado en Derecho y RRLyRRHH) en la **Universidad Pablo de Olavide**.

---

## 1. Regla de Construcción Bimodal de Preguntas de Cierre de Sesión

Al diseñar el Reto Manuscrito Individual de Cierre (Fase 5 de cada sesión presencial de EB), se deben cumplir obligatoriamente dos principios pedagógicos:

1. **Cuestión Conceptual y Analítica Institucional:**
   * Debe evaluar la comprensión cualitativa profunda de los mecanismos causales, marco normativo/institucional o implicaciones de política pública (ej. desánimo laboral, sesgos de medición EPA, efectos incentivo vs. sustitución en subsidios, canales de transmisión del CLU).
   * Se responde en 3 o 4 líneas explicativas con rigor terminológico sin necesidad de cálculo complejo.

2. **Problema Aplicado o Cuantitativo con Experiencia Previa en Aula:**
   * **Prohibido evaluar cálculos o descomposiciones a ciegas:** Si en el reto final se solicita un cálculo formal (ej. tasas EPA, descomposición del CLU, elasticidades o coste laboral), en las diapositivas o en la micro-app del **Laboratorio Activo (Fase 4)** debe haberse desarrollado un **caso práctico análogo resuelto paso a paso**.
   * El estudiantado debe haber experimentado previamente la simulación o el cálculo antes de redactarlo de forma manuscrita e individual en papel.

---

## 2. Flujo de Trabajo Obligatorio al Cerrar Cada Sesión

Cada vez que se complete la evaluación de una sesión de Enseñanzas Básicas (`Sesion XX`), se debe seguir el siguiente protocolo:

1. **Extracción y Clasificación:** Registrar las preguntas del Reto Individual de la sesión y las soluciones canónicas de la cátedra.
2. **Incorporación a la Base de Datos:** Crear o actualizar el archivo correspondiente en:  
   `alumnos/examenes/base de datos/sesion_XX_preguntas.md`  
   Siguiendo el esquema estandarizado:
   * **Metadatos:** Identificador único, Sesión de origen, Tema oficial de la Guía Docente, Nivel de dificultad y Tiempo estimado (10 min).
   * **Enunciado Oficial:** Texto idéntico al proyectado en el aula con el código QR.
   * **Rúbrica y Solución Oficial Canónica:** Criterios precisos de corrección (Sobresaliente 1.000 pts, Parcial 500 pts, No Apto 0 pts) y errores conceptuales típicos descalificantes.
3. **Compilación al Pasaporte Digital:** Ejecutar el script:
   ```powershell
   py -3.11 "alumnos/compilar_pasaporte_evaluacion.py"
   ```
   para sincronizar las nuevas calificaciones y transcripciones en la base de datos cifrada Zero-Knowledge de la micro-app oficial.
