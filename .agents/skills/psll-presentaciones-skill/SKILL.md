---
name: psll-presentaciones-skill
description: "Usar SIEMPRE que el usuario pida crear, editar o maquetar una presentación, deck, diapositivas (.pptx / .pdf y .html interactivo) para la asignatura Políticas Sociolaborales (PSLL) de la UPO. A partir de la Sesión 12, genera OBLIGATORIAMENTE las presentaciones en DOBLE FORMATO dentro de la carpeta de cada sesión: (1) Formato Clásico (.pptx + .pdf) como Plan B y (2) Formato Web Interactivo (.html) con la paleta PSLL, marca de agua de anillos entrelazados, recorte de prensa fundamental, las 5 fases docentes y gráficos SVG hiper-dinámicos animados por beats."
---

# PSLL · Presentaciones en Doble Formato (`.pptx`/`.pdf` + `.html` Interactivo)

Genera presentaciones de la asignatura **Políticas Sociolaborales y de Empleo (UPO)** con identidad de marca coherente.

> [!IMPORTANT]
> **REGLA DE ORO DEL DOBLE FORMATO OBLIGATORIO (A partir de la Sesión 12):**
> Toda sesión debe generarse simultáneamente en **dos formatos completos e independientes guardados en la carpeta de la sesión** (`Temas EB/Sesiones EB/Sesion XX/`), sin crear portal web externo (`index.html`):
> 1. **Formato 1 (Clásico / Plan B):** Presentación PowerPoint nativa (`Sesion XX - [Título].pptx`) + exportación sincronizada a PDF (`Sesion XX - [Título].pdf`), generada con `python-pptx` y figuras PNG a 300 DPI. No se sustituye nunca por el HTML; se mantiene siempre como Plan B operativo.
> 2. **Formato 2 (Interactivo Hiper-Dinámico):** Presentación web autocontenida en un único archivo (`Sesion XX - [Título].html`), inspirada en el motor técnico de *Economía Aplicada* pero **100% adaptada a la paleta oficial de PSLL**, con **marca de agua vectorial de los anillos entrelazados**, **recorte de prensa fundamental**, las **mismas 5 fases docentes** y **gráficos SVG 100% dinámicos y animados por *beats***.

## Orden de trabajo (obligatorio)

1. **Leer la guía de marca** `Logos y skills/BRAND.md` (paleta, tipografías, logos, contraste). Es la fuente de verdad de colores.
2. **Generar el Formato 1 (`.pptx` + `.pdf`)** aplicando la estructura canónica de PSLL y verificando visualmente el PDF.
3. **Generar el Formato 2 (`.html` interactivo)** en la misma carpeta de la sesión (`Temas EB/Sesiones EB/Sesion XX/`), programando todos los gráficos de la sesión como **SVG dinámicos animados por *beats***.

## Paleta oficial (resumen — detalle en BRAND.md y marca/guia_de_estilo.md · Aplica a PPTX, PDF y HTML)

- Fondos claros: blanco puro `#FFFFFF` y menta tenue `#F4F8F5` para tarjetas (borde `#C2D8C9`).
- Fondos oscuros / contraste: verde pino `#113927` o verde salvia `#76927A`, con texto blanco `#FFFFFF`.
- Texto de cuerpo sobre claro: verde tinta `#2F3A30` (nunca salvia sobre blanco ni negro puro).
- Acento: coral dinámico `#E98F71`, para cifras clave, llamadas de atención, bordes de recorte/QR o la onda de políticas.
- Series de datos, en orden: `#113927` (pino), `#76927A` (salvia), `#E98F71` (coral), `#EDB090` (melocotón), `#566B56` (verde intermedio).

## Tipografías

- Titulares: **Outfit** (Bold / Heavy), en sintonía directa con Macroeconomía UPO. Alternativa de respaldo: Inter o Segoe UI.
- Cuerpo: **16 pt Calibri obligatorio** en `.pptx` (tamaño estándar fijado para proyección en aula; no usar tamaños inferiores en párrafos de contenido). Nunca Aptos. En `.html`: `Calibri`, `Inter` o `Work Sans` a escala equivalente ($\ge 19\text{–}22\text{ px}$ sobre lienzo `1600×900`), `Newsreader` / `Georgia` para el recorte de prensa y `JetBrains Mono` / `IBM Plex Mono` para fórmulas y datos.

## Resumen Técnico de Ambos Formatos

- **Formato 1 (`.pptx` + `.pdf`):** Portada en `#113927` con `logo_psll_upo.png` (`4.800" × 2.618"`, ratio $1.833$) y franja blanca inferior con `upo_logo.jpg` (`0.495" × 0.700"`, ratio $0.707$); diapositivas de contenido con `psll_lockup.png` (`1.013" × 0.320"`, ratio $3.167$); 5 fases cronometradas; subíndices nativos y códigos QR cuadrados `1:1`.
- **Formato 2 (`.html` interactivo):** Lienzo `#stage` fijo `1600×900 px` autoescalable; capa `#stage > .watermark-layer` fija (`z-index: 1`) con los **dos anillos entrelazados de PSLL y la onda coral**; diapositiva de apertura con **recorte de prensa (`.newspaper-card`)** e insignias de hilo conductor (`.news-thread-badge`); motor reversible de *beats* (`nextFrag` / `prevFrag`), quiz interactivo en vivo + QR, notas del orador (`N`) y **gráficos SVG 100% dinámicos (`tween`, `stroke-dashoffset`, barras animadas, contadores `.bignum`)**.

