# SE Horizon — Edition 07 Build README

## What This Is
Canonical **Edition 07** of the SE Horizon newsletter.
Output location: `ibm-sf-intel-brief/newsletters/2026-09-21/`

---

## Key Facts
| Field | Value |
|---|---|
| Edition | 07 |
| Coverage Window | Sep 10–21, 2026 |
| Published Date | Sep 21, 2026 |
| Territory | South Florida · Territory 26 |
| Total Accounts | 27 |
| Strike (4) | Lennar, Chewy, Dycom, MasTec |
| Engage (11) | HEICO, NCLH, SGWS, H.I.G., ODP, Herc, BK/RBI, Kforce, Citco, Frontline, Icahn |
| Standby (12) | Lennar Mtg, JM Family, SeaWorld, Chico's, Memorial, S. Broward, Hex Federal, Hex Mining, Octave, Pellera, ANSCO, Data Mgmt Brevard |

---

## Build Status — ALL THREE PHASES COMPLETE ✅

| File | Status | Lines | Notes |
|---|---|---|---|
| `phase1.html` | ✅ Complete | 2,303 | Account Radar — all 27 accounts, light theme, Edition 06 format |
| `phase2.html` | ✅ Complete | 4,227 | Intel Brief — all 27 accounts in Edition 06 dark-grid format |
| `phase3.html` | ✅ Complete | 3,359 | My Accounts — Aug 17 structure, SaaS+Trans added, Who to Call removed |

---

## What Changed Edition 06 → Edition 07

| Account | Ed 06 Tier | Ed 07 Tier | Key Change Sep 10–21 |
|---|---|---|---|
| Lennar | Engage | **Strike** | Q3 miss Sep 16 — gross margin 15.8% (−170 bps), ASP $372K, SG&A 9.2% |
| Chewy | Strike | Strike | S-3 filed Sep 14 (new); $50M AI savings target still live |
| Dycom | Engage | **Strike** | D.A. Davidson conference Sep 24 announced + $150M buyback authorized |
| MasTec | Strike | Strike | New VP IR Ati Modak appointed Sep 10 — relationship reset |
| HEICO | Strike | **Engage** | 14-week window to Dec 17 open; week 2 of 14 |
| NCLH | — | Engage | New CEO John Chidsey named; guidance cut |
| SGWS | — | Engage | $12.5M federal probe resolved Sep 10–21; H2 strategy published |
| H.I.G. | Engage | Engage | EverRise Lift Group formed Sep 14 — 4th deal in 2 weeks |
| ODP | Engage | Engage | GenAI pilots paused Sep 15; Atlas 90-day audit window closing |
| Herc | Engage | Engage | Talent Acquisition lead posted Sep 14; guidance raised |
| Kforce | Engage | Engage | Rule 10b5-1 buyback Sep 15; Ohio pension $4.34M position |
| SeaWorld | Standby | Standby | Howl-O-Scream season LIVE Sep 11 — key timing trigger |
| Pellera | Standby | Standby | Converge + Mainline merger confirmed → post-merger partner window |

---

## Format Rules — Edition 06 Standard (phase1 + phase2)

- **Light theme**: `--ground:#F4F6FA`, `--panel:#FFFFFF`, dark text `--ink:#161C2D`
- **IBM blue accent**: `--ibm-deep:#0F62FE`, NOT dark/navy backgrounds
- **Full-width stacked cards** (`flex-direction:column`), NOT 3-col grid
- **Card structure**: `.c-left` header (name+meta LEFT, urgency+brands RIGHT) → `.c-mid` (`.c-mid-left` signals + `.c-right` sales panel) → `.c-actions` bottom bar
- **Section labels**: "Why Now" · "Hiring Signals" · "IBM Angle" · "What to Say" · "How to Sell" · "Do This Now"
- **Bullet markers**: `▸` at 14px, NOT `—`
- **Font**: IBM Plex Sans only (not Mono/Condensed for body text)
- **Gold standard reference**: `ibm-sf-intel-brief/newsletters/2026-09-10/phase1.html` (Edition 06)

---

## Phase 3 Rules — Aug 17 Structure (phase3)

- Same left-rail + detail-panel layout as Edition 05 (`ibm-sf-intel-brief/newsletters/2026-08-17/phase3.html`)
- **Who to Call section REMOVED** from every panel (0 remaining)
- **SaaS (`--saas`) and Trans (`--trans`) CSS tokens ADDED** — filter pills + brand badges included
- `BSS_BRANDS` array includes: D&AI, Auto, Storage, P&C, **SaaS, Trans**
- `BR` const includes all six brand types
- ACCOUNTS array updated with Sep 21 hooks and correct tiers
- Panel sections per account: IBM Play Heat Scores · Big Bets · Small Bets · Competitive Threats · Why IBM Wins · Objection Handler · Displacement Map · Live Signals · This Week's Move

---

## Intelligence Sources
- Primary Sep 10–21 signals: `se-horizon/editions/2026-09-17/phase1.html` and `phase2.html`
- Edition 06 gold standard format: `ibm-sf-intel-brief/newsletters/2026-09-10/phase1.html`
- Edition 05 phase3 structure: `ibm-sf-intel-brief/newsletters/2026-08-17/phase3.html`

---

## Next Steps for Edition 08

When tomorrow's intelligence is ready:
1. Drop new signals into a source file at `se-horizon/editions/2026-09-28/` (or whatever date)
2. Build `ibm-sf-intel-brief/newsletters/2026-09-28/` using this edition as the template
3. Update tier changes in the ACCOUNTS array and diff table
4. **phase1**: refresh "Why Now" bullets with dated signals from the new coverage window
5. **phase2**: update pulse-row text and Signals sections for any tier changes
6. **phase3**: update ACCOUNTS array hooks + tier badges only (panels carry forward unless content changes)

---

## Folder Contents

```
2026-09-21/
├── BUILD_README.md       ← this file
├── LOGOS/                ← all account logos (31 files)
├── phase1.html           ← Account Radar (2,303 lines)
├── phase2.html           ← Intel Brief (4,227 lines)
└── phase3.html           ← My Accounts (3,359 lines)
```
