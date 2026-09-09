# Contexto y Reglas del Proyecto PSLL (2026-27)

## Integración con Google NotebookLM

Este proyecto está vinculado permanentemente al cuaderno de NotebookLM:
- **Título**: *Estrategias y Dinámicas para un Aprendizaje Significativo y Práctico*
- **Notebook ID**: `b94a743f-30fe-4b04-b7b4-d4da08e06d16`
- **Notebook URL**: `https://notebook.google.com/notebook/b94a743f-30fe-4b04-b7b4-d4da08e06d16`
- **Enfoque y Contenido**: Innovación pedagógica, aula invertida (*Flipped Classroom*), Aprendizaje Basado en Problemas/Proyectos (ABP), narrativas transmedia, gamificación y evaluación formativa orientados a la docencia de **Políticas Sociolaborales y de Empleo (PSLL)** (especialmente para el diseño de las sesiones prácticas EPD y dinámicas participativas).

### Instrucciones para el Asistente:
1. **Consulta de Contexto**: Cuando Manuel solicite diseño de actividades EPD, metodologías docentes, redacción de contenidos, dinámicas activas o alineación con guías de aprendizaje, debes consultar este cuaderno utilizando `notebook_query` con `notebook_id: "b94a743f-30fe-4b04-b7b4-d4da08e06d16"`.
2. **Gestión de Autenticación**: Si una llamada a las herramientas MCP de `notebooklm` falla con un error de autenticación expirada (`Authentication expired` o `RPC Error 16`):
   - Intenta primero recargar credenciales con `refresh_auth`.
   - Si persiste, avisa brevemente a Manuel para que ejecute en la terminal:
     ```powershell
     notebooklm-mcp-auth
     ```
     o que proporcione la cookie actualizada para reconectar.

## Metodología Docente de las Sesiones Teóricas (EB): El Ciclo del Choque Cognitivo y el Reto Final

En el diseño de las sesiones teóricas (EB) y sus diapositivas:
- **Apertura con Sondeo Previo (Bloque 1):** Arranca siempre con una pregunta de sondeo (en Microsoft Forms con QR institucional o Mentimeter) antes de mostrar datos, figuras o teorías, capturando los prejuicios espontáneos e intuiciones populares de los alumnos.
- **Choque empírico posterior:** Inmediatamente después del sondeo, se proyectan las figuras y datos reales (EPA, Eurostat, OCDE) para desmentir empíricamente el prejuicio mayoritario, creando la necesidad intelectual del modelo teórico.
- **Cierre con Reto Manuscrito y Subida Fotográfica (Bloque 5 · Regla de Oro):**
  - Toda sesión EB concluye con un **reto o caso práctico individual de 10 minutos**.
  - **Vinculación obligatoria:** Las preguntas deben estar **100% basadas en lo explicado en clase ese día y en el material previo** colgado en el aula virtual. No requieren memorismo enciclopédico ni fórmulas oscuras; su fin es **demostrar atención y comprensión conceptual en el aula**. El docente conoce la pregunta de antemano para asegurar que ese mecanismo se enfatiza con nitidez durante la sesión.
  - **Mecánica:** Se redacta **a mano en papel (10 min)** en entorno controlado $\rightarrow$ A la orden del profesor, se proyecta el **Código QR de Microsoft Forms (cuenta UPO)** para subir una foto nítida de la hoja manuscrita (2 min).
  - **Incentivo / Gamificación:** Las entregas válidas acumulan puntos en el seguimiento que desbloquean **beneficios tangibles para el examen final (70%)** (por ejemplo: comodín para descartar una pregunta en el examen o bonificación de nota), incentivando directamente la asistencia y la concentración activa en el aula.
  - **Corrección escalable:** Las fotos subidas a OneDrive se transcriben y corrigen con IA de visión multimodal aplicando la rúbrica oficial de la sesión.

## Marca e Identidad Visual Oficial

Este proyecto cuenta con una identidad visual moderna y vanguardista de inspiración institucional (*Modern Labor Economics & Think Tank*), homologada con la línea gráfica de **Macroeconomía UPO**, documentada en [Logos y skills/marca/guia_de_estilo.md](file:///c:/Users/Usuario/Dropbox/DOCENCIA%20UPO/CURSO%2026-27/PSLL/Logos%20y%20skills/marca/guia_de_estilo.md) y [Logos y skills/BRAND.md](file:///c:/Users/Usuario/Dropbox/DOCENCIA%20UPO/CURSO%2026-27/PSLL/Logos%20y%20skills/BRAND.md):
- **Símbolo Oficial:** Dos anillos entrelazados (oferta de trabajo en Verde Pino `#113927` y demanda en Verde Salvia `#76927A`) atravesados por una onda aerodinámica transversal en Coral Activo (`#E98F71`, mediación y políticas activas de empleo).
- **Ámbito de aplicación:** Aplica obligatoriamente al redactar o editar documentos (`.docx`, apuntes, lecturas), diapositivas (`.pptx`) y figuras/gráficos en Python (`matplotlib`).
- **Paleta oficial definitiva:**
  - Lienzo y fondos base: Blanco puro `#FFFFFF`.
  - Color primario y titular: Verde Pino PSLL `#113927`.
  - Estructura y subtítulo: Verde Salvia `#76927A`.
  - Acento dinámico: Coral Active Wave `#E98F71`.
  - Tarjetas y callouts suaves: Verde Menta Tenue `#F4F8F5`.
  - Texto de lectura (cuerpo): Verde Tinta `#2F3A30` (nunca negro puro).
  - Escudo institucional: Azul Marino UPO `#0B1C36`.
- **Tipografías oficiales:**
  - Titulares: `Outfit` (Bold / Heavy), en sintonía con Macroeconomía. Alternativa de respaldo: `Inter` o `Segoe UI`.
  - Cuerpo de texto en diapositivas: **16 pt Calibri obligatorio** para legibilidad completa en proyección de aula. Nunca `Aptos`.
- **Gráficos en Python:** Usar la paleta oficial (Pino `#113927`, Salvia `#76927A`, Coral `#E98F71`) con pie de autoría y fuente institucional.
- **Histórico:** Se eliminaron definitivamente las versiones antiguas ilustradas (libros/pluma) y terracota. La única referencia válida es la marca de anillos de emparejamiento.

## Maquetación y Formato de Apuntes (Skill de Maquetación)

Para la edición, diseño y maquetación de los documentos de apuntes (`.docx`) de la asignatura:
- Se debe utilizar obligatoriamente la skill de maquetación ubicada en `.skills/psll-apuntes-skill/`.
- Esta skill gobierna la aplicación sistemática de la identidad visual de PSLL:
  - Tipografías oficiales (`Poppins` para títulos, `Calibri` para cuerpo de texto).
  - Paleta oficial (títulos en `#566B56`, subtítulos en `#76927A`, texto en verde tinta `#2F3A30`, cajas de aviso en coral `#E99073` / melocotón `#EDB090`).
  - Cajas destacadas (*Callout boxes*) con fondos suaves e iconos semánticos.
  - Tablas estilizadas con cabeceras en verde profundo y alternancia de filas.
  - Inserción de figuras de datos en alta resolución (300 DPI) generadas con el motor de gráficos `matplotlib` adaptado a la marca.
  - Encabezados con emblema oficial (`psll_emblem.png`) y pie de página con paginación dinámica.
- Se prohíbe maquetar apuntes de forma manual o ad-hoc sin apoyarse en este motor de estilo, asegurando la reproducibilidad y homogeneidad total en todos los temas del curso.

## Remasterización Gráfica y Figuras Académicas (Skill de Figuras)

Para la generación, vectorización y rediseño de esquemas y gráficos de la asignatura:
- Se debe utilizar la skill gráfica modular ubicada en `.skills/psll-figuras-skill/`.
- Trabaja de manera coordinada con `psll-apuntes-skill`:
  - `psll-apuntes-skill` extrae las figuras del original a `Temas EB/Tema X/figuras/originales/`.
  - `psll-figuras-skill` genera las versiones en alta resolución (300 DPI) con la paleta oficial (menta/salvia/coral) en `Temas EB/Tema X/figuras/remasterizadas/`.
  - Al maquetar, las versiones remasterizadas sustituyen automáticamente a las originales sin pérdida de ninguna figura.
  - Las figuras remasterizadas son reutilizables transversalmente en apuntes (`.docx`), presentaciones (`.pptx`) y actividades EPD.
