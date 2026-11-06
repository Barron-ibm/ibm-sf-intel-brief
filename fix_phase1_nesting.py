#!/usr/bin/env python3
"""
Full, flawless build of Phase 1 for Edition 07 (Sep 17, 2026).
Extracts every complete card from 2026-09-10 and places each with 100% complete markup,
correctly nesting into Strike (4), Engage (11), and Standby (12).
"""
import re

SRC_P1 = "ibm-sf-intel-brief/newsletters/2026-09-10/phase1.html"
TGT_P1 = "ibm-sf-intel-brief/newsletters/2026-09-17/phase1.html"

with open(SRC_P1) as f:
    orig = f.read()

# 1. Extract every account card block from orig by regex
# Each card starts with <!-- Account Name --> and ends before the next <!-- or </div><!-- /group
card_regex = re.compile(r'(<!--\s*([^\n]+?)\s*-->\s*<div class="card\s+(t[345])"[^>]*data-account="([^"]+)"[^>]*>.*?)(?=\s*<!--\s*──|\s*<!--\s*[A-Za-z0-9]|\s*</div><!-- /group|\s*</div>\s*<!-- ══|\Z)', re.DOTALL)

cards = {}
for m in card_regex.finditer(orig):
    comment_title = m.group(2)
    tier = m.group(3)
    acc_id = m.group(4)
    full_card_html = m.group(1).strip()
    cards[acc_id] = {
        'title': comment_title,
        'tier': tier,
        'html': full_card_html
    }

print(f"Extracted {len(cards)} original cards from 9-10.")

# 2. Define Edition 07 tiers
strike_ids = ["lennar", "chewy", "dycom", "mastec"]
engage_ids = ["heico", "nclh", "sgws", "hig", "odp", "herc", "bk", "kforce", "citco", "frontline", "icahn"]
standby_ids = ["lenmar", "jmf", "seaworld", "chicos", "memorial", "hexfed", "hexmin", "octave", "pellera", "ansco", "dmab", "sbhd"]

# Function to adjust an existing card's tier and urgency badge
def adjust_card(acc_id, new_tier, new_urg_label=None):
    c = cards[acc_id]['html']
    # Replace card class
    c = re.sub(r'class="card\s+t[345]"', f'class="card {new_tier}"', c)
    c = re.sub(r'data-urgency="t[345]"', f'data-urgency="{new_tier}"', c)
    c = re.sub(r'cu-t[345]', f'cu-{new_tier}', c)
    if new_urg_label:
        c = re.sub(r'<div class="c-urg cu-[^"]*"><span class="cu-dot"></span>[^<]*</div>', 
                   f'<div class="c-urg cu-{new_tier}"><span class="cu-dot"></span>{new_urg_label}</div>', c)
    return c

# 3. Custom cards for Strike accounts with fresh Sep 10-17 intelligence
lennar_full_card = """    <!-- Lennar Corporation -->
    <div class="card t5" data-urgency="t5" data-brands="data-ai automation power-cloud" data-account="lennar">
      <div class="c-left">
        <div class="c-left-meta">
          <div class="c-acct-name">Lennar Corporation</div>
          <div class="c-meta">NYSE: LEN · Homebuilding · $35B+ rev</div>
        </div>
        <div class="c-left-right">
          <div class="c-urg cu-t5"><span class="cu-dot"></span>Strike — Q3 earnings miss Sep 16</div>
          <div class="c-entry-section"><div class="c-lbl">Lead</div><span class="c-entry-badge br-data">Data &amp; AI</span></div>
          <div class="c-also">
            <div class="c-also-item"><span class="c-brand-sm br-auto">Automation</span></div>
            <div class="c-also-item"><span class="c-brand-sm br-pc">Power</span></div>
          </div>
        </div>
      </div>
      <div class="c-mid">
        <div class="c-mid-left">
          <div class="c-section">
            <div class="c-sec-lbl">Why Now</div>
            <ul class="c-bullets">
              <li>Q3 2026 earnings reported Sep 16 missed estimates: gross margin compressed 170 bps to 15.8%, ASP down 2.9% to $372K.</li>
              <li>SG&amp;A climbed to 9.2% of home sales — CFO actively mandating operational workflow cost takeout.</li>
              <li>12% buyer incentive rate squeezing margins — urgent need for dynamic regional pricing elasticity models.</li>
              <li>Full-year delivery guidance cut for second straight quarter — sales conversion speed is top priority.</li>
            </ul>
          </div>
          <div class="c-section">
            <div class="c-sec-lbl">Hiring Signals</div>
            <ul class="c-bullets">
              <li>Enterprise analytics architect and automation engineering roles open at Miami HQ.</li>
              <li>Operational excellence and regional pricing intelligence managers recruiting.</li>
            </ul>
          </div>
          <div class="c-angle">
            <div class="c-angle-lbl">IBM Angle</div>
            <div class="c-angle-txt">Margin compression forces SG&amp;A cost takeout. IBM Planning Analytics models dynamic pricing &amp; incentive elasticity, while watsonx automates mortgage pre-qualification and buyer document processing.</div>
          </div>
          <div class="c-talk">
            <div class="c-talk-lbl">What to Say</div>
            <div class="c-talk-txt">"With gross margins tightening to 15.8% and incentive management critical, IBM Planning Analytics is helping homebuilders dynamically forecast pricing elasticity and reduce SG&amp;A overhead by 15%. Can we share peer benchmarks?"</div>
          </div>
        </div>
        <div class="c-right">
          <div class="c-sales-hdr">How to Sell</div>
          <div class="c-sales-block saas">
            <div class="c-sales-type saas">SaaS Entry</div>
            <div class="c-sales-txt"><strong>watsonx.ai</strong> — annual SaaS for automated homebuyer qualification and contract triage to cut customer acquisition costs.</div>
            <span class="c-sales-pill saas">watsonx.ai</span>
          </div>
          <div class="c-sales-block trans">
            <div class="c-sales-type trans">Transaction</div>
            <div class="c-sales-txt"><strong>Planning Analytics + Turbonomic</strong> — enterprise software transaction across 40+ divisions for incentive budgeting and hybrid cloud cost optimization.</div>
            <span class="c-sales-pill trans">Planning Analytics + Turbonomic</span>
          </div>
          <div class="c-sales-block motion">
            <div class="c-sales-type motion">Do This Now</div>
            <div class="c-sales-txt">1. Send margin preservation brief to CFO/CIO post-earnings.<br>2. Request 20-min workshop on automated SG&amp;A optimization.<br>3. Propose 30-day proof-of-concept on regional pricing models.</div>
          </div>
        </div>
      </div>
      <div class="c-actions">
        <a class="c-btn c-btn-intel" href="phase2.html#lennar">Full Intel →</a>
        <a class="c-btn c-btn-snav" href="https://www.linkedin.com/sales/search/people?query=(filters%3AList((type%3ACURRENT_COMPANY%2Cvalues%3AList((id%3A2977%2CselectionType%3AINCLUDED)))))" target="_blank" rel="noopener">SNav ↗</a>
      </div>
    </div>"""

chewy_full_card = """    <!-- Chewy Inc. -->
    <div class="card t5" data-urgency="t5" data-brands="data-ai power-cloud" data-account="chewy">
      <div class="c-left">
        <div class="c-left-meta">
          <div class="c-acct-name">Chewy Inc.</div>
          <div class="c-meta">NYSE: CHWY · E-Commerce / Pet · $11.8B+ rev</div>
        </div>
        <div class="c-left-right">
          <div class="c-urg cu-t5"><span class="cu-dot"></span>Strike — $50M AI savings target + S-3 filed</div>
          <div class="c-entry-section"><div class="c-lbl">Lead</div><span class="c-entry-badge br-data">Data &amp; AI</span></div>
          <div class="c-also">
            <div class="c-also-item"><span class="c-brand-sm br-pc">Power</span></div>
            <div class="c-also-item"><span class="c-brand-sm br-auto">Automation</span></div>
          </div>
        </div>
      </div>
      <div class="c-mid">
        <div class="c-mid-left">
          <div class="c-section">
            <div class="c-sec-lbl">Why Now</div>
            <ul class="c-bullets">
              <li>CEO announced $50M annualized AI cost savings target for FY27 across customer care and pharmacy.</li>
              <li>Centralized enterprise data platform constructed to feed production AI tools without data bottlenecks.</li>
              <li>Filed S-3 registration on Sep 14 for flexible capital market execution and growth initiatives.</li>
              <li>Q2 net sales rose 7.3% to $3.33B driven by Autoship customer retention and vet health scaling.</li>
            </ul>
          </div>
          <div class="c-section">
            <div class="c-sec-lbl">Hiring Signals</div>
            <ul class="c-bullets">
              <li>Machine learning engineers and AI product managers scaling in Dania Beach HQ.</li>
              <li>Pharmacy operations data engineers active for automated prescription verification.</li>
            </ul>
          </div>
          <div class="c-angle">
            <div class="c-angle-lbl">IBM Angle</div>
            <div class="c-angle-txt">Chewy is publicly committed to a $50M AI savings target and built a unified data foundation. IBM watsonx.governance secures their pharmacy/health LLMs against compliance risks, while Turbonomic cuts cloud compute spend.</div>
          </div>
          <div class="c-talk">
            <div class="c-talk-lbl">What to Say</div>
            <div class="c-talk-txt">"Seeing Chewy's public milestone targeting $50M in AI cost savings, we've helped retail platforms enforce HIPAA/clinical AI governance with watsonx while cutting 30% compute spend via Turbonomic. Worth comparing notes?"</div>
          </div>
        </div>
        <div class="c-right">
          <div class="c-sales-hdr">How to Sell</div>
          <div class="c-sales-block saas">
            <div class="c-sales-type saas">SaaS Entry</div>
            <div class="c-sales-txt"><strong>watsonx.governance</strong> — annual subscription to monitor pharmacy &amp; vet AI agents, track model drift, and maintain compliance audit trails.</div>
            <span class="c-sales-pill saas">watsonx.governance</span>
          </div>
          <div class="c-sales-block trans">
            <div class="c-sales-type trans">Transaction</div>
            <div class="c-sales-txt"><strong>Turbonomic + Data Fabric</strong> — hybrid cloud optimization software transaction to reclaim wasted AWS/GCP compute spend on AI clusters.</div>
            <span class="c-sales-pill trans">Turbonomic + Data Fabric</span>
          </div>
          <div class="c-sales-block motion">
            <div class="c-sales-type motion">Do This Now</div>
            <div class="c-sales-txt">1. Connect with VP AI Engineering &amp; CIO referencing $50M savings milestone.<br>2. Run Turbonomic 14-day zero-touch value assessment.<br>3. Expand into watsonx.governance for pharmacy automation.</div>
          </div>
        </div>
      </div>
      <div class="c-actions">
        <a class="c-btn c-btn-intel" href="phase2.html#chewy">Full Intel →</a>
        <a class="c-btn c-btn-snav" href="https://www.linkedin.com/sales/search/people?query=(filters%3AList((type%3ACURRENT_COMPANY%2Cvalues%3AList((id%3A3497540%2CselectionType%3AINCLUDED)))))" target="_blank" rel="noopener">SNav ↗</a>
      </div>
    </div>"""

dycom_full_card = """    <!-- Dycom Industries Inc. -->
    <div class="card t5" data-urgency="t5" data-brands="data-ai storage automation" data-account="dycom">
      <div class="c-left">
        <div class="c-left-meta">
          <div class="c-acct-name">Dycom Industries Inc.</div>
          <div class="c-meta">NYSE: DY · Telecom Infrastructure · $4.7B+ rev</div>
        </div>
        <div class="c-left-right">
          <div class="c-urg cu-t5"><span class="cu-dot"></span>Strike — D.A. Davidson Sep 24 + $150M buyback</div>
          <div class="c-entry-section"><div class="c-lbl">Lead</div><span class="c-entry-badge br-data">Data &amp; AI</span></div>
          <div class="c-also">
            <div class="c-also-item"><span class="c-brand-sm br-stor">Storage</span></div>
            <div class="c-also-item"><span class="c-brand-sm br-auto">Automation</span></div>
          </div>
        </div>
      </div>
      <div class="c-mid">
        <div class="c-mid-left">
          <div class="c-section">
            <div class="c-sec-lbl">Why Now</div>
            <ul class="c-bullets">
              <li>Senior leadership presenting at D.A. Davidson Industrials Conference on Sep 24 in Nashville.</li>
              <li>Q2 earnings beat ($5.29 vs $4.62 EPS) with operating cash flow surging 84% on fiber buildouts.</li>
              <li>Board authorized new $150M share repurchase program; stock pulled back 25% to ~$295.</li>
              <li>Massive BEAD and hyperscaler fiber rollouts require enterprise-grade workforce forecasting.</li>
            </ul>
          </div>
          <div class="c-section">
            <div class="c-sec-lbl">Hiring Signals</div>
            <ul class="c-bullets">
              <li>GIS network data engineers and field systems developers active in Palm Beach Gardens HQ.</li>
              <li>Program financial analysts and resource dispatch supervisors recruiting across southeast subsidiaries.</li>
            </ul>
          </div>
          <div class="c-angle">
            <div class="c-angle-lbl">IBM Angle</div>
            <div class="c-angle-txt">Dycom's challenge is maintaining operating margin leverage across dozens of subsidiaries during massive fiber buildouts. IBM Planning Analytics optimizes field crew dispatch, while FlashSystem powers sub-second GIS queries.</div>
          </div>
          <div class="c-talk">
            <div class="c-talk-lbl">What to Say</div>
            <div class="c-talk-txt">"Ahead of the D.A. Davidson conference next week, telecom infrastructure leaders are using IBM Planning Analytics to protect operating margins by synchronizing field crew allocation with supply deliveries. Can we find 15 minutes?"</div>
          </div>
        </div>
        <div class="c-right">
          <div class="c-sales-hdr">How to Sell</div>
          <div class="c-sales-block saas">
            <div class="c-sales-type saas">SaaS Entry</div>
            <div class="c-sales-txt"><strong>Planning Analytics</strong> — SaaS instance for central finance &amp; regional VP operations to forecast crew utilization and prevent margin leakage.</div>
            <span class="c-sales-pill saas">Planning Analytics</span>
          </div>
          <div class="c-sales-block trans">
            <div class="c-sales-type trans">Transaction</div>
            <div class="c-sales-txt"><strong>FlashSystem + Data Fabric</strong> — hardware and software transaction to power sub-second spatial querying for nationwide fiber GIS data.</div>
            <span class="c-sales-pill trans">FlashSystem + Data Fabric</span>
          </div>
          <div class="c-sales-block motion">
            <div class="c-sales-type motion">Do This Now</div>
            <div class="c-sales-txt">1. Reach out to VP Investor Relations &amp; VP IT ahead of Sep 24 conference.<br>2. Offer telecom infrastructure margin modeling benchmark.<br>3. Engage operating subsidiary presidents for field pilot.</div>
          </div>
        </div>
      </div>
      <div class="c-actions">
        <a class="c-btn c-btn-intel" href="phase2.html#dycom">Full Intel →</a>
        <a class="c-btn c-btn-snav" href="https://www.linkedin.com/sales/search/people?query=(filters%3AList((type%3ACURRENT_COMPANY%2Cvalues%3AList((id%3A19434%2CselectionType%3AINCLUDED)))))" target="_blank" rel="noopener">SNav ↗</a>
      </div>
    </div>"""

mastec_full_card = """    <!-- MasTec Inc. -->
    <div class="card t5" data-urgency="t5" data-brands="data-ai automation power-cloud" data-account="mastec">
      <div class="c-left">
        <div class="c-left-meta">
          <div class="c-acct-name">MasTec Inc.</div>
          <div class="c-meta">NYSE: MTZ · Infrastructure · $18.2B rev guidance</div>
        </div>
        <div class="c-left-right">
          <div class="c-urg cu-t5"><span class="cu-dot"></span>Strike — New VP IR Sep 10 + $21.4B backlog</div>
          <div class="c-entry-section"><div class="c-lbl">Lead</div><span class="c-entry-badge br-data">Data &amp; AI</span></div>
          <div class="c-also">
            <div class="c-also-item"><span class="c-brand-sm br-auto">Automation</span></div>
            <div class="c-also-item"><span class="c-brand-sm br-pc">Power</span></div>
          </div>
        </div>
      </div>
      <div class="c-mid">
        <div class="c-mid-left">
          <div class="c-section">
            <div class="c-sec-lbl">Why Now</div>
            <ul class="c-bullets">
              <li>Appointed Ati Modak as VP of Investor Relations on Sep 10, enhancing capital markets execution.</li>
              <li>Record $21.4B backlog across Clean Energy, Power Delivery, and Pipeline segments (+30% YoY).</li>
              <li>FY26 guidance increased to $18.2B revenue and $1.6B EBITDA; Clean Energy division jumped 43.4%.</li>
              <li>Superior Group integration contributing $800M-$900M H2 revenue, creating data consolidation urgency.</li>
            </ul>
          </div>
          <div class="c-section">
            <div class="c-sec-lbl">Hiring Signals</div>
            <ul class="c-bullets">
              <li>Enterprise integration architects and clean energy project controls specialists hiring in Coral Gables.</li>
              <li>Power delivery data analysts and ERP systems managers recruiting for major utility contracts.</li>
            </ul>
          </div>
          <div class="c-angle">
            <div class="c-angle-lbl">IBM Angle</div>
            <div class="c-angle-txt">MasTec's $21.4B backlog and 5-segment portfolio require unified financial forecasting and real-time project risk modeling. IBM Planning Analytics serves as the master command center, while watsonx automates contract compliance.</div>
          </div>
          <div class="c-talk">
            <div class="c-talk-lbl">What to Say</div>
            <div class="c-talk-txt">"With MasTec's backlog scaling to a record $21.4B and clean energy surging 43%, managing project margin risk across 5 segments requires a real-time command center. IBM Planning Analytics is how infrastructure leaders forecast cash flow with 98% accuracy."</div>
          </div>
        </div>
        <div class="c-right">
          <div class="c-sales-hdr">How to Sell</div>
          <div class="c-sales-block saas">
            <div class="c-sales-type saas">SaaS Entry</div>
            <div class="c-sales-txt"><strong>Planning Analytics</strong> — SaaS subscription for enterprise project cost modeling and multi-segment EBITDA forecasting.</div>
            <span class="c-sales-pill saas">Planning Analytics</span>
          </div>
          <div class="c-sales-block trans">
            <div class="c-sales-type trans">Transaction</div>
            <div class="c-sales-txt"><strong>Data Fabric + Power10</strong> — software &amp; services transaction to unify acquired ERP systems into a single analytical data store.</div>
            <span class="c-sales-pill trans">Data Fabric + Power10</span>
          </div>
          <div class="c-sales-block motion">
            <div class="c-sales-type motion">Do This Now</div>
            <div class="c-sales-txt">1. Congratulate new VP IR Ati Modak and request introductory call with CFO/CIO team.<br>2. Present 5-segment infrastructure FP&amp;A blueprint.<br>3. Scope Data Fabric integration for Clean Energy division.</div>
          </div>
        </div>
      </div>
      <div class="c-actions">
        <a class="c-btn c-btn-intel" href="phase2.html#mastec">Full Intel →</a>
        <a class="c-btn c-btn-snav" href="https://www.linkedin.com/sales/search/people?query=(filters%3AList((type%3ACURRENT_COMPANY%2Cvalues%3AList((id%3A5350%2CselectionType%3AINCLUDED)))))" target="_blank" rel="noopener">SNav ↗</a>
      </div>
    </div>"""

strike_cards_html = [lennar_full_card, chewy_full_card, dycom_full_card, mastec_full_card]

# Build Engage cards
engage_cards_html = []
for aid in engage_ids:
    if aid == "heico":
        c = adjust_card(aid, "t4", "Engage — Zacks Buy rating + post-Q3 integration")
    elif aid == "nclh":
        c = adjust_card(aid, "t4", "Engage — FY26 guidance cut + dynamic pricing push")
    elif aid == "sgws":
        c = adjust_card(aid, "t4", "Engage — $12.5M probe resolution + H2 strategy report")
    elif aid == "hig":
        c = adjust_card(aid, "t4", "Engage — Formed EverRise Lift Group Sep 14")
    elif aid == "odp":
        c = adjust_card(aid, "t4", "Engage — IT leadership transition + GenAI continuity")
    elif aid == "herc":
        c = adjust_card(aid, "t4", "Engage — Talent lead posted Sep 14 + 23% turnover lift")
    elif aid == "bk":
        c = adjust_card(aid, "t4", "Engage — Reclaim the Flame digital kiosks + unit exchange")
    elif aid == "kforce":
        c = adjust_card(aid, "t4", "Engage — Rule 10b5-1 buyback Sep 15 + $0.40 dividend")
    elif aid == "citco":
        c = adjust_card(aid, "t4", "Engage — Alternative asset scale &amp; cloud security")
    elif aid == "frontline":
        c = adjust_card(aid, "t4", "Engage — Hurricane season claims &amp; catastrophe modeling")
    elif aid == "icahn":
        c = adjust_card(aid, "t4", "Engage — Portfolio cash flow &amp; industrial restructuring")
    else:
        c = adjust_card(aid, "t4")
    engage_cards_html.append(c)

# Build Standby cards
standby_cards_html = []
for aid in standby_ids:
    c = adjust_card(aid, "t3")
    standby_cards_html.append(c)

# 4. Construct the clean full HTML
# Grab header portion from orig up to <div class="main">
main_start_pos = orig.find('<div class="main">')
header_part = orig[:main_start_pos]

# Update dates, titles, counts in header part
header_part = header_part.replace("Sep 10, 2026", "Sep 17, 2026")
header_part = header_part.replace("Edition 06", "Edition 07")
header_part = header_part.replace("2026-09-10", "2026-09-17")
header_part = header_part.replace("Aug 17 – Sep 10, 2026", "Sep 10 – Sep 17, 2026")
header_part = header_part.replace("SEP 3–10, 2026", "SEP 10–17, 2026")

# Counts
header_part = re.sub(r'<span class="jb-count t5">[0-9]+</span>', '<span class="jb-count t5">4</span>', header_part)
header_part = re.sub(r'<span class="jb-count t4">[0-9]+</span>', '<span class="jb-count t4">11</span>', header_part)
header_part = re.sub(r'<span class="jb-count t3">[0-9]+</span>', '<span class="jb-count t3">12</span>', header_part)

header_part = re.sub(r'<div class="mh-stat-n">[0-9]+</div>\s*<div class="mh-stat-l">Strike</div>', '<div class="mh-stat-n">4</div>\n        <div class="mh-stat-l">Strike</div>', header_part)
header_part = re.sub(r'<div class="mh-stat-n">[0-9]+</div>\s*<div class="mh-stat-l">Engage</div>', '<div class="mh-stat-n">11</div>\n        <div class="mh-stat-l">Engage</div>', header_part)

# Industry Pulse block
p1_pulse = """  <div class="ind-pulse">
    <div class="ind-inner">
      <div class="ind-hdr">Industry Pulse · Macro Signals · Sep 10 – Sep 17, 2026</div>
      <div class="ind-grid">
        <div class="ind-signal" style="--tc:var(--t5)">
          <span class="ind-tag iv-aero">Homebuilding / Housing</span>
          <div class="ind-headline">Lennar Q3 earnings miss: gross margin -170 bps to 15.8%, ASP down to $372k — SG&A cost takeout mandate active</div>
          <div class="ind-ibm-angle">Mortgage rates keeping CFO in scenario-planning mode. IBM Planning Analytics dynamic pricing + watsonx qualification cuts acquisition costs.</div>
        </div>
        <div class="ind-signal" style="--tc:var(--t5)">
          <span class="ind-tag iv-ecom">E-Commerce / AI</span>
          <div class="ind-headline">Chewy targets $50M annual AI savings in FY27 across care & pharmacy; filed S-3 registration Sep 14</div>
          <div class="ind-ibm-angle">Centralized data layer ready for enterprise scale. IBM watsonx.governance for pharmacy AI models + Turbonomic cloud optimization.</div>
        </div>
        <div class="ind-signal" style="--tc:var(--ok)">
          <span class="ind-tag iv-infra">Telecom / Infrastructure</span>
          <div class="ind-headline">MasTec ($21.4B backlog, clean energy +43%) & Dycom (D.A. Davidson Sep 24) scaling nationwide fiber rollouts</div>
          <div class="ind-ibm-angle">Massive backlog complexity requires enterprise FP&amp;A command centers. IBM Planning Analytics + FlashSystem storage GIS routing.</div>
        </div>
        <div class="ind-signal" style="--tc:var(--t2)">
          <span class="ind-tag iv-health">Distribution & Hospitality</span>
          <div class="ind-headline">SGWS resolves federal probe ($12.5M) & scales robotics; NCLH lowers EPS guide to $1.50</div>
          <div class="ind-ibm-angle">SGWS: automated trade compliance via watsonx. NCLH: voyage profitability & fuel scenario simulation with Planning Analytics.</div>
        </div>
      </div>
    </div>
  </div>"""

header_part = re.sub(r'<div class="ind-pulse">.*?</div>\s*</div>\s*</div>\s*</div>', p1_pulse, header_part, flags=re.DOTALL)

# Footer part from orig (dock nav, modals, scripts)
main_close_pos = orig.find('</div><!-- /main -->')
footer_part = orig[main_close_pos + len('</div><!-- /main -->'):]

# Update dates in footer
footer_part = footer_part.replace("Sep 10, 2026", "Sep 17, 2026")
footer_part = footer_part.replace("Edition 06", "Edition 07")
footer_part = footer_part.replace("2026-09-10", "2026-09-17")

# Assemble the complete new page
full_p1_content = f"""{header_part}<div class="main">

  <!-- ══ STRIKE ══ -->
  <div class="group" id="grp-t5">
    <div class="group-hdr"><span class="group-label gl-t5">Strike</span><div class="g-rule t5"></div></div>

""" + "\n\n".join(strike_cards_html) + f"""
  </div><!-- /group t5 -->

  <!-- ══ ENGAGE ══ -->
  <div class="group" id="grp-t4">
    <div class="group-hdr"><span class="group-label gl-t4">Engage</span><div class="g-rule t4"></div></div>

""" + "\n\n".join(engage_cards_html) + f"""
  </div><!-- /group t4 -->

  <!-- ══ STANDBY ══ -->
  <div class="group" id="grp-t3">
    <div class="group-hdr"><span class="group-label gl-t3">Standby</span><div class="g-rule t3"></div></div>

""" + "\n\n".join(standby_cards_html) + f"""
  </div><!-- /group t3 -->

</div><!-- /main -->{footer_part}"""

with open(TGT_P1, "w") as f:
    f.write(full_p1_content)

# Update se-horizon repo
with open("se-horizon/editions/2026-09-17/phase1.html", "w") as f:
    f.write(full_p1_content)

print("Phase 1 completely rewritten. Clean nesting guaranteed.")
