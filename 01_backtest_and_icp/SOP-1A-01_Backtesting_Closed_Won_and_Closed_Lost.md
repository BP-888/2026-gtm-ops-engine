# SOP-1A-01: Backtesting Closed-Won and Closed-Lost

| Field | Value |
|---|---|
| SOP ID | SOP-1A-01 |
| Phase | Phase 1: Backtest and ICP Modeling |
| Component | Component 1A: Backtest Model |
| Version | v1.0 |
| Status | **Final (baseline)**: approved structure. Pipeline stages, beta rule and reason lists are B2B SaaS best-practice baselines that Brad will tune directly in HubSpot |
| Owner | Brad (Head of Sales & Operations) |
| Last updated | 2 Oct 2026 |
| Depends on | None. This is the first SOP in the playbook. |
| Feeds | SOP-1B-01 Building the ICP Model *(planned)* · SOP-2B-01 Generating Lookalike Audiences (seed sets) · SOP-3B-01 Size-Based Tiering *(planned)* |

---

## 1. Overview & Context

**What this SOP achieves.** It turns ERMOS's real sales outcomes into evidence about who actually buys, who doesn't, and why. Every closed deal, won or lost, is captured in HubSpot with a fixed set of fields. Then, on a schedule, the closed deals are analysed for patterns. Those patterns are written up as **ICP hypotheses** for Brad to accept or reject in SOP-1B-01.

**How it aligns with Phase 1.** The blueprint's Phase 1 flow is **Backtest Model → CRM Sync → Closed Won / Closed Lost → ICP Model**:
- **Closed Won:** analyse the highest-spend customers, and interview the people who sold and serviced them (the blueprint's "AEs and CSMs"; at ERMOS that's the founders, John Moustache and partner staff).
- **Closed Lost:** look for what the lost deals have in common.
- **Output:** feeds the ICP Model (Component 1B), which feeds everything downstream.

**Final Output alignment.** Backtesting decides which firms count as **Accounts Mapped**, what the **Company Tiers** really predict, and which **Signals** are worth tracking. It's the quality check behind the whole Prioritization equation.

**ERMOS reality check (2 Oct 2026).** This SOP has two modes, because there is almost no closed-deal data yet.

| Fact (checked live, 2 Oct 2026) | Consequence |
|---|---|
| HubSpot (portal "ERMOS") has **0 deals** in any stage | There is nothing to backtest in the CRM yet |
| HubSpot has **487 company records**, and the sample checked was auto-created leads from unrelated email domains (e.g. outreach and PR senders) | Company records alone are **not** evidence of fit. They are excluded from the backtest |
| Only the default pipeline exists; `closed_won_reason` and `closed_lost_reason` are free-text | Outcomes can't be compared until reasons are standardised |
| The portal currency is **USD** and the timezone **US/Eastern** | All ERMOS pricing is AUD, ex GST, and the business runs on Sydney time. Fix this before the first deal is created |
| Known outcomes live **outside** HubSpot: the law and accounting beta engagements, the 30 Sep partner discussions, website trial and consultation requests | These must be backfilled as deals before the first backtest |

- **Mode A: Foundation and Backfill** (run once, now): configure HubSpot for backtesting and load every known outcome.
- **Mode B: Recurring Backtest** (monthly, once there's enough data): pull closed deals, analyse, publish hypotheses.

## 2. Visuals & References

| Reference | Location |
|---|---|
| Playbook blueprint | `00_global_context/GTM_Playbook_2026.pdf`: Backtest Model, CRM Sync, Closed Won (Analyze Highest Spend Customers; Interview AEs and CSMs), Closed Lost (Look for Commonalities), ICP Model |
| Hierarchy map | `00_global_context/gtm_playbook_2026_flow.md`, Phase 1 / Component 1A |
| Figma: Phase 1 overview | `[FIGMA PLACEHOLDER: Phase 1 Backtest and ICP Modeling frame, link TBD]` |
| Figma: 1A workflow diagram | `[FIGMA PLACEHOLDER: SOP-1A-01 n8n flows WF-1A-A/B/C, link TBD]` |
| Workflows.io technical reference | `[TO ADD: equivalent Workflows.io closed-won / win-loss / ICP backtest playbook URL]`. workflows.io is blocked by this environment's network policy, so the automation design in section 6 is **not yet validated against Workflows.io** (CLAUDE.md rule) |
| Context: tiers, verification rules, buying committee | `00_global_context/account_scoring_and_enrichment.md` |
| Context: verticals, sources, pipeline folders | `00_global_context/data_extraction_broad_map.md` |
| Context: competitors (loss reasons, "competitor considered") | `00_global_context/ermos_competitive_analysis.md` |
| Context: partner attribution and deal registration | `00_global_context/meeting_ermos_comarket.md` |
| Pricing basis for MRR checks | Notion 05 Decisions Log: Edge scaling rules (24 Sep) and Dominion per-seat pricing (28 Sep) |

## 3. Tools Required

| Tool | Role in this SOP | Access / credentials | Stack status |
|---|---|---|---|
| **HubSpot** (portal ERMOS, ap1) | System of record for deals, companies, contacts, win/loss fields and interview notes | Super admin to configure settings and properties (one-off). n8n private app token with CRM read/write scopes | **Core** |
| **n8n** | Runs the three workflows: close capture, monthly backtest, interview capture | ERMOS n8n instance (hosting TBD), HubSpot / Google / Slack credentials | **Core** |
| **Google Sheets: `Backtest_Dataset`** (new tab in ICP_Master) | Flat analysis table, one row per closed deal | Google service account | **Infrastructure** |
| **Google Drive: `3. DATA / backtest/`** (new folder) | Monthly report files (CSV, JSON, Markdown) | Google service account | **Infrastructure** |
| **Slack** | Missing-field alerts, monthly summary, approval prompt | n8n Slack credential; channel TBD (e.g. `#gtm-pipeline`) | **Infrastructure** |
| **n8n Form** | Structured interview capture | Built into n8n | **Core** (part of n8n) |
| **Claude API (Anthropic)** | Optional: drafts the narrative summary of the monthly numbers, with a strict "no claim beyond the sample" prompt | API key in the n8n credential store | **Infrastructure** |
| **ICP_Master (Google Sheets)** | Source of verified staff count, vertical and signals for backfilled firms | Read | **Infrastructure** |
| **Gmail / Smartlead / website form records** | Evidence for backfilling outcomes in Mode A | Brad's accounts (manual) | Smartlead: **Core**. Gmail and website form: manual sources only, no integration built |

## 4. The Absolutes (Non-negotiables)

### Before starting
1. **HubSpot is configured** (Mode A step 1): AUD currency, Australia/Sydney timezone, the ERMOS pipeline, and every required property in 6.3 exists.
2. **Only deals are analysed.** A company counts only if it has a deal that reached Closed Won or Closed Lost. Auto-created companies without deals are never evidence.
3. **Every analysed firm has a verified staff count** (from the firm's own website, ICP_Master rule) and a tier computed from it: Tier 3 = 1–9, Tier 1 = 10–30, Tier 2 = 31–50. Vendor headcount is never used.
4. **Credentials stay in n8n.** No HubSpot token or API key appears in sheets, reports, prompts or this repo.

### Before completing
5. **Every closed deal has all required close fields** (6.3), coded from the fixed lists. "Other" needs a written explanation.
6. **Sample size is stated next to every finding**, e.g. "law, won 2 / lost 1". Below the thresholds in section 7 a finding is labelled **Hypothesis**, never **Pattern**.
7. **No ICP or tier rule changes automatically.** Backtest output is a recommendation. Only Brad changes the ICP, through SOP-1B-01 and the Decisions Log.
8. **The report is reproducible:** each monthly run saves the exact dataset it analysed (CSV) next to the report, with a run id.
9. **People data stays in HubSpot.** Reports and Drive files carry company-level and deal-level data only. Interview notes name roles, not people, outside HubSpot. Internal names follow the naming rule: John Moustache internally.

## 5. Step-by-Step Procedure

### Mode A: Foundation and Backfill (run once; about 1 day of Brad's time plus 30–60 minutes of each founder's)

**Step A1: Fix the HubSpot account settings (Brad, 15 minutes; approved 2 Oct 2026)**
1. In HubSpot Settings → Account defaults, set the **time zone to Australia/Sydney**.
2. Set **company currency to AUD**. Do this before the first deal is created: changing currency is simplest while the portal has 0 deals. If HubSpot won't allow the change, add AUD as the deal currency and record that in Open Items.
3. Record the before and after values in the run log.

**Step A2: Create the ERMOS pipeline (Brad, 20 minutes)**
Rename the default "Sales Pipeline" to **"ERMOS New Business"** and set the stages below. This is a **B2B SaaS best-practice baseline** (approved 2 Oct 2026). Brad tunes the names and probabilities directly in HubSpot later. Every stage has exit criteria, so the backtest can see exactly where deals stall.

| # | Stage | Exit criteria (what must be true to move on) | Required properties on entry | Baseline win probability |
|---|---|---|---|---|
| 1 | Discovery Booked | A first meeting is in the calendar | Company vertical, `ermos_deal_source` | 10% |
| 2 | Discovery Completed (Qualified) | Pain confirmed; fits ICP (vertical, 1–50 staff); Decision Maker identified | Verified staff count and tier; DM association | 20% |
| 3 | Solution Demo | ERMOS shown against their workflow; product direction (Edge / Dominion) agreed | `ermos_product` | 35% |
| 4 | Trial / Pilot | 30-day trial or beta live, with agreed success criteria | `ermos_deal_category` (Trial / Beta), seats estimate | 50% |
| 5 | Proposal / SoW Sent | Commercial offer issued | `ermos_seats`, `ermos_mrr_aud`, `ermos_pricing_basis` | 65% |
| 6 | Negotiation / Contract Sent | Agreement out for signature | Close date | 80% |
| 7 | Closed Won | Signed agreement, or a paid subscription active | All close fields (6.3) | 100% |
| 8 | Closed Lost | Opportunity ended at any stage | All close fields (6.3), including `ermos_stage_lost_at` | 0% |

Deals may skip stages (e.g. straight from Demo to Proposal). Skipped stages stay blank, never back-filled.

**Step A3: Create the custom properties (Brad, or n8n via HubSpot API, 30 minutes)**
Create every property in 6.3 with exactly the internal names and options given. Make the close fields **required for Closed Won and Closed Lost** in the pipeline's stage settings, so HubSpot blocks a close with missing data.

**Step A4: Backfill known outcomes (Brad, about 2 hours)**
1. List every opportunity that reached a decision, from:
   - the beta SoWs (law and accounting);
   - signed or declined partner discussions that involved an end customer;
   - website consultation and trial requests (excluding test submissions);
   - Smartlead replies that ended an opportunity ("not interested", "using Copilot", etc.);
   - founder-network conversations.
2. For each one, create the company (if not already present, matched on domain), the deal, and the associated contacts with buying-committee labels (Decision Maker / Influencer / Champion).
3. Fill every close field. **Beta rule (baseline):** a beta engagement with a **signed SoW** is **Closed Won** with `ermos_deal_category = Beta` and `ermos_pricing_basis = Beta`. Beta wins are reported separately from paid wins and never count towards highest-spend analysis. An **unsigned or still-running** beta stays at **Trial / Pilot**. A beta that ended without converting is **Closed Lost** with a coded reason. Confirm each with the founder who owns it.
4. Set `ermos_backtest_include = true` only for real end-customer opportunities (not tests, partners or vendors).

**Step A5: Interview the people who sold them (Brad runs it; David, Will and John Moustache answer; 30–45 minutes each)**
1. For each won and lost deal they were involved in, the interviewer fills the n8n form **"1A Deal Interview"** (WF-1A-C) live during the conversation.
2. The questions are fixed (6.4), so answers can be compared across deals.
3. The form writes a structured note to the HubSpot deal and a row to `Backtest_Interviews`.

**Step A6: First baseline report (n8n WF-1A-B, run manually)**
1. Run the backtest once over the backfilled data.
2. Expect almost everything to be labelled **Hypothesis**. That's the correct output at this stage.
3. Brad reviews it and takes any hypotheses worth acting on into SOP-1B-01.

### Mode B: Recurring Backtest (monthly)

**Step B1: Capture at close (automatic, WF-1A-A)**
1. When any deal moves to Closed Won or Closed Lost, n8n checks the close fields, snapshots the company's tier, vertical, source and signals at that moment, and appends a row to `Backtest_Dataset`.
2. If anything is missing, the deal owner gets a HubSpot task and a Slack DM within minutes.

**Step B2: Monthly run (automatic, WF-1A-B, first business day, 8:00 Sydney)**
n8n pulls all closed deals with `ermos_backtest_include = true`, then computes the analysis set (section 6.5):
- win rate and average MRR by vertical, tier, product, source and partner;
- the **highest-spend profile** (the top 25% of won deals by MRR: what they share);
- the **lost-deal commonalities** (reason codes, competitor considered, stage lost, tier, vertical);
- sales cycle length;
- signal presence on won vs lost deals.

**Step B3: Review and decide (Brad, 30 minutes)**
1. Read the Slack summary and the Markdown report.
2. For each finding marked **Pattern**, choose **Accept → SOP-1B-01** (ICP change proposal), **Watch** (re-test next month) or **Reject** (with reason).
3. Decisions are recorded in the `Backtest_Decisions` tab. Accepted ones are logged in Notion 05 Decisions Log when the ICP actually changes.

**Step B4: Quarterly interview round (Brad)**
Every quarter, re-interview owners of the quarter's three highest-MRR wins and three most recent losses, using the same form (WF-1A-C).

## 6. Data Flow & Automation

### 6.1 n8n workflow WF-1A-A: "1A Close Capture"

| # | Node | Purpose | Notes |
|---|---|---|---|
| 1 | **HubSpot Trigger** (deal property change: `dealstage`) | Fires on every stage change | Continue only if the new stage is `closedwon` or `closedlost` |
| 2 | **HubSpot: Get deal** + associated company and contacts | Load the full record | Deal close fields; company `ermos_verified_staff_count`, `ermos_vertical`, `ermos_account_tier`, state; contact association labels |
| 3 | **Code: Validate** | Check required fields (6.3); tier vs staff-count consistency; MRR sanity check (section 8) | Outputs `valid` / `missing[]` / `anomalies[]` |
| 4 | **IF: Missing fields** | Missing → create a HubSpot task on the deal for its owner ("Complete close fields: …") and send a Slack DM | Re-checks when the deal updates (same trigger) |
| 5 | **Google Sheets: Append/Update** `Backtest_Dataset` | One row per deal, keyed on `deal_id` (update if it already exists) | Snapshot at close: later company edits don't rewrite history |
| 6 | **Slack: Post** to the pipeline channel | "Closed Won: law, Tier 1, Edge, 18 seats, A$1,782 MRR, source Partner referral" | No personal names in the channel |
| E | **Error Workflow** | Failure → Slack alert with deal id; no partial row | Shared n8n error workflow |

### 6.2 n8n workflow WF-1A-B: "1A Monthly Backtest"

| # | Node | Purpose | Notes |
|---|---|---|---|
| 1 | **Schedule Trigger**: first business day of the month, 08:00 Australia/Sydney; also a Manual Trigger | Start the run | `run_id = 1A-<YYYYMM>` |
| 2 | **HubSpot: Search deals** `dealstage IN (closedwon, closedlost)` AND `ermos_backtest_include = true` | All closed deals to date | Paginate; include associations |
| 3 | **Google Sheets: Read** `Backtest_Dataset` + `Backtest_Interviews` | Snapshots and interview codes | The sheet snapshot wins over live HubSpot values for company fields at close |
| 4 | **Code: Build analysis set** | Join, dedupe by `deal_id`, compute metrics (6.5), apply sample-size labels | Deterministic: same input, same output |
| 5 | **Code: Flag checks** | Apply the flagging triggers (section 8) | Flags go into the report |
| 6 | **Claude API (optional)** | Turn the computed tables into a short narrative. The system prompt forbids any claim not in the tables and requires the n next to every statement | Numbers come from node 4, never from the model |
| 7 | **Google Drive: Upload** to `3. DATA/backtest/` | `backtest_<YYYYMM>_dataset.csv`, `backtest_<YYYYMM>_metrics.json`, `backtest_<YYYYMM>_report.md` | Never overwrite: one set per run |
| 8 | **Google Sheets: Append** `Backtest_Decisions` | One row per finding, with Decision blank | Brad fills in the Decision |
| 9 | **Slack: Post** | Headline metrics, top 3 findings with labels, flags, link to the report | Includes "Review findings" link |
| E | **Error Workflow** | As WF-1A-A | n/a |

### 6.3 HubSpot property schema (custom properties, internal names)

**Company**

| Internal name | Type | Options / rule |
|---|---|---|
| `ermos_vertical` | Dropdown | `accounting` · `law` · `aged care` · `healthcare` · `finance` |
| `ermos_verified_staff_count` | Number | From the firm's own website |
| `ermos_staff_count_evidence` | Single-line text | URL or exact phrase that confirmed the count |
| `ermos_account_tier` | Dropdown | `T1` (10–30) · `T2` (31–50) · `T3` (1–9) · `DQ` (over 50) · `Unverified`. Set by n8n from the verified count, never by hand |
| `ermos_state` | Dropdown | NSW · VIC · QLD · WA · SA · TAS · ACT · NT |

**Deal**

| Internal name | Type | Options / rule |
|---|---|---|
| `ermos_product` | Dropdown | `Edge` · `Dominion` · `Both` |
| `ermos_seats` | Number | Contracted seats |
| `ermos_mrr_aud` | Number (AUD) | Monthly recurring subscription, ex GST |
| `ermos_pricing_basis` | Dropdown | `Standard` · `VIP` · `Beta` · `Discounted` |
| `ermos_deal_category` | Dropdown | `Paid` · `Beta` · `Trial` |
| `ermos_deal_source` | Dropdown | `Outbound: Automated` · `Outbound: Manual` · `Inbound: Website form` · `Inbound: Trial request` · `Partner: Referral` · `Partner: Reseller` · `Founder network` · `Event / Webinar` |
| `ermos_partner_name` | Single-line text | Required when source is Partner. Matches the client's backend-instance registration |
| `ermos_win_reason_primary` | Dropdown (required at Closed Won) | `Data sovereignty / onshore` · `Client confidentiality` · `Privacy Act / compliance` · `Workflow fit` · `Price / commercial model` · `Partner trust` · `Champion-led` · `Other` |
| `ermos_loss_reason_primary` | Dropdown (required at Closed Lost) | `No budget` · `Timing / not now` · `Chose Microsoft 365 Copilot` · `Chose public AI (ChatGPT / Claude / Gemini / Grok)` · `Built in-house / IT provider` · `Security or IT objection` · `No decision / went dark` · `Not a fit: vertical` · `Not a fit: size` · `Other` |
| `ermos_competitor_considered` | Multi-checkbox | `Microsoft 365 Copilot` · `ChatGPT` · `Claude` · `Gemini` · `Grok` · `In-house / IT provider` · `None` · `Other` |
| `ermos_stage_lost_at` | Dropdown | The pipeline stage before Closed Lost (stages 1–6 in step A2) |
| `ermos_reason_notes` | Multi-line text | Required if the reason is `Other` |
| `ermos_backtest_include` | Checkbox | False for tests, partners and vendors |

HubSpot's standard `closed_won_reason` and `closed_lost_reason` (free text) stay available for narrative. Analysis uses the coded fields only.

**Contact ↔ Deal association labels:** `Decision Maker`, `Influencer`, `Champion` (the buying committee in `CLAUDE.md`).

### 6.4 Interview form (WF-1A-C "1A Deal Interview")
**Trigger:** n8n Form. **Fields:** `deal_id`, interviewer, interviewee role (Founder / Partner / Customer), and these fixed questions, mostly coded with optional free text:
1. What triggered the firm to look now? (`Client incident` · `Regulation / Privacy Act` · `Staff using public AI` · `IT provider recommendation` · `Peer referral` · `Our outreach` · `Other`)
2. Who championed it internally (role)?
3. Who signed (role)? Was anyone a blocker (role)?
4. What alternatives were considered? (same list as `ermos_competitor_considered`)
5. What was the deciding factor? (same list as the win or loss reason)
6. What nearly killed the deal, or what did?
7. How long from first touch to decision (weeks)?
8. Which product and why?
9. On a 1–5 scale, how typical is this firm of who we should target?
10. One thing we'd change in how we sold it.

**Flow:** Form → Code (validate `deal_id`) → HubSpot: create Note on the deal (structured) → Google Sheets: append `Backtest_Interviews` (coded answers only, no names) → Slack confirmation to the interviewer.

### 6.5 Analysis set (computed in WF-1A-B node 4)

| Output | Definition |
|---|---|
| Win rate | Won ÷ (Won + Lost), by vertical, tier, product, source and partner |
| Highest-spend profile | Top 25% of won deals by `ermos_mrr_aud`: share of each vertical, tier, state, source, product, win reason. Compared with all won deals |
| Lost commonalities | Distribution of `ermos_loss_reason_primary`, `ermos_competitor_considered`, `ermos_stage_lost_at` and tier / vertical among losses, compared with wins |
| Sales cycle | Median days from create to close, won vs lost |
| Signal lift | Share of won vs lost deals whose company had each tracked signal (once Phase 5 exists) |
| Sample label | Per cut: **Pattern** if at least 5 won **and** 5 lost in that cut; otherwise **Hypothesis** |

### 6.6 Data flow summary

```
Mode A (once):  Gmail / Smartlead / SoWs / founder knowledge ──(manual backfill)──► HubSpot deals + companies + contacts
                Founder & partner interviews ──► n8n Form (WF-1A-C) ──► HubSpot deal notes + Backtest_Interviews

Mode B (ongoing):
  HubSpot deal → Closed Won/Lost ──► n8n WF-1A-A ──► validate ──► Backtest_Dataset (snapshot)  + HubSpot task / Slack DM if incomplete
  Monthly schedule ──► n8n WF-1A-B ──► HubSpot (closed deals) + Backtest_Dataset + Backtest_Interviews
                                     ──► metrics + labels ──► Drive 3. DATA/backtest (CSV, JSON, MD)
                                     ──► Backtest_Decisions (Brad decides) ──► SOP-1B-01 ICP change proposals
                                     ──► Slack summary
```

**Systems of record:** HubSpot holds deals, companies, contacts and interview notes. `Backtest_Dataset` holds the frozen close-time snapshot. Drive holds the monthly reports. The ICP itself changes only through SOP-1B-01.

## 7. Quality Assurance (QA) Guidelines

### What "Good" Looks Like

| Metric | Target |
|---|---|
| Close-field completeness | 100% of Closed Won / Closed Lost deals have every required field within 2 business days of close |
| "Other" reason rate | ≤ 15% of closed deals (higher means the reason lists need revising) |
| Tier integrity | 100% of analysed deals have a verified staff count and a tier matching it |
| Interview coverage | 100% of wins and at least 50% of losses interviewed in Mode A; quarterly round done on time in Mode B |
| Reproducibility | Every report has its dataset CSV and run id; re-running gives the same metrics |
| Decision closure | Every **Pattern** finding has an Accept / Watch / Reject decision within 5 business days |

**A good report reads like this:** "Law, Tier 1: won 6 / lost 5 (**Pattern**). Highest-spend wins are 70% partner-sourced, and data sovereignty is the primary win reason in 5 of 6. Losses cluster at Trial / Beta (4 of 5), with 3 choosing Copilot. Recommendation: test 'Copilot already licensed' as a negative fit signal (→ SOP-1B-01)."

### What "Bad" Looks Like
- **Backtesting on HubSpot companies without deals,** e.g. the 487 auto-created companies. That's noise, not customers.
- **Tiny-sample certainty:** "law wins 100% of the time" from 2 deals.
- **Free-text loss reasons** that can't be counted ("they went quiet I think").
- **Tier taken from vendor headcount,** or a tier edited by hand to match a story.
- **Treating beta or trial as won revenue:** beta engagements belong in `ermos_deal_category = Beta`, analysed separately from paid wins.
- **Partner deals without partner attribution,** which breaks commission and partner-signal analysis.
- **Changing the ICP straight from a report** without SOP-1B-01 and Brad's decision.
- **USD amounts or US-time dates** in an AUD, Sydney business.

## 8. Exception Handling

### Auto-Pass Criteria
A closed deal goes into `Backtest_Dataset` and the monthly analysis with no human touch when **all** of these hold:
1. every required close field (6.3) is filled, and no reason is `Other` without notes;
2. the company has `ermos_verified_staff_count` with evidence, and `ermos_account_tier` matches it (T3 1–9, T1 10–30, T2 31–50);
3. `ermos_vertical` is one of the five approved verticals;
4. `ermos_mrr_aud` passes the sanity check: **seats × A$99** for Standard pricing (Edge and Dominion are both A$99 per seat per month, 10-seat minimum), **seats × A$49.50** for Edge VIP, or any value for `Beta` / `Discounted` when a note is present;
5. `ermos_backtest_include = true`.

### Flagging Triggers
Flagged deals still go into `Backtest_Dataset` but are **excluded from metrics** until cleared. Brad reviews them in the `Backtest_Dataset` "Flags" view; reviews are due before the monthly run.

| Code | Trigger | Reviewer action |
|---|---|---|
| `B01_missing_fields` | Close fields missing 2 business days after close | Chase the owner (automatic task), then fill |
| `B02_tier_mismatch` | Tier doesn't match the verified staff count, or the count has no evidence | Re-verify on the firm's website |
| `B03_disqualified_size` | Verified staff count over 50 on a won deal | Check: data error, or an ICP exception worth logging? |
| `B04_off_vertical` | Vertical outside the five approved | Decide: exclude, or log as an ICP expansion signal |
| `B05_mrr_mismatch` | MRR fails the sanity check, or seats are below the 10-seat minimum on Standard pricing | Confirm the commercial terms |
| `B06_partner_unattributed` | Source is Partner, but `ermos_partner_name` is empty or doesn't match a registered backend instance | Fix attribution (affects commission) |
| `B07_other_overuse` | `Other` is over 15% of a month's closes | Revise the reason lists (a schema change, approved by Brad) |
| `B08_reopened` | A closed deal reopened or changed stage after its snapshot | Re-snapshot; note the change |
| `B09_small_sample` | A cut has fewer than 5 won or 5 lost | Not an error: the finding is auto-labelled **Hypothesis** and not offered as a Pattern |

---

## Open Items

**Resolved 2 Oct 2026 (Brad):**
- **Tools:** Google Workspace, Notion, Slack and the Claude API are approved infrastructure. No tool in this SOP is pending Ask First.
- **HubSpot settings:** the switch to AUD and Australia/Sydney is approved (step A1).
- **Junk companies:** excluding the 487 auto-created companies is confirmed. Nothing is deleted.
- **Pipeline stages, beta rule, reason lists:** baselines set in step A2, step A4 and section 6.3. Brad tunes the values in HubSpot.
- **Sample threshold:** baseline of 5 won and 5 lost per cut for a Pattern.
- **Interviews:** founders and John Moustache by default. Customer champions only with their consent, optional.

**Still open:**
1. **Super-admin:** who makes the HubSpot settings change (step A1). If HubSpot won't allow the currency change, record the workaround here.
2. **Workflows.io:** section 6 isn't yet validated against a Workflows.io playbook (the site is blocked in this environment). Paste the equivalent page to validate it.
3. **n8n hosting and Slack channel names** (shared with SOP-2B-01 and SOP-5A-01).

## Change Log

| Version | Date | Author | Change |
|---|---|---|---|
| v1.0 | 2 Oct 2026 | Claude Code for Brad | Finalised: AUD/Sydney approved; 487 companies excluded; B2B SaaS baseline pipeline (8 stages with exit criteria and probabilities), beta rule and reason lists; Workspace/Slack/Claude API approved as infrastructure |
| v0.1 | 2 Oct 2026 | Claude Code for Brad | First draft, built to the CLAUDE.md SOP Template. HubSpot state checked live (0 deals, 487 companies, default pipeline, USD / US-Eastern). Tools marked against the Core Tech Stack; non-core tools pending Ask First |
