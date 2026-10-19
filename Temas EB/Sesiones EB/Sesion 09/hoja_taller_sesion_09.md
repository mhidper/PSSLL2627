# Hoja de Taller y Laboratorio Activo · Sesión EB 9
## Fase 4 (70–85 min · 15 min): «Simulación de la Balanza de Protección y Estructura Dual del SEPE»
**Asignatura:** Políticas Sociolaborales y de Empleo (Código 102023)  
**Profesor:** Manuel A. Hidalgo Pérez · Universidad Pablo de Olavide  
**Herramienta Digital:** Micro-App Oficial · La Balanza de la Protección Social  
**Enlace directo:** [`https://mhidper.github.io/micro_apps/balanza_proteccion.html`](https://mhidper.github.io/micro_apps/balanza_proteccion.html)  

---

### 📱 1. Misión del Analista (Enlace Teórico-Práctico)

Esta sesión te sitúa en el papel de **Analista Técnico del Servicio Público de Empleo Estatal (SEPE)**.  
Vas a experimentar desde tu teléfono móvil cómo se articulan los dos niveles del sistema español de protección por desempleo (contributivo y asistencial) y a resolver en directo tres casos de fijación de prestaciones y dilemas de política pública.

1. Desbloquea tu dispositivo móvil.
2. Escanea el código QR proyectado en pantalla (`qr_app_sesion09.png`) o entra en:  
   👉 **`https://mhidper.github.io/micro_apps/balanza_proteccion.html`**
3. Carga el simulador y sigue los tres retos analíticos guiados.

---

### 🧪 2. Tres Escenarios Cuantitativos a Prueba

#### Escenario 1: Cálculo y Topes de la Prestación Contributiva
* **Perfil del trabajador:** Carmen, 34 años, despedida tras 4 años ininterrumpidos de trabajo (1.440 días cotizados) con una base de cotización de 2.200 €/mes en los últimos 180 días. Tiene 1 hijo a cargo.
* **Cálculo guiado en la app:**
  1. **Duración devengada:** Según la escala legal del art. 269 LGSS, a 1.440 días de cotización (tramo 1.440 a 1.619 días) corresponden **480 días (16 meses)** de prestación.
  2. **Cuantía mensual:**
     - Primeros 180 días (6 meses): $70\% \text{ de } 2.200\text{ \euro} = \mathbf{1.540\text{ \euro/mes}}$.
     - A partir del día 181: $60\% \text{ de } 2.200\text{ \euro} = \mathbf{1.320\text{ \euro/mes}}$.
  3. **Comprobación de topes legales (IPREM 2026 = 600 €/mes):**
     - Tope máximo con 1 hijo (200% IPREM + 1/6): $1.400\text{ \euro/mes}$.
     - *Resultado:* Carmen sufrirá el tope máximo legal; cobrará 1.400 €/mes durante los primeros 6 meses (reduciendo su tasa de reemplazo efectiva del 70% al 63,6%).

---

#### Escenario 2: La Red Asistencial y el Subsidio de Mayores de 52 Años
* **Perfil del trabajador:** Antonio, 53 años, agota su prestación contributiva tras 24 meses de desempleo. No tiene ingresos propios y su cónyuge percibe 600 €/mes.
* **Preguntas clave en el simulador:**
  1. **Criterio de carencia de rentas:** Sus ingresos propios no superan el 75% del SMI (excluidas pagas extraordinarias). Cumple el requisito.
  2. **Cuantía del subsidio asistencial general vs mayores de 52:**
     - En el subsidio ordinario reformado (RDL 2/2024 / 2026), la cuantía es decreciente: 95% del IPREM los primeros 6 meses (570 €), 90% los 6 siguientes (540 €) y 80% el resto (480 €).
     - En el **subsidio de mayores de 52 años**, la cuantía se mantiene fija en el **80% del IPREM (480 €/mes)** de forma indefinida hasta alcanzar la edad de jubilación, con la singularidad crucial de que **el Estado cotiza por él para la pensión de jubilación sobre una base del 125% del tope mínimo**.

---

#### Escenario 3: El Dilema de la Balanza de Protección
* **Simulación de trade-off macroeconómico:**
  - Ajusta el control de generosidad de la tasa de reemplazo neta:
    - Si la situamos al **40%**: el riesgo moral es nulo y el coste fiscal mínimo, pero se disparan los desahucios, la pobreza sobrevenida y el trabajador se ve forzado a aceptar empleos precarios y de nula productividad.
    - Si la situamos al **90%**: aseguramiento perfecto y alto consumo, pero el salario de reserva se dispara, se ralentiza la tasa de salida del paro ($f \downarrow$) y el déficit público del sistema se vuelve insostenible.
  - **Punto óptimo según la literatura empírica (Chetty):** Una tasa de reemplazo entre el **60% y el 70%** combinada con un perfil decreciente y condicionalidad activa equilibra la suavización del consumo con los incentivos a la reinserción.
