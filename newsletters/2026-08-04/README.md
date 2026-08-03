# SE Horizon — Edition 03 · August 4, 2026

**Biweekly Pulse** · Coverage: July 19 – August 4, 2026 · 27 Accounts

---

## Edition Summary

This is the third edition of SE Horizon, the biweekly IBM South Florida SE intelligence newsletter. The coverage period runs **July 19 – August 4, 2026** (16 days). It contains 27 accounts: 10 returning core accounts and 17 accounts first introduced in Edition 02 (July 19) as Annual Deep Dives — all now transitioned to the Biweekly Pulse format with fresh Jul 19–Aug 4 signals.

Key structural change from Edition 02: the "New Account / Annual Deep Dive" banner has been replaced with a universal `pulse-box` blue banner across all 27 accounts, reflecting that every account now has biweekly coverage, not a first-look intro.

---

## Files in This Edition

| File | Phase | Description |
|---|---|---|
| `phase1.html` | Phase 1 | Signal Tracker — top signals across all accounts, Jul 19–Aug 4 |
| `phase2.html` | Phase 2 | Full Intel Brief — 27 accounts with pulse updates, talk tracks, cadences |
| `phase3.html` | Phase 3 | Brand Index — entry point to all 4 brand seller views |
| `phase3-data-ai.html` | Phase 3 | Data & AI — Alyssa's Territory (IBM Blue · `#0f62fe`) |
| `phase3-automation.html` | Phase 3 | Automation — Gavin's Territory (Green · `#42be65`) |
| `phase3-storage.html` | Phase 3 | Storage — William's Territory (Purple · `#8b5cf6`) |
| `phase3-power-cloud.html` | Phase 3 | Power & Hybrid Cloud — Rick & Kevin's Territory (Amber · `#f59e0b`) |

---

## Logo Files (LOGOS/ folder)

All 27 accounts use external logo files from the `LOGOS/` directory (not base64 inline). Files must be present for logos to render. Key mappings:

| Account | Logo File |
|---|---|
| Southern Glazer's | `SGWS.png` |
| NCLH | `NCLW.webp` |
| JM Family | `jmfamily.png` |
| Citco | `citco.png` |
| Lennar | `lennar.jpg` |
| Lennar Mortgage | `lennarmort_logo.png` |
| Octave | `octave-logo.png` |
| Hexagon Federal | `hexagonfederal.png` |
| Hexagon Mining | `Hexagon_logo_mining.svg` |
| Pellera | `Pellera_Technologies_Pellera_Technologies_Launches_Official_New.jpg` |
| HEICO | `heico-vector-logo.png` |
| H.I.G. Capital | `HIG_Capital_Logo.jpeg` |
| Kforce | `kforce_trademark_fullcolor_500.png` |
| Burger King / RBI | `burgerking.png` |
| SeaWorld | `Seaworld_logo.svg` |
| S. Broward Hospital Dist. | `broward-and-memorial-logos.jpg` |
| Icahn Enterprises | `icahn-enterprises-l-p.jpeg` |
| ANSCO | `ansco-and-associates-squarelogo-1555338841264.webp` |
| Dycom | `DYCOM-Logo-Color-1-1024x168.png` |
| Herc Rentals | `herc.jpeg` |
| Data Mgmt. Brevard | *(no logo — placeholder only)* |
| Memorial Healthcare | `MemorialHealthSystem_BlueLogo.jpg` |
| MasTec | `MasTec_Logo.jpg` |
| Frontline Insurance | `Frontline_Insurance_Logo.jpg` |
| Office Depot | `ODP_Wht-e1594114705114.jpg` |
| Chewy | `chewy.png` |
| Chico's FAS | `Chicos_FAS.jpg` |

---

## Top Signals This Edition (Jul 19 – Aug 4)

| Account | Signal | Brand |
|---|---|---|
| NCLH | Q2 beat Jul 30 — revenue $2.53B (+7%), EPS $0.52 beat; post-earnings window open Aug 4–11 | Data & AI |
| HEICO | Q3 earnings Aug 25 — pre-call window open; AeroAntenna acquisition closed July | Data & AI |
| Kforce | Q2 beat Jul 27 — "Strategic AI Focus" confirmed on earnings call; stock +5.5% | Data & AI |
| Herc Rentals | Q2 beat Jul 28 — H&E IT integration confirmed complete; "one company" declared on call | Data & AI |
| Memorial Healthcare | IT Security RFP active (decision end of Aug); Douglas Road ER opens Aug 2026 | Power & Cloud |
| Dycom | Power Solutions acquisition announced; Q2 earnings Aug 20 pre-call window open | Storage |
| Burger King / RBI | Q2 EPS miss ($0.94 vs $0.97) — CFO under efficiency pressure | Automation |
| Hexagon Federal | Compass 2026 conference Aug 25–27 — pre-event outreach window open NOW | Power & Cloud |
| MasTec | $1.65B Superior Plus acquisition closed Jul 7 — IT integration live Day 30–90 | Storage |
| Citco | SS&C + SEI both launched AI fund reporting updates this fortnight | Data & AI |

---

## Phase 3 Brand Color Reference

Each brand file has its own color identity matching the Jul 19 edition. All colors are applied to: topbar border, topbar badge, active nav underline, hero gradient, eyebrow text, h1 accent span, prod-tag colors, card left border, active pnav pill.

| Brand | Seller | Topbar Border | Badge BG | Hero Gradient | Active Color |
|---|---|---|---|---|---|
| Data & AI | Alyssa | `#0f62fe` | `#0f62fe` | `#0a1628 → #0f2040` | `#0f62fe` / subs `#a8c8ff` |
| Automation | Gavin | `#42be65` | `#42be65` (black text) | `#0a1a0f → #0e2a14` | `#42be65` / subs `#6ee08a` |
| Storage | William | `#7c3aed` | `#8b5cf6` | `#0e0a1a → #1a0f2e` | `#8b5cf6` / subs `#a78bfa` |
| Power & Cloud | Rick & Kevin | `#d97706` | `#f59e0b` (black text) | `#1a1200 → #2a1e00` | `#f59e0b` / subs `#fcd34d` |

---

## Design Consistency Checklist

Every brand page in this edition must have:
- [x] `se-topbar` border — brand color (not generic `#0f62fe`)
- [x] `se-topbar-badge` — `Phase 3 · [Brand]` in brand color
- [x] `se-topbar-links a.se-active` — `border-bottom-color` = brand color
- [x] `se-topbar-links a.se-sub.se-active` — sub-link color = brand accent
- [x] `brand-hero` — brand-colored dark gradient (not generic blue)
- [x] `brand-eyebrow` — brand accent color
- [x] `brand-hero h1 span` — brand accent color
- [x] Page nav pills (`.pnav-pill.active`) — active pill = brand color
- [x] Account cards (`.acct-card-full`) — `border-left` = brand color
- [x] Section label — reflects biweekly pulse coverage window

---

## Coverage Period Labels

The following text is used consistently throughout this edition to identify coverage scope:

- Cover subtitle: `"Jul 19 – Aug 4, 2026"`
- Quick Play table header: `"Coverage: Jul 19 – Aug 4, 2026"`
- Cover footer: `"Edition 03 · Aug 4, 2026 · Coverage: Jul 19 – Aug 4"`
- Account `acct-date-line`: `"Jul 19 – Aug 4, 2026 · [Type] · [Industry] · [City]"`
- Account cadence title: `"Biweekly Cadence — Aug 4–18"`

---

## Mirror

This folder is mirrored to:
```
se-horizon/editions/2026-08-04/
```
After every change: mirror files, commit + push both repos.

---

## Edition History

| Edition | Folder | Publish Date | Coverage | Accounts |
|---|---|---|---|---|
| Edition 01 | `../2026-07-19/` | July 21, 2026 | Annual Deep Dive | 26 |
| Edition 02 | `../2026-07-19/` | July 21, 2026 | *(same folder, July 19 label)* | 26 |
| Edition 03 | `../2026-08-04/` | August 4, 2026 | Jul 21 – Aug 4, 2026 | 27 |

> Note: The `2026-07-19/` folder was created as the Edition 01/02 base. The publish date was corrected to July 21 in the HTML but the folder name reflects the start-of-period date. Edition 03 is the first true biweekly pulse edition.
