---
name: marca-psll
description: Aplica la identidad visual oficial de Políticas Sociolaborales (PSLL, UPO) — paleta menta/salvia/coral del emblema PSLL real — siempre que se cree, edite o revise cualquier apunte (.docx), presentación (.pptx) o gráfico/figura (Python/Matplotlib/Seaborn) de la asignatura. Actívala también al auditar o corregir material ya existente para comprobar que cumple la marca.
---

# Identidad Visual y Marca PSLL (Docencia UPO)

> [!IMPORTANT]
> Esta es la guía de marca **autorizada**. Coincide con el emblema real de la asignatura (`assets/psll_emblem.png`: libros + pluma, "PS" en salvia y "LL" en coral, sobre fondo menta). Existe otra guía anterior en el repositorio (`Logos y skills/marca_psll/`, paleta crema/terracota) que **no** coincide con el logo y no debe usarse — está pendiente de limpieza/archivo.

Actívala siempre que se genere o modifique:
1. **Documentos y apuntes:** `.docx`, guías didácticas, lecturas complementarias, Markdown.
2. **Presentaciones:** `.pptx` de cualquier tema de la asignatura.
3. **Figuras y gráficos:** scripts o gráficos con `matplotlib`/`seaborn` sobre datos del mercado de trabajo.

---

## 1. Paleta de color oficial (muestreada del emblema)

| Rol | Nombre | HEX | Aplicación |
| :--- | :--- | :--- | :--- |
| Principal | Menta | `#E1F6EA` | Fondos claros, lienzos, portadas |
| Estructura | Salvia | `#76927A` | Volúmenes, fondos de cabecera, serie principal de datos, "PS" |
| Contorno / texto fuerte | Verde profundo | `#566B56` | Líneas, sombras, títulos sobre fondo claro, fondos oscuros de portada/divisor |
| Tinta / cuerpo | Verde tinta | `#2F3A30` | Texto de cuerpo sobre fondo claro |
| Acento | Coral | `#E99073` | Resaltes, cifras clave, "LL", una palabra — nunca párrafos enteros |
| Acento suave | Melocotón | `#EDB090` | Acentos secundarios, tercera serie de datos |
| Neutro cálido | Crema | `#F3EFDC` | Tarjetas, cajas destacadas — **no** como fondo de página/diapositiva a sangre completa |
| Blanco | — | `#FFFFFF` | Fondo de diapositivas y páginas de contenido |
| Apoyo | Verde claro de apoyo | `#9DBE8F` | Quinta serie de datos, categorías de apoyo |

### Reglas críticas de contraste
- **Nunca** salvia `#76927A` como color de texto de cuerpo sobre menta: contraste insuficiente.
- Texto de cuerpo: verde tinta `#2F3A30` sobre fondo claro; blanco `#FFFFFF` sobre salvia o verde profundo.
- Coral solo como acento puntual (una cifra, una palabra, un icono). Nunca un párrafo entero en coral.
- Secuencia para series de datos, en este orden: `#76927A` → `#E99073` → `#EDB090` → `#566B56` → `#9DBE8F`.
- El escudo de la UPO (azul marino y oro) **no** se integra en la composición pastel: colocarlo siempre discreto, en pie o esquina, sobre fondo blanco o claro, respetando su área de protección (sin recolorear ni deformar).

## 2. Tipografías

- **Titulares:** Poppins (bold/semibold) — geométrica redondeada, coherente con el logotipo. Alternativa segura sin instalación: Century Schoolbook o Cambria.
- **Cuerpo y datos:** Calibri o Arial, 10.5–11.5 pt en texto, 9–10 pt en tablas/gráficos.
- **Prohibido:** usar Aptos como fuente por defecto.

## 3. Logos y activos (`assets/`)

- `psll_emblem.png` — emblema principal ilustrado. Portadas, primera diapositiva, pósters. No reducir por debajo de ~120 px.
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
4. **Diapositivas de contenido:** fondo blanco `#FFFFFF`; `psll_lockup.png` pequeño en una esquina superior (altura ≈ 0.3"), discreto — no repetir el emblema grande en cada slide. Preferir párrafo desarrollado + un elemento visual (esquema, cifra grande, comparativa) frente a listas largas de viñetas.
5. **Datos:** gráficos con la secuencia de color de marca (sección 1); fuente citada al pie en 10–12 pt.
6. **Cierre:** síntesis + logo UPO institucional (presencia obligatoria en material oficial) + emblema PSLL. **Nunca** dejar marcas de la herramienta de generación (marcas de agua, créditos de terceros) en la diapositiva final.
7. **Prohibido:** líneas/subrayados bajo los títulos, barras o franjas decorativas en los bordes, diapositivas solo-texto.

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
