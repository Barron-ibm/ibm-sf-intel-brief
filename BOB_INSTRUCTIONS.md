# SE Horizon — Bob's Biweekly Generation Instructions

> Bob reads this file at the start of every newsletter cycle.
> It tells Bob exactly what to do, in what order, to produce and publish a new edition.

---

## Trigger Phrase

When the user says **"generate the next SE Horizon newsletter"**, Bob executes
the full workflow below from top to bottom.

---

## Step 1 — Determine the Issue Date

- Check the `newsletters/` directory to find the most recent dated folder
- The new issue date = **most recent date + 14 days**
- Create the folder: `newsletters/YYYY-MM-DD/`

---

## Step 2 — Read the Master Spec

Read `SE_HORIZON_README.md` in full. This file contains:
- All 26 account names, tickers, and research scope
- The complete structure for PHASE1.html and PHASE2.html
- IBM Sales Plays per account
- Persona guide per industry
- Logo file paths
- LinkedIn Company IDs

---

## Step 3 — Web Research (run all searches in parallel)

For **existing accounts** (those already in the previous issue):
- Search last **14 days only** for each account
- Focus: earnings, news, hiring signals, technology signals, external market factors

For **new accounts** (first time appearing):
- Search last **12 months** for each account
- Focus: company overview, financials, 2026 signals, IBM angle

Use `tavily_search` for all research. Run account searches in parallel to save time.

---

## Step 4 — Write PHASE1.html

- Copy the structure from the previous issue's `PHASE1.html` as the base
- Update all account data objects with new research findings
- Update the issue date in the footer to the new date
- Save to `newsletters/YYYY-MM-DD/PHASE1.html`

---

## Step 5 — Write PHASE2.html

- Copy the structure from the previous issue's `PHASE2.html` as the base
- Update all account pages with new research findings
- Update the issue date on the cover page and all footers
- Save to `newsletters/YYYY-MM-DD/PHASE2.html`

---

## Step 6 — Update index.html

Open `index.html` and:
1. Add a new `<div class="issue-card latest">` block at the TOP of the `.issue-list` div
   for the new issue — using the new date, issue number, and a one-line summary
2. Remove the `badge-latest` span and `latest` class from the previous issue's card
   (it is no longer the latest)
3. Replace the `<div class="placeholder-card">` with a new one showing the NEXT
   upcoming issue date (new date + 14 days)

### New issue card HTML template:
```html
<div class="issue-card latest">
  <div class="issue-meta">
    <div class="issue-date">MONTH DD, YYYY &nbsp;·&nbsp; Issue #N</div>
    <div class="issue-title">ONE LINE SUMMARY <span class="badge-latest">Latest</span></div>
    <div class="issue-desc">Brief description of what's new this cycle — key accounts, signals, themes.</div>
  </div>
  <div class="issue-links">
    <a class="issue-btn btn-secondary" href="newsletters/YYYY-MM-DD/PHASE1.html">Weekly Pulse</a>
    <a class="issue-btn btn-primary"   href="newsletters/YYYY-MM-DD/PHASE2.html">Intel Brief</a>
  </div>
</div>
```

---

## Step 7 — Commit and Push

Run the following git commands to publish the new edition:

```bash
git add newsletters/YYYY-MM-DD/ index.html
git commit -m "SE Horizon — MONTH DD, YYYY edition"
git push origin main
```

GitHub Actions will deploy the site automatically within ~30 seconds.

---

## Notes

- Never delete old newsletter folders — the archive must be preserved
- Always use the exact date format `YYYY-MM-DD` for folder names
- The `SE_HORIZON_README.md` is the source of truth for structure — if anything
  conflicts with this file, the README wins

---

*SE Horizon · IBM South Florida SE Team · Generated with IBM Bob*
