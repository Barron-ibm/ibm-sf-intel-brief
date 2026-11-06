# SE Horizon — Edition 07 Build README

## What This Is
Canonical **Edition 07** of the SE Horizon newsletter.
Output location: `ibm-sf-intel-brief/newsletters/2026-09-17/`

## Key Facts
| Field | Value |
|---|---|
| Edition | 07 |
| Coverage Window | Sep 10–21, 2026 |
| Published Date | Sep 21, 2026 (Monday) |
| Territory | South Florida · Territory 26 |
| Total Accounts | 27 |
| Strike (t5) | 4 — Lennar, Chewy, Dycom, MasTec |
| Engage (t4) | 11 — HEICO, NCLH, SGWS, H.I.G., ODP, Herc, BK/RBI, Kforce, Citco, Frontline, Icahn |
| Standby (t3) | 12 — Lennar Mtg, JM Family, SeaWorld, Chico's, Memorial, S. Broward, Hex Federal, Hex Mining, Octave, Pellera, ANSCO, Data Mgmt Brevard |

## Format Rules — MUST MATCH EDITION 06
- **Light theme**: `--ground:#F4F6FA`, `--panel:#FFFFFF`, dark text `--ink:#161C2D`
- **IBM blue accent**: `--ibm-deep:#0F62FE`, NOT dark/navy backgrounds
- **Full-width stacked cards** (`flex-direction:column`), NOT 3-col grid
- **Card header** (`.c-left`): horizontal flex — name+meta LEFT, urgency+brands RIGHT
- **Card body** (`.c-mid`): 2-col grid — `c-mid-left` (signals) + `c-right` (sales panel)
- **Card footer** (`.c-actions`): separate bottom row with `Full Intel →` and `SNav ↗` buttons
- **Bullet markers**: `▸` (not `—`), larger font (14px), "Why Now" label
- **Talk track label**: "What to Say" (not "Suggested Talk Track")
- **Sales block label**: "How to Sell" (not "How to Drive SaaS & Transaction Sales")
- **Motion label**: "Do This Now" (not "Motion")
- **Font**: IBM Plex Sans only (not Mono/Condensed variants for body)

## Files to Build
- [ ] `phase1.html` — Account Radar (full 27 accounts, urgency-sorted)
- [ ] `phase2.html` — Intel Brief (deep-dive per account)
- [ ] `phase3.html` — My Accounts (rail + detail view)

## Build Chunks for phase1.html
Since the file is large (~2200 lines), build in these chunks:

### Chunk 1: Head + CSS + Nav + Jumpbar + Masthead + Filters + Market Pulse
### Chunk 2: Strike group (4 accounts: Lennar, Chewy, Dycom, MasTec)
### Chunk 3: Engage group part 1 (HEICO, NCLH, SGWS, H.I.G., ODP, Herc)
### Chunk 4: Engage group part 2 (BK/RBI, Kforce, Citco, Frontline, Icahn) + close group
### Chunk 5: Standby group part 1 (Lennar Mtg, JM Family, SeaWorld, Chico's, Memorial, S. Broward)
### Chunk 6: Standby group part 2 (Hex Federal, Hex Mining, Octave, Pellera, ANSCO, DMAB) + Side Dock + Footer + Script

## Intelligence Source
All account pulses, signals, angles, and talk tracks carried from the Edition 07 draft
located at `se-horizon/editions/2026-09-17/phase1.html`.
You will add fresh intelligence tomorrow (Mon Sep 21) before publish.

## Diff from Edition 06
- Lennar PROMOTED Strike (Q3 miss Sep 16, post-earnings window open)
- HEICO MOVED Engage→Standby window extended but tier dropped from Strike
- SGWS, HIG, ODP, Herc, BK/RBI, Kforce, Citco, Frontline, Icahn all added to Engage
- Standby count dropped from 18 to 12 as accounts moved up
- Market Pulse updated to Sep 10–21 window signals

## Status
- [ ] Chunk 1 — Head/CSS/Nav/Masthead
- [ ] Chunk 2 — Strike (4 accounts)
- [ ] Chunk 3 — Engage pt 1 (6 accounts)
- [ ] Chunk 4 — Engage pt 2 (5 accounts)
- [ ] Chunk 5 — Standby pt 1 (6 accounts)
- [ ] Chunk 6 — Standby pt 2 + dock + footer
- [ ] phase2.html
- [ ] phase3.html
