# SOP-2B-01: Generating Lookalike Audiences

| Field | Value |
|---|---|
| SOP ID | SOP-2B-01 |
| Phase | Phase 2: Broad TAM Mapping |
| Component | Component 2B: Find Lookalikes |
| Version | v0.1 |
| Status | **Draft for Brad's review** |
| Owner | Brad (Head of Sales & Operations) |
| Last updated | 2 Oct 2026 |
| Depends on | SOP-1B-01 Building the ICP Model *(planned)*. Until it exists, seed sets come from the interim rule in step 1. |
| Feeds | SOP-3A-01 Account Verification and Research *(planned)* → SOP-3B-01 Size-Based Tiering *(planned)* |

---

## 1. Overview & Context

**What this SOP achieves.** It takes a small, verified set of "best-fit" ERMOS accounts (the seeds), runs them through lookalike engines (Discolike, Ocean.io, AI Ark), and produces a **deduplicated, Australian, single-vertical list of candidate firms** that look like those seeds. It finds firms that firmographic filters miss, especially small professional-services practices with thin or wrong database records.

**Where it sits in the Phase.** Phase 2 (Broad TAM Mapping) has two Components that run side by side:
- **2A Firmographic Fits** pulls firms that match the ICP's hard filters (industry, location, size).
- **2B Find Lookalikes** (this SOP) pulls firms that *resemble our best accounts*, including ones whose database labels are wrong.

Both feed **Phase 3** (Account Research → Scoring → Enriched TAL). This SOP creates **candidates only**. It does not verify, tier, enrich contacts or contact anyone.

**Final Output alignment.** This SOP feeds the first term of the Final Output equation, **Accounts Mapped**. Company Tiers, Stakeholder Maps, Signals and Awareness Scores are added downstream.

**Scope.**
- In scope: end-customer firms in the five approved verticals (accounting, law, aged care, healthcare, finance), Australia only, 1–50 staff target. Healthcare and law are the current priority verticals.
- Out of scope: partner and integrator recruitment lists (separate Partner ICP), contact or people lookalikes (Phase 4B), any CRM write (Phase 4C).

## 2. Visuals & References

| Reference | Location |
|---|---|
| Playbook blueprint | `00_global_context/GTM_Playbook_2026.pdf`, the "Broad TAM Map → Find Lookalikes" box (Discolike, Ocean.io, AI Ark) |
| Hierarchy map | `00_global_context/gtm_playbook_2026_flow.md`, Phase 2 / Component 2B |
| Figma: Phase 2 overview | `[FIGMA PLACEHOLDER: Phase 2 Broad TAM Mapping frame, link TBD]` |
| Figma: 2B workflow diagram | `[FIGMA PLACEHOLDER: SOP-2B-01 n8n flow diagram, link TBD]` |
| Context: fit criteria, sources, pipeline folders | `00_global_context/data_extraction_broad_map.md` |
| Context: tiers, signals, verification rules | `00_global_context/account_scoring_and_enrichment.md` |
| Context: competitor technographics (seed/negative signals) | `00_global_context/ermos_competitive_analysis.md` |
| Context: partner and integrator routing | `00_global_context/meeting_ermos_comarket.md` |
| Vendor docs | Discolike: https://api.discolike.com/v1/docs/ · Ocean.io: https://app.ocean.io/docs · AI Ark: https://docs.ai-ark.com/ |

## 3. Tools Required

All three lookalike engines are **candidates under test** (R-02OCT: no tool is locked in). Steps 4–6 below are the test that decides which ones are kept.

| Tool | Role in this SOP | Known capability (vendor docs, checked 2 Oct 2026) | Access / credentials | Status |
|---|---|---|---|---|
| **Discolike** | Lookalike engine A | Lookalike search from up to 10 seed domains, plus up to 10 "exclude-lookalikes-of" domains. Also takes natural-language ICP queries. Covers 70M+ domains in 180+ countries, built from website content. REST API, Python SDK, CLI. | API key in the n8n credential store | Candidate |
| **Ocean.io** | Lookalike engine B | Lookalike companies from up to 10 seed domains. Minimum similarity score (default 0.79). Filters: primary country (HQ), size, industry, technographics, keywords, domains to exclude. REST API; Clay integration. | API key in the n8n credential store | Candidate |
| **AI Ark** | Lookalike engine C | "AI Lookalike" company search inside Company Search. REST (JSON, `X-TOKEN` header). Also has a hosted MCP server and Clay templates. | API key in the n8n credential store | Candidate |
| **n8n** | Orchestration: read seeds, call engines, normalise, dedupe, write files, notify | n/a | ERMOS n8n instance (hosting TBD) | Required |
| **Google Sheets: ICP_Master** | Seed source; dedupe against Master, Holding and Exclusions | Drive `1cgunhz43AF45AReQm_IOSpdoI2L7MuTnx95icTH3INk` | Google service account (read; write only to the new tabs below) | Required |
| **Google Sheets: Smartlead Extraction Register** | Dedupe against firms already extracted for outreach | Drive `1gmwkEl4Wa9udutJQoLfsLseOFeKLj3g783jT4aPQdJI` | Read | Required |
| **Google Drive: `3. DATA / PIPELINE / 01_raw`** | Output hand-off folder for Phase 3 | Drive folder `1nIpskjvSHuK3dCXXubP9h_SeTXXn4bTe` (PIPELINE) | Write | Required |
| **Slack** | Run summaries, flags and approval prompts | Channel TBD (e.g. `#gtm-pipeline`) | n8n Slack credential | Required |
| **Claude (this repo)** | Seed-set QA, sample review support, run reports | n/a | n/a | Optional |

## 4. The Absolutes (Non-negotiables)

### Before starting
1. **Approved seed set.** The seed set is in the `Lookalike_Seeds` register with Status `Approved` by Brad.
2. **One vertical per seed set.** Never mix verticals; a mixed set produces a blurred "average" firm.
3. **Seeds are verified.** Every seed domain has been confirmed on the firm's own website as an Australian, independent firm in the stated vertical, with 1–50 staff (ICP_Master verification rule). No seed is accepted because a vendor database says so.
4. **Seed count is 3 to 10.** Under 3 is too thin to generalise. 10 is the cap for both Discolike and Ocean.io.
5. **Run caps set.** The run has a maximum result count per tool and a dollar spend cap in A$ (set by Brad, see Open Items). Pilot mode: 50 results per tool. Never raise a cap mid-run.
6. **Credentials stay in n8n.** API keys live only in the n8n credential store. Never in sheets, CSVs, run logs, prompts or this repo.
7. **Pilot before batch.** A new seed set, vertical or tool always runs in `pilot` mode first. `batch` mode needs Brad's approval of the pilot.

### Before completing
8. **Australia only.** Every passed row has an Australian HQ (primary country = AU, or a `.au` domain plus an Australian address).
9. **Deduplicated on domain** within the run, against all three engines, ICP_Master (Master, Holding and Exclusions tabs) and the Smartlead Extraction Register.
10. **No people data.** Company-level fields only. No names, emails or phone numbers are pulled or stored by this SOP.
11. **Nothing leaves the pipeline.** Output goes only to `PIPELINE/01_raw` and the run log. No CRM write, no sequence enrolment, no outreach.
12. **Run is logged.** One CSV plus one `.run.json` manifest per run, and one row in `Lookalike_Run_Log`. Never overwrite an earlier run's files.
13. **No tier is assigned.** Tiers come only from verified staff counts in SOP-3B-01. Vendor headcount is a pre-filter, never a tier.

## 5. Step-by-Step Procedure

### Step 1: Build the seed set (manual, Brad, about 30 minutes per vertical)
1. Open ICP_Master and filter to one vertical.
2. Choose 3–10 seeds using this **interim rule**, which applies until SOP-1B-01 defines the ICP model:
   - first, any **closed-won or beta customer** in that vertical (e.g. the law and accounting beta firms);
   - then the strongest **verified** firms in the vertical, preferring Tier 1 size (10–30 staff) and firms with the strongest signals (e.g. a data-sovereignty stance, document-heavy practice, named practice-management software).
3. Choose 0–10 **negative seeds** (firms the engines should steer away from). Examples: large or national firms, franchise networks, firms already lost, look-alike-but-wrong types (e.g. barristers' chambers for law, retail pharmacy for healthcare).
4. Add a row to the `Lookalike_Seeds` tab (schema in section 6.3). Status `Proposed`.
5. Brad reviews it and sets Status to `Approved`.

### Step 2: Configure the run (manual, about 5 minutes)
In the `Lookalike_Run_Config` row for this run, set:
- `seed_set_id`, `mode` (`pilot` or `batch`), `tools` (any of `discolike`, `ocean`, `aiark`);
- `max_results_per_tool` (pilot 50; batch per Brad);
- `spend_cap_aud` (per Brad);
- `ocean_min_similarity` (start at the vendor default, 0.79);
- the filters below.

**Filters, applied in each engine where supported:**

| Filter | Value | Discolike | Ocean.io | AI Ark |
|---|---|---|---|---|
| Country | Australia | Country filter | Primary country = AU | Location filter |
| Size | ≤ 50 staff (use the smallest vendor bands, e.g. 1–10 and 11–50) | Where supported | Company size | Headcount filter |
| Exclude domains | Negative seeds + known customers + partners | Exclude-lookalikes-of (≤10) | Domains to exclude | Exclusion list where supported |
| Industry | Leave **off** at first: lookalikes should find firms that industry codes mislabel. Turn on only if precision is poor. | n/a | Industry categories | Industry filter |

*The exact parameter names must be confirmed against each vendor's API reference during the pilot build. Record them in the n8n workflow notes.*

### Step 3: Run the n8n workflow `2B-01 Lookalike Generator`
Trigger it manually or through the n8n form trigger with `run_config_id`. The workflow (section 6.1) reads the seeds, calls each selected engine, normalises the results, dedupes them, applies the auto-pass and flag rules, writes the files, logs the run and posts to Slack.

### Step 4: Review the pilot sample (manual, Brad or delegate, about 45 minutes)
1. Open the run CSV in `01_raw`.
2. Each tool's pilot is reviewed on a random sample of **30 passed rows** (or all rows, if fewer).
3. For each sampled row, open the firm's website and mark `review_result`:
   - `fit`: AU, independent, right vertical, plausibly 1–50 staff;
   - `wrong_vertical`;
   - `too_large`;
   - `not_au`;
   - `not_a_firm` (directory, association, software vendor, etc.);
   - `dead_site`.
4. The workflow's review form writes the results back to the run log.

### Step 5: Score the tools (automatic, from the review)
For each tool, the run log calculates:
- **Precision** = `fit` ÷ sampled.
- **Unique yield** = passed rows not found by any other tool and not already in ICP_Master.
- **Cost per fit** = run cost ÷ (passed rows × precision).
- **Overlap** with the other tools.

### Step 6: Decide and record (Brad)
1. **Keep** a tool for this vertical if its precision is at or above the threshold and its cost per fit is acceptable. Thresholds are proposed in section 7 and set by Brad.
2. **Drop or retune** a tool otherwise: adjust the similarity threshold, the negative seeds, or turn on the industry filter, then re-pilot.
3. Record the decision in Notion 05 Decisions Log and set the tool's Status in section 3 to `selected` or `dropped` for that vertical.

### Step 7: Batch run (after approval)
1. Set `mode = batch` with the approved tools and caps.
2. Run the workflow.
3. Batch output follows the same review rule: a 10% random sample (minimum 20 rows) is spot-checked before hand-off.

### Step 8: Hand off to Phase 3
1. Set the run's `handoff_status` to `ready_for_3A`.
2. SOP-3A-01 picks up passed rows from `01_raw`. That is where verification, staff counts and tiering happen.
3. Flagged rows stay in `01_raw` until they are resolved (section 8).

## 6. Data Flow & Automation

### 6.1 n8n workflow: `2B-01 Lookalike Generator`

| # | Node | Purpose | Notes |
|---|---|---|---|
| 1 | **Form Trigger / Manual Trigger** | Start a run with `run_config_id` | No schedule. Runs are deliberate. |
| 2 | **Google Sheets: Read** `Lookalike_Run_Config` and `Lookalike_Seeds` | Load config and seeds | Abort if seed set Status ≠ `Approved` |
| 3 | **IF: Validate** | Check Absolutes 1–7: 3–10 seeds, one vertical, caps present, mode valid, pilot passed before batch | On fail: Slack alert, stop |
| 4 | **Switch: per tool** | Branch to each selected engine | Branches run in parallel |
| 5a–c | **HTTP Request: Discolike / Ocean.io / AI Ark** | Lookalike call with seeds, negative seeds and filters | Header-auth credential per vendor; pagination loop until `max_results_per_tool`; retry 3× with backoff on 429/5xx |
| 6 | **Code: Normalise** | Map each vendor response to the common schema (6.2) | Normalise domains: lowercase, strip protocol, `www.` and path. Keep raw vendor fields in `vendor_raw` (JSON) |
| 7 | **Merge + Code: Dedupe within run** | One row per domain | Keep highest `similarity_score`; `found_by` lists every tool that returned it |
| 8 | **Google Sheets: Read** ICP_Master (Master, Holding, Exclusions) + Smartlead Extraction Register | Build the "already known" domain set | Read-only |
| 9 | **Code: Classify** | Set `dedupe_status` and apply the auto-pass and flag rules (section 8) | Sets `pass_status` = `auto_pass` / `flagged` / `excluded` |
| 10 | **Code: Cost check** | Sum the reported or estimated cost per tool vs `spend_cap_aud` | If the cap is hit mid-run, stop further calls, mark the run `capped`, keep what was retrieved |
| 11 | **Google Drive: Upload** | Write `lookalike_<vertical>_<seed_set_id>_<YYYY-MM-DD>_<HHMM>.csv` and a matching `.run.json` to `PIPELINE/01_raw` | Never overwrite: the filename includes a timestamp |
| 12 | **Google Sheets: Append** `Lookalike_Run_Log` | One row per run per tool | Counts, cost, file link |
| 13 | **Slack: Post** | Summary: rows per tool, auto-pass / flagged / excluded counts, cost vs cap, link to the file and the review form | Pilot runs include the "Start review" link |
| 14 | **Wait (form / Slack approval)** | Pilot only: hold `handoff_status` until review is complete and Brad approves | Batch runs skip to `ready_for_3A` after the spot check |
| E | **Error Workflow** | Any node failure → Slack alert with run id and node; run marked `failed`; no partial file is handed off | Shared n8n error workflow |

### 6.2 Output schema: run CSV (one row per candidate firm)

| Field | Type | Description |
|---|---|---|
| `run_id` | string | `2B01-<YYYYMMDD>-<HHMM>-<seed_set_id>` |
| `seed_set_id` | string | From `Lookalike_Seeds` |
| `vertical` | enum | `accounting` · `law` · `aged care` · `healthcare` · `finance` |
| `domain` | string | Normalised. **Dedupe key** across the whole pipeline |
| `company_name` | string | As returned by the vendor |
| `website` | url | `https://` + domain unless the vendor gives a fuller URL |
| `country` | string | Vendor HQ country |
| `state` | string | AU state if available |
| `city` | string | If available |
| `vendor_headcount` | integer/blank | Vendor figure. **Pre-filter only**, never a tier |
| `vendor_headcount_band` | string | e.g. `1-10`, `11-50` |
| `vendor_industry` | string | Vendor label |
| `similarity_score` | number | Best score across tools (each vendor's own scale, recorded as given) |
| `found_by` | list | `discolike;ocean;aiark` |
| `found_by_count` | integer | 1–3. Higher means stronger agreement |
| `linkedin_company_url` | url/blank | If returned |
| `dedupe_status` | enum | `new` · `in_icp_master` · `in_holding` · `in_exclusions` · `in_smartlead_register` |
| `pass_status` | enum | `auto_pass` · `flagged` · `excluded` |
| `flag_reasons` | list | Codes from section 8 |
| `review_result` | enum/blank | Filled during the pilot sample (step 4) |
| `retrieved_at` | datetime | ISO 8601, Sydney time |
| `vendor_raw` | json | Raw vendor fields, for audit |

The `.run.json` manifest holds: run config, seed and negative-seed domains, per-tool request parameters (no keys), row counts by status, reported cost per tool, `capped` flag, workflow version and SOP version (`SOP-2B-01 v0.1`).

### 6.3 New Google Sheets tabs (in ICP_Master)

| Tab | Key fields |
|---|---|
| `Lookalike_Seeds` | `seed_set_id`, `vertical`, `seed_domains` (3–10), `negative_domains` (0–10), `seed_rationale`, `proposed_by`, `status` (`Proposed` / `Approved` / `Retired`), `approved_by`, `approved_at` |
| `Lookalike_Run_Config` | `run_config_id`, `seed_set_id`, `mode`, `tools`, `max_results_per_tool`, `spend_cap_aud`, `ocean_min_similarity`, `filters_json` |
| `Lookalike_Run_Log` | `run_id`, `tool`, `rows_returned`, `auto_pass`, `flagged`, `excluded`, `cost_aud`, `capped`, `sample_size`, `precision`, `unique_yield`, `cost_per_fit`, `file_link`, `handoff_status` |

### 6.4 Data flow summary

```
Lookalike_Seeds (Approved) ──► n8n 2B-01 ──► Discolike / Ocean.io / AI Ark APIs
                                   │
                                   ├─ normalise + dedupe ◄── ICP_Master (Master/Holding/Exclusions) + Smartlead Register  [read-only]
                                   │
                                   ├─► PIPELINE/01_raw: run CSV + .run.json      ──► SOP-3A-01 (verification, staff count)
                                   ├─► ICP_Master: Lookalike_Run_Log            (system of record for runs and tool scores)
                                   └─► Slack: run summary, flags, approval prompt
```

**System of record:** ICP_Master stays the record for firms. This SOP never writes to the Master tab. Firms enter Master only after Phase 3 verification. The CRM is not touched until Phase 4C.

## 7. Quality Assurance (QA) Guidelines

### What "Good" Looks Like

| Metric | Proposed starting target (Brad to set) | Measured in |
|---|---|---|
| Pilot precision (sample review) | ≥ 60% `fit` per tool per vertical | `Lookalike_Run_Log` |
| AU rate among passed rows | 100% (enforced by rules) | Run CSV |
| Unique yield | ≥ 30% of passed rows are new to ICP_Master | `Lookalike_Run_Log` |
| Multi-tool agreement | Rows found by 2+ tools convert to `fit` at a visibly higher rate than single-tool rows | Pilot review |
| Duplicates in hand-off | 0 domains duplicated against the pipeline | Run CSV |
| Run hygiene | Every run has a CSV, a manifest, a log row and a Slack post. No keys anywhere | Run audit |

**A good run reads like this:** "Law seed set L-01 (8 seeds, 4 negatives). Ocean.io and Discolike returned 50 each. 71 unique, 52 auto-pass, 11 flagged, 8 excluded. Pilot precision 68% (Ocean) and 63% (Discolike). 24 of the passed rows are new to ICP_Master. A$X spent of a A$Y cap."

### What "Bad" Looks Like
- **Mixed or unverified seeds:** an accounting firm in a law seed set, or a seed with 120 staff. The output drifts to the wrong vertical or size.
- **Generic seeds:** using big-brand firms as seeds, which pulls in mid-tier and national firms (all disqualified over 50).
- **Treating vendor headcount as truth:** tiering, or excluding a firm with blank headcount, from vendor data. Small AU firms are often missing or wrong in vendor databases.
- **Industry filter on too early,** which hides the mislabelled firms this Component exists to find.
- **Directory and aggregator pollution:** law-firm directories, health booking platforms, accounting associations and software vendors appearing as "firms".
- **Partner contamination:** IT MSPs and integrators in an end-customer list. They belong to the Partner ICP.
- **Silent overwrites or untraceable rows:** no `run_id`, no manifest, files overwritten.
- **Spend creep:** raising caps mid-run, or running batch without a reviewed pilot.

## 8. Exception Handling

### Auto-Pass Criteria
A row is set to `auto_pass` (handed to SOP-3A-01 for verification, with no human touch in this SOP) only when **all** of these hold:
1. `dedupe_status = new`;
2. Australian HQ (country = AU, or a `.au` domain with an AU address);
3. `vendor_headcount` ≤ 50, **or blank** (blank is normal for small firms, and 3A verifies it);
4. a domain is present and resolves (HTTP 200, or a redirect to the same registrable domain);
5. no flag trigger below fires.

Rows matching an **exclusion rule** are set to `excluded`, with no review needed:
- `vendor_headcount` > 50 → `excluded:too_large`, logged but not handed off;
- domain already in ICP_Master Exclusions → `excluded:known_exclusion`;
- domain in ICP_Master Master/Holding or the Smartlead register → `excluded:already_known` (logged for unique-yield maths).

### Flagging Triggers
These set `flagged`. Flagged rows stay in `01_raw` until reviewed in the run's review form. The reviewer is Brad or a delegate; reviews are due within 2 business days of the run.

| Code | Trigger | Why it needs a human |
|---|---|---|
| `F01_not_au_or_unclear` | Country missing or conflicting (e.g. `.com` domain, no AU address) | Could be an AU firm on a global domain |
| `F02_dead_site` | Domain doesn't resolve, or redirects to a different registrable domain | Possible merger or rebrand; could be a duplicate under another domain |
| `F03_aggregator` | Name or domain matches directory, association, marketplace or booking-platform patterns | Not a firm; but check it isn't a real firm with an odd name |
| `F04_partner_type` | Vendor industry is IT services, MSP, cloud or software | Route to the Partner ICP list, not end-customer |
| `F05_franchise_or_network` | Name suggests a branch of a national network or franchise | Purchasing may sit elsewhere (disqualifier) |
| `F06_low_similarity` | Similarity score in the bottom 20% of the run, or below `ocean_min_similarity` + 0.03 | Borderline match |
| `F07_vertical_drift` | Vendor industry outside the seed set's vertical | Possible mislabel (keep) or wrong type (drop) |
| `F08_negative_seed_neighbour` | Firm closely matches a negative seed | The engine may be ignoring the exclusion |
| `F09_run_anomaly` | Run-level: >40% of a tool's rows excluded or flagged, >50% non-AU, or the run hit its spend cap | Seed set or filters need retuning before more spend |

**Run-level escalation:** if `F09` fires, n8n posts to Slack and **blocks batch mode** for that seed set and tool until Brad clears it.

---

## Open Items

1. **Spend caps:** the A$ cap per run, per tool, for pilot and batch. Vendor cost models (credits per result) need confirming during the pilot build.
2. **Precision and yield thresholds:** confirm or replace the proposed starting targets in section 7.
3. **Vendor accounts:** confirm which of Discolike, Ocean.io and AI Ark ERMOS will open trial or API accounts with, and who holds the credentials.
4. **n8n hosting and Slack channel:** where n8n runs (cloud or self-hosted), and the channel name for run alerts.
5. **Seed approval:** confirm the beta customers can be used as seeds. This is internal use only; no customer data leaves ERMOS beyond the domain sent to the vendor API.
6. **Vendor data handling:** confirm each vendor's terms allow storing returned company data in ICP_Master, and note each vendor's data location (seed domains are sent offshore to these APIs; company domains only, no client data).
7. **Figma links:** add once the Phase 2 frames exist.
8. **Dependency:** SOP-1B-01 (ICP Model) will replace the interim seed rule in step 1.

## Change Log

| Version | Date | Author | Change |
|---|---|---|---|
| v0.1 | 2 Oct 2026 | Claude Code for Brad | First draft, built to the CLAUDE.md SOP Template |
