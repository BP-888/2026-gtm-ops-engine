# SOP-2B-02: Accounting Lead Generation & Enrichment Pipeline

| Field | Value |
|---|---|
| SOP ID | SOP-2B-02 |
| Phase | Phase 2: Broad TAM Mapping (sprint pipeline running through Phases 3, 4 and 8) |
| Component | Sourcing for Phase 2 (Google Maps listings; the firmographic-fit side of the map, 2A, is used here under the 2B sprint ID Brad assigned). Also executes **3A/3B** (verify and tier), **4B** (contact sourcing) and **8A** (Automated Outbound, 1:1). **4C (CRM upload) is deliberately not part of this pipeline**: cold records never enter HubSpot |
| Version | v0.4 |
| Status | **Draft for Brad's review**: Parramatta pilot passed (2 Oct 2026). Ready to run wave 1 once Apify access and caps are set |
| Owner | Brad (Head of Sales & Operations) |
| Last updated | 2 Oct 2026 |
| Depends on | `leadgen-google-scraper` skill (web-site-builder repo) and its Notion SOP v0.2 · **ICP_Master** (Google Drive) · Smartlead campaigns named per the Campaign Naming Standard (`T1` / `T2` / `T3`) |
| Feeds | SOP-5A-01 Automated Outbound Reply Management. Engaged accounts are created in HubSpot there, not here |

---

## 1. Overview & Context

**What this SOP achieves.** It grows the ERMOS accounting outbound list from **about 700 leads to 6,000** with one repeatable, cost-first pipeline: **Google Maps (Apify) → dedupe against ICP_Master → Clay (enrich, tier, 1–2 decision-makers) → ICP_Master → Smartlead**, with **n8n** connecting the steps. Every lead that reaches Smartlead is:
- at an Australian accounting practice with 1–50 staff;
- tiered by size: **T3** 1–9, **T1** 10–30, **T2** 31–50;
- recorded in **ICP_Master** before any email is sent;
- a named decision-maker with a validated email.

**Data sync rule (Brad, 2 Oct 2026).** **ICP_Master in Google Drive is the single source of truth and the only master database for the cold pipeline.**
- **HubSpot is completely bypassed in this SOP.** A firm enters HubSpot only after it shows confirmed interest (e.g. an Interested reply), and that happens in SOP-5A-01.
- This keeps the CRM clean and avoids paying for, or cluttering, CRM records for thousands of cold contacts.

**Architecture: cost-first, per the Workflows.io "TAM Mapping Playbook" (Brad, 2 Oct 2026).** Money is spent only on records that have survived every cheaper step:
1. **Cheap sourcing:** Apify scrapes raw company names, basic details and websites at scale (Stage 1). No people data.
2. **Dedupe before enrichment:** raw companies are checked **strictly against ICP_Master** (Master, Holding and Exclusions tabs), by domain and normalised company name. Known firms, existing leads and known-invalid targets are dropped **before** Clay (Stage 2).
3. **Company enrichment and tiering:** only net-new, valid companies go to Clay for firmographics, the website staff count, the ICP check and Tiers 1–3 (Stage 3).
4. **Surgical contact sourcing:** only tiered, qualified companies get a people search, through Apollo inside Clay's waterfall, capped at **1–2 decision-makers per company** (Stage 3).
5. **Store, then activate:** the finished, tiered leads are written to **ICP_Master** (Stage 4). Approved decision-makers are routed from ICP_Master straight into **Smartlead** (Stage 5).

**How it aligns with the playbook.** The sprint runs straight through the blueprint's Broad TAM Map, Account Research, Account Scoring (Tiers 1–3), Enriched TAL, Contact Sourcing and Demand Generation 1:1 (Automated Outbound). The blueprint's **CRM Upload** box is moved downstream: it happens on engagement (SOP-5A-01), not on enrichment.

**Final Output alignment.** Each firm processed adds to **Accounts Mapped**, **Company Tiers** and **Stakeholder Maps**, all held in ICP_Master. Smartlead activity then generates the **Signals** and **Awareness Scores** handled in SOP-5A-01.

**What "lead" means here.** A **lead** is one decision-maker contact, at an in-ICP firm, ready to enrol in Smartlead. The 6,000 target counts contacts, not firms (Open Items: confirm).

### Sprint maths (planning ratios; re-set from actuals)

| Step | Pass rate | Basis |
|---|---|---|
| Raw Google Maps listing → kept by the scraper (exclusions, dedupe) | 80% planned; **95% in the Parramatta pilot** (19 of 20) | Exclusion list + domain dedupe |
| → has a website / domain | 85% planned; **95% in pilot** (18 of 19) | n/a |
| → net-new after ICP_Master dedupe | TBD from wave 1 | Rises in later waves as ICP_Master fills |
| → passes ICP in Clay (accounting practice, AU, 1–50 staff, independent) | 70% | Bookkeepers, franchises and over-50 firms removed. The pilot pre-screen held 3 of 18 (bookkeepers, a possible virtual office) |
| → at least one decision-maker with a validated email | 70% | Clay people search (Apollo) + email waterfall |
| Decision-makers per firm | ~1.3 | T3 = 1; T1 and T2 = up to 2 |
| **Net leads per raw listing** | **≈ 0.40–0.45** | Re-set after wave 1 |

Needed: 6,000 − 700 = **5,300 net new leads ÷ ~0.42 ≈ 12,500 raw listings**. Wave 1 (48 high-density locations) is expected to produce roughly 4,000–6,000 unique listings. Waves 2–3 close the gap.

### Pilot result (Parramatta, 2 Oct 2026)
- Apify run `ea0R0JkbCPUZ9eZC9`: 20 places in 13 seconds. Cost under US$0.10 (the connector doesn't report cost; that's the rate-card estimate).
- **19 rows kept** (1 H&R Block franchise excluded). **95% have a domain.** All 18 columns are present, with no contact data.
- **Notion pilot criteria: PASS.**
- **ICP_Master dedupe (full read of Master 1,219 / Holding 353 / Exclusions 381 rows):** 2 suppressed.
  - Accounting Hands: already in Holding (3 staff, below-floor hold).
  - Smarter Advisory & Accounting: a **name match** in Exclusions under a different domain (`smarteraa.com.au`, network roll-up). This shows why name matching is needed alongside domain matching.
- **Review confidence (rule added 4 Oct):** of the 13 for Clay, Strong 6 (EKNIK, C&N, ATX, Silver Peacock, Beyond Taxation, Clear Tax) · Moderate 5 (Tax Save, Sanath, ATB Partners, Ray Accounting, Tax Solutions NSW) · Questionable 2 (All Pro Accounting: 1 review; Perfect Accounting: none) · Poor 0.
- **Net result:** 13 net-new to Clay, 3 held (2 bookkeepers, 1 possible virtual office), 1 with no domain.
- Files: `outputs/pipeline/01_raw/accounting_parramatta_2026-10-02_1836.csv` (+ `.run.json`), and `outputs/pipeline/02_enriched/pilot_parramatta_triage_2026-10-02.csv`.

## 2. Visuals & References

| Reference | Location |
|---|---|
| Playbook blueprint | `00_global_context/GTM_Playbook_2026.pdf`: Broad TAM Map → Account Research → Account Scoring (Tiers) → Enriched TAL → Contact Sourcing → Demand Generation (Automated Outbound) |
| Hierarchy map | `00_global_context/gtm_playbook_2026_flow.md`, Phases 2–3 and 8 |
| Figma | `[FIGMA PLACEHOLDER: SOP-2B-02 sprint pipeline, link TBD]` |
| Workflows.io technical reference | **"TAM Mapping Playbook"** (architecture supplied by Brad, 2 Oct 2026; the page is blocked in this environment). Its five-step, cost-first sequence is adopted in §1 and Stages 1–5. **Deviation:** the playbook's CRM push is replaced by ICP_Master storage (ERMOS data sync rule) |
| Source skill | `web-site-builder` repo, `skills/leadgen-google-scraper/` (SKILL.md, `scripts/google_scraper.py`, `config/segments/accounting.json`, `config/exclusions.txt`, `config/locations/accounting_wave1.txt`) |
| Skill SOP (Notion) | 03 SOPs › `leadgen-google-scraper` v0.2, Approved for this sprint (2 Oct 2026) |
| **Master database** | Drive **ICP_Master** (`1cgunhz43AF45AReQm_IOSpdoI2L7MuTnx95icTH3INk`): Legend, Master (1,219 firms on 2 Oct 2026), Holding (353), Exclusions (381). **Always address it by this file ID**: an older file with the same name exists (`1Kg62MnZBkTpOXQ_JnkSlfjFt11besr1OGEtwGl_1F1k`, 20 Aug) |
| Context: accounting fit, signals, verification | `00_global_context/data_extraction_broad_map.md` (accounting section), `account_scoring_and_enrichment.md` |
| Context: competitors (copy hooks) | `00_global_context/ermos_competitive_analysis.md` |

## 3. Tools Required

| Tool | Role in this SOP | Access / credentials | Stack status |
|---|---|---|---|
| **Apify** (actor `compass/crawler-google-places`) via the `leadgen-google-scraper` skill | Raw Google Maps business listings (name, website, phone, address, category). All paid add-ons off | `APIFY_TOKEN` (env) for the script; or the Apify connector where `api.apify.com` is blocked | **Approved source** (CLAUDE.md sourcing rule) |
| **Google Sheets: ICP_Master** | **Master database** for the cold pipeline: dedupe source, lead store, activation queue, reply status | Google service account in n8n (read/write) | **Infrastructure** |
| **Clay** | Company enrichment, website staff count, ICP check, tiering, decision-maker search (Apollo inside the waterfall), **email and phone waterfall** | Clay workspace; table "ACC Sprint: Accounts" with a webhook source and an HTTP callback to n8n | **Core** (waterfall providers approved) |
| **Apollo** | People provider **inside** Clay's waterfall for the 1–2 decision-maker search | Connected inside Clay | **Core** |
| **Smartlead AI** | Tiered outbound sequences, fed from ICP_Master. CTA is "Reply yes" | API key in n8n | **Core** |
| **n8n** | All orchestration, every ICP_Master write, every Smartlead push | ERMOS n8n instance | **Core** |
| **Google Drive** | `3. DATA / PIPELINE` hand-off folders (`01_raw`, `02_enriched`, `03_ready`, `_processed`) | Service account | **Infrastructure** |
| **Slack** | Batch approval prompts and run summaries | Slack app (same as SOP-5A-01) | **Infrastructure** |
| **HubSpot** | **Not used in this SOP** (data sync rule). Engaged accounts enter it via SOP-5A-01 | n/a | **Core** (not used here) |

## 4. The Absolutes (Non-negotiables)

### Before starting
1. **The skill gate passes:** the Notion SOP `leadgen-google-scraper` Status is `Approved` (v0.2), and the version is passed to the script with `--sop-version`.
2. **Pilot before batch:** done. The Parramatta pilot passed on 2 Oct 2026. Any new segment or source gets its own pilot.
3. **Spend caps are set by Brad:** an Apify cap per wave (US$) and a Clay credit budget per wave. Never raised mid-run.
4. **ICP_Master is the dedupe set:** its Master, Holding and Exclusions tabs (domains + normalised firm names) are loaded before anything reaches Clay. The existing ~700 leads must already be in ICP_Master (Open Items: confirm, or backfill them first).
5. **Smartlead campaigns exist per tier** (`T1`, `T2`, `T3` tokens, Campaign Naming Standard), with "Reply yes" copy, sender identification and an unsubscribe line. They're wired to the SOP-5A-01 reply webhook. Smartlead's global blocklist and "skip leads already in other campaigns" settings are **on**.
6. **Credentials live only in n8n or the environment.** Never in sheets, Clay text columns, CSVs or this repo.

### Before completing (per record)
7. **ICP:** Australian accounting practice, independent (not a franchise, network branch or Big 4 / mid-tier), with **1–50 staff**. Over 50 is `DQ`, not contacted.
8. **The tier comes from a staff count read off the firm's own website** (team or about page, read by Clay's AI column). A vendor-only headcount gives `Unverified`, which is **not activated** (held for review).
9. **Contact quality:** a named decision-maker, with a **validated** email at the firm's domain. No generic inboxes (`info@`, `admin@`, `reception@`) and no free-mail addresses. Hard cap: **T3 = 1, T1 and T2 = up to 2.**
10. **ICP_Master first:** the firm and its decision-makers are written to ICP_Master (with tier, evidence, source and sprint tags) **before** enrolment in Smartlead. Smartlead is fed **only** from ICP_Master rows.
11. **No HubSpot writes:** this SOP never creates or updates HubSpot records.
12. **Batch approval:** every Smartlead push is approved by Brad (one Slack approval per batch, not per record).
13. **Email source is recorded** (`Email source` column: firm website or Clay waterfall provider) for Spam Act inferred-consent hygiene. Every email identifies ERMOS and carries a working unsubscribe.

## 5. Step-by-Step Procedure

### Stage 0: Set-up (once, about half a day)
1. **ICP_Master:** fix the A1 headers on Master and Holding, then add the sprint columns in §6.4 after column X (no existing column renamed). Re-map the Tier column to `T1`/`T2`/`T3`/`DQ`/`Unverified` (TASKS T-005). Confirm the existing ~700 leads are present (Open Items).
2. **Clay:** build the table "ACC Sprint: Accounts" with the columns in Stage 3.
3. **Smartlead:** create three campaigns following the Campaign Naming Standard (`T1`, `T2`, `T3` size tokens, accounting vertical, sprint id) with tier-appropriate "Reply yes" copy. Attach the SOP-5A-01 webhook. Turn on blocklist and cross-campaign duplicate protection.
4. **n8n:** import WF-2B02-A/B/C (§6.1) and attach credentials (Google, Clay webhook, Smartlead, Slack).

### Stage 1: Source (the skill)
1. **Pilot:** done (Parramatta, 2 Oct 2026; see §1).
2. **Wave 1 batch** (after Brad sets the cap):
   ```bash
   cd skills/leadgen-google-scraper
   export APIFY_TOKEN=...            # from the environment / secret store, never typed into chat
   export PIPELINE_RAW_DIR=<local folder synced to Drive 3. DATA/PIPELINE/01_raw>
   python3 scripts/google_scraper.py --segment accounting --mode batch \
     --suburbs-file config/locations/accounting_wave1.txt \
     --max-places-per-search 60 --run-cap-usd <Brad's wave cap> --sop-version v0.2
   ```
   Or use the wrapper `scripts/run_wave.sh` (§6.6), which runs a dry run first and refuses to start without a cap.
3. **Waves 2–3:** more location files, or `ALL,<STATE>` runs, until the funnel maths in §1 is met.

### Stage 2: Dedupe against ICP_Master (n8n WF-2B02-A, automatic on each new file in `01_raw`)
1. Validate the 18-column schema, and dedupe across all sprint files on `domain`, falling back to `place_id`.
2. **Check strictly against ICP_Master** (Master, Holding and Exclusions tabs):
   - match on **domain** first;
   - then on **normalised company name** (lowercase; strip "Pty Ltd", "& Co" and punctuation), to catch firms listed under another domain.
   Any match is suppressed, with the reason (`in_master`, `in_holding`, `in_exclusions`) logged per row.
3. **Review-volume confidence check** (Brad, 4 Oct 2026; `scripts/review_confidence.py`). Each listing's Google rating is weighed against its review count:

   | Band | Rule | Effect on the Clay queue |
   |---|---|---|
   | **Strong** | ≥ 4.5 stars **and** ≥ 50 reviews | Priority 1 |
   | **Moderate** | Everything between the other bands | Priority 2 |
   | **Questionable** | < 10 reviews (even at 5.0 stars), or no reviews at all. Low statistical weight or a dormant listing | Priority 3 (last), flag `L11` |
   | **Poor** | < 3.0 stars with ≥ 10 reviews | **Held** for Brad, no Clay spend, flag `L12` |

   It sets **queue order and caution, never the tier** (tiers come only from staff counts). Under a credit budget, Strong firms are enriched first.
4. Rows without a domain go to `02_enriched/no_domain_<run>.csv`. They're held, not sent to Clay, until Brad decides whether Clay should hunt for their domains (it costs credits).
5. Push the remaining **net-new** rows to the Clay table webhook, **in priority order (1 → 3)**, in chunks (e.g. 100 per minute). Move the source file to `_processed/`.

### Stage 3: Enrich, tier and source contacts (Clay, automatic per row)

| Clay column (in order) | What it does |
|---|---|
| Company enrichment | Firmographics from the domain: name, LinkedIn, vendor headcount, industry, location |
| **Website staff count** (AI column reading the team / about / people page) | Returns `staff_count`, `evidence_url`, `confidence` |
| **ICP check** (AI column) | Accounting practice? Independent (not a franchise or network branch)? Australian? Returns `pass` / `fail` / `unsure` + reason |
| **Tier** (formula) | `staff_count` 1–9 → `T3` · 10–30 → `T1` · 31–50 → `T2` · > 50 → `DQ` · missing or low confidence → `Unverified` |
| **Surgical contact sourcing** (only if ICP = pass and tier ∈ T1/T2/T3) | People search through Clay's waterfall, **Apollo as the people provider**. Decision-maker titles only: Principal, Director, Managing Director, Managing Partner, Partner, Owner, Founder |
| Contacts per company (hard cap) | **T3:** exactly 1 · **T1:** up to 2 · **T2:** up to 2. The search stops once the cap is met |
| **Email waterfall + validation** | Work email via Clay's waterfall, then a validation status. Only `valid` emails proceed |
| **Phone waterfall** | **T1 and T2 decision-makers only** in this sprint (credit control). T3 phones are found on reply (SOP-5A-01) |
| Callback | HTTP column posts the finished row (company + up to 2 decision-makers) to n8n WF-2B02-B |

### Stage 4: Store in ICP_Master (n8n WF-2B02-B, automatic per Clay callback)
1. Validate the row (Absolutes 7–9) → `ready`, `held` or `rejected`.
2. **Write to ICP_Master, by outcome:**
   - **Ready** → append to the **Master** tab (one row per firm, decision-makers in the DM1 / DM2 columns), with `Pipeline status = Ready for Smartlead`.
   - **Held** (Unverified, low confidence, ICP unsure, no valid decision-maker) → append to the **Holding** tab with the hold reason.
   - **Rejected** (DQ over 50, ICP fail, franchise or network) → append to the **Exclusions** tab with the reason, so no future wave pays to enrich it again.
3. Upsert by domain: if the domain already exists in any tab (a race between batches), update instead of appending, and flag it.
4. Write `02_enriched` and `03_ready` CSV snapshots per batch to Drive, for audit.

### Stage 5: Activate from ICP_Master (n8n WF-2B02-C: daily at 09:00 Sydney, or on demand)
1. Read ICP_Master Master rows with `Pipeline status = Ready for Smartlead`, grouped by tier.
2. **Capacity check:** cap the batch to what the 9 warmed mailboxes can carry (Open Items 3).
3. Post a Slack approval card to Brad, showing:
   - count per tier;
   - a sample of 10 rows with firm, suburb, decision-maker title, tier and staff evidence link;
   - held and rejected counts with their top reasons.
4. **On approve:** add each decision-maker to the matching tier campaign in Smartlead, in batches. Custom fields: `first_name`, `firm_name`, `suburb`, `tier`, `staff_count`. Then write back to the ICP_Master row: `Smartlead campaign`, `Smartlead lead id(s)`, `Enrolled at`, `Pipeline status = Enrolled`.
5. **On reject:** nothing is sent. Brad's comment is logged in the batch log.

### After enrolment (handled by SOP-5A-01)
- Every reply outcome is written back to the firm's ICP_Master row (`Reply status`, `Last reply at`).
- Only **confirmed interest** (an Interested reply, a meeting request, or a completed AI health check survey) creates the company and contacts in **HubSpot**. The ICP_Master row is then marked `In HubSpot` with the HubSpot ids.

### Running wave 1 today
1. **Apify access:** `api.apify.com` allowed and `APIFY_TOKEN` set in this environment (Brad's settings change), or run `scripts/run_wave.sh` on Brad's machine.
2. **Cap:** Brad sets the wave 1 Apify cap. The wrapper refuses to run without one.
3. **Run wave 1** → the CSV lands in `01_raw`.
4. **Until n8n is live (manual-assist):**
   - dedupe the CSV against ICP_Master (Claude Code can do this from Drive);
   - import net-new rows into the Clay table and run Stage 3;
   - export Clay results and paste ready / held / rejected rows into the ICP_Master tabs;
   - upload approved decision-makers per tier to Smartlead as CSV.
   No HubSpot step.

## 6. Data Flow & Automation

### 6.1 n8n workflows

**WF-2B02-A "Sprint Intake and Dedupe"**

| # | Node | Purpose |
|---|---|---|
| 1 | Google Drive Trigger (new file in `PIPELINE/01_raw`, name starts `accounting_`) | Start on each scraper output |
| 2 | Drive: download CSV + `.run.json` · Code: schema check | Abort and alert if the 18 columns aren't present |
| 3 | Google Sheets: read **ICP_Master** Master, Holding and Exclusions (domain + firm name columns only) | Build the dedupe set |
| 4 | Code: cross-file dedupe + ICP_Master match (domain, then normalised name) + **review-volume confidence band** (same logic as `scripts/review_confidence.py`) + split (to Clay by priority / no-domain hold / Poor hold / suppressed) | Reasons logged per row |
| 5 | Loop (chunks of 100) → HTTP: Clay table webhook | Rate-limited feed into Clay |
| 6 | Drive: move file to `_processed/` · write `02_enriched/suppressed_<run>.csv` and `no_domain_<run>.csv` | Audit trail |
| 7 | Slack: run summary (rows in, suppressed by tab, held, sent to Clay) | n/a |

**WF-2B02-B "Clay → ICP_Master"**

| # | Node | Purpose |
|---|---|---|
| 1 | Webhook (from the Clay HTTP column; secret path) | One finished company row with up to 2 decision-makers |
| 2 | Code: validate (Absolutes 7–9) → `ready` / `held` / `rejected` | n/a |
| 3 | Google Sheets: lookup domain in ICP_Master (all tabs) | Upsert, not duplicate |
| 4 | Google Sheets: append or update **Master** (ready) / **Holding** (held) / **Exclusions** (rejected) | Master database write |
| 5 | Error branch: Sheets 429 (quota) → wait and retry with backoff; persistent failure → Slack alert with domain | No silent drops |

**WF-2B02-C "ICP_Master → Smartlead Activation"**

| # | Node | Purpose |
|---|---|---|
| 1 | Schedule (09:00 Australia/Sydney) + Manual trigger | n/a |
| 2 | Google Sheets: read Master rows `Pipeline status = Ready for Smartlead` | Activation queue |
| 3 | Code: capacity check (9 mailboxes × daily limit ÷ sequence steps) → trim the batch; split DM1/DM2 into one lead per decision-maker; group by tier | Never over-enrol |
| 4 | Slack: approval card (Send and Wait for Response) | **Human gate** |
| 5 | On approve: Smartlead add leads to the `T1` / `T2` / `T3` campaign (batched) | n/a |
| 6 | Google Sheets: write campaign, lead ids, enrolled time, `Pipeline status = Enrolled` | Status lives in ICP_Master |
| 7 | Slack: confirmation with counts | n/a |

### 6.2 Raw input schema (from the skill)
`segment, search_term, suburb_searched, firm_name, website, domain, phone, address, state, postcode, google_category, rating, reviews_count, place_id, maps_url, scraped_at, source, run_id`. Fixed 18 columns. `state` is normalised to NSW / VIC / QLD / WA / SA / TAS / ACT / NT.

### 6.3 Clay output (callback payload)
**Company:**
- `domain`, `firm_name`, `website`, `address`, `suburb`, `state`, `postcode`, `google_place_id`, `google_category`;
- `vendor_headcount`, `staff_count`, `staff_count_evidence_url`, `staff_count_confidence`, `tier`;
- `icp_pass`, `icp_reason`, `linkedin_company_url`, `run_id`.

**Decision-makers (max 2):**
- `first_name`, `last_name`, `title`, `email`, `email_status`, `email_source`;
- `phone`, `phone_source`, `linkedin_url`.

### 6.4 ICP_Master columns
**Existing Master and Holding columns (24, A–X), used as-is:** Firm name · Domain · Website · Segment(s) · Source segment · City / Region · Staff count · Services · Professional body · Segment signals · M365 or Copilot evidence · **Contact 1 name · Contact 1 title · Contact 1 email · Contact 1 LinkedIn · Contact 2 name · Contact 2 title · Contact 2 email · Contact 2 LinkedIn** · Signals found · Tier · Verification evidence · Notes / exclusion reason · Batch.

**Existing Exclusions columns (6):** Firm name · Domain · Segment · Exclusion reason · Evidence (URL/phrase) · Batch.

**Mapping from Clay:**
- decision-maker 1 → Contact 1 columns; decision-maker 2 → Contact 2 columns;
- `staff_count` → Staff count; `staff_count_evidence_url` → Verification evidence;
- `tier` → Tier (re-mapped to `T1`/`T2`/`T3`/`DQ`/`Unverified`, TASKS T-005);
- `icp_reason` / hold reason → Notes / exclusion reason; `run_id` → Batch;
- Segment(s) = `Accounting`; Source segment = `Accounting`.

**Columns to add after X (Master and Holding):**

| Column | Values / rule |
|---|---|
| `Source` | `google_maps` · `apollo` · `lookalike` · `partner` |
| `Sprint` | e.g. `ACC-2026-10` |
| `Google place id` | Dedupe fallback |
| `Staff count confidence` | 0–1, from Clay |
| `Contact 1 email status` · `Contact 2 email status` | Validation result |
| `Contact 1 phone` · `Contact 2 phone` | T1/T2 only in this sprint |
| `Email source` | Waterfall provider or `firm website` |
| `Pipeline status` | `Ready for Smartlead` · `Enrolled` · `Held` · `Rejected` · `In HubSpot` |
| `Smartlead campaign` · `Smartlead lead id(s)` · `Enrolled at` | Written at activation |
| `Reply status` · `Last reply at` | Written by SOP-5A-01 |
| `HubSpot company id` | Written by SOP-5A-01 when the account becomes engaged |

**Hygiene to fix at set-up:** cell A1 on Master and Holding holds pasted prompt text instead of the "Firm name" header. Some cells contain unquoted commas. n8n must read the sheet by column, never from a text/CSV export.

**Scale note:** Google Sheets holds up to 10 million cells. About 5,000 firm rows × ~45 columns is roughly 225,000 cells, well inside the limit. n8n writes in batches to stay within Sheets API quotas.

### 6.5 Data flow summary

```
leadgen-google-scraper (Apify) ──► Drive PIPELINE/01_raw (CSV + manifest)
   └─► n8n WF-2B02-A: schema check → dedupe vs ICP_Master (Master/Holding/Exclusions) → net-new → Clay
          └─► Clay: enrich → website staff count → ICP check → Tier → 1–2 DMs (Apollo in waterfall) → email + phone waterfall
                 └─► n8n WF-2B02-B: validate → ICP_Master (Master = ready · Holding = held · Exclusions = rejected)
                        └─► n8n WF-2B02-C (daily): Ready rows → capacity check → Slack approval → Smartlead T1/T2/T3
                               └─► replies → SOP-5A-01 → status back to ICP_Master; confirmed interest only → HubSpot
```

**Systems of record:** **ICP_Master** for every cold record. **HubSpot** only from confirmed interest onward. Clay is the enrichment workspace. Drive holds immutable batch files. Smartlead holds sending state only.

### 6.6 Batch runner (`scripts/run_wave.sh`, web-site-builder repo)
A wrapper for the scraper that:
1. refuses to run without `--cap` (Brad's wave cap) and a locations file;
2. checks `APIFY_TOKEN`, `PIPELINE_RAW_DIR` and that `api.apify.com` is reachable;
3. prints a dry run and an estimated maximum place count and cost;
4. asks for a typed `yes` before spending (or `--yes` for unattended runs).

## 7. Quality Assurance (QA) Guidelines

### What "Good" Looks Like

| Metric | Target |
|---|---|
| Net-new rate after dedupe | Reported per wave. Every suppressed row has a tab reason |
| Review confidence | Every row has a band (Strong / Moderate / Questionable / Poor). The band mix is reported per wave; Poor firms never reach Clay |
| Net leads per raw listing | ≥ 0.40 (re-set after wave 1) |
| Tier accuracy | ≥ 90% on a weekly sample of 20 firms, checked by Brad against the evidence URL |
| ICP accuracy | ≥ 95% of enrolled firms are genuine independent AU accounting practices of 1–50 staff (same sample) |
| Contact discipline | 100% of firms have ≤ 2 decision-makers (T3 = 1). 0 non-decision-maker roles enrolled |
| Email quality | 100% of enrolled contacts `valid`. Smartlead bounce rate < 2% per campaign |
| Duplicates | 0 firms enriched twice; 0 contacts enrolled twice |
| ICP_Master-first | 100% of enrolled contacts sit on an ICP_Master Master row with tier, evidence, source and status before the first send |
| CRM hygiene | 0 cold records in HubSpot |
| Sprint progress | Leads Ready + Enrolled tracked weekly against 6,000 (from the ICP_Master Pipeline status column) |

### What "Bad" Looks Like
- Treating a 5.0-star listing with 1 review as strong social proof, or spending Clay credits on Questionable firms before Strong ones.
- Paying Clay to enrich a firm already in ICP_Master, including one previously rejected in Exclusions.
- Bookkeepers, tax-return franchises, financial planners or software vendors tagged as accounting practices.
- Tiers from vendor headcount instead of the firm's own team page.
- Three or more contacts scraped per firm, or `info@` / receptionist addresses enrolled.
- Cold contacts created in HubSpot "just in case".
- Leads in Smartlead with no ICP_Master row, or an ICP_Master row whose status says `Ready` after it was enrolled.
- Enrolling more than the 9 mailboxes can send, so sequences stall and domains burn.

## 8. Exception Handling

### Auto-Pass Criteria
A firm's decision-makers go to `Ready for Smartlead` with no human review (beyond Brad's batch approval) when **all** of these hold:
1. `icp_pass = true`, a tier of T1/T2/T3, and `staff_count_confidence` ≥ 0.8 with an evidence URL;
2. each decision-maker has a `valid` email at the firm's domain, and it isn't a generic or free-mail address;
3. the domain and normalised name aren't already in ICP_Master (any tab);
4. the firm is in Australia.

### Flagging Triggers
These go to the **Holding** tab with a reason. Brad reviews Holding twice a week.

| Code | Trigger | Handling |
|---|---|---|
| `L01_unverified_size` | No website staff count, or confidence < 0.8 | Manual count from the team page, or leave held |
| `L02_boundary_size` | Staff count of 9–11 or 29–31 (tier boundary) | Confirm the count. The tier decides the campaign |
| `L03_icp_unsure` | ICP check returned `unsure` (e.g. bookkeeper, accountant + financial planner) | Decide: in, out, or another vertical (finance) |
| `L04_network_or_virtual` | Network or franchise member not on the exclusion list, or a virtual-office address shared with another firm | Add to exclusions if it's a pattern |
| `L05_no_dm` | ICP pass but no decision-maker with a valid email | Leave held. Optional manual LinkedIn find |
| `L06_catch_all` | Email is catch-all, or only risky validation is available | Hold. Don't enrol in this sprint |
| `L07_name_match` | Domain is new but the normalised name matches an ICP_Master row | Brad confirms: same firm (merge) or different (proceed) |
| `L08_no_domain` | The listing has no website | Held file. Brad decides whether Clay should hunt for a domain |
| `L09_cap_reached` | Apify or Clay wave budget reached | Stop and report. Never raise the cap without Brad's number |
| `L10_capacity` | Ready contacts exceed sending capacity | Trim the batch; the rest wait for the next day |
| `L11_low_review_signal` | Fewer than 10 Google reviews (or none), whatever the star rating | Enriched last. Brad sees the flag in the batch approval sample. Not excluded on this alone |
| `L12_poor_reputation` | Under 3.0 stars with 10+ reviews | Held before Clay (no credits spent). Brad decides whether it's still worth contacting |

---

## Open Items

1. **"Lead" definition:** confirm 6,000 counts decision-maker contacts (assumed), not firms.
2. **Wave 1 caps:** the Apify cap (estimate US$22–58 for up to ~14,400 places at US$1.50–4 per 1,000) and the Clay credit budget per wave.
3. **Sending capacity, 9 warmed mailboxes (confirmed):** at 30–50 emails per mailbox per day, that's 270–450 sends a day. With a 3-step sequence, about 90–150 new contacts can start each day, so 5,300 new contacts take roughly **35–60 sending days**. Confirm the per-mailbox daily limit set in Smartlead. WF-2B02-C enforces it.
4. **Existing ~700 leads in ICP_Master:** ICP_Master holds 1,219 firms on Master. Confirm every firm already contacted (Hit List MASTER, Smartlead Master List, Extraction Register) is among them. If any aren't, backfill them once so dedupe catches them.
5. **ICP_Master column names:** confirm the added sprint columns (§6.4) before n8n is built. Existing headers aren't renamed, and Contact 1/2 are reused for the two decision-makers.
6. **Phone scope:** confirm phones for T1/T2 decision-makers only in this sprint (T3 on reply).
7. **Geography:** wave 1 is metro-only. Confirm whether regional areas (and Tasmania / NT) are in for waves 2–3.
8. **Bookkeepers and tax agents:** in or out of the accounting ICP? The pilot held two bookkeepers (`L03`).
9. **Apify access:** pending Brad's environment change (`api.apify.com` allowed + `APIFY_TOKEN` environment variable).
10. **Workflows.io:** the TAM Mapping Playbook page itself, to validate §6 node by node.

## Change Log

| Version | Date | Author | Change |
|---|---|---|---|
| v0.4 | 4 Oct 2026 | Claude Code for Brad | Review-volume confidence check (Strong / Moderate / Questionable / Poor) added to Stage 2; sets Clay queue order; Poor held before Clay; flags L11 and L12 |
| v0.3 | 2 Oct 2026 | Claude Code for Brad | **Data sync rule:** ICP_Master is the master database for the cold pipeline; HubSpot is bypassed (engaged accounts only, via SOP-5A-01). Dedupe strictly against ICP_Master; outcomes written to its Master / Holding / Exclusions tabs; Smartlead fed from ICP_Master. Pilot results recorded; batch runner added |
| v0.2 | 2 Oct 2026 | Claude Code for Brad | Cost-first architecture from the Workflows.io TAM Mapping Playbook; contacts capped at 1–2 decision-makers via Apollo inside Clay's waterfall; 9-mailbox capacity maths |
| v0.1 | 2 Oct 2026 | Claude Code for Brad | First draft |
