# Memoria de Trabajo y Registro de Sesión · Sesión EB 11
## «Garantía de rentas, trampa de la pobreza e Ingreso Mínimo Vital (IMV)»
**Asignatura:** Políticas Sociolaborales y de Empleo (Código 102023)  
**Profesor:** Manuel A. Hidalgo Pérez · Universidad Pablo de Olavide (UPO)  
**Curso Académico:** 2026-27 · Grado en Relaciones Laborales y Recursos Humanos  
**Fecha de Generación y Registro:** 01 de Noviembre de 2026  
**Ubicación:** `Temas EB/Sesiones EB/Sesion 11/`  

---

### 1. Resumen Ejecutivo de la Sesión de Trabajo

En esta conversación de desarrollo docente se ha diseñado, generado, ajustado y desplegado de forma integral todo el ecosistema de materiales pedagógicos, analíticos y digitales para la **Sesión EB 11 (Semana 8, 120 minutos)** de Políticas Sociolaborales y de Empleo.

La sesión aborda el cierre del **Tema 3 (Políticas Pasivas y Garantía de Rentas)**, integrando la columna de opinión del profesor en *Cinco Días* (*«Un Ingreso Mínimo Vital mejor diseñado alcanzaría mejor sus objetivos»*), microdatos oficiales de la AIReF y la Seguridad Social, análisis microeconómico del Tipo Marginal Efectivo ($EMTR$), desmontaje de mitos sobre nacionalidad y fraude, y una experiencia interactiva de gamificación en aula con micro-apps móviles.

---

### 2. Cronología Detallada de Decisiones y Ajustes Realizados

#### Hito 1: Localización del Ecosistema de Micro-Apps
* Se identificó el repositorio y alojamiento de las herramientas interactivas del docente:
  - Repositorio local: `C:\Users\Usuario\Documents\Dropbox\DOCENCIA UPO\micro_apps`
  - Despliegue en producción (GitHub Pages): `https://mhidper.github.io/micro_apps/`

#### Hito 2: Generación Integral de la Sesión 11 (2 horas · 120 min)
* Se integraron los 5 pilares del artículo de *Cinco Días* (Hidalgo, 2026):
  1. Los 3 estigmas infundados del IMV frente a la realidad contable y social.
  2. La trampa del $EMTR$ tradicional ($100\%$) en la prestación diferencial.
  3. La trampa agravada ($EMTR > 100\%$) provocada por la concurrencia de subsidios en el 51% de hogares vulnerables (pérdida de bono social térmico/eléctrico y becas comedor).
  4. La evidencia econométrica de la AIReF (-3 pp / -12% de probabilidad de empleo).
  5. Los límites del RD 240/2026 (incentivo transitorio sobre incrementos anuales) frente a las propuestas estructurales (retirada gradual continua sobre nivel / Impuesto Negativo, concesión proactiva de oficio cruzando datos con IRPF/TGSS y prestación universal por crianza).

#### Hito 3: Evidencia Empírica de Nacionalidad y Filtro Jurídico (Slide 7)
* A petición expresa de Manuel sobre los datos de beneficiarios por nacionalidad:
  - **Dato oficial Seguridad Social:** **82,5% ciudadanos españoles** vs. **17,5% extranjeros**.
  - **Filtro legal del art. 10 de la Ley 19/2021:** Exigencia obligatoria de **residencia legal continuada e ininterrumpida en España durante al menos 1 año inmediatamente anterior a la solicitud** (con excepciones tasadas para víctimas de violencia de género y trata). Las personas en situación administrativa irregular están legalmente excluidas.
  - Se diseñó y generó la **Figura 3.6 a 300 DPI** (`figura_3_6_nacionalidad_imv.png`) con donut comparativo, dispersión provincial y esquema del filtro legal, insertándose en la **Slide 7** de la presentación oficial.

#### Hito 4: Depuración Terminológica en Slide 11
* Se eliminó el término sensacionalista "escándalo", adoptando una denominación analítica rigurosa homologada con el estilo académico del profesor:
  - **Título anterior:** *Slide 11 · El Escándalo del Non-Take-Up...*
  - **Título definitivo:** *Fase 2 (20–45 min) · La Paradoja de la Exclusión Administrativa: La Brecha de Cobertura y Non-Take-Up en el IMV*.

#### Hito 5: Inclusión de Tres Ejemplos Numéricos de Aula en Slide 12
* Para facilitar la comprensión matemática y laboral del $EMTR$, la **Slide 12** se dotó de tres casos cuantitativos detallados con un salario bruto común ($\Delta Y_{\text{bruto}} = +400\ \text{€/mes}$):
  1. **$EMTR = 0\%$ (Incentivo Pleno · RD 240/2026):** Renta líquida aumenta en 400 € íntegros (pasa de 650 € a 1.050 €).
  2. **$EMTR = 100\%$ (Trampa Clásica · Diferencial Pura):** El subsidio se reduce 400 €; la renta permanece en 650 € ($\Delta Y_{\text{disp}} = 0\ \text{€}$). Con gastos de transporte (-50 €), trabajar cuesta dinero.
  3. **$EMTR > 100\%$ (Trampa Agravada · Concurrencia de Subsidios):** Pérdida de IMV (-400 €) + Bono luz (-50 €) + Beca comedor (-120 €). La renta cae de 820 € a 650 € ($\Delta Y_{\text{disp}} = -170\ \text{€}$). $EMTR = 142,5\%$. Trabajar destruye liquidez familiar.

#### Hito 6: Remasterización Didáctica y Guía de Lectura de la Figura 3.4 (Slide 13)
* Para superar la abstracción de las curvas microeconómicas:
  - Se regeneró `figura_3_4_trampa_pobreza_emtr.png` incorporando **equivalencias mensuales en el eje X** (0 €, 250 €/m, 500 €/m, 733 €/m, SMI), **callouts explicativos directos sobre las curvas** (por qué la línea coral es plana y por qué la verde sube) y rótulos de confiscación vs incentivo en el Panel B.
  - La **Slide 13** se enriqueció con **tres tarjetas inferiores de lectura** (Coral, Pino y Salvia) con la guía directa que el profesor puede seguir en pizarra.

#### Hito 7: Dinamización Docente y «El Reto del Ministro de Seguridad Social» (Fase 4 · 20 min)
* Para resolver el problema de terminar la clase antes de tiempo y «estirar el chicle» con alto valor pedagógico:
  - Se propuso un menú de 5 dinámicas participativas activas.
  - Se seleccionó e implementó la **Competición de Aula en Parejas: «El Reto del Ministro»** en la Fase 4 (70–90 min).
  - Se modificó la micro-app interactiva (`simulador_imv_trampa.html`) en la Pestaña 3, añadiendo un evaluador algorítmico en tiempo real con 3 metas simultáneas:
    * *Meta 1 (Cobertura):* Hogares cubiertos $\ge 50\%$.
    * *Meta 2 (Techo Fiscal):* Gasto $\le 0,55\%$ del PIB.
    * *Meta 3 (Empleo):* Desincentivo laboral $< -1,5\ \text{pp}$.
  - Se programó el badge interactivo 🏆 **«¡MISIÓN CUMPLIDA, SEÑOR/A MINISTRO/A!»** al cuadrar el trilema, y se desplegó en GitHub Pages.
  - Se actualizaron la **Slide 18**, la [hoja_taller_sesion_11.md](file:///c:/Users/Usuario/Documents/Dropbox/DOCENCIA%20UPO/CURSO%2026-27/PSLL/Temas%20EB/Sesiones%20EB/Sesion%2011/hoja_taller_sesion_11.md) y el [guion_sesion_11.md](file:///c:/Users/Usuario/Documents/Dropbox/DOCENCIA%20UPO/CURSO%2026-27/PSLL/Temas%20EB/Sesiones%20EB/Sesion%2011/guion_sesion_11.md).

---

### 3. Inventario Completo de Materiales Entregados

| Fichero | Tipo | Descripción |
| :--- | :---: | :--- |
| [Sesion 11 · PPTX](file:///c:/Users/Usuario/Documents/Dropbox/DOCENCIA%20UPO/CURSO%2026-27/PSLL/Temas%20EB/Sesiones%20EB/Sesion%2011/Sesion%2011%20-%20Garantia%20de%20rentas,%20trampa%20de%20la%20pobreza%20e%20Ingreso%20Minimo%20Vital.pptx) | Diapositivas | 25 slides widescreen 16:9, paleta oficial PSLL, 16 pt Calibri, QR institucionales y retos. |
| [Sesion 11 · PDF](file:///c:/Users/Usuario/Documents/Dropbox/DOCENCIA%20UPO/CURSO%2026-27/PSLL/Temas%20EB/Sesiones%20EB/Sesion%2011/Sesion%2011%20-%20Garantia%20de%20rentas,%20trampa%20de%20la%20pobreza%20e%20Ingreso%20Minimo%20Vital.pdf) | Proyección | Réplica vectorial de alta fidelidad compilada mediante PowerPoint COM. |
| [generar_presentacion_sesion_11.py](file:///c:/Users/Usuario/Documents/Dropbox/DOCENCIA%20UPO/CURSO%2026-27/PSLL/Temas%20EB/Sesiones%20EB/Sesion%2011/generar_presentacion_sesion_11.py) | Python | Script generador reproducible 100% de la presentación oficial. |
| [simulador_imv_trampa.html](file:///c:/Users/Usuario/Documents/Dropbox/DOCENCIA%20UPO/CURSO%2026-27/PSLL/Temas%20EB/Sesiones%20EB/Sesion%2011/simulador_imv_trampa.html) | Web / Móvil | Micro-app con simulador de EMTR, verificador de estigmas, Reto del Ministro y casos. |
| [guion_sesion_11.md](file:///c:/Users/Usuario/Documents/Dropbox/DOCENCIA%20UPO/CURSO%2026-27/PSLL/Temas%20EB/Sesiones%20EB/Sesion%2011/guion_sesion_11.md) | Guion | Arquitectura en 5 fases ajustada a 120 min, pautas docentes y moderación de debates. |
| [enigma_previo_sesion_11.md](file:///c:/Users/Usuario/Documents/Dropbox/DOCENCIA%20UPO/CURSO%2026-27/PSLL/Temas%20EB/Sesiones%20EB/Sesion%2011/enigma_previo_sesion_11.md) | Fase 1 | Noticia disparadora de Cinco Días, sondeo Forms, choque empírico y mitos de nacionalidad. |
| [hoja_taller_sesion_11.md](file:///c:/Users/Usuario/Documents/Dropbox/DOCENCIA%20UPO/CURSO%2026-27/PSLL/Temas%20EB/Sesiones%20EB/Sesion%2011/hoja_taller_sesion_11.md) | Fase 4 | Ficha de laboratorio activo móvil con el Caso María y la ficha del Reto del Ministro. |
| [reto_manuscrito_sesion_11.md](file:///c:/Users/Usuario/Documents/Dropbox/DOCENCIA%20UPO/CURSO%2026-27/PSLL/Temas%20EB/Sesiones%20EB/Sesion%2011/reto_manuscrito_sesion_11.md) | Fase 5 | Enunciados diferenciados Martes (L1) y Viernes (L2), rúbricas 0–1.000 pts y soluciones modelo. |
| `figura_3_4_trampa_pobreza_emtr.png` | Figura 300 DPI | Restricción presupuestaria y EMTR con callouts explicativos y guía pedagógica. |
| `figura_3_5_cobertura_nontakeup_imv.png` | Figura 300 DPI | Perfil de perceptores (infancia/empleo/mujeres) y tasas de non-take-up de AIReF. |
| `figura_3_6_nacionalidad_imv.png` | Figura 300 DPI | Donut 82,5% vs 17,5%, dispersión territorial y filtro jurídico art. 10 Ley 19/2021. |
| Códigos QR oficiales | Gráficos 1:1 | `qr_sondeo_sesion11.png`, `qr_app_sesion11.png`, `qr_reto_sesion11.png`, `qr_pasaporte_psll.png`. |

---

### 4. Cronómetro Maestro de Aula (120 minutos)

| Fase | Minutos | Metodología | Foco de Atención del Alumnado |
| :---: | :---: | :--- | :--- |
| **Fase 1** | **00 – 20 min** | Noticia Cinco Días + Sondeo Forms + Desmontaje Mitos (82,5% españoles) | Móviles activos (sondeo) $\to$ Choque empírico |
| **Fase 2** | **20 – 45 min** | Mini-Lección 1: Arquitectura legal, umbrales y paradoxa del non-take-up | Solo papel y lápiz (pantallas cerradas) |
| **Fase 3** | **45 – 70 min** | Mini-Lección 2: Análisis analítico $EMTR$ (3 ejemplos) + Guía Fig. 3.4 | Pizarra y formulación analítica laboral |
| **Fase 4** | **70 – 90 min** | **Laboratorio y Competición en Parejas: «El Reto del Ministro»** | Móviles activos (micro-app) $\to$ Debate de políticas |
| **Fase 5a** | **90 – 98 min** | Síntesis institucional en pizarra y preparación para el reto | Transición reflexiva sin dispositivos |
| **Fase 5b** | **98 – 108 min** | **Reto Manuscrito Individual en Papel (10 min)** | Silencio absoluto y concentración máxima |
| **Fase 5c** | **108 – 110 min** | Subida fotográfica instantánea vía QR de Forms | Móviles activos solo para fotografiar y subir |
| **Fase 5d** | **110 – 120 min** | Co-evaluación cruzada en parejas con rúbrica oficial (0–1.000 pts) | Feedback formativo entre iguales y Pasaporte |

---
*Memoria compilada y guardada para consulta permanente del docente.*
