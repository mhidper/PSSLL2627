# Hoja de Laboratorio Activo · Sesión 07 EB (Fase 4 · 20 min)
## «Simulación Cuantitativa de Incentivos a la Contratación y Lanzadera a EPD 1»
**Asignatura:** Políticas Sociolaborales y de Empleo (Código 102023)  
**Profesor:** Manuel A. Hidalgo Pérez · Universidad Pablo de Olavide  
**Herramienta Digital:** Micro-App Oficial y Calculadora Laboral de Empleo Neto  
**Enlace directo:** [`https://mhidper.github.io/micro_apps/epd_laboratorio.html`](https://mhidper.github.io/micro_apps/epd_laboratorio.html)

---

### 📱 1. Misión del Taller Activo (Enlace Teórico-Práctico)

Esta sesión te sitúa en el papel de **Analista de Políticas de Empleo de la Dirección General de Intermediación y Orientación**.  
Antes de entrar al aula de informática para la **EPD 1 (Caso 1: Programa Emplea-T)**, vas a experimentar de forma guiada cómo los parámetros de diseño normativo determinan si un programa de incentivos crea empleo real o se convierte en un simple subsidio a la cuenta de resultados de las empresas.

1. Desbloquea tu dispositivo móvil.
2. Escanea el código QR proyectado en la pantalla del aula o accede a:  
   👉 **`https://mhidper.github.io/micro_apps/epd_laboratorio.html`**
3. Carga el módulo de **«Incentivos a la Contratación: Descomposición del Empleo Neto»**.

---

### 🧪 2. Tres Escenarios de Política Pública a Prueba

#### Escenario 1: El Subsidio Genérico y Universal (La Trampa del Peso Muerto)
* **Parámetros del programa:** Subvención de 6.000 € a fondo perdido por cada contrato indefinido formalizado con menores de 30 años sin exigir requisitos adicionales de plantilla.
* **Presupuesto ejecutado:** 12.000.000 € (2.000 contratos subvencionados).
* **Parámetros observados en la simulación:**
  * Tasa de Peso Muerto (*Deadweight*): **72%** (contrataciones que la empresa necesitaba hacer por demanda).
  * Tasa de Sustitución: **14%** (se contrata al joven en lugar de a un trabajador de 35 años).
  * Tasa de Desplazamiento: **4%**.
* **Cálculo guiado en tu dispositivo:**
  $$\text{Tasa de Ineficiencia Total} = 0,72 + 0,14 + 0,04 = 0,90 \quad (90\%)$$
  $$\Delta N_{\text{neto}} = 2.000 \cdot (1 - 0,90) = 2.000 \cdot 0,10 = \mathbf{200 \text{ empleos netos}}$$
  $$\text{Coste Fiscal por Empleo Neto} = \frac{12.000.000\text{ \euro}}{200\text{ empleos}} = \mathbf{60.000 \text{ \euro / empleo}}$$
* **Pregunta clave para debate:** ¿Tiene sentido pagar 60.000 € de dinero público por cada puesto neto cuando el salario bruto anual del joven es de 18.000 €?

---

#### Escenario 2: El Programa Emplea-T con Salvaguardas Básicas (El Modelo Andaluz)
* **Parámetros del programa:** Subvenciones entre 6.000 € y 12.000 € (Líneas 1 y 2) con el **doble candado normativo**:
  * Obligación de mantener el puesto al menos **12 meses**.
  * Obligación de **no reducir la plantilla fija** durante dicho periodo.
* **Efecto de las salvaguardas sobre los parámetros:**
  * La cláusula de no reducción de plantilla desploma la tasa de sustitución del 14% al **5%**.
  * La obligación de 12 meses reduce el efecto rotación a corto plazo.
  * Sin embargo, si la subvención sigue concediéndose a perfiles con titulación técnica universitaria de alta demanda, el **peso muerto se mantiene alto (55%)**.
* **Resultado del escenario:**
  $$\Delta N_{\text{neto}} = 2.000 \cdot [1 - (0,55 + 0,05 + 0,04)] = 2.000 \cdot 0,36 = \mathbf{720 \text{ empleos netos}}$$
  $$\text{Coste Fiscal por Empleo Neto} = \frac{12.000.000\text{ \euro}}{720\text{ empleos}} = \mathbf{16.666 \text{ \euro / empleo}}$$

---

#### Escenario 3: La Reforma Estructural Recomendada por la AIReF
* **Parámetros del programa:**
  * Hiper-focalización en parados de muy larga duración (> 24 meses) y personas en riesgo de exclusión con informe de perfilado (*profiling*).
  * Exigencia de **incremento neto de la plantilla media** de los últimos 12 meses.
  * Bonificación mensual en cotizaciones sociales vinculada a permanencia de 24 meses y formación técnica en el puesto.
* **Resultado del escenario:**
  * Peso muerto: **25%** (porque casi nadie contrata espontáneamente a un parado de muy larga duración sin incentivo).
  * Sustitución: **5%**.
  * Empleo neto generado: **1.400 empleos netos** (70% de eficacia).
  * Coste por empleo neto: **8.571 € / empleo**.

---

### 🚀 3. Conexión Inmediata con la EPD 1 (Al salir de esta clase)
Al terminar esta sesión presencial te desplazarás al aula de informática:
* **Línea 1:** EPD 11 (11:30, Aula E24AINFB01) y EPD 12 (13:00, Aula E14AINF1).
* **Línea 2:** EPD 21 (19:30, Aula E10AINF6).

En la **EPD 1** arranca el **Bloque 1 del Proyecto: Diagnóstico del Desempleo Sénior en Andalucía**:
1. Accederás a la Web App (`https://mhidper.github.io/micro_apps/epd_laboratorio.html`) introduciendo tu **acrónimo oficial UPO** para desbloquear tu caso asignado (Caso A: 45–54 años vs. Caso B: 55+ años).
2. Explorarás los microdatos de la **EPA (INE)** y **Eurostat (LFS)**: tasas de paro por cohortes, peso de parados de larga duración (>12 meses) y muy larga duración (>24 meses), y brechas territoriales.
3. Completarás el taller de cálculo dinámico y redactarás tu dictamen para sellar y entregar el **Entregable Individual 1 (0,50 puntos)**.

*(Nota de coordinación: La auditoría cuantitativa y simulación de costes salariales de la Orden de Emplea-T se desarrollará en la **EPD 4 en la Semana 10**, aplicando el instrumental de peso muerto y sustitución que hemos formalizado en la EB 7).*
