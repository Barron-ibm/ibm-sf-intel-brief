# SE Horizon — Resume Point

## Repo & Site Info
- **GitHub repo:** https://github.com/Barron-ibm/ibm-sf-intel-brief
- **Live site:** https://barron-ibm.github.io/ibm-sf-intel-brief/
- **Local path:** `/Users/barronkwekuowusu/Desktop/bobmode/se-horizon-site/`
- **Branch:** main — every push auto-deploys via GitHub Pages

## What Is Done
- `newsletters/2026-07-19/phase1.html` — complete, all 26 accounts, logos as asset files, reputable sources only, LinkedIn company pages for all 26, SNav links pre-filtered for Florida region + Director/VP/CXO seniority
- `newsletters/2026-07-19/phase2.html` — 19 of 26 account pages complete (cover page + accounts 1–18: SGWS through Dycom)
- `assets/logos/` — all 24 logo files present as separate image files
- `index.html` — archive index with July 19 issue card linking to both phases
- `netlify.toml` — present (not needed for GitHub Pages)

## What Is NOT Done
`phase2.html` is missing the last 8 account pages. The file currently ends at line 2573 (closing `</div>` of the Dycom page). Everything after line 2573 is broken old markup that must be replaced.

**The 8 missing accounts to add (in this order):**

| # | Account | id= | snavId | Logo file |
|---|---------|-----|--------|-----------|
| 20 | Herc Rentals Inc. / Herc Holdings | herc | 2848055 | `images.jpeg` |
| 21 | Data Management Associates of Brevard | dmab | 163065 | none — use `<div class="logo-svg-placeholder">DMAB</div>` |
| 22 | Memorial Healthcare System | memorial | 15052 | `MemorialHealthSystem_BlueLogo.jpg` |
| 23 | MasTec Inc. | mastec | 5350 | `MasTec_Logo.jpg` |
| 24 | Frontline Insurance Managers | frontline | 2523441 | `Frontline_Insurance_Logo.jpg` |
| 25 | Office Depot / ODP Corporation | odp | 3492 | `ODP_Wht-e1594114705114.jpg` |
| 26 | Chewy Inc. | chewy | 3497540 | `Screenshot 2026-07-19 at 7.27.22 PM.png` (has narrow no-break space \u202f before PM) |
| 27 | Chico's FAS / KnitWell Group | chicos | 11398 | `images.jpeg` |

Logo paths are relative: `../../assets/logos/<filename>`

## IBM Sales Plays Per Missing Account
- **Herc:** IBM Planning Analytics + watsonx.data | Supporting: Automation
- **DMAB:** IBM Z Modernization + Storage + Security | Supporting: Hybrid Cloud
- **Memorial:** AI Governance + Security + watsonx | Supporting: IBM Planning Analytics
- **MasTec:** Storage + Data Fabric + Automation | Supporting: Power Systems
- **Frontline:** IBM Planning Analytics + AI Governance | Supporting: watsonx
- **ODP:** IBM Planning Analytics + watsonx + Automation | Supporting: Data Fabric
- **Chewy:** watsonx + Automation + AI Governance | Supporting: IBM Planning Analytics
- **Chico's:** IBM Planning Analytics + watsonx | Supporting: Data Fabric

## Where to Get the Account Content
All summaries, signals, hiring signals, why it matters, talk tracks, and sources for all 8 accounts are already written in `newsletters/2026-07-19/phase1.html`. Search for each account key (e.g. `herc:`, `dmab:`, `memorial:`, etc.) in that file to find the full data object.

## Page Structure to Follow Exactly
Copy the **Dycom page** (lines 2453–2573 in phase2.html) as the template for each new page. Every page is:

```
<div class="page" id="ACCTKEY">
  <!-- Scrollable dark top nav — same links every page, THIS account highlighted:
       background:#1a7a3a;color:#fff on the active link -->
  <div class="top-bar"></div>
  <div class="new-acct-banner">✦ New Account — Annual Deep Dive · NYSE/info · City, FL</div>
  <div class="acct-header-row">
    <div class="acct-logo-cell"><img src="../../assets/logos/FILENAME" class="acct-logo-img" alt="NAME"></div>
    <div class="acct-header-text">
      <div class="acct-se-horizon">SE HORIZON · JULY 19, 2026</div>
      <div class="acct-name-large">Full Account Name</div>
      <div class="acct-date-line">Annual Deep Dive · Ticker · Industry · City, FL</div>
    </div>
  </div>
  <div class="mission-row"><span class="mission-badge">Mission</span><span class="mission-text">...</span></div>
  <hr class="dashed-div">
  <div class="meta-rows">
    <div class="meta-row"><span class="meta-label">Priority</span><span class="meta-value">HIGH/MED · key signal</span></div>
    <div class="meta-row"><span class="meta-label">Thesis</span><span class="meta-value-italic">...</span></div>
  </div>
  <div class="linkedin-row">
    <!-- LinkedIn SVG icon + suggested search string -->
  </div>
  <hr class="dashed-div">
  <div class="dark-grid">
    <div class="grid-col-left">Why Now? bullets</div>
    <div class="grid-col-mid">Pain Point bullets</div>
    <div class="grid-col-right">Key Personas (3 contact-entry divs)</div>
    <div class="play-li-row">
      <div class="ibm-play-bar-full">IBM Sales Play + why it wins</div>
      <div class="snav-panel">SNav button + keywords</div>
    </div>
  </div>
  <hr class="dashed-div">
  <div class="lower-section">
    <div class="lower-row"><span class="action-btn">Seller Move</span>...</div>
    <div class="lower-row"><span class="action-btn grey">Talk Track</span>...</div>
  </div>
  <div class="message-cadence">3-week cadence</div>
  <div class="sources-footer">reputable sources + LinkedIn company page</div>
  <div class="page-footer">SE Horizon · Account Name · July 19, 2026 · ✦ New Account</div>
</div>
```

## SNav URL Pattern (already in file — copy from Dycom page)
```
https://www.linkedin.com/sales/search/people?query=(filters%3AList((type%3ACURRENT_COMPANY%2Cvalues%3AList((id%3ASNAV_ID%2CselectionType%3AINCLUDED)))%2C(type%3AREGION%2Cvalues%3AList((id%3A101318387%2CselectionType%3AINCLUDED%2Ctext%3AFlorida)))%2C(type%3ASENIORITY_LEVEL%2Cvalues%3AList((id%3A10%2CselectionType%3AINCLUDED%2Ctext%3ADirector)%2C(id%3A9%2CselectionType%3AINCLUDED%2Ctext%3AVP)%2C(id%3A8%2CselectionType%3AINCLUDED%2Ctext%3ACXO)))))
```
Replace SNAV_ID with the numeric ID for each account.

## How to Resume (exact steps)
1. Read `se-horizon-site/newsletters/2026-07-19/phase2.html` to confirm it ends at the Dycom `</div>` — the cut marker is `'\n\n<!-- ═══════════════════════ PAGE 20'`
2. Truncate the file at that cut marker (keep everything before it)
3. Build all 8 account pages using the Dycom page as the template and the phase1.html data objects for content
4. Append all 8 pages + `</body></html>` to the truncated file
5. Run: `cd /Users/barronkwekuowusu/Desktop/bobmode/se-horizon-site && git add newsletters/2026-07-19/phase2.html && git commit -m "Add missing 8 account pages to phase2 (Herc through Chico's)" && git push origin main`

## Prompt to Paste in New Task
```
Read the file at se-horizon-site/RESUME.md and follow the "How to Resume" steps exactly to add the 8 missing account pages to se-horizon-site/newsletters/2026-07-19/phase2.html, then commit and push to GitHub.
```
