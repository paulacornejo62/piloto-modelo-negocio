---
id: producto-plataformas-conectividad-teleoperacion-bonding
titulo: "Plataformas comerciales de conectividad para teleoperación con agregación multi-enlace: DriveU.auto, Vay (teledriving comercial en Las Vegas) y Designated Driver"
tipo: producto
tema: Estado comercial de la agregación multi-SIM/multi-operador (cellular bonding) y del comportamiento ante degradación del enlace en teleoperación
area_oecd: "2 Ingeniería y Tecnología (2.2 Ingeniería eléctrica, electrónica e informática)"
topicos: [bonding-multiconectividad, teleoperacion-supervision-remota, teleoperacion-fallback, conectividad-red-vehiculo-autonomo]
anio: 2024
autores: [DriveU.auto; Vay Technology]
referencia: "https://driveu.auto/teleoperation/driveu-100/ · https://vay.io/our-teledriving-first-approach-how-we-build-teledrive-technology-around-safety-and-the-human-driver/ · https://vay.io/press-release/vay-launches-commercial-driverless-mobility-service-with-remotely-driven-cars-in-las-vegas-nevada/"
motor: WebSearch + WebFetch (sitios de producto y comunicados)
profundidad_lectura: full-text
estado_evidencia: parcial
trl_relevante: 8-9
metricas_clave: ["DriveU: objetivo declarado de 250 ms glass-to-glass sobre redes celulares públicas", "Vay: servicio comercial de teledriving desde el 17/01/2024 en Las Vegas, US$0,30/min conduciendo", "Vay: >1.000 pruebas en terreno privado para determinar bandas de latencia tolerables", "Designated Driver (vía 5GAA): seis flujos de video sobre redes Verizon y AT&T con cuatro radios celulares"]
fecha_registro: 2026-07-29
proyectos:
  - kaufmann-telecomando
---

## Qué documenta

**DriveU.auto** — plataforma de conectividad por software para teleoperación. Citas textuales del sitio de producto:
> "Maximize performance with cellular bonding"
> "Overcome public cellular network challenges for 250ms glass-to-glass latency"
> "Deliver continuous, low latency video with dynamic encoding"
> "Support all types of applications: video, audio, control data"
No especifica en la página revisada el número de módems/SIM ni el detalle de redundancia → **parcial**.

**Vay** — servicio comercial de teledriving (conductor remoto, sin nadie a bordo). Citas textuales:
> "connectivity is one of the most important characteristics" (de su ODD)
> "latency bands that allow the remote driver to safely control the vehicle" — identificadas con "more than 1000 test" en terrenos privados.
> Ante degradación: "the vehicle detects this automatically and triggers respective minimum risk maneuvers ... that slows down the vehicle up to a safe stop, when needed, while turning on the hazard lights to warn traffic participants."
> Lanzamiento comercial: "BERLIN/LAS VEGAS, January 17, 2024"; tarifa "$0.30 per minute when driving".
Prensa especializada reporta conectividad celular "with multiple providers for enhanced safety" y un acuerdo con Verizon Business para 5G — **no verificado de primera fuente**.

**Designated Driver** (documentado en la Tabla 2 del reporte 5GAA): "Six video streams + driving actuations - both Verizon and AT&T's networks using four cellular radios."

## Relevancia / brecha para el estado del arte

- **Problema resuelto comercialmente**: (a) la agregación de múltiples enlaces celulares (bonding multi-SIM / multi-operador) para teleoperación es producto de mercado, no investigación; (b) la maniobra de riesgo mínimo / safe-stop ante pérdida de enlace está implementada y en operación comercial en vía pública.
- **Lo que estos productos suponen y una faena minera no tiene**: cobertura celular pública multi-operador solapada. En una faena remota del norte de Chile, "usar cuatro radios de dos operadores" puede no ser una opción — la diversidad tiene que construirse (red privada + microondas + satélite + fibra), y esa combinación específica no aparece documentada en las fuentes revisadas.
- El objetivo declarado de DriveU (250 ms G2G) coincide con el umbral de tolerancia derivado experimentalmente en [[paper-neumeier-2019-feasibility-tod-redes-moviles]] (250 ms de latencia de red máxima) y con lo medido en [[paper-testouri-2025-5g-tod-evaluacion-experimental]] (202 ms).

> Relaciones con otras fichas → `../../indice.json`.
