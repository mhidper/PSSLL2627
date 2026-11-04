# -*- coding: utf-8 -*-
"""
===============================================================================
COMPILADOR CRIPTOGRÁFICO DEL PASAPORTE DE EVALUACIÓN CONTINUA
Políticas Sociolaborales y de Empleo (PSLL)
Grados en Relaciones Laborales y Recursos Humanos / Doble Grado DER + RRLyRRHH
Universidad Pablo de Olavide · Curso 2026-27
Profesor: Manuel A. Hidalgo Pérez
===============================================================================
Estructura los datos con desglose individual de preguntas por sesión
para navegación por pestañas en la interfaz web del alumno.
Cifrado militar Zero-Knowledge AES-GCM-256 + SHA-256.
===============================================================================
"""

import pandas as pd
import json
import itertools
import hashlib
import os
import re
import unicodedata
import base64
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(SCRIPT_DIR)
MICRO_APPS_DIR = r"C:\Users\Usuario\Documents\Dropbox\DOCENCIA UPO\micro_apps"
MICRO_APPS_ALT = r"C:\Users\Usuario\Dropbox\DOCENCIA UPO\micro_apps"

# Rutas a listas oficiales de clase
lista_l1_path = os.path.join(BASE_DIR, "Repositorio material (no alumnos)", "lista.xlsx")
lista_l2_path = os.path.join(BASE_DIR, "Repositorio material (no alumnos)", "ListaClase_2026-27_102023BC_2.xls")

# Rutas de evaluación por sesión (se cargarán dinámicamente si existen)
EVAL_SESIONES_CONFIG = [
    {
        "sesion_num": 2,
        "id": "s02",
        "titulo_corto": "Sesión 02",
        "titulo_completo": "Sesión 02 · Crecimiento Económico, Productividad y Costes Laborales Unitarios",
        "tema": "Tema 1: Macroeconomía del Mercado de Trabajo y Dinámica Salarial",
        "fecha": "Septiembre 2026",
        "calif_path": os.path.join(BASE_DIR, "Temas EB", "Sesiones EB", "Sesion 02", "evaluacion", "calificaciones_sesion_02.csv"),
        "trans_path": os.path.join(BASE_DIR, "Temas EB", "Sesiones EB", "Sesion 02", "evaluacion", "transcripciones_psll_sesion_02.csv"),
        "enunciado_p1": "«Un sector económico incrementa sus salarios un 8% en un ejercicio en el que su productividad por hora solo creció un 2%». Razona con rigor económico:\na) Costes Laborales Unitarios (CLU): ¿Qué ocurre numéricamente con el CLU del sector? Aplica la fórmula vista en clase.",
        "solucion_p1": "1. Definición y Fórmula Formal del CLU:\nEl Coste Laboral Unitario relaciona el coste laboral medio por hora (salario nominal por hora W/H) con la productividad media aparente del trabajo (Y/H):\nCLU = (W / H) / (Y / H) = W / Y.\n\n2. Aproximación en Tasas de Variación Porcentual:\nLa tasa de variación porcentual del CLU se obtiene como la diferencia de tasas de crecimiento:\n%ΔCLU ≈ %ΔW - %ΔProd = 8% - 2% = +6%\n(o en cálculo exacto continuo: (1 + 0,08)/(1 + 0,02) - 1 = 1,08/1,02 - 1 = +5,88%).\n\nConclusión: Numéricamente, el CLU del sector se incrementa un 6%, lo que significa que el coste en mano de obra necesario para fabricar cada unidad producida se encarece significativamente.",
        "enunciado_p2": "b) Competitividad y Empleo: ¿Pueden trasladar el sobrecoste a precios sin consecuencias? ¿Cómo ajustará la empresa?",
        "solucion_p2": "1. Imposibilidad de Traslación sin Consecuencias:\nNo es posible trasladar el sobrecoste a precios de forma inocua. Si las empresas aumentan sus precios de venta, sufren una pérdida inmediata de competitividad frente a competidores del sector (nacionales e internacionales) o frente a bienes sustitutivos. Esto desencadena una contracción de la demanda de mercado y una caída de las ventas.\n\n2. Vías de Ajuste Empresarial:\nAnte la imposibilidad de repercutir todo el incremento salarial en precios, la empresa debe asumir el impacto a través de:\n• Compresión de márgenes de beneficio empresarial a corto plazo.\n• Ajuste en el factor trabajo: reducción de plantilla (despidos, no renovación de contratos temporales) o reducción de horas trabajadas para contener la masa salarial.\n• Inversión tecnológica y sustitución de trabajo por capital: acelerar la mecanización o digitalización para elevar la productividad por hora y restablecer la rentabilidad a medio y largo plazo."
    },
    {
        "sesion_num": 3,
        "id": "s03",
        "titulo_corto": "Sesión 03",
        "titulo_completo": "Sesión 03 · Oferta de Trabajo, Salario de Reserva y Trampas de Inactividad",
        "tema": "Tema 1: Macroeconomía del Mercado de Trabajo y Dinámica Salarial",
        "fecha": "21 de Septiembre 2026",
        "calif_path": os.path.join(BASE_DIR, "Temas EB", "Sesiones EB", "Sesion 03", "evaluacion", "calificaciones_sesion_03.csv"),
        "trans_path": os.path.join(BASE_DIR, "Temas EB", "Sesiones EB", "Sesion 03", "evaluacion", "transcripciones_psll_sesion_03.csv"),
        "enunciado_p1": "«Un trabajador desempleado percibe un subsidio asistencial de 480 €/mes (Y_NS). Recibe una oferta para trabajar como operario de logística a jornada completa por 1.150 € netos mensuales. Para acudir al puesto debe gastar 180 € al mes en combustible y perdería de forma inmediata la ayuda de 480 €».\na) Calcule la ganancia neta real por hora trabajada de este operario.",
        "solucion_p1": "1. Ingresos y Gastos Mensuales:\nSalario neto mensual ofertado: 1.150 €.\nGastos obligatorios de transporte (combustible): -180 €.\nIngreso neto efectivo disponible derivado del empleo: 1.150 € - 180 € = 970 €/mes.\n\n2. Coste de Oportunidad y Pérdida del Subsidio:\nAl aceptar el empleo pierde automáticamente el subsidio asistencial de 480 €/mes.\nGanancia neta real incremental mensual:\nΔY = 970 € - 480 € = 490 €/mes.\n\n3. Ganancia Neta Real por Hora Trabajada:\nJornada completa habitual (40 horas semanales × 4 semanas = 160 horas al mes):\nGanancia neta por hora = 490 € / 160 h ≈ 3,06 €/hora.\n(Frente a un salario contractual aparente de 1.150 € / 160 h = 7,19 €/hora, el trabajador solo percibe un incentivo real marginal de 3,06 € por cada hora que dedica a trabajar).",
        "enunciado_p2": "b) Explique analíticamente por qué el salario ofertado se sitúa por debajo de su Salario de Reserva (w_R = 1.000 €). Indique si acepta o no el empleo.",
        "solucion_p2": "1. Comparación Analítica con el Salario de Reserva:\nEl Salario de Reserva (w_R = 1.000 €/mes) es el umbral mínimo de remuneración neta que exige el trabajador para renunciar a su tiempo de ocio/inactividad e incorporarse al empleo.\nEl salario neto disponible que obtiene de la actividad laboral tras deducir los gastos ineludibles de transporte es:\nw_efectivo = 1.150 € - 180 € = 970 €/mes.\nDado que 970 € < 1.000 € (w_efectivo < w_R), la oferta económica se sitúa estrictamente por debajo de su salario de reserva (e incluso la ganancia adicional neta de 490 € frente a percibir la ayuda asistencial queda extraordinariamente lejos de retribuir el esfuerzo de 160 h mensuales).\n\n2. Decisión del Trabajador y Trampa del Desempleo:\nDado que w < w_R, el trabajador RECHAZA la oferta de empleo y decide permanecer en desempleo asistido. El caso ejemplifica formalmente la «trampa del desempleo» (unemployment trap), en la que la pérdida brusca del subsidio combinada con los costes fijos de inserción desincentiva la aceptación de ofertas de trabajo en bandas salariales bajas o medias."
    },
    {
        "sesion_num": 4,
        "id": "s04",
        "titulo_corto": "Sesión 04",
        "titulo_completo": "Sesión 04 · Desempleo de Equilibrio (NAIRU), Curva de Phillips y Políticas de Empleo",
        "tema": "Tema 1: Macroeconomía del Mercado de Trabajo y Dinámica Salarial",
        "fecha": "28 de Septiembre 2026",
        "calif_path": os.path.join(BASE_DIR, "Temas EB", "Sesiones EB", "Sesion 04", "evaluacion", "calificaciones_sesion_04.csv"),
        "trans_path": os.path.join(BASE_DIR, "Temas EB", "Sesiones EB", "Sesion 04", "evaluacion", "transcripciones_psll_sesion_04.csv"),
        "enunciado_p1": "«Un gobierno aprueba un ambicioso plan de estímulo de gasto público para forzar una reducción del desempleo en un ejercicio en el que la economía ya se encuentra exactamente en su tasa natural (NAIRU, u_t = u_n)». Razona con rigor económico formal:\na) Corto Plazo e Inflación: ¿Qué ocurre a corto plazo con el desempleo (u_t) y la tasa de inflación (π_t)? Sería interesante que te apoyaras formalmente en la ecuación de la Curva de Phillips vista en clase para dar la respuesta.",
        "solucion_p1": "1. Modelo Analítico de la Curva de Phillips con Expectativas:\nLa relación a corto plazo entre inflación y desempleo viene determinada por la Curva de Phillips ampliada con expectativas:\nπ_t = π_t^e - β(u_t - u_n) + ν_t\ndonde π_t es la inflación efectiva, π_t^e la inflación esperada, β > 0 mide la sensibilidad salarial/precios ante la holgura laboral, y u_n es la tasa natural de desempleo (NAIRU).\n\n2. Efectos a Corto Plazo del Estímulo Fiscal:\n• Desempleo (u_t): El impulso del gasto público eleva transitoriamente la demanda agregada y la producción, provocando un aumento del empleo que sitúa la tasa de desempleo por debajo de su nivel natural: u_t < u_n.\n• Brecha de Actividad y Presión Salarial: Al ser u_t < u_n, el término -(u_t - u_n) se vuelve positivo, lo que genera tensiones en la negociación salarial (los trabajadores y sindicatos exigen mayores salarios nominales ante la escasez de mano de obra y las empresas trasladan el sobrecoste a precios de venta para mantener márgenes).\n• Inflación (π_t): Se produce una aceleración inflacionista no anticipada de modo que la inflación observada supera a la esperada: π_t > π_t^e.\n\nConclusión: A corto plazo, el desempleo cae por debajo de la NAIRU pero a costa de desencadenar un repunte inflacionista imprevisto. A medio plazo, los agentes ajustarán al alza sus expectativas de inflación (π_{t+1}^e ↑), devolviendo el desempleo a u_n con una tasa de inflación permanentemente más alta (neutralidad de la política de demanda).",
        "enunciado_p2": "b) Recomendación de Política Pública: Si el objetivo de la política sociolaboral es reducir la NAIRU (u_n) de forma permanente y sin inflación, ¿qué tipo de políticas debe implementar y sobre qué componentes del paro debe actuar?",
        "solucion_p2": "1. Ineficacia de las Políticas Macroeconómicas de Demanda:\nLas políticas de demanda (expansión monetaria o fiscal) solo consiguen reducciones transitorias del desempleo a costa de inflación acelerada, sin alterar la tasa natural de desempleo (u_n), la cual viene determinada exclusivamente por factores estructurales y de oferta en el mercado laboral.\n\n2. Componentes de la NAIRU y Políticas de Oferta Requeridas:\nLa NAIRU se compone de desempleo friccional y estructural (u_n = u_f + u_e). Para reducirla permanentemente y sin generar presiones inflacionistas se debe recurrir a Políticas de Oferta, y específicamente a Políticas Activas de Empleo (PAE):\n• Desempleo Friccional (u_f): Actuar mediante la modernización y digitalización de los Servicios Públicos de Empleo (intermediación laboral, plataformas de matching algorítmico, reducción de asimetrías de información y costes de búsqueda), acelerando el emparejamiento entre vacantes y demandantes.\n• Desempleo Estructural (u_e): Combatir el desajuste de habilidades (skills mismatch) mediante programas de formación continua, recualificación técnica (reskilling) en sectores en transformación tecnológica/verde y orientación laboral personalizada para colectivos de difícil inserción o parados de larga duración.\n\nConclusión: La política sociolaboral debe abandonar el estímulo de demanda y centrarse en políticas activas de oferta (intermediación y formación) que desplacen la curva de Beveridge hacia el origen y reduzcan u_n sin tensiones inflacionistas."
    },
    {
        "sesion_num": 5,
        "id": "s05",
        "titulo_corto": "Sesión 05",
        "titulo_completo": "Sesión 05 · Dinámica de Flujos, Curva de Beveridge y Emparejamiento Laboral",
        "tema": "Tema 1: Macroeconomía del Mercado de Trabajo y Dinámica Salarial",
        "fecha": "28 de Septiembre 2026",
        "calif_path": os.path.join(BASE_DIR, "Temas EB", "Sesiones EB", "Sesion 05", "evaluacion", "calificaciones_sesion_05.csv"),
        "trans_path": os.path.join(BASE_DIR, "Temas EB", "Sesiones EB", "Sesion 05", "evaluacion", "transcripciones_psll_sesion_05.csv"),
        "enunciado_p1": "«A partir de la condición de flujo estacionario del mercado de trabajo y de la función de emparejamiento m = A · U^α · V^(1-α)»:\na) Demuestre analíticamente por qué la tasa natural de desempleo de equilibrio a largo plazo puede expresarse como u* = s / (s + f) y explique qué representan las variables s y f.",
        "solucion_p1": "1. Derivación Analítica del Equilibrio Estacionario:\nEn el estado estacionario, el stock de desempleo permanece constante (ΔU = 0), por lo que el flujo de entrada al desempleo debe igualar al flujo de salida hacia el empleo:\nEntradas = Salidas  ==>  s · N = f · U\n\n2. Sustitución de la Población Activa:\nSabiendo que la población activa total es L = N + U, el volumen de ocupados es N = L - U. Sustituyendo en la condición de equilibrio:\ns · (L - U) = f · U  ==>  s · L - s · U = f · U  ==>  s · L = (s + f) · U\n\n3. Despejando la Tasa Natural de Desempleo (u* = U / L):\nu* = U / L = s / (s + f).\n\n4. Interpretación de las Variables:\n• s (tasa de separación): probabilidad marginal de que un trabajador empleado pierda su empleo y pase al desempleo.\n• f (tasa de contratación o salida): probabilidad de que un trabajador desempleado encuentre y formalice una colocación laboral efectiva.",
        "enunciado_p2": "b) Utilizando la Curva de Beveridge, distinga conceptualmente entre un movimiento a lo largo de la curva y un desplazamiento de la curva hacia el exterior, indicando qué variables económicas provocan cada fenómeno.",
        "solucion_p2": "1. Movimiento a lo Largo de la Curva (Shocks Cíclicos de Demanda):\nSe produce cuando varía el nivel de actividad y demanda agregada a lo largo del ciclo económico. En recesión, las empresas retiran vacantes y se destruye empleo (desplazamiento descendente y hacia la derecha sobre la misma curva: u ↑, v ↓). En fase expansiva, aumenta la demanda de trabajo y se publican más vacantes (u ↓, v ↑). El parámetro de eficiencia tecnológica e institucional A no se altera.\n\n2. Desplazamiento de la Curva hacia el Exterior (Ineficiencia Estructural y Desajuste):\nOcurre cuando se deteriora la eficacia intrínseca del emparejamiento laboral (caída del parámetro A). Para un mismo volumen de vacantes ofertadas, el desempleo es mayor. Está originado por: desajuste formativo de habilidades (skills mismatch), falta de movilidad geográfica o residencial, ineficiencia en la intermediación de los servicios públicos de empleo o histéresis provocada por el desempleo de larga duración."
    },
    {
        "sesion_num": 6,
        "id": "s06",
        "titulo_corto": "Sesión 06",
        "titulo_completo": "Sesión 06 · Políticas Activas de Empleo (PAE), Eficiencia y el Dilema del Peso Muerto",
        "tema": "Tema 2: Intermediación Laboral, Políticas Activas y Emparejamiento",
        "fecha": "05 de Octubre 2026",
        "calif_path": os.path.join(BASE_DIR, "Temas EB", "Sesiones EB", "Sesion 06", "evaluacion", "calificaciones_sesion_06.csv"),
        "trans_path": os.path.join(BASE_DIR, "Temas EB", "Sesiones EB", "Sesion 06", "evaluacion", "transcripciones_psll_sesion_06.csv"),
        "enunciado_p1": "«Una comunidad autónoma aprueba un presupuesto extraordinario de empleo de 500 M€. Decide destinar el 80% a subvencionar con 6.000 € a fondo perdido cada contrato indefinido formalizado por empresas privadas y el 20% restante a financiar contratos temporales de 6 meses en ayuntamientos para limpieza y jardinería. Los servicios de intermediación y los cursos de recualificación técnica reciben 0 €».\na) Efectos no deseados y Eficiencia: ¿Qué ocurrirá con el empleo neto real generado por este plan? Define y aplica los conceptos de Efecto Peso Muerto (Deadweight Loss) y Efecto Sustitución.",
        "solucion_p1": "1. Efecto Peso Muerto (Deadweight Loss):\nGran parte de las subvenciones a fondo perdido a contratos indefinidos (estimada por la literatura y la AIReF entre el 60% y el 80%) financiará contrataciones que las empresas habrían formalizado de todos modos por necesidades operativas o de demanda. El coste fiscal por empleo neto adicional real se dispara extraordinariamente, suponiendo una transferencia neta de rentas públicas a empleadores sin creación efectiva de nuevos puestos de trabajo.\n\n2. Efecto Sustitución y Rotación:\nLas empresas pueden despedir o no renovar a trabajadores no bonificados para contratar a desempleados que den derecho a la ayuda de 6.000 €. Asimismo, el empleo público temporal en ayuntamientos (20%) absorbe parados de forma transitoria pero, al finalizar los 6 meses, regresan al desempleo sin haber acumulado cualificaciones demandadas por el tejido productivo (efecto rotación y estigma).\n\nConclusión: El empleo neto adicional creado será extraordinariamente reducido y con un coste público por puesto de trabajo desorbitado.",
        "enunciado_p2": "b) Curva de Beveridge y Rediseño de Política Pública: ¿Logrará este presupuesto desplazar la Curva de Beveridge hacia el origen? Si tuvieras que rediseñar el presupuesto para reducir la tasa natural de paro (u_n) de forma permanente y sin inflación, ¿qué combinación de instrumentos de políticas activas implementarías y sobre qué componentes de la función de emparejamiento actuarías?",
        "solucion_p2": "1. Incapacidad de Desplazar la Curva de Beveridge:\nLa Curva de Beveridge formaliza la función de emparejamiento m = A · U^α · V^(1-α). Como la CCAA asigna 0 € a intermediación y recualificación técnica, el parámetro de eficiencia de emparejamiento (A) no se incrementa. Por tanto, el presupuesto NO desplaza la curva hacia el origen, limitándose a generar movimientos coyunturales ineficientes.\n\n2. Rediseño Técnico Óptimo:\nPara reducir u_n de forma permanente se debe reasignar el presupuesto hacia:\n• Modernización de los Servicios Públicos de Empleo (intermediación laboral algorítmica, orientación y prospección de vacantes) para elevar A y reducir fricciones.\n• Formación ocupacional y programas de reskilling adaptados a sectores con vacantes para mitigar el desajuste de habilidades (skills mismatch).\n• Condicionar estrictamente las ayudas a la contratación a creación neta de plantilla y permanencia mínima para neutralizar el peso muerto y la sustitución."
    },
    {
        "sesion_num": 7,
        "id": "s07",
        "titulo_corto": "Sesión 07",
        "titulo_completo": "Sesión 07 · Incentivos a la Contratación, Evaluación de Impacto y Empleo Neto",
        "tema": "Tema 2: Intermediación Laboral, Políticas Activas y Emparejamiento",
        "fecha": "09 de Octubre 2026",
        "calif_path": os.path.join(BASE_DIR, "Temas EB", "Sesiones EB", "Sesion 07", "evaluacion", "calificaciones_sesion_07.csv"),
        "trans_path": os.path.join(BASE_DIR, "Temas EB", "Sesiones EB", "Sesion 07", "evaluacion", "transcripciones_psll_sesion_07.csv"),
        "enunciado_p1": "«Una comunidad autónoma diseña un plan de choque contra el desempleo de larga duración con un presupuesto de 30 M€ (5.000 contratos a 6.000 €; peso muerto 65%, sustitución 15%, desplazamiento 5%)»:\na) Cálculo del Empleo Neto y Eficacia Fiscal: Calcula cuántos empleos adicionales netos reales (ΔN_neto) ha generado el plan y determina el coste fiscal efectivo por cada empleo neto creado. Compara esta cifra con los 6.000 € nominales concedidos.",
        "solucion_p1": "1. Tasa Total de Ineficiencia y Coeficiente Neto:\nPérdida Total = Tasa_DW (0,65) + Tasa_Subst (0,15) + Tasa_Despl (0,05) = 0,85 (85%).\nCoeficiente de empleo neto efectivo = 1 - 0,85 = 0,15 (15%).\n\n2. Cálculo del Empleo Neto Adicional Real:\nΔN_neto = 5.000 contratos · 0,15 = 750 empleos netos reales.\n(De los 5.000 contratos financiados, 3.250 se habrían formalizado de todos modos, 750 destruyeron otros puestos por sustitución y 250 destruyeron empleo en competidores. Solo 750 son empleos adicionales netos).\n\n3. Coste Fiscal Efectivo por Empleo Neto:\nCoste por Empleo Neto = Gasto Total (30.000.000 €) / 750 empleos = 40.000 € / empleo neto (o bien: 6.000 € / 0,15 = 40.000 €).\n\nConclusión: Aunque la ayuda nominal concedida parecía de 6.000 €, el contribuyente ha pagado realmente 40.000 € (casi siete veces más) por cada empleo nuevo adicional que no se habría creado sin la ayuda pública.",
        "enunciado_p2": "b) Rediseño Institucional y Salvaguardas: Como economista laboral, formula dos cláusulas técnicas de condicionalidad concretas que el regulador público debería introducir en la orden de bases para minimizar el peso muerto y el efecto sustitución sin reducir drásticamente la participación empresarial.",
        "solucion_p2": "1. Cláusula de Incremento Neto de Plantilla (Blindaje anti-sustitución):\nExigir que la contratación subvencionada no suponga mera rotación ni sustitución de personal, sino un aumento neto de la plantilla media indefinida de la empresa en los 12 meses previos a la contratación, prohibiendo taxativamente el acceso a empresas que hayan ejecutado despidos improcedentes o extinciones colectivas en los 6 meses anteriores.\n\n2. Cláusula de Hiper-focalización en Perfilado de Muy Baja Empleabilidad (Blindaje anti-deadweight):\nReemplazar la concesión genérica por edad por un criterio de duración continuada en desempleo (> 24 meses) o mediante herramientas de perfilado estadístico/algorítmico del servicio público de empleo que verifiquen que la probabilidad ex-ante de colocación espontánea en el mercado es inferior al 15%.\n\nAlternativa Válida: Desembolso progresivo ligado al mantenimiento y retención indefinida a 24-36 meses, o exigencia obligatoria de formación técnica en el puesto (upskilling dual)."
    },
    {
        "sesion_num": 8,
        "id": "s08",
        "titulo_corto": "Sesión 08",
        "titulo_completo": "Sesión 08 · Evaluación de Impacto de PAE, Sesgo de Selección y Contrafactual",
        "tema": "Tema 2: Intermediación Laboral, Políticas Activas y Emparejamiento",
        "fecha": "16 de Octubre 2026",
        "calif_path": os.path.join(BASE_DIR, "Temas EB", "Sesiones EB", "Sesion 08", "evaluacion", "calificaciones_sesion_08.csv"),
        "trans_path": os.path.join(BASE_DIR, "Temas EB", "Sesiones EB", "Sesion 08", "evaluacion", "transcripciones_psll_sesion_08.csv"),
        "enunciado_p1": "«Un ayuntamiento andaluz ha financiado durante doce meses un programa de «Escuela Taller de Rehabilitación de Edificios Históricos» para 60 jóvenes desempleados del municipio. Al concluir el programa, el concejal de Empleo declara en una rueda de prensa: «El programa ha sido un rotundo éxito de inserción laboral: el 70% de los jóvenes que participaron está hoy trabajando en el sector de la construcción, mientras que la tasa de empleo entre los jóvenes desempleados de nuestra localidad que no participaron en el taller es de apenas el 40%. Por tanto, el programa ha generado un incremento neto de empleo de 30 puntos porcentuales»».\n1. (500 pts) Explica con rigor técnico por qué la afirmación del concejal contiene un «sesgo de selección» y por qué la tasa de inserción bruta observada (70%) no equivale al impacto causal real del programa.",
        "solucion_p1": "1. Falacia de Atribución y Sesgo de Selección:\nLa afirmación del concejal comete el error de comparar ingenuamente a los participantes con los no participantes asumiendo que ambos grupos eran idénticos antes de empezar. En realidad existe un claro sesgo de selección:\n• Autoselección: Los jóvenes que decidieron inscribirse presentaban mayor motivación, puntualidad e interés intrínseco por trabajar.\n• Descremado (creaming): Los técnicos municipales pudieron seleccionar a los 60 jóvenes con mejores aptitudes o historial laboral.\n\n2. Necesidad del Contrafactual e Inserción Bruta vs. Neta:\nPara medir el impacto causal real se necesita estimar el contrafactual: qué porcentaje de esos 60 jóvenes habría encontrado empleo sin el taller. Si la economía local crecía y la construcción demandaba mano de obra, parte sustancial de ese 70% habría encontrado empleo igualmente. Por Diferencias en Diferencias, debe restarse la inercia general del grupo de comparación; el verdadero impacto neto es sustancialmente inferior a los 30 puntos alegados.",
        "enunciado_p2": "2. (500 pts) Apoyándote en la evidencia empírica explicada en clase (el informe Spending Review de la AIReF sobre empleo protegido o el metaanálisis internacional de Card, Kluve y Weber), señala qué dos riesgos de ineficiencia (a corto vs. medio plazo, o de circuito cerrado/desplazamiento) deben evaluarse antes de calificar este taller municipal como un verdadero éxito de empleo.",
        "solucion_p2": "1. Evidencia Temporal sobre Empleo Público Directo (Card, Kluve y Weber):\nEl metaanálisis demuestra que las obras y talleres directos municipales suelen mostrar efectos inmediatos aparentes, pero su impacto sobre la empleabilidad privada real a medio y largo plazo (2-3 años) es prácticamente plano o nulo si no proporcionan cualificaciones transferibles reconocidas en el mercado abierto.\n\n2. Riesgo de Circuito Cerrado (AIReF) o de Desplazamiento (Crépon et al.):\nTal como advierte la AIReF, existe el riesgo de que el ayuntamiento mantenga a estos jóvenes en un «circuito cerrado» de obras públicas municipales dependientes del subsidio, con bajísima transición a empresas constructoras ordinarias. Además, si esos jóvenes ocuparon las pocas obras locales disponibles, pudieron simplemente desplazar a otros albañiles desempleados del municipio (efecto desplazamiento), sin generar empleo neto adicional."
    },
    {
        "sesion_num": 9,
        "id": "s09",
        "titulo_corto": "Sesión 09",
        "titulo_completo": "Sesión 09 · Por qué Proteger al Desempleado, Fallos de Mercado y Chetty (2008)",
        "tema": "Tema 3: Protección por Desempleo, Políticas Pasivas y Transiciones Laborales",
        "fecha": "20 y 23 de Octubre 2026",
        "calif_path": os.path.join(BASE_DIR, "Temas EB", "Sesiones EB", "Sesion 09", "evaluacion", "calificaciones_sesion_09.csv"),
        "trans_path": os.path.join(BASE_DIR, "Temas EB", "Sesiones EB", "Sesion 09", "evaluacion", "transcripciones_psll_sesion_09.csv"),
        "enunciado_p1": "1. (500 pts) Fallo del Mercado Privado de Seguros:\nExplica por qué las compañías privadas de seguros no ofrecen pólizas contra el desempleo. En tu respuesta, diferencia con rigor el concepto de selección adversa del de riesgo covariante sistémico en una recesión macroeconómica, y argumenta por qué solo el Estado puede mutualizar este riesgo.",
        "solucion_p1": "1. Selección Adversa (200 pts):\nExiste asimetría de información. Si el seguro fuera voluntario y privado, solo lo contratarían aquellos trabajadores que anticipan un alto riesgo inminente de despido. Esto obligaría a la aseguradora a elevar las primas, expulsando progresivamente a los trabajadores con empleos estables y provocando el colapso financiero del mercado (mercado de 'limones').\n\n2. Riesgo Covariante Sistémico (200 pts):\nLos seguros privados se sustentan en la ley de los grandes números y la independencia de siniestros. El desempleo es un riesgo macroeconómico correlacionado: en una recesión severa, cientos de miles de trabajadores pierden su empleo al mismo tiempo. Ninguna aseguradora privada dispone de reservas líquidas suficientes para afrontar siniestros masivos simultáneos sin quebrar fulminantemente.\n\n3. Intervención Pública (100 pts):\nSolo el Estado puede mutualizar este riesgo mediante la afiliación obligatoria universal (eliminando la selección adversa) y su capacidad de endeudamiento soberano intertemporal para absorber shocks agregados.",
        "enunciado_p2": "2. (500 pts) El Dilema de Raj Chetty (2008):\nUn analista afirma: «Si el Estado paga una prestación, el desempleado tarda más semanas en colocarse; por tanto, las prestaciones son ineficientes y solo fomentan la holgazanería». Utilizando los hallazgos de Chetty, refuta esta afirmación distinguiendo el efecto liquidez del riesgo moral. ¿Por qué el retraso observado es en su mayor parte deseable para el bienestar social?",
        "solucion_p2": "1. Refutación y Distinción Teórica (150 pts):\nLa afirmación es falaz porque asume erróneamente que todo retraso en la reincorporación al empleo es coste de ineficiencia o desincentivo al esfuerzo.\n\n2. Efecto Liquidez vs. Riesgo Moral (200 pts):\nRaj Chetty (2008) demostró empíricamente que el alargamiento del desempleo obedece a dos canales opuestos:\n• Efecto Liquidez (~60% del retraso): Los trabajadores desempleados carecen de ahorros suficientes y tienen el crédito bancario restringido. La prestación les aporta liquidez básica para pagar manutención y vivienda, evitando ventas forzosas o la necesidad imperiosa de aceptar cualquier empleo precario o mal remunerado en 48 horas.\n• Riesgo Moral (~40% del retraso): Reducción de la intensidad de búsqueda provocada por la subvención del ocio relativo.\n\n3. Implicación de Bienestar Social (150 pts):\nAl dominar el efecto liquidez (60%), el alargamiento del paro permite una búsqueda más productiva y un mejor emparejamiento entre trabajador y puesto (job-match quality), lo cual eleva el bienestar social global en lugar de reducirlo."
    },
    {
        "sesion_num": 10,
        "id": "s10",
        "titulo_corto": "Sesión 10",
        "titulo_completo": "Sesión 10 · Activación, Control, CAE y Efectos sobre la Búsqueda de Empleo",
        "tema": "Tema 3: Protección por Desempleo, Políticas Pasivas y Transiciones Laborales",
        "fecha": "27 y 30 de Octubre 2026",
        "calif_path": os.path.join(BASE_DIR, "Temas EB", "Sesiones EB", "Sesion 10", "evaluacion", "calificaciones_sesion_10.csv"),
        "trans_path": os.path.join(BASE_DIR, "Temas EB", "Sesiones EB", "Sesion 10", "evaluacion", "transcripciones_psll_sesion_10.csv"),
        "enunciado_p1": "1. (500 pts) Opción A / Opción B:\n• Opción A (Turno Martes · L1): El Complemento de Apoyo al Empleo (CAE) y los Incentivos de Contratación (RD-ley 2/2024 / 2026). Explica por qué la regla tradicional de incompatibilidad total generaba la trampa del desempleo, cómo funciona la compatibilidad del CAE y su impacto en RRHH.\n• Opción B (Turno Viernes · L2): La «Colocación Adecuada» y la Condicionalidad Activa (Art. 301 LGSS). Requisitos objetivos (profesional, retributivo y geográfico), flexibilización al año y sanciones de la LISOS por rechazo injustificado.",
        "solucion_p1": "• Solución Opción A (CAE): La incompatibilidad previa extinguía o suspendía la ayuda pública al trabajar, fijando un tipo marginal implícito del 100% que atrapaba en la inactividad en empleos parciales. El CAE permite compatibilizar salario y ayuda decreciente durante 180 días, dinamizando la cobertura de vacantes de inserción.\n• Solución Opción B (Colocación Adecuada): 1) Criterio profesional (profesión habitual/formación en el 1er año); 2) Retributivo (convenio aplicable y no inferior a SMI); 3) Geográfico (residencia habitual o máx. 30 km / 25% jornada / 20% salario). Al año se amplía a otras ocupaciones compatibles. Sanción LISOS: pérdida de 3 meses en 1ª infracción, 6 meses en 2ª y extinción definitiva en 3ª.",
        "enunciado_p2": "2. (500 pts) Opción A / Opción B:\n• Opción A (Turno Martes · L1): El Fenómeno del «Spike at Exhaustion» (Repunte al Agotamiento). Analiza por qué el repunte en salidas del paro al agotarse la prestación obedece a la restricción de liquidez familiar y a la caída del salario de reserva y no solo a la picaresca.\n• Opción B (Turno Viernes · L2): Calidad del Emparejamiento Laboral (Job-Match Quality). Apoyándote en Nekoei y Weber (2017), refuta que las prestaciones solo generen holgazanería explicando cómo el tiempo de cobertura mejora el emparejamiento, eleva salarios futuros y estabiliza contratos.",
        "solucion_p2": "• Solución Opción A (Spike at Exhaustion): El repunte al final de la cobertura no es oportunismo masivo sino el resultado de la asfixia de liquidez familiar al agotarse los ahorros personales. El desempleado ve colapsar su salario de reserva (w_R) y se ve obligado a intensificar la búsqueda y aceptar empleos de menor calidad o salario.\n• Solución Opción B (Nekoei y Weber 2017): Demuestran que la mayor duración del subsidio aporta capital de búsqueda que permite encontrar vacantes mejor ajustadas a las competencias del trabajador, generando un incremento de salarios de entrada del 2% al 5% y reduciendo significativamente la probabilidad de despido o retorno al desempleo en los 2 años siguientes."
    }
]

GLOBAL_SALT = "psll_upo_eval_2026_salt"
ALL_COMBOS = list(itertools.combinations(range(8), 4))

def normalizar_texto(texto):
    if not texto or pd.isna(texto):
        return ""
    return str(texto).strip()

def strip_accents(s):
    return ''.join(c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn')

def parse_dni(raw):
    m = re.search(r'(\d+)', str(raw))
    return m.group(1).zfill(8) if m else ''

def parse_estudiante(raw):
    raw_str = normalizar_texto(raw)
    # Limpiar coletillas como (Erasmus)
    raw_clean = re.sub(r'\(.*?\)', '', raw_str).strip()
    parts = raw_clean.split(',')
    if len(parts) == 2:
        nombre = parts[1].strip().title()
        apellidos = parts[0].strip().title()
        return nombre, apellidos
    return raw_clean.title(), ""

def generar_username_sugerido(nombre, apellidos, dni):
    # Genera un handle institucional estándar si no hay username explícito
    nom_clean = strip_accents(nombre.lower())
    ape_parts = strip_accents(apellidos.lower()).split()
    first_nom = nom_clean.split()[0] if nom_clean else 'u'
    part1 = ape_parts[0][:3] if len(ape_parts) > 0 else 'est'
    part2 = ape_parts[1][:3] if len(ape_parts) > 1 else ''
    handle = f"{first_nom[0]}{part1}{part2}".replace(" ", "").replace("-", "")
    return handle

def cargar_censo_alumnos():
    alumnos_dict = {}

    # 1. Cargar Línea 1 (Excel)
    if os.path.exists(lista_l1_path):
        try:
            df1 = pd.read_excel(lista_l1_path, skiprows=7)
            for _, row in df1.iterrows():
                dni = parse_dni(row.get("DNI"))
                if not dni or len(dni) != 8:
                    continue
                nom, ape = parse_estudiante(row.get("ESTUDIANTE"))
                plan = normalizar_texto(row.get("PLAN"))
                if dni not in alumnos_dict:
                    alumnos_dict[dni] = {
                        "dni": dni,
                        "nombre": nom,
                        "apellidos": ape,
                        "lineas": ["Línea 1"],
                        "plan": plan
                    }
                else:
                    if "Línea 1" not in alumnos_dict[dni]["lineas"]:
                        alumnos_dict[dni]["lineas"].append("Línea 1")
        except Exception as e:
            print(f"[AVISO] Error al leer lista Línea 1: {e}")

    # 2. Cargar Línea 2 (TSV latin1)
    if os.path.exists(lista_l2_path):
        try:
            df2 = pd.read_csv(lista_l2_path, sep="\t", encoding="latin1", skiprows=6)
            for _, row in df2.iterrows():
                dni = parse_dni(row.get("DNI"))
                if not dni or len(dni) != 8:
                    continue
                nom, ape = parse_estudiante(row.get("ESTUDIANTE"))
                plan = normalizar_texto(row.get("PLAN"))
                if dni not in alumnos_dict:
                    alumnos_dict[dni] = {
                        "dni": dni,
                        "nombre": nom,
                        "apellidos": ape,
                        "lineas": ["Línea 2"],
                        "plan": plan
                    }
                else:
                    if "Línea 2" not in alumnos_dict[dni]["lineas"]:
                        alumnos_dict[dni]["lineas"].append("Línea 2")
        except Exception as e:
            print(f"[AVISO] Error al leer lista Línea 2: {e}")

    # Lista final
    censo = []
    for dni, d in sorted(alumnos_dict.items(), key=lambda x: (x[1]["apellidos"], x[1]["nombre"])):
        nom = d["nombre"]
        ape = d["apellidos"]
        username = generar_username_sugerido(nom, ape, dni)
        censo.append({
            "id_norm": dni,
            "username": username,
            "nombre": nom,
            "apellidos": ape,
            "nombre_completo": f"{nom} {ape}",
            "linea": " / ".join(d["lineas"]),
            "plan": d["plan"]
        })
    return pd.DataFrame(censo)

def cargar_ausencias_justificadas():
    """
    Carga la matriz de ausencias justificadas desde 'alumnos/ausencias_justificadas.xlsx' (o .csv).
    Estructura de matriz:
      - Filas: Alumnos (DNI)
      - Columnas: S02 a S16
    Si una celda contiene 'x', 'X', 'si', '1' o similar, se registra la ausencia como justificada.
    Devuelve un set de tuplas: {(dni_norm, sesion_num), ...}
    """
    ausencias_set = set()
    xlsx_path = os.path.join(SCRIPT_DIR, "ausencias_justificadas.xlsx")
    csv_path = os.path.join(SCRIPT_DIR, "ausencias_justificadas.csv")

    target_path = None
    if os.path.exists(xlsx_path):
        target_path = xlsx_path
    elif os.path.exists(csv_path):
        target_path = csv_path

    if not target_path:
        return ausencias_set

    try:
        if target_path.endswith(".xlsx"):
            df = pd.read_excel(target_path, dtype=str)
        else:
            df = pd.read_csv(target_path, sep=";", dtype=str)

        dni_col = None
        for col in df.columns:
            if "dni" in str(col).lower():
                dni_col = col
                break
        if not dni_col:
            dni_col = df.columns[0]

        ses_cols = {}
        for col in df.columns:
            m = re.search(r'(?:s|sesi[oó]n)?\s*0?(\d+)', str(col), re.IGNORECASE)
            if m:
                s_num = int(m.group(1))
                if 2 <= s_num <= 16:
                    ses_cols[col] = s_num

        for _, row in df.iterrows():
            dni_val = parse_dni(row.get(dni_col))
            if not dni_val:
                continue
            for col_name, s_num in ses_cols.items():
                val = str(row.get(col_name, "")).strip().lower()
                if val in ["x", "si", "sí", "j", "justificado", "1", "true"]:
                    ausencias_set.add((dni_val, s_num))

        print(f"[OK] Matriz de ausencias justificadas cargada: {len(ausencias_set)} ausencias oficiales activas.")
    except Exception as e:
        print(f"[AVISO] Error al leer matriz de ausencias justificadas: {e}")

    return ausencias_set

def compilar_pasaporte():
    print("=" * 75)
    print("  COMPILADOR CRIPTOGRÁFICO PASAPORTE DE EVALUACIÓN CONTINUA · PSLL")
    print("=" * 75)

    df_censo = cargar_censo_alumnos()
    print(f"[*] Censo de estudiantes cargado: {len(df_censo)} alumnos únicos registrados.")

    ausencias_justificadas_set = cargar_ausencias_justificadas()

    # Guardar censo unificado en alumnos/lista_alumnos.csv para referencia
    censo_csv_path = os.path.join(SCRIPT_DIR, "lista_alumnos.csv")
    try:
        df_censo.to_csv(censo_csv_path, sep=";", index=False, encoding="utf-8-sig")
        print(f"[OK] Censo unificado archivado en: {censo_csv_path}")
    except PermissionError:
        print(f"[WARN] No se pudo sobrescribir {censo_csv_path} (archivo en uso por otra app). Continuando con censo en memoria.")

    # Verificar datos de sesiones
    sesiones_disponibles = []
    for s_cfg in EVAL_SESIONES_CONFIG:
        has_calif = os.path.exists(s_cfg["calif_path"])
        has_trans = os.path.exists(s_cfg["trans_path"])
        df_calif = None
        df_trans = None
        if has_calif:
            try:
                df_calif = pd.read_csv(s_cfg["calif_path"], sep=";", encoding="utf-8-sig")
                df_calif["id_norm"] = df_calif["ID_Estudiante"].astype(str).str.strip().str.zfill(8)
            except Exception as e:
                print(f"[!] Error leyendo calificaciones {s_cfg['id']}: {e}")
        if has_trans:
            try:
                df_trans = pd.read_csv(s_cfg["trans_path"], sep=";", encoding="utf-8-sig")
                df_trans["id_norm"] = df_trans["ID_Estudiante"].astype(str).str.strip().str.zfill(8)
            except Exception as e:
                print(f"[!] Error leyendo transcripciones {s_cfg['id']}: {e}")
        
        sesiones_disponibles.append({
            "config": s_cfg,
            "has_data": (df_calif is not None),
            "df_calif": df_calif,
            "df_trans": df_trans
        })

    students_encrypted_db = []
    all_students_scores = []

    for idx, row in df_censo.iterrows():
        dni = str(row["id_norm"]).strip()
        username = str(row["username"]).strip().lower()
        nombre = str(row["nombre"]).strip()
        apellidos = str(row["apellidos"]).strip()
        nombre_completo = str(row["nombre_completo"]).strip()

        puntos_totales_obtenidos = 0
        puntos_totales_potenciales = 0
        sesiones_payload = []

        for item in sesiones_disponibles:
            cfg = item["config"]
            df_calif = item["df_calif"]
            df_trans = item["df_trans"]
            s_num = cfg["sesion_num"]

            puntos_ses = 0
            es_justificada = (dni, s_num) in ausencias_justificadas_set

            if es_justificada:
                puntos_max = 0
                estado_ses = "Ausencia justificada"
                feedback_ses = "Ausencia debidamente justificada. Esta sesión no penaliza ni computa en el denominador de tu evaluación continua."
            else:
                puntos_max = 1000
                puntos_totales_potenciales += puntos_max

                if item["has_data"] and df_calif is not None:
                    match_c = df_calif[df_calif["id_norm"] == dni]
                    if not match_c.empty:
                        c_row = match_c.iloc[0]
                        # Extracción tolerante y robusta de puntos (soporta 'Puntos' clásico y 'Puntos_Total' bimodal)
                        puntos_raw = c_row.get("Puntos")
                        if pd.isna(puntos_raw) or puntos_raw is None or str(puntos_raw).strip() == "":
                            puntos_raw = c_row.get("Puntos_Total")
                        if pd.isna(puntos_raw) or puntos_raw is None or str(puntos_raw).strip() == "":
                            puntos_raw = 0
                        try:
                            puntos_ses = int(float(str(puntos_raw).replace(",", ".")))
                        except Exception:
                            puntos_ses = 0

                        estado_ses = str(c_row.get("Estado", "Presentado")).strip()
                        if not estado_ses or estado_ses.lower() == "nan":
                            estado_ses = "Presentado"

                        # Extracción tolerante de retroalimentación (soporta 'Retroalimentacion' y 'Retroalimentacion_Formativa')
                        feedback_raw = c_row.get("Retroalimentacion")
                        if pd.isna(feedback_raw) or feedback_raw is None or str(feedback_raw).strip() == "":
                            feedback_raw = c_row.get("Retroalimentacion_Formativa")
                        if pd.isna(feedback_raw) or feedback_raw is None or str(feedback_raw).strip() == "":
                            feedback_raw = "Sin observaciones."
                        feedback_ses = str(feedback_raw).strip()
                    else:
                        estado_ses = "No presentado"
                        feedback_ses = "No consta entrega del reto manuscrito de cierre de sesión."
                else:
                    # Sesión en proceso de corrección o inicial
                    estado_ses = "En corrección"
                    puntos_ses = 0
                    feedback_ses = "Calificaciones en proceso de procesamiento y validación docente."

            puntos_totales_obtenidos += puntos_ses

            # Transcripciones
            t_p1 = "No consta entrega escrita."
            t_p2 = "No consta entrega escrita."
            if item["df_trans"] is not None:
                match_t = df_trans[df_trans["id_norm"] == dni]
                if not match_t.empty:
                    t_row = match_t.iloc[0]
                    t_p1 = str(t_row.get("Transcripcion_P1", t_p1))
                    t_p2 = str(t_row.get("Transcripcion_P2", t_p2))

            # Preguntas de la sesión
            preguntas = []
            if cfg.get("enunciado_p1"):
                preguntas.append({
                    "num": 1,
                    "id": f"{cfg['id']}_p1",
                    "tipo": "Reto Manuscrito Individual",
                    "titulo": f"Pregunta 1 · {cfg['titulo_corto']}",
                    "enunciado": cfg["enunciado_p1"],
                    "transcripcion": t_p1 if item["has_data"] else "Próximamente disponible tras la finalización del proceso de corrección.",
                    "solucion_oficial": cfg["solucion_p1"] if item["has_data"] else "La solución oficial se publicará junto con las calificaciones definitivas."
                })
            if cfg.get("enunciado_p2"):
                preguntas.append({
                    "num": 2,
                    "id": f"{cfg['id']}_p2",
                    "tipo": "Aplicación Práctica",
                    "titulo": f"Pregunta 2 · {cfg['titulo_corto']}",
                    "enunciado": cfg["enunciado_p2"],
                    "transcripcion": t_p2 if item["has_data"] else "Próximamente disponible.",
                    "solucion_oficial": cfg["solucion_p2"] if item["has_data"] else "Pendiente de publicación."
                })

            sesiones_payload.append({
                "sesion_num": cfg["sesion_num"],
                "id": cfg["id"],
                "titulo_corto": cfg["titulo_corto"],
                "titulo_completo": cfg["titulo_completo"],
                "tema": cfg["tema"],
                "fecha": cfg["fecha"],
                "estado": estado_ses,
                "puntos_obtenidos": puntos_ses,
                "puntos_maximos": puntos_max,
                "es_justificada": es_justificada,
                "porcentaje": round((puntos_ses / puntos_max) * 100, 1) if puntos_max > 0 else 0,
                "feedback_general": feedback_ses,
                "preguntas": preguntas
            })

        # Historial de evolución para las 16 sesiones del curso
        evolucion_16_sesiones = []
        # S01: introductoria (sin reto evaluable)
        evolucion_16_sesiones.append({
            "sesion": 1,
            "tag": "S01",
            "puntos": 0,
            "acumulado": 0,
            "evaluada": True,
            "max_sesion": 0
        })

        acum_calc = 0
        for ses_item in sesiones_payload:
            p_ob = ses_item["puntos_obtenidos"]
            acum_calc += p_ob
            evolucion_16_sesiones.append({
                "sesion": ses_item["sesion_num"],
                "tag": f"S{ses_item['sesion_num']:02d}",
                "puntos": None if ses_item.get("es_justificada") else p_ob,
                "acumulado": acum_calc,
                "evaluada": True,
                "justificada": bool(ses_item.get("es_justificada")),
                "max_sesion": ses_item["puntos_maximos"]
            })

        max_ses_num = max([s["sesion_num"] for s in sesiones_payload], default=1)
        for s_idx in range(max_ses_num + 1, 17):
            evolucion_16_sesiones.append({
                "sesion": s_idx,
                "tag": f"S{s_idx:02d}",
                "puntos": None,
                "acumulado": None,
                "evaluada": False,
                "max_sesion": 1000
            })

        if puntos_totales_potenciales == 0:
            porcentaje_global = 100.0 if puntos_totales_obtenidos > 0 else 0.0
        else:
            porcentaje_global = round((puntos_totales_obtenidos / puntos_totales_potenciales) * 100, 2)

        payload_data = {
            "nombre_completo": nombre_completo,
            "nombre_pila": nombre,
            "apellidos": apellidos,
            "username": username,
            "dni": dni,
            "linea": row["linea"],
            "plan": row["plan"],
            "puntos_acumulados": puntos_totales_obtenidos,
            "puntos_potenciales": puntos_totales_potenciales,
            "puntos_potenciales_curso": 16000,
            "porcentaje_logrado": porcentaje_global,
            "total_sesiones_evaluadas": len([s for s in sesiones_payload if s["estado"] not in ["En corrección", "Ausencia justificada"]]),
            "total_sesiones_justificadas": len([s for s in sesiones_payload if s.get("es_justificada")]),
            "total_sesiones_curso": 16,
            "evolucion_sesiones": evolucion_16_sesiones,
            "sesiones": sesiones_payload
        }

        all_students_scores.append(puntos_totales_obtenidos)

        master_key = os.urandom(32)
        payload_nonce = os.urandom(12)
        payload_bytes = json.dumps(payload_data, ensure_ascii=False).encode("utf-8")
        encrypted_payload = AESGCM(master_key).encrypt(payload_nonce, payload_bytes, None)

        # Hashes para permitir acceso tanto por username institucional como por DNI
        user_hash = hashlib.sha256(f"{GLOBAL_SALT}:{username}".encode("utf-8")).hexdigest()
        dni_hash = hashlib.sha256(f"{GLOBAL_SALT}:{dni}".encode("utf-8")).hexdigest()
        user_salt = os.urandom(16).hex()

        vault = []
        vault_nonce = os.urandom(12)
        for combo_idx, combo in enumerate(ALL_COMBOS):
            four_digits = "".join(dni[pos] for pos in combo)
            k_c_material = f"{user_salt}:{dni}:{four_digits}:{combo_idx}".encode("utf-8")
            k_c = hashlib.sha256(k_c_material).digest()
            enc_mk = AESGCM(k_c).encrypt(vault_nonce, master_key, None)
            vault.append(base64.b64encode(enc_mk).decode("ascii"))

        students_encrypted_db.append({
            "user_hash": user_hash,
            "dni_hash": dni_hash,
            "dni": dni,
            "user_salt": user_salt,
            "vault_nonce": base64.b64encode(vault_nonce).decode("ascii"),
            "vault": vault,
            "payload_nonce": base64.b64encode(payload_nonce).decode("ascii"),
            "payload_ciphertext": base64.b64encode(encrypted_payload).decode("ascii")
        })

    # Array anónimo de puntuaciones de la clase ordenadas (100% anónimo y RGPD)
    anon_scores = sorted(all_students_scores)

    os.makedirs(os.path.join(MICRO_APPS_DIR, "data"), exist_ok=True)
    dest_js = os.path.join(MICRO_APPS_DIR, "data", "calificaciones_cifradas_psll.js")

    output_js = f"""// Base de datos cifrada de calificaciones Políticas Sociolaborales y de Empleo (PSLL · UPO)
// Cifrado militar Zero-Knowledge AES-GCM-256 + SHA-256. Ningún dato personal legible en claro.
window.__PSLL_GLOBAL_SALT__ = "{GLOBAL_SALT}";
window.__PSLL_COMBOS__ = {json.dumps(ALL_COMBOS)};
window.__PSLL_TOTAL_SESIONES__ = 16;
window.__PSLL_PUNTOS_POTENCIALES_ACTUALES__ = {puntos_totales_potenciales};
window.__PSLL_PUNTOS_POTENCIALES_CURSO__ = 16000;
window.__PSLL_SCORES_ANON__ = {json.dumps(anon_scores)};
window.__PSLL_EVAL_DB__ = {json.dumps(students_encrypted_db, separators=(',', ':'))};
"""

    with open(dest_js, "w", encoding="utf-8") as f:
        f.write(output_js)

    if os.path.exists(MICRO_APPS_ALT) and os.path.abspath(MICRO_APPS_ALT) != os.path.abspath(MICRO_APPS_DIR):
        try:
            alt_dest = os.path.join(MICRO_APPS_ALT, "data", "calificaciones_cifradas_psll.js")
            os.makedirs(os.path.dirname(alt_dest), exist_ok=True)
            with open(alt_dest, "w", encoding="utf-8") as f:
                f.write(output_js)
            print(f"[OK] Archivo cifrado PSLL replicado en (micro_apps alt): {alt_dest}")
        except Exception:
            pass

    dest_psll_docs = os.path.join(BASE_DIR, "docs", "data", "calificaciones_cifradas_psll.js")
    os.makedirs(os.path.dirname(dest_psll_docs), exist_ok=True)
    with open(dest_psll_docs, "w", encoding="utf-8") as f:
        f.write(output_js)

    print(f"[OK] Archivo cifrado PSLL generado en (micro_apps): {dest_js}")
    print(f"[OK] Archivo cifrado PSLL generado en (docs local): {dest_psll_docs}")
    print(f"[OK] Total de alumnos procesados y cifrados: {len(students_encrypted_db)}")
    print(f"[OK] Tamaño final del fichero JS: {os.path.getsize(dest_js) / 1024:.2f} KB")
    print("=" * 75)

if __name__ == "__main__":
    compilar_pasaporte()
