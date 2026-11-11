# -*- coding: utf-8 -*-
"""
Generador optimizado de la presentación web interactiva (.html) para la Sesión EB 12:
«Flexibilidad externa, protección del empleo (EPL) y dualidad laboral»
Ajustes ergonómicos:
- Ampliación tipográfica y eliminación de espacios vacíos en slides 8, 10, 12, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23.
- Rediseño limpio del Diagrama de Flujo en Slide 7 sin colisiones de texto con líneas.
- Eliminación del solape visual sobre "danés" en Slide 9 y protección de cabeceras.
- Destacado exterior ultra-legible de la Prima de Litigiosidad en Slide 13 con pastilla blanca de alto contraste.
- Ampliación de los códigos QR (a 310x310 px) en Slides 5, 18, 20 y 21.
Profesor: Manuel A. Hidalgo Pérez
"""

import os

SESION_DIR = r"c:\Users\Usuario\Documents\Dropbox\DOCENCIA UPO\CURSO 26-27\PSLL\Temas EB\Sesiones EB\Sesion 12"
OUTPUT_HTML = os.path.join(SESION_DIR, "Sesion 12 - Flexibilidad externa, proteccion del empleo y dualidad laboral.html")

html_code = r'''<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Sesión 12 · Flexibilidad Externa, Protección del Empleo (EPL) y Dualidad | PSLL UPO</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;600;700;800&family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,600;1,6..72,400&family=Calibri:wght@400;700&display=swap" rel="stylesheet">
<style>
:root {
  --pino: #113927;
  --salvia: #76927A;
  --coral: #E98F71;
  --menta: #F4F8F5;
  --menta-borde: #C2D8C9;
  --tinta: #2F3A30;
  --blanco: #FFFFFF;
  --papel: #FBFBF9;
  --gris-claro: #EBEFEB;
  --sombra-card: 0 4px 16px rgba(17, 57, 39, 0.06);
}

* { box-sizing: border-box; margin: 0; padding: 0; }

body {
  background-color: #0d1e15;
  color: var(--tinta);
  font-family: 'Calibri', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
  overflow: hidden;
  height: 100vh;
  width: 100vw;
  display: flex;
  justify-content: center;
  align-items: center;
  user-select: none;
}

#stage {
  width: 1600px;
  height: 900px;
  position: relative;
  background-color: var(--blanco);
  overflow: hidden;
  box-shadow: 0 20px 60px rgba(0,0,0,0.4);
  transform-origin: center center;
}

/* MARCA DE AGUA VECTORIAL FIJA (ANILLOS ENTRELAZADOS PSLL + ONDA CORAL) */
.watermark-layer {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  z-index: 1;
  pointer-events: none;
  opacity: 0.035; /* Ajustada para máxima sutileza institucional */
  display: flex;
  align-items: center;
  justify-content: center;
}

.watermark-layer svg {
  width: 900px;
  height: 900px;
}

/* DIAPOSITIVAS */
.slide {
  position: absolute;
  top: 0;
  left: 0;
  width: 1600px;
  height: 900px;
  padding: 50px 80px 60px 80px;
  opacity: 0;
  visibility: hidden;
  transition: opacity 0.35s ease, visibility 0.35s ease;
  z-index: 2;
  background: transparent;
  display: flex;
  flex-direction: column;
}

.slide.active {
  opacity: 1;
  visibility: visible;
}

/* PORTADA */
.slide-cover {
  background-color: var(--pino) !important;
  color: var(--blanco);
  padding: 0;
  justify-content: space-between;
}

.cover-body {
  flex: 1;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  text-align: center;
  padding: 40px 100px;
  position: relative;
}

.cover-logo-box {
  background: #ffffff;
  padding: 24px 44px;
  border-radius: 16px;
  box-shadow: 0 10px 30px rgba(0,0,0,0.25);
  margin-bottom: 45px;
}

.cover-logo-box img {
  height: 95px;
  display: block;
}

.cover-title {
  font-family: 'Outfit', sans-serif;
  font-size: 52px;
  font-weight: 800;
  letter-spacing: -1px;
  color: #ffffff;
  margin-bottom: 22px;
  text-transform: uppercase;
}

.cover-sub {
  font-family: 'Outfit', sans-serif;
  font-size: 28px;
  font-weight: 600;
  color: var(--coral);
  margin-bottom: 20px;
  max-width: 1200px;
  line-height: 1.35;
}

.cover-meta {
  font-family: 'Calibri', sans-serif;
  font-size: 20px;
  color: #d2e4d6;
  letter-spacing: 0.5px;
}

.cover-footer {
  height: 80px;
  background-color: var(--blanco);
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 80px;
  border-top: 2px solid var(--gris-claro);
}

.cover-footer-left {
  display: flex;
  align-items: center;
  gap: 20px;
}

.cover-footer-left img {
  height: 48px;
}

.cover-footer-right {
  font-size: 15px;
  color: var(--tinta);
  font-weight: 600;
}

/* CABECERA ESTÁNDAR CON PROTECCIÓN DE FONDO */
.slide-header {
  margin-bottom: 22px;
  position: relative;
  padding-bottom: 12px;
  border-bottom: 2px solid var(--menta-borde);
  display: flex;
  justify-content: space-between;
  align-items: flex-end;
  background: #FFFFFF;
  z-index: 5;
}

.header-left {
  max-width: 1250px;
}

.header-phase {
  font-family: 'Outfit', sans-serif;
  font-size: 14.5px;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 1.5px;
  color: var(--salvia);
  margin-bottom: 4px;
}

.header-title {
  font-family: 'Outfit', sans-serif;
  font-size: 31px;
  font-weight: 700;
  color: var(--pino);
  line-height: 1.2;
}

.header-right {
  display: flex;
  align-items: center;
  gap: 12px;
}

.header-right img {
  height: 32px;
}

.header-num {
  font-family: 'Outfit', sans-serif;
  font-size: 17px;
  font-weight: 700;
  color: var(--salvia);
}

/* CONTENEDORES Y TARJETAS */
.slide-body {
  flex: 1;
  display: flex;
  gap: 30px;
  position: relative;
}

.col-1-2 { flex: 1; display: flex; flex-direction: column; gap: 20px; }
.col-2-3 { flex: 2; display: flex; flex-direction: column; gap: 20px; }
.col-1-3 { flex: 1; display: flex; flex-direction: column; gap: 20px; }

.card {
  background: var(--menta);
  border: 1.5px solid var(--menta-borde);
  border-radius: 12px;
  padding: 26px 30px;
  box-shadow: var(--sombra-card);
  position: relative;
}

.card-white {
  background: var(--blanco);
  border: 1.5px solid var(--menta-borde);
  border-radius: 12px;
  padding: 26px 30px;
  box-shadow: var(--sombra-card);
}

.card-title {
  font-family: 'Outfit', sans-serif;
  font-size: 22px;
  font-weight: 700;
  color: var(--pino);
  margin-bottom: 14px;
}

.bullet-list {
  list-style: none;
  display: flex;
  flex-direction: column;
  gap: 15px;
}

.bullet-item {
  font-size: 18px;
  line-height: 1.55;
  color: var(--tinta);
  position: relative;
  padding-left: 22px;
}

.bullet-item::before {
  content: "•";
  position: absolute;
  left: 0;
  top: 0;
  font-size: 22px;
  color: var(--pino);
  line-height: 1;
}

.bullet-item strong {
  font-weight: 700;
  color: var(--pino);
}

/* RECORTE DE PRENSA (ESTÉTICA PERIÓDICO ECONÓMICO) */
.newspaper-card {
  background: var(--papel);
  border: 2px solid #222222;
  border-radius: 8px;
  padding: 30px 34px;
  box-shadow: 0 8px 24px rgba(0,0,0,0.08);
  display: flex;
  flex-direction: column;
  gap: 16px;
  position: relative;
}

.news-masthead {
  border-bottom: 2px solid #222222;
  padding-bottom: 8px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.news-masthead-title {
  font-family: 'Outfit', sans-serif;
  font-size: 14px;
  font-weight: 800;
  letter-spacing: 2px;
  color: var(--coral);
  text-transform: uppercase;
}

.news-masthead-date {
  font-size: 13px;
  color: #666;
  font-style: italic;
}

.news-headline {
  font-family: 'Newsreader', serif;
  font-size: 27px;
  font-weight: 600;
  line-height: 1.25;
  color: #111111;
  letter-spacing: -0.3px;
}

.news-columns {
  display: flex;
  gap: 25px;
  margin-top: 8px;
}

.news-col {
  flex: 1;
  font-size: 16px;
  line-height: 1.6;
  color: #222;
  text-align: justify;
}

.news-lead-quote {
  font-style: italic;
  font-weight: 600;
  color: var(--pino);
  border-left: 3px solid var(--coral);
  padding-left: 12px;
  margin-bottom: 12px;
}

/* FRAGMENTOS Y BEATS */
.frag {
  opacity: 0;
  transform: translateY(10px);
  transition: opacity 0.35s ease, transform 0.35s ease;
}

.frag.visible {
  opacity: 1;
  transform: translateY(0);
}

/* SONDEO INTERACTIVO */
.quiz-box {
  display: flex;
  flex-direction: column;
  gap: 16px;
  margin-top: 20px;
}

.quiz-opt {
  background: var(--blanco);
  border: 2px solid var(--menta-borde);
  border-radius: 10px;
  padding: 18px 24px;
  font-size: 18px;
  line-height: 1.5;
  cursor: pointer;
  transition: all 0.25s ease;
  position: relative;
}

.quiz-opt:hover {
  border-color: var(--salvia);
  transform: translateX(4px);
}

.quiz-opt.revealed-right {
  background: #E8F5E9 !important;
  border-color: #2E7D32 !important;
  color: #1B5E20 !important;
  font-weight: 700;
}

.quiz-opt.revealed-wrong {
  background: #FFEBEE !important;
  border-color: #C62828 !important;
  color: #B71C1C !important;
  opacity: 0.65;
}

/* TEMPORIZADOR PARA RETOS */
.timer-container {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 18px;
  background: var(--pino);
  color: #fff;
  padding: 16px 28px;
  border-radius: 12px;
  margin-top: 25px;
}

.timer-digits {
  font-family: 'Outfit', monospace;
  font-size: 38px;
  font-weight: 700;
  color: var(--coral);
  min-width: 110px;
  text-align: center;
}

.timer-btn {
  background: var(--coral);
  border: none;
  color: #fff;
  font-family: 'Outfit', sans-serif;
  font-size: 15px;
  font-weight: 700;
  padding: 10px 20px;
  border-radius: 8px;
  cursor: pointer;
  transition: background 0.2s;
}

.timer-btn:hover { background: #d97858; }

/* CAJA DE CÓDIGO QR MAXIMIZADA */
.qr-card-large {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  text-align: center;
  padding: 30px 24px;
  height: 100%;
}

.qr-card-large img {
  width: 310px;
  height: 310px;
  border-radius: 12px;
  border: 1.5px solid var(--gris-claro);
  margin-bottom: 18px;
  box-shadow: 0 6px 18px rgba(0,0,0,0.06);
}

.qr-link-text {
  font-size: 14.5px;
  font-weight: 700;
  color: var(--pino);
  text-decoration: none;
  word-break: break-all;
  line-height: 1.4;
}

/* ESTILOS GRÁFICOS SVG DINÁMICOS */
.chart-container {
  width: 100%;
  height: 100%;
  position: relative;
  background: #ffffff;
  border-radius: 12px;
  border: 1.5px solid var(--menta-borde);
  padding: 18px 24px;
  box-shadow: var(--sombra-card);
  display: flex;
  flex-direction: column;
}

.chart-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 10px;
}

.chart-legend {
  display: flex;
  gap: 22px;
  font-size: 14px;
  font-weight: 700;
}

.legend-item {
  display: flex;
  align-items: center;
  gap: 8px;
}

.legend-dot {
  width: 14px;
  height: 14px;
  border-radius: 3px;
}

.svg-chart {
  width: 100%;
  height: 100%;
  overflow: visible;
}

.axis-line { stroke: #D0DDD4; stroke-width: 1.5; }
.grid-line { stroke: #EEF4F0; stroke-width: 1; stroke-dasharray: 4 4; }
.axis-label { font-family: 'Calibri', sans-serif; font-size: 13.5px; fill: #617366; }
.chart-curve { fill: none; stroke-linecap: round; stroke-linejoin: round; }

/* BARRA DE PROGRESO Y CONTROLES INFERIORES */
#progress-bar {
  position: absolute;
  bottom: 0;
  left: 0;
  height: 5px;
  background: var(--coral);
  width: 0%;
  transition: width 0.3s ease;
  z-index: 10;
}

#hud {
  position: absolute;
  bottom: 12px;
  right: 25px;
  font-family: 'Outfit', sans-serif;
  font-size: 13px;
  font-weight: 600;
  color: var(--salvia);
  z-index: 10;
  display: flex;
  gap: 15px;
}

#notes-pane {
  position: fixed;
  bottom: 20px;
  left: 50%;
  transform: translateX(-50%);
  background: rgba(17, 57, 39, 0.95);
  color: #fff;
  padding: 18px 26px;
  border-radius: 12px;
  max-width: 850px;
  box-shadow: 0 10px 30px rgba(0,0,0,0.5);
  font-size: 16px;
  line-height: 1.5;
  display: none;
  z-index: 100;
}

#notes-pane.visible { display: block; }
</style>
</head>
<body>

<div id="stage">

  <!-- MARCA DE AGUA VECTORIAL FIJA (ANILLOS ENTRELAZADOS PSLL + ONDA CORAL) -->
  <div class="watermark-layer">
    <svg viewBox="0 0 400 400" fill="none" xmlns="http://www.w3.org/2000/svg">
      <circle cx="160" cy="200" r="100" stroke="#113927" stroke-width="26" stroke-linecap="round"/>
      <circle cx="240" cy="200" r="100" stroke="#76927A" stroke-width="26" stroke-linecap="round"/>
      <path d="M 70 240 C 130 140, 270 260, 330 160" stroke="#E98F71" stroke-width="16" stroke-linecap="round"/>
    </svg>
  </div>

  <!-- ===================================================================== -->
  <!-- SLIDE 1: PORTADA OFICIAL PSLL -->
  <!-- ===================================================================== -->
  <div class="slide slide-cover active" data-notes="Bienvenida a la Sesión 12 de Políticas Sociolaborales y de Empleo. Hoy abordamos el impacto estructural de la protección del empleo (EPL), la dualidad del mercado español y la Reforma Laboral de 2021.">
    <div class="cover-body">
      <div class="cover-logo-box">
        <img src="../../../Logos y skills/logo_psll_upo.png" alt="Logo PSLL UPO">
      </div>
      <h1 class="cover-title">Políticas Sociolaborales y de Empleo</h1>
      <h2 class="cover-sub">Sesión 12 – Flexibilidad Externa, Protección del Empleo (EPL) y Dualidad</h2>
      <p class="cover-meta">Semana 9 · Tema 4 (I) · Código 102023 · Manuel A. Hidalgo Pérez</p>
      <p class="cover-meta" style="font-size: 17px; margin-top: 6px; color: #a9cdb2;">Grado en Relaciones Laborales y Recursos Humanos · Doble Grado en Derecho y RRLL-RRHH · Universidad Pablo de Olavide</p>
    </div>
    <div class="cover-footer">
      <div class="cover-footer-left">
        <img src="../../../Logos y skills/psll-presentaciones-skill/assets/upo_logo.jpg" alt="Escudo UPO">
        <span style="font-size: 14px; font-weight: 700; color: #0B1C36;">UNIVERSIDAD PABLO DE OLAVIDE</span>
      </div>
      <div class="cover-footer-right">
        Departamento de Economía, Métodos Cuantitativos e Historia Económica
      </div>
    </div>
  </div>

  <!-- ===================================================================== -->
  <!-- SLIDE 2: HOJA DE RUTA EN 5 FASES -->
  <!-- ===================================================================== -->
  <div class="slide" data-notes="Repaso de la arquitectura pedagógica de la sesión en 5 fases cronometradas (120 minutos en total).">
    <div class="slide-header">
      <div class="header-left">
        <div class="header-phase">Metodología de Aula · Curso 2026-27</div>
        <div class="header-title">Hoja de Ruta · Arquitectura en 5 Fases de la Sesión 12 (120 min)</div>
      </div>
      <div class="header-right">
        <img src="../../../Logos y skills/psll_lockup.png" alt="PSLL Lockup">
        <span class="header-num">2 / 23</span>
      </div>
    </div>
    <div class="slide-body" style="flex-direction: column; gap: 16px;">
      <div class="card frag visible" style="display: flex; gap: 24px; align-items: center; padding: 20px 28px;">
        <span style="background: var(--pino); color: #fff; font-family: 'Outfit'; font-weight: 700; font-size: 15px; padding: 8px 16px; border-radius: 6px; min-width: 165px; text-align: center;">Fase 1 · 00–20 min</span>
        <div style="font-size: 18px; line-height: 1.5;"><strong style="color: var(--pino);">Apertura con Recorte de Prensa y Sondeo:</strong> Recorte de Cinco Días / El País sobre el desplome de la temporalidad privada (12,4%), el bloqueo público (>30%) y el fijo discontinuo. Sondeo Forms y choque empírico.</div>
      </div>
      <div class="card frag" style="display: flex; gap: 24px; align-items: center; padding: 20px 28px;">
        <span style="background: var(--salvia); color: #fff; font-family: 'Outfit'; font-weight: 700; font-size: 15px; padding: 8px 16px; border-radius: 6px; min-width: 165px; text-align: center;">Fase 2 · 20–45 min</span>
        <div style="font-size: 18px; line-height: 1.5;"><strong style="color: var(--salvia);">Mini-Lección I: Flexibilidad, Dualidad y EPL:</strong> Taxonomía de Atkinson (externa vs. interna). El Triángulo de Oro de la flexiseguridad danesa frente a la dualidad española. Indicador EPL de la OCDE y brecha ΔEPL.</div>
      </div>
      <div class="card frag" style="display: flex; gap: 24px; align-items: center; padding: 20px 28px;">
        <span style="background: var(--pino); color: #fff; font-family: 'Outfit'; font-weight: 700; font-size: 15px; padding: 8px 16px; border-radius: 6px; min-width: 165px; text-align: center;">Fase 3 · 45–70 min</span>
        <div style="font-size: 18px; line-height: 1.5;"><strong style="color: var(--pino);">Mini-Lección II: Despido y RDL 32/2021:</strong> Costes de despido en España (12, 20, 33 y doble tramo 45/33 días; ERE art. 51 ET y despido nulo). La Reforma Laboral (RDL 32/2021) y el fijo discontinuo (DENO vs. EPA).</div>
      </div>
      <div class="card frag" style="display: flex; gap: 24px; align-items: center; padding: 20px 28px;">
        <span style="background: var(--coral); color: #fff; font-family: 'Outfit'; font-weight: 700; font-size: 15px; padding: 8px 16px; border-radius: 6px; min-width: 165px; text-align: center;">Fase 4 · 70–85 min</span>
        <div style="font-size: 18px; line-height: 1.5;"><strong style="color: var(--coral);">Laboratorio con Micro-App:</strong> Móviles activos (15 min): simulación de indemnizaciones de despido, brecha de dualidad ΔEPL y auditoría estadística SEPE/EPA en <code>simulador_epl_dualidad.html</code>.</div>
      </div>
      <div class="card frag" style="display: flex; gap: 24px; align-items: center; padding: 20px 28px;">
        <span style="background: var(--pino); color: #fff; font-family: 'Outfit'; font-weight: 700; font-size: 15px; padding: 8px 16px; border-radius: 6px; min-width: 165px; text-align: center;">Fase 5 · 85–120 min</span>
        <div style="font-size: 18px; line-height: 1.5;"><strong style="color: var(--pino);">Reto Manuscrito y Evaluación:</strong> Síntesis en pizarra (10 min), reto individual en papel sin pantallas (10 min) con subida mediante QR a Forms y feedback formativo inmediato con rúbrica (0–1.000 pts).</div>
      </div>
    </div>
  </div>

  <!-- ===================================================================== -->
  <!-- SLIDE 3: RECORTE DE PRENSA FUNDAMENTAL -->
  <!-- ===================================================================== -->
  <div class="slide" data-notes="Recorte de prensa fundamental: Los 3 grandes titulares y dilemas del mercado laboral español tras la Reforma de 2021.">
    <div class="slide-header">
      <div class="header-left">
        <div class="header-phase">Fase 1 (00–20 min) · Apertura y Recorte de Prensa Disparador</div>
        <div class="header-title">El Debate Público: «El milagro de los indefinidos y el enigma del fijo discontinuo»</div>
      </div>
      <div class="header-right">
        <img src="../../../Logos y skills/psll_lockup.png" alt="PSLL Lockup">
        <span class="header-num">3 / 23</span>
      </div>
    </div>
    <div class="slide-body">
      <div class="col-2-3">
        <div class="newspaper-card">
          <div class="news-masthead">
            <span class="news-masthead-title">📰 Cinco Días / El País Economía · Análisis de Coyuntura</span>
            <span class="news-masthead-date">Edición Mercado de Trabajo</span>
          </div>
          <div class="news-headline">
            «La temporalidad privada cae al mínimo histórico del 12,4% tras el RDL 32/2021, pero el sector público supera el 30% y los fijos discontinuos abren la batalla estadística»
          </div>
          <div class="news-columns">
            <div class="news-col">
              <div class="news-lead-quote">"España ha dejado de ser el campeón europeo del empleo temporal en el sector privado, pero la rigidez se atrinchera en la Administración pública."</div>
              <p><strong>1. El vuelco histórico:</strong> La supresión del contrato por obra o servicio elevó la cuota de nuevos indefinidos del 10% tradicional a más del 44%, situando la tasa de asalariados temporales privados en el 12,4%, por debajo de la media europea (13,5%).</p>
            </div>
            <div class="news-col">
              <p><strong>2. La paradoja del Estado empleador:</strong> Mientras Trabajo sanciona a empresas privadas por encadenar contratos, los servicios de salud y educación pública rozan el 31% de interinidad.</p>
              <p style="margin-top: 12px;"><strong>3. El limbo estadístico:</strong> El contrato fijo discontinuo se multiplicó por diez. En inactividad cobran desempleo, pero en el SEPE no computan como Paro Registrado.</p>
            </div>
          </div>
        </div>
      </div>
      <div class="col-1-3">
        <div class="card" style="height: 100%; border-left: 5px solid var(--coral); padding: 30px;">
          <div class="card-title" style="color: var(--coral); font-size: 24px; margin-bottom: 20px;">❓ Dilemas para el Aula</div>
          <ul class="bullet-list" style="gap: 20px;">
            <li class="bullet-item frag visible"><strong>1.</strong> ¿Por qué durante 35 años (1984–2021) el 90% de los contratos mensuales en España fueron temporales?</li>
            <li class="bullet-item frag"><strong>2.</strong> ¿Hemos acabado realmente con la precariedad o una parte se ha reclasificado como fijos discontinuos e indefinidos de corta duración?</li>
            <li class="bullet-item frag"><strong>3.</strong> ¿Dónde figura estadísticamente una camarera de hotel en invierno?</li>
          </ul>
        </div>
      </div>
    </div>
  </div>

  <!-- ===================================================================== -->
  <!-- SLIDE 4: LOS DOS ENIGMAS -->
  <!-- ===================================================================== -->
  <div class="slide" data-notes="Planteamiento de los dos enigmas teóricos y jurídicos que resolveremos en las dos mini-lecciones.">
    <div class="slide-header">
      <div class="header-left">
        <div class="header-phase">Fase 1 (00–20 min) · Planteamiento del Enigma Económico y Jurídico</div>
        <div class="header-title">¿Por Qué España Fue la Campeona Europea de la Temporalidad y Qué Ha Cambiado?</div>
      </div>
      <div class="header-right">
        <img src="../../../Logos y skills/psll_lockup.png" alt="PSLL Lockup">
        <span class="header-num">4 / 23</span>
      </div>
    </div>
    <div class="slide-body">
      <div class="col-1-2">
        <div class="card frag visible" style="height: 100%; padding: 32px 36px;">
          <div class="card-title" style="color: var(--pino); font-size: 24px;">🧩 Enigma 1 · El Abismo de la Dualidad (ΔEPL)</div>
          <p style="font-size: 18px; line-height: 1.6; margin-bottom: 16px;">Imagina que diriges el departamento de Recursos Humanos de una empresa:</p>
          <ul class="bullet-list" style="gap: 16px;">
            <li class="bullet-item">Extinguir un <strong>contrato temporal</strong> al vencer cuesta <strong>12 días</strong> de salario por año y tiene <strong>cero litigiosidad judicial</strong>.</li>
            <li class="bullet-item">Despedir a un <strong>trabajador indefinido</strong> cuya causa económica sea rechazada por el juez (improcedente) cuesta <strong>33 días/año</strong> (o 45 días pre-2012).</li>
            <li class="bullet-item">Además, existía el contrato de obra o servicio para cualquier tarea rutinaria.</li>
          </ul>
          <div style="background: var(--blanco); border-left: 5px solid var(--pino); padding: 18px 22px; border-radius: 8px; margin-top: 25px; font-size: 17px; line-height: 1.5;">
            <strong>Veredicto Empresarial Racional:</strong> Se usa a los temporales como colchón flexible de choque y se les despide antes de que adquieran derechos indefinidos.
          </div>
        </div>
      </div>
      <div class="col-1-2">
        <div class="card frag" style="height: 100%; padding: 32px 36px;">
          <div class="card-title" style="color: var(--coral); font-size: 24px;">🔍 Enigma 2 · El Misterio del Fijo Discontinuo</div>
          <p style="font-size: 18px; line-height: 1.6; margin-bottom: 16px;">Una trabajadora con contrato fijo discontinuo en un hotel de la Costa del Sol finaliza su temporada el 31 de octubre:</p>
          <ul class="bullet-list" style="gap: 16px;">
            <li class="bullet-item">Durante noviembre, diciembre, enero y febrero <strong>no trabaja ni cobra salario</strong> de la empresa.</li>
            <li class="bullet-item">Acude al SEPE y cobra su <strong>prestación contributiva por desempleo</strong>.</li>
            <li class="bullet-item">Sin embargo, su contrato no se ha extinguido: <strong>sigue vigente pero suspendido</strong> a la espera del llamamiento de marzo.</li>
          </ul>
          <div style="background: var(--blanco); border-left: 5px solid var(--coral); padding: 18px 22px; border-radius: 8px; margin-top: 25px; font-size: 17px; line-height: 1.5;">
            <strong>Pregunta Clave:</strong> ¿Cuenta esta trabajadora como parada en la cifra oficial de Paro Registrado del SEPE? ¿Y cómo la clasifica la EPA del INE?
          </div>
        </div>
      </div>
    </div>
  </div>

  <!-- ===================================================================== -->
  <!-- SLIDE 5: SONDEO DE AULA EN DIRECTO (SIN PISTAS PREVIAS) -->
  <!-- ===================================================================== -->
  <div class="slide" data-notes="Sondeo previo anónimo: Los alumnos votan en el móvil escaneando el código QR. ¡Ninguna opción delata de antemano cuál es la correcta! Solo al pulsar o hacer clic sobre las opciones se desvela la respuesta.">
    <div class="slide-header">
      <div class="header-left">
        <div class="header-phase">Fase 1 (00–20 min) · Participación en Directo (Móviles Activos)</div>
        <div class="header-title">Sondeo de Aula: ¿Cómo Cuenta un Fijo Discontinuo en Periodo de Inactividad?</div>
      </div>
      <div class="header-right">
        <img src="../../../Logos y skills/psll_lockup.png" alt="PSLL Lockup">
        <span class="header-num">5 / 23</span>
      </div>
    </div>
    <div class="slide-body">
      <div class="col-2-3">
        <div class="card-white" style="height: 100%; padding: 32px 36px;">
          <p style="font-size: 21px; font-weight: 700; color: var(--pino); line-height: 1.4; margin-bottom: 12px;">
            Pregunta del Sondeo Previo (1 minuto):
          </p>
          <p style="font-size: 18px; color: var(--tinta); margin-bottom: 24px; line-height: 1.5;">
            Cuando un trabajador fijo discontinuo finaliza su campaña anual, pasa a inactividad sin sueldo y cobra el paro en el SEPE, ¿cómo se contabiliza en las estadísticas oficiales?
          </p>
          <div class="quiz-box">
            <div class="quiz-opt" data-opt="A">
              <strong>[Opción A]</strong> Suma como un parado más tanto en el Paro Registrado del SEPE como en la Encuesta de Población Activa (EPA).
            </div>
            <div class="quiz-opt" data-opt="B">
              <strong>[Opción B]</strong> NO cuenta como Paro Registrado en el SEPE (figura como Demandante No Ocupado - DENO), pero SÍ cuenta como parado en la EPA si busca activamente otro empleo.
            </div>
            <div class="quiz-opt" data-opt="C">
              <strong>[Opción C]</strong> Sigue contando como ocupado en activo en la EPA durante los meses que está en su casa porque su contrato formal es indefinido.
            </div>
          </div>
          <div style="margin-top: 28px; font-size: 14px; color: #888; font-style: italic;">
            * El profesor puede hacer clic en las opciones para desvelar la solución explicada en el aula tras la votación.
          </div>
        </div>
      </div>
      <div class="col-1-3">
        <div class="card qr-card-large">
          <div class="card-title" style="color: var(--pino); font-size: 24px; margin-bottom: 6px;">¡Escanea y Vota!</div>
          <div style="font-size: 16px; color: var(--salvia); margin-bottom: 20px;">Microsoft Forms UPO (Votación en vivo)</div>
          <img src="qr_sondeo_final.png" alt="QR Sondeo Sesión 12">
          <a class="qr-link-text" href="https://forms.office.com/e/PSLL-Sondeo-Sesion12" target="_blank">forms.office.com/e/PSLL-Sondeo-Sesion12</a>
          <span style="font-size: 13px; color: #888; margin-top: 10px;">Dispositivos autorizados para sondeo</span>
        </div>
      </div>
    </div>
  </div>

  <!-- ===================================================================== -->
  <!-- SLIDE 6: CHOQUE EMPÍRICO · GRÁFICO SVG HIPER-DINÁMICO (FIGURA 4.3) -->
  <!-- ===================================================================== -->
  <div class="slide" data-anim="figura43" data-notes="Choque empírico hiper-dinámico: Observad cómo las curvas se trazan en vivo. El desplome de la curva coral (Sector Privado) tras la zona sombreada del RDL 32/2021 frente a la rigidez estancada de la curva salvia (Sector Público). Las 4 barras de la derecha muestran el impacto contrastado por Fedea y Banco de España.">
    <div class="slide-header">
      <div class="header-left">
        <div class="header-phase">Fase 1 (00–20 min) · Choque Empírico con Datos Oficiales (EPA / INE)</div>
        <div class="header-title">Figura 4.3 · El Desplome de la Temporalidad Privada (12,4%) frente al Sector Público (>30%)</div>
      </div>
      <div class="header-right">
        <img src="../../../Logos y skills/psll_lockup.png" alt="PSLL Lockup">
        <span class="header-num">6 / 23</span>
      </div>
    </div>
    <div class="slide-body" style="flex-direction: column; gap: 14px;">
      <div class="chart-container" style="height: 520px;">
        <div class="chart-header">
          <span style="font-family: 'Outfit'; font-weight: 700; font-size: 16px; color: var(--pino);">PANEL A: Serie Temporal de la Tasa de Temporalidad (1990–2025)</span>
          <div class="chart-legend">
            <div class="legend-item"><div class="legend-dot" style="background: var(--pino);"></div> Total Asalariados (EPA)</div>
            <div class="legend-item"><div class="legend-dot" style="background: var(--coral);"></div> Sector Privado (12,4%)</div>
            <div class="legend-item"><div class="legend-dot" style="background: var(--salvia);"></div> Sector Público (31,2%)</div>
            <div class="legend-item"><div class="legend-dot" style="background: #999; border-top: 2px dashed #999; height: 0;"></div> Media UE-27 (13,5%)</div>
          </div>
        </div>
        <svg id="svg-fig43" class="svg-chart" viewBox="0 0 1440 440"></svg>
      </div>
      <div class="card" style="padding: 16px 28px;">
        <div style="display: flex; gap: 35px; font-size: 16px; line-height: 1.45;">
          <div class="frag visible"><strong style="color: var(--coral);">1. Convergencia privada histórica:</strong> Tras el RDL 32/2021, la temporalidad en el sector privado cayó del 29,2% (2018) al 12,4% (2024–2025), situando la tasa agregada en el 15,8% (mínimo desde 1987).</div>
          <div class="frag"><strong style="color: var(--salvia);">2. La anomalía del sector público:</strong> Las Administraciones Públicas mantienen un 31,2% de temporalidad (sanidad, educación y administración local) por la lentitud en estabilizar plazas interinas (Ley 20/2021).</div>
          <div class="frag"><strong style="color: var(--pino);">3. Sustitución de modalidades:</strong> La eliminación del contrato de obra o servicio trasladó el flujo de entrada hacia indefinidos ordinarios y fijos discontinuos.</div>
        </div>
      </div>
    </div>
  </div>

  <!-- ===================================================================== -->
  <!-- SLIDE 7: DIAGRAMA SVG DE FLUJOS ESTADÍSTICOS (REDISEÑADO SIN SOLAPES) -->
  <!-- ===================================================================== -->
  <div class="slide" data-anim="flujoSepeEpa" data-notes="Diagrama de flujo interactivo sin solapes: Dos ramas horizontales limpias. Arriba: Campaña activa. Abajo: Inactividad y bifurcación nítida SEPE vs EPA.">
    <div class="slide-header">
      <div class="header-left">
        <div class="header-phase">Fase 1 (00–20 min) · Resolución del Enigma Estadístico</div>
        <div class="header-title">¿Dónde Están los Fijos Discontinuos Inactivos? Registro SEPE (DENO) vs. EPA (INE)</div>
      </div>
      <div class="header-right">
        <img src="../../../Logos y skills/psll_lockup.png" alt="PSLL Lockup">
        <span class="header-num">7 / 23</span>
      </div>
    </div>
    <div class="slide-body" style="flex-direction: column; gap: 14px;">
      <div class="chart-container" style="height: 520px; padding: 22px;">
        <svg id="svg-flujo" class="svg-chart" viewBox="0 0 1440 450"></svg>
      </div>
      <div class="card" style="padding: 16px 28px;">
        <div style="display: flex; gap: 35px; font-size: 16px; line-height: 1.45;">
          <div><strong style="color: var(--pino);">Actividad en Campaña:</strong> Alta en TGSS y clasificado como Ocupado en la EPA. Plena coincidencia.</div>
          <div><strong style="color: var(--coral);">Inactividad en SEPE:</strong> Contrato suspendido &rarr; Clasificado como DENO &rarr; Excluido del Paro Registrado por Orden de 1985.</div>
          <div><strong style="color: var(--salvia);">Inactividad en EPA:</strong> Jamás es ocupado. Se clasifica con rigor OIT: Parado si busca activamente, o Inactivo si espera en casa.</div>
        </div>
      </div>
    </div>
  </div>

  <!-- ===================================================================== -->
  <!-- SLIDE 8: TAXONOMÍA DE ATKINSON (FUENTES Y ESPACIOS AMPLIADOS) -->
  <!-- ===================================================================== -->
  <div class="slide" data-notes="Mini-lección teórica I: Comenzamos con la taxonomía de flexibilidad de Atkinson. Flexibilidad externa (ajuste vía número de cabezas) vs. flexibilidad interna (ajuste vía horas, salarios o funciones sin destruir el empleo).">
    <div class="slide-header">
      <div class="header-left">
        <div class="header-phase">Fase 2 (20–45 min) · Mini-Lección Quirúrgica I (Sin Pantallas · Solo Papel)</div>
        <div class="header-title">Epígrafe 4.1 · ¿A Qué Llamamos Flexibilidad Laboral? La Taxonomía de Atkinson</div>
      </div>
      <div class="header-right">
        <img src="../../../Logos y skills/psll_lockup.png" alt="PSLL Lockup">
        <span class="header-num">8 / 23</span>
      </div>
    </div>
    <div class="slide-body">
      <div class="col-1-2">
        <div class="card frag visible" style="height: 100%; padding: 34px 38px;">
          <div class="card-title" style="color: var(--coral); font-size: 25px; margin-bottom: 18px;">1. Flexibilidad Externa (Ajuste vía Empleo · N)</div>
          <p style="font-size: 18.5px; line-height: 1.6; margin-bottom: 20px;">Capacidad de la empresa para adaptar el volumen de su plantilla (N) contratando en expansión o extinguiendo contratos en recesión.</p>
          <ul class="bullet-list" style="gap: 18px;">
            <li class="bullet-item"><strong>A. Entrada:</strong> Regulación de modalidades (indefinidos, temporales causales, fijos discontinuos, formativos) y Empresas de Trabajo Temporal (ETT).</li>
            <li class="bullet-item"><strong>B. Salida:</strong> Costes indemnizatorios, requisitos causales, plazos de preaviso y control judicial (despido objetivo, improcedente y ERE).</li>
            <li class="bullet-item" style="color: var(--coral); margin-top: 10px;"><strong>Riesgo macro:</strong> Si toda la flexibilidad descansa en la vía externa, la destrucción de empleo en cada crisis es masiva (patrón histórico español).</li>
          </ul>
        </div>
      </div>
      <div class="col-1-2">
        <div class="card frag" style="height: 100%; padding: 34px 38px;">
          <div class="card-title" style="color: var(--pino); font-size: 25px; margin-bottom: 18px;">2. Flexibilidad Interna (Ajuste sin Destruir Empleo)</div>
          <p style="font-size: 18.5px; line-height: 1.6; margin-bottom: 20px;">Capacidad de reorganizar el trabajo dentro de la empresa manteniendo intacto el vínculo contractual y el capital humano específico.</p>
          <ul class="bullet-list" style="gap: 18px;">
            <li class="bullet-item"><strong>A. Cuantitativa (Horas · H):</strong> Distribución irregular de jornada (hasta 10% anual, art. 34.2 ET), horas extras, ERTE (art. 47 ET) y Mecanismo RED (art. 47 bis ET).</li>
            <li class="bullet-item"><strong>B. Funcional (Tareas):</strong> Movilidad funcional dentro de grupos profesionales (art. 39 ET), polivalencia y teletrabajo.</li>
            <li class="bullet-item"><strong>C. Salarial (Costes):</strong> Retribución variable ligada a resultados y cláusulas de descuelgue salarial (art. 82.3 ET).</li>
          </ul>
        </div>
      </div>
    </div>
  </div>

  <!-- ===================================================================== -->
  <!-- SLIDE 9: DIAGRAMA SVG HIPER-DINÁMICO · TRIÁNGULO DE ORO VS DUALIDAD -->
  <!-- ===================================================================== -->
  <div class="slide" data-anim="figura41" data-notes="Comparativa interactiva de los dos modelos: A la izquierda, el Triángulo de Oro Danés con flujos circulares continuos entre empleo, seguro generoso y formación activa. A la derecha, el Muro de la Dualidad español que separa insiders protegidos de outsiders precarios.">
    <div class="slide-header">
      <div class="header-left">
        <div class="header-phase">Fase 2 (20–45 min) · Dos Modelos Institucionales Opuestos en Europa</div>
        <div class="header-title">Figura 4.1 · El Triángulo de Oro de la Flexiseguridad Danesa vs. la Dualidad Española</div>
      </div>
      <div class="header-right">
        <img src="../../../Logos y skills/psll_lockup.png" alt="PSLL Lockup">
        <span class="header-num">9 / 23</span>
      </div>
    </div>
    <div class="slide-body" style="flex-direction: column; gap: 14px;">
      <div class="chart-container" style="height: 520px; padding: 20px;">
        <svg id="svg-fig41" class="svg-chart" viewBox="0 0 1440 450"></svg>
      </div>
      <div class="card" style="padding: 16px 28px;">
        <div style="display: flex; gap: 35px; font-size: 16px; line-height: 1.45;">
          <div><strong style="color: var(--pino);">Triángulo Danés:</strong> Protege la renta y la empleabilidad de la persona en la transición laboral, en lugar de blindar rígidamente el puesto específico.</div>
          <div><strong style="color: var(--coral);">Dualidad Española:</strong> Para amortiguar el elevado coste del despido indefinido, se liberalizó el contrato temporal, creando dos castas laborales excluyentes.</div>
        </div>
      </div>
    </div>
  </div>

  <!-- ===================================================================== -->
  <!-- SLIDE 10: EPL Y BRECHA REGULATORIA (OCDE · FUENTES AMPLIADAS) -->
  <!-- ===================================================================== -->
  <div class="slide" data-notes="Definición formal del indicador de Legislación de Protección del Empleo (EPL) de la OCDE y la ecuación de la brecha regulatoria Delta EPL.">
    <div class="slide-header">
      <div class="header-left">
        <div class="header-phase">Fase 2 (20–45 min) · Medición Comparada de la Rigidez Normativa</div>
        <div class="header-title">Epígrafe 4.2.1 · La Legislación de Protección del Empleo (EPL) y la Brecha Regulatoria</div>
      </div>
      <div class="header-right">
        <img src="../../../Logos y skills/psll_lockup.png" alt="PSLL Lockup">
        <span class="header-num">10 / 23</span>
      </div>
    </div>
    <div class="slide-body" style="flex-direction: column; gap: 24px;">
      <div class="card" style="background: var(--pino); color: #fff; text-align: center; padding: 28px 20px; border-radius: 14px;">
        <div style="font-family: 'Outfit'; font-size: 17px; text-transform: uppercase; letter-spacing: 2px; color: var(--coral); margin-bottom: 8px;">Ecuación Fundamental de la Dualidad Laboral (OCDE)</div>
        <div style="font-family: 'Outfit'; font-size: 38px; font-weight: 700; color: #fff; letter-spacing: 0.5px;">
          ΔEPL = EPL<sub>indefinidos</sub> − Coste Efectivo de Salida Temporal (EPL<sub>temporal</sub>)
        </div>
      </div>
      <div style="display: flex; gap: 28px; flex: 1;">
        <div class="card-white frag visible" style="flex: 1; padding: 32px 30px;">
          <div class="card-title" style="color: var(--pino); font-size: 23px; margin-bottom: 16px;">Pilar 1 · Despido Individual</div>
          <p style="font-size: 18px; line-height: 1.6; color: var(--tinta);">Mide en escala de 0 a 6: preaviso, cuantía indemnizatoria según antigüedad, definición legal de causa justa y probabilidad de readmisión forzosa.</p>
        </div>
        <div class="card-white frag" style="flex: 1; padding: 32px 30px;">
          <div class="card-title" style="color: var(--salvia); font-size: 23px; margin-bottom: 16px;">Pilar 2 · Despidos Colectivos (ERE)</div>
          <p style="font-size: 18px; line-height: 1.6; color: var(--tinta);">Requisitos adicionales cuando se superan umbrales numéricos de despido masivo: periodos de consulta sindical, planes de recolocación e intervención administrativa.</p>
        </div>
        <div class="card-white frag" style="flex: 1; padding: 32px 30px;">
          <div class="card-title" style="color: var(--coral); font-size: 23px; margin-bottom: 16px;">Pilar 3 · Regulación Temporal</div>
          <p style="font-size: 18px; line-height: 1.6; color: var(--tinta);">Condiciones causales, duración máxima y coste de fin de contrato. Cuando ΔEPL es elevado, la empresa rota temporales sistemáticamente (efecto umbral).</p>
        </div>
      </div>
    </div>
  </div>

  <!-- ===================================================================== -->
  <!-- SLIDE 11: GRÁFICO SVG HIPER-DINÁMICO · EPL COMPARADO EN LA OCDE -->
  <!-- ===================================================================== -->
  <div class="slide" data-anim="figura42" data-notes="Evidencia empírica en países de la OCDE: Observad el crecimiento progresivo de las barras con tween. En España, tras el RDL 32/2021, la barra coral de temporales salta de 1,9 a 2,67, eliminando el atajo de la contratación temporal.">
    <div class="slide-header">
      <div class="header-left">
        <div class="header-phase">Fase 2 (20–45 min) · Evidencia Comparada en la OCDE</div>
        <div class="header-title">Figura 4.2 · Rigidez de Protección del Empleo (EPL) en Indefinidos vs. Temporales</div>
      </div>
      <div class="header-right">
        <img src="../../../Logos y skills/psll_lockup.png" alt="PSLL Lockup">
        <span class="header-num">11 / 23</span>
      </div>
    </div>
    <div class="slide-body" style="flex-direction: column; gap: 14px;">
      <div class="chart-container" style="height: 520px;">
        <div class="chart-header">
          <span style="font-family: 'Outfit'; font-weight: 700; font-size: 16px; color: var(--pino);">Indicador EPL de la OCDE (Escala 0 a 6: Mayor valor = Mayor rigidez regulatoria)</span>
          <div class="chart-legend">
            <div class="legend-item"><div class="legend-dot" style="background: var(--pino);"></div> EPL Indefinidos Individuales (EPR)</div>
            <div class="legend-item"><div class="legend-dot" style="background: var(--coral);"></div> EPL Contratos Temporales (EPT)</div>
          </div>
        </div>
        <svg id="svg-fig42" class="svg-chart" viewBox="0 0 1440 440"></svg>
      </div>
      <div class="card" style="padding: 16px 28px;">
        <div style="display: flex; gap: 35px; font-size: 16px; line-height: 1.45;">
          <div class="frag visible"><strong style="color: var(--pino);">1. Modelo Anglosajón (EE.UU. 0,09 · R. Unido 1,35):</strong> Doctrina del <em>employment-at-will</em>: mínima protección tanto en fijos como temporales, alta movilidad y corta duración del desempleo.</div>
          <div class="frag"><strong style="color: var(--salvia);">2. Flexiseguridad Nórdica (Dinamarca 1,53):</strong> Baja rigidez en indefinidos (1,53) combinada con generosa protección por desempleo y Políticas Activas de Empleo (PAE).</div>
          <div class="frag"><strong style="color: var(--coral);">3. Modelo Continental y Mediterráneo (España 2,00 en fijos / 2,67 en temporales):</strong> Alta protección legal en indefinidos y restricción drástica de temporales tras el RDL 32/2021.</div>
        </div>
      </div>
    </div>
  </div>

  <!-- ===================================================================== -->
  <!-- SLIDE 12: TIPOLOGÍA Y COSTES DE EXTINCIÓN EN ESPAÑA (EQUILIBRADA Y LLENA) -->
  <!-- ===================================================================== -->
  <div class="slide" data-notes="Mini-lección analítica II: El marco legal del despido en el Estatuto de los Trabajadores. Los cuatro tipos de extinción contractual y sus indemnizaciones tasadas.">
    <div class="slide-header">
      <div class="header-left">
        <div class="header-phase">Fase 3 (45–70 min) · Mini-Lección Quirúrgica II (Marco Jurídico-Económico)</div>
        <div class="header-title">Epígrafe 4.2.2 · Tipología y Costes de Extinción del Contrato en España (ET)</div>
      </div>
      <div class="header-right">
        <img src="../../../Logos y skills/psll_lockup.png" alt="PSLL Lockup">
        <span class="header-num">12 / 23</span>
      </div>
    </div>
    <div class="slide-body" style="flex-direction: column; gap: 18px;">
      <div class="card frag visible" style="border-left: 6px solid var(--salvia); padding: 22px 30px;">
        <strong style="color: var(--salvia); font-size: 21px;">1. Fin de Contrato Temporal (Art. 49.1.c ET):</strong>
        <p style="font-size: 18px; margin-top: 6px; line-height: 1.55;"><strong>12 días de salario por año de servicio</strong> (prorrateo por meses). Excepción: sustitución y formativos no devengan indemnización (0 días) a su término.</p>
      </div>
      <div class="card frag" style="border-left: 6px solid var(--pino); padding: 22px 30px;">
        <strong style="color: var(--pino); font-size: 21px;">2. Despido Objetivo Procedente (Arts. 52–53 ET) y Colectivo ERE (Art. 51 ET):</strong>
        <p style="font-size: 18px; margin-top: 6px; line-height: 1.55;">Causas ETOP o ineptitud. <strong>20 días de salario por año (tope 12 mensualidades = 360 días)</strong> + 15 días de preaviso. Umbrales ERE: &ge;10 (&lt;100 trab.), &ge;10% (100–300) o &ge;30 (>300).</p>
      </div>
      <div class="card frag" style="border-left: 6px solid var(--coral); padding: 22px 30px;">
        <strong style="color: var(--coral); font-size: 21px;">3. Despido Improcedente (Art. 56 ET · RDL 3/2012 y DT 11.ª ET):</strong>
        <p style="font-size: 18px; margin-top: 6px; line-height: 1.55;">Falta de acreditación de causa legal. <strong>33 días/año (tope 24 mensualidades = 720 días)</strong> sin salarios de tramitación. Contratos pre-12/02/2012: doble tramo (45 días tramo previo + 33 días posterior).</p>
      </div>
      <div class="card frag" style="border-left: 6px solid #222; padding: 22px 30px;">
        <strong style="color: #222; font-size: 21px;">4. Despido Nulo (Art. 55.5 ET · Tutela de Derechos Fundamentales):</strong>
        <p style="font-size: 18px; margin-top: 6px; line-height: 1.55;">Móvil discriminatorio, embarazo, maternidad o fraude procesal. Efecto: <strong>readmisión forzosa inmediata</strong> + abono íntegro de salarios de tramitación.</p>
      </div>
    </div>
  </div>

  <!-- ===================================================================== -->
  <!-- SLIDE 13: GRÁFICO SVG · CURVAS DE DESPIDO Y LITIGIOSIDAD ULTRA-NÍTIDA -->
  <!-- ===================================================================== -->
  <div class="slide" data-anim="figura44" data-notes="Gráfico interactivo de costes de despido: A la izquierda, observad el trazado matemático de las curvas según la antigüedad del trabajador y la pastilla destacada de litigiosidad (+65%). A la derecha, las barras de coste efectivo en euros para un salario representativo de 2.400 €/mes.">
    <div class="slide-header">
      <div class="header-left">
        <div class="header-phase">Fase 3 (45–70 min) · Análisis Gráfico de las Curvas de Indemnización</div>
        <div class="header-title">Figura 4.4 · Indemnización Acumulada según Antigüedad y Prima de Litigiosidad</div>
      </div>
      <div class="header-right">
        <img src="../../../Logos y skills/psll_lockup.png" alt="PSLL Lockup">
        <span class="header-num">13 / 23</span>
      </div>
    </div>
    <div class="slide-body" style="flex-direction: column; gap: 14px;">
      <div class="chart-container" style="height: 520px;">
        <div class="chart-header">
          <span style="font-family: 'Outfit'; font-weight: 700; font-size: 16px; color: var(--pino);">PANEL A: Curvas de Indemnización Legal por Antigüedad (0 a 30 años)</span>
          <div class="chart-legend">
            <div class="legend-item"><div class="legend-dot" style="background: var(--coral);"></div> Improcedente (33 d · máx 24 m)</div>
            <div class="legend-item"><div class="legend-dot" style="background: var(--pino);"></div> Objetivo (20 d · máx 12 m)</div>
            <div class="legend-item"><div class="legend-dot" style="background: #999; border-top: 2px dashed #999; height: 0;"></div> Pre-2012 (45 d · máx 42 m)</div>
          </div>
        </div>
        <svg id="svg-fig44" class="svg-chart" viewBox="0 0 1440 440"></svg>
      </div>
      <div class="card" style="padding: 16px 28px;">
        <div style="display: flex; gap: 35px; font-size: 16px; line-height: 1.45;">
          <div class="frag visible"><strong style="color: var(--pino);">1. Rebaja del RDL 3/2012 · De 45 d (42 m) a 33 d (24 m):</strong> Redujo la pendiente de 1,5 a 1,1 meses/año y recortó el tope de 42 a 24 mensualidades (tope que se satura a los 21,8 años).</div>
          <div class="frag"><strong style="color: var(--coral);">2. Brecha 33 vs. 20 días · Incertidumbre Judicial:</strong> La franja sombreada mide el sobrecoste (+65%) si un juez rechaza la causa objetiva (20 d) y declara improcedente (33 d).</div>
          <div class="frag"><strong style="color: var(--salvia);">3. El Abismo Temporal · 12 días vs. 33 días:</strong> Extinguir un temporal al año cuesta 12 días (1.000 €) sin juicio. Esa asimetría explicaba el uso de temporales como colchón.</div>
        </div>
      </div>
    </div>
  </div>

  <!-- ===================================================================== -->
  <!-- SLIDE 14: CÁLCULO NUMÉRICO DE INDEMNIZACIONES (AMPLIADO Y DESTACADO) -->
  <!-- ===================================================================== -->
  <div class="slide" data-notes="Práctica cuantitativa para graduados en RRLL: Aplicación de fórmulas con un salario de 2.400 €/mes (80 €/día) y 10 años de antigüedad.">
    <div class="slide-header">
      <div class="header-left">
        <div class="header-phase">Fase 3 (45–70 min) · Práctica Cuantitativa para Graduados en RRLL</div>
        <div class="header-title">Cálculo Aplicado de Indemnizaciones: Tres Escenarios Reales (Salario = 2.400 €/mes)</div>
      </div>
      <div class="header-right">
        <img src="../../../Logos y skills/psll_lockup.png" alt="PSLL Lockup">
        <span class="header-num">14 / 23</span>
      </div>
    </div>
    <div class="slide-body">
      <div class="col-1-3">
        <div class="card frag visible" style="height: 100%; padding: 30px 28px;">
          <div style="font-size: 14px; font-weight: 700; color: var(--salvia); letter-spacing: 1px;">CASO 1 · OBJETIVO PROCEDENTE</div>
          <div class="card-title" style="color: var(--pino); font-size: 22px; margin-top: 4px;">Art. 52 ET (20 d/año · Tope 12 m)</div>
          <ul class="bullet-list" style="font-size: 17px; gap: 14px;">
            <li class="bullet-item">Salario: 2.400 €/mes &rarr; <strong>80 €/día</strong>.</li>
            <li class="bullet-item">Antigüedad: 10 años exactos.</li>
            <li class="bullet-item">Días: 10 &times; 20 = 200 días.</li>
            <li class="bullet-item">Tope: 200 &lt; 360 días (12 meses).</li>
          </ul>
          <div style="background: #FFFFFF; border: 2px solid var(--pino); border-radius: 10px; padding: 18px; margin-top: 24px; text-align: center;">
            <div style="font-size: 13px; font-weight: 700; color: var(--pino); text-transform: uppercase;">Indemnización Total</div>
            <div style="font-family: 'Outfit'; font-size: 32px; font-weight: 800; color: var(--pino); margin-top: 4px;">16.000 €</div>
            <div style="font-size: 13.5px; color: #666; margin-top: 4px;">+ 15 días de preaviso obligatorio</div>
          </div>
        </div>
      </div>
      <div class="col-1-3">
        <div class="card frag" style="height: 100%; border-top: 5px solid var(--coral); padding: 30px 28px;">
          <div style="font-size: 14px; font-weight: 700; color: var(--coral); letter-spacing: 1px;">CASO 2 · IMPROCEDENTE VIGENTE</div>
          <div class="card-title" style="color: var(--coral); font-size: 22px; margin-top: 4px;">Art. 56 ET (33 d/año · Tope 24 m)</div>
          <ul class="bullet-list" style="font-size: 17px; gap: 14px;">
            <li class="bullet-item">Mismo empleado (10 años, 80 €/día).</li>
            <li class="bullet-item">Juez tumba causa organizativa.</li>
            <li class="bullet-item">Días: 10 &times; 33 = 330 días.</li>
            <li class="bullet-item">Tope: 330 &lt; 720 días (24 meses).</li>
          </ul>
          <div style="background: #FFFFFF; border: 2px solid var(--coral); border-radius: 10px; padding: 18px; margin-top: 24px; text-align: center;">
            <div style="font-size: 13px; font-weight: 700; color: var(--coral); text-transform: uppercase;">Indemnización Total</div>
            <div style="font-family: 'Outfit'; font-size: 32px; font-weight: 800; color: var(--coral); margin-top: 4px;">26.400 €</div>
            <div style="font-size: 14px; font-weight: 700; color: var(--coral); margin-top: 4px;">+10.400 € (+65% sobrecoste)</div>
          </div>
        </div>
      </div>
      <div class="col-1-3">
        <div class="card frag" style="height: 100%; border-top: 5px solid var(--pino); padding: 30px 28px;">
          <div style="font-size: 14px; font-weight: 700; color: var(--pino); letter-spacing: 1px;">CASO 3 · DOBLE TRAMO PRE-2012</div>
          <div class="card-title" style="color: var(--pino); font-size: 22px; margin-top: 4px;">DT 11.ª ET (45 d previo + 33 d post)</div>
          <ul class="bullet-list" style="font-size: 17px; gap: 14px;">
            <li class="bullet-item">4 años pre-2012 + 12 años post-2012.</li>
            <li class="bullet-item">Tramo 1: 4 &times; 45 = 180 días.</li>
            <li class="bullet-item">Tramo 2: 12 &times; 33 = 396 días.</li>
            <li class="bullet-item">Total días: 180 + 396 = 576 días.</li>
          </ul>
          <div style="background: #FFFFFF; border: 2px solid var(--pino); border-radius: 10px; padding: 18px; margin-top: 24px; text-align: center;">
            <div style="font-size: 13px; font-weight: 700; color: var(--pino); text-transform: uppercase;">Indemnización Total</div>
            <div style="font-family: 'Outfit'; font-size: 32px; font-weight: 800; color: var(--pino); margin-top: 4px;">46.080 €</div>
            <div style="font-size: 13.5px; color: var(--salvia); font-weight: 700; margin-top: 4px;">Protección derechos adquiridos</div>
          </div>
        </div>
      </div>
    </div>
  </div>

  <!-- ===================================================================== -->
  <!-- SLIDE 15: LOS CUATRO PILARES DEL RDL 32/2021 (AMPLIADA) -->
  <!-- ===================================================================== -->
  <div class="slide" data-notes="El nuevo marco de contratación laboral tras el RDL 32/2021: Presunción indefinida, causas estrictas del art. 15, límite al encadenamiento y penalización a microcontratos.">
    <div class="slide-header">
      <div class="header-left">
        <div class="header-phase">Fase 3 (45–70 min) · El Cambio de Paradigma en la Flexibilidad de Entrada</div>
        <div class="header-title">Epígrafe 4.2.3 · Los Cuatro Pilares de la Reforma Laboral (RDL 32/2021)</div>
      </div>
      <div class="header-right">
        <img src="../../../Logos y skills/psll_lockup.png" alt="PSLL Lockup">
        <span class="header-num">15 / 23</span>
      </div>
    </div>
    <div class="slide-body" style="flex-direction: column; gap: 18px;">
      <div class="card frag visible" style="padding: 22px 30px; border-left: 6px solid var(--pino);">
        <strong style="color: var(--pino); font-size: 21px;">1. Presunción Indefinida y Supresión de Obra o Servicio (Art. 15 ET):</strong>
        <p style="font-size: 18px; margin-top: 6px; line-height: 1.55;">El contrato de trabajo se presume por tiempo indefinido. Se deroga definitivamente el contrato por obra o servicio determinado, principal vía histórica de fraude y rotación en España desde 1984.</p>
      </div>
      <div class="card frag" style="padding: 22px 30px; border-left: 6px solid var(--salvia);">
        <strong style="color: var(--salvia); font-size: 21px;">2. Redefinición Estricta de Temporales Causales (Art. 15 ET):</strong>
        <p style="font-size: 18px; margin-top: 6px; line-height: 1.55;">Solo dos causas: a) Circunstancias de producción <strong>imprevisibles</strong> (máx. 6 meses, ampliable a 12 por convenio) y <strong>previsibles</strong> (máx. 90 días/año por empresa, no continuados); b) Sustitución de persona con reserva de puesto.</p>
      </div>
      <div class="card frag" style="padding: 22px 30px; border-left: 6px solid var(--coral);">
        <strong style="color: var(--coral); font-size: 21px;">3. Límite al Encadenamiento y Recargo a Micro-Contratos:</strong>
        <p style="font-size: 18px; margin-top: 6px; line-height: 1.55;">Pasa a fijo quien encadene <strong>&gt;18 meses en 24 meses</strong> (antes 24 en 30). Además, cada baja de contrato temporal &lt;30 días abona un <strong>recargo fijo de 31,40 €</strong> en la cotización a la Seguridad Social (art. 151 LGSS).</p>
      </div>
      <div class="card frag" style="padding: 22px 30px; border-left: 6px solid var(--pino);">
        <strong style="color: var(--pino); font-size: 21px;">4. Nuevos Contratos Formativos (Art. 11 ET):</strong>
        <p style="font-size: 18px; margin-top: 6px; line-height: 1.55;">Formación en alternancia (compatibilizar empleo y estudios, de 3 meses a 2 años) y Práctica profesional para titulados universitarios o de FP (de 6 meses a 1 año).</p>
      </div>
    </div>
  </div>

  <!-- ===================================================================== -->
  <!-- SLIDE 16: EL CONTRATO FIJO DISCONTINUO (FUENTES AMPLIADAS) -->
  <!-- ===================================================================== -->
  <div class="slide" data-notes="Análisis de la figura estrella de la Reforma: El contrato fijo discontinuo (art. 16 ET), sus avances jurídicos y el debate económico sobre la estabilidad de rentas y la opacidad en el registro del paro.">
    <div class="slide-header">
      <div class="header-left">
        <div class="header-phase">Fase 3 (45–70 min) · La Figura Estrella de la Reforma Laboral</div>
        <div class="header-title">El Contrato Fijo Discontinuo (Art. 16 ET): Naturaleza Jurídica y Derechos</div>
      </div>
      <div class="header-right">
        <img src="../../../Logos y skills/psll_lockup.png" alt="PSLL Lockup">
        <span class="header-num">16 / 23</span>
      </div>
    </div>
    <div class="slide-body">
      <div class="col-1-2">
        <div class="card frag visible" style="height: 100%; padding: 34px 38px;">
          <div class="card-title" style="color: var(--pino); font-size: 25px; margin-bottom: 20px;">¿Cuándo se Utiliza y Qué Derechos Otorga?</div>
          <ul class="bullet-list" style="gap: 18px;">
            <li class="bullet-item"><strong>Objeto legal (Art. 16.1 ET):</strong> Trabajos de naturaleza estacional (turismo, agricultura, educación), actividades intermitentes con periodos ciertos o inciertos, y contratas mercantiles o concesiones.</li>
            <li class="bullet-item"><strong>Derecho de llamamiento:</strong> Obligación empresarial de llamar al trabajador al inicio de cada campaña según orden formal fijado en convenio. La falta injustificada de llamamiento equivale a un <strong>despido improcedente (33 días)</strong>.</li>
            <li class="bullet-item"><strong>Cómputo de antigüedad (TS y TJUE):</strong> Para trienios y promoción computa todo el tiempo natural de la relación laboral (incluida la inactividad). Para la indemnización por despido computa el tiempo efectivamente trabajado.</li>
          </ul>
        </div>
      </div>
      <div class="col-1-2">
        <div class="card frag" style="height: 100%; padding: 34px 38px;">
          <div class="card-title" style="color: var(--coral); font-size: 25px; margin-bottom: 20px;">El Debate Económico: ¿Estabilidad Real o Nominal?</div>
          <ul class="bullet-list" style="gap: 18px;">
            <li class="bullet-item"><strong>Avance real en derechos:</strong> El trabajador gana estabilidad de vínculo, tutela judicial frente al despido y fin de la angustia de renovación mensual.</li>
            <li class="bullet-item"><strong>Sombra 1 · Inestabilidad de rentas:</strong> Estar indefinido no garantiza trabajar 12 meses al año ni elimina la precariedad salarial acumulada.</li>
            <li class="bullet-item"><strong>Sombra 2 · Rotación intra-indefinida:</strong> Se firman más contratos indefinidos por persona al año (mayor rotación y pluriempleo).</li>
            <li class="bullet-item"><strong>Sombra 3 · Opacidad estadística:</strong> En periodos de inactividad, los trabajadores figuran como DENO sin reflejarse en la cifra de cabecera del Paro Registrado.</li>
          </ul>
        </div>
      </div>
    </div>
  </div>

  <!-- ===================================================================== -->
  <!-- SLIDE 17: BALANCE EMPÍRICO DEL RDL 32/2021 (EQUILIBRADA) -->
  <!-- ===================================================================== -->
  <div class="slide" data-notes="Balance cuantitativo de la evidencia empírica acumulada por Banco de España, FEDEA y Funcas tras dos años de vigencia del RDL 32/2021.">
    <div class="slide-header">
      <div class="header-left">
        <div class="header-phase">Fase 3 (45–70 min) · Evaluación Empírica de la Reforma Laboral</div>
        <div class="header-title">Balance del RDL 32/2021: Tres Éxitos Estructurales y Tres Retos Pendientes</div>
      </div>
      <div class="header-right">
        <img src="../../../Logos y skills/psll_lockup.png" alt="PSLL Lockup">
        <span class="header-num">17 / 23</span>
      </div>
    </div>
    <div class="slide-body" style="flex-direction: column; gap: 20px;">
      <div class="card frag visible" style="padding: 24px 32px; border-left: 6px solid var(--pino);">
        <strong style="color: var(--pino); font-size: 21px;">ÉXITO 1 · Hundimiento de la Temporalidad Privada (29,2% &rarr; 12,4%):</strong>
        <p style="font-size: 18px; margin-top: 6px; line-height: 1.55;">España ha convergido con la media europea en el sector privado, reduciendo la brecha en 16 puntos porcentuales sin destruir empleo agregado y mejorando la certidumbre en hogares jóvenes.</p>
      </div>
      <div class="card frag" style="padding: 24px 32px; border-left: 6px solid var(--coral);">
        <strong style="color: var(--coral); font-size: 21px;">RETOS Y SOMBRAS 2 · Aumento de Bajas en Periodo de Prueba y Despidos Cortos:</strong>
        <p style="font-size: 18px; margin-top: 6px; line-height: 1.55;">Al cerrarse la válvula temporal sin tocar los costes del despido indefinido, ha aumentado la extinción en los primeros meses (no superación de periodo de prueba y despidos de muy baja antigüedad).</p>
      </div>
      <div class="card frag" style="padding: 24px 32px; border-left: 6px solid var(--salvia);">
        <strong style="color: var(--salvia); font-size: 21px;">RETOS Y SOMBRAS 3 · Enquistamiento de la Temporalidad Pública (&gt;30%):</strong>
        <p style="font-size: 18px; margin-top: 6px; line-height: 1.55;">Las Administraciones Públicas mantienen una tasa superior al 30%, exigiendo culminar los procesos de estabilización (Ley 20/2021) y reformar el acceso para cumplir la directiva europea y el TJUE.</p>
      </div>
    </div>
  </div>

  <!-- ===================================================================== -->
  <!-- SLIDE 18: LABORATORIO ACTIVO CON MICRO-APP (QR MAXIMIZADO) -->
  <!-- ===================================================================== -->
  <div class="slide" data-notes="Fase 4: Laboratorio móvil activo. Los alumnos abren simulador_epl_dualidad.html en su móvil y resuelven las tres misiones interactivas.">
    <div class="slide-header">
      <div class="header-left">
        <div class="header-phase">Fase 4 (70–85 min · 15 min) · Laboratorio Activo desde el Móvil</div>
        <div class="header-title">Taller Práctico: «Calculadora de Despido, Brecha ΔEPL y Auditoría SEPE/EPA»</div>
      </div>
      <div class="header-right">
        <img src="../../../Logos y skills/psll_lockup.png" alt="PSLL Lockup">
        <span class="header-num">18 / 23</span>
      </div>
    </div>
    <div class="slide-body">
      <div class="col-2-3">
        <div class="card-white" style="height: 100%; padding: 34px 38px;">
          <div class="card-title" style="color: var(--pino); font-size: 25px; margin-bottom: 16px;">🎯 Misión en el Simulador Móvil (3 Escenarios en 15 minutos)</div>
          <p style="font-size: 18px; margin-bottom: 22px; line-height: 1.5;">Desbloquead el teléfono móvil, escanead el código QR de la derecha y resolved las tres pestañas del simulador interactivo:</p>
          <ul class="bullet-list" style="font-size: 17.5px; gap: 18px;">
            <li class="bullet-item">
              <strong style="color: var(--pino);">Misión 1 · Calculadora de Despido (Pestaña 1):</strong> Introduce un salario de 2.400 €/mes (80 €/día) y 10 años de antigüedad. Comprueba el salto de 16.000 € (objetivo 20 d) a 26.400 € (improcedente 33 d) y simula el doble tramo pre-2012 (45/33 d).
            </li>
            <li class="bullet-item">
              <strong style="color: var(--salvia);">Misión 2 · Brecha de Dualidad ΔEPL (Pestaña 2):</strong> Pulsa el botón 'Aplicar Reforma RDL 32/2021' y analiza cómo la supresión de obra o servicio y el recargo de 31,40 € hunden la temporalidad privada al 12,4%.
            </li>
            <li class="bullet-item">
              <strong style="color: var(--coral);">Misión 3 · Auditoría del Fijo Discontinuo (Pestaña 3):</strong> Simula el paso a inactividad de 1.000 trabajadores de hostelería y contrasta el registro SEPE (+1.000 DENO, +0 Paro Registrado) frente a la EPA del INE.
            </li>
          </ul>
        </div>
      </div>
      <div class="col-1-3">
        <div class="card qr-card-large">
          <div class="card-title" style="color: var(--coral); font-size: 24px; margin-bottom: 6px;">¡Abre la Micro-App!</div>
          <div style="font-size: 15px; color: var(--salvia); margin-bottom: 18px;">Simulador de EPL, Despido y Dualidad</div>
          <img src="qr_app_final.png" alt="QR Micro-App Sesión 12">
          <a class="qr-link-text" href="https://mhidper.github.io/micro_apps/simulador_epl_dualidad.html" target="_blank">mhidper.github.io/micro_apps/<br>simulador_epl_dualidad.html</a>
        </div>
      </div>
    </div>
  </div>

  <!-- ===================================================================== -->
  <!-- SLIDE 19: SÍNTESIS INSTITUCIONAL Y PREPARACIÓN DEL RETO (AMPLIADA) -->
  <!-- ===================================================================== -->
  <div class="slide" data-notes="Síntesis en pizarra antes del reto manuscrito individual. Guardamos dispositivos y preparamos papel y bolígrafo.">
    <div class="slide-header">
      <div class="header-left">
        <div class="header-phase">Fase 5A (85–95 min) · Síntesis Institucional y Debate de Aula</div>
        <div class="header-title">Claves Estratégicas para un Graduado en Relaciones Laborales y RRHH</div>
      </div>
      <div class="header-right">
        <img src="../../../Logos y skills/psll_lockup.png" alt="PSLL Lockup">
        <span class="header-num">19 / 23</span>
      </div>
    </div>
    <div class="slide-body">
      <div class="col-1-2">
        <div class="card frag visible" style="height: 100%; padding: 34px 38px;">
          <div class="card-title" style="color: var(--pino); font-size: 25px; margin-bottom: 20px;">De la Flexibilidad Externa a la Flexibilidad Interna</div>
          <ul class="bullet-list" style="gap: 18px;">
            <li class="bullet-item"><strong>El fin del atajo temporal:</strong> Durante 37 años (1984–2021), las empresas españolas ajustaron costes despidiendo a temporales baratos. El RDL 32/2021 ha cerrado esa vía al suprimir el contrato de obra o servicio.</li>
            <li class="bullet-item"><strong>La brecha ΔEPL sigue determinando el ajuste:</strong> Mientras exista un salto brusco de costes e incertidumbre judicial, el diseño institucional debe vigilar que la rotación no se traslade a despidos en periodo de prueba.</li>
            <li class="bullet-item"><strong>El papel de RRHH:</strong> Gestionar la estacionalidad exige hoy dominar el contrato fijo discontinuo y la flexibilidad interna (ERTE / RED).</li>
          </ul>
        </div>
      </div>
      <div class="col-1-2">
        <div class="card frag" style="height: 100%; padding: 34px 38px;">
          <div class="card-title" style="color: var(--coral); font-size: 25px; margin-bottom: 20px;">Rigor Estadístico y Preparación del Reto</div>
          <ul class="bullet-list" style="gap: 18px;">
            <li class="bullet-item"><strong>Leer estadísticas sin trampas:</strong> Un graduado en RRLL sabe por qué el SEPE clasifica al fijo discontinuo inactivo como DENO (vínculo suspendido) mientras la EPA lo clasifica según su búsqueda real.</li>
            <li class="bullet-item"><strong>El reto pendiente del sector público:</strong> No se puede exigir estabilidad al sector privado (12,4%) manteniendo a más del 30% de los empleados públicos en interinidad.</li>
            <li class="bullet-item" style="color: var(--coral); font-weight: 700; margin-top: 10px;"><strong>Transición al Reto (Fase 5b):</strong> Guardamos los teléfonos móviles. Solo cuartilla oficial y bolígrafo (10 minutos).</li>
          </ul>
        </div>
      </div>
    </div>
  </div>

  <!-- ===================================================================== -->
  <!-- SLIDE 20: RETO TURNO MARTES (L1 · QR MAXIMIZADO) -->
  <!-- ===================================================================== -->
  <div class="slide" data-notes="Reto de evaluación continua para el Turno Martes Línea 1 (10 de noviembre de 2026). Cuenta con temporizador de 10 minutos y el QR de entrega directa en Forms.">
    <div class="slide-header">
      <div class="header-left">
        <div class="header-phase">Fase 5B (95–105 min) · Reto Manuscrito Individual (10 min · Solo Papel)</div>
        <div class="header-title">Turno Martes · Línea 1 (10 de Noviembre de 2026)</div>
      </div>
      <div class="header-right">
        <img src="../../../Logos y skills/psll_lockup.png" alt="PSLL Lockup">
        <span class="header-num">20 / 23</span>
      </div>
    </div>
    <div class="slide-body">
      <div class="col-2-3">
        <div class="card-white" style="height: 100%; padding: 34px 38px;">
          <div style="font-family: 'Outfit'; font-size: 16px; font-weight: 700; color: var(--coral); text-transform: uppercase;">Reto de Evaluación Continua · Turno Martes (Línea 1) · 1.000 pts</div>
          <p style="font-size: 16px; color: var(--salvia); margin-bottom: 22px;">Entorno libre de pantallas. Redacta a mano en tu cuartilla oficial (máximo 1 cara por alumno):</p>
          <div style="background: var(--menta); border-left: 5px solid var(--pino); padding: 24px 28px; border-radius: 10px;">
            <div style="font-family: 'Outfit'; font-size: 23px; font-weight: 700; color: var(--pino); margin-bottom: 12px;">
              Flexiseguridad Danesa vs. Dualidad Española y Brecha de EPL:
            </div>
            <p style="font-size: 18.5px; line-height: 1.6; color: var(--tinta);">
              Explica los tres vértices que integran el «Triángulo de Oro» de la flexiseguridad danesa y contrástalo con el modelo histórico de dualidad laboral español (insiders vs. outsiders). ¿Por qué una elevada brecha en la legislación de protección del empleo (ΔEPL) entre contratos indefinidos y temporales desincentiva la conversión en fijos y dispara la volatilidad del empleo en las recesiones?
            </p>
          </div>
          <div class="timer-container">
            <span style="font-size: 17px; font-weight: 600;">Tiempo restante:</span>
            <div class="timer-digits" id="t-martes">10:00</div>
            <button class="timer-btn" onclick="startTimer('t-martes', 600)">Iniciar</button>
            <button class="timer-btn" style="background: var(--salvia);" onclick="resetTimer('t-martes', 600)">Reiniciar</button>
          </div>
        </div>
      </div>
      <div class="col-1-3">
        <div class="card qr-card-large">
          <div class="card-title" style="color: var(--pino); font-size: 24px; margin-bottom: 6px;">Entrega del Reto</div>
          <div style="font-size: 15px; color: var(--salvia); margin-bottom: 18px;">Sube la foto cenital de tu cuartilla</div>
          <img src="qr_reto_martes_final.png" alt="QR Reto Martes">
          <a class="qr-link-text" href="https://forms.office.com/e/PSLL-Reto-Sesion12" target="_blank">forms.office.com/e/PSLL-Reto-Sesion12</a>
          <span style="font-size: 13px; color: #888; margin-top: 10px;">Cuenta institucional UPO</span>
        </div>
      </div>
    </div>
  </div>

  <!-- ===================================================================== -->
  <!-- SLIDE 21: RETO TURNO VIERNES (L2 · QR MAXIMIZADO) -->
  <!-- ===================================================================== -->
  <div class="slide" data-notes="Reto de evaluación continua para el Turno Viernes Línea 2 (13 de noviembre de 2026). Cuenta con temporizador de 10 minutos y el QR de entrega directa en Forms.">
    <div class="slide-header">
      <div class="header-left">
        <div class="header-phase">Fase 5B (95–105 min) · Reto Manuscrito Individual (10 min · Solo Papel)</div>
        <div class="header-title">Turno Viernes · Línea 2 (13 de Noviembre de 2026)</div>
      </div>
      <div class="header-right">
        <img src="../../../Logos y skills/psll_lockup.png" alt="PSLL Lockup">
        <span class="header-num">21 / 23</span>
      </div>
    </div>
    <div class="slide-body">
      <div class="col-2-3">
        <div class="card-white" style="height: 100%; padding: 34px 38px;">
          <div style="font-family: 'Outfit'; font-size: 16px; font-weight: 700; color: var(--coral); text-transform: uppercase;">Reto de Evaluación Continua · Turno Viernes (Línea 2) · 1.000 pts</div>
          <p style="font-size: 16px; color: var(--salvia); margin-bottom: 22px;">Entorno libre de pantallas. Redacta a mano en tu cuartilla oficial (máximo 1 cara por alumno):</p>
          <div style="background: var(--menta); border-left: 5px solid var(--pino); padding: 24px 28px; border-radius: 10px;">
            <div style="font-family: 'Outfit'; font-size: 23px; font-weight: 700; color: var(--pino); margin-bottom: 12px;">
              La Paradoja Estadística y Laboral del Contrato Fijo Discontinuo:
            </div>
            <p style="font-size: 18.5px; line-height: 1.6; color: var(--tinta);">
              Un trabajador de hostelería con contrato fijo discontinuo finaliza la campaña de verano y pasa a situación de inactividad durante 4 meses, solicitando su prestación por desempleo.<br><br>
              <strong>a)</strong> Explica con precisión cómo se contabiliza a este trabajador durante esos 4 meses en el Paro Registrado del SEPE (y por qué) frente a cómo lo clasifica la EPA del INE.<br>
              <strong>b)</strong> Señala una ventaja y una limitación real del auge de esta figura contractual tras 2022.
            </p>
          </div>
          <div class="timer-container">
            <span style="font-size: 17px; font-weight: 600;">Tiempo restante:</span>
            <div class="timer-digits" id="t-viernes">10:00</div>
            <button class="timer-btn" onclick="startTimer('t-viernes', 600)">Iniciar</button>
            <button class="timer-btn" style="background: var(--salvia);" onclick="resetTimer('t-viernes', 600)">Reiniciar</button>
          </div>
        </div>
      </div>
      <div class="col-1-3">
        <div class="card qr-card-large">
          <div class="card-title" style="color: var(--pino); font-size: 24px; margin-bottom: 6px;">Entrega del Reto</div>
          <div style="font-size: 15px; color: var(--salvia); margin-bottom: 18px;">Sube la foto cenital de tu cuartilla</div>
          <img src="qr_reto_viernes_final.png" alt="QR Reto Viernes">
          <a class="qr-link-text" href="https://forms.office.com/e/PSLL-Reto-Sesion12" target="_blank">forms.office.com/e/PSLL-Reto-Sesion12</a>
          <span style="font-size: 13px; color: #888; margin-top: 10px;">Cuenta institucional UPO</span>
        </div>
      </div>
    </div>
  </div>

  <!-- ===================================================================== -->
  <!-- SLIDE 22: SOLUCIÓN Y RÚBRICA TURNO MARTES (L1 · AMPLIADA) -->
  <!-- ===================================================================== -->
  <div class="slide" data-notes="Proyección de la solución oficial modelo y criterios de baremación continua (0-1.000 pts) para el Turno Martes L1.">
    <div class="slide-header">
      <div class="header-left">
        <div class="header-phase">Fase 5D (107–120 min) · Feedback Formativo Inmediato</div>
        <div class="header-title">Solución Modelo y Rúbrica Oficial (0–1.000 pts) · Turno Martes (L1)</div>
      </div>
      <div class="header-right">
        <img src="../../../Logos y skills/psll_lockup.png" alt="PSLL Lockup">
        <span class="header-num">22 / 23</span>
      </div>
    </div>
    <div class="slide-body">
      <div class="card-white" style="width: 100%; height: 100%; padding: 34px 40px;">
        <div class="card-title" style="color: var(--pino); font-size: 24px; margin-bottom: 24px;">
          Cuestión 1 · Flexiseguridad vs. Dualidad y Brecha de EPL (1.000 pts)
        </div>
        <ul class="bullet-list" style="font-size: 18.5px; gap: 24px;">
          <li class="bullet-item frag visible">
            <strong style="color: var(--pino);">• Triángulo de Oro Danés (400 pts):</strong> Combina tres vértices interconectados: 1) Baja protección del puesto fijo (despido ágil y flexible); 2) Red de seguridad y seguro de desempleo muy generoso (80–90% del salario); y 3) Políticas Activas de Empleo (PAE) obligatorias y eficaces que recualifican y recolocan rápidamente al trabajador.
          </li>
          <li class="bullet-item frag">
            <strong style="color: var(--salvia);">• Dualidad Española (300 pts):</strong> Segmentación histórica entre <em>insiders</em> (contratos indefinidos con alta protección indemnizatoria y judicial) y <em>outsiders</em> (contratos temporales precarios sin tutela efectiva que absorbían todo el ajuste del ciclo).
          </li>
          <li class="bullet-item frag">
            <strong style="color: var(--coral);">• Efecto de la Brecha ΔEPL (300 pts):</strong> Una gran asimetría de costes entre despedir a un indefinido y extinguir a un temporal genera un «efecto umbral»: las empresas rotan trabajadores sistemáticamente antes del plazo legal para no asumir el riesgo de indemnización fija, desincentivan la formación específica y disparan la destrucción de empleo en recesiones.
          </li>
        </ul>
      </div>
    </div>
  </div>

  <!-- ===================================================================== -->
  <!-- SLIDE 23: SOLUCIÓN Y RÚBRICA TURNO VIERNES (L2 · AMPLIADA) -->
  <!-- ===================================================================== -->
  <div class="slide" data-notes="Proyección de la solución oficial modelo y criterios de baremación continua (0-1.000 pts) para el Turno Viernes L2. Cierre de la sesión y avance de la siguiente clase.">
    <div class="slide-header">
      <div class="header-left">
        <div class="header-phase">Fase 5D (107–120 min) · Feedback Formativo Inmediato</div>
        <div class="header-title">Solución Modelo y Rúbrica Oficial (0–1.000 pts) · Turno Viernes (L2)</div>
      </div>
      <div class="header-right">
        <img src="../../../Logos y skills/psll_lockup.png" alt="PSLL Lockup">
        <span class="header-num">23 / 23</span>
      </div>
    </div>
    <div class="slide-body">
      <div class="card-white" style="width: 100%; height: 100%; padding: 34px 40px;">
        <div class="card-title" style="color: var(--pino); font-size: 24px; margin-bottom: 24px;">
          Cuestión 2 · Paradoja Estadística y Laboral del Fijo Discontinuo (1.000 pts)
        </div>
        <ul class="bullet-list" style="font-size: 18.5px; gap: 24px;">
          <li class="bullet-item frag visible">
            <strong style="color: var(--pino);">• a) Contabilización en Inactividad · SEPE vs. EPA (600 pts):</strong><br>
            - <strong>SEPE:</strong> Al estar el contrato suspendido y no extinguido, el trabajador se registra como <strong>DENO</strong> (Demandante No Ocupado con relación laboral) y <strong>NO suma en el Paro Registrado</strong> oficial (Orden Ministerial de 11/03/1985).<br>
            - <strong>EPA (INE):</strong> Aplica criterios objetivos de la OIT sin mirar la etiqueta administrativa: al no trabajar en la semana de referencia jamás es ocupado; si busca activamente otro empleo y está disponible es <strong>PARADO</strong>; si espera el llamamiento en casa sin buscar es <strong>INACTIVO</strong>.
          </li>
          <li class="bullet-item frag">
            <strong style="color: var(--coral);">• b) Ventaja y Limitación Real del Auge Contractual (400 pts):</strong><br>
            - <strong>Ventaja:</strong> Estabilidad jurídica indefinida, derecho preferente de llamamiento con tutela de despido improcedente (33 días) y cómputo de la inactividad a efectos de trienios y antigüedad.<br>
            - <strong>Limitación:</strong> No garantiza trabajar 12 meses (intermitencia salarial y precariedad anual) y ha provocado un incremento de la rotación dentro de las relaciones indefinidas.
          </li>
        </ul>
      </div>
    </div>
  </div>

  <!-- BARRA DE PROGRESO Y CONTROLES HUD -->
  <div id="progress-bar"></div>
  <div id="hud">
    <span>[←/→/Espacio] Navegar</span>
    <span>[N] Notas</span>
    <span>[F] Pantalla Completa</span>
  </div>
  <div id="notes-pane"></div>

</div>

<script>
// =============================================================================
// MOTOR TÉCNICO INTERACTIVO Y HELPER SVG
// =============================================================================
const NS = "http://www.w3.org/2000/svg";

function el(tag, attrs, parent, text){
  const e = document.createElementNS(NS, tag);
  for (const k in attrs) e.setAttribute(k, attrs[k]);
  if (text !== undefined) e.textContent = text;
  if (parent) parent.appendChild(e);
  return e;
}

function tween(dur, fn, delay){
  const start = performance.now() + (delay || 0);
  function step(t){
    const p = Math.max(0, Math.min(1, (t - start) / dur));
    const e = 1 - Math.pow(1 - p, 3); // ease-out cubic
    fn(e);
    if (p < 1) requestAnimationFrame(step);
  }
  requestAnimationFrame(step);
}

// =============================================================================
// ANIMACIONES HIPER-DINÁMICAS POR DIAPOSITIVA (ANIMS)
// =============================================================================
const anims = {

  // ---------------------------------------------------------------------------
  // SLIDE 6 (FIGURA 4.3): BEAT A BEAT (LÍNEA + BARRA CORRESPONDIENTE)
  // ---------------------------------------------------------------------------
  figura43(beat = 1, mode = 'forward') {
    const svg = document.getElementById('svg-fig43');
    if (!svg) return;

    const needsBuild = !svg.querySelector('.axis-line') || mode === 'forward' || mode === 'backward';

    const W = 1440, H = 440;
    const splitX = 900;

    const x0 = 80, x1 = 840, y0 = 360, y1 = 40;
    const xMap = yr => x0 + ((yr - 1990) / (2025 - 1990)) * (x1 - x0);
    const yMap = val => y0 - (val / 45) * (y0 - y1);

    const ptsPriv = [[1990, 32.2], [1995, 35.0], [2000, 32.1], [2006, 34.0], [2010, 24.8], [2014, 24.0], [2018, 29.2], [2021, 27.4], [2022, 17.5], [2025, 12.4]];
    const ptsPub = [[1990, 16.0], [1995, 21.0], [2000, 20.5], [2006, 26.0], [2010, 24.5], [2014, 24.2], [2018, 27.8], [2021, 31.0], [2023, 31.5], [2025, 31.2]];
    const ptsTot = [[1990, 29.8], [1995, 33.5], [2000, 31.6], [2006, 33.8], [2010, 24.7], [2014, 24.0], [2018, 26.8], [2021, 25.4], [2022, 17.9], [2025, 15.8]];

    function makePath(pts) {
      return pts.map((p, i) => `${i === 0 ? 'M' : 'L'} ${xMap(p[0]).toFixed(1)} ${yMap(p[1]).toFixed(1)}`).join(' ');
    }

    if (needsBuild) {
      svg.innerHTML = '';

      el('line', {x1: x0, y1: y0, x2: x1, y2: y0, class: 'axis-line'}, svg);
      el('line', {x1: x0, y1: y0, x2: x0, y2: y1, class: 'axis-line'}, svg);

      [10, 20, 30, 40].forEach(v => {
        el('line', {x1: x0, y1: yMap(v), x2: x1, y2: yMap(v), class: 'grid-line'}, svg);
        el('text', {x: x0 - 10, y: yMap(v) + 4, class: 'axis-label', 'text-anchor': 'end'}, svg, v + '%');
      });

      [1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025].forEach(yr => {
        el('line', {x1: xMap(yr), y1: y0, x2: xMap(yr), y2: y0 + 6, class: 'axis-line'}, svg);
        el('text', {x: xMap(yr), y: y0 + 22, class: 'axis-label', 'text-anchor': 'middle'}, svg, yr.toString());
      });

      const xReform = xMap(2021.9);
      el('rect', {
        x: xReform, y: y1, width: x1 - xReform, height: y0 - y1,
        fill: 'rgba(233, 143, 113, 0.12)', stroke: '#E98F71', 'stroke-width': 1.5, 'stroke-dasharray': '4 4'
      }, svg);
      el('text', {x: xReform + 10, y: y1 + 20, 'font-family': 'Outfit', 'font-size': 13, 'font-weight': '700', fill: '#E98F71'}, svg, 'RDL 32/2021');

      const yUE = yMap(13.5);
      el('line', {x1: x0, y1: yUE, x2: x1, y2: yUE, stroke: '#888', 'stroke-width': 2, 'stroke-dasharray': '5 5'}, svg);
      el('text', {x: x0 + 15, y: yUE - 6, 'font-family': 'Calibri', 'font-size': 13, 'font-weight': '700', fill: '#666'}, svg, 'Media UE-27: 13,5%');

      el('line', {x1: splitX, y1: y1, x2: splitX, y2: y0, stroke: '#D0DDD4', 'stroke-width': 1.5, 'stroke-dasharray': '3 3'}, svg);
      el('text', {x: splitX + 30, y: y1 + 10, 'font-family': 'Outfit', 'font-weight': '700', 'font-size': 16, fill: '#113927'}, svg, 'PANEL B: Impacto Real vs. Dualidad (Fedea/BdE)');

      const bX0 = splitX + 30;
      let bY = y1 + 50;

      // BEAT 1: SECTOR PRIVADO (LÍNEA CORAL + BARRA CORAL)
      const gBeat1 = el('g', {id: 'f43-beat1'}, svg);
      const pPriv = el('path', {d: makePath(ptsPriv), stroke: '#E98F71', 'stroke-width': 4.5, fill: 'none', class: 'chart-curve'}, gBeat1);
      const lPriv = pPriv.getTotalLength(); pPriv.style.strokeDasharray = lPriv; pPriv.style.strokeDashoffset = lPriv;
      el('circle', {cx: xMap(2025), cy: yMap(12.4), r: 6, fill: '#E98F71', stroke: '#fff', 'stroke-width': 2, id: 'f43-dot-priv', opacity: 0}, gBeat1);
      el('text', {x: xMap(2025) + 10, y: yMap(12.4) + 5, 'font-family': 'Outfit', 'font-size': 15, 'font-weight': '800', fill: '#E98F71', id: 'f43-txt-priv', opacity: 0}, gBeat1, '12,4%');

      el('text', {x: bX0, y: bY, 'font-family': 'Calibri', 'font-weight': '700', 'font-size': 14, fill: '#2F3A30'}, gBeat1, 'Temporalidad Privada');
      el('text', {x: bX0 + 380, y: bY, 'font-family': 'Outfit', 'font-weight': '700', 'font-size': 14, fill: '#E98F71', 'text-anchor': 'end'}, gBeat1, '-11,2 pp');
      el('rect', {x: bX0, y: bY + 8, width: 0, height: 14, fill: '#D0DDD4', rx: 3, id: 'f43-b1-pre'}, gBeat1);
      el('text', {x: bX0 + 5, y: bY + 20, 'font-family': 'Outfit', 'font-size': 11, fill: '#444', id: 'f43-t1-pre', opacity: 0}, gBeat1, 'Pre: 23.9%');
      el('rect', {x: bX0, y: bY + 26, width: 0, height: 16, fill: '#E98F71', rx: 3, id: 'f43-b1-post'}, gBeat1);
      el('text', {x: bX0 + 5, y: bY + 39, 'font-family': 'Outfit', 'font-weight': '700', 'font-size': 12, fill: '#fff', id: 'f43-t1-post', opacity: 0}, gBeat1, 'Post: 12.7%');

      // BEAT 2: SECTOR PÚBLICO (LÍNEA SALVIA + BARRA SALVIA)
      const gBeat2 = el('g', {id: 'f43-beat2'}, svg);
      const pPub = el('path', {d: makePath(ptsPub), stroke: '#76927A', 'stroke-width': 3.5, fill: 'none', class: 'chart-curve'}, gBeat2);
      const lPub = pPub.getTotalLength(); pPub.style.strokeDasharray = lPub; pPub.style.strokeDashoffset = lPub;
      el('circle', {cx: xMap(2025), cy: yMap(31.2), r: 6, fill: '#76927A', stroke: '#fff', 'stroke-width': 2, id: 'f43-dot-pub', opacity: 0}, gBeat2);
      el('text', {x: xMap(2025) + 10, y: yMap(31.2) + 5, 'font-family': 'Outfit', 'font-size': 15, 'font-weight': '800', fill: '#76927A', id: 'f43-txt-pub', opacity: 0}, gBeat2, '31,2%');

      bY += 75;
      el('text', {x: bX0, y: bY, 'font-family': 'Calibri', 'font-weight': '700', 'font-size': 14, fill: '#2F3A30'}, gBeat2, 'Contratos Anuales Firmados');
      el('text', {x: bX0 + 380, y: bY, 'font-family': 'Outfit', 'font-weight': '700', 'font-size': 14, fill: '#76927A', 'text-anchor': 'end'}, gBeat2, '-24%');
      el('rect', {x: bX0, y: bY + 8, width: 0, height: 14, fill: '#D0DDD4', rx: 3, id: 'f43-b2-pre'}, gBeat2);
      el('text', {x: bX0 + 5, y: bY + 20, 'font-family': 'Outfit', 'font-size': 11, fill: '#444', id: 'f43-t2-pre', opacity: 0}, gBeat2, 'Pre: 20.3 M');
      el('rect', {x: bX0, y: bY + 26, width: 0, height: 16, fill: '#76927A', rx: 3, id: 'f43-b2-post'}, gBeat2);
      el('text', {x: bX0 + 5, y: bY + 39, 'font-family': 'Outfit', 'font-weight': '700', 'font-size': 12, fill: '#fff', id: 'f43-t2-post', opacity: 0}, gBeat2, 'Post: 15.4 M');

      // BEAT 3: TOTAL ASALARIADOS (LÍNEA PINO + BARRAS FIJOS DISCONTINUOS Y SUPERVIVENCIA)
      const gBeat3 = el('g', {id: 'f43-beat3'}, svg);
      const pTot = el('path', {d: makePath(ptsTot), stroke: '#113927', 'stroke-width': 3, fill: 'none', class: 'chart-curve'}, gBeat3);
      const lTot = pTot.getTotalLength(); pTot.style.strokeDasharray = lTot; pTot.style.strokeDashoffset = lTot;
      el('circle', {cx: xMap(2025), cy: yMap(15.8), r: 5.5, fill: '#113927', stroke: '#fff', 'stroke-width': 2, id: 'f43-dot-tot', opacity: 0}, gBeat3);
      el('text', {x: xMap(2025) + 10, y: yMap(15.8) + 5, 'font-family': 'Outfit', 'font-size': 14.5, 'font-weight': '800', fill: '#113927', id: 'f43-txt-tot', opacity: 0}, gBeat3, '15,8%');

      bY += 75;
      el('text', {x: bX0, y: bY, 'font-family': 'Calibri', 'font-weight': '700', 'font-size': 14, fill: '#2F3A30'}, gBeat3, 'Stock Fijos Discontinuos');
      el('text', {x: bX0 + 380, y: bY, 'font-family': 'Outfit', 'font-weight': '700', 'font-size': 14, fill: '#113927', 'text-anchor': 'end'}, gBeat3, '+118%');
      el('rect', {x: bX0, y: bY + 8, width: 0, height: 14, fill: '#D0DDD4', rx: 3, id: 'f43-b3-pre'}, gBeat3);
      el('text', {x: bX0 + 5, y: bY + 20, 'font-family': 'Outfit', 'font-size': 11, fill: '#444', id: 'f43-t3-pre', opacity: 0}, gBeat3, 'Pre: 0.65 M');
      el('rect', {x: bX0, y: bY + 26, width: 0, height: 16, fill: '#113927', rx: 3, id: 'f43-b3-post'}, gBeat3);
      el('text', {x: bX0 + 5, y: bY + 39, 'font-family': 'Outfit', 'font-weight': '700', 'font-size': 12, fill: '#fff', id: 'f43-t3-post', opacity: 0}, gBeat3, 'Post: 1.42 M');

      bY += 75;
      el('text', {x: bX0, y: bY, 'font-family': 'Calibri', 'font-weight': '700', 'font-size': 14, fill: '#2F3A30'}, gBeat3, 'Supervivencia Indef. Ordinarios');
      el('text', {x: bX0 + 380, y: bY, 'font-family': 'Outfit', 'font-weight': '700', 'font-size': 14, fill: '#D97858', 'text-anchor': 'end'}, gBeat3, '-4,5 pp');
      el('rect', {x: bX0, y: bY + 8, width: 0, height: 14, fill: '#D0DDD4', rx: 3, id: 'f43-b4-pre'}, gBeat3);
      el('text', {x: bX0 + 5, y: bY + 20, 'font-family': 'Outfit', 'font-size': 11, fill: '#444', id: 'f43-t4-pre', opacity: 0}, gBeat3, 'Pre: 52.5%');
      el('rect', {x: bX0, y: bY + 26, width: 0, height: 16, fill: '#D97858', rx: 3, id: 'f43-b4-post'}, gBeat3);
      el('text', {x: bX0 + 5, y: bY + 39, 'font-family': 'Outfit', 'font-weight': '700', 'font-size': 12, fill: '#fff', id: 'f43-t4-post', opacity: 0}, gBeat3, 'Post: 48.0%');
    }

    const animateBeat1 = (instant = false) => {
      const p = svg.querySelector('#f43-beat1 path');
      const l = p ? p.getTotalLength() : 0;
      const dot = svg.querySelector('#f43-dot-priv'), txt = svg.querySelector('#f43-txt-priv');
      const bPre = svg.querySelector('#f43-b1-pre'), bPost = svg.querySelector('#f43-b1-post');
      const tPre = svg.querySelector('#f43-t1-pre'), tPost = svg.querySelector('#f43-t1-post');
      const targetWPre = (23.9 / (23.9 * 1.25)) * 320, targetWPost = (12.7 / (23.9 * 1.25)) * 320;

      if (instant) {
        if (p) p.style.strokeDashoffset = 0;
        if (dot) dot.setAttribute('opacity', 1);
        if (txt) txt.setAttribute('opacity', 1);
        if (bPre) bPre.setAttribute('width', targetWPre);
        if (bPost) bPost.setAttribute('width', targetWPost);
        if (tPre) tPre.setAttribute('opacity', 1);
        if (tPost) tPost.setAttribute('opacity', 1);
      } else {
        tween(1200, e => {
          if (p) p.style.strokeDashoffset = l * (1 - e);
          if (bPre) bPre.setAttribute('width', targetWPre * e);
          if (bPost) bPost.setAttribute('width', targetWPost * e);
          if (e > 0.8) {
            const op = (e - 0.8) / 0.2;
            if (dot) dot.setAttribute('opacity', op);
            if (txt) txt.setAttribute('opacity', op);
            if (tPre) tPre.setAttribute('opacity', 1);
            if (tPost) tPost.setAttribute('opacity', 1);
          }
        }, 100);
      }
    };

    const animateBeat2 = (instant = false) => {
      const p = svg.querySelector('#f43-beat2 path');
      const l = p ? p.getTotalLength() : 0;
      const dot = svg.querySelector('#f43-dot-pub'), txt = svg.querySelector('#f43-txt-pub');
      const bPre = svg.querySelector('#f43-b2-pre'), bPost = svg.querySelector('#f43-b2-post');
      const tPre = svg.querySelector('#f43-t2-pre'), tPost = svg.querySelector('#f43-t2-post');
      const maxVal = 20.3 * 1.25;
      const targetWPre = (20.3 / maxVal) * 320, targetWPost = (15.4 / maxVal) * 320;

      if (instant) {
        if (p) p.style.strokeDashoffset = 0;
        if (dot) dot.setAttribute('opacity', 1);
        if (txt) txt.setAttribute('opacity', 1);
        if (bPre) bPre.setAttribute('width', targetWPre);
        if (bPost) bPost.setAttribute('width', targetWPost);
        if (tPre) tPre.setAttribute('opacity', 1);
        if (tPost) tPost.setAttribute('opacity', 1);
      } else {
        tween(1200, e => {
          if (p) p.style.strokeDashoffset = l * (1 - e);
          if (bPre) bPre.setAttribute('width', targetWPre * e);
          if (bPost) bPost.setAttribute('width', targetWPost * e);
          if (e > 0.8) {
            const op = (e - 0.8) / 0.2;
            if (dot) dot.setAttribute('opacity', op);
            if (txt) txt.setAttribute('opacity', op);
            if (tPre) tPre.setAttribute('opacity', 1);
            if (tPost) tPost.setAttribute('opacity', 1);
          }
        }, 100);
      }
    };

    const animateBeat3 = (instant = false) => {
      const p = svg.querySelector('#f43-beat3 path');
      const l = p ? p.getTotalLength() : 0;
      const dot = svg.querySelector('#f43-dot-tot'), txt = svg.querySelector('#f43-txt-tot');
      const b3Pre = svg.querySelector('#f43-b3-pre'), b3Post = svg.querySelector('#f43-b3-post');
      const t3Pre = svg.querySelector('#f43-t3-pre'), t3Post = svg.querySelector('#f43-t3-post');
      const b4Pre = svg.querySelector('#f43-b4-pre'), b4Post = svg.querySelector('#f43-b4-post');
      const t4Pre = svg.querySelector('#f43-t4-pre'), t4Post = svg.querySelector('#f43-t4-post');

      const max3 = 1.42 * 1.25;
      const w3Pre = (0.65 / max3) * 320, w3Post = (1.42 / max3) * 320;
      const max4 = 52.5 * 1.25;
      const w4Pre = (52.5 / max4) * 320, w4Post = (48.0 / max4) * 320;

      if (instant) {
        if (p) p.style.strokeDashoffset = 0;
        if (dot) dot.setAttribute('opacity', 1);
        if (txt) txt.setAttribute('opacity', 1);
        if (b3Pre) b3Pre.setAttribute('width', w3Pre);
        if (b3Post) b3Post.setAttribute('width', w3Post);
        if (t3Pre) t3Pre.setAttribute('opacity', 1);
        if (t3Post) t3Post.setAttribute('opacity', 1);
        if (b4Pre) b4Pre.setAttribute('width', w4Pre);
        if (b4Post) b4Post.setAttribute('width', w4Post);
        if (t4Pre) t4Pre.setAttribute('opacity', 1);
        if (t4Post) t4Post.setAttribute('opacity', 1);
      } else {
        tween(1200, e => {
          if (p) p.style.strokeDashoffset = l * (1 - e);
          if (b3Pre) b3Pre.setAttribute('width', w3Pre * e);
          if (b3Post) b3Post.setAttribute('width', w3Post * e);
          if (b4Pre) b4Pre.setAttribute('width', w4Pre * e);
          if (b4Post) b4Post.setAttribute('width', w4Post * e);
          if (e > 0.8) {
            const op = (e - 0.8) / 0.2;
            if (dot) dot.setAttribute('opacity', op);
            if (txt) txt.setAttribute('opacity', op);
            if (t3Pre) t3Pre.setAttribute('opacity', 1);
            if (t3Post) t3Post.setAttribute('opacity', 1);
            if (t4Pre) t4Pre.setAttribute('opacity', 1);
            if (t4Post) t4Post.setAttribute('opacity', 1);
          }
        }, 100);
      }
    };

    const resetBeat2 = () => {
      const g = svg.querySelector('#f43-beat2');
      if (!g) return;
      const p = g.querySelector('path');
      if (p) p.style.strokeDashoffset = p.getTotalLength();
      const dot = g.querySelector('#f43-dot-pub'); if (dot) dot.setAttribute('opacity', 0);
      const txt = g.querySelector('#f43-txt-pub'); if (txt) txt.setAttribute('opacity', 0);
      const bPre = g.querySelector('#f43-b2-pre'); if (bPre) bPre.setAttribute('width', 0);
      const bPost = g.querySelector('#f43-b2-post'); if (bPost) bPost.setAttribute('width', 0);
      const tPre = g.querySelector('#f43-t2-pre'); if (tPre) tPre.setAttribute('opacity', 0);
      const tPost = g.querySelector('#f43-t2-post'); if (tPost) tPost.setAttribute('opacity', 0);
    };

    const resetBeat3 = () => {
      const g = svg.querySelector('#f43-beat3');
      if (!g) return;
      const p = g.querySelector('path');
      if (p) p.style.strokeDashoffset = p.getTotalLength();
      const dot = g.querySelector('#f43-dot-tot'); if (dot) dot.setAttribute('opacity', 0);
      const txt = g.querySelector('#f43-txt-tot'); if (txt) txt.setAttribute('opacity', 0);
      ['#f43-b3-pre', '#f43-b3-post', '#f43-b4-pre', '#f43-b4-post'].forEach(id => {
        const el = g.querySelector(id); if (el) el.setAttribute('width', 0);
      });
      ['#f43-t3-pre', '#f43-t3-post', '#f43-t4-pre', '#f43-t4-post'].forEach(id => {
        const el = g.querySelector(id); if (el) el.setAttribute('opacity', 0);
      });
    };

    if (mode === 'backward') {
      animateBeat1(true);
      animateBeat2(true);
      animateBeat3(true);
    } else if (beat === 1) {
      animateBeat1(mode === 'instant');
      resetBeat2();
      resetBeat3();
    } else if (beat === 2) {
      animateBeat1(true);
      animateBeat2(mode === 'instant');
      resetBeat3();
    } else if (beat >= 3) {
      animateBeat1(true);
      animateBeat2(true);
      animateBeat3(mode === 'instant');
    }
  },

  // ---------------------------------------------------------------------------
  // SLIDE 7: DIAGRAMA DE FLUJO SEPE VS EPA (REDISEÑADO SIN SOLAPES)
  // ---------------------------------------------------------------------------
  flujoSepeEpa() {
    const svg = document.getElementById('svg-flujo');
    if (!svg) return;
    svg.innerHTML = '';

    // Marcador de flecha en defs
    const defs = el('defs', {}, svg);
    const marker = el('marker', {id: 'arr', viewBox: '0 0 10 10', refX: '6', refY: '5', markerWidth: '6', markerHeight: '6', orient: 'auto-start-reverse'}, defs);
    el('path', {d: 'M 0 1 L 10 5 L 0 9 z', fill: '#113927'}, marker);

    const markerCoral = el('marker', {id: 'arr-c', viewBox: '0 0 10 10', refX: '6', refY: '5', markerWidth: '6', markerHeight: '6', orient: 'auto-start-reverse'}, defs);
    el('path', {d: 'M 0 1 L 10 5 L 0 9 z', fill: '#E98F71'}, markerCoral);

    // 1. Nodo Entrada Central Izquierda
    const g0 = el('g', {}, svg);
    el('rect', {x: 40, y: 155, width: 280, height: 110, rx: 12, fill: '#F4F8F5', stroke: '#113927', 'stroke-width': 2.5}, g0);
    el('text', {x: 180, y: 195, 'font-family': 'Outfit', 'font-weight': '800', 'font-size': 18, fill: '#113927', 'text-anchor': 'middle'}, g0, 'FIJO DISCONTINUO');
    el('text', {x: 180, y: 220, 'font-family': 'Calibri', 'font-weight': '700', 'font-size': 15, fill: '#76927A', 'text-anchor': 'middle'}, g0, 'Contrato Indefinido (Art. 16 ET)');
    el('text', {x: 180, y: 242, 'font-family': 'Calibri', 'font-size': 14, fill: '#2F3A30', 'text-anchor': 'middle'}, g0, 'Vínculo laboral permanente');

    // RAMA SUPERIOR: ACTIVIDAD (CAMPAÑA)
    // Línea limpia
    el('path', {d: 'M 320 185 C 390 185, 410 75, 480 75', stroke: '#113927', 'stroke-width': 3, fill: 'none', 'marker-end': 'url(#arr)'}, svg);
    // Badge de etiqueta sobre fondo blanco
    el('rect', {x: 340, y: 105, width: 120, height: 26, rx: 5, fill: '#FFFFFF', stroke: '#113927', 'stroke-width': 1.5}, svg);
    el('text', {x: 400, y: 123, 'font-family': 'Outfit', 'font-weight': '700', 'font-size': 12, fill: '#113927', 'text-anchor': 'middle'}, svg, 'EN TEMPORADA');

    // Caja Actividad
    const gAct = el('g', {}, svg);
    el('rect', {x: 490, y: 25, width: 890, height: 95, rx: 12, fill: '#FFFFFF', stroke: '#113927', 'stroke-width': 2}, gAct);
    el('text', {x: 520, y: 60, 'font-family': 'Outfit', 'font-weight': '800', 'font-size': 20, fill: '#113927'}, gAct, 'EN ACTIVIDAD · PLENA COINCIDENCIA (TGSS = EPA)');
    el('text', {x: 520, y: 92, 'font-family': 'Calibri', 'font-size': 16.5, fill: '#2F3A30'}, gAct, '• TGSS: Afiliado en ALTA cotizando  |  • SEPE: No demandante  |  • INE EPA: OCUPADO (&ge; 1 hora trabajada)');

    // RAMA INFERIOR: INACTIVIDAD
    // Línea limpia
    el('path', {d: 'M 320 235 C 380 235, 400 300, 470 300', stroke: '#E98F71', 'stroke-width': 3.5, fill: 'none', 'marker-end': 'url(#arr-c)'}, svg);
    // Badge de etiqueta
    el('rect', {x: 335, y: 265, width: 130, height: 26, rx: 5, fill: '#FFFFFF', stroke: '#E98F71', 'stroke-width': 1.5}, svg);
    el('text', {x: 400, y: 283, 'font-family': 'Outfit', 'font-weight': '700', 'font-size': 12, fill: '#E98F71', 'text-anchor': 'middle'}, svg, 'FIN DE CAMPAÑA');

    // Nodo Puente Inactividad
    const gInact = el('g', {}, svg);
    el('rect', {x: 480, y: 235, width: 270, height: 130, rx: 12, fill: '#FFF5F2', stroke: '#E98F71', 'stroke-width': 2.5}, gInact);
    el('text', {x: 615, y: 272, 'font-family': 'Outfit', 'font-weight': '800', 'font-size': 18, fill: '#E98F71', 'text-anchor': 'middle'}, gInact, 'EN INACTIVIDAD');
    el('text', {x: 615, y: 300, 'font-family': 'Calibri', 'font-weight': '700', 'font-size': 15, fill: '#2F3A30', 'text-anchor': 'middle'}, gInact, 'Contrato SUSPENDIDO');
    el('text', {x: 615, y: 324, 'font-family': 'Calibri', 'font-size': 14.5, fill: '#2F3A30', 'text-anchor': 'middle'}, gInact, 'Cobra prestación de desempleo');
    el('text', {x: 615, y: 346, 'font-family': 'Calibri', 'font-weight': '700', 'font-size': 13.5, fill: '#E98F71', 'text-anchor': 'middle'}, gInact, 'Vínculo sigue vivo');

    // Bifurcación desde Puente a SEPE vs EPA
    el('line', {x1: 750, y1: 275, x2: 830, y2: 215, stroke: '#E98F71', 'stroke-width': 2.5, 'marker-end': 'url(#arr-c)'}, svg);
    el('line', {x1: 750, y1: 325, x2: 830, y2: 375, stroke: '#76927A', 'stroke-width': 2.5, 'marker-end': 'url(#arr)'}, svg);

    // Caja SEPE
    const gSepe = el('g', {}, svg);
    el('rect', {x: 840, y: 155, width: 550, height: 120, rx: 12, fill: '#FFFFFF', stroke: '#E98F71', 'stroke-width': 2}, gSepe);
    el('text', {x: 865, y: 190, 'font-family': 'Outfit', 'font-weight': '800', 'font-size': 18, fill: '#E98F71'}, gSepe, 'REGISTRO SEPE: DEMANDANTE NO OCUPADO (DENO)');
    el('text', {x: 865, y: 220, 'font-family': 'Calibri', 'font-size': 15.5, fill: '#2F3A30'}, gSepe, '• Orden Ministerial 11/03/1985: Excluido del Paro Registrado.');
    el('text', {x: 865, y: 245, 'font-family': 'Calibri', 'font-weight': '700', 'font-size': 15.5, fill: '#E98F71'}, gSepe, '• No suma en la cifra oficial de desempleo mensual.');

    // Caja EPA
    const gEpa = el('g', {}, svg);
    el('rect', {x: 840, y: 310, width: 550, height: 120, rx: 12, fill: '#FFFFFF', stroke: '#76927A', 'stroke-width': 2}, gEpa);
    el('text', {x: 865, y: 345, 'font-family': 'Outfit', 'font-weight': '800', 'font-size': 18, fill: '#113927'}, gEpa, 'ENCUESTA EPA (INE): CRITERIO PURO DE LA OIT');
    el('text', {x: 865, y: 375, 'font-family': 'Calibri', 'font-size': 15.5, fill: '#2F3A30'}, gEpa, '• ¿Búsqueda activa y disponibilidad? &rarr; Clasificado como PARADO.');
    el('text', {x: 865, y: 400, 'font-family': 'Calibri', 'font-size': 15.5, fill: '#2F3A30'}, gEpa, '• ¿Espera pasiva sin buscar empleo? &rarr; Clasificado como INACTIVO.');
  },

  // ---------------------------------------------------------------------------
  // SLIDE 9: TRIÁNGULO DE ORO DANÉS VS DUALIDAD ESPAÑOLA (LIMPIO)
  // ---------------------------------------------------------------------------
  figura41() {
    const svg = document.getElementById('svg-fig41');
    if (!svg) return;
    svg.innerHTML = '';

    // PANEL IZQUIERDO: TRIÁNGULO DANÉS
    el('text', {x: 360, y: 40, 'font-family': 'Outfit', 'font-weight': '800', 'font-size': 21, fill: '#113927', 'text-anchor': 'middle'}, svg, 'TRIÁNGULO DE ORO DANÉS (FLEXISEGURIDAD)');

    el('rect', {x: 220, y: 75, width: 280, height: 75, rx: 10, fill: '#113927'}, svg);
    el('text', {x: 360, y: 105, 'font-family': 'Outfit', 'font-weight': '700', 'font-size': 16, fill: '#fff', 'text-anchor': 'middle'}, svg, '1. DESPIDO FLEXIBLE Y ÁGIL');
    el('text', {x: 360, y: 130, 'font-family': 'Calibri', 'font-size': 14, fill: '#D2E4D6', 'text-anchor': 'middle'}, svg, 'Baja indemnización, agilidad empresarial');

    el('rect', {x: 50, y: 310, width: 280, height: 75, rx: 10, fill: '#76927A'}, svg);
    el('text', {x: 190, y: 340, 'font-family': 'Outfit', 'font-weight': '700', 'font-size': 16, fill: '#fff', 'text-anchor': 'middle'}, svg, '2. RED DE SEGURIDAD GENEROSA');
    el('text', {x: 190, y: 365, 'font-family': 'Calibri', 'font-size': 14, fill: '#F4F8F5', 'text-anchor': 'middle'}, svg, 'Seguro de desempleo (80–90% salario)');

    el('rect', {x: 390, y: 310, width: 280, height: 75, rx: 10, fill: '#E98F71'}, svg);
    el('text', {x: 530, y: 340, 'font-family': 'Outfit', 'font-weight': '700', 'font-size': 16, fill: '#fff', 'text-anchor': 'middle'}, svg, '3. PAE Y FORMACIÓN ACTIVA');
    el('text', {x: 530, y: 365, 'font-family': 'Calibri', 'font-size': 14, fill: '#FFF5F2', 'text-anchor': 'middle'}, svg, 'Recualificación y búsqueda intensiva');

    el('line', {x1: 290, y1: 150, x2: 210, y2: 310, stroke: '#113927', 'stroke-width': 3, 'stroke-dasharray': '6 6'}, svg);
    el('line', {x1: 430, y1: 150, x2: 510, y2: 310, stroke: '#E98F71', 'stroke-width': 3, 'stroke-dasharray': '6 6'}, svg);
    el('line', {x1: 330, y1: 347, x2: 390, y2: 347, stroke: '#76927A', 'stroke-width': 3, 'stroke-dasharray': '6 6'}, svg);

    el('circle', {cx: 360, cy: 235, r: 52, fill: '#FFFFFF', stroke: '#113927', 'stroke-width': 2.5}, svg);
    el('text', {x: 360, y: 230, 'font-family': 'Outfit', 'font-weight': '800', 'font-size': 15, fill: '#113927', 'text-anchor': 'middle'}, svg, 'SEGURIDAD');
    el('text', {x: 360, y: 250, 'font-family': 'Calibri', 'font-weight': '700', 'font-size': 13.5, fill: '#76927A', 'text-anchor': 'middle'}, svg, 'en la persona');

    // PANEL DERECHO: MURO DE DUALIDAD
    el('line', {x1: 720, y1: 25, x2: 720, y2: 415, stroke: '#D0DDD4', 'stroke-width': 1.5, 'stroke-dasharray': '3 3'}, svg);
    el('text', {x: 1080, y: 40, 'font-family': 'Outfit', 'font-weight': '800', 'font-size': 21, fill: '#E98F71', 'text-anchor': 'middle'}, svg, 'MODELO DUAL ESPAÑOL (INSIDERS VS OUTSIDERS)');

    el('rect', {x: 770, y: 80, width: 260, height: 180, rx: 10, fill: '#F4F8F5', stroke: '#113927', 'stroke-width': 2.5}, svg);
    el('text', {x: 900, y: 112, 'font-family': 'Outfit', 'font-weight': '800', 'font-size': 17, fill: '#113927', 'text-anchor': 'middle'}, svg, 'INSIDERS (INDEFINIDOS)');
    el('text', {x: 790, y: 145, 'font-family': 'Calibri', 'font-size': 14.5, fill: '#2F3A30'}, svg, '• Alta protección legal (EPL)');
    el('text', {x: 790, y: 175, 'font-family': 'Calibri', 'font-size': 14.5, fill: '#2F3A30'}, svg, '• 33–45 días de indemnización');
    el('text', {x: 790, y: 205, 'font-family': 'Calibri', 'font-size': 14.5, fill: '#2F3A30'}, svg, '• Formación específica acumulada');
    el('text', {x: 790, y: 235, 'font-family': 'Calibri', 'font-weight': '700', 'font-size': 14.5, fill: '#113927'}, svg, '• Blindados frente al ciclo');

    el('rect', {x: 1050, y: 70, width: 60, height: 200, rx: 6, fill: '#E98F71'}, svg);
    el('text', {x: 1080, y: 145, 'font-family': 'Outfit', 'font-weight': '800', 'font-size': 14, fill: '#fff', 'text-anchor': 'middle'}, svg, 'MURO');
    el('text', {x: 1080, y: 168, 'font-family': 'Outfit', 'font-weight': '800', 'font-size': 15, fill: '#fff', 'text-anchor': 'middle'}, svg, 'ΔEPL');
    el('text', {x: 1080, y: 198, 'font-family': 'Calibri', 'font-size': 12, fill: '#fff', 'text-anchor': 'middle'}, svg, 'Brecha');

    el('rect', {x: 1130, y: 80, width: 260, height: 180, rx: 10, fill: '#FFF5F2', stroke: '#E98F71', 'stroke-width': 2.5}, svg);
    el('text', {x: 1260, y: 112, 'font-family': 'Outfit', 'font-weight': '800', 'font-size': 17, fill: '#E98F71', 'text-anchor': 'middle'}, svg, 'OUTSIDERS (TEMPORALES)');
    el('text', {x: 1150, y: 145, 'font-family': 'Calibri', 'font-size': 14.5, fill: '#2F3A30'}, svg, '• Extinción barata (12 días)');
    el('text', {x: 1150, y: 175, 'font-family': 'Calibri', 'font-size': 14.5, fill: '#2F3A30'}, svg, '• Sin tutela judicial efectiva');
    el('text', {x: 1150, y: 205, 'font-family': 'Calibri', 'font-size': 14.5, fill: '#2F3A30'}, svg, '• Nula inversión en formación');
    el('text', {x: 1150, y: 235, 'font-family': 'Calibri', 'font-weight': '700', 'font-size': 14.5, fill: '#E98F71'}, svg, '• Absorben 85% del despido');

    el('rect', {x: 770, y: 295, width: 620, height: 95, rx: 10, fill: '#FFF9F6', stroke: '#E98F71', 'stroke-width': 1.5, 'stroke-dasharray': '4 4'}, svg);
    el('text', {x: 1080, y: 325, 'font-family': 'Outfit', 'font-weight': '700', 'font-size': 16, fill: '#E98F71', 'text-anchor': 'middle'}, svg, 'CÍRCULO VICIOSO DE LA DUALIDAD (PRODUCTIVIDAD ESTANCADA)');
    el('text', {x: 1080, y: 355, 'font-family': 'Calibri', 'font-size': 14.5, fill: '#2F3A30', 'text-anchor': 'middle'}, svg, 'Alta rotación de temporales → Falta de horizonte temporal → Menor inversión formativa → Baja productividad');
  },

  // ---------------------------------------------------------------------------
  // SLIDE 11: EPL OCDE
  // ---------------------------------------------------------------------------
  figura42() {
    const svg = document.getElementById('svg-fig42');
    if (!svg) return;
    svg.innerHTML = '';

    const countries = [
      {name: 'EE.UU.', epr: 0.09, ept: 0.25},
      {name: 'Reino Unido', epr: 1.35, ept: 0.54},
      {name: 'Dinamarca', epr: 1.53, ept: 1.63},
      {name: 'Media OCDE', epr: 2.05, ept: 1.82},
      {name: 'Alemania', epr: 2.50, ept: 2.00},
      {name: 'Francia', epr: 2.56, ept: 2.40},
      {name: 'España (Pre-2021)', epr: 2.00, ept: 1.90},
      {name: 'España (Post-2021)', epr: 2.00, ept: 2.67}
    ];

    const W = 1440, H = 440;
    const x0 = 80, x1 = 1380, y0 = 360, y1 = 40;
    const yMap = v => y0 - (v / 4.0) * (y0 - y1);

    [0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5].forEach(v => {
      el('line', {x1: x0, y1: yMap(v), x2: x1, y2: yMap(v), class: 'grid-line'}, svg);
      el('text', {x: x0 - 12, y: yMap(v) + 4, class: 'axis-label', 'text-anchor': 'end'}, svg, v.toFixed(1));
    });
    el('line', {x1: x0, y1: y0, x2: x1, y2: y0, class: 'axis-line'}, svg);

    const groupW = (x1 - x0) / countries.length;
    const barW = 32;

    countries.forEach((c, idx) => {
      const gX = x0 + idx * groupW + groupW / 2;

      el('text', {x: gX, y: y0 + 26, 'font-family': 'Outfit', 'font-weight': '700', 'font-size': 14, fill: idx >= 6 ? '#E98F71' : '#113927', 'text-anchor': 'middle'}, svg, c.name);

      const hEPR = (c.epr / 4.0) * (y0 - y1);
      const bEPR = el('rect', {x: gX - barW - 2, y: y0, width: barW, height: 0, fill: '#113927', rx: 3}, svg);
      const tEPR = el('text', {x: gX - barW/2 - 2, y: y0 - 8, 'font-family': 'Outfit', 'font-weight': '700', 'font-size': 13, fill: '#113927', 'text-anchor': 'middle', opacity: 0}, svg, c.epr.toFixed(2));

      const hEPT = (c.ept / 4.0) * (y0 - y1);
      const bEPT = el('rect', {x: gX + 2, y: y0, width: barW, height: 0, fill: '#E98F71', rx: 3}, svg);
      const tEPT = el('text', {x: gX + barW/2 + 2, y: y0 - 8, 'font-family': 'Outfit', 'font-weight': '700', 'font-size': 13, fill: '#E98F71', 'text-anchor': 'middle', opacity: 0}, svg, c.ept.toFixed(2));

      tween(1200, e => {
        const curH1 = hEPR * e;
        const curH2 = hEPT * e;
        bEPR.setAttribute('y', y0 - curH1);
        bEPR.setAttribute('height', curH1);
        tEPR.setAttribute('y', y0 - curH1 - 6);

        bEPT.setAttribute('y', y0 - curH2);
        bEPT.setAttribute('height', curH2);
        tEPT.setAttribute('y', y0 - curH2 - 6);

        if (e > 0.7) {
          tEPR.setAttribute('opacity', (e - 0.7) / 0.3);
          tEPT.setAttribute('opacity', (e - 0.7) / 0.3);
        }
      }, 100 + idx * 120);
    });
  },

  // ---------------------------------------------------------------------------
  // SLIDE 13: CURVAS DE DESPIDO Y LITIGIOSIDAD BEAT A BEAT
  // ---------------------------------------------------------------------------
  figura44(beat = 1, mode = 'forward') {
    const svg = document.getElementById('svg-fig44');
    if (!svg) return;

    const needsBuild = !svg.querySelector('.axis-line') || mode === 'forward' || mode === 'backward';

    const W = 1440, H = 440;
    const splitX = 920;

    const x0 = 80, x1 = 880, y0 = 360, y1 = 40;
    const xMap = yr => x0 + (yr / 30) * (x1 - x0);
    const yMap = m => y0 - (m / 45) * (y0 - y1);

    const ptsPre = [[0, 0], [10, 15], [20, 30], [28, 42], [30, 42]];
    const ptsObj = [[0, 0], [5, 3.33], [10, 6.67], [15, 10], [18, 12], [30, 12]];
    const ptsImp = [[0, 0], [5, 5.5], [10, 11], [15, 16.5], [21.8, 24], [30, 24]];

    function makePath(pts) {
      return pts.map((p, i) => `${i === 0 ? 'M' : 'L'} ${xMap(p[0]).toFixed(1)} ${yMap(p[1]).toFixed(1)}`).join(' ');
    }

    const polyPts = [
      ...ptsImp.map(p => `${xMap(p[0]).toFixed(1)},${yMap(p[1]).toFixed(1)}`),
      ...ptsObj.slice().reverse().map(p => `${xMap(p[0]).toFixed(1)},${yMap(p[1]).toFixed(1)}`)
    ].join(' ');

    const maxEuros = 45000;
    const bW = 340;

    if (needsBuild) {
      svg.innerHTML = '';

      el('line', {x1: x0, y1: y0, x2: x1, y2: y0, class: 'axis-line'}, svg);
      el('line', {x1: x0, y1: y0, x2: x0, y2: y1, class: 'axis-line'}, svg);

      [10, 20, 24, 30, 42].forEach(m => {
        el('line', {x1: x0, y1: yMap(m), x2: x1, y2: yMap(m), class: 'grid-line'}, svg);
        el('text', {x: x0 - 10, y: yMap(m) + 4, class: 'axis-label', 'text-anchor': 'end'}, svg, m + ' m');
      });

      [5, 10, 15, 20, 25, 30].forEach(a => {
        el('line', {x1: xMap(a), y1: y0, x2: xMap(a), y2: y0 + 6, class: 'axis-line'}, svg);
        el('text', {x: xMap(a), y: y0 + 22, class: 'axis-label', 'text-anchor': 'middle'}, svg, a + ' años');
      });

      el('line', {x1: splitX, y1: y1, x2: splitX, y2: y0, stroke: '#D0DDD4', 'stroke-width': 1.5, 'stroke-dasharray': '3 3'}, svg);
      el('text', {x: splitX + 30, y: y1 + 10, 'font-family': 'Outfit', 'font-weight': '700', 'font-size': 16, fill: '#113927'}, svg, 'PANEL B: Coste Real para 2.400 €/mes (80 €/d)');

      // BEAT 1: OBJETIVO PROCEDENTE (20 d) + PRE-2012 (45 d) + BARRAS OBJETIVO (8.000 € y 24.000 €)
      const gBeat1 = el('g', {id: 'f44-beat1'}, svg);
      const pPre = el('path', {d: makePath(ptsPre), stroke: '#999', 'stroke-width': 2.5, 'stroke-dasharray': '5 5', fill: 'none', class: 'chart-curve'}, gBeat1);
      const lPre = pPre.getTotalLength(); pPre.style.strokeDasharray = lPre; pPre.style.strokeDashoffset = lPre;

      const pObj = el('path', {d: makePath(ptsObj), stroke: '#113927', 'stroke-width': 3.5, fill: 'none', class: 'chart-curve'}, gBeat1);
      const lObj = pObj.getTotalLength(); pObj.style.strokeDasharray = lObj; pObj.style.strokeDashoffset = lObj;

      const ey2 = y1 + 55 + 65;
      el('text', {x: splitX + 30, y: ey2, 'font-family': 'Calibri', 'font-weight': '700', 'font-size': 14, fill: '#2F3A30'}, gBeat1, 'Objetivo Procedente (5 años · 20 d)');
      el('rect', {x: splitX + 30, y: ey2 + 8, width: 0, height: 20, fill: '#113927', rx: 4, id: 'f44-b-obj5'}, gBeat1);
      el('text', {x: splitX + 35, y: ey2 + 23, 'font-family': 'Outfit', 'font-weight': '700', 'font-size': 13.5, fill: '#fff', id: 'f44-t-obj5', opacity: 0}, gBeat1, '8.000 €');

      const ey4 = y1 + 55 + 65 * 3;
      el('text', {x: splitX + 30, y: ey4, 'font-family': 'Calibri', 'font-weight': '700', 'font-size': 14, fill: '#2F3A30'}, gBeat1, 'Objetivo Procedente (15 años · 20 d)');
      el('rect', {x: splitX + 30, y: ey4 + 8, width: 0, height: 20, fill: '#113927', rx: 4, id: 'f44-b-obj15'}, gBeat1);
      el('text', {x: splitX + 35, y: ey4 + 23, 'font-family': 'Outfit', 'font-weight': '700', 'font-size': 13.5, fill: '#fff', id: 'f44-t-obj15', opacity: 0}, gBeat1, '24.000 €');

      // BEAT 2: IMPROCEDENTE (33 d) + LITIGIOSIDAD (+65%) + BARRAS IMPROCEDENTE (13.200 € y 39.600 €)
      const gBeat2 = el('g', {id: 'f44-beat2'}, svg);
      el('polygon', {points: polyPts, fill: 'rgba(233, 143, 113, 0.28)', id: 'f44-lit-area', opacity: 0}, gBeat2);

      const pImp = el('path', {d: makePath(ptsImp), stroke: '#E98F71', 'stroke-width': 4.5, fill: 'none', class: 'chart-curve'}, gBeat2);
      const lImp = pImp.getTotalLength(); pImp.style.strokeDasharray = lImp; pImp.style.strokeDashoffset = lImp;

      const badgeLit = el('g', {id: 'f44-badge-lit', opacity: 0}, gBeat2);
      el('rect', {x: xMap(6), y: yMap(23), width: 280, height: 42, rx: 8, fill: '#FFFFFF', stroke: '#E98F71', 'stroke-width': 2.5}, badgeLit);
      el('text', {x: xMap(6) + 140, y: yMap(23) + 26, 'font-family': 'Outfit', 'font-size': 15, 'font-weight': '800', fill: '#113927', 'text-anchor': 'middle'}, badgeLit, 'PRIMA DE LITIGIOSIDAD (+65%)');
      el('line', {x1: xMap(10), y1: yMap(23) + 42, x2: xMap(11), y2: yMap(11), stroke: '#E98F71', 'stroke-width': 2, 'stroke-dasharray': '3 3'}, badgeLit);

      const ey3 = y1 + 55 + 65 * 2;
      el('text', {x: splitX + 30, y: ey3, 'font-family': 'Calibri', 'font-weight': '700', 'font-size': 14, fill: '#2F3A30'}, gBeat2, 'Improcedente Vigente (5 años · 33 d)');
      el('rect', {x: splitX + 30, y: ey3 + 8, width: 0, height: 20, fill: '#E98F71', rx: 4, id: 'f44-b-imp5'}, gBeat2);
      el('text', {x: splitX + 35, y: ey3 + 23, 'font-family': 'Outfit', 'font-weight': '700', 'font-size': 13.5, fill: '#fff', id: 'f44-t-imp5', opacity: 0}, gBeat2, '13.200 €');

      const ey5 = y1 + 55 + 65 * 4;
      el('text', {x: splitX + 30, y: ey5, 'font-family': 'Calibri', 'font-weight': '700', 'font-size': 14, fill: '#2F3A30'}, gBeat2, 'Improcedente Vigente (15 años · 33 d)');
      el('rect', {x: splitX + 30, y: ey5 + 8, width: 0, height: 20, fill: '#E98F71', rx: 4, id: 'f44-b-imp15'}, gBeat2);
      el('text', {x: splitX + 35, y: ey5 + 23, 'font-family': 'Outfit', 'font-weight': '700', 'font-size': 13.5, fill: '#fff', id: 'f44-t-imp15', opacity: 0}, gBeat2, '39.600 €');

      // BEAT 3: FIN TEMPORAL (12 d · 960 €)
      const gBeat3 = el('g', {id: 'f44-beat3'}, svg);
      const ey1 = y1 + 55;
      el('text', {x: splitX + 30, y: ey1, 'font-family': 'Calibri', 'font-weight': '700', 'font-size': 14, fill: '#2F3A30'}, gBeat3, 'Fin Temporal (1 año · 12 d)');
      el('rect', {x: splitX + 30, y: ey1 + 8, width: 0, height: 20, fill: '#76927A', rx: 4, id: 'f44-b-temp'}, gBeat3);
      el('text', {x: splitX + 35, y: ey1 + 23, 'font-family': 'Outfit', 'font-weight': '700', 'font-size': 13.5, fill: '#fff', id: 'f44-t-temp', opacity: 0}, gBeat3, '960 €');
    }

    const animateBeat1 = (instant = false) => {
      const g = svg.querySelector('#f44-beat1');
      if (!g) return;
      const paths = g.querySelectorAll('path');
      const pPre = paths[0], pObj = paths[1];
      const lPre = pPre ? pPre.getTotalLength() : 0;
      const lObj = pObj ? pObj.getTotalLength() : 0;

      const b5 = g.querySelector('#f44-b-obj5'), t5 = g.querySelector('#f44-t-obj5');
      const b15 = g.querySelector('#f44-b-obj15'), t15 = g.querySelector('#f44-t-obj15');
      const w5 = (8000 / maxEuros) * bW;
      const w15 = (24000 / maxEuros) * bW;

      if (instant) {
        if (pPre) pPre.style.strokeDashoffset = 0;
        if (pObj) pObj.style.strokeDashoffset = 0;
        if (b5) b5.setAttribute('width', w5);
        if (t5) t5.setAttribute('opacity', 1);
        if (b15) b15.setAttribute('width', w15);
        if (t15) t15.setAttribute('opacity', 1);
      } else {
        tween(1200, e => {
          if (pPre) pPre.style.strokeDashoffset = lPre * (1 - e);
          if (pObj) pObj.style.strokeDashoffset = lObj * (1 - e);
          if (b5) b5.setAttribute('width', w5 * e);
          if (b15) b15.setAttribute('width', w15 * e);
          if (e > 0.6) {
            if (t5) t5.setAttribute('opacity', 1);
            if (t15) t15.setAttribute('opacity', 1);
          }
        }, 100);
      }
    };

    const animateBeat2 = (instant = false) => {
      const g = svg.querySelector('#f44-beat2');
      if (!g) return;
      const pImp = g.querySelector('path');
      const lImp = pImp ? pImp.getTotalLength() : 0;
      const lit = g.querySelector('#f44-lit-area');
      const badge = g.querySelector('#f44-badge-lit');

      const b5 = g.querySelector('#f44-b-imp5'), t5 = g.querySelector('#f44-t-imp5');
      const b15 = g.querySelector('#f44-b-imp15'), t15 = g.querySelector('#f44-t-imp15');
      const w5 = (13200 / maxEuros) * bW;
      const w15 = (39600 / maxEuros) * bW;

      if (instant) {
        if (pImp) pImp.style.strokeDashoffset = 0;
        if (lit) lit.setAttribute('opacity', 1);
        if (badge) badge.setAttribute('opacity', 1);
        if (b5) b5.setAttribute('width', w5);
        if (t5) t5.setAttribute('opacity', 1);
        if (b15) b15.setAttribute('width', w15);
        if (t15) t15.setAttribute('opacity', 1);
      } else {
        tween(1200, e => {
          if (pImp) pImp.style.strokeDashoffset = lImp * (1 - e);
          if (lit) lit.setAttribute('opacity', e);
          if (badge) badge.setAttribute('opacity', e);
          if (b5) b5.setAttribute('width', w5 * e);
          if (b15) b15.setAttribute('width', w15 * e);
          if (e > 0.6) {
            if (t5) t5.setAttribute('opacity', 1);
            if (t15) t15.setAttribute('opacity', 1);
          }
        }, 100);
      }
    };

    const animateBeat3 = (instant = false) => {
      const g = svg.querySelector('#f44-beat3');
      if (!g) return;
      const bT = g.querySelector('#f44-b-temp'), tT = g.querySelector('#f44-t-temp');
      const wT = (960 / maxEuros) * bW;

      if (instant) {
        if (bT) bT.setAttribute('width', wT);
        if (tT) tT.setAttribute('opacity', 1);
      } else {
        tween(1000, e => {
          if (bT) bT.setAttribute('width', wT * e);
          if (e > 0.6 && tT) tT.setAttribute('opacity', 1);
        }, 100);
      }
    };

    const resetBeat2 = () => {
      const g = svg.querySelector('#f44-beat2');
      if (!g) return;
      const pImp = g.querySelector('path');
      if (pImp) pImp.style.strokeDashoffset = pImp.getTotalLength();
      const lit = g.querySelector('#f44-lit-area'); if (lit) lit.setAttribute('opacity', 0);
      const badge = g.querySelector('#f44-badge-lit'); if (badge) badge.setAttribute('opacity', 0);
      const b5 = g.querySelector('#f44-b-imp5'); if (b5) b5.setAttribute('width', 0);
      const t5 = g.querySelector('#f44-t-imp5'); if (t5) t5.setAttribute('opacity', 0);
      const b15 = g.querySelector('#f44-b-imp15'); if (b15) b15.setAttribute('width', 0);
      const t15 = g.querySelector('#f44-t-imp15'); if (t15) t15.setAttribute('opacity', 0);
    };

    const resetBeat3 = () => {
      const g = svg.querySelector('#f44-beat3');
      if (!g) return;
      const bT = g.querySelector('#f44-b-temp'); if (bT) bT.setAttribute('width', 0);
      const tT = g.querySelector('#f44-t-temp'); if (tT) tT.setAttribute('opacity', 0);
    };

    if (mode === 'backward') {
      animateBeat1(true);
      animateBeat2(true);
      animateBeat3(true);
    } else if (beat === 1) {
      animateBeat1(mode === 'instant');
      resetBeat2();
      resetBeat3();
    } else if (beat === 2) {
      animateBeat1(true);
      animateBeat2(mode === 'instant');
      resetBeat3();
    } else if (beat >= 3) {
      animateBeat1(true);
      animateBeat2(true);
      animateBeat3(mode === 'instant');
    }
  }

};

// =============================================================================
// NAVEGACIÓN Y TECLADO
// =============================================================================
let curSlide = 0;
const slides = document.querySelectorAll('.slide');
const totalSlides = slides.length;
const stage = document.getElementById('stage');
const progressBar = document.getElementById('progress-bar');
const notesPane = document.getElementById('notes-pane');

function fit() {
  const w = window.innerWidth;
  const h = window.innerHeight;
  const scale = Math.min(w / 1600, h / 900);
  stage.style.transform = `scale(${scale})`;
}
window.addEventListener('resize', fit);
fit();

// Marcar fragmentos que comienzan visibles por defecto
slides.forEach(slide => {
  slide.querySelectorAll('.frag.visible').forEach(f => {
    f.dataset.initial = 'true';
  });
});

function updateUI(dir = 'forward') {
  slides.forEach((s, idx) => {
    s.classList.toggle('active', idx === curSlide);
  });
  const pct = ((curSlide + 1) / totalSlides) * 100;
  progressBar.style.width = pct + '%';

  const notes = slides[curSlide].getAttribute('data-notes') || 'Sin notas para esta diapositiva.';
  notesPane.innerHTML = `<strong>Notas del Orador (Slide ${curSlide + 1}/${totalSlides}):</strong><br>${notes}`;

  const currentSlideEl = slides[curSlide];

  // Gestión de beats/fragmentos según la dirección de entrada
  if (dir === 'forward') {
    currentSlideEl.querySelectorAll('.frag').forEach(f => {
      if (f.dataset.initial === 'true') {
        f.classList.add('visible');
      } else {
        f.classList.remove('visible');
      }
    });
  } else if (dir === 'backward') {
    currentSlideEl.querySelectorAll('.frag').forEach(f => {
      f.classList.add('visible');
    });
  }

  const visCount = currentSlideEl.querySelectorAll('.frag.visible').length || 1;
  const animName = currentSlideEl.getAttribute('data-anim');
  if (animName && anims[animName]) {
    anims[animName](visCount, dir);
  }
}

function getFrags(slide) {
  return Array.from(slide.querySelectorAll('.frag'));
}

function next() {
  const s = slides[curSlide];
  const frags = getFrags(s);
  const hiddenFrag = frags.find(f => !f.classList.contains('visible'));
  if (hiddenFrag) {
    hiddenFrag.classList.add('visible');
    const visCount = s.querySelectorAll('.frag.visible').length;
    const animName = s.getAttribute('data-anim');
    if (animName && anims[animName]) {
      anims[animName](visCount, 'step');
    }
    return;
  }
  if (curSlide < totalSlides - 1) {
    curSlide++;
    updateUI('forward');
  }
}

function prev() {
  const s = slides[curSlide];
  const frags = getFrags(s);
  const visibleNonInitial = frags.filter(f => f.classList.contains('visible') && f.dataset.initial !== 'true');
  if (visibleNonInitial.length > 0) {
    visibleNonInitial[visibleNonInitial.length - 1].classList.remove('visible');
    const visCount = s.querySelectorAll('.frag.visible').length;
    const animName = s.getAttribute('data-anim');
    if (animName && anims[animName]) {
      anims[animName](visCount, 'step');
    }
    return;
  }
  if (curSlide > 0) {
    curSlide--;
    updateUI('backward');
  }
}

window.addEventListener('keydown', (e) => {
  if (e.key === 'ArrowRight' || e.key === ' ' || e.key === 'PageDown') {
    e.preventDefault();
    next();
  } else if (e.key === 'ArrowLeft' || e.key === 'PageUp' || e.key === 'Backspace') {
    e.preventDefault();
    prev();
  } else if (e.key === 'n' || e.key === 'N') {
    notesPane.classList.toggle('visible');
  } else if (e.key === 'f' || e.key === 'F') {
    if (!document.fullscreenElement) {
      document.documentElement.requestFullscreen();
    } else {
      document.exitFullscreen();
    }
  }
});

// INTERACTIVIDAD EN SONDEO (SIN PISTA PREVIA)
document.querySelectorAll('.quiz-opt').forEach(opt => {
  opt.addEventListener('click', () => {
    document.querySelectorAll('.quiz-opt').forEach(o => {
      if (o.dataset.opt === 'B') o.classList.add('revealed-right');
      else o.classList.add('revealed-wrong');
    });
  });
});

// TEMPORIZADORES DE RETOS (10 MINUTOS)
const timers = {};
function startTimer(id, durationSeconds) {
  if (timers[id]) return;
  let remaining = durationSeconds;
  const el = document.getElementById(id);
  timers[id] = setInterval(() => {
    remaining--;
    if (remaining <= 0) {
      clearInterval(timers[id]);
      timers[id] = null;
      el.textContent = "00:00";
      el.style.color = "#ff4444";
      return;
    }
    const m = Math.floor(remaining / 60).toString().padStart(2, '0');
    const s = (remaining % 60).toString().padStart(2, '0');
    el.textContent = `${m}:${s}`;
  }, 1000);
}

function resetTimer(id, durationSeconds) {
  if (timers[id]) {
    clearInterval(timers[id]);
    timers[id] = null;
  }
  const el = document.getElementById(id);
  const m = Math.floor(durationSeconds / 60).toString().padStart(2, '0');
  const s = (durationSeconds % 60).toString().padStart(2, '0');
  el.textContent = `${m}:${s}`;
  el.style.color = "var(--coral)";
}

updateUI();
</script>
</body>
</html>
'''

with open(OUTPUT_HTML, "w", encoding="utf-8") as f:
    f.write(html_code)

print("¡HTML optimizado generado con éxito!")
