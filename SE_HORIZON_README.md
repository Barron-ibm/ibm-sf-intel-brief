# SE Horizon Newsletter — Build Instructions
**For IBM South Florida SE Team · July 19, 2026**

---

## What You Are Building

Two HTML files for an IBM South Florida SE team newsletter:

- **PHASE1.html** — Single-page interactive weekly pulse (JavaScript-driven, all 26 accounts in one scrollable page)
- **PHASE2.html** — Multi-page intelligence brief (one full HTML page per account)

Both files live at `/Users/barronkwekuowusu/Desktop/bobmode/`
Logos are in `/Users/barronkwekuowusu/Desktop/bobmode/LOGOS/`

---

## CRITICAL RULE — READ THIS FIRST

> **Do ALL web research before touching any files. Run searches in parallel. Compile all 26 accounts worth of findings. Then and only then write the HTML.**
>
> Do NOT rewrite files from scratch. Patch the existing working files.
> The existing PHASE1.html has a working HTML shell and 10 accounts in a JS `accounts {}` object.
> The existing PHASE2.html has a working cover page and 10 account pages.
> You are adding to them — not replacing them.

---

## Step 1 — Web Research

### Existing 10 Accounts — Search Last 14 Days Only (July 5–19, 2026)
For each: news, earnings, hiring signals, external market factors, technology signals.

1. Norwegian Cruise Line Holdings (NCLH) — NYSE: NCLH
2. Southern Glazer's Wine & Spirits — Private
3. JM Family Enterprises — Private
4. Citco Group — Private, Fund Administration
5. Octave (formerly Hexagon ALI division) — Independent since May 2026
6. Hexagon Federal — Government Technology
7. Hexagon Mining — Mining Technology Software
8. Pellera Technologies — IBM Partner / MSP
9. Lennar Corporation — NYSE: LEN
10. Lennar Mortgage (Lennar Financial Services)

### New 16 Accounts — Annual Deep-Dive (July 2025–July 2026)
For each: company overview, financials, key 2026 signals, hiring trends, IBM angle.

1. HEICO Corporation (NYSE: HEI) — Hollywood FL — Aerospace & Defense
2. H.I.G. Capital Inc. — Miami FL — Private Equity (~$74B AUM)
3. Kforce Inc. (NASDAQ: KFRC) — Tampa FL — Technology & Finance Staffing
4. Burger King / Restaurant Brands International (NYSE: QSR) — Miami FL — QSR
5. SeaWorld Entertainment / United Parks & Resorts (NYSE: PRKS) — Orlando FL
6. Icahn Enterprises LP (NYSE: IEP) — Sunny Isles Beach FL — Diversified Holding
7. ANSCO & Associates Inc. — Palm Harbor FL — Telecom Engineering (Dycom subsidiary)
8. Dycom Industries Inc. (NYSE: DY) — Palm Beach Gardens FL — Telecom Infrastructure
9. Herc Rentals Inc. / Herc Holdings (NYSE: HRI) — Bonita Springs FL — Equipment Rental
10. Data Management Associates of Brevard Inc. — Melbourne FL — IBM Mainframe Managed Services
11. Memorial Healthcare System — Hollywood FL — Public Health System (6 hospitals)
12. MasTec Inc. (NYSE: MTZ) — Coral Gables FL — Infrastructure Construction
13. Frontline Insurance Managers — Lake Mary FL — Florida Homeowners Insurance
14. Office Depot / ODP Corporation (NYSE: ODP) — Boca Raton FL — Office Products & B2B
15. Chewy Inc. (NYSE: CHWY) — Plantation FL — Pet Products E-Commerce
16. Chico's FAS / KnitWell Group (NYSE: CHS) — Fort Myers FL — Retail Apparel

---

## Step 2 — PHASE1.html

### What to Edit
Open the existing `PHASE1.html`. It already has:
- Working HTML shell (nav, pills, tracker table, footer)
- 10 accounts in the `var accounts = {}` JS object
- A `render()` function
- A click event listener

You need to:
1. Add 16 new nav items to the `#accountNav` div (green color, `●` prefix)
2. Add a logo display area below the nav (already scaffolded as `#logoWrap` / `#acctLogo`)
3. Add 16 new account objects to `var accounts = {}`
4. Update the `render()` function to handle the new fields below
5. Update the footer text to: `Made with IBM Bob · SE Horizon · July 19, 2026 · ● = New Account`

### Account Object Structure (add ALL fields to existing 10 accounts too)

```js
accountKey: {
  name: "Full Account Name",
  logo: "LOGOS/filename.ext",        // relative path to logo file
  isNew: true,                        // false for existing 10
  coverage: "Last 14 Days",           // or "Annual Deep Dive — 2026"
  mission: "Mission statement text",  // only populated for new 16; empty string for existing 10
  signal: "high",                     // "high" / "medium" / "low"
  summary: "Account pulse summary paragraph...",
  signals: ["Signal 1", "Signal 2", "Signal 3"],
  hiring: ["Hiring signal 1", "Hiring signal 2", "Hiring signal 3"],
  external: ["External factor 1", "External factor 2", "External factor 3"],
  why: ["Why it matters 1", "Why it matters 2", "Why it matters 3"],
  trackerNews: "One-line news finding for tracker table",
  trackerHiring: "One-line hiring finding for tracker table",
  trackerExternal: "One-line external factor for tracker table",
  trackerTech: "One-line technology signal for tracker table",
  snavId: "12345",                    // LinkedIn company numeric ID
  personas: [
    "CFO", "CIO", "COO", "VP Finance", "FP&A Director",
    // + 4–6 bottom-up personas tailored to the industry (see persona guide below)
  ],
  sources: [
    { label: "Source Name", url: "https://..." }
  ]
}
```

### Updated render() Function Requirements

The `render(key)` function must:
- Toggle `.mission-box` visibility: add class `visible` if `a.isNew`, remove if not
- Set `#missionText` content from `a.mission`
- Set `#pillCoverage` text from `a.coverage`
- Show/hide logo: if `a.logo` exists, set `#acctLogo` src and display; else hide
- Add `<span class="badge-new">NEW</span>` after account name in `#pillAccount` if `a.isNew`
- Change `#summaryHdr` text to "Annual Company Overview" if `a.isNew`, else "Account Pulse Summary"
- Render each persona as a row with name + individual SNav button:

```js
document.getElementById('personasList').innerHTML = a.personas.map(function(p) {
  var snavUrl = 'https://www.linkedin.com/sales/search/people?query=(filters%3AList((type%3ACURRENT_COMPANY%2Cvalues%3AList((id%3A' + a.snavId + '%2CselectionType%3AINCLUDED)))))';
  return '<div class="persona-tag">' + p +
    '<a class="snav-btn" href="' + snavUrl + '" target="_blank" rel="noopener">SNav</a>' +
    '</div>';
}).join('') +
'<div class="snav-keywords"><strong>SNav Search:</strong> "' + a.name.split(' ')[0] + '" + ' + a.personas.slice(0,5).join(', ') + '</div>';
```

### Nav Item HTML for New Accounts
```html
<div class="nav-item is-new" data-account="heico">● HEICO</div>
<div class="nav-item is-new" data-account="hig">● H.I.G. Capital</div>
<div class="nav-item is-new" data-account="kforce">● Kforce</div>
<div class="nav-item is-new" data-account="bk">● Burger King</div>
<div class="nav-item is-new" data-account="seaworld">● SeaWorld</div>
<div class="nav-item is-new" data-account="icahn">● Icahn Enterprises</div>
<div class="nav-item is-new" data-account="ansco">● ANSCO</div>
<div class="nav-item is-new" data-account="dycom">● Dycom</div>
<div class="nav-item is-new" data-account="herc">● Herc Rentals</div>
<div class="nav-item is-new" data-account="dmab">● Data Mgmt. Brevard</div>
<div class="nav-item is-new" data-account="memorial">● Memorial Healthcare</div>
<div class="nav-item is-new" data-account="mastec">● MasTec</div>
<div class="nav-item is-new" data-account="frontline">● Frontline Insurance</div>
<div class="nav-item is-new" data-account="odp">● Office Depot</div>
<div class="nav-item is-new" data-account="chewy">● Chewy</div>
<div class="nav-item is-new" data-account="chicos">● Chico's FAS</div>
```

### CSS Already in File (do not duplicate)
```css
.nav-item.is-new { color: #6ee08a; }
.nav-item.is-new.active { background: #0f62fe; color: #fff; }
.acct-logo-img { max-width:90px; max-height:56px; object-fit:contain; mix-blend-mode:multiply; }
.mission-box { display:none; }
.mission-box.visible { display:block; }
.badge-new { color:#161616; background:#6ee08a; font-size:11px; font-weight:700; padding:2px 10px; border-radius:20px; margin-left:6px; }
.snav-btn { display:inline-block; font-size:10px; font-weight:600; color:#0a66c2; background:#e8f2ff; border:1px solid #b8d4f5; border-radius:3px; padding:2px 6px; text-decoration:none; }
.snav-keywords { font-size:11px; color:#525252; margin-top:8px; padding:6px 8px; background:#e8f1ff; border-radius:3px; }
```

---

## Step 3 — PHASE2.html

### What to Edit
Open the existing `PHASE2.html`. It already has:
- A working cover page
- 10 complete account pages (SGWS through Lennar Mortgage)
- All CSS

You need to:
1. Update the cover page Quick Plays table — add all 16 new accounts (marked ✦), update Rapid Recap
2. Update the cover pill nav — add all 16 new accounts in green
3. **Remove every `<div class="bottom-nav-bar">...</div>` block** from all 10 existing account pages
4. Add a Phase 1-style scrollable dark top nav to the TOP of every account page (existing + new)
5. Add 16 new account pages

### Top Nav to Add to Every Account Page (goes above `<div class="top-bar">`)

```html
<div style="background:#161616;overflow-x:auto;border-bottom:3px solid #0f62fe;display:flex;scrollbar-width:thin;scrollbar-color:#4c4c4c #262626;">
  <a href="#top" style="flex-shrink:0;padding:11px 18px;font-size:11.5px;font-weight:700;color:#a8c8ff;white-space:nowrap;text-decoration:none;border-right:1px solid #2e2e2e;">↑ Cover</a>
  <!-- existing 10 accounts — white/grey color -->
  <a href="#sgws" style="flex-shrink:0;padding:11px 18px;font-size:11.5px;font-weight:500;color:#a8a8a8;white-space:nowrap;text-decoration:none;border-right:1px solid #2e2e2e;">Southern Glazer's</a>
  <a href="#nclh" style="...">NCLH</a>
  <a href="#jmf" style="...">JM Family</a>
  <a href="#citco" style="...">Citco</a>
  <a href="#octave" style="...">Octave</a>
  <a href="#hexfed" style="...">Hexagon Federal</a>
  <a href="#hexmin" style="...">Hexagon Mining</a>
  <a href="#pellera" style="...">Pellera</a>
  <a href="#lennar" style="...">Lennar</a>
  <a href="#lennarmtg" style="...">Lennar Mortgage</a>
  <!-- new 16 accounts — green color #6ee08a -->
  <a href="#heico" style="color:#6ee08a;...">● HEICO</a>
  <a href="#hig" style="color:#6ee08a;...">● H.I.G. Capital</a>
  <a href="#kforce" style="color:#6ee08a;...">● Kforce</a>
  <a href="#bk" style="color:#6ee08a;...">● Burger King</a>
  <a href="#seaworld" style="color:#6ee08a;...">● SeaWorld</a>
  <a href="#icahn" style="color:#6ee08a;...">● Icahn Enterprises</a>
  <a href="#ansco" style="color:#6ee08a;...">● ANSCO</a>
  <a href="#dycom" style="color:#6ee08a;...">● Dycom</a>
  <a href="#herc" style="color:#6ee08a;...">● Herc Rentals</a>
  <a href="#dmab" style="color:#6ee08a;...">● Data Mgmt. Brevard</a>
  <a href="#memorial" style="color:#6ee08a;...">● Memorial Healthcare</a>
  <a href="#mastec" style="color:#6ee08a;...">● MasTec</a>
  <a href="#frontline" style="color:#6ee08a;...">● Frontline Insurance</a>
  <a href="#odp" style="color:#6ee08a;...">● Office Depot</a>
  <a href="#chewy" style="color:#6ee08a;...">● Chewy</a>
  <a href="#chicos" style="color:#6ee08a;...">● Chico's FAS</a>
</div>
```
The currently active account's link gets `background:#0f62fe; color:#fff;`

### New Account Page Structure (in order, no exceptions)

```
1. Top scrollable nav (above everything on the page)
2. Green new-account banner div:
   ✦ New Account — Annual Deep Dive · Added July 2026
   (background:#1a4a1a; border-left:5px solid #42be65; color:#6ee08a)
3. <div class="top-bar"></div>
4. Account header row (.acct-header-row) with logo + name
5. Mission statement row (green tinted background, italic text, "Mission" badge)
6. <hr class="dashed-div">
7. Meta rows: Priority & Confidence + Seller Thesis
8. LinkedIn suggested search row (.linkedin-row)
9. <hr class="dashed-div">
10. Three-column dark grid (.dark-grid):
    - Col 1 (.grid-col-left): Why Now?
    - Col 2 (.grid-col-mid): Pain Point
    - Col 3 (.grid-col-right): Key Personas / Below C-Suite
11. IBM Sales Play + LinkedIn SNav — 50/50 grid spanning full width below dark grid:
    grid-template-columns: 1fr 1fr; grid-column: 1 / 4
    - Left cell: IBM Sales Play bar (background:#0f62fe)
    - Right cell: LinkedIn SNav panel (background:#0a50cc) with:
        "Open Sales Navigator" white button linking to SNav URL
        Keyword search terms listed below button
12. <hr class="dashed-div">
13. Seller Move + Talk Track (.lower-section)
14. Message Cadence (.message-cadence) — 3-week sequence
15. Sources footer strip (.sources-footer)
16. Page footer (.page-footer) — NO bottom-nav-bar div
```

### IBM Sales Play Row HTML Pattern
```html
<div style="display:grid;grid-template-columns:1fr 1fr;grid-column:1/4;">
  <div class="ibm-play-bar">
    <div class="play-bar-label"><span class="grid-chevron">&raquo;</span><span class="play-bar-label-text">IBM Sales Play</span></div>
    <div class="play-main-text">IBM Planning Analytics + <span>watsonx</span></div>
    <div class="play-supporting-text"><strong>Supporting:</strong> AI Governance, Automation</div>
    <div class="play-why-text">Why this play wins here...</div>
  </div>
  <div style="background:#0a50cc;padding:14px 18px;">
    <div style="font-size:9px;font-weight:800;letter-spacing:1.5px;text-transform:uppercase;color:#fff;margin-bottom:10px;">LinkedIn Sales Navigator</div>
    <a href="https://www.linkedin.com/sales/search/people?query=(filters%3AList((type%3ACURRENT_COMPANY%2Cvalues%3AList((id%3A{COMPANY_ID}%2CselectionType%3AINCLUDED)))))"
       target="_blank" rel="noopener"
       style="display:inline-block;background:#fff;color:#0a50cc;font-size:11px;font-weight:800;padding:7px 16px;border-radius:3px;text-decoration:none;margin-bottom:8px;">
      Open Sales Navigator
    </a>
    <div style="font-size:11px;color:rgba(255,255,255,0.7);line-height:1.6;">
      Search: "CompanyName" + CFO, CIO, VP Finance, FP&A Director, COO
    </div>
  </div>
</div>
```

---

## LinkedIn Company IDs

| Account | LinkedIn Company ID |
|---------|-------------------|
| NCLH | 2297 |
| Southern Glazer's | 10408 |
| JM Family | 5765 |
| Citco | 3439 |
| Lennar | 4605 |
| HEICO | 163065 |
| Dycom | 19434 |
| MasTec | 5350 |
| Chewy | 3497540 |
| Office Depot / ODP | 3492 |
| Kforce | 18877 |
| Memorial Healthcare | 15052 |
| H.I.G. Capital | 28523 |
| Herc Rentals | 2848055 |
| Burger King / RBI | 166764 |
| SeaWorld / United Parks | 2812068 |
| Icahn Enterprises | 12432 |
| Frontline Insurance | 2523441 |
| ANSCO | 880528 |
| Chico's FAS | 11398 |

### SNav URL Pattern
```
https://www.linkedin.com/sales/search/people?query=(filters%3AList((type%3ACURRENT_COMPANY%2Cvalues%3AList((id%3A{COMPANY_ID}%2CselectionType%3AINCLUDED)))))
```

---

## IBM Sales Plays Per New Account

| Account | Primary Play | Supporting |
|---------|-------------|------------|
| HEICO | Data Fabric + watsonx.data + AI Governance | Storage, Security |
| H.I.G. Capital | IBM Planning Analytics + AI Governance + watsonx | Data Fabric |
| Kforce | IBM Planning Analytics + watsonx | Automation |
| Burger King / RBI | AI Governance + watsonx + Automation | Data Fabric |
| SeaWorld / United Parks | IBM watsonx + Planning Analytics + Security | Automation |
| Icahn Enterprises | IBM Planning Analytics + Data Fabric | Power Systems |
| ANSCO | Red Hat OpenShift + Automation | Security |
| Dycom | Storage + Data Fabric + watsonx | Automation |
| Herc Rentals | IBM Planning Analytics + watsonx.data | Automation |
| Data Mgmt. Brevard | IBM Z Modernization + Storage + Security | Hybrid Cloud |
| Memorial Healthcare | AI Governance + Security + watsonx | IBM Planning Analytics |
| MasTec | Storage + Data Fabric + Automation | Power Systems |
| Frontline Insurance | IBM Planning Analytics + AI Governance | watsonx |
| Office Depot / ODP | IBM Planning Analytics + watsonx + Automation | Data Fabric |
| Chewy | watsonx + Automation + AI Governance | IBM Planning Analytics |
| Chico's FAS / KnitWell | IBM Planning Analytics + watsonx | Data Fabric |

---

## Logo File Paths

| Account | Logo Path |
|---------|-----------|
| NCLH | `LOGOS/NCLW.webp` |
| Southern Glazer's | `LOGOS/SGWS.png` |
| JM Family | `LOGOS/jmfamily.png` |
| Citco | `LOGOS/citco.png` |
| Octave | `LOGOS/octave-logo.png` |
| Hexagon Federal | `LOGOS/hexagonfederal.png` |
| Hexagon Mining | `LOGOS/Hexagon_logo_mining.svg` |
| Pellera | `LOGOS/Pellera_Technologies_Pellera_Technologies_Launches_Official_New.jpg` |
| Lennar | `LOGOS/lennar.jpg` |
| Lennar Mortgage | `LOGOS/lennarmort_logo.png` |
| HEICO | `LOGOS/heico-vector-logo.png` |
| H.I.G. Capital | `LOGOS/HIG_Capital_Logo.jpeg` |
| Kforce | `LOGOS/kforce_trademark_fullcolor_500.png` |
| Burger King | `LOGOS/images.png` |
| SeaWorld | `LOGOS/Seaworld_logo.svg` |
| Icahn Enterprises | `LOGOS/icahn-enterprises-l-p.jpeg` |
| ANSCO | `LOGOS/ansco-and-associates-squarelogo-1555338841264.webp` |
| Dycom | `LOGOS/DYCOM-Logo-Color-1-1024x168.png` |
| Herc Rentals | `LOGOS/images.jpeg` |
| Data Mgmt. Brevard | SVG placeholder — no file exists |
| Memorial Healthcare | `LOGOS/MemorialHealthSystem_BlueLogo.jpg` |
| MasTec | `LOGOS/MasTec_Logo.jpg` |
| Frontline Insurance | `LOGOS/Frontline_Insurance_Logo.jpg` |
| Office Depot | `LOGOS/ODP_Wht-e1594114705114.jpg` |
| Chewy | `LOGOS/Screenshot 2026-07-19 at 7.27.22 PM.png` |
| Chico's FAS | `LOGOS/images.jpeg` |

**Logo CSS (apply to all):**
```css
max-width:90px; max-height:56px; object-fit:contain; mix-blend-mode:multiply;
```
On dark grid cell backgrounds use `mix-blend-mode:screen` instead.

---

## Persona Guide by Industry

Every account needs both tiers. Always include the top-down 5 first, then add industry-specific bottom-up personas.

**Top-Down (always include for every account):**
CFO, CIO, COO, VP Finance, FP&A Director / VP

**Bottom-Up by Industry:**

| Industry | Bottom-Up Personas |
|----------|-------------------|
| Homebuilding (Lennar) | FP&A Manager, Financial Modeler, IT Systems Admin, Supply Chain Planner, Data Science Lead |
| Mortgage (Lennar Mortgage) | Compliance Technology Lead, Risk Analytics Manager, Digital Mortgage Lead, Underwriting Manager |
| Cruise / Hospitality (NCLH) | Revenue Management Analyst, Guest Experience Tech Lead, Fleet Systems Manager, Cybersecurity Analyst |
| Beverage Distribution (SGWS) | Pricing Analyst, Supply Chain Planner, Sales Ops Lead, Compliance Manager, Data Analytics Manager |
| Fund Administration (Citco) | Fund Operations Manager, Data Governance Lead, Compliance Tech Lead, Investor Reporting Lead |
| Industrial Software (Octave) | Platform Engineering Lead, Cloud Architect, Capture Manager, Federal Sales Lead |
| Government Tech (Hexagon Federal) | Program Manager, Capture Lead, Cybersecurity Engineer, Systems Integrator |
| Mining Tech (Hexagon Mining) | Mining Operations Lead, Fleet Analytics Manager, Autonomy Engineer, Safety Tech Lead |
| IT Solutions / MSP (Pellera) | IBM Practice Lead, VP Alliances, Defense Practice Lead, Hybrid Cloud Architect |
| Aerospace & Defense (HEICO) | M&A Integration Lead, Supply Chain Planner, Controller, IT Systems Admin, Compliance Lead |
| Private Equity (H.I.G.) | Portfolio Analytics Lead, FP&A Manager, Investment Ops Manager, LP Relations Lead |
| Staffing (Kforce) | Workforce Planning Manager, FP&A Analyst, Sales Ops Lead, HR Analytics Manager |
| QSR / Restaurant (Burger King) | Restaurant Technology Lead, Franchise Analytics Manager, Digital Ordering Lead, Labor Planning Manager |
| Theme Parks / Entertainment (SeaWorld / United Parks) | Guest Experience Tech Lead, Ride Systems Manager, Revenue Management Analyst, Cybersecurity Analyst |
| Diversified Holding (Icahn) | Segment Finance Lead, Enterprise Data Lead, Portfolio Operations Manager |
| Telecom Engineering (ANSCO, Dycom) | Field Operations Manager, Workforce Scheduling Lead, Project Manager, IT Systems Admin |
| Equipment Rental (Herc) | Fleet Planning Manager, Utilization Analyst, Rental Operations Lead, Financial Modeler |
| Mainframe / Federal IT (Data Mgmt. Brevard) | z/OS Systems Programmer, Disaster Recovery Lead, Federal Contract Manager |
| Healthcare (Memorial) | Clinical Informatics Lead, IT Security Manager, EHR Systems Manager, Revenue Cycle Lead |
| Infrastructure Construction (MasTec) | Project Data Manager, Supply Chain Lead, Field Ops IT Manager, Integration Lead |
| Insurance (Frontline) | Actuarial Analyst, Product Manager, Compliance Lead, Risk Modeling Manager |
| Office Products / B2B (Office Depot) | B2B Sales Analytics Lead, Procurement Tech Lead, SG&A Finance Manager, IT Systems Admin |
| Pet E-Commerce (Chewy) | Personalization AI Lead, Vet Platform Tech Lead, Pharmacy Ops Manager, Data Science Lead |
| Retail Apparel (Chico's FAS) | Merchandise Planning Lead, Demand Forecasting Manager, Retail Tech Lead, Customer Analytics Lead |

---

## Dates

- All dates throughout both files: **July 19, 2026**
- Cover page date: **July 19, 2026**
- Footer date: **July 19, 2026**

---

## Final Checklist Before Submitting

- [ ] All 26 accounts researched (10 last 14 days + 16 annual deep-dive)
- [ ] All 26 accounts in PHASE1 `accounts {}` object
- [ ] All 26 nav items in PHASE1 nav bar (new ones green with ●)
- [ ] `render()` handles `isNew`, logo, mission box, coverage pill, SNav buttons per persona, keyword block
- [ ] PHASE2 cover Quick Plays table has all 26 rows (new ones marked ✦)
- [ ] PHASE2 cover pill nav has all 26 accounts (new ones in green)
- [ ] Every `<div class="bottom-nav-bar">` removed from all 10 existing PHASE2 account pages
- [ ] Scrollable dark top nav added to every PHASE2 account page
- [ ] All 16 new PHASE2 account pages added with complete structure
- [ ] IBM Sales Play + SNav panel rendered as 50/50 grid in every PHASE2 account page
- [ ] Every SNav button/link opens in `target="_blank" rel="noopener"`
- [ ] Logo paths correct and `mix-blend-mode:multiply` applied
- [ ] Date is July 19, 2026 throughout

---

*Made with IBM Bob · SE Horizon · IBM South Florida*
