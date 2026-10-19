# SE Horizon — Edition Build Runbook (read this first in any new chat)

Permanent checklist for building every new weekly edition. Territory 26 · IBM South Florida · 27 accounts.
Per-edition status lives in `newsletters/<YYYY-MM-DD>/BUILD_README.md`. Structure and design source of truth: `../SE_HORIZON_README.md` and `BOB_INSTRUCTIONS.md` (Standing Rules section).

## 0. Start-of-chat sanity check (do this before touching anything)
1. Call `get_current_datetime`. Never guess the date or year.
2. Read, in this order: this file → latest `newsletters/<date>/BUILD_README.md` → `BOB_INSTRUCTIONS.md` → `../SE_HORIZON_README.md`.
3. Confirm the new folder exists (`cp -R` of the previous edition). If not, create it. Never delete or edit old edition folders.
4. Confirm the previous edition's tiers (the starting point) and open the "Resume point" in the new edition's BUILD_README.

## 1. Hard rules (set by the user — always follow)
- **Phases 1–3 are built ONE PHASE AT A TIME, THREE ACCOUNTS AT A TIME (user rule, restated Oct 19, 2026 — NEXT EDITION MUST FOLLOW THIS).**
  - Do NOT patch all three phases in the same pass for a batch. Work on a single phase, 3 accounts per pass: e.g. Phase 1 for accounts 1–3 → verify → Phase 1 for accounts 4–6 → ... then move to the next phase.
  - Research can be shared, but each phase is built and verified on its own, 3 accounts at a time. Tick off each phase/batch separately in the edition's BUILD_README.
  - Edition 11 was built the other way (3 accounts patched into all three phases per pass) with the user's one-time OK. Do not repeat that in Edition 12 or later.
- **Phase 4 (named contacts) must use the `account-intel-brief` skill** in `contacts` mode only. Also 3 accounts at a time.
  - Skill: `/Users/barronkwekuowusu/.bob/skills/account-intel-brief/SKILL.md` (re-activate with `use_skill`).
  - Per account: 16–25 verified current employees (12–15 Practitioners, 7–10 Executives).
  - Discovery: Sales Navigator Account IQ plus at least 6 LinkedIn people searches (`data`, `AI`/ML, `CIO`/`VP`/`technology`, `analytics`/BI, `architecture`/`integration`/`cloud`, one account-specific term).
  - Each contact: verified current employer, real `https://www.linkedin.com/in/<slug>` URL (else "Not publicly verified" — never guess a slug), warmth (Hot/Warm/Cold), Champion flag, 0–100 score, one of the six watsonx.data play tracks, "why this person", best path in.
  - Needs debug Chrome: `--remote-debugging-port=9222`, profile `~/.chrome-debug-profile`, logged in to LinkedIn and Sales Navigator (Sales Nav may bounce to IBM w3id SSO — the user must sign in; if it won't render, record the gap and continue with LinkedIn people search).
  - Outputs: `phase4.html` + `phase4-contacts.xlsx` (via the `write_contacts` MCP, sheet "Leads", emails blank). Skill briefs go to `/Users/barronkwekuowusu/Documents/IBM Bob/Briefings/<territory>/`; run `convert.py` after writing Markdown.
  - Check every carried-over contact for departures. Do not carry names forward unchecked.
- **Named people appear ONLY in Phase 4.** Phases 1–3 use positions (CFO, CIO, "Investor Relations").
- **Web research = Tavily MCP only** (`tavily_search`, `tavily_extract`). No curl/scripts for web data. Prefer `time_range: week`. Cite sources.
- **Do not commit, push, or mirror to `se-horizon/editions/`** unless the user asks.
- Minimal changes: patch the copied files; do not rewrite from scratch.

## 2. Accuracy rules (the "is this current?" test)
- Every date, price, day-count and earnings date must be re-derived from today's date. Never leave a copied "N days" figure.
- If sources conflict, say so: "~Nov 18–24, unconfirmed". Never assert a date you could not verify.
- Facts that are still true but older than the window keep their real date (e.g. "Oct 9 ...") — do not relabel them as new.
- Hiring wording when nothing is found: "no dated postings surfaced in the Oct 12–19 scan" (use the current window).
- Claims from the previous edition that were not re-verified: mark "not re-verified" or drop. Do not repeat them as fact.
- Entity checks: confirm each company is the right entity (e.g. Frontline Insurance Managers, Lake Mary FL vs Frontline plc, Oslo). Confirm current CEO/CFO before naming anyone in Phase 4.
- Keep deal sizes as `$X–X/yr` (not "ARR"). No Security brand. No seller names.

## 3. Patching method (tooling lessons)
- **Never run parallel `search_and_replace` / `apply_diff` calls on the same file** — they race and overwrite each other.
- For each batch, write one Python script that runs `str.replace` for each (old, new) pair across `phase1.html`, `phase2.html`, `phase3.html`, printing `MISS` when a pattern isn't in a file. A MISS in one phase is normal (phases differ). Examples: `/tmp/patch_b*.py` (ephemeral — recreate).
- Use HTML entities exactly as in the source (`&amp;`, `&quot;`, `&apos;`). In the phase 3 JS `ACCOUNTS` array, apostrophes are escaped (`\'`).
- **Why Now bullets are duplicated 3× per Phase 2 page** (`pulse-row`, `bullets-grid`, `dark-grid`) — a global replace updates all.
- After each batch, grep for stale strings (see §6).

## 4. Edition workflow
| Step | What |
|---|---|
| A | Copy previous edition folder → `newsletters/<new-date>/`. Write a BUILD_README stub with a Resume point. |
| B | One phase at a time (Phase 1, then 2, then 3), batches of 3 accounts each, tick each phase/batch separately: stock/price, earnings date, day counts, news in the window, hiring line, "Why Now" heading date, hooks (phase 3 `ACCOUNTS`), phase 3 panel vitals and "This Week's Move". |
| C | Global pass: Phase 1 title/`tn-badge`/`tn-right`/header/Market Pulse (4 headlines)/footer; Phase 2 title/topbar/cover/Top Plays/Quick Plays, every `acct-se-horizon`, `acct-date-line`, "Pulse", "Signals — <window>"; Phase 3 every `acct-eyebrow` (27), fallback panel text, topbar/banner. |
| D | Tier review (Strike/Engage/Standby). Class convention: `cu-t5`/`t5` = Strike, `cu-t4`/`t4` = Engage, `cu-t3`/`t3` = Standby. Keep Phase 1/2/3 consistent. |
| E | Phase 4 via the skill, 3 accounts at a time. Update nav links in phases 1–3. |
| F | Update `index.html`: add the new edition card with "Latest" badge, demote the previous one to Previous Issues. |
| G | Finish the edition's BUILD_README (final tiers, corrections, unverified items, Phase 4 counts, known gaps). |
| H | Validate (§6). Stop. Wait for the user to ask before git. |

## 5. Design conventions
Light theme, IBM Plex Sans. Section labels: Why Now · Hiring Signals · IBM Angle · What to Say · How to Sell · Do This Now. Logos in `LOGOS/` copied unchanged.

## 6. Validation checklist (run before reporting done)
Run from `newsletters/<new-date>/`:
- Stale previous-edition strings: `grep -n "Edition 10\|Oct 12, 2026\|Oct 5–12\|Oct 5–Oct 12\|Oct 12 Pulse" phase*.html` → every hit must be intentional (a real event on that date) or fixed.
- Stale day counts: `grep -n "[0-9]\+ days\|[0-9]\+d)" phase*.html` → recompute each from today.
- Account coverage: 27 cards in phase 1, 27 `class="page"` in phase 2, 27 `PANELS[` in phase 3 and 27 sections in phase 4.
- Tier counts match across all phases and the README.
- Links: `phase2.html#<id>` anchors exist; LOGOS paths resolve; phase 4 nav present.
- Phases 1–3 contain no individual's name (positions only).
- Phase 4: every contact has a real `/in/` URL or "Not publicly verified"; counts in the README match the page.
- Open pages in a browser (Chrome DevTools MCP) and check the console for errors.
