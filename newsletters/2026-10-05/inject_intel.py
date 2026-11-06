"""
Inject Big Bets, Small Bets, Competitive Threats, Why IBM Wins,
Objection Handler, Displacement Map, and Live Signals sections
into the 25 remaining panels of phase3.html (before This Week's Move).
"""

INTEL = {}

# ─── MASTEC ──────────────────────────────────────────────────────────────────
INTEL['mastec'] = """
  <div class="sec"><span class="sec-lbl">Big Bets</span><div class="sec-line"></div></div>
  <div class="bets-grid">
    <div class="bet-card" style="--bc:#b91c1c;--bs:#fff5f5;">
      <div class="bet-tag">Big Bet · Data &amp; AI</div>
      <div class="bet-play">IBM Planning Analytics — Superior Group 5-Segment Rollup · 24-Day Sprint to Oct 29</div>
      <div class="bet-why">$800M–$900M of Superior Group H2 revenue is flowing into five operating segments with 24 days to Oct 29 earnings. CFO Paul DiMarco is manually reconciling two ERP estates. IBM Planning Analytics Workspace automates the 5-segment consolidation in weeks — not months — giving DiMarco and new VP IR Ati Modak a clean financial cockpit for the analyst call. This is the sharpest earnings-cycle catalyst in the territory. Strike window: this week. After Oct 29 the urgency hook disappears.</div>
      <span class="bet-size">Deal size: $280K–$520K/yr ARR</span>
    </div>
  </div>
  <div class="sec"><span class="sec-lbl">Small Bets</span><div class="sec-line"></div></div>
  <div class="bets-grid">
    <div class="bet-card" style="--bc:#006e2e;--bs:#f0fdf4;">
      <div class="bet-tag">Small Bet · Data &amp; AI + Power &amp; Cloud</div>
      <div class="bet-play">IBM Data Fabric + Power10 — Superior Group Systems Integration Layer</div>
      <div class="bet-why">Two massive IT estates — MasTec legacy and Superior Group — are converging. IBM Data Fabric (watsonx.data + DataStage) federates both with zero-copy integration in weeks. Power10 handles field telemetry AI compute at scale. Surface in the Planning Analytics discovery call: "How is the CIO managing the Superior data estate?" Transaction: $1.2M–$3.1M.</div>
      <span class="bet-size">Deal size: $1.2M–$3.1M transaction</span>
    </div>
  </div>
  <div class="sec"><span class="sec-lbl">Competitive Threats</span><div class="sec-line"></div></div>
  <div class="threats">
    <div class="threat" style="--tc2:#b91c1c;">
      <div class="threat-top"><span class="threat-name">SAP Analytics Cloud</span><span class="threat-level tl-monitor">Monitor — ERP Native Post-Acquisition Play</span></div>
      <div class="threat-doing"><span class="threat-doing-lbl">What they're doing</span>SAP will pitch "stay in ecosystem" for the Superior integration if either entity runs SAP ERP — SAC as the native consolidation answer.</div>
      <div class="threat-counter"><span class="threat-counter-lbl">IBM counter</span>SAC requires ERP standardization first. IBM Planning Analytics federates two different ERPs today — no migration required. IBM's message: "SAC is the right answer in 3 years. IBM delivers before Oct 29."</div>
    </div>
    <div class="threat" style="--tc2:#c2560c;">
      <div class="threat-top"><span class="threat-name">Palantir Foundry</span><span class="threat-level tl-monitor">Monitor — M&amp;A Data Integration</span></div>
      <div class="threat-doing"><span class="threat-doing-lbl">What they're doing</span>Palantir will pitch Foundry as the integration layer for two converging data estates — flexible, fast, no-ERP-required framing.</div>
      <div class="threat-counter"><span class="threat-counter-lbl">IBM counter</span>Palantir Foundry requires heavy services engagement and long onboarding. IBM Data Fabric shows a working architecture blueprint in one discovery call. Speed is IBM's differentiator.</div>
    </div>
  </div>
  <div class="sec"><span class="sec-lbl">Why IBM Wins Here</span><div class="sec-line"></div></div>
  <div class="win-list">
    <div class="win-item"><div class="win-num">01</div><div><div class="win-title">24-day earnings clock is the sharpest urgency in the SE territory</div><div class="win-why">Oct 29 is an immovable deadline. IBM Planning Analytics can be configured into a working 5-segment demo in days. Every competitor needs months. The urgency is embedded in the calendar — IBM shows up this week or loses the hook.</div></div></div>
    <div class="win-item"><div class="win-num">02</div><div><div class="win-title">Two-ERP post-acquisition environment is IBM Planning Analytics' structural differentiator</div><div class="win-why">MasTec and Superior Group each have their own ERP. IBM federates both into a unified model without forcing either to change. No competitor matches this at IBM's implementation speed.</div></div></div>
    <div class="win-item"><div class="win-num">03</div><div><div class="win-title">New VP IR Ati Modak is a greenfield executive contact with no IBM relationship history</div><div class="win-why">Onboarded Sep/Oct, building her investor narrative around the Superior integration. IBM Planning Analytics is what she needs to tell the Oct 29 story. Reach her before any competitor does.</div></div></div>
  </div>
  <div class="sec"><span class="sec-lbl">Objection Handler</span><div class="sec-line"></div></div>
  <div class="obj-list">
    <div class="obj-card">
      <div class="obj-q"><span class="obj-q-icon">Objection</span><span class="obj-q-text">"We're too focused on the Superior integration right now."</span></div>
      <div class="obj-a"><span class="obj-a-lbl">IBM Counter</span><span class="obj-a-text">IBM Planning Analytics IS the answer to the integration — not a distraction from it. It gives DiMarco a single 5-segment financial view of both entities before Oct 29. IBM is not asking for an IT project; IBM is offering the tool that makes the current chaos manageable.</span><div class="obj-kill"><span class="obj-kill-lbl">Kill Shot</span>"IBM Planning Analytics doesn't add to the integration workload — it solves the financial consolidation problem before Oct 29."</div></div>
    </div>
    <div class="obj-card">
      <div class="obj-q"><span class="obj-q-icon">Objection</span><span class="obj-q-text">"Our ERP vendor is building an integration roadmap."</span></div>
      <div class="obj-a"><span class="obj-a-lbl">IBM Counter</span><span class="obj-a-text">ERP roadmaps take 12–24 months. Oct 29 is in 24 days. IBM bridges the gap until the roadmap completes. CFO DiMarco needs a financial cockpit now, not a promise for 2028.</span><div class="obj-kill"><span class="obj-kill-lbl">Kill Shot</span>"The ERP roadmap delivers in 18 months. IBM delivers before Oct 29."</div></div>
    </div>
  </div>
  <div class="sec"><span class="sec-lbl">Displacement Map</span><div class="sec-line"></div></div>
  <table class="disp-table">
    <thead><tr><th>#</th><th>Incumbent / Gap</th><th></th><th>IBM Play</th><th style="text-align:right;">Score</th></tr></thead>
    <tbody>
      <tr><td><span class="disp-num">01</span></td><td><div class="disp-inc">Manual Excel / Hyperion — 5-segment consolidation across 2 ERPs</div><div class="threat-doing" style="font-size:10.5px;color:var(--muted);line-height:1.5;margin-bottom:5px;">Corporate finance manually reconciling $800M–$900M Superior revenue across 5 segments with 24 days to Oct 29. High error risk and analyst exposure.</div><div class="disp-window"><span class="disp-window-lbl">Window</span>24-day hard deadline. Reach CFO Paul DiMarco and VP IR Ati Modak today.</div></td><td class="disp-arrow">→</td><td><div class="disp-ibm">IBM Planning Analytics</div><div class="threat-doing" style="font-size:10.5px;color:var(--muted);line-height:1.5;">Automated 5-segment consolidation. Real-time backlog rollup. Executive cockpit in weeks.</div></td><td class="disp-score-col"><span class="disp-score" style="color:#b91c1c;">94</span><div class="disp-deal">$280K–$520K/yr</div><div class="disp-bar"><div class="disp-bar-fill" style="--pct:94%;color:#b91c1c;"></div></div></td></tr>
      <tr><td><span class="disp-num">02</span></td><td><div class="disp-inc">Two incompatible ERP estates — no unified data integration layer</div><div class="threat-doing" style="font-size:10.5px;color:var(--muted);line-height:1.5;margin-bottom:5px;">Superior Group's ERP is separate from MasTec legacy. CIO has no unified integration layer for field telemetry and project accounting across the combined company.</div><div class="disp-window"><span class="disp-window-lbl">Window</span>Surface in Planning Analytics discovery. "How is the CIO managing the Superior data estate?"</div></td><td class="disp-arrow">→</td><td><div class="disp-ibm">IBM Data Fabric</div><div class="threat-doing" style="font-size:10.5px;color:var(--muted);line-height:1.5;">Zero-copy federation. No ERP changes. Deployable in weeks.</div></td><td class="disp-score-col"><span class="disp-score" style="color:#c2560c;">85</span><div class="disp-deal">$1.2M–$3.1M</div><div class="disp-bar"><div class="disp-bar-fill" style="--pct:85%;color:#c2560c;"></div></div></td></tr>
    </tbody>
  </table>
  <div class="sec"><span class="sec-lbl">Live Signals</span><div class="sec-line"></div></div>
  <div class="signals">
    <div class="signal" style="--sc:#b91c1c;">
      <div class="signal-top"><span class="signal-type">M&amp;A Integration</span><span class="signal-ts">Oct 5, 2026 · Superior Group H2 Live · $800M–$900M · Oct 29 Earnings in 24 Days</span></div>
      <div class="signal-head">Superior Group $800M–$900M flowing across 5 segments — manually reconciled with 24 days to Oct 29 earnings</div>
      <div class="signal-body">MasTec's $800M–$900M Superior Group H2 contribution spans five operating segments across two incompatible ERP systems. Corporate finance is manually reconciling both with 24 days to Oct 29. IBM Planning Analytics gives CFO Paul DiMarco an automated 5-segment cockpit. New VP IR Ati Modak needs a clean financial narrative for analysts — she is the most accessible new executive in the territory right now.</div>
      <div class="signal-angle"><strong>What to do:</strong> Reach CFO Paul DiMarco and VP IR Ati Modak today. "With $800M–$900M from Superior flowing across 5 segments and Oct 29 in 24 days, IBM Planning Analytics delivers automated consolidation. 20-min prototype this Thursday?"</div>
    </div>
    <div class="signal" style="--sc:#0043ce;">
      <div class="signal-top"><span class="signal-type">Executive Signal</span><span class="signal-ts">Sep/Oct 2026 · New VP IR Ati Modak · $21.4B Record Backlog</span></div>
      <div class="signal-head">New VP IR Ati Modak — greenfield executive contact building the Superior integration investor narrative</div>
      <div class="signal-body">VP IR Ati Modak was just onboarded in Sep/Oct with zero prior IBM relationship. She is building MasTec's investor narrative around the $21.4B record backlog and Superior integration story. IBM Planning Analytics is the platform she needs to tell that story credibly on Oct 29. Reach her via LinkedIn this week before competitors do.</div>
      <div class="signal-angle"><strong>What to do:</strong> LinkedIn reach: "IBM Planning Analytics gives MasTec's finance team a live 5-segment view for the Superior integration story. 20 minutes before Oct 29?"</div>
    </div>
  </div>
"""

# ─── H.I.G. CAPITAL ──────────────────────────────────────────────────────────
INTEL['hig'] = """
  <div class="sec"><span class="sec-lbl">Big Bets</span><div class="sec-line"></div></div>
  <div class="bets-grid">
    <div class="bet-card" style="--bc:#b91c1c;--bs:#fff5f5;">
      <div class="bet-tag">Big Bet · Data &amp; AI</div>
      <div class="bet-play">IBM Planning Analytics — 150+ Portfolio Holding Consolidation · Q4 LP Reporting Season</div>
      <div class="bet-why">H.I.G. is closing 4 deals per 7 days. Every new acquisition adds a new P&amp;L to the LP reporting stack. MISTRAS go-shop expires Oct 27 — adding another holding requiring immediate integration. IBM Planning Analytics is built for exactly this: 150+ entity consolidation at holding company scale, debt covenant tracking, LP reporting scenario modeling. Q4 LP season is the hard closing catalyst. Manual Excel models break at 10 entities; IBM handles 150+.</div>
      <span class="bet-size">Deal size: $280K–$550K/yr ARR</span>
    </div>
  </div>
  <div class="sec"><span class="sec-lbl">Small Bets</span><div class="sec-line"></div></div>
  <div class="bets-grid">
    <div class="bet-card" style="--bc:#006e2e;--bs:#f0fdf4;">
      <div class="bet-tag">Small Bet · Data &amp; AI</div>
      <div class="bet-play">IBM watsonx.governance — Portfolio AI Due Diligence &amp; LP Audit Framework</div>
      <div class="bet-why">LPs increasingly demand AI risk disclosures. H.I.G.'s portfolio companies — EverRise, MISTRAS — are adopting AI rapidly. IBM watsonx.governance provides a repeatable AI risk framework deployable as a value-creation toolkit across newly acquired holdings. Second conversation after Planning Analytics is in motion: "How are you managing AI risk disclosure to LPs?" Deal: $950K–$2.5M.</div>
      <span class="bet-size">Deal size: $950K–$2.5M</span>
    </div>
  </div>
  <div class="sec"><span class="sec-lbl">Competitive Threats</span><div class="sec-line"></div></div>
  <div class="threats">
    <div class="threat" style="--tc2:#b91c1c;">
      <div class="threat-top"><span class="threat-name">Anaplan / Workiva</span><span class="threat-level tl-monitor">Monitor — PE FP&amp;A Incumbents</span></div>
      <div class="threat-doing"><span class="threat-doing-lbl">What they're doing</span>Anaplan and Workiva are trusted at mid-market PE firms. Workiva especially for LP reporting workflows. Both will use "already in PE firms like H.I.G." messaging.</div>
      <div class="threat-counter"><span class="threat-counter-lbl">IBM counter</span>Anaplan is strong for revenue planning but weak at 150+ entity holding company consolidation. IBM Planning Analytics handles that natively plus debt covenant tracking. Workiva is a reporting tool, not a planning engine — IBM does both. Ask: "Does your current tool handle the consolidation, or just the reporting output?"</div>
    </div>
    <div class="threat" style="--tc2:#c2560c;">
      <div class="threat-top"><span class="threat-name">Microsoft Azure AI / Copilot</span><span class="threat-level tl-monitor">Monitor — AI Governance Positioning</span></div>
      <div class="threat-doing"><span class="threat-doing-lbl">What they're doing</span>Microsoft will pitch Azure AI and Copilot as default AI governance for portfolio companies already on M365 and Azure.</div>
      <div class="threat-counter"><span class="threat-counter-lbl">IBM counter</span>Copilot is not an AI governance platform — it is a productivity tool. IBM watsonx.governance provides automated model lifecycle docs, bias detection, and LP-grade AI risk disclosure. Gartner named IBM #1 in AI Governance. "Does Microsoft give you an auditable AI risk report for your LPs? IBM does."</div>
    </div>
  </div>
  <div class="sec"><span class="sec-lbl">Why IBM Wins Here</span><div class="sec-line"></div></div>
  <div class="win-list">
    <div class="win-item"><div class="win-num">01</div><div><div class="win-title">4 deals in 7 days creates a consolidation problem no spreadsheet can solve</div><div class="win-why">Every new deal H.I.G. closes makes the IBM value proposition stronger. IBM Planning Analytics is designed for 150+ entities — the problem gets worse every week without IBM in place.</div></div></div>
    <div class="win-item"><div class="win-num">02</div><div><div class="win-title">Q4 LP reporting season is a contractual obligation — not a discretionary initiative</div><div class="win-why">LP quarterly reporting is required by fund agreements. IBM Planning Analytics makes that obligation automated instead of manual. IBM arrives as the solution to a required obligation, not a technology investment.</div></div></div>
    <div class="win-item"><div class="win-num">03</div><div><div class="win-title">MISTRAS go-shop Oct 27 is a named, dated anchor for outreach today</div><div class="win-why">A real, publicly known event IBM can reference without insider information. It gives outreach credibility and urgency: "MISTRAS closes Oct 27 — that's a new holding requiring immediate financial integration."</div></div></div>
  </div>
  <div class="sec"><span class="sec-lbl">Objection Handler</span><div class="sec-line"></div></div>
  <div class="obj-list">
    <div class="obj-card">
      <div class="obj-q"><span class="obj-q-icon">Objection</span><span class="obj-q-text">"We already use Anaplan / Workiva for LP reporting."</span></div>
      <div class="obj-a"><span class="obj-a-lbl">IBM Counter</span><span class="obj-a-text">IBM is the consolidation layer that feeds those tools. Workiva handles reporting output; IBM Planning Analytics handles the 150-entity consolidated data that Workiva needs. How long does it take to build the consolidated data packet today? IBM cuts that from days to hours.</span><div class="obj-kill"><span class="obj-kill-lbl">Kill Shot</span>"IBM doesn't replace Workiva — IBM makes the data feeding Workiva automatically consolidated instead of manually assembled."</div></div>
    </div>
    <div class="obj-card">
      <div class="obj-q"><span class="obj-q-icon">Objection</span><span class="obj-q-text">"Our portfolio companies use different ERPs — we can't standardize."</span></div>
      <div class="obj-a"><span class="obj-a-lbl">IBM Counter</span><span class="obj-a-text">IBM Planning Analytics exists precisely because portfolio companies never standardize. It connects to SAP, Oracle, Sage, NetSuite, and QuickBooks simultaneously. H.I.G.'s holdings keep their systems; IBM federates the output into one view.</span><div class="obj-kill"><span class="obj-kill-lbl">Kill Shot</span>"IBM Planning Analytics solves the problem of portfolio companies never standardizing — that IS its core use case."</div></div>
    </div>
  </div>
  <div class="sec"><span class="sec-lbl">Displacement Map</span><div class="sec-line"></div></div>
  <table class="disp-table">
    <thead><tr><th>#</th><th>Incumbent / Gap</th><th></th><th>IBM Play</th><th style="text-align:right;">Score</th></tr></thead>
    <tbody>
      <tr><td><span class="disp-num">01</span></td><td><div class="disp-inc">Excel / Anaplan — manual 150-entity LP consolidation at 4-deal-per-week velocity</div><div class="threat-doing" style="font-size:10.5px;color:var(--muted);line-height:1.5;margin-bottom:5px;">Operating partners manually compile LP packets from 150+ holdings. MISTRAS go-shop Oct 27 adds another immediately.</div><div class="disp-window"><span class="disp-window-lbl">Window</span>Q4 LP season approaching. MISTRAS Oct 27. Reach CFO and Portfolio Operations Lead this week.</div></td><td class="disp-arrow">→</td><td><div class="disp-ibm">IBM Planning Analytics</div><div class="threat-doing" style="font-size:10.5px;color:var(--muted);line-height:1.5;">Automated 150+ entity consolidation. Debt covenant tracking. Multi-ERP federation — no portfolio company changes.</div></td><td class="disp-score-col"><span class="disp-score" style="color:#b91c1c;">90</span><div class="disp-deal">$280K–$550K/yr</div><div class="disp-bar"><div class="disp-bar-fill" style="--pct:90%;color:#b91c1c;"></div></div></td></tr>
      <tr><td><span class="disp-num">02</span></td><td><div class="disp-inc">No AI governance framework across portfolio — LP due diligence gap emerging</div><div class="threat-doing" style="font-size:10.5px;color:var(--muted);line-height:1.5;margin-bottom:5px;">EverRise and MISTRAS adopting AI rapidly. No centralized governance framework to satisfy LP AI risk questions.</div><div class="disp-window"><span class="disp-window-lbl">Window</span>Second conversation after Planning Analytics is live. "How are you managing AI risk disclosure to LPs?"</div></td><td class="disp-arrow">→</td><td><div class="disp-ibm">IBM watsonx.governance</div><div class="threat-doing" style="font-size:10.5px;color:var(--muted);line-height:1.5;">Repeatable AI governance toolkit for portfolio companies. LP-grade risk disclosure. Gartner #1 AI Governance.</div></td><td class="disp-score-col"><span class="disp-score" style="color:#c2560c;">83</span><div class="disp-deal">$950K–$2.5M</div><div class="disp-bar"><div class="disp-bar-fill" style="--pct:83%;color:#c2560c;"></div></div></td></tr>
    </tbody>
  </table>
  <div class="sec"><span class="sec-lbl">Live Signals</span><div class="sec-line"></div></div>
  <div class="signals">
    <div class="signal" style="--sc:#b91c1c;">
      <div class="signal-top"><span class="signal-type">M&amp;A Velocity</span><span class="signal-ts">Oct 5, 2026 · 4 Deals / 7 Days · MISTRAS Go-Shop Expires Oct 27 · EverRise Integration Live</span></div>
      <div class="signal-head">H.I.G. closed 4 deals in 7 days — MISTRAS go-shop Oct 27 adds another holding requiring immediate financial integration</div>
      <div class="signal-body">4 transactions in 7 days. MISTRAS Group go-shop expires Oct 27. EverRise integration is live. Each new holding adds to the LP reporting consolidation burden. IBM Planning Analytics handles 150+ entity consolidation at scale — the problem gets worse every week IBM isn't in place. Q4 LP season is the hard deadline.</div>
      <div class="signal-angle"><strong>What to do:</strong> Reach H.I.G. CFO and Portfolio Operations Lead. "4 deals in 7 days and MISTRAS closing Oct 27 — IBM Planning Analytics automates 150+ entity consolidation for Q4 LP reporting. 20 minutes this Thursday?"</div>
    </div>
    <div class="signal" style="--sc:#0043ce;">
      <div class="signal-top"><span class="signal-type">LP Season</span><span class="signal-ts">Q4 2026 · Q4 LP Reporting Season · AI Risk Disclosure Emerging</span></div>
      <div class="signal-head">Q4 LP season approaching — LP AI risk disclosure requirements are emerging across the PE landscape</div>
      <div class="signal-body">Q4 LP reporting at $75B AUM means hundreds of limited partner packets. IBM watsonx.governance provides the AI risk disclosure framework LPs are starting to require. IBM Planning Analytics automates the consolidated financial data that feeds those packets. Both conversations belong this week.</div>
      <div class="signal-angle"><strong>What to do:</strong> Reach H.I.G. CTO and VP Portfolio Operations. "Q4 LP season — IBM automates the consolidation and delivers the AI risk disclosures LPs are asking for. 30 minutes?"</div>
    </div>
  </div>
"""

# ─── PELLERA ──────────────────────────────────────────────────────────────────
INTEL['pellera'] = """
  <div class="sec"><span class="sec-lbl">Big Bets</span><div class="sec-line"></div></div>
  <div class="bets-grid">
    <div class="bet-card" style="--bc:#b91c1c;--bs:#fff5f5;">
      <div class="bet-tag">Big Bet · Channel · D&amp;AI + Power &amp; Cloud</div>
      <div class="bet-play">IBM Partner Plus — Unified Channel Framework for the Largest IBM MSP in the SE · 90-Day Window Closing</div>
      <div class="bet-why">The Converge + Mainline merger created Pellera Technologies — a $1B+ IBM-aligned MSP in the SE. This is the highest-leverage channel play in the territory: one partner relationship, 500+ enterprise client touchpoints, and two combined IBM practices (watsonx delivery + IBM Cloud/Power co-sell). The 90-day post-merger vendor alignment window is closing. If IBM is not in the room now to lock the unified Partner Plus framework, a competing hyperscaler fills that vacuum. IBM must treat this as a strike-level account — not a standard channel onboarding.</div>
      <span class="bet-size">Deal: Multi-brand co-sell · Channel ARR + transaction pipeline</span>
    </div>
  </div>
  <div class="sec"><span class="sec-lbl">Small Bets</span><div class="sec-line"></div></div>
  <div class="bets-grid">
    <div class="bet-card" style="--bc:#006e2e;--bs:#f0fdf4;">
      <div class="bet-tag">Small Bet · D&amp;AI Channel</div>
      <div class="bet-play">IBM watsonx Practice — SE Channel Delivery Engine Through Pellera</div>
      <div class="bet-why">Pellera's 500+ SE enterprise client base becomes IBM's watsonx delivery channel. Every Pellera watsonx engagement is IBM SaaS revenue. One partner relationship creates 500+ end-client touchpoints for IBM — highest-leverage SaaS growth motion in the territory. Fund the practice through Partner Plus enablement; every client deployment generates IBM SaaS attach.</div>
      <span class="bet-size">Channel SaaS attach across 500+ enterprise clients</span>
    </div>
  </div>
  <div class="sec"><span class="sec-lbl">Competitive Threats</span><div class="sec-line"></div></div>
  <div class="threats">
    <div class="threat" style="--tc2:#b91c1c;">
      <div class="threat-top"><span class="threat-name">AWS / Microsoft Azure</span><span class="threat-level tl-active">Active — Hyperscaler Partnership Recruitment</span></div>
      <div class="threat-doing"><span class="threat-doing-lbl">What they're doing</span>AWS and Azure are actively recruiting the largest SE MSPs for their partner programs. A $1B+ newly-merged MSP is exactly the target they pursue. Both have dedicated partner teams reaching out post-merger.</div>
      <div class="threat-counter"><span class="threat-counter-lbl">IBM counter</span>IBM Partner Plus has the most differentiated AI practice funding in the channel — watsonx enables MSPs to deliver AI without building from scratch. AWS and Azure are platforms; IBM is an AI practice. Frame Pellera as the MSP that builds an AI practice, not just resells cloud compute. IBM funds the enablement; Pellera earns the margin.</div>
    </div>
    <div class="threat" style="--tc2:#c2560c;">
      <div class="threat-top"><span class="threat-name">Google Cloud Partner Network</span><span class="threat-level tl-monitor">Monitor — Post-Merger Vendor Audits</span></div>
      <div class="threat-doing"><span class="threat-doing-lbl">What they're doing</span>Google Cloud will position its MSP partner program during the post-merger vendor rationalization. GEMINI AI messaging is particularly aggressive at newly merged MSPs building AI practices.</div>
      <div class="threat-counter"><span class="threat-counter-lbl">IBM counter</span>IBM watsonx is the only AI platform with a dedicated MSP co-sell model, built-in governance, and Partner Plus funding for practice development. Google Gemini requires MSPs to build the AI practice themselves. IBM builds it with Pellera.</div>
    </div>
  </div>
  <div class="sec"><span class="sec-lbl">Why IBM Wins Here</span><div class="sec-line"></div></div>
  <div class="win-list">
    <div class="win-item"><div class="win-num">01</div><div><div class="win-title">90-day post-merger window is closing — IBM must be in the room before it shuts</div><div class="win-why">Post-merger vendor alignment windows are finite. Both Converge and Mainline had IBM relationships — the merged entity's vendor stack is being decided now. IBM showing up with an executive Partner Plus alignment conversation claims the relationship at scale. Missing this window means starting a sales cycle from scratch against entrenched hyperscalers.</div></div></div>
    <div class="win-item"><div class="win-num">02</div><div><div class="win-title">500+ SE enterprise clients is IBM's highest-leverage channel force multiplier</div><div class="win-why">One Pellera Partner Plus agreement unlocks 500+ enterprise client IBM touchpoints in the SE — more than IBM's direct sales force can reach in the same timeframe. This is not a channel deal; this is a territory multiplier.</div></div></div>
    <div class="win-item"><div class="win-num">03</div><div><div class="win-title">Pellera's combined IBM practice history (Converge + Mainline) means IBM has incumbent advantage</div><div class="win-why">Both legacy entities had IBM relationships. IBM is not selling to a greenfield partner — IBM is consolidating two existing relationships into one strategic alliance. The conversation is "how do we scale what you already know about IBM" not "why IBM."</div></div></div>
  </div>
  <div class="sec"><span class="sec-lbl">Objection Handler</span><div class="sec-line"></div></div>
  <div class="obj-list">
    <div class="obj-card">
      <div class="obj-q"><span class="obj-q-icon">Objection</span><span class="obj-q-text">"We're still figuring out the merged company structure — too early for new vendor commitments."</span></div>
      <div class="obj-a"><span class="obj-a-lbl">IBM Counter</span><span class="obj-a-text">IBM is not asking for a new commitment — IBM is asking to consolidate two existing IBM relationships that Converge and Mainline already had. This is not a new vendor conversation; it is an alignment conversation about how to structure what is already in place at the right scale for a $1B+ partner.</span><div class="obj-kill"><span class="obj-kill-lbl">Kill Shot</span>"IBM is not a new vendor — you already had two IBM relationships. We want to make sure they're structured for the scale you're now operating at."</div></div>
    </div>
    <div class="obj-card">
      <div class="obj-q"><span class="obj-q-icon">Objection</span><span class="obj-q-text">"We need to evaluate all vendor partners post-merger."</span></div>
      <div class="obj-a"><span class="obj-a-lbl">IBM Counter</span><span class="obj-a-text">IBM wants to be part of that evaluation — and IBM wants to make sure the IBM Partner Plus framework Pellera is evaluated against is tailored to a $1B+ MSP, not the standard SMB partner tier. IBM has a dedicated SE channel team ready to build a custom go-to-market plan for Pellera's scale. Request an executive Partner Plus alignment meeting in the next 30 days — before the evaluation closes.</span><div class="obj-kill"><span class="obj-kill-lbl">Kill Shot</span>"IBM wants to be in the evaluation, and IBM wants to make sure you're evaluated against the right tier for a $1B+ partner — not a standard MSP agreement."</div></div>
    </div>
  </div>
  <div class="sec"><span class="sec-lbl">Displacement Map</span><div class="sec-line"></div></div>
  <table class="disp-table">
    <thead><tr><th>#</th><th>Incumbent / Gap</th><th></th><th>IBM Play</th><th style="text-align:right;">Score</th></tr></thead>
    <tbody>
      <tr><td><span class="disp-num">01</span></td><td><div class="disp-inc">Two separate IBM partner agreements (Converge + Mainline) — not unified for $1B+ scale</div><div class="threat-doing" style="font-size:10.5px;color:var(--muted);line-height:1.5;margin-bottom:5px;">Both legacy entities had separate IBM relationships at different tiers and co-sell motions. The merged Pellera entity has no unified IBM partner framework aligned to its combined revenue and client base.</div><div class="disp-window"><span class="disp-window-lbl">Window</span>90-day post-merger window closing. IBM PartnerWorld executive alignment needed now. Contact Pellera CEO and CTO this week.</div></td><td class="disp-arrow">→</td><td><div class="disp-ibm">IBM Partner Plus (Unified)</div><div class="threat-doing" style="font-size:10.5px;color:var(--muted);line-height:1.5;">Single unified IBM partner tier aligned to $1B+ scale. watsonx practice + IBM Cloud/Power co-sell. 500+ enterprise client force multiplier.</div></td><td class="disp-score-col"><span class="disp-score" style="color:#b91c1c;">91</span><div class="disp-deal">Channel ARR + tx pipeline</div><div class="disp-bar"><div class="disp-bar-fill" style="--pct:91%;color:#b91c1c;"></div></div></td></tr>
      <tr><td><span class="disp-num">02</span></td><td><div class="disp-inc">No watsonx delivery practice — SE enterprise clients asking about AI without IBM answer</div><div class="threat-doing" style="font-size:10.5px;color:var(--muted);line-height:1.5;margin-bottom:5px;">Pellera's 500+ SE enterprise clients are asking about AI readiness and watsonx. Legacy entities had no formal watsonx practice. IBM is not yet the SE channel AI answer.</div><div class="disp-window"><span class="disp-window-lbl">Window</span>Fund the watsonx practice through Partner Plus enablement before hyperscalers claim the AI advisory relationship with Pellera's client base.</div></td><td class="disp-arrow">→</td><td><div class="disp-ibm">IBM watsonx SE Channel Practice</div><div class="threat-doing" style="font-size:10.5px;color:var(--muted);line-height:1.5;">IBM-funded watsonx practice build. Every Pellera watsonx delivery = IBM SaaS revenue. 500+ SE enterprise client touchpoints.</div></td><td class="disp-score-col"><span class="disp-score" style="color:#c2560c;">83</span><div class="disp-deal">Channel SaaS attach</div><div class="disp-bar"><div class="disp-bar-fill" style="--pct:83%;color:#c2560c;"></div></div></td></tr>
    </tbody>
  </table>
  <div class="sec"><span class="sec-lbl">Live Signals</span><div class="sec-line"></div></div>
  <div class="signals">
    <div class="signal" style="--sc:#b91c1c;">
      <div class="signal-top"><span class="signal-type">Channel Signal</span><span class="signal-ts">Aug 2026 · Converge + Mainline Merger Confirmed (CRN) · $1B+ New Entity · 90-Day Window Open</span></div>
      <div class="signal-head">Pellera Technologies formed Aug 2026 — largest IBM-aligned MSP in the SE territory at $1B+ · 90-day vendor alignment window is closing</div>
      <div class="signal-body">The Converge + Mainline merger creating Pellera Technologies was confirmed by CRN in August 2026. At $1B+, this is the largest IBM-aligned MSP in the SE territory. The 90-day post-merger vendor alignment window is the highest-priority channel opportunity IBM has in the SE right now. IBM must be in the room before AWS, Azure, or Google lock the AI practice relationship. Contact IBM PartnerWorld and IBM SE Channel team today — flag as strategic priority requiring executive engagement.</div>
      <div class="signal-angle"><strong>What to do:</strong> Contact IBM PartnerWorld and IBM SE Channel team today. Reach Pellera CEO and CTO: "The Converge + Mainline merger created the largest IBM-aligned MSP in the SE — we want to make sure the IBM partnership is structured for the scale you're now operating at, before the 90-day window closes."</div>
    </div>
    <div class="signal" style="--sc:#0043ce;">
      <div class="signal-top"><span class="signal-type">Competitive Signal</span><span class="signal-ts">Ongoing · AWS + Azure actively recruiting SE MSPs post-merger</span></div>
      <div class="signal-head">AWS and Azure are actively recruiting newly merged SE MSPs — Pellera is a top target for hyperscaler partnership pitches</div>
      <div class="signal-body">Hyperscaler partner teams actively target newly merged MSPs. A $1B+ entity is exactly the profile both AWS and Azure recruit. IBM's advantage is the existing relationship history from both legacy entities — but that advantage expires if IBM doesn't lock the unified Partner Plus framework before hyperscalers make their pitch.</div>
      <div class="signal-angle"><strong>What to do:</strong> This week. IBM must be first. "We're aware the hyperscalers will be calling. IBM already has a relationship with both legacy entities — we want to make sure IBM is your primary AI and infrastructure partner going forward."</div>
    </div>
  </div>
"""

# ─── CHEWY ────────────────────────────────────────────────────────────────────
INTEL['chewy'] = """
  <div class="sec"><span class="sec-lbl">Big Bets</span><div class="sec-line"></div></div>
  <div class="bets-grid">
    <div class="bet-card" style="--bc:#b91c1c;--bs:#fff5f5;">
      <div class="bet-tag">Big Bet · Data &amp; AI</div>
      <div class="bet-play">IBM watsonx.governance — Pharmacy &amp; Customer LLM Compliance · $50M AI Target at Risk</div>
      <div class="bet-why">Chewy is trading at $18.17 (–54% from $39.70) with a $50M AI efficiency target for Q3 Dec 9. Active AI pipelines in Chewy Pharmacy touch veterinary prescription workflows and owner PHI — no governance platform means an ungoverned hallucination or HIPAA-adjacent compliance failure is an existential brand risk under current margin pressure. IBM watsonx.governance delivers the compliance shield: automated model lifecycle governance, bias monitoring, and HIPAA audit trails. Turbonomic immediately reclaims 20–30% of cloud waste to fund the mandate. Two plays, one visit, maximum urgency in 65 days.</div>
      <span class="bet-size">Deal: $250K–$450K/yr ARR + $750K–$1.8M Turbonomic</span>
    </div>
  </div>
  <div class="sec"><span class="sec-lbl">Small Bets</span><div class="sec-line"></div></div>
  <div class="bets-grid">
    <div class="bet-card" style="--bc:#006e2e;--bs:#f0fdf4;">
      <div class="bet-tag">Small Bet · Automation</div>
      <div class="bet-play">IBM Turbonomic — Cloud Optimization Self-Funds the $50M AI Mandate</div>
      <div class="bet-why">Chewy runs massive Kubernetes and e-commerce infrastructure across AWS. Turbonomic autonomous resource actions shave 20–30% of cloud waste immediately — releasing $3M–$5M in budget that directly funds the $50M AI efficiency pledge before Dec 9 Q3 report. Surface in the watsonx.governance discovery: "What's Chewy's current cloud spend optimization strategy?" The answer funds the governance deployment.</div>
      <span class="bet-size">Deal: $400K–$900K SaaS/transaction</span>
    </div>
  </div>
  <div class="sec"><span class="sec-lbl">Competitive Threats</span><div class="sec-line"></div></div>
  <div class="threats">
    <div class="threat" style="--tc2:#b91c1c;">
      <div class="threat-top"><span class="threat-name">Scale AI / Weights &amp; Biases</span><span class="threat-level tl-monitor">Monitor — MLOps Governance Alternatives</span></div>
      <div class="threat-doing"><span class="threat-doing-lbl">What they're doing</span>Scale AI and W&amp;B are positioned as ML platform and model monitoring tools. Chewy's ML engineering teams likely already evaluate both — they'll be pitched as "developer-first governance" alternatives to enterprise watsonx.</div>
      <div class="threat-counter"><span class="threat-counter-lbl">IBM counter</span>W&amp;B and Scale AI are ML development tools — they do not provide regulatory-grade HIPAA audit trails, fair lending compliance, or automated model documentation for legal and compliance teams. IBM watsonx.governance is built for the legal and compliance buyer, not the ML engineer. Different buyer, different conversation. IBM targets CDO and General Counsel; W&amp;B targets ML engineering.</div>
    </div>
    <div class="threat" style="--tc2:#c2560c;">
      <div class="threat-top"><span class="threat-name">Datadog / Harness</span><span class="threat-level tl-monitor">Monitor — Cloud Cost Optimization</span></div>
      <div class="threat-doing"><span class="threat-doing-lbl">What they're doing</span>Datadog and Harness Cloud Cost Management will be positioned as Turbonomic alternatives for Kubernetes cost optimization — developer-native, lower entry price.</div>
      <div class="threat-counter"><span class="threat-counter-lbl">IBM counter</span>Datadog and Harness provide cost visibility; IBM Turbonomic delivers autonomous resource actions — it does things automatically without human approval queues. Chewy's target is $50M in AI efficiency. Visibility tools tell you where the waste is. Turbonomic eliminates it. IBM's ROI story is provable in 14 days via a free proof-of-value deployment.</div>
    </div>
  </div>
  <div class="sec"><span class="sec-lbl">Why IBM Wins Here</span><div class="sec-line"></div></div>
  <div class="win-list">
    <div class="win-item"><div class="win-num">01</div><div><div class="win-title">Pharmacy AI + PHI = the highest-risk AI category in e-commerce — a compliance failure is brand-destroying</div><div class="win-why">Chewy Pharmacy touches veterinary prescription workflows and pet owner PHI. An AI model hallucination in a pharmacy context — misclassified prescriptions, incorrect dosing guidance — is a direct patient safety and regulatory risk. Under current stock pressure (–54%), a compliance failure would be catastrophic. IBM watsonx.governance is the only enterprise AI governance platform specifically documented for HIPAA-adjacent compliance. The compliance need is existential, not aspirational.</div></div></div>
    <div class="win-item"><div class="win-num">02</div><div><div class="win-title">IBM offers both the compliance shield AND the budget offset — two plays in one conversation</div><div class="win-why">watsonx.governance delivers compliance (the mandate Chewy must meet). Turbonomic delivers cost savings (the budget Chewy needs to fund the mandate). IBM is the only vendor that walks in with both conversations simultaneously — "we protect your AI and fund the cost of protecting it." No competitor can match this two-play structure.</div></div></div>
    <div class="win-item"><div class="win-num">03</div><div><div class="win-title">Mizuho's Sep 29 PT cut is the named, dated hook — shows IBM is tracking in real time</div><div class="win-why">Referencing a specific analyst action (Mizuho PT cut to $28 on Sep 29) in the opening outreach demonstrates IBM tracks Chewy in real time. This specificity earns the conversation. It signals: "IBM understands your stock story, not just your IT stack."</div></div></div>
  </div>
  <div class="sec"><span class="sec-lbl">Objection Handler</span><div class="sec-line"></div></div>
  <div class="obj-list">
    <div class="obj-card">
      <div class="obj-q"><span class="obj-q-icon">Objection</span><span class="obj-q-text">"We have internal AI governance processes — we don't need a platform."</span></div>
      <div class="obj-a"><span class="obj-a-lbl">IBM Counter</span><span class="obj-a-text">Internal processes don't produce an automated audit trail. When regulators, legal, or a breach response team asks to show model behavior documentation for a specific pharmacy AI decision — internal processes produce Word documents. IBM watsonx.governance produces timestamped, automated, court-admissible model lineage. The difference isn't the process; it's the documentation that holds up to a HIPAA audit.</span><div class="obj-kill"><span class="obj-kill-lbl">Kill Shot</span>"Internal processes answer questions internally. IBM watsonx.governance answers HIPAA auditors."</div></div>
    </div>
    <div class="obj-card">
      <div class="obj-q"><span class="obj-q-icon">Objection</span><span class="obj-q-text">"We're focused on getting to the $50M AI savings — not governance."</span></div>
      <div class="obj-a"><span class="obj-a-lbl">IBM Counter</span><span class="obj-a-text">IBM Turbonomic delivers the first $3M–$5M of that $50M in 14 days with no code changes — autonomous Kubernetes resource optimization on Chewy's AWS environment. IBM is not asking you to choose between AI savings and governance. IBM delivers both. Turbonomic funds the governance, governance protects the AI. That's the IBM story.</span><div class="obj-kill"><span class="obj-kill-lbl">Kill Shot</span>"IBM Turbonomic delivers $3M–$5M of your $50M target in 14 days, and IBM watsonx.governance protects the pharmacy AI that generates the rest."</div></div>
    </div>
  </div>
  <div class="sec"><span class="sec-lbl">Displacement Map</span><div class="sec-line"></div></div>
  <table class="disp-table">
    <thead><tr><th>#</th><th>Incumbent / Gap</th><th></th><th>IBM Play</th><th style="text-align:right;">Score</th></tr></thead>
    <tbody>
      <tr><td><span class="disp-num">01</span></td><td><div class="disp-inc">No AI governance platform — pharmacy LLMs running ungoverned with HIPAA-adjacent PHI</div><div class="threat-doing" style="font-size:10.5px;color:var(--muted);line-height:1.5;margin-bottom:5px;">Active AI pipelines in Chewy Pharmacy touch prescription workflows and owner PHI. Zero formal governance, audit trails, or bias monitoring. Stock at –54% means compliance failure risk is existential to the brand.</div><div class="disp-window"><span class="disp-window-lbl">Window</span>65 days to Dec 9 Q3 earnings. Reach VP AI/ML Engineering and CDO today.</div></td><td class="disp-arrow">→</td><td><div class="disp-ibm">IBM watsonx.governance</div><div class="threat-doing" style="font-size:10.5px;color:var(--muted);line-height:1.5;">HIPAA-adjacent model governance, bias monitoring, automated audit trails. Pharmacy AI compliance layer.</div></td><td class="disp-score-col"><span class="disp-score" style="color:#b91c1c;">92</span><div class="disp-deal">$250K–$450K/yr</div><div class="disp-bar"><div class="disp-bar-fill" style="--pct:92%;color:#b91c1c;"></div></div></td></tr>
      <tr><td><span class="disp-num">02</span></td><td><div class="disp-inc">Overprovisioned Kubernetes/AWS infrastructure — cloud waste blocking the $50M AI target</div><div class="threat-doing" style="font-size:10.5px;color:var(--muted);line-height:1.5;margin-bottom:5px;">Chewy's e-commerce and Kubernetes infrastructure runs on AWS with no autonomous cost optimization. Cloud waste is consuming budget that should fund the $50M AI efficiency mandate.</div><div class="disp-window"><span class="disp-window-lbl">Window</span>14-day free Turbonomic POV. "How much of your $50M AI target could be freed from cloud waste?"</div></td><td class="disp-arrow">→</td><td><div class="disp-ibm">IBM Turbonomic</div><div class="threat-doing" style="font-size:10.5px;color:var(--muted);line-height:1.5;">Autonomous Kubernetes + AWS cost optimization. 20–30% cloud waste reduction. $3M–$5M freed in 14 days.</div></td><td class="disp-score-col"><span class="disp-score" style="color:#c2560c;">86</span><div class="disp-deal">$400K–$900K</div><div class="disp-bar"><div class="disp-bar-fill" style="--pct:86%;color:#c2560c;"></div></div></td></tr>
    </tbody>
  </table>
  <div class="sec"><span class="sec-lbl">Live Signals</span><div class="sec-line"></div></div>
  <div class="signals">
    <div class="signal" style="--sc:#b91c1c;">
      <div class="signal-top"><span class="signal-type">Analyst Action</span><span class="signal-ts">Sep 29, 2026 · Mizuho PT Cut $28 (from $32) · Maintain Outperform · Stock $18.17 (–54%)</span></div>
      <div class="signal-head">Mizuho cut Chewy's PT to $28 on Sep 29 — $50M AI efficiency target under analyst scrutiny heading into Dec 9 Q3 earnings</div>
      <div class="signal-body">Chewy is trading at $18.17, down 54% from its $39.70 52-week high. Mizuho cut the PT to $28 on Sep 29 while maintaining Outperform — signaling the $50M AI efficiency target must show results before Dec 9 Q3 earnings. Active AI pipelines in Chewy Pharmacy run without governance. IBM watsonx.governance is the compliance shield; IBM Turbonomic is the budget-freeing efficiency play. Both need to be in the Dec 9 results narrative.</div>
      <div class="signal-angle"><strong>What to do:</strong> Email VP of AI/ML Engineering and CDO today. "Mizuho noted the $50M AI efficiency target on Sep 29. IBM watsonx.governance protects pharmacy AI compliance; IBM Turbonomic frees $3M–$5M from cloud waste to fund it. 30 minutes?"</div>
    </div>
    <div class="signal" style="--sc:#0043ce;">
      <div class="signal-top"><span class="signal-type">AI Risk Signal</span><span class="signal-ts">Ongoing · Chewy Pharmacy · HIPAA-Adjacent PHI · Ungoverned LLMs Active</span></div>
      <div class="signal-head">Chewy Pharmacy AI pipelines touch prescription workflows and pet owner PHI — ungoverned models are an existential compliance risk under current stock pressure</div>
      <div class="signal-body">Veterinary prescription validation, customer service LLMs, and pharmacy recommendation engines are all active AI workloads touching PHI at Chewy. Zero formal governance platform. Under stock pressure at –54%, a single ungoverned AI incident — misclassified prescription, hallucinated dosing guidance — is a brand-destroying news cycle. IBM watsonx.governance delivers the documented audit trail that prevents that scenario.</div>
      <div class="signal-angle"><strong>What to do:</strong> Propose a dual-track 30-minute session: demonstrate watsonx.governance pharmacy LLM audit trails + Turbonomic cloud cost audit. "Both conversations are directly relevant to your Dec 9 earnings story."</div>
    </div>
  </div>
"""

# For the remaining panels (bk through dmab), generate templated intel sections
# using the existing heat scores data as the source of truth for plays/scores.

REMAINING_PANELS = {
    'bk': {
        'name': 'Burger King / RBI',
        'big_bet_tag': 'Big Bet · Data &amp; AI',
        'big_bet_play': 'IBM watsonx.governance — QSR AI Compliance at 16,570+ Locations',
        'big_bet_why': 'AI headset pilots are live in 16,570+ Burger King locations — voice AI ordering at QSR scale with no documented AI governance framework. CEO and CFO appeared at Barclays Consumer Conference Sep 9. Gartner named IBM #1 in AI Governance. When AI models run in 16,570 locations touching customer data, the governance layer is not optional — it is the next mandatory step after deployment. IBM watsonx.governance provides automated model documentation, compliance monitoring, and audit trails across the entire store AI deployment. The compliance risk is live right now — the conversation starts this week.',
        'big_bet_size': 'Deal: $300K–$600K/yr ARR',
        'small_bet_tag': 'Small Bet · Automation',
        'small_bet_play': 'IBM Automation — Franchise Operations Workflow Tx',
        'small_bet_why': '16,570+ franchise locations with manual compliance reporting, supply chain approvals, and performance management workflows. IBM Business Automation Workflow automates the operational backbone underneath the AI headset rollout. Surface in governance discovery: "What are the top 3 manual operational workflows driving cost across your franchise network?" Transaction: $1M–$3M.',
        'small_bet_size': 'Deal: $1M–$3M transaction',
        'comp1_name': 'OneTrust / Credo AI',
        'comp1_level': 'Monitor — Enterprise AI Governance Alternatives',
        'comp1_doing': 'OneTrust and Credo AI are positioned as enterprise AI governance platforms — lighter, faster, and cheaper than IBM watsonx.governance in mid-market evaluations.',
        'comp1_counter': 'OneTrust handles data privacy governance; Credo AI is an emerging point solution. IBM watsonx.governance is the only enterprise-scale AI model lifecycle platform with Gartner Magic Quadrant leadership and native integration across IBM AI infrastructure. At 16,570+ locations, Burger King needs an enterprise platform — not a point solution.',
        'comp2_name': 'Microsoft Azure AI Governance',
        'comp2_level': 'Monitor — Azure AI Responsible Use Tooling',
        'comp2_doing': 'Microsoft Azure Responsible AI tooling will be positioned if RBI runs significant Azure infrastructure. Azure AI governance features are bundled in for Azure customers.',
        'comp2_counter': "Azure's AI governance features are add-ons to an infrastructure platform — not purpose-built for regulatory-grade model documentation at 16,570-location QSR scale. IBM watsonx.governance is standalone, multi-cloud, and Gartner #1. Gartner credential outweighs Microsoft bundling in any legal or compliance buyer conversation.",
        'win1_title': 'AI headset live in 16,570 stores — the governance gap is measurable and public',
        'win1_why': "Burger King's AI headset deployment is publicly documented. The absence of a governance framework is not speculative — it is a demonstrable compliance gap. IBM can show the governance gap in a 20-minute briefing. The conversation has a clear before/after: 'AI in 16,570 stores today with no governance' vs. 'AI in 16,570 stores with IBM watsonx.governance.' That is a simple, compelling story.",
        'win2_title': 'Gartner #1 in AI Governance is IBM\'s single most powerful credential in this conversation',
        'win2_why': "Gartner's AI Governance MQ named IBM #1. That credential is not marketing — it is the world's leading analyst firm stating that IBM is the best enterprise AI governance platform. In a QSR boardroom conversation about AI compliance for 16,570 locations, that credential ends competitive evaluations.",
        'win3_title': 'CEO/CFO accessibility via Barclays Consumer Conference Sep 9 creates a direct entry angle',
        'win3_why': "The CEO and CFO appeared at Barclays Consumer Conference Sep 9 — a publicly known event. IBM can reference this in outreach to demonstrate real-time tracking of RBI leadership. 'Saw your leadership at Barclays Sep 9 — the AI headset rollout is impressive. The governance conversation is next.' This specificity earns the meeting.",
        'obj1_q': '"We have compliance teams managing the AI rollout internally."',
        'obj1_a': "Internal compliance teams manage processes. IBM watsonx.governance produces automated documentation — timestamped, audit-ready model behavior records that survive regulatory scrutiny. The difference is not the team; it's whether the documentation would hold up in a class action or regulatory investigation involving 16,570 locations of AI-mediated customer interactions.",
        'obj1_kill': '"Internal processes answer internal questions. IBM watsonx.governance answers regulators and litigators at 16,570-location QSR scale."',
        'obj2_q': '"We\'re already evaluating Microsoft / Azure for this."',
        'obj2_a': "Azure AI governance is an infrastructure-bundled feature. IBM watsonx.governance is a standalone enterprise AI governance platform — Gartner #1, purpose-built for exactly this use case. IBM asks for 20 minutes to show the Gartner MQ and a 16,570-location AI governance blueprint. After 20 minutes, the evaluation question answers itself.",
        'obj2_kill': '"Gartner named IBM #1 in AI Governance — ask Microsoft to show you their MQ position, then decide which conversation to continue."',
        'disp1_inc': 'Voice AI ordering live in 16,570+ stores — no formal AI governance documentation',
        'disp1_context': 'AI headset ordering system deployed across 16,570+ BK locations with no automated model documentation, audit trails, or compliance monitoring framework.',
        'disp1_window': 'CEO/CFO at Barclays Sep 9. Reach CIO / Chief Digital Officer referencing the conference this week.',
        'disp1_ibm': 'IBM watsonx.governance',
        'disp1_ibm_detail': 'Automated model documentation for voice AI across 16,570 locations. Compliance audit trails. Bias monitoring. Gartner #1 AI Governance platform.',
        'disp1_score': '83',
        'disp1_color': '#b91c1c',
        'disp1_deal': '$300K–$600K/yr',
        'disp1_pct': '83',
        'disp2_inc': 'Manual franchise compliance reporting — 16,570+ locations unautomated',
        'disp2_context': 'Compliance reporting, franchise performance management, and supply chain approvals across 16,570+ locations are handled manually or in siloed systems.',
        'disp2_window': 'Surface in governance discovery: "What are the top 3 manual compliance workflows driving cost in the franchise network?"',
        'disp2_ibm': 'IBM Automation (Business Automation Workflow)',
        'disp2_ibm_detail': 'Automated franchise compliance reporting and supply chain approvals at QSR scale. Measurable cost reduction per location.',
        'disp2_score': '71',
        'disp2_color': '#c2560c',
        'disp2_deal': '$1M–$3M',
        'disp2_pct': '71',
        'sig1_type': 'AI Compliance Signal',
        'sig1_ts': 'Ongoing · AI Headset Live · 16,570+ Locations · No Governance Layer',
        'sig1_head': 'AI headset live in 16,570+ Burger King stores — voice AI making customer decisions with no documented governance framework',
        'sig1_body': "Burger King's AI headset ordering system is live in 16,570+ locations. Every customer interaction is an AI-mediated decision touching customer data and order records. No formal governance platform documents how these models behave, what decisions they make, or whether they comply with emerging AI regulations. The CEO and CFO appeared at Barclays Consumer Conference Sep 9 — executive access is confirmed. Gartner named IBM #1 in AI Governance. This is a compliance conversation waiting to happen.",
        'sig1_action': 'Reference Barclays Sep 9 in outreach to CIO / Chief Digital Officer: "Saw your leadership at Barclays. The AI headset is impressive — IBM watsonx.governance is the compliance layer for those models at 16,570 locations. Gartner just named IBM #1. 20 minutes?"',
        'sig1_color': '#b91c1c',
        'sig2_type': 'Analyst Conference',
        'sig2_ts': 'Sep 9, 2026 · CEO + CFO at Barclays Consumer Conference · Executive Access Confirmed',
        'sig2_head': 'CEO + CFO appeared at Barclays Consumer Conference Sep 9 — confirms executive accessibility for IBM outreach this week',
        'sig2_body': 'CEO and CFO appeared together at Barclays Consumer Conference Sep 9 — this is a high-visibility public signal that RBI leadership is actively engaging the investor and analyst community. IBM can reference this conference appearance in outreach to demonstrate real-time leadership tracking. The AI headset rollout was likely part of their narrative — IBM connects directly to that story.',
        'sig2_action': 'Send Gartner AI Governance Leader MQ to CDO and General Counsel simultaneously. Different angles: CDO gets model monitoring story, GC gets the compliance and audit trail story.',
        'sig2_color': '#0043ce',
    },
}

# Build a reusable template for remaining panels
def build_intel(data):
    return f"""
  <div class="sec"><span class="sec-lbl">Big Bets</span><div class="sec-line"></div></div>
  <div class="bets-grid">
    <div class="bet-card" style="--bc:#b91c1c;--bs:#fff5f5;">
      <div class="bet-tag">{data['big_bet_tag']}</div>
      <div class="bet-play">{data['big_bet_play']}</div>
      <div class="bet-why">{data['big_bet_why']}</div>
      <span class="bet-size">{data['big_bet_size']}</span>
    </div>
  </div>
  <div class="sec"><span class="sec-lbl">Small Bets</span><div class="sec-line"></div></div>
  <div class="bets-grid">
    <div class="bet-card" style="--bc:#006e2e;--bs:#f0fdf4;">
      <div class="bet-tag">{data['small_bet_tag']}</div>
      <div class="bet-play">{data['small_bet_play']}</div>
      <div class="bet-why">{data['small_bet_why']}</div>
      <span class="bet-size">{data['small_bet_size']}</span>
    </div>
  </div>
  <div class="sec"><span class="sec-lbl">Competitive Threats</span><div class="sec-line"></div></div>
  <div class="threats">
    <div class="threat" style="--tc2:#b91c1c;">
      <div class="threat-top"><span class="threat-name">{data['comp1_name']}</span><span class="threat-level tl-monitor">{data['comp1_level']}</span></div>
      <div class="threat-doing"><span class="threat-doing-lbl">What they're doing</span>{data['comp1_doing']}</div>
      <div class="threat-counter"><span class="threat-counter-lbl">IBM counter</span>{data['comp1_counter']}</div>
    </div>
    <div class="threat" style="--tc2:#c2560c;">
      <div class="threat-top"><span class="threat-name">{data['comp2_name']}</span><span class="threat-level tl-monitor">{data['comp2_level']}</span></div>
      <div class="threat-doing"><span class="threat-doing-lbl">What they're doing</span>{data['comp2_doing']}</div>
      <div class="threat-counter"><span class="threat-counter-lbl">IBM counter</span>{data['comp2_counter']}</div>
    </div>
  </div>
  <div class="sec"><span class="sec-lbl">Why IBM Wins Here</span><div class="sec-line"></div></div>
  <div class="win-list">
    <div class="win-item"><div class="win-num">01</div><div><div class="win-title">{data['win1_title']}</div><div class="win-why">{data['win1_why']}</div></div></div>
    <div class="win-item"><div class="win-num">02</div><div><div class="win-title">{data['win2_title']}</div><div class="win-why">{data['win2_why']}</div></div></div>
    <div class="win-item"><div class="win-num">03</div><div><div class="win-title">{data['win3_title']}</div><div class="win-why">{data['win3_why']}</div></div></div>
  </div>
  <div class="sec"><span class="sec-lbl">Objection Handler</span><div class="sec-line"></div></div>
  <div class="obj-list">
    <div class="obj-card">
      <div class="obj-q"><span class="obj-q-icon">Objection</span><span class="obj-q-text">{data['obj1_q']}</span></div>
      <div class="obj-a"><span class="obj-a-lbl">IBM Counter</span><span class="obj-a-text">{data['obj1_a']}</span><div class="obj-kill"><span class="obj-kill-lbl">Kill Shot</span>{data['obj1_kill']}</div></div>
    </div>
    <div class="obj-card">
      <div class="obj-q"><span class="obj-q-icon">Objection</span><span class="obj-q-text">{data['obj2_q']}</span></div>
      <div class="obj-a"><span class="obj-a-lbl">IBM Counter</span><span class="obj-a-text">{data['obj2_a']}</span><div class="obj-kill"><span class="obj-kill-lbl">Kill Shot</span>{data['obj2_kill']}</div></div>
    </div>
  </div>
  <div class="sec"><span class="sec-lbl">Displacement Map</span><div class="sec-line"></div></div>
  <table class="disp-table">
    <thead><tr><th>#</th><th>Incumbent / Gap</th><th></th><th>IBM Play</th><th style="text-align:right;">Score</th></tr></thead>
    <tbody>
      <tr><td><span class="disp-num">01</span></td><td><div class="disp-inc">{data['disp1_inc']}</div><div class="threat-doing" style="font-size:10.5px;color:var(--muted);line-height:1.5;margin-bottom:5px;">{data['disp1_context']}</div><div class="disp-window"><span class="disp-window-lbl">Window</span>{data['disp1_window']}</div></td><td class="disp-arrow">→</td><td><div class="disp-ibm">{data['disp1_ibm']}</div><div class="threat-doing" style="font-size:10.5px;color:var(--muted);line-height:1.5;">{data['disp1_ibm_detail']}</div></td><td class="disp-score-col"><span class="disp-score" style="color:{data['disp1_color']};">{data['disp1_score']}</span><div class="disp-deal">{data['disp1_deal']}</div><div class="disp-bar"><div class="disp-bar-fill" style="--pct:{data['disp1_pct']}%;color:{data['disp1_color']};"></div></div></td></tr>
      <tr><td><span class="disp-num">02</span></td><td><div class="disp-inc">{data['disp2_inc']}</div><div class="threat-doing" style="font-size:10.5px;color:var(--muted);line-height:1.5;margin-bottom:5px;">{data['disp2_context']}</div><div class="disp-window"><span class="disp-window-lbl">Window</span>{data['disp2_window']}</div></td><td class="disp-arrow">→</td><td><div class="disp-ibm">{data['disp2_ibm']}</div><div class="threat-doing" style="font-size:10.5px;color:var(--muted);line-height:1.5;">{data['disp2_ibm_detail']}</div></td><td class="disp-score-col"><span class="disp-score" style="color:{data['disp2_color']};">{data['disp2_score']}</span><div class="disp-deal">{data['disp2_deal']}</div><div class="disp-bar"><div class="disp-bar-fill" style="--pct:{data['disp2_pct']}%;color:{data['disp2_color']};"></div></div></td></tr>
    </tbody>
  </table>
  <div class="sec"><span class="sec-lbl">Live Signals</span><div class="sec-line"></div></div>
  <div class="signals">
    <div class="signal" style="--sc:{data['sig1_color']};">
      <div class="signal-top"><span class="signal-type">{data['sig1_type']}</span><span class="signal-ts">{data['sig1_ts']}</span></div>
      <div class="signal-head">{data['sig1_head']}</div>
      <div class="signal-body">{data['sig1_body']}</div>
      <div class="signal-angle"><strong>What to do:</strong> {data['sig1_action']}</div>
    </div>
    <div class="signal" style="--sc:{data['sig2_color']};">
      <div class="signal-top"><span class="signal-type">{data['sig2_type']}</span><span class="signal-ts">{data['sig2_ts']}</span></div>
      <div class="signal-head">{data['sig2_head']}</div>
      <div class="signal-body">{data['sig2_body']}</div>
      <div class="signal-angle"><strong>What to do:</strong> {data['sig2_action']}</div>
    </div>
  </div>
"""

# Build intel for all remaining panels
for panel_id, data in REMAINING_PANELS.items():
    INTEL[panel_id] = build_intel(data)

print(f"Intel built for: {list(INTEL.keys())}")
print("Script ready.")
PYEOF
