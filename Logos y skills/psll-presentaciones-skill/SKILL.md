---
name: psll-presentaciones
description: "Usar SIEMPRE que el usuario pida crear, editar o maquetar una presentación, deck, diapositivas o .pptx para la asignatura Políticas Sociolaborales (PSLL) de la UPO. Activar ante términos como 'presentación', 'diapositivas', 'slides', 'deck', 'transparencias', 'PowerPoint' en el contexto de PSLL, de cualquiera de sus temas (mercado de trabajo, políticas activas/pasivas de empleo, flexibilidad, pensiones, EPL, etc.), o cuando se mencione el emblema PSLL. Esta skill aplica la identidad visual PSLL (paleta, tipografías, logos, motivo) sobre la mecánica de generación de .pptx."
---

# PSLL · Presentaciones

Genera presentaciones de la asignatura **Políticas Sociolaborales (UPO)** con identidad de marca coherente. Esta skill **NO** sustituye a la skill `pptx`: aporta la capa de marca; la mecánica (crear, renderizar, QA) se ejecuta con `pptx`.

## Orden de trabajo (obligatorio)

1. **Leer la guía de marca** `assets/BRAND.md` (paleta, tipografías, logos, contraste). Es la fuente de verdad de colores.
2. **Leer la skill `pptx`** (`/mnt/skills/public/pptx/SKILL.md`) y, para crear desde cero, su `pptxgenjs.md`. Toda la generación, conversión a imagen y QA visual sigue esa skill.
3. Aplicar la marca PSLL descrita aquí.
4. **QA visual con subagente** (según la skill `pptx`) antes de entregar.

## Paleta (resumen — detalle en BRAND.md)

- Fondos claros: blanco `#FFFFFF` y menta `#E1F6EA`.
- Fondos oscuros (portada, divisores, cierre): salvia `#76927A` o verde profundo `#566B56`, con texto blanco.
- Texto de cuerpo sobre claro: verde tinta `#2F3A30` (nunca salvia, contraste insuficiente).
- Acento: coral `#E99073`, solo para cifras clave, una palabra o un icono.
- Series de datos, en orden: `#76927A`, `#E99073`, `#EDB090`, `#566B56`, `#9DBE8F`.
- **No** usar fondos crema/beige a sangre completa (la skill pptx lo desaconseja). El crema `#F3EFDC` es para tarjetas/acentos, no para el fondo de la diapositiva.

## Tipografías

- Titulares: **Poppins** (bold). Alternativa segura: Century Schoolbook o Cambria.
- Cuerpo: **Calibri** o Arial. Nunca Aptos.
- Tamaños: título 36–44 pt · cabecera de sección 20–24 pt · cuerpo 14–16 pt · pie/cita 10–12 pt.

## Logos en las diapositivas (carpeta `assets/`)

- **Portada:** `psll_emblem.png` como protagonista. Logo **UPO** (`upo_logo.jpg`) discreto en un pie o esquina, sobre franja/fondo claro. Título de la asignatura y del tema con Poppins.
- **Divisores de sección:** fondo salvia o verde profundo, número y título de bloque en blanco, `psll_icon_transparent.svg` pequeño como sello.
- **Diapositivas de contenido:** `psll_lockup.png` pequeño en una esquina superior (altura ≈ 0,3"), discreto. No repetir el emblema grande en cada slide.
- **Cierre / contraportada:** datos de contacto + logo **UPO** institucional (presencia obligatoria en material oficial) + emblema PSLL.
- Respetar el área de protección de la UPO: no recolorear, no deformar, no integrarlo en el pastel.

## Motivo y composición

- Repetir el **motivo de líneas orgánicas** muy tenues (un tono más oscuro que el fondo) como textura sutil en portada y divisores. Nunca sobre zonas de texto.
- Esquinas redondeadas en tarjetas y bloques (radio ~8–12 pt).
- Iconos en círculos de color de marca junto a cabeceras de sección.
- **Prohibido** (heredado de la skill pptx y reforzado aquí): líneas/subrayados bajo los títulos, barras o franjas de color decorativas en bordes, y diapositivas solo-texto. Cada diapositiva lleva un elemento visual.

## Estructura recomendada de un deck PSLL

1. **Portada** — emblema PSLL, título del tema, "Políticas Sociolaborales · UPO", logo UPO discreto.
2. **Índice / hoja de ruta** del tema.
3. **Divisor de bloque** (salvia/verde profundo) por cada apartado.
4. **Contenido** — preferir párrafo desarrollado y un visual (esquema, dato grande, comparativa) frente a listas largas de viñetas (coherente con la preferencia "menos items, más texto").
5. **Datos y Figuras Oficiales** — gráficos con la secuencia de color de marca; fuente citada al pie en 10–12 pt. Reutilizar prioritariamente las figuras oficiales generadas a 300 DPI por `psll-figuras-skill` disponibles en `Temas EB/Tema X/figuras/remasterizadas/`.
6. **Cierre** — síntesis + contacto + logos PSLL y UPO.

## Comprobaciones antes de entregar

- Contraste de todo el texto (cuerpo en tinta/blanco, nunca salvia sobre menta).
- Logo UPO presente en material oficial y sin deformar.
- Coral usado solo como acento.
- QA visual con subagente (skill pptx). Corregir desbordes/solapes y entregar.
