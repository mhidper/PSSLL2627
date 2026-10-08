# Manual de Uso de la Aplicación de Laboratorio · EPD PSLL
## Políticas Sociolaborales y de Empleo (102023) · Curso 2026-27
### Grados en Relaciones Laborales y RRHH / Doble Grado en Derecho y RRLL-RRHH
### Universidad Pablo de Olavide · Departamento de Economía, Métodos Cuantitativos e Historia Económica
**Profesor:** Manuel Alejandro Hidalgo Pérez

---

## 1. Acceso y Autenticación en la Plataforma

Todo el trabajo práctico de la asignatura se realiza a través de la **Web App Oficial de Laboratorio de PSLL**:

🌐 **Dirección Oficial de Acceso:**  
`https://mhidper.github.io/micro_apps/epd_laboratorio.html`

### Pasos de Identificación:
1. **Tu Acrónimo Institucional UPO:** En la pantalla inicial, introduce tu acrónimo oficial UPO (ej. `sagudel`, `laltucl`).
2. **Generación del Código EPD Permanente (`PSLL-EPD-XXXX`):** La plataforma genera tu código personal e intransferible. Anótalo; te identificará en todas las sesiones del semestre.
3. **Asignación Paramétrica de Caso:** Tu código desbloquea de forma automática tu cohorte específica (tramo de edad, género, ámbito territorial de contraste y ventana temporal).
4. **Monitor de Sesión:** En la cabecera superior se visualiza tu código, tiempo efectivo de trabajo y el estado de guardado.

---

## 2. Flujo de Trabajo en las Sesiones de Laboratorio

Cada sesión práctica (comenzando por la **EPD 1 · Radiografía del Desempleo Sénior y de Larga Duración**) se estructura en 4 fases:

1. **Fase 1 (00–15 min) · Activación y Sondeo Previo:** Vídeo-píldora introductoria y votación en el sondeo diagnóstico para capturar prejuicios intuitivos.
2. **Fase 2 (15–50 min) · Exploración Empírica:** Manejo interactivo de microdatos oficiales de la EPA (INE) y Eurostat con gráficos dinámicos y tablas territoriales.
3. **Fase 3 (50–70 min) · Checkpoint Cuantitativo (Fórmulas KaTeX):** Cálculo numérico de tasas oficiales (paro general, paro de larga duración >12 meses, muy larga duración >24 meses) con validación automática y tolerancia de cálculo.
4. **Fase 4 (70–90 min) · Redacción Técnica de Diagnóstico:** Redacción de los 4 ejes analíticos del informe, respaldando cada conclusión con datos empíricos.

---

## 3. Autoguardado Continuo y Sistema de Borradores Portátiles (.json)

Para garantizar que ningún estudiante pierda información ante fallos de conexión o cambios de equipo en el aula:

* **Autoguardado en Segundo Plano:** El navegador guarda tu trabajo cada 15 segundos en `localStorage`. Un indicador verde (`● Guardado`) confirma la persistencia local.
* **Descarga de Borrador Portátil (`💾 Borrador`):** En la barra superior, pulsa este botón para descargar un archivo `.json` (`borrador_epd1_[usuario]_[codigo].json`). Descárgalo siempre antes de finalizar la clase o si te cambias de ordenador.
* **Carga de Borrador Portátil (`📂 Cargar Borrador (.json)`):** En la pantalla de bienvenida, permite restaurar tu sesión al 100% en cualquier otro navegador u ordenador sin tener que repetir cálculos ni textos.

---

## 4. Integridad Académica y Sistema Anti-IA

* **Casos Paramétricos Únicos:** Cada estudiante cuenta con datos distintos; consultas generales a herramientas de IA generarán cifras erróneas que bloquearán los checkpoints.
* **Detector de Pegado Masivo (*Clipboard Trap*):** Las cajas de texto detectan el copiado y pegado masivo y analizan la velocidad de tecleo (WPM). El texto debe redactarse directamente desde el teclado.
* **Validación en DOM Local:** Los datos residen en la aplicación y requieren cálculo aritmético exacto.
* **Telemetría Docente:** Se registran tiempos de permanencia, intentos de validación y marcas temporales.

---

## 5. Sellado Criptográfico SHA-256 y Entrega Oficial

1. Al completar los cálculos y la redacción, se desbloquea el botón de **Entrega Definitiva**.
2. La plataforma genera un **Sello Criptográfico SHA-256** único con marca de tiempo.
3. Se produce un **bloqueo post-entrega** para certificar la integridad académica del informe.
4. Puedes descargar tu **comprobante oficial firmado en PDF**.
5. La calificación y el sello se sincronizan de forma transparente con el **Pasaporte de Evaluación Continua**.

---

## 6. Preguntas Frecuentes (FAQ)

* **¿Cómo introduzco los decimales en los cálculos?**  
  Utiliza punto (.) o coma (,) según se indique y calcula sobre la población activa de tu cohorte específica.
* **¿Qué hago si se cierra el navegador?**  
  Vuelve a entrar e introduce tu acrónimo: el autoguardado restaurará tu sesión. Si cambiaste de ordenador, utiliza el botón `📂 Cargar Borrador (.json)`.
* **¿Puedo entregar desde casa?**  
  No. La entrega debe realizarse dentro del aula informática durante el horario oficial de la sesión.
