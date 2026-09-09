---
name: marca-psll
description: Aplica la identidad visual oficial de Políticas Sociolaborales (PSLL, UPO) — nueva paleta moderna de anillos de emparejamiento (Verde Pino, Salvia y Coral) y tipografía Outfit — y la convención de versionado de archivos, siempre que se cree, edite o revise cualquier apunte (.docx), presentación (.pptx) o gráfico/figura (Python/Matplotlib/Seaborn) de la asignatura. Actívala también al auditar o corregir material ya existente para comprobar que cumple la marca.
---

# Identidad Visual y Marca PSLL (Docencia UPO)

> [!IMPORTANT]
> Esta es la guía de marca **oficial y autorizada**. Coincide con el nuevo emblema geométrico de la asignatura (`assets/logo_psll_upo.png` e `isotipo_psll_upo.png`: anillos entrelazados de oferta y demanda laboral con onda transversal de políticas activas de empleo).

Actívala siempre que se genere o modifique:
1. **Documentos y apuntes:** `.docx`, guías didácticas, lecturas complementarias, Markdown.
2. **Presentaciones:** `.pptx` de cualquier tema de la asignatura.
3. **Figuras y gráficos:** scripts o gráficos con `matplotlib`/`seaborn` sobre datos del mercado de trabajo.

---

## 0. Convención de versionado de archivos (obligatoria)

Cuando se reelabora un `.docx` o `.pptx` ya existente del curso (apuntes, diapositivas), aprovechando al máximo el contenido y el material ya suministrado — no se parte de cero salvo que se indique explícitamente:

- El archivo nuevo se guarda **en el mismo directorio** que el original (misma carpeta `Apuntes/`, `Diapositivas/`, etc.).
- El nombre es el del archivo original **+ sufijo `_2627`** justo antes de la extensión. Ejemplos: `Tema 1 2526.docx` → `Tema 1 2526_2627.docx`; `Tema 5.pptx` → `Tema 5_2627.pptx`.
- El archivo original **nunca se sobrescribe ni se borra** al crear la versión `_2627` — queda como referencia/histórico hasta que el profesor decida qué hacer con él (p. ej. moverlo a `Versiones antiguas/`).
- Esta convención aplica a cualquier documento que resulte de ejecutar un checklist de `work_in_progress/` o de aplicar una nueva dinámica de clase sobre material ya existente.

---

## 1. Paleta de color oficial

| Rol | Nombre | HEX | Aplicación |
| :--- | :--- | :--- | :--- |
| Principal / Contraste | Verde Pino PSLL | `#113927` | Titulares principales, anillo izquierdo, botones de acción |
| Estructura | Verde Salvia | `#76927A` | Anillo derecho, subtítulos, serie principal de datos |
| Acento Dinámico | Coral Active Wave | `#E98F71` | Onda de políticas de empleo, cifras clave, llamadas de atención |
| Lienzo / Fondo Claro | Blanco Puro | `#FFFFFF` | Fondo de diapositivas y páginas de contenido |
| Tarjetas / Callouts | Verde Menta Tenue | `#F4F8F5` | Fondos suaves de tarjetas, contenedores de fórmulas |
| Tinta / Cuerpo | Verde Tinta | `#2F3A30` | Texto de lectura corrido (nunca negro puro) |
| Institucional UPO | Azul Marino UPO | `#0B1C36` | Escudo oficial UPO en tarjetas reservadas |

### Reglas críticas de contraste
- **Nunca** salvia `#76927A` como color de texto de cuerpo sobre fondos claros: contraste insuficiente.
- Texto de cuerpo: verde tinta `#2F3A30` sobre fondo claro; blanco `#FFFFFF` sobre fondos oscuros.
- Coral solo como acento puntual (una cifra, una palabra, un icono). Nunca un párrafo entero en coral.
- Secuencia para series de datos, en este orden: `#113927` → `#76927A` → `#E98F71` → `#EDB090` → `#566B56`.
- El escudo de la UPO (azul marino y oro) **no** se integra en la composición de color: colocarlo siempre discreto, en pie o esquina, sobre fondo blanco o claro, respetando su área de protección (sin recolorear ni deformar).

## 2. Tipografías

- **Titulares:** `Outfit` (Bold / Heavy), coincidiendo con la línea de Macroeconomía UPO. Alternativa de respaldo sin instalación: Inter o Segoe UI.
- **Cuerpo y datos:**
  - En documentos y apuntes (`.docx`): Calibri o Arial, 10.5–11.5 pt en texto corrido.
  - En presentaciones y diapositivas (`.pptx`): **16 pt Calibri obligatorio** para el texto de cuerpo de todas las slides (estándar adoptado para garantizar máxima legibilidad en proyección de aula; no usar tamaños inferiores en párrafos explicativos).
- **Prohibido:** usar Aptos como fuente por defecto.

## 3. Logos y activos (`assets/` y `marca/`)

- `logo_psll_upo.png` / `.svg` — logotipo oficial completo (anillos + titular y subtítulo institucional).
- `isotipo_psll_upo.png` / `.svg` — isotipo cuadrado de los anillos y onda.
- `psll_lockup.png` — logotipo horizontal compacto para cabeceras de diapositivas y pies.
- `psll_icon_transparent.svg` — isotipo transparente vectorial.
- `banner_aula_virtual_psll.png` — banner panorámico de cabecera del Aula Virtual.
- `psll_lockup.svg` / `psll_lockup.png` — logo horizontal (símbolo + "PSLL"). Cabeceras, pies, documentos.
- `psll_icon.svg` / `psll_icon_512.png` — icono sobre cuadrado menta redondeado.
- `psll_icon_transparent.svg` — símbolo sin fondo, para colocar sobre cualquier color; sello discreto en divisores.
- `favicon.ico`, `apple-touch-icon.png` — uso web.
- `upo_logo.jpg` — logo institucional UPO. Debe aparecer en todo material oficial, de forma discreta (ver reglas de contraste).

### Motivo visual
Líneas orgánicas, fluidas y tenues (filigranas de viento/vegetales), en un tono apenas más oscuro que el fondo, como textura sutil en portadas y divisores — nunca sobre zonas de texto. Tarjetas y bloques con esquinas redondeadas (radio ~8–12 pt).

## 4. Documentos de texto (`.docx` / Markdown)

- **Título del documento (H1):** 22–26 pt, bold, verde profundo `#566B56`.
- **Encabezado 1 (H2 — apartados principales):** 15–17 pt, bold, verde profundo `#566B56` (o salvia `#76927A` si el fondo es blanco puro), espacio anterior 12 pt / posterior 4 pt.
- **Encabezado 2 (H3 — subapartados):** 12.5–13.5 pt, bold, salvia `#76927A`.
- **Cuerpo de texto:** 10.5–11 pt, interlineado 1.15, espacio posterior 4–6 pt, verde tinta `#2F3A30`.
- **Cajas destacadas (callouts, casos, paradojas):** fondo crema `#F3EFDC`, borde izquierdo grueso 3 pt en coral `#E99073`, título en negrita coral, cuerpo en verde tinta.
- **Tablas:** cabecera con fondo salvia `#76927A` y texto blanco (o fondo crema con texto verde profundo en negrita y borde inferior salvia); filas alternas blanco/menta muy claro; bordes interiores finos `#C9DCC9`; alineación izquierda para texto, derecha para cifras/porcentajes.
- **Logo UPO:** en pie de página o portada, discreto, sobre fondo claro.

## 5. Presentaciones (`.pptx`)

Esta guía aporta la capa de marca; la mecánica de generación/edición de `.pptx` (crear, renderizar, QA visual) sigue las herramientas/skills de pptx disponibles en la sesión.

1. **Portada:** `psll_emblem.png` como protagonista; logo UPO discreto en pie o esquina sobre franja clara; título de la asignatura y del tema en Poppins.
2. **Índice / hoja de ruta** del tema, coherente con el número real de bloques del deck (verificar que no falte ninguno).
3. **Divisores de bloque:** fondo salvia `#76927A` o verde profundo `#566B56`, número y título en blanco, `psll_icon_transparent.svg` pequeño como sello.
4. **Diapositivas de contenido:** fondo blanco `#FFFFFF`; `psll_lockup.png` pequeño en una esquina superior (altura ≈ 0.3"), discreto — no repetir el emblema grande en cada slide. **Texto de cuerpo a 16 pt Calibri obligatorio** (asegura visibilidad y síntesis clara). Preferir párrafo desarrollado + un elemento visual (esquema, cifra grande, comparativa) frente a listas largas de viñetas.
5. **Datos:** gráficos con la secuencia de color de marca (sección 1); fuente citada al pie en 10–12 pt.
6. **Reto Final y Cierre Metacognitivo (10 min):** Slide con la pregunta de reto (100% basada en lo visto en clase y material previo) redactada a mano en papel + código QR de Microsoft Forms para subir foto (2 min). Slide posterior con la rúbrica y solución oficial comentada.
7. **Cierre:** síntesis + logo UPO institucional (presencia obligatoria en material oficial) + emblema PSLL. **Nunca** dejar marcas de la herramienta de generación (marcas de agua, créditos de terceros) en la diapositiva final.
8. **Prohibido:** líneas/subrayados bajo los títulos, barras o franjas decorativas en los bordes, diapositivas solo-texto.

## 6. Gráficos y figuras (Python / Matplotlib / Seaborn)

Usar siempre el módulo `references/estilo_graficos.py` de este skill:

```python
from estilo_graficos import aplicar_estilo_psll, BRAND_COLORS, COLOR_CYCLE, anadir_firma

aplicar_estilo_psll()
fig, ax = plt.subplots(figsize=(8, 4.5))
ax.plot(x, y, color=BRAND_COLORS['primary'], label='Tasa de Paro')
anadir_firma(ax, fuente="EPA, INE")
```

Reglas:
- Pie de autoría y fuentes obligatorio (usar `anadir_firma()`): `Fuente: [INE / EPA / Eurostat / SEPE] · Políticas Sociolaborales (UPO)`.
- Exportar con `dpi=300`, `bbox_inches='tight'`, formato `.png`.

## 7. Checklist de comprobación (QA de marca)

Antes de entregar cualquier documento, presentación o figura:
- [ ] ¿Paleta menta/salvia/coral (no la crema/terracota antigua)?
- [ ] ¿Verde tinta `#2F3A30` para cuerpo de texto (nunca negro puro ni salvia sobre menta)?
- [ ] ¿Coral usado solo como acento puntual, nunca en párrafos enteros?
- [ ] ¿Logo UPO presente en material oficial, discreto y sin deformar?
- [ ] ¿Figuras de Matplotlib con `aplicar_estilo_psll()` y firma de fuente/autoría?
- [ ] ¿Tablas con el formato editorial (cabecera salvia, bordes `#C9DCC9`)?
- [ ] ¿Tipografías coherentes (Poppins/Century Schoolbook para titulares, Calibri/Arial para cuerpo)?
- [ ] En `.pptx`: ¿sin marcas de la herramienta de generación en ninguna diapositiva?
