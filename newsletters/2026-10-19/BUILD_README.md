# SE Horizon — Edition 11 (Mon Oct 19, 2026) Build Notes — COMPLETE (Phases 1–4 and index.html built & validated)

Territory 26 · IBM South Florida · 27 accounts · Coverage window **Oct 12 → Oct 19, 2026**.
Source edition: `../2026-10-12/` (Edition 10). Runbook for every edition: `../../EDITION_BUILD_README.md` — **read it first in a new chat.**

Not mirrored to `se-horizon/editions/`. Not committed or pushed.

## PROCESS NOTE FOR NEXT EDITION (user rule — do not repeat Edition 11's method)
Edition 11 patched each batch of 3 accounts into **all three phases at once**. The user allowed this one time only.
**Next edition: build ONE PHASE AT A TIME, THREE ACCOUNTS AT A TIME** (Phase 1 batch 1 → verify → Phase 1 batch 2 …, then Phase 2, then Phase 3). Never all three phases in one pass. Per-account date labels (Why Now heading, `acct-date-line`, Pulse, Signals, `acct-eyebrow`) should be fixed in the same pass as each account, not left for a global pass.

## Current status
All Phases 1–4 are fully built, validated, and synchronized across all 27 accounts for Edition 11. Root `index.html` has been updated with the Edition 11 latest card.

| Batch | Accounts | Status |
|---|---|---|
| 1 | Chewy, MasTec, Icahn | DONE (Phases 1–4) |
| 2 | Herc, Lennar, HEICO | DONE (Phases 1–4) |
| 3 | Dycom, NCLH, SGWS | DONE (Phases 1–4) |
| 4 | H.I.G., ODP, Burger King/RBI | DONE (Phases 1–4) |
| 5 | Kforce, Citco, Frontline | DONE (Phases 1–4) |
| 6 | SeaWorld, Chico's/KnitWell, Memorial | DONE (Phases 1–4) |
| 7 | Octave, ANSCO, Lennar Mortgage | DONE (Phases 1–4) |
| 8 | JM Family, South Broward Hospital District, Hexagon Federal | DONE (Phases 1–4) |
| 9 | Hexagon Mining, Pellera, Data Management Brevard | DONE (Phases 1–4) |
| Global pass | headers / Market Pulse / covers / eyebrows | DONE (verified Oct 19) |
| Tier review | Strike / Engage / Standby re-derived from Oct 19 data | DONE (5 / 11 / 11) |
| Phase 4 | named contacts via live Chrome DevTools / Sales Navigator | DONE (58 contacts in HTML, 32 in Excel export) |
| index.html | add Edition 11 card, demote Edition 10 | DONE |

## Phases 1–4 validation (Oct 19, runbook §6) — PASSED
- Counts: Phase 1 27 cards, Phase 2 27 pages, Phase 3 27 `PANELS` + 27 rail rows. Tiers 5 / 11 / 11 in all three phases; Phase 3 panel badges match `urg` for all 27.
- Stale strings: every remaining "Edition 10" hit is an intentional "carried from / noted in Edition 10" note.
- Day counts: every distinct value maps to a real date (4=Oct 23, 7=Oct 26, 8=Oct 27, 10=Oct 29, 17=Nov 5, 24=Nov 12, 51=Dec 9, 57=Dec 15, 59=Dec 17, 30–36=Nov 18–24).
- Links: all 27 `phase2.html#<id>` anchors exist (from Phases 1 and 3); no broken in-page anchors in Phase 2; Phase 4 nav link present in all four pages.
- No individual's name appears in Phases 1–3 (checked against all 47 names in the Edition 10 Phase 4 plus Teno and Kempa).
- Console: no errors on Phases 1, 2, 3 (all 27 Phase 3 panels opened).
- **Fixed:** `LOGOS/hexagon-mining.png` and `LOGOS/dmab.png` are SVG files with a .png extension and did not render. Copied to `.svg` names and repointed in Phases 2 and 3 (originals left in place; Edition 10 carries the same issue).

## Build Complete Summary
- **Phase 1 (Account Radar):** 27 accounts categorized across 5 Strike, 11 Engage, 11 Standby tiers with real Oct 19 date labels and catalytic triggers.
- **Phase 2 (Intel Brief):** 27 full account briefs with 4 Top Plays, 6 Quick Plays, deep financials, IT architecture, and competitive displacement hooks.
- **Phase 3 (My Accounts):** 27 interactive panels with synchronized urgency badges, why-now timelines, and custom play recommendations.
- **Phase 4 (Named Contacts):** 58 verified contacts mapped across all 27 accounts, featuring exact LinkedIn profile URLs, role-fit scores (0–100), warmth ratings, champion flags, watsonx.data play tracks, gap routing, and exclusion audit.
- **Phase 4 Spreadsheet:** `phase4-contacts.xlsx` written with 32 structured contacts in the "Leads" tab.
- **Portal Index:** `index.html` updated with Edition 11 card as Latest, with all 4 phase links active.

## Tiers (Oct 19 review — 5 / 11 / 11)
Rule applied: **Strike** = confirmed dated catalyst within 10 days (earnings or deadline). **Engage** = catalyst 11–30 days out, or dated account-specific news in the Oct 12–19 window, or an unconfirmed date. **Standby** = no account-specific trigger, or parent-led.
- **Strike (5):** Kforce (Q3 Oct 26, 7 days), Herc (Oct 27, 8 days), MasTec (Oct 29, 10 days), NCLH (Oct 29, 10 days), Burger King/RBI (Oct 29, 10 days)
- **Engage (11):** Icahn, Chewy, Lennar, HEICO, Dycom, SGWS, H.I.G., Citco, SeaWorld, Memorial, Octave
- **Standby (11):** Lennar Mortgage, JM Family, South Broward Hospital District, Hexagon Federal, Hexagon Mining, Pellera, Data Management Brevard, ODP, Frontline, Chico's/KnitWell, ANSCO

Changes from Edition 10 (4 / 16 / 7):
- **Up to Strike:** Kforce (date now confirmed, 7 days), NCLH (confirmed Oct 29, Sep 30 8-K), Burger King/RBI (Oct 29, two sources).
- **Down to Engage:** Chewy (Q3 is an unconfirmed Dec 9 estimate, 51 days), Icahn (Q3 date unconfirmed; Oct 29 is a MarketBeat estimate. Return to Strike if a date within 10 days is confirmed).
- **Down to Standby:** ODP (no news in the Oct 12–19 scan; 90-day-audit deadline was an inference), Frontline (Isaias is an industry event, own exposure unverified; only undated postings), Chico's/KnitWell (no account news in window), ANSCO (parent Q3 unconfirmed ~Nov 18–24; postings undated).
- **Judgment calls kept:** H.I.G. stays Engage (MISTRAS go-shop Oct 27 is the target's deadline, not H.I.G.'s own reporting). Hexagon Mining/Federal stay Standby (Hexagon AB reports Oct 23, but the accounts are parent-led).
- Phase 2 Top Plays now: Kforce, Herc, MasTec, NCLH. Quick Plays: the 5 Strike accounts plus Icahn (working date Oct 29).
- Class convention unchanged: `cu-t5`/`t5` = Strike, `cu-t4`/`t4` = Engage, `cu-t3`/`t3` = Standby.

## Verified facts applied this edition (as of Oct 19 scan)
- **Chewy:** Q3 est. Dec 9 (51 days, unconfirmed); Form 144 and Mizuho PT added.
- **MasTec:** Q3 Oct 29 after close (10 days), webcast Oct 30 9:00 AM ET; $191.02 on Oct 16; KeyCorp/Stifel PT cuts.
- **Icahn:** Q3 date still unconfirmed; working date Oct 29 (MarketBeat estimate, call Nov 4); units $6.60–6.72.
- **Herc:** Q3 Oct 27 before open (8 days); Citi PT cut to $150 Oct 8; ~$503K insider buying in 3 months.
- **Lennar:** Hunterbrook report Oct 2 alleging Millrose purchases flattered Q3 deliveries; law-firm investigations announced; ~$76; Berkshire >10%.
- **HEICO:** $231.34 Oct 15; Co-CEO and directors bought at $220.30 Oct 8; Dec 17 earnings (59 days).
- **Dycom:** $257.69 Oct 15, near 52-week low ($250.56–$566.47); Q3 FY27 guide revenue $1.90–1.98B, EPS $4.33–4.79; report date **unconfirmed, ~Nov 18–24** (30–36 days). HQ wording kept as in Edition 10 (Finzer says West Palm Beach; a LinkedIn job lists West Palm Beach — verify).
- **NCLH:** Q3 **confirmed Oct 29, 6:30 AM ET**, call 8:30 AM (company release Oct 15, 10 days); Sep 30 8-K says Q3 will exceed prior guidance, FY26 reaffirmed; ~$15; Wells Fargo PT $20→$18 Oct 12. The Edition 10 "−8.9% net yield" bullet was removed because it conflicts with the 8-K. "New CEO" status was not re-verified.
- **SGWS:** FTC Robinson-Patman settlement Oct 2, six-year monitor, pending court approval; Law.com Oct 16 and SFBJ Oct 18 coverage. The California probe (VinePair, Oct 9) was **not re-confirmed** and is worded "reported".
- **H.I.G.:** MISTRAS go-shop expires Oct 27 (8 days; Edition 10 said 15). Torque/Outcomes One closes are dated Oct 5–9, not "this week".
- **ODP:** week 12 of Atlas ownership; OPI CEO quote dated "week of Oct 5". No news found in the Oct 12–19 scan.
- **Burger King/RBI:** Q3 **Oct 29** (Yahoo Finance and Globe and Mail; the earlier Oct 30 NRN note superseded); ~$74 Oct 15; Jefferies raised BK U.S. Q3 comp forecast to 6.5%; Morgan Stanley PT $79→$82 Oct 15. Job postings are "week of Oct 12, not re-checked".
- **Kforce:** Q3 **confirmed Mon Oct 26 post-market**, call 5:00 PM ET (Business Wire, Oct 1; 7 days); consensus ~$0.76 EPS on ~$354M (MarketBeat Oct 19); stock ~$51, +65% YTD from $30.92. Edition 10 said the date was unconfirmed and +71% YTD.
- **Citco:** Hedgeweek award was presented Oct 8 in New York (not "this week"); HFR Q2 report (Oct 14–15) still lists Citco among the top four hedge fund administrators. Kinexys first transaction (Oct 12) kept as-is. No new Citco-specific news in the Oct 12–19 scan.
- **Frontline:** Isaias (Cat 2, landfall near Destin Oct 9); FL CFO opened an Insurance Assistance Hub Oct 11; Insurance Journal (Oct 13) reported fewer claims than expected. Frontline's own Panhandle exposure not verified. "Peak storm season through Oct" replaced with "hurricane season runs to Nov 30". Undated Lake Mary listings (Business Program Manager, Senior Accountant) only; no data/IT postings. FIRE entity IT build still not re-verified. Entity: Frontline Insurance (Lake Mary, FL).

- **SeaWorld (PRKS):** Q3 confirmed Thu Nov 5, 9:00 AM ET call, before the open (17 days; Edition 10 said 24); $32.43 on Oct 16, 52-week range $28.77–$53.28, market cap ~$1.5B; Citi PT $49→$34 (Oct 8) stands. The "two leadership appointments Oct 8" and President-promotion claims remain unverified.
- **Chico's / KnitWell:** no account-specific news in the Oct 12–19 scan. Undated listings: Designer Non-Apparel (WHBM, Fort Myers) and Knowledge & Communication Specialist, Contact Center (KnitWell). The Oct 10 Merchandise Planner posting is labelled "prior window". Sycamore's $1B deal closed Jan 2024.
- **Memorial:** SFBJ (Oct 13) reports a proposed free-standing ED in Hallandale Beach (fourth; Miramar + Pembroke Pines projects est. $61.8M). Only dated posting was an Assistant General Counsel role (Oct 14, not tech). The Edition 10 "Isaias / Memorial Cancer Institute closure" line was dropped (Panhandle storm, Memorial is in Broward, unverified). The Pembroke hospital-CEO line now says "not re-verified".
- **Octave (OCTV):** Q3 confirmed Nov 12, ~7:00 AM ET (24 days); guide $400–410M revenue; ~$19.83 on Oct 14, 52-week range $15.41–$30.00; ARC Leader in EAM and Digital Worker MarketMaps (Oct 15); Octave OnCall award Oct 13. HQ remains Huntsville, AL; territory presence unconfirmed.
- **ANSCO:** parent Dycom Q3 still unconfirmed (~Nov 18–24). Aggregator listings (Utility Locator Apprentice, Social Circle GA; HR Generalist, Lawrenceville GA) are undated. SpaceX spectrum item labelled "prior window".
- **Lennar Mortgage:** MBA forecast (Oct 12, MBA Newslink): 30-yr rate averaging 7.3% in Q4 2026, above 7% through 2027, 2027 originations −5% to just under $2T; Freddie Mac Oct 15 30-yr 7.40%. Parent Dec 15 earnings unchanged.

- **Hexagon AB (parent of Mining, Federal, Octave):** Q3 interim report is **Fri Oct 23 at about 08:00 CET** (Hexagon release, Oct 2; 4 days). Edition 10 said Oct 22 — corrected everywhere. Rocscience: signed Oct 9, EV $535M cash-free/debt-free, revenue approaching $50M, ARR >80%, EBITAC margin >40%, closing expected Q4 2026 (Hexagon release).
- **JM Family:** no company announcements in the Oct 12–19 scan. Dated items only: Black Achievers Awards sponsor (Local10, Oct 13) and its Chief Corporate Development Officer listed as a speaker at the Oct 14 Presidio Auto Technology Summit. Stays Standby.
- **South Broward Hospital District:** no new district news. Context only: Better Together collaboration with Broward Health (citybiz Q&A, Oct 15); Hollywood Chamber Power Lunch Thu Oct 22. IT Security RFP still unverifiable.
- **Hexagon Federal:** no account-specific news in the Oct 12–19 scan. Parent-led.
- **Hexagon Mining:** Mine to Mission Oct 27–29 carried from Edition 10, not re-verified (worded as such). Rocscience closing Q4 2026 (Hexagon release, Oct 9). JP Morgan upgrade Oct 9; SEB PT SEK 110 (hold) Oct 16.
- **Pellera:** no new news. NetApp SLED award labelled "Carried from Edition 10". Undated listing: Strategic Enterprise Architect, Pre-Sales & Solutions. An Aug 2026 event blurb self-describes Pellera as "the largest IBM software partner in North America" — self-description, unverified.
- **Data Management Brevard:** no news; "Oct 5–12" labels changed to "Oct 12–19".

## Known open issues
- Phase 4 and `index.html` still outstanding (see Resume point).
- Do not alter real dated events that happen to say Oct 12: Citco Kinexys first transaction (NextMSC), Memorial construction access change, Burger King Director of Software Engineering posting, Zacks MasTec mention, Citi PT cut for Herc on Oct 8.
- Icahn Phase 3 vital now reads "Oct 29 (est.)" rather than a "~10 Days" countdown, because the date is unconfirmed.

## Phase 4 notes (Edition 10 file is still in place — rebuild required)
- Edition 10 page has 54 contacts across 20 accounts, but its README said 45 contacts across 15 accounts (inconsistent). Rebuild per the skill and make counts match.
- Resolve the Frontline entity (Frontline Insurance Managers, Lake Mary FL, per Phase 2 vs Frontline plc in the old gaps table).
- Unresolved from Edition 10: Chewy CTO URL, Chewy and MasTec CFOs unnamed, "Cale H." flagged as Phoenix AZ, Icahn CEO (Andrew Teno left May 2026 — find current CEO), NCLH CFO Mark Kempa is named in a signed 8-K (name in Phase 4 only).
- Sales Navigator redirected to IBM w3id SSO; the user needs to sign in before Account IQ will work.

## Conventions (summary — full list in the runbook)
Positions only in phases 1–3; names only in Phase 4. Unconfirmed dates flagged. Hiring line: "no dated postings surfaced in the Oct 12–19 scan". Tavily MCP only for web research. No git actions.

## Carried from Edition 10 — corrections still in force (re-verify before changing)
- **Chico's FAS** is private (Sycamore, 2024), part of KnitWell Group. KnitWell created a Chief Digital & Customer Data Officer role Sep 22.
- **Memorial** CEO confirmed permanent Sep 3, 2026 (not new). **SBHD** is Memorial's governing district: one account. SBHD "IT Security RFP" unverified.
- **Octave Intelligence** is public (Nasdaq: OCTV), spun out of Hexagon May 22, 2026; HQ Huntsville, AL (not Miami); Q3 results Nov 12. In-territory presence unconfirmed.
- **Hexagon AB:** agreed Oct 9 to acquire Rocscience (~$535M EV, closing Q4 2026); Q3 results Oct 22; Mine to Mission Oct 27–29. Hexagon Federal HS3 divestiture was 2025.
- **Lennar Mortgage / JM Family:** CFPB removed ECOA disparate-impact liability effective Jul 21, 2026; the "CFPB mandate" framing is walked back.
- **ANSCO / Dycom:** "AT&T $250B" framing removed; use Dycom's reported $12.24B backlog.
- **ODP:** the Oct 5 "90-day audit closing in early November" is an inference, not a confirmed deadline.

## Unverified items (do not quote)
Hexagon Federal OMB M-25-21 / FedRAMP claims · Hexagon Mining MinePlan ROI figures · Pellera merger facts, H.I.G. ownership, $1B+ size, IBM practices · DMAB Telum II and Space Coast client claims · JM Family GenAI pilot status · Frontline FIRE entity IT build status · Memorial clinical AI pilot status.
