# Contexto y Reglas del Proyecto PSLL (2026-27)

## Integración con Google NotebookLM

Este proyecto está vinculado permanentemente al cuaderno de NotebookLM de la asignatura **Políticas Sociolaborales y de Empleo (PSLL)**:

- **Notebook ID**: `b94a743f-30fe-4b04-b7b4-d4da08e06d16`
- **Notebook URL**: `https://notebooklm.google.com/notebook/b94a743f-30fe-4b04-b7b4-d4da08e06d16`

### Instrucciones para el Asistente:
1. **Consulta de Contexto**: Cuando Manuel solicite información, redacción de contenidos, diseño de actividades EPD, dudas sobre temarios o alineación con las guías docentes, debes consultar este cuaderno utilizando la herramienta MCP `notebook_query` pasando:
   - `notebook_id`: `"b94a743f-30fe-4b04-b7b4-d4da08e06d16"`
   - `query`: La consulta específica o palabras clave necesarias para resolver la petición.
2. **Gestión de Autenticación**: Si una llamada a las herramientas MCP de `notebooklm` falla con un error de autenticación expirada (`Authentication expired` o `RPC Error 16`):
   - Intenta primero recargar credenciales con `refresh_auth`.
   - Si persiste, avisa brevemente a Manuel para que ejecute en la terminal:
     ```powershell
     notebooklm-mcp-auth
     ```
     o que proporcione la cookie actualizada para reconectar.
