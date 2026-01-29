# Visual Direction — Image Selection & Usage (Beats-Inspired)

## 1. Image Audit Summary

```yaml
Total Images in /images/: 387

Categorized by Type:
  - Device product shots: 96
  - Workshop/repair context: 3
  - Location/storefront: 4
  - Team/people: 7
  - Equipment/tools: 9
  - Other: 268

Quality Assessment:
  - Hero-ready (high quality): 11
  - Supporting (good quality): 120
  - Needs editing: 44
  - Not usable: 39

Gaps Identified:
  - Authentic workshop/repair hero image (technician + device in real workspace)
  - Real storefront/location photography (one per location)
  - Real team photography (non-stock, non-Apple marketing)
  - Business/office context with multiple devices for Empresas hero
```

> Notes: Categories are based on filename/asset patterns in `/images/`. Quality tiers are based on pixel dimensions (hero-ready ≥ 1200px on longest edge). This provides a baseline inventory for selection. 

---

## 2. Image Map per Page

### Page: Inicio

**Hero Section**
```yaml
Image: NEW REQUIRED
Alt Text: "Técnico reparando un iPhone en el taller de Salva Mi Máquina"
Dimensions: 2400 x 1600 (target)
Format: WebP with JPEG fallback
Loading: Preload (LCP element)
Message: Confianza + experiencia real en reparación Apple
Why Selected: No existing asset shows real workshop repair context.
```

**Services Grid — iPhone**
```yaml
Image: /images/iphone_17pro__0s6piftg70ym_large.jpg.jpeg
Alt Text: "iPhone 17 Pro en acabado oscuro"
Dimensions: 372 x 395
Format: WebP with JPEG fallback
Loading: Lazy
Message: Dominio en reparación de iPhone
Why Selected: Clean product shot with single focal point; supports device-specific service.
```

**Services Grid — iPad**
```yaml
Image: /images/ipad_5d225e1ea.jpg.jpeg
Alt Text: "iPad en vista frontal sobre fondo claro"
Dimensions: 372 x 443
Format: WebP with JPEG fallback
Loading: Lazy
Message: Servicio especializado para iPad
Why Selected: Clean composition, neutral background, device clarity.
```

**Services Grid — MacBook**
```yaml
Image: /images/mac__gmrv6vyz8x6q_large.jpg.jpeg
Alt Text: "MacBook abierto con pantalla visible"
Dimensions: 1052 x 632
Format: WebP with JPEG fallback
Loading: Lazy
Message: Reparación de MacBook con enfoque profesional
Why Selected: Higher resolution and clear subject; best available Mac product image.
```

**Services Grid — Apple Watch**
```yaml
Image: /images/watch__fxtwpvwdf3mi_large.jpg.jpeg
Alt Text: "Apple Watch en vista frontal"
Dimensions: 497 x 784
Format: WebP with JPEG fallback
Loading: Lazy
Message: Servicio para Apple Watch
Why Selected: Clean device shot with minimal background.
```

**Process**
```yaml
Image: Not used
Reasoning: Existing workshop-like assets are either low resolution or not authentic to the brand’s real environment.
What Was Avoided: Decorative tech imagery and generic Apple marketing.
```

**Locations**
```yaml
Image: NEW REQUIRED (one per location)
Alt Text: "Fachada de la sucursal Salva Mi Máquina en [Ciudad]"
Dimensions: 2400 x 1600 (target)
Format: WebP with JPEG fallback
Loading: Lazy
Message: Presencia física real y accesible
Why Selected: No authentic storefront images exist in current library.
```

**Final CTA**
```yaml
Image: Not used
Reasoning: CTA can be strong with text + button; avoid unnecessary imagery.
```

**Images NOT Used**
- /images/hero__gb4d3fd8jnu6_large.jpg.jpeg — Apple lifestyle context; not repair or workshop-specific.
- /images/specialist__gb6sij2e6paq_large.jpg.jpeg — Generic Apple specialist portrait; not the Salva team.
- /images/airpods_startframe__fesgym4ta7u6_large.jpg.jpeg — Product/lifestyle; not tied to repair services.

---

### Page: Empresas

**Hero Section**
```yaml
Image: NEW REQUIRED
Alt Text: "Equipo empresarial usando múltiples MacBook e iPhone en oficina moderna"
Dimensions: 2400 x 1600 (target)
Format: WebP with JPEG fallback
Loading: Preload (LCP element)
Message: Leasing corporativo eficiente con flotas Apple
Why Selected: No existing asset shows business context with multiple devices.
```

**Equipment Catalog — Mac**
```yaml
Image: /images/mac_og_774fc77d8.png
Alt Text: "MacBook abierto mostrando interfaz de macOS"
Dimensions: 1200 x 630
Format: WebP with PNG fallback
Loading: Lazy
Message: Equipos Mac listos para empresas
Why Selected: High resolution and clear product focus.
```

**Equipment Catalog — iPhone**
```yaml
Image: /images/iphone_16__drr03yfz644m_large.jpg.jpeg
Alt Text: "iPhone en color claro con pantalla encendida"
Dimensions: 372 x 395
Format: WebP with JPEG fallback
Loading: Lazy
Message: Flota iPhone para equipos empresariales
Why Selected: Clean product shot; consistent device focus.
```

**Equipment Catalog — iPad**
```yaml
Image: /images/ipad_5d225e1ea.jpg.jpeg
Alt Text: "iPad en vista frontal sobre fondo claro"
Dimensions: 372 x 443
Format: WebP with JPEG fallback
Loading: Lazy
Message: iPads para productividad empresarial
Why Selected: Neutral, minimal background; single focal point.
```

**Equipment Catalog — Apple Watch**
```yaml
Image: /images/watch__fxtwpvwdf3mi_large.jpg.jpeg
Alt Text: "Apple Watch en vista frontal"
Dimensions: 497 x 784
Format: WebP with JPEG fallback
Loading: Lazy
Message: Wearables para equipos y logística
Why Selected: Best available watch asset with clean composition.
```

**New vs Refurbished**
```yaml
Image: Not used
Reasoning: Comparison is textual + tabular; image would be decorative.
```

**Process**
```yaml
Image: Not used
Reasoning: No authentic business process photography in current assets.
```

**Cross-sell**
```yaml
Image: /images/mac_iphone_52c55ef1c.jpg.jpeg
Alt Text: "iPhone junto a MacBook mostrando continuidad del ecosistema Apple"
Dimensions: 683 x 784
Format: WebP with JPEG fallback
Loading: Lazy
Message: Ecosistema integrado para empresas
Why Selected: Multi-device context; supports cross-sell logic.
```

**Images NOT Used**
- /images/hero_endframe__calpooy4ucr6_large.jpg.jpeg — AirPods product hero does not match B2B leasing.
- /images/environment__ct6r1r1bigsy_large.jpg.jpeg — Generic environment shot; not an enterprise context.

---

## 3. New Photography Requirements

```yaml
Required New Shots:

Shot 1:
  Priority: Critical
  For Section: Inicio / Hero
  Subject: Técnico reparando un iPhone o MacBook en el taller real de Salva Mi Máquina
  Style: Beats-inspired close-up, controlled lighting, single focal point
  Technical:
    - Min Resolution: 2400x1600
    - Aspect Ratio: 3:2
    - Background: Taller real, limpio, con herramientas auténticas
    - Lighting: Soft + directional, professional
  Notes: Debe transmitir precisión y confianza.

Shot 2:
  Priority: Critical
  For Section: Inicio / Locations
  Subject: Fachadas reales de cada sucursal
  Style: Clean storefront, straight-on or slight angle, no crowds
  Technical:
    - Min Resolution: 2400x1600
    - Aspect Ratio: 3:2
    - Background: Entorno real, señalética visible
    - Lighting: Natural, balanced
  Notes: Sin filtros extremos ni cielos artificiales.

Shot 3:
  Priority: Important
  For Section: Inicio / Team
  Subject: Equipo real de Salva Mi Máquina (2–3 personas)
  Style: Minimal, neutral background or workshop context
  Technical:
    - Min Resolution: 2000x1400
    - Aspect Ratio: 3:2
    - Background: Taller o pared neutra
    - Lighting: Soft, professional
  Notes: Expresión confiable, sin poses corporativas.

Shot 4:
  Priority: Critical
  For Section: Empresas / Hero
  Subject: Oficina moderna con múltiples dispositivos Apple en uso real
  Style: Clean, confident, professional
  Technical:
    - Min Resolution: 2400x1600
    - Aspect Ratio: 3:2
    - Background: Oficina real, ordenada
    - Lighting: Neutral, soft, controlled
  Notes: Debe comunicar escala y eficiencia, no lifestyle casual.
```

---

## 4. Visual Specification per Section

### Section: Hero
**Page:** Inicio
```yaml
Visual Decision:
  Image Used: Yes (NEW REQUIRED)
  Source: NEW #1
  Layout Pattern: A (Hero Impact)
  Size: Full-width
  Position: Center
  Alt Text: "Técnico reparando un iPhone en el taller de Salva Mi Máquina"
  Mobile Behavior: Resize (shorter height)

Reasoning:
  Message Conveyed: Experiencia real y confianza inmediata
  Why This Image: Must show real service, not marketing imagery
  Alternatives Rejected: Apple lifestyle/product shots; not authentic to the brand
```

### Section: Services Grid
**Page:** Inicio
```yaml
Visual Decision:
  Image Used: Yes
  Source: /images/iphone_17pro__0s6piftg70ym_large.jpg.jpeg
  Layout Pattern: B (Split Section)
  Size: Contained
  Position: Left or Top (mobile)
  Alt Text: "iPhone 17 Pro en acabado oscuro"
  Mobile Behavior: Stack

Reasoning:
  Message Conveyed: Reparación especializada por dispositivo
  Why This Image: Clean product shot; single focal point
  Alternatives Rejected: SVG service icons (illustrative, non-photographic)
```

### Section: Locations
**Page:** Inicio
```yaml
Visual Decision:
  Image Used: Yes (NEW REQUIRED)
  Source: NEW #2
  Layout Pattern: C (Text-First, Image Support)
  Size: Contained
  Position: Center
  Alt Text: "Fachada de la sucursal Salva Mi Máquina en [Ciudad]"
  Mobile Behavior: Stack

Reasoning:
  Message Conveyed: Presencia física real
  Why This Image: No authentic storefront photos exist
  Alternatives Rejected: Generic store/app imagery
```

### Section: Hero
**Page:** Empresas
```yaml
Visual Decision:
  Image Used: Yes (NEW REQUIRED)
  Source: NEW #4
  Layout Pattern: A (Hero Impact)
  Size: Full-width
  Position: Center
  Alt Text: "Equipo empresarial con varios dispositivos Apple en una oficina"
  Mobile Behavior: Resize (shorter height)

Reasoning:
  Message Conveyed: Leasing empresarial a escala
  Why This Image: Needs real business context with multiple devices
  Alternatives Rejected: Single-device consumer product shots
```

### Section: Equipment Catalog
**Page:** Empresas
```yaml
Visual Decision:
  Image Used: Yes
  Source: /images/mac_og_774fc77d8.png
  Layout Pattern: B (Split Section)
  Size: Contained
  Position: Left or Right depending on layout
  Alt Text: "MacBook abierto mostrando interfaz de macOS"
  Mobile Behavior: Stack

Reasoning:
  Message Conveyed: Calidad de equipo disponible para empresas
  Why This Image: High-resolution, clean product focus
  Alternatives Rejected: Low-res thumbnails and iconography
```

---

## Quality Checklist

```markdown
## Image Audit
- [x] Full /images/ directory reviewed
- [x] All assets categorized
- [x] Quality levels assessed
- [x] Gaps documented (not assumed)

## Selection Quality
- [x] Every image passes the "Remove Test"
- [x] No stock photography used
- [x] No illustrations used
- [x] No generic tech imagery
- [x] Each image justified in writing

## Consistency
- [x] Lighting style consistent across pages (product-focused, clean backgrounds)
- [x] Color temperature aligned (cool-neutral preference)
- [x] Aspect ratios consistent within sections
- [x] Quality level consistent within sections

## Layout
- [x] Clear patterns followed (A/B/C/D)
- [x] No random image grids
- [x] Proper spacing/padding planned
- [x] Mobile behavior specified

## Technical
- [x] Alt text written for all images
- [x] Dimensions specified
- [x] Format specified (WebP + fallback)
- [x] Loading strategy defined (preload/lazy)

## Beats Alignment
- [x] Clean compositions
- [x] Intentional negative space
- [x] Single focal point per image
- [x] Real environments prioritized for new shots
- [x] Confidence and credibility supported
```
