This document serves as the **single source of truth** for the Salva Mi Máquina website architecture, content strategy, and design guidelines. It ensures consistency across all development, content creation, and marketing efforts.

**Use this codex when:**
- Developing new features or pages
- Writing or editing content
- Making SEO decisions
- Designing UI/UX elements
- Onboarding new team members

---

## 📋 Table of Contents

1. [Brand Overview](#-brand-overview)
2. [Website Architecture](#-website-architecture)
3. [Page 1: Home (Inicio) - B2C Repair](#-page-1-home-inicio---b2c-repair)
4. [Page 2: Empresas - B2B Leasing](#-page-2-empresas---b2b-leasing)
5. [SEO Strategy](#-seo-strategy)
6. [Design System](#-design-system)
7. [Content Guidelines](#-content-guidelines)
8. [Technical Requirements](#-technical-requirements)
9. [Quality Checklist](#-quality-checklist)

---

## 🏢 Brand Overview

### Brand Statement

```
Salva equips and repairs Apple devices in Panama 
with the same standards as an internal technical team.
```

### Brand Attributes

| Attribute | Description |
|-----------|-------------|
| **Specialization** | Apple-exclusive (no Android, no generic electronics) |
| **Market** | Panama (local focus is non-negotiable) |
| **Services** | B2C Repair + B2B Leasing |
| **Tone** | Professional, calm, competent |
| **Differentiator** | Operational excellence, not marketing hype |

### What Salva IS

- ✅ Apple specialists
- ✅ Local Panama experts
- ✅ Transparent and process-driven
- ✅ Reliable technical partners

### What Salva IS NOT

- ❌ A generic electronics repair shop
- ❌ A discount/budget service
- ❌ An aggressive sales organization
- ❌ A faceless corporation

---

## 🏗 Website Architecture

### Site Map

```
salvamimaquina.com/
│
├── / (Home - Inicio)
│   └── Purpose: B2C Apple Repair
│
├── /empresas
│   └── Purpose: B2B Apple Leasing
│
├── /catalogo
│   └── Purpose: Equipment catalog
│
├── /ubicaciones
│   └── Purpose: Store locations
│
└── /contacto
    └── Purpose: Contact information
```

### Page Role Matrix

| Page | Audience | Intent | Conversion Goal | Emotional Target |
|------|----------|--------|-----------------|------------------|
| **Home** | Individuals | Repair my device | WhatsApp / Visit | Calm, Trust |
| **Empresas** | Businesses | Equip my team | Quote Request | Control, Relief |

### Critical Rule: No Cannibalization

```
⚠️ NEVER mix B2C and B2B content on the same page.
⚠️ NEVER use repair keywords on Empresas.
⚠️ NEVER use leasing keywords on Home.
```

---

## 🏠 Page 1: Home (Inicio) - B2C Repair

### Page Identity

| Property | Value |
|----------|-------|
| **URL** | `salvamimaquina.com/` |
| **Title Tag** | `Reparación Apple en Panamá - iPhone, MacBook, iPad | Salva Mi Máquina` |
| **Primary Goal** | Convert visitors to repair customers |
| **Secondary Goal** | Establish local SEO dominance |

### Screenshot Reference

![Home Page](screenshots/home-repair.png)

*Current implementation of the Home page showing repair services focus*

---

### SEO Configuration

#### Target Keywords

| Priority | Keyword | Search Intent | Volume Est. |
|----------|---------|---------------|-------------|
| 🔴 High | `reparación iPhone Panamá` | Transactional | High |
| 🔴 High | `reparación MacBook Panamá` | Transactional | Medium |
| 🔴 High | `servicio técnico Apple Panamá` | Commercial | Medium |
| 🟡 Medium | `arreglar iPad Panamá` | Transactional | Low |
| 🟡 Medium | `reparación Apple Watch Panamá` | Transactional | Low |
| 🟢 Low | `cambio pantalla iPhone Panamá` | Transactional | Medium |

#### Keywords to AVOID on This Page

```diff
- leasing
- empresas
- corporativo
- alquiler equipos
- flotas
- B2B
```

---

### Target Audience

#### Primary Personas

**1. The Stressed Professional**
```yaml
Age: 25-45
Device: MacBook Pro / iPhone
Situation: Device broke, needs it for work
Mindset: "I need this fixed NOW but I don't want to be scammed"
Decision Speed: Fast (same day)
```

**2. The Careful Student**
```yaml
Age: 18-25
Device: MacBook Air / iPhone
Situation: Cracked screen, limited budget
Mindset: "Is this place legit? Can I trust them?"
Decision Speed: Medium (researches first)
```

**3. The Busy Parent**
```yaml
Age: 30-50
Device: Family iPads / iPhones
Situation: Kid broke something
Mindset: "I don't have time for this, just fix it"
Decision Speed: Fast
```

#### Audience Characteristics

- They are **stressed but rational**
- They are **not tech-illiterate**
- They **rely on their devices daily**
- They **fear being overcharged or scammed**

---

### Content Strategy

#### Core Message

> **"We repair Apple devices in Panama, cleanly, quickly, and without unnecessary complications."**

This sentence must work. Everything else supports it.

#### Hero Section Requirements

```yaml
Headline: Clear value proposition (repair + Apple + Panama)
Subheadline: Trust signals (guarantee, speed, expertise)
Primary CTA: "Solicitar diagnóstico" (WhatsApp)
Secondary CTA: "Ver ubicaciones"
Trust Badges: 
  - "+1000 clientes atendidos"
  - "6 meses de garantía"
  - "Diagnóstico en 24h"
```

#### Required Sections

| Section | Purpose | CTA |
|---------|---------|-----|
| **Hero** | Capture attention, establish credibility | WhatsApp |
| **Services Grid** | Show repair capabilities by device | None (informational) |
| **Process Steps** | Reduce anxiety, show transparency | Implicit |
| **Why Choose Us** | Differentiate from competitors | None (trust building) |
| **Locations** | Enable physical visits | WhatsApp / Map |
| **Final CTA** | Last conversion opportunity | WhatsApp |

#### Section: Services Grid

Must include:
- Reparación de iPhone
- Reparación de MacBook
- Reparación de iPad
- Reparación de Apple Watch

Each card should have:
- Device image
- Service name
- 2-3 line description
- Common repairs mentioned

#### Section: Process Steps

```
1. Diagnóstico → Evaluamos tu equipo en menos de 24 horas
2. Reparación → Técnicos especializados, piezas certificadas
3. Entrega → Recoge en sucursal o envío a domicilio
```

#### Section: Why Choose Us (Trust Signals)

| Signal | Description |
|--------|-------------|
| **6 meses de garantía** | All repairs covered |
| **Técnicos especializados** | Apple-only expertise |
| **Piezas de calidad** | Certified components |
| **Diagnóstico en 24 horas** | Fast response time |

---

### Emotional Design Goals

#### Target Emotional Journey

```
BEFORE: 😰 "My device is broken, I'm stressed"
        ↓
DURING: 😌 "These people seem professional and calm"
        ↓
AFTER:  😊 "I can trust them with my device"
```

#### Design Must Convey

| Emotion | How to Achieve |
|---------|----------------|
| **Calm** | Clean whitespace, no aggressive colors |
| **Competence** | Professional photography, clear process |
| **Trust** | Real testimonials, visible guarantees |
| **Safety** | Physical locations shown, contact easy |

#### Design Must AVOID

| Anti-Pattern | Why |
|--------------|-----|
| ❌ Red urgency banners | Creates panic, not trust |
| ❌ Countdown timers | Feels scammy |
| ❌ "LIMITED OFFER!" | Not our brand |
| ❌ Stock photos of happy people | Feels fake |

---

### Conversion Requirements

#### Primary Conversion: WhatsApp Contact

```yaml
Button Text: "Contactar por WhatsApp"
Button Color: Brand green (#25D366 or brand equivalent)
Position: Hero, Locations, Footer, Floating
Behavior: Opens WhatsApp with pre-filled message
Pre-filled Message: "Hola, necesito información sobre reparación de [DEVICE]"
```

#### Secondary Conversion: Store Visit

```yaml
Locations Section: Must show both stores
Information Required:
  - Store name (San Francisco / Bella Vista)
  - Full address
  - Phone number
  - Hours of operation
  - WhatsApp button
  - "Ver mapa" link
```

#### Conversion KPIs

| Metric | Target |
|--------|--------|
| Time to first CTA visible | < 2 seconds |
| WhatsApp click rate | > 5% |
| Bounce rate | < 50% |
| Avg. time on page | > 1 minute |

---

### Content Restrictions

#### NEVER Include on Home Page

```diff
- Leasing information or pricing
- B2B / corporate language
- "Empresas" or business-focused content
- Comparisons with traditional purchase
- Fleet management mentions
- Invoice or tax benefits for businesses
```

#### Tone Restrictions

| ❌ Don't Say | ✅ Say Instead |
|-------------|----------------|
| "¡OFERTA LIMITADA!" | "Diagnóstico gratuito incluido" |
| "Somos los #1" | "Más de 1000 clientes confían en nosotros" |
| "Precios imbatibles" | "Precios transparentes, sin sorpresas" |
| "¡Llama YA!" | "Contáctanos por WhatsApp" |

---

## 🏢 Page 2: Empresas - B2B Leasing

### Page Identity

| Property | Value |
|----------|-------|
| **URL** | `salvamimaquina.com/empresas` |
| **Title Tag** | `Leasing de Equipos Apple para Empresas en Panamá | Salva Mi Máquina` |
| **Primary Goal** | Generate qualified B2B quote requests |
| **Secondary Goal** | Establish authority in corporate Apple solutions |

### Screenshot Reference

![Empresas Page](screenshots/empresas-leasing.png)

*Current implementation of the Empresas page showing leasing focus*

---

### SEO Configuration

#### Target Keywords

| Priority | Keyword | Search Intent | Volume Est. |
|----------|---------|---------------|-------------|
| 🔴 High | `leasing MacBook empresas Panamá` | Commercial | Low-Med |
| 🔴 High | `alquiler equipos Apple corporativo` | Transactional | Low |
| 🔴 High | `renting Apple empresas Panamá` | Commercial | Low |
| 🟡 Medium | `equipos Apple para empresas` | Informational | Medium |
| 🟡 Medium | `leasing tecnológico Panamá` | Commercial | Low |

#### Keywords to AVOID on This Page

```diff
- reparación
- arreglar
- pantalla rota
- diagnóstico
- servicio técnico (in repair context)
```

---

### Target Audience

#### Primary Personas

**1. The Startup Founder**
```yaml
Company Size: 5-20 employees
Role: CEO / Founder
Situation: Scaling team, needs equipment fast
Mindset: "I want MacBooks for the team without destroying cash flow"
Decision Speed: Fast (1-2 weeks)
Budget Authority: Full
```

**2. The IT Manager**
```yaml
Company Size: 20-100 employees
Role: IT Manager / CTO
Situation: Managing device lifecycle is painful
Mindset: "I need someone else to handle this headache"
Decision Speed: Medium (1-2 months)
Budget Authority: Partial (needs approval)
```

**3. The Operations Director**
```yaml
Company Size: 50-200 employees
Role: COO / Operations
Situation: Looking for operational efficiency
Mindset: "Leasing makes more financial sense than buying"
Decision Speed: Slow (2-3 months)
Budget Authority: High
```

**4. The Finance Lead**
```yaml
Company Size: Any
Role: CFO / Finance Director
Situation: Evaluating capex vs opex
Mindset: "Show me the numbers, not the features"
Decision Speed: Slow (needs analysis)
Budget Authority: Full
```

#### Audience Characteristics

- They want **predictability, not excitement**
- They think in **budgets and timelines**
- They value **operational efficiency**
- They need to **justify decisions to others**

---

### Content Strategy

#### Core Message

> **"We equip businesses in Panama with Apple devices, without locking cash or complicating operations."**

#### Hero Section Requirements

```yaml
Headline: Value proposition (equip + business + no cash lock)
Subheadline: Key benefits (warranty, renewal, support)
Primary CTA: "Solicitar cotización"
Trust Badges: Company logos (clients)
Visual: Professional workspace with Apple devices
```

#### Required Sections

| Section | Purpose | CTA |
|---------|---------|-----|
| **Hero** | Establish B2B positioning | Quote request |
| **Benefits Grid** | Show leasing advantages | None |
| **Equipment Catalog** | Display available devices | Implicit |
| **New vs Refurbished** | Address budget concerns | None |
| **Comparison Table** | Differentiate from alternatives | None |
| **Process Steps** | Show simplicity | Implicit |
| **Client Logos** | Social proof | None |
| **Technical Service CTA** | Cross-sell repair | Link to Home |
| **Final CTA** | Last conversion opportunity | Quote request |

---

#### Section: Benefits Grid

```yaml
Benefits:
  - title: "Sin inversión inicial"
    description: "Equipa tu empresa sin comprometer capital"
    icon: dollar-off
    
  - title: "Garantía total incluida"
    description: "Cobertura completa durante todo el contrato"
    icon: shield-check
    
  - title: "Renovación cada 2 años"
    description: "Tecnología actualizada, sin equipos obsoletos"
    icon: refresh
    
  - title: "Soporte prioritario"
    description: "Atención dedicada para empresas"
    icon: headset
```

#### Section: Equipment Catalog

| Device | Use Case | Target User |
|--------|----------|-------------|
| MacBook Pro | Power users, developers | Tech teams |
| MacBook Air | General productivity | Most employees |
| iMac 24" | Fixed workstations | Designers, reception |
| iPad Pro | Field work, presentations | Sales, executives |
| Mac Mini | Server, kiosk, dev | IT, specialized |
| Studio Display | Professional display | Designers, video |

#### Section: New vs Refurbished

```yaml
New Equipment:
  - Configuración de fábrica
  - Prioridad en stock original
  - Última generación disponible

Refurbished Equipment:
  - Certificados grado A+
  - Hasta 30% ahorro vs nuevo
  - Misma garantía y soporte
  - Opción eco-responsable
```

#### Section: Comparison Table

| Feature | Direct Purchase | Traditional Leasing | Salva Mi Máquina |
|---------|-----------------|---------------------|------------------|
| Proceso claro y directo | ❌ | ❌ | ✅ |
| Mejora la gestión de flujo de caja | ❌ | ✅ | ✅ |
| Equipos siempre actualizados | ❌ | ❌ | ✅ |
| Garantía y asistencia de alta calidad | ❌ | ❌ | ✅ |
| Equipo centralizado para gestión de flotas | ❌ | ❌ | ✅ |

#### Section: Process Steps

```yaml
Steps:
  1:
    title: "Cotización"
    description: "Cuéntanos qué necesitas y recibes un presupuesto en 24h"
    
  2:
    title: "Configuración"
    description: "Elegimos equipos ideales y configuraciones según tus necesidades"
    
  3:
    title: "Entrega"
    description: "Entregamos en tu oficina, configurados y listos con MDM"
    
  4:
    title: "Soporte"
    description: "Durante todo el contrato, resolvemos cualquier incidencia"
```

#### Section: Client Logos

Display recognizable company logos:
- R&R
- La Prensa
- BOSCH
- Shell
- Tetra Pak
- SUEZ

*Note: Only display logos with permission*

---

### Emotional Design Goals

#### Target Emotional Journey

```
BEFORE: 🤔 "Managing devices is a headache"
        ↓
DURING: 😮 "This actually makes operational sense"
        ↓
AFTER:  😌 "They've thought of everything"
```

#### Design Must Convey

| Emotion | How to Achieve |
|---------|----------------|
| **Control** | Clear pricing, predictable process |
| **Stability** | Established client logos, professional imagery |
| **Intelligence** | Comparison tables, clear ROI |
| **Relief** | "We handle everything" messaging |

#### Design Must AVOID

| Anti-Pattern | Why |
|--------------|-----|
| ❌ Broken device imagery | Wrong page, wrong emotion |
| ❌ Urgency language | B2B decisions take time |
| ❌ Playful/casual tone | Not appropriate for operations |
| ❌ Apple fanboy aesthetics | This is business, not lifestyle |

---

### Conversion Requirements

#### Primary Conversion: Quote Request

```yaml
Button Text: "Solicitar cotización por WhatsApp"
Alternative: "Solicitar cotización" (form)
Button Color: Brand green
Position: Hero, After comparison, Footer
Behavior: Opens WhatsApp or quote form
Pre-filled Message: "Hola, me interesa una cotización de leasing para [COMPANY]"
```

#### Cross-Sell: Technical Service

```yaml
Section: "¿También necesitas servicio técnico?"
Purpose: Connect B2B clients to repair services
CTA: "Conocer servicio para empresas"
Link: Separate B2B repair page or contact
```

#### Conversion KPIs

| Metric | Target |
|--------|--------|
| Quote requests / month | Track baseline, improve 10% |
| Time to quote response | < 24 hours |
| Quote to contract rate | > 20% |
| Average contract value | Track and grow |

---

### Content Restrictions

#### NEVER Include on Empresas Page

```diff
- Individual repair services
- Cracked screen imagery
- Emergency/urgent language
- "Fix your device" messaging
- Consumer pricing
- Walk-in service mentions
```

#### Tone Restrictions

| ❌ Don't Say | ✅ Say Instead |
|-------------|----------------|
| "¡Tu iPhone roto!" | (Don't mention repairs at all) |
| "Emergencia técnica" | "Soporte prioritario para empresas" |
| "Precios increíbles" | "Presupuestos claros y predecibles" |
| "¡Llámanos ya!" | "Solicita una cotización" |

---

## 🔍 SEO Strategy

### Keyword Segmentation

#### Absolute Rule

```
🚫 NEVER mix B2C and B2B keywords on the same page
```

#### Keyword Ownership

| Page | Owns These Keywords | Does NOT Use |
|------|---------------------|--------------|
| **Home** | repair, fix, service, broken, screen | leasing, rental, business, corporate |
| **Empresas** | leasing, rental, business, fleet, corporate | repair, fix, broken, screen |

### Local SEO Requirements

#### Both Pages Must Include

- "Panamá" in title tag
- "Panamá" in H1
- Physical addresses
- Local phone numbers
- Google Business Profile links

#### Schema Markup

```json
// Home Page
{
  "@type": "LocalBusiness",
  "name": "Salva Mi Máquina",
  "description": "Servicio técnico especializado en Apple",
  "@type": "Service",
  "serviceType": "Apple Device Repair"
}

// Empresas Page
{
  "@type": "LocalBusiness", 
  "name": "Salva Mi Máquina",
  "@type": "Service",
  "serviceType": "Apple Equipment Leasing"
}
```

### Internal Linking Strategy

```
Home ←→ Empresas: Minimal, only in designated cross-sell sections
Home → Ubicaciones: Strong linking
Home → Catálogo: Moderate linking
Empresas → Catálogo: Strong linking
```

---

## 🎨 Design System

### Color Palette

| Color | Hex | Usage |
|-------|-----|-------|
| **Primary Green** | `#00C853` (adjust to brand) | CTAs, accents |
| **Dark Text** | `#1A1A1A` | Headlines, body |
| **Gray Text** | `#666666` | Secondary text |
| **Light Background** | `#F8F9FA` | Section backgrounds |
| **White** | `#FFFFFF` | Cards, main background |

### Typography

```css
/* Headlines */
font-family: 'Inter', -apple-system, sans-serif;
font-weight: 600-700;

/* Body */
font-family: 'Inter', -apple-system, sans-serif;
font-weight: 400;
line-height: 1.6;
```

### Spacing System

```css
--space-xs: 4px;
--space-sm: 8px;
--space-md: 16px;
--space-lg: 24px;
--space-xl: 32px;
--space-2xl: 48px;
--space-3xl: 64px;
```

### Component Standards

#### Buttons

```yaml
Primary CTA:
  background: Primary Green
  color: White
  padding: 12px 24px
  border-radius: 8px
  
Secondary CTA:
  background: White
  color: Dark Text
  border: 1px solid #E0E0E0
  padding: 12px 24px
  border-radius: 8px
```

#### Cards

```yaml
Background: White
Border: 1px solid #E8E8E8
Border-radius: 12px
Padding: 24px
Shadow: 0 2px 8px rgba(0,0,0,0.08)
```

---

## 📝 Content Guidelines

### Voice & Tone

#### Brand Voice Attributes

| Attribute | Level | Description |
|-----------|-------|-------------|
| Professional | High | We know what we're doing |
| Calm | High | No panic, no pressure |
| Clear | High | No jargon, no confusion |
| Friendly | Medium | Approachable, not cold |
| Technical | Low | Accessible to everyone |

#### Tone by Context

| Context | Tone |
|---------|------|
| Hero headlines | Confident, clear |
| Service descriptions | Informative, reassuring |
| CTAs | Inviting, not pushy |
| Error messages | Helpful, understanding |
| Support | Patient, solution-focused |

### Writing Rules

#### DO

- ✅ Use active voice
- ✅ Keep sentences short
- ✅ Lead with benefits
- ✅ Use "tú" (informal you)
- ✅ Include specific numbers when possible
- ✅ Write for scanning (clear headers, short paragraphs)

#### DON'T

- ❌ Use superlatives without proof
- ❌ Write walls of text
- ❌ Use technical jargon
- ❌ Make promises you can't keep
- ❌ Use ALL CAPS or excessive exclamation!!!
- ❌ Sound desperate or pushy

### Proof Points

Only claim what you can prove:

| ✅ Claimable | ❌ Not Claimable |
|-------------|-----------------|
| "+1000 clientes atendidos" (if true) | "Los mejores de Panamá" |
| "6 meses de garantía" (policy) | "Calidad incomparable" |
| "Diagnóstico en 24 horas" (SLA) | "Servicio más rápido" |
| "2 ubicaciones en Panamá" (fact) | "Líderes del mercado" |

---

## ⚙️ Technical Requirements

### Performance Targets

| Metric | Target | Tool |
|--------|--------|------|
| LCP (Largest Contentful Paint) | < 2.5s | PageSpeed |
| FID (First Input Delay) | < 100ms | PageSpeed |
| CLS (Cumulative Layout Shift) | < 0.1 | PageSpeed |
| Mobile Score | > 90 | PageSpeed |
| Desktop Score | > 95 | PageSpeed |

### Responsive Breakpoints

```css
/* Mobile First */
@media (min-width: 640px) { /* sm */ }
@media (min-width: 768px) { /* md */ }
@media (min-width: 1024px) { /* lg */ }
@media (min-width: 1280px) { /* xl */ }
```

### WhatsApp Integration

```javascript
// WhatsApp link format
const whatsappLink = `https://wa.me/507XXXXXXXX?text=${encodeURIComponent(message)}`;

// Pre-filled messages
const repairMessage = "Hola, necesito información sobre reparación de mi equipo Apple";
const quoteMessage = "Hola, me interesa una cotización de leasing para mi empresa";
```

### Analytics Requirements

Track these events:

```javascript
// Home Page
- 'cta_click_whatsapp_hero'
- 'cta_click_whatsapp_locations'
- 'cta_click_whatsapp_footer'
- 'view_map_click'
- 'service_card_click'

// Empresas Page
- 'cta_click_quote_hero'
- 'cta_click_quote_footer'
- 'equipment_card_click'
- 'comparison_table_view'
- 'cross_sell_repair_click'
```

---

## ✅ Quality Checklist

### Before Publishing Home Page

```markdown
## SEO
- [ ] Title tag includes "Reparación Apple Panamá"
- [ ] H1 includes primary keyword
- [ ] No B2B/leasing keywords present
- [ ] Meta description is compelling and under 160 chars
- [ ] All images have alt text

## Content
- [ ] Core message is clear within 5 seconds
- [ ] All 4 device repair services shown
- [ ] Process steps are clear
- [ ] Both locations listed with full info
- [ ] Trust signals (guarantee, clients, speed) visible

## Conversion
- [ ] WhatsApp CTA in hero
- [ ] WhatsApp CTA in locations
- [ ] WhatsApp CTA in footer
- [ ] All WhatsApp links work
- [ ] Pre-filled messages are correct

## Design
- [ ] Mobile responsive
- [ ] No broken images
- [ ] Consistent spacing
- [ ] Brand colors correct
- [ ] No urgency/panic design elements

## Technical
- [ ] PageSpeed score > 90 mobile
- [ ] All links work
- [ ] Analytics tracking live
- [ ] WhatsApp floating button works
```

### Before Publishing Empresas Page

```markdown
## SEO
- [ ] Title tag includes "Leasing Apple Empresas Panamá"
- [ ] H1 includes primary keyword
- [ ] No B2C/repair keywords present
- [ ] Meta description targets business audience

## Content
- [ ] Core message is clear within 5 seconds
- [ ] All equipment options shown
- [ ] New vs Refurbished section present
- [ ] Comparison table accurate
- [ ] Process steps clear
- [ ] Client logos displayed (with permission)

## Conversion
- [ ] Quote CTA in hero
- [ ] Quote CTA after comparison
- [ ] Quote CTA in footer
- [ ] Cross-sell to repair service present
- [ ] All CTAs work

## Design
- [ ] Mobile responsive
- [ ] Professional, operational tone in visuals
- [ ] No broken device imagery
- [ ] No urgency elements
- [ ] Consistent with Home page design system

## Technical
- [ ] PageSpeed score > 90 mobile
- [ ] All links work
- [ ] Analytics tracking live
- [ ] Form submissions working (if applicable)
```

---

## 📚 Appendix

### Glossary

| Term | Definition |
|------|------------|
| **B2C** | Business-to-Consumer (individual customers) |
| **B2B** | Business-to-Business (company customers) |
| **CTA** | Call-to-Action (button or link prompting action) |
| **Leasing** | Equipment rental with support and renewal |
| **MDM** | Mobile Device Management (fleet management software) |
| **LCP** | Largest Contentful Paint (performance metric) |
| **Cannibalization** | When pages compete for the same keywords |

### Related Documents

- Brand Guidelines (if exists)
- Content Calendar
- SEO Keyword Research
- Analytics Dashboard

### Version History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | Jan 2025 | Team | Initial codex |

---

## 📞 Questions?

If anything in this codex is unclear or needs updating, contact the project lead.

**Remember:** When in doubt, ask yourself:
- *"Does this help the user accomplish their goal?"*
- *"Does this respect the page's specific audience?"*
- *"Does this align with the brand's calm, competent tone?"*

---

*© 2025 Salva Mi Máquina. This codex is internal documentation.*
