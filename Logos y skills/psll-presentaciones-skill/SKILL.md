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

## Paleta oficial (resumen — detalle en BRAND.md y marca/guia_de_estilo.md)

- Fondos claros: blanco puro `#FFFFFF` y menta tenue `#F4F8F5` para tarjetas.
- Fondos oscuros / contraste: verde pino `#113927` o verde salvia `#76927A`, con texto blanco.
- Texto de cuerpo sobre claro: verde tinta `#2F3A30` (nunca salvia sobre blanco ni negro puro).
- Acento: coral dinámico `#E98F71`, solo para cifras clave, una palabra destacada o la onda de políticas.
- Series de datos, en orden: `#113927` (pino), `#76927A` (salvia), `#E98F71` (coral), `#EDB090` (melocotón), `#566B56` (verde intermedio).

## Tipografías

- Titulares: **Outfit** (Bold / Heavy), en sintonía directa con Macroeconomía UPO. Alternativa de respaldo: Inter o Segoe UI.
- Cuerpo: **16 pt Calibri obligatorio** (tamaño estándar fijado para proyección en aula; no usar tamaños inferiores en párrafos de contenido). Nunca Aptos.
- Tamaños en diapositivas (.pptx): título 36–44 pt · cabecera de sección 20–24 pt · **cuerpo: 16 pt Calibri** · pie/cita 10–12 pt.

## Logos en las diapositivas (carpeta `assets/` y `marca/`)

- **Portada:** `logo_psll_upo.png` (o `psll_emblem.png` que ahora contiene la nueva marca) como protagonista. Logo **UPO** (`upo_logo.jpg`) discreto en un pie o esquina, sobre franja/fondo claro con su caja de protección.
- **Divisores de sección:** fondo verde pino o salvia, número y título de bloque en blanco, `psll_icon_transparent.svg` pequeño como sello.
- **Diapositivas de contenido:** `psll_lockup.png` (símbolo de anillos + "PSLL") pequeño en una esquina superior (altura ≈ 0,3"), discreto.
- **Cierre / contraportada:** síntesis + datos de contacto + logo **UPO** institucional + nuevo logotipo PSLL.
- Respetar el área de protección de la UPO: no recolorear, no deformar, no integrarlo en el pastel.

## Motivo y composición

- Repetir el **motivo de líneas orgánicas** muy tenues (un tono más oscuro que el fondo) como textura sutil en portada y divisores. Nunca sobre zonas de texto.
- Esquinas redondeadas en tarjetas y bloques (radio ~8–12 pt).
- Iconos en círculos de color de marca junto a cabeceras de sección.
- **Prohibido** (heredado de la skill pptx y reforzado aquí): líneas/subrayados bajo los títulos, barras o franjas de color decorativas en bordes, y diapositivas solo-texto. Cada diapositiva lleva un elemento visual.

## Estructura recomendada de un deck PSLL (Sesiones EB)

1. **Portada:** emblema PSLL, título del tema, "Políticas Sociolaborales · UPO", logo UPO discreto.
2. **Índice / hoja de ruta** de la sesión (tiempos y bloques).
3. **Bloque 1 (Apertura y Choque):** Sondeo previo (Microsoft Forms / Mentimeter) para capturar prejuicios populares $\rightarrow$ Choque empírico inmediato con gráficos oficiales a 300 DPI (EPA, Eurostat) que desmienten el prejuicio.
4. **Bloques 2 y 3 (Mini-Lecciones teóricas):** Desarrollo conceptual con figuras oficiales, fórmulas clave y comparativas (párrafo desarrollado a **16 pt Calibri**, nunca solo-texto).
5. **Bloque 4 (Taller / Simulación):** Actividad aplicada con micro-apps o datos guiados.
6. **Bloque 5 (Reto Final de Cierre · 10 min):**
   * **Slide de Reto:** Pregunta **100% basada en lo explicado en clase y el material previo**, redactada a mano en papel (10 min) + **Código QR de Microsoft Forms (UPO)** para subir foto (2 min). Entrega puntuable con beneficios para el examen final (70%).
   * **Slide de Solución y Rúbrica:** Solución oficial comentada en voz alta al cerrarse la entrega.
7. **Cierre:** síntesis de conclusiones + contacto + logos PSLL y UPO.

## Comprobaciones antes de entregar

- Contraste de todo el texto (cuerpo en tinta/blanco, nunca salvia sobre menta).
- Logo UPO presente en material oficial y sin deformar.
- Coral usado solo como acento.
- QA visual con subagente (skill pptx). Corregir desbordes/solapes y entregar.
