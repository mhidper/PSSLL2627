# Hoja de Laboratorio Activo · Sesión 5 EB (Semana 3)
## «Trazado, Diagnóstico y Simulación de Políticas en la Curva de Beveridge: El Reto del Programa Emplea-T»
**Asignatura:** Políticas Sociolaborales y de Empleo (Código 102023)  
**Curso Académico:** 2026-2027 | Semestre 1 · Universidad Pablo de Olavide  
**Modalidad:** Trabajo en Parejas (Analistas Técnicos de la Consejería de Empleo / Gabinete de Evaluación de Políticas)  
**Evaluación:** Registro de logro en el **Pasaporte de Evaluación Continua** (Hacia el 10% de Participación y Retos Activos)

---

### 👥 Datos del Equipo Técnico de Analistas
* **Nombre Analista 1:** __________________________________________________  
* **Nombre Analista 2:** __________________________________________________  
* **Grupo / Turno:** Línea 1 (Mañana) [ ] · Línea 2 (Tarde) [ ]  
* **Fecha:** ___ / 09 / 2026

---

### 🎯 Misión Institucional
La Dirección General de Intermediación y Orientación Laboral os encomienda modelizar el funcionamiento del mercado de trabajo mediante el instrumental de la **Curva de Beveridge** y la **función de emparejamiento** ($m = A \cdot U^\alpha \cdot V^{1-\alpha}$). Vuestro objetivo es **diagnosticar si las 155.000 vacantes sin cubrir en España son síntoma de un problema cíclico o de ineficiencia estructural**, y **evaluar técnicamente el diseño de las subvenciones del Programa Emplea-T** que auditaréis en las sesiones prácticas de EPD.

---

### 🧪 Fase 1: Geometría de Beveridge y Dinámica de Flujos (10 min)

1. **La Condición de Flujo Estacionario:**
   Recordad que el desempleo de equilibrio a largo plazo es $u^* = \frac{s}{s+f}$. Si la tasa de separación mensual de Andalucía es $s = 0,015$ (el 1,5% de los ocupados pierde su empleo cada mes) y la tasa de salida del paro es $f = 0,105$ (el 10,5% de los desempleados encuentra empleo cada mes):
   - Calculad la tasa natural de desempleo de equilibrio:
     $$u^* = \frac{0,015}{0,015 + 0,105} = \text{___________} \;\%$$
   - Si una reforma en los servicios públicos de empleo (SAE) duplica la tasa de colocación hasta $f = 0,210$, ¿cuál sería la nueva tasa de desempleo de equilibrio?
     $$u^{*\prime} = \frac{0,015}{0,015 + 0,210} = \text{___________} \;\%$$

2. **Trazado de Puntos Notables en el Plano $(U, V)$:**
   En el gráfico inferior, ubicad razonadamente los tres puntos teóricos descritos en el **Epígrafe 6.3 de los apuntes oficiales**:
   - **Punto A (Equilibrio Natural):** Sobre la bisectriz de 45° ($u = v$), donde todo el desempleo es friccional y estructural, sin componente cíclico.
   - **Punto B (Desempleo Alto / Recesión):** Por debajo de la bisectriz ($u > v$), reflejando desempleo involuntario por falta de demanda agregada.
   - **Punto C (Sobrecalentamiento):** Por encima de la bisectriz ($u < v$), reflejando tensión máxima de vacantes y escasez crítica de mano de obra.

```
       Tasa Vacantes (V)
            ▲
            │       \                      / Bisectriz (u = v)
            │        \                    /
            │         \   [ Punto ___ ]  /
            │          \                /
            │           \              /
            │            \  [ Punto A ]
            │             \          /
            │              \        /
            │               \      /   [ Punto ___ ]
            │                \    /
            └─────────────────\──/────────────────────► Tasa Desempleo (U)
                               \
```

---

### 📱 Fase 2: Simulación Interactiva con la Micro-App Móvil (10 min)

Abrid en vuestro teléfono móvil la micro-app oficial escaneando el código QR proyectado en clase:  
[`https://mhidper.github.io/micro_apps/simulador_curva_beveridge.html`](https://mhidper.github.io/micro_apps/simulador_curva_beveridge.html)

1. **Experimento 1: Movimiento a lo largo de la curva (Ciclo Económico):**
   - Moved el control deslizante de *Ciclo Económico* de **Recesión Moderada (-15)** a **Fuerte Expansión (+35)** manteniendo constante la eficiencia $A = 78$.
   - *¿Qué ocurre con la tasa de paro $u$ y la tasa de vacantes $v$?*  
     _________________________________________________________________________________________
   - *¿Se ha desplazado la Curva de Beveridge? ¿Por qué?*  
     _________________________________________________________________________________________

2. **Experimento 2: Desplazamiento de la curva (Shock Estructural y Desajuste):**
   - Activad el escenario **«Shock Desajuste Estructural»** ($A = 60$, *Skills Mismatch* alto).
   - Observad la nueva posición de la curva respecto al origen:
     * *¿Por qué un país con la misma tasa de vacantes ($v = 0,75\%$) tiene ahora mucho más desempleo?*  
       _________________________________________________________________________________________
   - Revisad la pestaña **«Caso España»**:  
     * ¿Cuánto explicó la caída de la eficiencia de emparejamiento ($A$) sobre la destrucción de empleo durante la Gran Recesión de 2008-2013 según el modelo DGEM de los apuntes? **[ _______ % ]**  
     * ¿Y sobre la caída del PIB? **[ _______ % ]**

---

### ⚖️ Fase 3: Gabinete de Políticas · Lanzamiento del Caso 1 EPD (Emplea-T) (10 min)

La Junta de Andalucía ha aprobado la **Orden de 3 de octubre de 2024 (Programa Emplea-T)** para incentivar la contratación de colectivos vulnerables, especialmente parados de larga duración (PLD).

| Cuestión Técnica | Análisis del Gabinete de Analistas |
| :--- | :--- |
| **1. Objetivo en la Curva de Beveridge** | ¿Qué busca lograr el Programa Emplea-T: un movimiento *a lo largo* de la curva o un *desplazamiento hacia el origen* ($BC_2 \rightarrow BC_1$)? Justificad la respuesta en base a la variable $A$.<br><br>__________________________________________________________________ |
| **2. La Amenaza del Peso Muerto (*Deadweight*)** | Si una empresa de logística iba a contratar de todos modos a 5 mozos de almacén para la campaña de Navidad y aprovecha la subvención de Emplea-T para cobrar 6.000 € por contrato: ¿se ha reducido el desempleo estructural? ¿Por qué este efecto encarece el coste por empleo neto adicional?<br><br>__________________________________________________________________ |
| **3. La Cláusula Anti-Sustitución** | ¿Por qué la Orden exige que las contrataciones supongan un **incremento neto de la plantilla media** respecto a los 12 meses anteriores?<br><br>__________________________________________________________________ |

---

### 🏁 Conclusión del Taller
Firmad vuestra hoja de trabajo. Las conclusiones de este laboratorio constituyen el marco conceptual directo que utilizaréis en la **Sesión 1 de EPD** para auditar los microdatos de demandantes de empleo en Andalucía.
