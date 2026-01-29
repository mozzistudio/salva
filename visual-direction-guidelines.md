# 📸 Visual Direction Guidelines

> **For:** Senior Visual Director / Web Designer  \
> **Project:** Salva Mi Máquina Website Redesign  \
> **Philosophy:** Visual discipline, not decoration

---

## Table of Contents

1. [Context & Constraints](#1-context--constraints)
2. [Image Library Protocol](#2-image-library-protocol)
3. [Visual Rules (Non-Negotiable)](#3-visual-rules-non-negotiable)
4. [Beats-Inspired Visual Logic](#4-beats-inspired-visual-logic)
5. [Page-Specific Visual Strategy](#5-page-specific-visual-strategy)
6. [Section-by-Section Image Framework](#6-section-by-section-image-framework)
7. [Image Selection Decision Tree](#7-image-selection-decision-tree)
8. [Technical Specifications](#8-technical-specifications)
9. [Quality Validation](#9-quality-validation)

---

## 1. Context & Constraints

### Project Context

This project redesigns the Salva Mi Máquina website with visual logic inspired by **Beats by Dre**:
- Confident, intentional imagery
- Visual proof over verbal explanation
- Premium feel through restraint, not excess

### Related Documents

| Document | Reference For |
|----------|---------------|
| `strategy.md` | Brand positioning, audience profiles |
| `beats-analysis.md` | Visual logic principles, rhythm patterns |
| `seo-architecture.md` | Content placement, section structure |
| `phase3-design-prompt.md` | Full page structure and copy |

---

### Critical Constraint: Local Image Library

```
⚠️ IMPORTANT: A LARGE IMAGE DIRECTORY exists in this project.

Location: /images/

Protocol:
├── ALWAYS check existing images first
├── PRIORITIZE reusing available assets
├── NEVER assume new sourcing without explicit request
├── NEVER suggest stock platforms
└── NEVER generate or invent images
```

### What This Document Covers

```yaml
IN SCOPE:
  - Visual direction and intent
  - Image selection logic
  - Layout integration principles
  - Quality standards

OUT OF SCOPE:
  - Specific filenames (determined during implementation)
  - Image editing/retouching specifications
  - Photography briefs for new shoots
```

---

## 2. Image Library Protocol

### Before Selecting Any Image

```
STEP 1: Review /images/ directory
STEP 2: Categorize available assets
STEP 3: Match to section requirements
STEP 4: Identify gaps (if any)
STEP 5: Document reuse decisions
```

### Image Inventory Categories

When reviewing the local library, organize by:

| Category | Examples | Priority Use |
|----------|----------|--------------|
| **Workshop/Environment** | Workspace shots, tools, setup | Trust-building sections |
| **Device Close-ups** | iPhone, MacBook, iPad, Watch | Service cards, hero |
| **Process/Action** | Hands working, repairs in progress | Process sections |
| **Team/People** | Technicians, real staff | About, trust sections |
| **Storefront/Location** | Store exterior, interior | Location sections |
| **Equipment/Fleet** | Multiple devices, business setup | Empresas page |
| **Before/After** | Repair transformations | Proof sections |

### Reuse Decision Framework

```yaml
Question: "Do we have an image that works?"

If YES and STRONG:
  → Use it. Document why.

If YES but WEAK:
  → Can it be cropped/reframed to work?
  → If yes, use it with art direction notes
  → If no, mark gap for future

If NO:
  → Document the gap clearly
  → Do NOT force a substitute
  → Section may work without image (text-only is valid)
```

---

## 3. Visual Rules (Non-Negotiable)

### Absolute Prohibitions

These are **hard rules** — no exceptions, no "just this once":

```diff
- ❌ Generic stock photography
- ❌ Illustrations or vector graphics
- ❌ Abstract visuals or patterns
- ❌ "Happy people pointing at laptops"
- ❌ Fake corporate smiles
- ❌ Handshake photos
- ❌ Diverse-team-around-table clichés
- ❌ Floating devices on gradient backgrounds
- ❌ Lens flare or artificial glow effects
- ❌ Watermarked or low-resolution images
- ❌ Obviously AI-generated imagery
```

### Why These Rules Exist

| Prohibition | Reason |
|-------------|--------|
| Stock photography | Destroys authenticity, signals "we have nothing real to show" |
| Illustrations | Wrong tone — this is a technical service, not a startup app |
| Abstract visuals | Don't communicate anything specific |
| Corporate clichés | Immediate credibility loss with discerning audience |
| Fake smiles | Subconsciously registers as untrustworthy |

### The Alternative

```
Instead of STOCK → Show REAL workshop, real devices, real team
Instead of ILLUSTRATIONS → Show PHOTOGRAPHY of actual process
Instead of ABSTRACT → Show CONCRETE proof of work
Instead of CLICHÉS → Show AUTHENTIC moments (even imperfect)
Instead of FAKE → Show GENUINE (serious technician > smiling model)
```

---

## 4. Beats-Inspired Visual Logic

### Core Principle

> **"Images must replace explanations, not decorate them."**

If you can photograph it, don't write it.  \
If you can show it, don't describe it.  \
If an image doesn't communicate, remove it.

---

### 4.1 Image Style

| Attribute | Requirement | Rationale |
|-----------|-------------|-----------|
| **Framing** | Close-up shots preferred | Intimacy, detail, expertise signal |
| **Subject** | Real-life scenes only | Authenticity over polish |
| **Environment** | Real spaces, real situations | Trust through transparency |
| **Lighting** | Controlled, intentional | Professional quality signal |
| **Contrast** | High when relevant | Visual impact, premium feel |
| **Background** | Clean, uncluttered | Focus on subject, no distraction |

#### Style Examples

```yaml
GOOD - Close-up of technician's hands soldering:
  → Shows expertise
  → Real environment
  → Intentional framing
  → Communicates "precision"

BAD - Wide shot of generic office with people:
  → Says nothing specific
  → Could be any company
  → No expertise signal
  → Filler, not communication
```

---

### 4.2 Image Role

Images serve specific functions. Every image must have a job:

| Role | Function | Example |
|------|----------|---------|
| **Hero Anchor** | Establish emotional tone, immediate positioning | MacBook + iPhone product shot |
| **Proof Point** | Demonstrate capability without words | Before/after repair |
| **Environment Trust** | Show real workspace = real business | Workshop interior |
| **Process Illustration** | Replace step descriptions | Hands during diagnosis |
| **Human Connection** | Real people = real accountability | Technician portrait |
| **Location Signal** | Prove physical presence | Storefront exterior |

#### Role Validation Test

For every image, answer:

```
1. What specific message does this image convey?
2. Could this section work without any image?
3. Does this image REPLACE text or just ACCOMPANY it?
4. Would a competitor use the exact same image?
```

If #4 is "yes" → Find a different image or use none.

---

### 4.3 Image Quantity

> **"Fewer images, but stronger impact."**

#### The Restraint Principle

```yaml
Beats Logic:
  - One powerful image > three mediocre ones
  - Empty space communicates quality
  - Visual noise = desperation signal
  - Every image must justify its existence

Application:
  - Hero: 1 strong image
  - Per section: 0-1 image (not 3-4)
  - Total per page: 6-10 images maximum
  - Expandable sections: May have 0 images
```

#### Quantity Guidelines by Page

| Page | Hero | Body Sections | FAQ/Expandable | Total Max |
|------|------|---------------|----------------|-----------|
| **Inicio** | 1 | 4-6 | 0 | 8 |
| **Empresas** | 1 | 5-7 | 0 | 10 |

---

### 4.4 Image Usage in Layout

#### Layout Patterns

| Pattern | When to Use | Execution |
|---------|-------------|-----------|
| **Full-width hero** | Page opening | Edge-to-edge, text overlay or split |
| **Split section** | Feature highlight | 50/50 image-text, alternating sides |
| **Contained image** | Supporting visual | Within content container, not bleeding |
| **Background image** | Atmosphere only | Low opacity or section-defining |
| **No image** | Text-sufficient | FAQ, detailed specs, legal |

#### Layout Prohibitions

```diff
- ❌ Random image grids (Pinterest-style)
- ❌ Image carousels with 10+ slides
- ❌ Tiny thumbnails scattered throughout
- ❌ Images as bullet point decorations
- ❌ Background images with unreadable text overlay
- ❌ Multiple images competing in same viewport
```

#### Rhythm Pattern

Follow the Beats "breathing" pattern:

```
VISUAL-HEAVY  (Hero)
     ↓
VISUAL-LIGHT  (Trust badges, icons only)
     ↓
VISUAL-MEDIUM (Split section with image)
     ↓
VISUAL-NONE   (Text section, breathing room)
     ↓
VISUAL-MEDIUM (Split section, opposite side)
     ↓
VISUAL-NONE   (Process steps, icons acceptable)
     ↓
[repeat pulse...]
     ↓
VISUAL-LIGHT  (CTA section, minimal imagery)
```

---

### 4.5 Image Selection Logic

For each section, document:

```yaml
Section: [Name]

Image Decision:
  Used: Yes / No

If Yes:
  Role: [Hero Anchor / Proof Point / Environment Trust / etc.]
  Message: [What specific message does it convey?]
  Why This Image: [Why is this the right choice?]
  Alternatives Considered: [What else was available?]

If No:
  Reason: [Why no image needed?]
  What Carries the Section: [Text / Icons / Whitespace]
```

---

## 5. Page-Specific Visual Strategy

### 5.1 Inicio (B2C Repair)

#### Visual Objective

```
Communicate: "Expert Apple repair, real workshop, real people, Panama"
Feel: Calm confidence, technical competence, local trust
```

#### Image Priority by Section

| Section | Image Priority | Primary Message |
|---------|----------------|-----------------|
| Hero | 🔴 Critical | "Apple specialists in Panama" |
| Trust Bar | ⚪ None (icons) | Numbers speak |
| Services Grid | 🟡 Optional | Device recognition |
| Process Steps | 🟡 Optional | Can be icon-based |
| Why Choose Us | 🟢 Low | Text-sufficient |
| Locations | 🔴 Critical | "We exist physically" |
| FAQ | ⚪ None | Text-only |
| Final CTA | 🟢 Low | CTA is the focus |

#### Image Types Needed

```yaml
Must Have:
  - Hero product shot (iPhone + MacBook, clean)
  - Workshop/environment shot (real workspace)
  - Storefront photos (both locations)

Nice to Have:
  - Technician hands close-up
  - Before/after repair example
  - Device being handed to customer

Do NOT Use:
  - Broken/cracked screens (anxiety-inducing)
  - Sad people with broken phones
  - Generic "tech repair" stock
```

---

### 5.2 Empresas (B2B Leasing)

#### Visual Objective

```
Communicate: "Professional Apple fleet management, operational efficiency"
Feel: Business-appropriate, stable, organized
```

#### Image Priority by Section

| Section | Image Priority | Primary Message |
|---------|----------------|-----------------|
| Hero | 🔴 Critical | "Business-grade Apple equipment" |
| Client Logos | ⚪ None (logos) | Social proof |
| Benefits Grid | 🟢 Low | Icons sufficient |
| Equipment Catalog | 🟡 Medium | Product recognition |
| New vs Refurbished | 🟢 Low | Comparison focus |
| Comparison Table | ⚪ None | Data focus |
| Process Steps | 🟡 Optional | Can be icon-based |
| Testimonials | 🟢 Low | Quote is focus |
| FAQ | ⚪ None | Text-only |
| Cross-sell | 🟢 Low | CTA is focus |
| Final CTA | 🟢 Low | CTA is focus |

#### Image Types Needed

```yaml
Must Have:
  - Hero: Modern office with Apple devices
  - Equipment: Clean product shots (MacBook, iMac, etc.)

Nice to Have:
  - Team using MacBooks in meeting
  - Device fleet/multiple units
  - Professional unboxing/setup

Do NOT Use:
  - Broken devices (wrong page, wrong emotion)
  - Consumer/home settings
  - Single person "working from home" vibe
  - Overly casual/startup aesthetic
```

---

## 6. Section-by-Section Image Framework

### Template for Documentation

```yaml
# ─────────────────────────────────────────
# SECTION: [Section Name]
# PAGE: [Inicio / Empresas]
# ─────────────────────────────────────────

Visual Decision: [Image / No Image / Icons Only]

If IMAGE:

  Role:
    # What job does this image do?
    # [Hero Anchor / Proof Point / Environment Trust /
    #  Process Illustration / Human Connection / Location Signal]

  Message:
    # In one sentence, what does this image SAY?
    # Example: "We have a real, professional workshop"

  Subject Requirements:
    # What must be IN the image?
    # Example: "Clean workspace, visible tools, good lighting"

  Subject Prohibitions:
    # What must NOT be in the image?
    # Example: "No clutter, no people in frame, no branding"

  Framing:
    # Close-up / Medium / Wide
    # Portrait / Landscape / Square

  Mood:
    # What emotional tone?
    # Example: "Calm, professional, precise"

  Layout Integration:
    # Full-width / Split / Contained / Background
    # Left / Right / Center

  Mobile Behavior:
    # How does it adapt?
    # Example: "Stacks above text, crops to center focus"

  From Library:
    # Can this be sourced from /images/?
    # [Yes - describe match / Partial - needs crop / No - gap identified]

If NO IMAGE:

  Reason:
    # Why is no image needed?
    # Example: "Section is data-driven, table format, image would distract"

  Visual Carrier:
    # What carries the visual weight instead?
    # [Icons / Typography / Whitespace / Color blocks]

# ─────────────────────────────────────────
```

---

### Example: Inicio Hero

```yaml
# ─────────────────────────────────────────
# SECTION: Hero
# PAGE: Inicio
# ─────────────────────────────────────────

Visual Decision: Image

Role: Hero Anchor

Message: "Professional Apple device repair — this is our expertise"

Subject Requirements:
  - iPhone and/or MacBook as primary subjects
  - Clean, neutral background
  - Professional lighting (not harsh, not flat)
  - Devices should look premium, not damaged

Subject Prohibitions:
  - No cracked screens
  - No human hands in hero (save for process sections)
  - No busy backgrounds
  - No other brand devices

Framing:
  - Landscape orientation
  - Medium shot showing full devices
  - Slight angle for depth

Mood: Clean, confident, premium, calm

Layout Integration:
  - Split layout: Text left, image right (desktop)
  - Or: Full-width with text overlay
  - Image should occupy ~50% of hero width

Mobile Behavior:
  - Stacks: Image above text
  - May crop to focus on single device
  - Maintain aspect ratio, don't stretch

From Library: [To be determined during implementation]

# ─────────────────────────────────────────
```

---

### Example: Section with No Image

```yaml
# ─────────────────────────────────────────
# SECTION: FAQ
# PAGE: Inicio
# ─────────────────────────────────────────

Visual Decision: No Image

Reason:
  - Section is purely informational
  - Users are scanning for specific answers
  - Images would slow down information retrieval
  - Accordion UI provides necessary visual structure

Visual Carrier:
  - Typography hierarchy (question bold, answer regular)
  - Whitespace between items
  - Subtle expand/collapse icons
  - Section header may have small icon

# ─────────────────────────────────────────
```

---

## 7. Image Selection Decision Tree

Use this flowchart for every section:

```
START: Does this section need an image?
│
├─► Is the section's message better shown than described?
│   │
│   ├─► YES → Image likely needed
│   │         │
│   │         ├─► Check /images/ library
│   │         │   │
│   │         │   ├─► Strong match exists? → USE IT
│   │         │   │
│   │         │   ├─► Partial match exists? → Can crop/reframe work?
│   │         │   │                           │
│   │         │   │                           ├─► YES → Use with notes
│   │         │   │                           └─► NO → Mark as gap
│   │         │   │
│   │         │   └─► No match? → Document gap, proceed without
│   │         │
│   │         └─► Does a weak image HARM more than no image?
│   │             │
│   │             ├─► YES → Use no image
│   │             └─► NO → Use weak image with improvement notes
│   │
│   └─► NO → Image likely not needed
│           │
│           └─► What carries visual weight?
│               │
│               ├─► Icons → Design icon set
│               ├─► Typography → Emphasize text hierarchy
│               ├─► Whitespace → Let content breathe
│               └─► Color → Background or accent treatment
│
└─► DOCUMENT your decision in the framework template
```

---

## 8. Technical Specifications

### Image File Requirements

| Attribute | Specification | Reason |
|-----------|---------------|--------|
| **Format** | WebP (primary), JPEG (fallback) | Performance + compatibility |
| **Max File Size** | Hero: 200KB / Body: 150KB / Icons: 20KB | Core Web Vitals |
| **Resolution** | 2x display (e.g., 1600px for 800px display) | Retina support |
| **Color Space** | sRGB | Web consistency |
| **Compression** | Quality 80-85% | Balance size/quality |

### Responsive Image Requirements

```html
<!-- Required srcset for all content images -->
<img
  src="image-800.webp"
  srcset="
    image-400.webp 400w,
    image-800.webp 800w,
    image-1200.webp 1200w,
    image-1600.webp 1600w
  "
  sizes="(max-width: 600px) 100vw, (max-width: 1200px) 50vw, 800px"
  alt="[Descriptive alt text with keywords]"
  width="800"
  height="600"
  loading="lazy"
>
```

### Hero Image Special Treatment

```yaml
Hero images are critical path:
  - DO NOT lazy load
  - Preload in <head>
  - Inline critical CSS for hero container
  - Max 200KB file size
  - LCP element priority
```

```html
<!-- In <head> -->
<link rel="preload" as="image" href="hero-image.webp">
```

### Alt Text Requirements

```yaml
Purpose: SEO + Accessibility

Format: [Subject] + [Context] + [Relevant keyword if natural]

Examples:
  Good: "Técnico reparando la pantalla de un iPhone en nuestro taller de Panamá"
  Bad: "image1" or "iPhone repair" or "photo of phone"

Rules:
  - Describe what's IN the image
  - Include location keyword where natural
  - Don't keyword stuff
  - If decorative, use alt=""
```

---

## 9. Quality Validation

### Pre-Implementation Checklist

```markdown
## For Each Section with Image

- [ ] Role clearly defined (not "decoration")
- [ ] Message articulated in one sentence
- [ ] Library checked for existing assets
- [ ] Framing and mood specified
- [ ] Mobile behavior defined
- [ ] Technical specs achievable

## For Each Section without Image

- [ ] Reason documented
- [ ] Alternative visual carrier identified
- [ ] Confirmed image wouldn't strengthen section
```

### Visual Quality Checklist

```markdown
## Image Meets Standards

- [ ] Not stock photography
- [ ] Not illustration/vector
- [ ] Real environment/situation
- [ ] Lighting is intentional
- [ ] Background is clean
- [ ] Subject is clear
- [ ] No clichés (handshakes, fake smiles)
- [ ] Supports confidence/credibility
- [ ] Serves specific communication purpose
```

### Layout Integration Checklist

```markdown
## Image Works in Context

- [ ] Doesn't compete with text for attention
- [ ] Clear visual hierarchy maintained
- [ ] Appropriate whitespace around image
- [ ] Mobile adaptation defined
- [ ] Doesn't break page rhythm
- [ ] File size within limits
- [ ] Responsive srcset prepared
- [ ] Alt text written
```

---

## Summary: The Visual Discipline Manifesto

```
1. REAL over STOCK
   → Show your actual workshop, team, devices

2. INTENTIONAL over DECORATIVE
   → Every image has a job; no fillers

3. FEWER over MORE
   → One strong image beats five weak ones

4. RESTRAINED over BUSY
   → Whitespace communicates quality

5. AUTHENTIC over POLISHED
   → A genuine moment beats a staged photo

6. LIBRARY FIRST over NEW SOURCING
   → Use what exists; document gaps

7. NONE over WEAK
   → No image is better than wrong image
```

---

## Document Info

| Property | Value |
|----------|-------|
| **Type** | Visual Direction Guidelines |
| **Scope** | All pages (Inicio, Empresas) |
| **Dependencies** | Requires `/images/` library access |
| **Used By** | Designer, Developer, Content team |
| **Updates** | When new photography is added |

---

*This document is part of the Salva Mi Máquina website codex.*
