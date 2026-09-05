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

## Marca e Identidad Visual

Este proyecto tiene una identidad visual oficial basada en el emblema real de la asignatura (`Logos y skills/psll-presentaciones-skill/assets/psll_emblem.png`), documentada en [Logos y skills/BRAND.md](file:///c:/Users/Usuario/Dropbox/DOCENCIA%20UPO/CURSO%2026-27/PSLL/Logos%20y%20skills/BRAND.md) y en [Logos y skills/psll-presentaciones-skill/SKILL.md](file:///c:/Users/Usuario/Dropbox/DOCENCIA%20UPO/CURSO%2026-27/PSLL/Logos%20y%20skills/psll-presentaciones-skill/SKILL.md) (para presentaciones). La versión equivalente para Claude Code vive en `.claude/skills/marca-psll/SKILL.md`.
- **Ámbito:** Aplica obligatoriamente al redactar o editar documentos (`.docx`, apuntes, lecturas), diapositivas (`.pptx`) y figuras/gráficos en Python (`matplotlib`).
- **Paleta oficial (menta/salvia/coral, la que coincide con el emblema real):** Lienzo menta `#E1F6EA`, salvia `#76927A` (estructura y serie principal), verde profundo `#566B56` (títulos y contraste fuerte), verde tinta `#2F3A30` (texto de cuerpo — nunca negro puro), coral `#E99073` (acento puntual, nunca párrafos enteros), melocotón `#EDB090` (acento suave).
- **Tipografías:** `Poppins` para titulares (alternativa: Century Schoolbook/Cambria), `Calibri` / `Arial` para cuerpo de texto y tablas. Nunca `Aptos`.
- **Gráficos en Python:** usar el módulo de estilo con la paleta menta/salvia/coral y añadir siempre el pie de fuente y autoría.
- **Nota:** existió una guía anterior con paleta crema/terracota (`Logos y skills/marca_psll/`) que no coincidía con el logo real; se eliminó del proyecto — no debe reintroducirse ni usarse como referencia.
