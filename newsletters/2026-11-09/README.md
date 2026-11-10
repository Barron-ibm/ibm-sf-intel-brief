# IBM SF Intel Brief — Edition 14

**Monday, November 9, 2026 · IBM South Florida · Territory 26**
Coverage window: **Nov 3 – Nov 9, 2026** (built Nov 10). All day counts are measured from Nov 9.

A weekly intelligence brief for the IBM South Florida team. It covers all **26 accounts** in the territory: what happened this week, how urgent each account is, which IBM plays fit, and who to call.

---

## Start here

Open `index.html` in this folder (the Edition 14 hub), or the repo-root `index.html` (the master hub). Every page has the same top bar: Hub, Phase 1–4, then one page per seller and the BSS team.

| Page | What it is |
|---|---|
| `index.html` | Edition 14 hub. Links to all four phases and every seller page |
| `phase1.html` | **Phase 1 · Account Radar.** 26 account cards sorted by urgency tier, with owner and brand filters |
| `phase2.html` | **Phase 2 · Intel Brief.** One deep-dive page per account: SaaS and transaction plays, tech spend, competitors |
| `phase3.html` | **Phase 3 · My Accounts.** One panel per account with heat scores and "This Week's Move", grouped by owner |
| `phase4.html` | **Phase 4 · Named Contacts.** 212 named people across 25 accounts, grouped by account owner |
| `seller-spencer.html` | Spencer Fenelon: Burger King / RBI, H.I.G. Capital |
| `seller-shari.html` | Shari Zahed: Icahn, Herc, MasTec |
| `seller-michael.html` | Michael Sanchez: HEICO, Chewy, Memorial Healthcare System |
| `seller-hazem.html` | Hazem Marzouk and Srajan Dube: Lennar, Lennar Mortgage, Pellera |
| `seller-mijee.html` | Mijee Walker: the other 15 accounts |
| `seller-bss.html` | BSS specialists: the 11 shared accounts |
| `LOGOS/` | Account logos used by the pages |
| `BUILD_README.md` | Build log: what was done in each batch, checks run, open questions |

The pages are plain HTML and CSS. There is no build step and nothing to install. Open them in a browser. A few pages load IBM Plex fonts from Google Fonts and fall back to system fonts when offline.

---

## Urgency tiers

| Tier | Meaning | Edition 14 count |
|---|---|---|
| **Strike** | Act this week. A dated event or open window | 2 (Icahn, Octave) |
| **Engage** | Active account with a live hook | 15 |
| **Standby** | Keep warm; wait for the next trigger | 9 |

Tier labels match across Phases 1–4 and the seller pages.

---

## Phase 4 contacts

- **212 contacts**, each with a Sales Navigator lead link, and a role-fit score from 0 to 100.
- **25 of 26 accounts** have contacts. **Doral Medical & Behavioral (DMAB)** has no matching Sales Navigator company, so it shows one "Not publicly verified" card and no names.
- Contacts are Director, VP and CXO level, **pulled from Sales Navigator on Nov 10, 2026**.
- They are **carried from the Edition 14 seller pages and were not re-pulled live** for Phase 4. Confirm a person is still in role before reaching out.
- On Mijee Walker's accounts, the profile links were not opened at the time of the pull.
- Named people appear **only in Phase 4**. Phases 1–3 use positions or account owners.

---

## Notes on the data

- Items carried over from Edition 13 that were not re-checked are marked "carried from Edition 13" or "not re-verified" in the text. They are not new findings.
- **Octave Federal** is the former Hexagon US Federal. It is labelled "Octave Federal (formerly Hexagon US Federal)" in Phases 1–4.
- **Seller pages:** a few older items on the seller pages have not been reconciled with Phases 1–3 and may read as stale. The list is in `BUILD_README.md` under "Open questions".
- The BSS first names that appear in the Specialists panels of Phases 1 and 3 are carried from Edition 13.

---

## What changed from Edition 13

- **New:** six per-seller pages (five sellers plus the BSS team) that did not exist in Edition 13.
- **Contacts:** 150 → 212. 58 people carried over, 154 are new, and 92 from Edition 13 are no longer listed.
- **Tiers:** 3 Strike / 14 Engage / 9 Standby → 2 / 15 / 9. SeaWorld moved from Strike to Engage.
- **Navigation:** one identical 48px top bar on every page, with the active tab highlighted, replacing the mix of bars used before.
- **Name:** the product is now "IBM SF Intel Brief" throughout.
- **Phases 1–3** were rebuilt for the Nov 3–9 window, with day counts from Nov 9.

---

## Design

IBM Plex Sans and Plex Mono, IBM blue `#0F62FE` for accents, navy `#0F1C3A` for owner bands. Tier colours: Strike red, Engage orange, Standby blue.

*Made with IBM Bob.*
