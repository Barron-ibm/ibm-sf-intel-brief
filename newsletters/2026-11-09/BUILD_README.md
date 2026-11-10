# IBM SF Intel Brief — Edition 14 (Mon Nov 9, 2026) Build Notes

Territory 26 · IBM South Florida · **26 accounts** · Coverage window **Nov 3 → Nov 9, 2026** (built Nov 10).
Source edition: `../2026-11-02/` (Edition 13). Runbook: `../../EDITION_BUILD_README.md`.
Not mirrored to `se-horizon/editions/`. Not committed or pushed.

## Resume point
**PHASE 1 COMPLETE. PHASE 2 COMPLETE** (26/26 pages + global pass, Chrome console clean). Nav on `seller-hazem.html` and `seller-bss.html` FIXED (Nov 10). **PHASE 3 COMPLETE** (26/26 panels, global pass done Nov 10). **PHASE 4 COMPLETE (Nov 10): 9 of 9 batches, 26/26 accounts, 212 named contacts, 212 Sales Nav links, 25 accounts with contacts + DMAB placeholder.** ALL FOUR PHASES DONE. Remaining work is only the open questions in the 'Open questions' section. User decided: Phase 4 reuses the contacts already in each seller page's `panel-p4` (pulled Nov 10); no live re-pull. Generator: `ed14-tools/p4.py add <keys>` (state in `ed14-tools/p4_done.json`).
Rule: one phase at a time, 3 accounts per pass, verify, then next batch.

## Phase 1 batches (card order in `phase1.html`)
| # | Accounts | Status |
|---|---|---|
| 1 | Burger King/RBI, H.I.G., Icahn | DONE (Nov 10) |
| 2 | Herc, MasTec, HEICO | DONE (Nov 10) |
| 3 | Chewy, Memorial, Lennar | DONE (Nov 10) |
| 4 | Lennar Mortgage, Pellera, SeaWorld | DONE (Nov 10) — SeaWorld card changed Strike→Engage (t5→t4); group counts/filters/hub tier text must be fixed in the global pass |
| 5 | Frontline, DMAB, Dycom | DONE (Nov 10) |
| 6 | ODP, ANSCO, Kforce | DONE (Nov 10) |
| 7 | Chico's, Octave, SGWS | DONE (Nov 10) |
| 8 | NCLH, Citco, JM Family | DONE (Nov 10) |
| 9 | Hexagon Mining, Hexagon Federal | DONE (Nov 10) |
| Global pass | title, `tn-badge`, nav, masthead, Market Pulse, filters, footer, tier counts (2 Strike / 15 Engage / 9 Standby, matches hub) | DONE (Nov 10) |

## Phase 2 batches (page order in `phase2.html`; base = Edition 13 phase2.html + unified nav)
Method: Phase 1's Edition 14 text is mirrored into Phase 2 (signals + Why Now, urgency, hiring, thesis, Do This Now, What to Say, tier badges, header dates). Problem / Personas / Plays / Sources reviewed by hand. Helper: `/tmp/ed14/lib3.py` (ephemeral).
Ed13 check: for all 26 accounts, Ed13 Phase 2 text matched Ed13 Phase 1 on those fields, so mirroring is the same method as before.
| # | Accounts | Status |
|---|---|---|
| Global | `<title>`, cover page, Top Plays, SVG text, footer, dropdown | DONE (Nov 10) |
| 1 | BK, H.I.G., Icahn | DONE (Nov 10) |
| 2 | Herc, MasTec, HEICO | DONE (Nov 10) |
| 3 | Chewy, Memorial, Lennar | DONE (Nov 10) |
| 4 | Lennar Mortgage (`lennarmtg`), Pellera, SeaWorld | DONE (Nov 10) |
| 5 | Frontline, DMAB, Dycom | DONE (Nov 10) |
| 6 | ODP, ANSCO, Kforce | DONE (Nov 10) |
| 7 | Chico's, Octave, SGWS | DONE (Nov 10) |
| 8 | NCLH, Citco, JM Family | DONE (Nov 10) |
| 9 | Hexagon Mining, Octave Federal (`hexfed`) | DONE (Nov 10) |

Phase 2 batch 1 notes: BK "5 RBI brands" -> 4 and "16,000+ stores" removed from play text (not supported). Problem/Personas/Sources otherwise unchanged and still valid.

Phase 2 batch 2 notes: Herc Problem/Persona/Supporting play rewritten, because Ed13 said Herc and H&E ran separate systems and Phase 1 now says the IT integration is complete (Stock Titan); text now asks about using the data and says to confirm in discovery. MasTec Problem: Superior and margin figures labeled 'not re-checked'. HEICO: no change needed beyond mirror. Remaining 'Edition 13' strings on these pages are intentional 'carried, not re-checked' labels.

Phase 2 batch 3 notes: Chewy Problem said stock 'near $21 vs $38.95 high'; changed to the Nov 4-5 close near $23 (+8% on the week, ~38% below the 52-week high, Investing.com) to match Phase 1. Memorial and Lennar needed no Problem/Persona/Source changes. Remaining 'Oct 26' / 'Nov 2' strings on Chewy and Lennar are real dated facts (insider sale Nov 2, Oct 26 credit-line amendment, short-interest date).

Phase 2 batch 4 notes: Lennar Mortgage Problem had the 7.41% Freddie Mac rate as current; now labeled 'earlier edition, HousingWire, not re-checked' (matches Phase 1). SeaWorld page now Engage (badge + play tier), Q3 Nov 5. Pellera stays Standby; its 'not re-verified' list kept. Page key is `lennarmtg` (Phase 1 card is `lenmar`).

Phase 2 batch 5 notes: Frontline OpenPages play text and CIO persona now say the 'new insurer still building its IT stack' is not re-verified (matches Phase 1). DMAB and Dycom: mirror only. DMAB identity (ColoBarn / Data Management Associates of Brevard) still unconfirmed.

Phase 2 batch 6 notes: mirror only; reviewed Problem/Personas/plays/Sources for ODP, ANSCO, Kforce and found nothing stale. ODP 'about 13 weeks' count stays dropped. Kforce 'Oct 26' and 'Edition 13' strings are the Q3 date and a carried-label.

Phase 2 batch 7 notes: Octave Problem said Q3 in 10 days -> 3 days (Nov 12); entry line 'warm intro through Hexagon AB' replaced (Octave is independent of Hexagon AB); Problem now says independent of Hexagon AB; Hexagon AB source link relabeled as history of the May 2026 split. Octave headcount/HQ conflicts kept as flags. Chico's and SGWS: mirror only (SGWS RNDC-Breakthru merger kept as a question, not a fact).

Phase 2 batch 8 notes: mirror only; NCLH, Citco, JM Family Problem/Personas/plays/Sources reviewed, nothing stale. NCLH new CFO Jan 1 = 53 days is now on the page. Citco day counts (13/19/32) come from Phase 1. Citco 'modernization program' is carried from Ed13 (also in Phase 1) and not re-verified. JM Family DRIVE hook is 'ask, don't assert'.

Phase 2 batch 9 notes: Hexagon Mining mirror only (its Hexagon AB parent-level door is kept for Mining only). Octave Federal (`hexfed`) page: name now 'Octave Federal (formerly Hexagon US Federal)'; Problem, Entry line ('Octave (parent)'), Suggested Search and Sources relabeled; Hexagon AB Newsroom link relabeled as history of the May 2026 split. Cover pill 'Hex Federal' and cover text still to fix in the global pass.

Phase 2 global pass notes: title/cover/footer now IBM SF Intel Brief, Edition 14, Nov 9. Top Plays rewritten from the pages: Octave (Strike, Nov 12), Icahn (Strike, notes callable Nov 15), SeaWorld (Engage, Q3 Nov 5), Kforce (Engage, J.P. Morgan conf Nov 17). Quick Plays table: Octave, Icahn, SeaWorld, Kforce, MasTec, Lennar Mtg, H.I.G., Dycom. Cover pill 'Hex Federal' -> 'Octave Federal'. Hub Phase 2 tile now says 26 accounts (both hub copies). Browser check: 26 pages, 2 Strike / 15 Engage / 9 Standby, 26 cover pills all resolve, no horizontal overflow, console clean. All 26 Phase 1 'Full Intel' links resolve to a Phase 2 page. the old product name had reappeared in seller-hazem and seller-bss; replaced again.

## Phase 3 batches (`phase3.html`; base = Edition 13 phase3.html + unified nav, Edition 14 title/banner)
Method: same as Phase 2. Phase 1's Edition 14 text is mirrored into each Phase 3 panel (header meta, Tier vital, thesis + opener, Now / Sell / Motion, rail hook and tier). Heat-score names, scores, deal sizes and conviction lines reviewed by hand. Helper: `ed14-tools/lib4.py` (`mirror3`, `heat`, `show`). Panels not yet reached still carry Edition 13 text; the `phase3.html` link in the nav is active but the page is not final until all 9 batches and the global pass are done.
| # | Accounts | Status |
|---|---|---|
| Base | nav (unified, Phase 3 active), `<title>`, banner, fallback panel date | DONE (Nov 10) |
| 1 | BK, H.I.G., Icahn | DONE (Nov 10) |
| 2 | Herc, MasTec, HEICO | DONE (Nov 10) |
| 3 | Chewy, Memorial, Lennar | DONE (Nov 10) |
| 4 | Lennar Mortgage (`lenmar`), Pellera, SeaWorld | DONE (Nov 10) |
| 5 | Frontline, DMAB, Dycom | DONE (Nov 10) |
| 6 | ODP, ANSCO, Kforce | DONE (Nov 10) |
| 7 | Chico's, Octave, SGWS | DONE (Nov 10) |
| 8 | NCLH, Citco, JM Family | DONE (Nov 10) |
| 9 | Hexagon Mining, Octave Federal (`hexfed`) | DONE (Nov 10) |
| Global | rail group headers, hub tile numbers/links, remove `soon` from Phase 3 link on all pages | DONE (Nov 10) |

Phase 3 batch 1 notes: Icahn heat card 1 rewritten (post-results loss quarter, CVR/Marathon deal) and card 2 conviction updated; other heat cards, scores and deal sizes carried from Edition 13 (unchanged, not re-scored). H.I.G. heat card 1 now says the 150+ count is not re-verified. BK heat cards carried; Phase 1 text already supports them. Hiring vital now reads "Nov 3 – 9 scan" with "None verified" for all three. Panel `<div>` balance is +2 per panel, same as the Edition 13 originals.

Phase 3 batch 2 notes: Herc heat cards 1-3 rewritten, because Ed13 said the H&E systems were still separate and Phase 1 now says the IT integration is complete (Stock Titan, not confirmed by Herc); card 3 renamed "Cover Any Systems Still Left to Join" and says to confirm in discovery. Herc Hiring vital: 2 open roles, undated. MasTec heat card 1 now includes the Nov 5 pause of large acquisition talks (buybacks first); cards 2-3 carried (Superior and Chief Data Center Officer items already labeled not re-verified). HEICO heat card 1 adds the credit line raise ($2.0B to $2.2B, up to $3.0B); Hiring vital "light signals only". Scores and deal sizes carried from Ed13, not re-scored. Chrome: all 3 panels open, console clean.

Phase 3 batch 3 notes: Chewy heat card 2 now uses the Nov 4-5 close near $23 (+8% on the week, ~38% below the 52-week high), replacing 'near $21'; card 1 notes the Nov 2 and Nov 4 insider sales were pre-set 10b5-1 plans, not a fresh signal. Memorial card 3 uses the Nov 6 Mobile Health Program results (62% fewer admissions, ~$4.3M saved in 2025) as an opener, not a buying signal. Lennar card 1 uses the Q4 guide gap (22,000-23,000 deliveries vs 19,500-20,500 orders) and earnings Dec 16 (TipRanks) / Dec 15 (Yahoo est.) = 37 days, replacing '43 days'; card 2 labels the 9.2% overhead figure as an Edition 13 figure, not re-checked. Berkshire and Millrose items are carried and labeled in the Phase 1 text, not re-checked. Lennar Specialists vital (BSS-covered names) left as in Ed13. FIX: mirror3 briefly wrote 'Engage — ...' in the Tier vital sub-line (duplicate tier word, since Phase 1's urgency line starts with the tier). Removed the prefix on all 9 panels so far and in lib4.py.

Phase 3 batch 4 notes: SeaWorld panel badge changed Strike -> Engage (matches Phase 1/2; rail entry also Engage). Q3 reported Nov 5: attendance -4.7%, rev/guest $78.29 (+3.8%), 2027 passes up more than 15%; heat cards 1-2 rewritten, card 3 (Maximo) carried. Lennar Mortgage: Nov 20 Kroll credit-monitoring deadline (11 days) added as a customer deadline, not a Lennar event; heat cards 1-3 conviction lines updated; 7.41% Freddie Mac rate labeled earlier-edition, not re-checked; parent earnings Dec 16 (Yahoo est. Dec 15) in the header; 'Dec 15' in the Do This Now line is the Yahoo estimate. Pellera: Hiring vital '2 postings' (Sr. Enterprise AE Oct 30, Pune engineer ~5 days old); card 1 notes IBM-skills hiring; Converge/Mainline merger, revenue, headcount and H.I.G. ownership stay 'not re-verified' as in Phase 1. Rail tier counts in the Phase 3 account list now 2 Strike / 15 Engage / 9 Standby (matches Phase 1 and the hub). Specialists vital still lists BSS first names for Lennar, Lennar Mortgage and Pellera (as in Ed13 and Phase 1); open question to the user.

Phase 3 batch 5 notes: Frontline hurricane count now 21 days (Ed13 panel said 28); thesis and Sell line now label the 'company still building its systems' claim as carried from Oct 5, not re-verified (matches Phase 1/2); heat card 2 adds the Oct 29 FLOIR rate-decrease note. DMAB: 'see the check above' pointed at a Phase 1 box that Phase 3 does not have, so the Now line now states the identity check itself (ColoBarn / Data Management Associates of Brevard, not confirmed); heat card 3 says to pursue only after identity is confirmed. DMAB uses a different panel layout (heat-prod/heat-copy, 'Opportunity Heat'), so its panel div balance is -1, same as the Ed13 original; I used a direct text patch for it. Dycom: header 'about Nov 24 (15 days)', stock low $186.25 Nov 5, $150M of work moved to FY28; heat cards 1-2 updated; Power Solutions dated about Nov 2025 (not new). ANSCO still to do in batch 6 (Dycom card says 'plan together with ANSCO').

Phase 3 batch 6 notes: ODP header now 'CEO since Dec 2025' (was 'New CEO'); heat cards 1-2 updated (Veyer fold-in; CEO in the job since about Dec 2025); Now line labels the paused GenAI pilots and open CFO/FP&A role as carried, not re-checked; Hiring vital 'Retail roles only'. ANSCO: parent Q3 about Nov 24 = 15 days (Ed13 panel said 22), header and rail hook updated; Hiring vital 'See brief / Valdosta posting undated, not re-found'; Georgia lease news labeled carried. Kforce: Q3 Oct 26 unchanged, J.P. Morgan conference Nov 17 (8 days) added; heat card 1 notes the $0.12 one-time insurance gain. EXCHANGE CONFLICT: Phase 1 and Phase 2 Ed14 say 'NYSE: KFRC' but Ed13 said 'NASDAQ: KFRC' (Kforce is Nasdaq-listed); Phase 3 keeps NASDAQ. Phase 1 and 2 still say NYSE and were not changed; ask the user. Tooling: lib4.mirror3 now accepts 'SaaS Entry (two plays)' style labels.

Phase 3 batch 7 notes: Octave stays Strike; Q3 results Thu Nov 12 = 3 days in the Tier vital, thesis, opener, heat cards 1 and Now line; thesis says Octave is independent of Hexagon AB and Octave Federal (formerly Hexagon US Federal) is a separate account to coordinate with; Q3 guide $400-410M in card 2; MAIRE and Attune Facilities labeled undated in card 3. Heat scores and deal sizes carried from Ed13, not re-scored. SGWS: header 'FTC deal filed Oct 2 (38 days ago), court approval still pending'; heat card 1 says the order is still a proposed consent decree and no approval was found Nov 3-9; the RNDC/Breakthru merger and the Reyes takeover are not in the Phase 3 panel (they are in Phase 1/2). Chico's: Standby; hiring vital '1 dated posting' (WHBM planner Oct 10 = 30 days); CDO role Sep 22 = 48 days; card 3 says the holiday-stock claim was never verified. Specialists vital for Octave and SGWS still lists BSS first names (as in Ed13 and Phase 1); open question. Chrome: all 3 panels open with 3 heat cards and a Move block, no stale strings, console clean. Screenshots not looked at.

Phase 3 batch 8 notes: NCLH header/Tier vital/thesis/opener/Now/Sell/Motion mirrored from Phase 1; the CFO change (Chief Strategy Officer becomes CFO Jan 1 = 53 days, announced Oct 29, missed in Ed13) is now in the Tier vital, opener and heat card 1; $325M new savings and the 'onshore and through AI' analyst question in cards 1-2; card 3 says the revenue management system timing is not stated, so ask (the Ed13 card implied it was under way). Citco: day counts 13 (Oct 27 report), asset-figure conflict ($1.2T vs $840B) shown in the header; Hiring vital '1 dated posting' (Mumbai fund accountant Nov 6 = 3 days, routine, outside South Florida); card 1 uses the Oct 27 report (funds over $10B took about 69% of new money), card 2 labeled carried from Ed13, not re-checked. JM Family: header shows the $16B vs $24.7B conflict; Hiring vital 'Interns only'; card 1 labeled carried from Oct 5, not re-verified; card 2 renamed 'Join Data Across Business Units' and now cites the DRIVE Data Team intern ads as ask-don't-assert (the Ed13 'five units, five data stores' claim is labeled carried, not re-checked). Heat scores and deal sizes carried from Ed13, not re-scored. Specialists vital still lists BSS first names on all three (as in Ed13 and Phase 1); open question. Panels +2 on div balance like the rest. Chrome: all 3 panels open with 3 heat cards and a Move block, no stale strings, console clean. Screenshots not looked at.

Phase 3 batch 9 notes: Hexagon Mining mirrored from Phase 1 (Q3 Fri Oct 23 = 17 days; Waygate closed Nov 2 labeled a parent-level item in Manufacturing Intelligence, not Mining; Rocscience Oct 9 = 31 days; Mine to Mission Oct 27-29 dates labeled carried from Ed10, not verified); Hiring vital 'None verified' with the ~1,500 Mining staff figure called a database number, not a posting. Octave Federal: panel title, rail name and logo alt renamed 'Octave Federal (formerly Hexagon US Federal)' (key stays `hexfed`); the Ed13 'part of Hexagon AB' header and 'one IBM-Hexagon story across Mining, Federal and Octave' wording are gone; panel now says it is a subsidiary of Octave, go in through Octave (Q3 Thu Nov 12 = 3 days), and Hexagon Mining is a separate Hexagon AB account; Hiring vital '1 undated posting' (Pre-Sales Engineer, Geospatial Solutions, location not checked); FedRAMP and OMB M-25-21 claims labeled carried from Oct 5, not verified. Heat scores and deal sizes carried from Ed13, not re-scored; note the Ed13 deal-size 'Transaction' label on the Octave Federal governance card and 'SaaS' label on its FlashSystem card look swapped vs the brand tag (left unchanged, flagged). Specialists vital still lists BSS first names (open question). Chrome (page ids changed after a browser reconnect): all 26 panels open, each with heat cards and a Move block, no stale strings, console clean. Screenshots not looked at.

Phase 3 global pass + nav unification (Nov 10): (1) Octave Federal heat cards 1-2: the Ed13 deal-size labels were swapped against the brand tags; now governance = 'SaaS: $220K-$480K/yr, D&AI' and FlashSystem = 'Transaction: $900K-$2.5M, Storage' (amounts unchanged, still not re-scored). (2) NAV: the `<style id="nav-unify">` block was one of three different variants (48px vs 51px height, three font stacks, `tn-right` shown/hidden). It is now ONE identical canonical block on all 11 pages (both hubs, phase1-3, six seller pages): 48px, IBM blue #0F62FE, IBM Plex Sans, 9.5px links, `tn-right` hidden. Phase 2 adds a tiny `nav-unify-p2` rule that re-shows `tn-right` only because it holds the Accounts jump dropdown. Phase 1 `.jumpbar` and Phase 2 `.brand-filter-bar` sticky offsets changed 51px -> 48px; Phase 3 shell height calc(100vh - 85px) so it fits with no page scroll. (3) The Phase 3 nav link is live (no `soon`) on all pages; Phase 4 stays greyed. (4) HUB (both copies): Phase 3 tile now links to phase3.html (was `#`) and reads '26 account panels' with Icahn + Octave Strike tags (was '3 full panels'); Phase 4 tile greyed and reads 'Not built yet' until Phase 4 exists. All three Territory View tiles and all six seller cards resolve to existing files. (5) Rail groups (computed from the ACCOUNTS array): Spencer 2, Shari 3, Michael 3, Hazem 3, Mijee 15 = 26. Chrome checks on every page: nav height 48, same border colour and font, correct active tab, no horizontal overflow, only Phase 4 greyed, sticky bars flush at 48px, console clean. navcheck.py: nav present on all 11 pages, no missing targets except Phase 2's #key anchors (false positive). Backups of the pre-change files are in /tmp/ed14_bak (temporary). Screenshots not looked at.

Nav fix notes (Nov 10): `seller-hazem.html` and `seller-bss.html` now carry the unified `<nav class="topnav">` and `<style id="nav-unify">` copied from `seller-michael.html`, with the right active tab; the hero "← Master Hub" link now points to `../../index.html`. `navcheck.py` shows all 10 pages with a nav (Phase 2's "missing" entries are `#key` anchors, a known false positive). "the old product name" count is 0 on every page.

Phase 4 (named contacts), 3 accounts per batch. Source = Edition 14 seller-page `panel-p4` blocks (owner pages: 26 accounts, 213 contacts; BSS page repeats 11 accounts with identical names). Layout from Edition 13 phase4.html, canonical nav, the old product name removed. DMAB has no Sales Nav company, so it shows the single 'Not publicly verified' card.
| Batch | Accounts | Status |
|---|---|---|
| 1 | bk, hig, icahn | DONE Nov 10: 18 contacts, 18 Sales Nav links, tiers Engage/Engage/Strike, nav 48px with Phase 4 active, console clean, old-name count = 0. Screenshot not looked at. |
| 2 | herc, mastec, heico | DONE Nov 10: 24 contacts (6+6+12), 24 Sales Nav links; names/titles/scores/why/URLs match the seller pages exactly; page total now 42 contacts across 6 accounts; Chrome: nav 48px, Phase 4 active, no overflow, jump links resolve, console clean, old-name count = 0. Screenshot not looked at. |
| 3 | chewy, memorial, lennar | DONE Nov 10: 36 contacts (12+12+12), 36 Sales Nav links; match the seller pages exactly; page total 78 contacts across 9 accounts (1 Strike, 8 Engage); Chrome: nav 48px, Phase 4 active, no overflow, jump links resolve, console clean, old-name count = 0. Screenshot not looked at. |
| 4 | lenmar, pellera, seaworld | DONE Nov 10: 28 contacts (10+10+8), 28 Sales Nav links; match the seller pages exactly; page total 106 contacts across 12 accounts (1 Strike, 10 Engage, 1 Standby); Hazem's 3 accounts complete and Mijee band started. SeaWorld links are marked 'links not yet opened' in the source and in the header. Chrome: nav 48px, Phase 4 active, no overflow, jump links resolve, console clean, old-name count = 0. Screenshot not looked at. |
| 5 | frontline, dmab, dycom | DONE Nov 10: Frontline 8, Dycom 8 (16 Sales Nav links); DMAB = one 'Not publicly verified' placeholder card (no matching Sales Nav company; page ID 28941786 returns Page Not Found; confirm the legal entity name), counted as 0 contacts. All match the seller page. Page total 122 contacts across 15 accounts, 14 with contacts (1 Strike, 11 Engage, 3 Standby). Chrome: nav 48px, Phase 4 active, no overflow, jump links resolve, console clean, old-name count = 0. Screenshot not looked at. |
| 6 | odp, ansco, kforce | DONE Nov 10: 24 contacts (8+8+8), 24 Sales Nav links; match the seller page exactly; page total 146 contacts across 18 accounts, 17 with contacts (1 Strike, 12 Engage, 5 Standby). Chrome: nav 48px, Phase 4 active, no overflow, jump links resolve, console clean, old-name count = 0. Screenshot not looked at. |
| 7 | chicos, octave, sgws | DONE Nov 10: 26 contacts (8+10+8), 26 Sales Nav links; match the seller page exactly; page total 172 contacts across 21 accounts, 20 with contacts (2 Strike, 13 Engage, 6 Standby). Chrome: nav 48px, Phase 4 active, no overflow, jump links resolve, console clean, old-name count = 0. Screenshot not looked at. |
| 8 | nclh, citco, jmf | DONE Nov 10: 24 contacts (8+8+8), 24 Sales Nav links; match the seller page exactly; page total 196 contacts across 24 accounts, 23 with contacts (2 Strike, 15 Engage, 7 Standby). Chrome: nav 48px, Phase 4 active, no overflow, jump links resolve, console clean, old-name count = 0. Screenshot not looked at. |
| 9 | hexmin, hexfed | DONE Nov 10: 16 contacts (8+8), 16 Sales Nav links; match the seller page exactly. Octave Federal header reads 'Octave Federal (formerly Hexagon US Federal)'. FINAL page total: 212 contacts, 212 links, 25 of 26 accounts with contacts (DMAB = placeholder), tiers 2 Strike / 15 Engage / 9 Standby, 26 sections. |

## Batch 1 notes
- BK: Q3 was Oct 29; nothing new from RBI in Nov 3–9. Burger King China JV is **not** new: closed Feb 2, 2026 (CPE 83%, RBI 17%).
- H.I.G.: MISTRAS vote Nov 24 = 15 days. No new H.I.G. deals found in Nov 3–9 (latest dated: L4A majority stake, Oct 22).
- Icahn: Q3 reported Nov 3. Net loss $225M / $0.31 per unit vs $287M profit a year ago; adj. EBITDA loss $214M; revenue $3.17B. CVR Energy signed a $4.2B Marathon refinery purchase on Nov 2. IEP senior notes (due May 2027) callable at par from Nov 15.

## Batch 2 notes
- Herc: Q3 was Tue Oct 27 (not Nov 5). Beat + raised outlook; analyst target raises Nov 3 week; CEO change Jan 1 = 53 days; IT integration of H&E complete. Hiring: Digital Logistics Platforms mgr + Cloud/Platform Eng mgr (undated).
- MasTec: new Nov 5 = suspended large acquisition talks, buyback priority ($250M). Price targets cut after Q3. Acquisitions of Power Delivery/Pipeline were announced Oct 29, not this week.
- HEICO: nothing new Nov 3-9. "+23.1%" is the Aug 25 fiscal Q3 report. Next earnings ~Dec 17 = 38 days (estimate). Market cap sources conflict.

## Batch 3 notes
- Chewy: nothing from the company; stock ~$23 (+8% wk); CEO sold 23,002 sh Nov 2 and CAO sold 4,815 sh Nov 4 (10b5-1 plans). Earnings ~Dec 9 = 30 days (estimate).
- Memorial: Nov 6 Mobile Health Program release (62% fewer admissions, $4.3M saved 2025). CEO made permanent Sep 3 = 67 days. Venture Center $69M buy is a Sep 11 report.
- Lennar: 8-K Oct 29 (credit line to $3.795B, $4.545B w/ accordion, Oct 26 amendment). Stock -5.4% Nov 3, sector-wide. Earnings Dec 16 confirmed (TipRanks) / Dec 15 (Yahoo est) = 37 days. Berkshire + Millrose items carried, not re-checked.

## Batch 4 notes
- Lennar Mortgage: Ramkissoon v. Lennar Corp (1:26-cv-25518) combines both incidents; Oct 21 docket entry 64 text not public; mediation referred, no result. Kroll monitoring deadline Nov 20 = 11 days. Stock -5.4% Nov 3, then +7.1% Nov 4 (WSJ).
- Pellera: no new news. Hiring: Sr. Enterprise AE (Oct 30), System Engineer Pune (IBM certs a plus).
- SeaWorld: Q3 reported Nov 5 (rev $506.5M -1.1%, NI $80.0M -10.5%, attendance -4.7%, rev/guest +3.8%). Moved Strike→Engage because the Nov 5 event has passed. Octave (Nov 12, 3 days) is the likely second Strike - verify in batch 7. Hub says 2 Strike (Icahn + ?).

## Batch 5 notes
- Frontline: nothing company-specific. Hurricane season ends Nov 30 = 21 days. FLOIR Oct 29: more homeowner rate decreases in Nov/Dec. Headcount ~563 (+20%).
- DMAB: nothing found; identity of company still unconfirmed (ColoBarn / Data Management Associates of Brevard).
- Dycom: earnings est. Nov 24 (MarketBeat) / Nov 25 (Yahoo) = 15-16 days. Stock 52-wk low $186.25 Nov 5, +7.6% Nov 6 to $207.52. Also bought Power Solutions (Simply Wall St) - Ed13 only named NTI.

## Batch 6 notes
- ODP: no news. Atlas deal closed Dec 2025; the Ed13 "13 weeks" count could not be reproduced and was dropped. Nov 3 lead-plaintiff deadline passed (no outcome found). Related Group $177M loan on the OLD HQ site is not an ODP signal. CEO named only by position.
- ANSCO: no news. Parent earnings ~Nov 24 (MarketBeat) / Nov 25 (Yahoo) = 15-16 days. Valdosta laborer posting not re-found.
- Kforce: new Nov 3 = J.P. Morgan conf Nov 17 (8 days), Truist Dec 11/14. Director Form 144 (overlapping figures). Q3 Oct 26 unchanged.
- Dycom: Power Solutions acquisition dated ~Nov 2025 (company database), not new.

## Batch 7 notes
- Octave: Q3 results Thu Nov 12 = 3 days (Ed13 said 10, counted from Nov 2). Stays Strike. Q3 guide $400–410M (2–4% organic cc); FY outlook cut Aug 12; stock ~$21.12 Nov 9. Employee count conflicts (7,200 in Ed13 vs ~3,771 in a database) so none quoted; HQ conflicts (Huntsville vs Madison, AL). Octave Specialty Group (OSG, insurer) is a different company. MAIRE AI collaboration and Attune Facilities are undated.
- SGWS: day counts fixed: FTC filing Oct 2 = 38 days, Reyes takeover Jan 1 = 53 days. New: Legal 500 article Nov 9 (consent decree still proposed). RNDC + Breakthru merger (Wine Spectator/Shanken) — announcement date NOT confirmed; other sources show RNDC in Chapter 11 breakup, so flagged as a question, not a fact. Bacardi/Reyes, Clare Rose, California review labeled "before the window".
- Chico's: no company news Nov 3–9; Standby. Sep 22 CDO role = 48 days; Oct 10 planner posting = 30 days.

## Batch 8 notes
- NCLH: nothing new from the company Nov 3–9. Added CFO change announced Oct 29 (Chief Strategy Officer becomes CFO Jan 1 = 53 days; outgoing CFO advisor to Jun 30) — missed in Ed13. Q3: rev $2.95B (+0.3%), adj EBITDA $937M, adj EPS $1.12, occupancy 106.5%; FY EBITDA ~$2.55B; 2027 net yield guide +1–2%; $325M new cost savings. Stock $18.43 close Nov 9. Q4 weak-yield items carried. Stays Engage.
- Citco: no new company news Nov 3–9. Day counts re-derived: Oct 27 = 13, Oct 21 SPV head = 19, Oct 8 award = 32. Hiring: Mumbai fund accountant posted Nov 6 (routine). Asset figure conflicts ($1.2T carried vs $840B in a job ad). Stays Engage.
- JM Family: no new business news; stays Standby. Found "DRIVE" data program via summer-2027 Southeast Toyota Finance intern ads (undated, ask-don't-assert). Revenue conflicts ($16B description vs $24.7B intern site).
- Names rule: CFO/CEO referred to by position only.

## Batch 9 notes
- Hexagon Mining: nothing Mining-specific Nov 3–9; Standby. Hexagon AB Q3 was Fri Oct 23 (17 days; confirmed). NEW vs Ed13: Waygate acquisition ($1.45B, from Baker Hughes) CLOSED Nov 2, consolidated Nov 1 (Ed13 said Q4). Sits in Manufacturing Intelligence, parent-level only. Rocscience Oct 9 = 31 days. Next Hexagon report ~Jan 28, 2027 (estimate). Hexagon Composites ASA (Oslo) is a different company.
- Hexagon US Federal: CORRECTION to Ed13 — rebranded **Octave Federal** in May 2026 and is a subsidiary of Octave, not Hexagon AB. Card now says so; angle/motion changed to go in via Octave (results Nov 12 = 3 days). Account name on the card still reads "Hexagon US Federal" (key `hexfed`) — decide in global pass whether to rename to "Octave Federal (formerly Hexagon US Federal)". Octave card's "ask Hexagon AB parent for a warm introduction" removed (Octave is independent of Hexagon AB).
- Hexagon Mining "Work with Hexagon AB parent-level door" kept for Mining only.
- Cross-account: Octave, Hexagon Mining, Octave Federal should no longer be pitched as one Hexagon story. Check Phase 2/3 text for the same.

## Phase 1 global pass notes
- Branding: the old product name → IBM SF Intel Brief, Edition 14, Nov 9, coverage Nov 3–9 (title, nav, badge, masthead, Market Pulse header, footer).
- Market Pulse rewritten (4 signals), no personal names (owners only). Removed Ed13 claims "Jim", SeaWorld-as-Strike, "Hexagon family one parent-level conversation".
- Counts verified in browser: 26 cards; 2 Strike (Icahn, Octave) / 15 Engage / 9 Standby; Mijee group sub-line fixed to 1 Strike · 6 Engage · 8 Standby. Other group sub-lines already correct.
- Hexagon US Federal renamed "Octave Federal (formerly Hexagon US Federal)" on card, filter pill and side dock; hub BSS/Mijee text renamed too. Key stays `hexfed`.
- Chrome console: no errors or warnings on reload. Phase 1 tile in both hubs now links to phase1.html.
- Phase 2/3/4 links in phase1.html (Full Intel → phase2.html#key) still point to the old 3-account phase2.html until Phase 2 is rebuilt.

## Inconsistencies found in already-built Edition 14 pages (not yet fixed)
- Hub signal strip and `seller-spencer.html` present the Burger King China JV as this week's news ("China JV signed"). It closed Feb 2, 2026.
- `seller-shari.html` says Icahn "Net loss $150M vs $22M loss YoY". Filing shows net loss attributable to IEP $225M vs $287M **profit**.


## Phase 4 wrap-up (Nov 10)
- `phase4.html` built from the contacts already on the Edition 14 seller pages (`panel-p4`, pulled Nov 10). Not re-pulled live. Generator: `ed14-tools/p4.py` (state `ed14-tools/p4_done.json`). Per account, names/titles/scores/why/URLs were compared against the seller page after every batch: all identical.
- Source note: the owner pages hold 213 contact cards (212 real + the DMAB placeholder). `seller-bss.html` repeats 11 of those accounts with identical names. Frontline's header says '5 of 8 name-matched; 3 out-of-network profiles hide the name' (copied from the source).
- Nav: the Phase 4 link is live (no `soon`) on all 11 pages; both hub Phase 4 tiles now link to phase4.html and read '212 named contacts · 25 of 26 accounts'.
- FIX during wrap-up: `seller-bss.html` had silently lost its canonical nav (reverted to the old `<div class="topnav">` variant with a different link set and a hub link of `index.html`) and its Phase 4 panel text had changed 'links not yet opened' -> 'Verified live' (an outside edit, 12:56). I restored the canonical `<nav class="topnav">` block from `seller-michael.html` (BSS Team active) and set the hero-back link to `../../index.html`. The panel wording change was left as the user's edit.
- Final checks (Chrome, Nov 10): every page nav height 48, canonical font and blue top border, correct active tab, no `soon` link, no horizontal overflow, console clean. `navcheck.py`: nav present on all 12 files, only Phase 2's `#key` false positives. Every `href` in both hubs and the 11 pages resolves to a file. old-name count = 0 in all of them. Screenshots were never looked at.
- Nothing committed or pushed. Edits only under `ibm-sf-intel-brief/` plus `ed14-tools/`.

## Open questions for the user
1. BSS first names (Alyssa, Gavin, William, Rick, Kevin) still appear in Phases 1 and 3 Specialists vitals; this conflicts with 'named people only in Phase 4'.
2. Kforce exchange: Phases 1-2 say NYSE: KFRC, Phase 3 says NASDAQ: KFRC. Unverified.
3. Seller-page content that looks stale: Burger King 'China JV signed' (closed Feb 2, 2026); Icahn '$150M loss vs $22M' (actual $225M loss vs $287M profit); Herc 'Q3 beat Nov 5' (Q3 was Oct 27); HEICO '+23.1%' (from Aug 25); MasTec '2 acquisitions this week' (announced Oct 29). Seller pages still say 'Hexagon US Federal' in many places.
4. Stale `README.md` and `CONTINUE_README.md` in this folder still say the old product name.
5. Hub alert and seller cards name people (e.g. CFO Robert Flint, Aaron Birnbaum); not changed.
6. Contacts were carried from the seller pages, not re-pulled live; Mijee's accounts' links were noted 'not yet opened' at the time.

## Mark Wylie (added Nov 10)

- Mark Wylie is an IBM Technology Sales Leader, not a Sales Navigator contact (searches at NCLH, JM Family, SGWS and IBM found no match). He is added as "Mark Wylie (Technology Sales Leader)" to the Work with / specialist line for NCLH, SGWS and JM Family in `phase1.html`, `phase2.html`, `phase3.html` and `seller-bss.html`. `phase4.html` and `seller-mijee.html` were not changed (no specialist lines there).
- New owner page `seller-mark.html`: 3 accounts (NCLH, SGWS, JM Family), 4 phase tabs, 24 contacts. Mijee Walker is still the account owner on all three. Generated by `ed14-tools/seller_mark.py`, which copies the shell and CSS from `seller-michael.html` and pulls the current Edition 14 text from `phase1-4.html`. Re-run it after any change to those three accounts; it overwrites `seller-mark.html`.
- A "Mark" link was added to the topnav of every page (after Mijee) and a Mark card to the seller grid in both hubs.
- Open question: Mark is named in Phases 1-3, which goes against the "named people only in Phase 4" rule. The user accepted this.
- Checks: `navcheck.py` shows the nav on all pages with Mark active on his page; Chrome: nav 48px, all 4 tabs switch, Phase 3 rail switches, 24 Sales Nav links, jump pills and Full Intel links resolve, no broken logos, no console messages, no horizontal overflow. Only the Phase 3 screenshot was looked at. Nothing committed or pushed.
