# SOP-2B-02: Accounting Lead Generation & Enrichment Pipeline

| Field | Value |
|---|---|
| SOP ID | SOP-2B-02 |
| Phase | Phase 2: Broad TAM Mapping (sprint pipeline running through Phases 3, 4 and 8) |
| Component | Sourcing for Phase 2 (Google Maps listings; the firmographic-fit side of the map, 2A, is used here under the 2B sprint ID Brad assigned). Also executes **3A/3B** (verify and tier), **4B** (contact sourcing), **4C** (CRM upload) and **8A** (Automated Outbound, 1:1) |
| Version | v0.1 |
| Status | **Draft for Brad's review**: built to run the first batch today |
| Owner | Brad (Head of Sales & Operations) |
| Last updated | 2 Oct 2026 |
| Depends on | `leadgen-google-scraper` skill (web-site-builder repo) and its Notion SOP v0.2 · HubSpot properties from SOP-1A-01 §6.3 · Smartlead campaigns named per the Campaign Naming Standard (`T1` / `T2` / `T3`) |
| Feeds | SOP-5A-01 Automated Outbound Reply Management (replies from these campaigns) · SOP-1A-01 (deal outcomes) |

---

## 1. Overview & Context

**What this SOP achieves.** It grows the ERMOS accounting outbound list from **about 700 leads to 6,000**. It does this with one repeatable pipeline: **Google Maps (Apify) → Clay (enrich and tier) → HubSpot (system of record) → Smartlead (sequence)**, with **n8n** connecting the steps. Every firm that reaches Smartlead is:
- an Australian accounting practice with 1–50 staff;
- tiered by size: **T3** 1–9, **T1** 10–30, **T2** 31–50;
- recorded in HubSpot before any email is sent;
- represented by a named decision-maker with a validated email.

**How it aligns with the playbook.** This is a sprint pipeline that runs straight through the blueprint:
- **Broad TAM Map** (sourcing);
- **Account Research** and **Account Scoring** (Clay, Tiers 1–3);
- **Enriched TAL**;
- **Contact Sourcing** (the buying committee);
- **CRM Upload**;
- **Demand Generation 1:1, Automated Outbound** (Smartlead).

**Final Output alignment.** Each firm processed adds to **Accounts Mapped**, **Company Tiers** and **Stakeholder Maps**. Smartlead activity then generates the **Signals** and **Awareness Scores** handled in SOP-5A-01.

**What "lead" means here.** A **lead** is one decision-maker contact, at an in-ICP firm, ready to enrol in Smartlead. The 6,000 target counts contacts, not firms (Open Items: confirm).

### Sprint maths (planning ratios; replaced by pilot actuals)

| Step | Assumed pass rate | Basis |
|---|---|---|
| Raw Google Maps listing → kept by the scraper (exclusions, dedupe) | 80% | Exclusion list + domain dedupe |
| → has a website / domain | 85% | Accounting practices are usually listed with a website |
| → passes ICP in Clay (accounting practice, AU, 1–50 staff, not already known) | 70% | Bookkeepers, franchises, over-50 firms and existing leads removed |
| → at least one decision-maker with a validated email | 70% | Clay people search + email waterfall |
| Decision-makers activated per firm | ~1.2 | T3 = 1; T1 and T2 = 1–2 decision-makers (e.g. two partners) |
| **Net leads per raw listing** | **≈ 0.40** | 0.8 × 0.85 × 0.7 × 0.7 × 1.2 |

Needed: 6,000 − 700 = **5,300 net new leads ÷ 0.40 ≈ 13,000 raw listings**. Wave 1 (48 high-density locations) is expected to produce roughly 4,000–6,000 unique listings. Waves 2–3 (more suburbs, or state-wide `ALL,<STATE>` runs) close the gap. Every ratio is re-set from the pilot and wave 1 actuals.

## 2. Visuals & References

| Reference | Location |
|---|---|
| Playbook blueprint | `00_global_context/GTM_Playbook_2026.pdf`: Broad TAM Map → Account Research → Account Scoring (Tiers) → Enriched TAL → Contact Sourcing → CRM Upload → Demand Generation (Automated Outbound) |
| Hierarchy map | `00_global_context/gtm_playbook_2026_flow.md`, Phases 2–4 and 8 |
| Figma | `[FIGMA PLACEHOLDER: SOP-2B-02 sprint pipeline, link TBD]` |
| Workflows.io technical reference | Not supplied for this SOP. The automation design follows the same plumbing pattern as SOP-5A-01's validated blueprint (webhook → n8n → Clay → HubSpot → Smartlead). Marked **not yet validated against Workflows.io** |
| Source skill | `web-site-builder` repo, `skills/leadgen-google-scraper/` (SKILL.md, `scripts/google_scraper.py`, `config/segments/accounting.json`, `config/exclusions.txt`, `config/locations/accounting_wave1.txt`) |
| Skill SOP (Notion) | 03 SOPs › `leadgen-google-scraper` v0.2, Approved for this sprint (2 Oct 2026) |
| Context: accounting fit, signals, verification | `00_global_context/data_extraction_broad_map.md` (accounting section), `account_scoring_and_enrichment.md` |
| Context: competitors (copy hooks) | `00_global_context/ermos_competitive_analysis.md` |
| Existing lead stores (suppression) | Drive "ERMOS Accounting Hit List — MASTER", "Smartlead Master List for Accounting", "Smartlead Extraction Register - Accounting", ICP_Master |

## 3. Tools Required

| Tool | Role in this SOP | Access / credentials | Stack status |
|---|---|---|---|
| **Apify** (actor `compass/crawler-google-places`) via the `leadgen-google-scraper` skill | Raw Google Maps business listings (name, website, phone, address, category). All paid add-ons off | `APIFY_TOKEN` (env) for the script; or the Apify connector where `api.apify.com` is blocked | **Approved source** (CLAUDE.md sourcing rule) |
| **Clay** | Company enrichment, website staff count, ICP check, tiering, decision-maker search, **email and phone waterfall** | Clay workspace; table "ACC Sprint: Accounts" with a webhook source and an HTTP callback to n8n | **Core** (waterfall providers approved) |
| **Apollo** | Company-level sourcing supplement (Phase 2 lookups by domain when Clay's company match is thin). Not used for contacts or phones | API key in n8n | **Core** |
| **HubSpot** | System of record for companies, contacts, tiers, sources and enrolment status | Private app token (CRM read/write) in n8n | **Core** |
| **Smartlead AI** | Tiered outbound sequences. CTA is "Reply yes" | API key in n8n | **Core** |
| **n8n** | All orchestration and every CRM / Smartlead injection | ERMOS n8n instance | **Core** |
| **Google Drive** | `3. DATA / PIPELINE` hand-off folders (`01_raw`, `02_enriched`, `03_ready`, `_processed`) | Service account | **Infrastructure** |
| **Slack** | Batch approval prompts and run summaries | Slack app (same as SOP-5A-01) | **Infrastructure** |
| **Claude API** | Optional, only if a Clay AI column isn't used: classify the "is this an independent accounting practice?" check from website text | Key in n8n | **Infrastructure** |

## 4. The Absolutes (Non-negotiables)

### Before starting
1. **The skill gate passes:** the Notion SOP `leadgen-google-scraper` Status is `Approved` (v0.2), and the version is passed to the script with `--sop-version`.
2. **Pilot before batch:** 1 term × 1 suburb × 20 places, cap US$1. A batch starts only after Brad says the pilot passed.
3. **Spend caps are set by Brad:** an Apify cap per wave (US$) and a Clay credit budget per wave. They are never raised mid-run.
4. **Suppression lists are loaded** before anything reaches Clay:
   - HubSpot companies (by domain) and contacts (by email);
   - the existing ~700 leads (Hit List MASTER, Smartlead Master List, Extraction Register);
   - Smartlead's global blocklist;
   - HubSpot unsubscribes.
5. **Smartlead campaigns exist per tier** (`T1`, `T2`, `T3` tokens, Campaign Naming Standard), with "Reply yes" copy, sender identification and an unsubscribe line. They are wired to the SOP-5A-01 reply webhook.
6. **Credentials live only in n8n or the environment.** Never in sheets, Clay text columns, CSVs or this repo.

### Before completing (per record)
7. **ICP:** Australian accounting practice, independent (not a franchise, network branch or Big 4 / mid-tier), with **1–50 staff**. Over 50 is `DQ`, not contacted.
8. **The tier comes from a staff count read off the firm's own website**, i.e. the team or about page, read by Clay's AI column. A vendor-only headcount gives `Unverified`, which is **not activated** (it's held for review).
9. **Contact quality:** a named person in a decision-maker role, with a **validated** email at the firm's domain. No generic inboxes (`info@`, `admin@`, `reception@`) and no free-mail addresses in Smartlead.
10. **HubSpot first:** the company and contact exist in HubSpot, with tier, source and sprint tags, **before** enrolment in Smartlead.
11. **Batch approval:** every Smartlead push is approved by Brad (one Slack approval per batch, not per record).
12. **Email source is recorded** (`ermos_email_source`, e.g. firm website or Clay waterfall provider) for Spam Act inferred-consent hygiene. Every email identifies ERMOS and carries a working unsubscribe.

## 5. Step-by-Step Procedure

### Stage 0: Set-up (once, about half a day)
1. **HubSpot:** confirm the SOP-1A-01 §6.3 properties exist, and add the sprint properties in §6.4.
2. **Clay:** build the table "ACC Sprint: Accounts" with the columns in §6.3, plus a people table "ACC Sprint: Contacts" linked by domain.
3. **Smartlead:** create three campaigns following the Campaign Naming Standard (`T1`, `T2`, `T3` size tokens, accounting vertical, sprint id) with tier-appropriate "Reply yes" copy. Attach the SOP-5A-01 webhook.
4. **n8n:** import WF-2B02-A/B/C (§6.1) and attach credentials. Load the suppression sets.

### Stage 1: Source (the skill)
1. **Pilot:**
   ```bash
   python3 scripts/google_scraper.py --segment accounting --mode pilot \
     --suburb "Parramatta,NSW" --run-cap-usd 1 --sop-version v0.2
   ```
   If `api.apify.com` is blocked (as in Claude Code cloud sessions), run the same input through the Apify connector, save the items, and normalise them with `--from-items-file` (see SKILL.md).
2. **Pilot pass criteria (Notion SOP):**
   - CSV and `.run.json` are in `01_raw`;
   - at least 70% of rows have a domain;
   - all 18 columns are present;
   - cost under US$1;
   - no contact data.
3. **Wave 1 batch** (after Brad's go, with his cap):
   ```bash
   python3 scripts/google_scraper.py --segment accounting --mode batch \
     --suburbs-file config/locations/accounting_wave1.txt \
     --max-places-per-search 60 --run-cap-usd <Brad's wave cap> --sop-version v0.2
   ```
4. **Waves 2–3:** more location files, or `ALL,<STATE>` runs, until the funnel maths in §1 is met.

### Stage 2: Pre-Clay hygiene (n8n WF-2B02-A, automatic on each new file in `01_raw`)
1. Validate the 18-column schema and dedupe across all sprint files on `domain`, falling back to `place_id`.
2. Suppress against HubSpot, the existing 700 and Smartlead, logging the reason per row.
3. Rows without a domain go to `02_enriched/no_domain_<run>.csv`. They're held, not sent to Clay, until Brad decides whether Clay should hunt for their domains (it costs credits).
4. Push the remaining rows to the Clay table webhook in chunks (e.g. 100 per minute). Move the source file to `_processed/`.

### Stage 3: Enrich and tier (Clay, automatic per row)

| Clay column (in order) | What it does |
|---|---|
| Company enrichment | Firmographics from the domain: name, LinkedIn, vendor headcount, industry, location |
| **Website staff count** (AI column reading the team / about / people page) | Returns `staff_count`, `evidence_url`, `confidence` |
| **ICP check** (AI column) | Accounting practice? Independent (not a franchise or network branch)? Australian? Returns `pass` / `fail` + reason |
| **Tier** (formula) | `staff_count` 1–9 → `T3` · 10–30 → `T1` · 31–50 → `T2` · > 50 → `DQ` · missing or low confidence → `Unverified` |
| Find people (only if ICP = pass and tier ∈ T1/T2/T3) | Searches decision-maker titles: Principal, Director, Managing Director, Managing Partner, Partner, Owner, Founder. Also returns practice managers for HubSpot (multi-threading), flagged `role = Influencer/Champion` |
| Contacts per tier | **T3:** 1 decision-maker · **T1:** up to 2 (decision-makers first) · **T2:** up to 3 (decision-makers + practice/operations manager) |
| **Email waterfall + validation** | Work email via Clay's waterfall, then a validation status. Only `valid` emails proceed to Smartlead |
| **Phone waterfall** | **T1 and T2 decision-makers only** in this sprint (credit control). T3 phones are found on reply (SOP-5A-01). Brad can widen this |
| Callback | HTTP column posts the finished row (company + contacts) to n8n WF-2B02-B |

### Stage 4: CRM sync (n8n WF-2B02-B, automatic per Clay callback)
1. Validate the row. Absolutes 7–9 decide whether it is `ready`, `held` (Unverified, low confidence) or `rejected` (DQ, ICP fail).
2. **Upsert to HubSpot:**
   - company by domain;
   - contacts by email, associated with the company, with buying-committee labels (Decision Maker / Influencer / Champion);
   - properties per §6.4.
3. Set `ermos_lead_status = Ready for Smartlead` (ready decision-makers only); `Held` or `Rejected` with a reason otherwise.
4. Write `02_enriched` and `03_ready` CSV snapshots per batch, for audit.

### Stage 5: Activate (n8n WF-2B02-C: daily at 09:00 Sydney, or on demand)
1. Collect HubSpot contacts with `Ready for Smartlead`, grouped by tier.
2. Post a Slack approval card to Brad, showing:
   - count per tier;
   - a sample of 10 records with firm, suburb, title, tier and staff evidence link;
   - held and rejected counts with their top reasons.
3. **On approve:** add the contacts to the matching tier campaign in Smartlead, in batches. Custom fields: `first_name`, `firm_name`, `suburb`, `tier`, `staff_count`. Then write back to HubSpot: `ermos_smartlead_campaign`, `ermos_smartlead_lead_id`, `ermos_enrolled_at`, and status `Enrolled`.
4. **On reject:** nothing is sent. Brad's comment is logged on the batch.
5. **Respect sending capacity:** never enrol more contacts than the campaigns' mailboxes can send in the sequence window (Open Items: mailbox inventory).

### Today's runbook (manual-assist, before n8n is live)
1. **Pilot now:** run through the Apify connector (from this session) or the script on Brad's machine, then normalise to the CSV.
2. **Brad reviews the pilot.** If it passes, run wave 1 where `api.apify.com` is reachable (Brad's machine), with his cap.
3. **Clay:** import the wave CSV into "ACC Sprint: Accounts" (CSV import) and run the columns in Stage 3.
4. **HubSpot:** export Clay's ready rows to CSV and use HubSpot's native import (dedupe on domain and email). This is a **temporary exception** to "n8n runs every CRM injection", for today only, if Brad approves it.
5. **Smartlead:** upload the approved decision-makers per tier campaign as CSV, and start sending within mailbox limits.
6. **Next:** n8n WF-2B02-A/B/C replace steps 3–5 from the next wave.

## 6. Data Flow & Automation

### 6.1 n8n workflows

**WF-2B02-A "Sprint Intake"**

| # | Node | Purpose |
|---|---|---|
| 1 | Google Drive Trigger (new file in `PIPELINE/01_raw`, name starts `accounting_`) | Start on each scraper output |
| 2 | Drive: download CSV + `.run.json` · Code: schema check | Abort and alert if the 18 columns aren't present |
| 3 | HubSpot: search companies by domain (batched) · Google Sheets: read existing-lead lists · Smartlead: blocklist | Build the suppression set |
| 4 | Code: cross-file dedupe + suppress + split (to Clay / no-domain hold / suppressed) | Reasons logged per row |
| 5 | Loop (chunks of 100) → HTTP: Clay table webhook | Rate-limited feed into Clay |
| 6 | Drive: move file to `_processed/` · write `02_enriched/suppressed_<run>.csv` and `no_domain_<run>.csv` | Audit trail |
| 7 | Slack: run summary (rows in, suppressed, held, sent to Clay) | n/a |

**WF-2B02-B "Clay → HubSpot"**

| # | Node | Purpose |
|---|---|---|
| 1 | Webhook (from the Clay HTTP column; secret path) | One finished company row with contacts |
| 2 | Code: validate (Absolutes 7–9) → `ready` / `held` / `rejected` | n/a |
| 3 | HubSpot: upsert company (domain) → upsert contacts (email) → associate + labels | System of record |
| 4 | HubSpot: set sprint properties and lead status | n/a |
| 5 | Error branch: HubSpot 409/429 → retry with backoff; persistent failure → Slack alert with domain | No silent drops |

**WF-2B02-C "Smartlead Activation"**

| # | Node | Purpose |
|---|---|---|
| 1 | Schedule (09:00 Australia/Sydney) + Manual trigger | n/a |
| 2 | HubSpot: search contacts `ermos_lead_status = Ready for Smartlead`, by tier | n/a |
| 3 | Code: capacity check (mailboxes × daily limit × sequence days) → trim the batch | Never over-enrol |
| 4 | Slack: approval card (Send and Wait for Response) | **Human gate** |
| 5 | On approve: Smartlead add leads to the tier campaign (batched) | n/a |
| 6 | HubSpot: write campaign, lead id, enrolled time, status `Enrolled` | n/a |
| 7 | Slack: confirmation with counts | n/a |

### 6.2 Raw input schema (from the skill)
`segment, search_term, suburb_searched, firm_name, website, domain, phone, address, state, postcode, google_category, rating, reviews_count, place_id, maps_url, scraped_at, source, run_id`. Fixed 18 columns. `state` is normalised to NSW / VIC / QLD / WA / SA / TAS / ACT / NT.

### 6.3 Clay output (callback payload)
**Company:**
- `domain`, `firm_name`, `website`, `address`, `suburb`, `state`, `postcode`, `google_place_id`, `google_category`;
- `vendor_headcount`, `staff_count`, `staff_count_evidence_url`, `staff_count_confidence`, `tier` (`T1`/`T2`/`T3`/`DQ`/`Unverified`);
- `icp_pass`, `icp_reason`, `linkedin_company_url`, `run_id`.

**Contacts[]:**
- `first_name`, `last_name`, `title`, `role` (Decision Maker / Influencer / Champion), `email`, `email_status`, `email_source`;
- `phone`, `phone_source`, `linkedin_url`.

### 6.4 HubSpot properties (in addition to SOP-1A-01 §6.3)

| Object | Internal name | Type | Values / rule |
|---|---|---|---|
| Company | `ermos_source` | Dropdown | `google_maps` · `apollo` · `lookalike` · `inbound` · `partner` |
| Company | `ermos_sprint` | Single-line text | e.g. `ACC-2026-10` |
| Company | `ermos_google_place_id` | Single-line text | Dedupe fallback |
| Company | `ermos_icp_reason` | Single-line text | From Clay |
| Company | `ermos_staff_count_confidence` | Number (0–1) | From Clay |
| Contact | `ermos_lead_status` | Dropdown | `Ready for Smartlead` · `Enrolled` · `Held` · `Rejected` |
| Contact | `ermos_email_source` | Single-line text | Waterfall provider or `firm website` |
| Contact | `ermos_smartlead_campaign` | Single-line text | Campaign name |
| Contact | `ermos_smartlead_lead_id` | Single-line text | n/a |
| Contact | `ermos_enrolled_at` | Datetime | Sydney time |

Existing properties reused: `ermos_vertical = accounting`, `ermos_verified_staff_count`, `ermos_staff_count_evidence`, `ermos_account_tier`, `ermos_state` (SOP-1A-01).

### 6.5 Data flow summary

```
leadgen-google-scraper (Apify) ──► Drive PIPELINE/01_raw (CSV + manifest)
        └─► n8n WF-2B02-A: schema check → dedupe → suppress (HubSpot, existing 700, Smartlead) → Clay webhook
                └─► Clay: company enrich → website staff count → ICP check → Tier → find people → email + phone waterfall
                        └─► n8n WF-2B02-B: validate → HubSpot upsert (company, contacts, associations, tier, status)
                                └─► n8n WF-2B02-C (daily): Ready DMs → capacity check → Slack approval → Smartlead tier campaigns
                                        └─► replies → SOP-5A-01
```

**System of record:** HubSpot. Clay is the enrichment workspace. Drive holds immutable batch files. Smartlead holds sending state only.

## 7. Quality Assurance (QA) Guidelines

### What "Good" Looks Like

| Metric | Target |
|---|---|
| Pilot | Passes the Notion pilot criteria (≥ 70% with a domain, 18 columns, < US$1, no contact data) |
| Net leads per raw listing | ≥ 0.40 (re-set from the pilot) |
| Tier accuracy | ≥ 90% on a weekly sample of 20 firms, checked by Brad against the evidence URL |
| ICP accuracy | ≥ 95% of enrolled firms are genuine independent AU accounting practices of 1–50 staff (same sample) |
| Email quality | 100% of enrolled contacts `valid`. Smartlead bounce rate < 2% per campaign |
| Duplicates | 0 contacts enrolled twice; 0 overlap with the existing 700 |
| HubSpot-first | 100% of enrolled contacts have a HubSpot company + contact with tier and source before the first send |
| Sprint progress | Leads Ready + Enrolled tracked weekly against 6,000 |

### What "Bad" Looks Like
- Batches over many suburbs with overlapping search terms, re-buying the same firms (check the duplicate counts in each manifest).
- Bookkeepers, tax-return franchises, financial planners or software vendors tagged as accounting practices.
- Tiers from vendor headcount ("LinkedIn says 11–50") instead of the firm's own team page.
- `info@` inboxes or a receptionist enrolled as the "decision-maker".
- Enrolling more contacts than the mailboxes can send, so sequences stall and domains burn.
- Contacts in Smartlead that aren't in HubSpot, or that are on the existing 700 list.
- Phone credits spent on every T3 sole practitioner before they've replied.

## 8. Exception Handling

### Auto-Pass Criteria
A contact goes to `Ready for Smartlead` with no human review (beyond Brad's batch approval) when **all** of these hold:
1. the company has `icp_pass = true`, a `tier` of T1/T2/T3, and `staff_count_confidence` ≥ 0.8 with an evidence URL;
2. the contact role is Decision Maker, the email is `valid`, the domain matches the firm, and it isn't a generic or free-mail address;
3. the contact isn't suppressed (HubSpot, existing 700, Smartlead blocklist, unsubscribes);
4. the firm's state is in Australia.

### Flagging Triggers
These set `Held` with a reason. Brad reviews the Held view in HubSpot twice a week.

| Code | Trigger | Handling |
|---|---|---|
| `L01_unverified_size` | No website staff count, or confidence < 0.8 | Manual count from the team page, or leave held |
| `L02_boundary_size` | Staff count of 9–11 or 29–31 (tier boundary) | Confirm the count. The tier decides the campaign |
| `L03_icp_unsure` | ICP check returned `unsure` (e.g. accountant + financial planner, bookkeeper) | Decide: in, out, or another vertical (finance) |
| `L04_network_member` | Name or website suggests a network or franchise member not on the exclusion list | Add to exclusions if it's a pattern |
| `L05_no_dm` | ICP pass but no decision-maker with a valid email | Leave held. Optional manual LinkedIn find |
| `L06_catch_all` | Email is catch-all, or only risky validation is available | Hold. Don't enrol in this sprint |
| `L07_existing_relationship` | Firm already in HubSpot with a deal, a partner registration, or a replied contact | Never cold-enrol. Route to the owner |
| `L08_no_domain` | The listing has no website | Held file. Brad decides whether Clay should hunt for a domain |
| `L09_cap_reached` | Apify or Clay wave budget reached | Stop and report. Never raise the cap without Brad's number |
| `L10_capacity` | Ready contacts exceed sending capacity | Trim the batch; the rest wait for the next day |

---

## Open Items

1. **"Lead" definition:** confirm 6,000 counts decision-maker contacts (assumed), not firms.
2. **Wave 1 caps:** the Apify cap for wave 1 (estimate US$22–58 for up to ~14,400 places at US$1.50–4 per 1,000), and the Clay credit budget per wave.
3. **Sending capacity:** how many warmed Smartlead mailboxes, at what daily limit? 5,300 new contacts × a 3-step sequence is about 16,000 emails. At 40 per mailbox per day with 10 mailboxes, that's about 40 days. This sets the realistic enrolment pace.
4. **Today's HubSpot import:** approve the one-off CSV import into HubSpot (and CSV upload to Smartlead) before n8n is live, or wait for WF-2B02-B/C.
5. **Practice managers:** decision-makers only go to Smartlead (per the brief). Should practice managers at T1/T2 firms get their own campaign later (multi-threading), or stay HubSpot-only?
6. **Phone scope:** confirm phones for T1/T2 decision-makers only in this sprint (T3 on reply).
7. **Geography:** wave 1 is metro-only (five largest metros plus Canberra). Confirm whether regional areas (and Tasmania / NT) are in for waves 2–3.
8. **Bookkeepers and tax agents:** in or out of the accounting ICP? They're currently held via `L03`.
9. **Apify access:** add `api.apify.com` to this environment's allowed domains and `APIFY_TOKEN` as an environment secret, so batches can run from Claude Code. Or run them on Brad's machine.
10. **Workflows.io:** supply a lead-gen / enrichment playbook page to validate §6.

## Change Log

| Version | Date | Author | Change |
|---|---|---|---|
| v0.1 | 2 Oct 2026 | Claude Code for Brad | First draft: Google Maps → Clay → HubSpot → Smartlead sprint pipeline on the Core Tech Stack, with today's manual-assist runbook |
