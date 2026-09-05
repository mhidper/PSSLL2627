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

## Marca e Identidad Visual (Skill `marca_psll`)

Este proyecto dispone de una skill de identidad visual de marca oficial en [.agents/skills/marca_psll/SKILL.md](file:///c:/Users/Usuario/Dropbox/DOCENCIA%20UPO/CURSO%2026-27/PSLL/.agents/skills/marca_psll/SKILL.md):
- **Ámbito:** Aplica obligatoriamente al redactar o editar documentos (`.docx`, apuntes, lecturas), diapositivas (`.pptx`) y figuras/gráficos en Python (`matplotlib`).
- **Paleta oficial (estilo editorial cálido):** Lienzo crema suave `#FDFBF7`, cajas `#FAF6F0`, texto de lectura `#4A3B32` (nunca negro puro), rojo ladrillo `#A33327` (titulares y serie principal), terracota `#D47B5A` (subtítulos y 2ª serie), ámbar `#C68B59`.
- **Tipografías:** `Poppins` / `Century Gothic` para titulares, `Calibri` / `Arial` para cuerpo de texto y tablas.
- **Gráficos en Python:** Aplicar siempre los `rcParams` de marca y añadir el pie de fuente y autoría con `anadir_firma()`.
