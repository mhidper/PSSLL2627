# Registro y Memoria de Sesión: Desarrollo y Despliegue de la EPD 1 (Laboratorio y Telemetría)

**Asignatura:** Políticas Sociolaborales y de Empleo (PSLL) · Grado en Relaciones Laborales y Recursos Humanos  
**Universidad:** Universidad Pablo de Olavide (UPO) · Curso Académico 2026-27  
**Fecha:** 1 de octubre de 2026  
**Conversation ID Antigravity:** `5a76b4c0-d206-4909-88e9-df4942bd72fd`

---

## 1. Resumen Ejecutivo de la Sesión

En esta sesión se han diseñado, desarrollado y puesto en producción todos los elementos técnicos, pedagógicos y audiovisuales correspondientes a la **EPD 1: Laboratorio de Diagnóstico del Desempleo Sénior en Andalucía**:

1. **Laboratorio Interactivo Web (`epd_laboratorio.html`):**
   - Arquitectura en 3 fases: Fase 0 (Briefing y asignación ciega de caso A o B según acrónimo del estudiante), Fase 1 (Exploración EPA, tarjetas de impacto y taller de cálculo dinámico de tasa de paro y tasa PLD), Fase 2 (Redacción analítica en 4 ejes guiados y sellado SHA-256).
   - Generación de informe oficial maquetado en A4 mediante estilos `@media print` para exportación en PDF y subida al Aula Virtual.
   - Sincronización dinámica de enunciados, tarjetas y placeholders para garantizar coherencia absoluta entre el caso asignado (45-54 años vs. 55+ años) y las preguntas del informe.

2. **Sistema de Telemetría Docente en Tiempo Real:**
   - Webhook en Google Apps Script enlazado a Google Sheets para monitorizar la actividad individual de los 78 estudiantes.
   - Registro de accesos (`ACCESO_INICIAL`), avance de fases (`CAMBIO_FASE`), interacciones con el taller de cálculo (`CALCULO_VERIFICADO`), tiempo de permanencia y generación final del informe oficial con hash de integridad (`GENERACION_INFORME`).
   - Acceso directo creado en la carpeta del curso: [Telemetria_EPD1_GoogleSheets.url](file:///c:/Users/Usuario/Dropbox/DOCENCIA%20UPO/CURSO%2026-27/PSLL/EPD/Telemetria_EPD1_GoogleSheets.url).

3. **Recursos Audiovisuales y de Comunicación:**
   - **Guión Institucional de 45 segundos:** [guion_video_informativo_epd1.md](file:///c:/Users/Usuario/Dropbox/DOCENCIA%20UPO/CURSO%2026-27/PSLL/EPD/guion_video_informativo_epd1.md) estructurado en 4 escenas con locución en off, planos de cámara, estilo visual y código de colores PSLL (Verde Pino, Salvia y Coral).
   - **Master Prompt para IA Generativa de Vídeo:** [prompt_ia_video_epd1.md](file:///c:/Users/Usuario/Dropbox/DOCENCIA%20UPO/CURSO%2026-27/PSLL/EPD/prompt_ia_video_epd1.md) listo para su uso directo en plataformas como HeyGen, Sora, Runway o Pika Labs.

---

## 2. Enlaces y Recursos Activos

- **Web en Vivo (GitHub Pages):** [https://mhidper.github.io/micro_apps/epd_laboratorio.html](https://mhidper.github.io/micro_apps/epd_laboratorio.html)
- **Hoja de Telemetría Docente (Google Sheets):** [https://docs.google.com/spreadsheets/d/1-BmRwUdXXBVbepSCavqwYexFvLbyImOiloVHnEFC-zw/edit?gid=0#gid=0](https://docs.google.com/spreadsheets/d/1-BmRwUdXXBVbepSCavqwYexFvLbyImOiloVHnEFC-zw/edit?gid=0#gid=0)
- **Endpoint Webhook (Apps Script):** `https://script.google.com/macros/s/AKfycbyr7IVupbtb38B1ZCyclcfkGez2lnuoWH5bRy6L4yqyCqZMNmVu2jJaeurxc3ygCtT4/exec`
- **Código Fuente Local:** [epd_laboratorio.html](file:///c:/Users/Usuario/Dropbox/DOCENCIA%20UPO/CURSO%2026-27/PSLL/EPD/epd_laboratorio.html)

---

## 3. Corrección Clave Realizada en el Laboratorio

- **Problema detectado:** Al estudiante asignado al **Caso B (55+ años)** le aparecían en el informe de la Fase 2 preguntas que solicitaban analizar el colectivo de "más de 45 años".
- **Ajuste aplicado:** Se adaptaron los elementos del DOM en tiempo de ejecución:
  - **Caso A (45-54 años):** Preguntas centradas en magnitud decenal, tasa del 13,9% frente a España (9,8%) y políticas de inserción laboral.
  - **Caso B (55+ años):** Preguntas centradas en la ganancia de cuota relativa (11,7% a 19,7%), brecha estructural frente a la UE-27 (13,5% vs. 4,9%, 53,4% de parados >2 años) y barreras de edadismo en RRHH para evitar la desconexión total del mercado.
  - **PDF Descargable:** Títulos y subtítulos alineados exactamente con la cohorte del estudiante.
