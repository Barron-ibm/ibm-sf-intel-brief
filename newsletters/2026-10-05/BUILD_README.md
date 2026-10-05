# SE Horizon — Edition 08 Build README

## What This Is
**Edition 08** of the SE Horizon newsletter.
Output location: `ibm-sf-intel-brief/newsletters/2026-10-05/`

---

## Key Facts
| Field | Value |
|---|---|
| Edition | 08 |
| Coverage Window | Sep 22 – Oct 5, 2026 |
| Published Date | Oct 5, 2026 |
| Territory | South Florida · Territory 26 |
| Total Accounts | 27 |
| Strike (3) | Chewy, MasTec, Icahn |
| Engage (12) | Lennar, HEICO, Dycom, NCLH, SGWS, H.I.G., ODP, Herc, BK/RBI, Kforce, Citco, Frontline |
| Standby (12) | Lennar Mtg, JM Family, SeaWorld, Chico's, Memorial, S. Broward, Hex Federal, Hex Mining, Octave, Pellera, ANSCO, Data Mgmt Brevard |

---

## Build Status

| File | Status | Lines | Notes |
|---|---|---|---|
| `phase1.html` | ✅ Built | 2,341 | Account Radar — all 27 accounts, light theme, Ed 07 format. ⚡ Why Now bullets need Sep 22–Oct 5 signal refresh from intelligence run |
| `phase2.html` | ⬜ Pending | — | Intel Brief — scaffold from Ed 07 phase2 when signals are in |
| `phase3.html` | ⬜ Pending | — | My Accounts — update ACCOUNTS array tiers and hooks only |

---

## What Changed Edition 07 → Edition 08

| Account | Ed 07 Tier | Ed 08 Tier | Key Change |
|---|---|---|---|
| Icahn | Engage | **Strike** | Nov 4 earnings now 4 weeks out — pre-report prep window is hot |
| Lennar | Strike | **Engage** | Post-Q3-miss wave settling, 2+ weeks old, urgency dropping |
| Dycom | Strike | **Engage** | D.A. Davidson Sep 24 conference has passed — post-conference follow-up window now live |
| Chewy | Strike | Strike | $50M AI target + Q3 earnings approaching — urgency sustained |
| MasTec | Strike | Strike | Q3 earnings mid-Oct — pre-earnings window live, VP IR relationship window still open |
| HEICO | Engage | Engage | Week 4 of 14 — 10 weeks remain to Dec 17, AeroAntenna integration live |
| NCLH | Engage | Engage | New CEO 3 weeks in, Q3 = his first earnings report — dual trigger |
| SGWS | Engage | Engage | Probe resolved 2+ weeks ago — news cycle fading, act now |
| H.I.G. | Engage | Engage | Q4 LP reporting season approaching — adds urgency to EverRise trigger |
| ODP | Engage | Engage | Atlas 90-day window actively closing — this week matters |
| Herc | Engage | Engage | Q3 earnings approaching — guidance-raised pre-earnings pitch |
| Citco | Engage | Engage | Q4 = fund administration's highest-pressure NAV season |
| Frontline | Engage | Engage | October = peak hurricane season + FIRE entity stack decisions |
| SeaWorld | Standby | Standby | Howl-O-Scream peak Oct + Q3 close = dual urgency trigger (near-Strike) |
| Chico's | Standby | Standby | Q4 inventory locking mid-Oct — last window before holiday |
| Memorial | Standby | Standby | Q4 IT budget season opening at public health systems |
| Hex Federal | Standby | Standby | Federal FY Q1 started Oct 1 — federal budget flush window live |
| Pellera | Standby | Standby | Q4 = IBM partner planning season for FY2027 |

---

## ⚡ Signal Refresh Required — When Intelligence Run Completes

For each account, replace the `⚡ Why Now — refresh with Sep 22–Oct 5 signals` notice block with dated bullets from the intelligence run. Pattern: `Technical fact (date) — what it means for the seller.`

**Priority order for refresh:**
1. **Strike** — Chewy (Q3 earnings date), MasTec (Q3 earnings date), Icahn (any Nov 4 prep signals)
2. **Engage** — Lennar (any Q4 guidance signals), NCLH (Q3 earnings date), Herc (Q3 earnings date), SGWS (H2 strategy updates)
3. **Standby** — SeaWorld (Howl-O-Scream attendance data), Chico's (inventory update)

---

## Market Pulse — To Refresh

All 4 Market Pulse signals in `phase1.html` are currently placeholder `⚡ REFRESH PENDING` entries. Replace with actual Sep 22–Oct 5 signals when intelligence run delivers.

---

## Format Rules (same as Edition 06/07)

- **Light theme**: `--ground:#F4F6FA`, `--panel:#FFFFFF`, dark text `--ink:#161C2D`
- **IBM blue accent**: `--ibm-deep:#0F62FE`
- **Full-width stacked cards** (`flex-direction:column`)
- **Card structure**: `.c-left` → `.c-mid` (`.c-mid-left` + `.c-right`) → `.c-actions`
- **Section labels**: "Why Now" · "Hiring Signals" · "IBM Angle" · "What to Say" · "How to Sell" · "Do This Now"
- **Signal refresh notice** (`.c-refresh-notice`): remove when bullets are updated

---

## Intelligence Sources for Refresh
- Primary Sep 22–Oct 5 signals: intelligence run output (pending)
- Ed 07 gold standard: `ibm-sf-intel-brief/newsletters/2026-09-21/phase1.html`
- Ed 07 phase2: `ibm-sf-intel-brief/newsletters/2026-09-21/phase2.html`

---

## Folder Contents
```
2026-10-05/
├── BUILD_README.md       ← this file
├── LOGOS/                ← copy from 2026-09-21/LOGOS/ when ready
├── phase1.html           ← Account Radar (2,341 lines) ✅ Built, ⚡ Why Now needs refresh
├── phase2.html           ← Intel Brief (⬜ pending)
└── phase3.html           ← My Accounts (⬜ pending)
```
