// Acceso a navegador del sistema (Playwright/Chromium) para el Deep Research y el QA.
// Uso:
//   node tools/browse.mjs open "<url>" [maxChars]  → abre y extrae título + texto (verificar fuentes)
//   node tools/browse.mjs pat "<numero>"           → PATENTE: metadatos + PLIEGO DE REIVINDICACIONES COMPLETO
//   node tools/browse.mjs gp "<query>" [PAIS]      → busca en Google Patents, lista resultados
//   node tools/browse.mjs scholar "<query>"        → busca en Google Académico (puede bloquear bots)
// Imprime JSON/markdown a stdout. Pensado para que un agente lo invoque vía Bash.
//
// REGLA DE HONESTIDAD: si el texto se trunca, la salida lo declara en `truncado` y `chars_totales`.
// Nunca se recorta en silencio: un pliego de claims cortado hace juzgar alcance sobre un documento incompleto.
// Para leer reivindicaciones usar SIEMPRE el modo `pat`, que no recorta el pliego.
import { chromium } from 'playwright';

const [mode, arg] = [process.argv[2], process.argv[3]];
const MAX_DEFAULT = 200000;   // antes 6000: truncaba pliegos de claims sin avisar
const UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 ' +
           '(KHTML, like Gecko) Chrome/124.0 Safari/537.36';

async function withPage(fn) {
  const browser = await chromium.launch();
  const ctx = await browser.newContext({ userAgent: UA, locale: 'es-CL' });
  const page = await ctx.newPage();
  try { return await fn(page); }
  finally { await browser.close(); }
}

async function open(url) {
  const max = Number(process.argv[4]) || MAX_DEFAULT;
  return withPage(async (page) => {
    const resp = await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 45000 });
    await page.waitForTimeout(1500);
    const status = resp ? resp.status() : 0;
    const title = await page.title().catch(() => '');
    const text = await page.evaluate(() => {
      const el = document.querySelector('main, article') || document.body;
      return (el.innerText || '').replace(/\n{3,}/g, '\n\n').trim();
    }).catch(() => '');
    const truncado = text.length > max;
    console.log(JSON.stringify({
      url, finalUrl: page.url(), status, title,
      chars_totales: text.length, truncado,
      ...(truncado ? { aviso: `TRUNCADO a ${max} de ${text.length} caracteres. Reintenta con un límite mayor: browse.mjs open "<url>" ${text.length + 1000}` } : {}),
      text: truncado ? text.slice(0, max) : text,
    }, null, 2));
  });
}

// Patente: metadatos + PLIEGO DE REIVINDICACIONES COMPLETO, sin recorte.
// Distingue lo que la patente REIVINDICA (claims → alcance de infracción) de lo que
// DIVULGA (descripción → destruye novedad aunque esté expirada).
async function patente(num) {
  const id = String(num).trim().toUpperCase().replace(/\s+/g, '');
  return withPage(async (page) => {
    const url = `https://patents.google.com/patent/${encodeURIComponent(id)}/en`;
    const resp = await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 45000 });
    const status = resp ? resp.status() : 0;
    await page.waitForTimeout(3000);
    const d = await page.evaluate(() => {
      const txt = (sel) => { const n = document.querySelector(sel); return n ? (n.innerText || '').trim() : ''; };
      const meta = (name) => { const n = document.querySelector(`meta[name="${name}"]`); return n ? n.content.trim() : ''; };
      const dd = (label) => {
        for (const n of document.querySelectorAll('dt')) {
          if ((n.innerText || '').trim().toLowerCase() === label.toLowerCase()) {
            const v = n.nextElementSibling; if (v) return (v.innerText || '').trim();
          }
        }
        return '';
      };
      const eventos = Array.from(document.querySelectorAll('tr.event, .event'))
        .map((n) => (n.innerText || '').replace(/\s*\n+\s*/g, ' ').trim()).filter(Boolean).slice(0, 60);
      // La primera fila de eventos trae la línea de países de la familia (p.ej. "2003 US DE MX ... 2004 ZA").
      const familiaLinea = eventos.find((t) => /^\d{4}\s+([A-Z]{2}\s+){2,}/.test(t)) || '';
      const paises = Array.from(new Set((familiaLinea.match(/\b[A-Z]{2}\b/g) || [])));
      const pick = (re) => { const e = eventos.find((t) => re.test(t)); return e || ''; };
      const body = (document.body.innerText || '');
      const mStatus = body.match(/Status\s*\n?\s*(Active|Expired[^\n]*|Withdrawn[^\n]*|Ceased[^\n]*|Abandoned[^\n]*|Pending|Not-in-force[^\n]*)/i);
      return {
        titulo: meta('DC.title') || txt('h1#title') || document.title,
        titular_actual: dd('Current Assignee'),
        titular_original: meta('DC.contributor') || dd('Original Assignee') || dd('Assignee'),
        inventor: meta('DC.creator') || dd('Inventor'),
        prioridad: (pick(/Priority (to|claimed)|Priority to/i).match(/^\d{4}-\d{2}-\d{2}/) || [''])[0] || meta('citation_patent_priority_date'),
        publicacion: meta('DC.date') || (pick(/Publication of/i).match(/^\d{4}-\d{2}-\d{2}/) || [''])[0],
        concesion: (pick(/granted/i).match(/^\d{4}-\d{2}-\d{2}/) || [''])[0],
        estado_legal: (mStatus ? mStatus[1].trim() : '') || dd('Status'),
        anticipada_expiracion: (pick(/Anticipated expiration|Expiration/i) || ''),
        familia_paises: paises,
        familia_linea: familiaLinea,
        abstract: txt('abstract') || txt('.abstract') || meta('DC.description'),
        claims: txt('section#claims') || txt('.claims') || txt('#claims'),
        descripcion: txt('section#description') || txt('.description') || txt('#description'),
        eventos_legales: eventos,
      };
    }).catch(() => ({}));
    const claims = d.claims || '';
    // Google Patents deja el andamiaje «Claims ()» aunque no exponga el pliego (típico en publicaciones
    // nacionales, p.ej. CL). El encabezado «Claims (N)» es la fuente fiable del conteo: los documentos US
    // numeran cada reivindicación en línea, pero los EP no las numeran y solo declaran N en la cabecera.
    const mCab = claims.match(/Claims\s*\((\d*)\)/);
    const nCabecera = mCab && mCab[1] ? Number(mCab[1]) : 0;
    const nNumeradas = (claims.match(/^\s*\d+\s*\./gm) || []).length;
    const nReivindicaciones = Math.max(nCabecera, nNumeradas);
    // Cuerpo real = lo que queda al sacar el andamiaje de la página.
    const cuerpo = claims.replace(/Claims\s*\(\d*\)/, '').replace(/Hide Dependent|translated from/g, '').trim();
    const sinPliego = nReivindicaciones === 0 || cuerpo.length < 120;
    const paises = d.familia_paises || [];
    console.log(JSON.stringify({
      engine: 'google-patents-doc', patente: id, url, status,
      titulo: d.titulo,
      // OJO: el titular ACTUAL puede diferir del solicitante original (cesiones).
      titular_actual: d.titular_actual, titular_original: d.titular_original,
      inventor: d.inventor,
      fecha_prioridad: d.prioridad, fecha_publicacion: d.publicacion, fecha_concesion: d.concesion,
      estado_legal: d.estado_legal, anticipada_expiracion: d.anticipada_expiracion,
      familia_paises: paises,
      tiene_miembro_chileno: paises.includes('CL'),
      familia_linea: d.familia_linea,
      eventos_legales: d.eventos_legales,
      abstract: d.abstract,
      claims_chars: claims.length,
      n_reivindicaciones: nReivindicaciones,
      claims_vacios: sinPliego,
      ...(sinPliego ? { aviso: 'SIN PLIEGO DE REIVINDICACIONES EXPUESTO (0 reivindicaciones numeradas; el texto que sigue es solo andamiaje de la página). Frecuente en publicaciones nacionales (p.ej. CL): Google Patents muestra solo el resumen. Sabes qué DIVULGA, no qué RECLAMA — NO afirmes alcance de infracción con esto; para el alcance real hace falta el registro nacional (INAPI), paso manual.' } : {}),
      claims,                       // COMPLETO, sin recorte
      descripcion_chars: (d.descripcion || '').length,
      descripcion: d.descripcion,   // COMPLETA: cuenta como divulgación para novedad
    }, null, 2));
  });
}

async function googlePatents(q) {
  // arg puede traer país al final: gp "<query>" CL  → process.argv[4]
  const pais = (process.argv[4] || '').toUpperCase();
  return withPage(async (page) => {
    let url = 'https://patents.google.com/?q=' + encodeURIComponent(q) + '&num=15';
    if (pais) url += '&country=' + pais;   // p.ej. CL = patentes con publicación chilena
    await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 45000 });
    await page.waitForTimeout(3500); // resultados cargan por JS
    const items = await page.evaluate(() => {
      const out = [];
      document.querySelectorAll('search-result-item').forEach((n) => {
        const t = n.innerText?.trim();
        // Filtra ruido de UI; conserva filas con número de patente (p.ej. WO2023..., US10..., CL...).
        if (t && t.length > 20 && /[A-Z]{2}\d{5,}/.test(t)) out.push(t.replace(/\n{2,}/g, ' | ').slice(0, 300));
      });
      return out.slice(0, 15);
    });
    console.log(JSON.stringify({ engine: 'google-patents', query: q, pais: pais || 'todos', n: items.length, items }, null, 2));
  });
}

// Registros oficiales bot-protegidos: intentamos y reportamos HONESTAMENTE.
const REGISTROS = {
  espacenet: { url: (q) => 'https://worldwide.espacenet.com/patent/search?q=' + encodeURIComponent(q),
               via: 'EPO Open Patent Services (OPS) — API REST con registro/OAuth gratuito' },
  inapi: { url: () => 'https://buscadorpatentes.inapi.cl/UI/MainSearch.aspx',
           via: 'Búsqueda manual en buscadorpatentes.inapi.cl (sin API pública)' },
  patentscope: { url: (q) => 'https://patentscope.wipo.int/search/en/result.jsf?query=' + encodeURIComponent(q),
                 via: 'WIPO PatentScope manual o su API de servicios' },
};

async function registro(engine, q) {
  const cfg = REGISTROS[engine];
  if (!cfg) { console.log(JSON.stringify({ error: `registro desconocido: ${engine}` })); return; }
  return withPage(async (page) => {
    let status = 0, bloqueado = false, motivo = '';
    try {
      const r = await page.goto(cfg.url(q), { waitUntil: 'domcontentloaded', timeout: 45000 });
      status = r ? r.status() : 0;
      await page.waitForTimeout(4000);
      const t = await page.evaluate(() => (document.body.innerText || '').slice(0, 400));
      bloqueado = status >= 400 || /security verification|not a bot|Cloudflare|Forbidden|captcha|valid user/i.test(t);
      motivo = bloqueado ? (status >= 400 ? `HTTP ${status}` : 'anti-bot (Cloudflare/captcha)') : 'accesible';
    } catch (e) { bloqueado = true; motivo = e.message; }
    // Honestidad: estos registros NO se pueden buscar/extraer de forma automática
    // (anti-bot o formulario). Aunque la landing cargue, NO declaramos 'cubierto'.
    const cobertura = bloqueado ? 'no_accesible' : 'requiere_manual';
    console.log(JSON.stringify({
      engine, query: q, status, cargo_landing: !bloqueado, cobertura, motivo,
      recomendacion: `Búsqueda/extracción automática no disponible (${bloqueado ? 'anti-bot' : 'formulario, sin API libre'}). `
        + `Vía oficial: ${cfg.via}. Para cobertura de patentes usar Google Patents (gp), que agrega familias EP/WO/US/CN/CL.`,
    }, null, 2));
  });
}

async function scholar(q) {
  return withPage(async (page) => {
    const url = 'https://scholar.google.com/scholar?q=' + encodeURIComponent(q);
    await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 45000 });
    await page.waitForTimeout(2000);
    const blocked = (await page.content()).toLowerCase().includes('unusual traffic');
    const items = await page.evaluate(() => Array.from(document.querySelectorAll('.gs_ri h3'))
      .map((h) => h.innerText.trim()).slice(0, 12));
    console.log(JSON.stringify({ engine: 'scholar', query: q, blocked, n: items.length, items }, null, 2));
  });
}

const run = {
  open, scholar,
  pat: patente,                                       // pat "<numero>" → claims COMPLETOS
  gp: googlePatents,                                  // gp "<query>" [PAIS]  (p.ej. CL)
  espacenet: (q) => registro('espacenet', q),         // intenta + reporta honesto
  inapi: (q) => registro('inapi', q),
  patentscope: (q) => registro('patentscope', q),
};
if (!run[mode] || !arg) {
  console.error('Uso: node tools/browse.mjs <open|pat|gp|scholar|espacenet|inapi|patentscope> "<url|query|numero>" [maxChars para open · PAIS para gp]\n'
    + '  pat "<numero>"  → metadatos + pliego de reivindicaciones COMPLETO (usar SIEMPRE para juzgar alcance)');
  process.exit(2);
}
run[mode](arg).catch((e) => { console.log(JSON.stringify({ error: e.message })); process.exit(1); });
