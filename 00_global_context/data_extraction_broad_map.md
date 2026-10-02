# Data Extraction Broad Map (TAM baseline)

| | |
|---|---|
| **Purpose** | How firms are sourced, extracted, verified and staged into the outbound pipeline: tools, folders, sheet conventions, fit criteria and field schemas. |
| **Provenance** | Synthesised 2 Oct 2026 from Notion Ermos HQ and Google Drive |
| **Status** | Draft for Brad's review |
| **Authority** | Notion Ermos HQ (ERMOS RevOps Operating System) is the single source of truth. Drive briefs are used only where Notion is silent, and only where no 05 Decisions Log ruling overrides them. Source keys in [brackets] resolve in §11. |

---

## 1. Governing rulings that shape extraction (apply before anything below)

| Rule | Value | Source |
|---|---|---|
| Outbound size band | **10 to 50 seats/staff, strictly.** Every list and campaign holds firms in this band only. Product sweet spot is 5 to 50, but that is not a targeting band. | [D-24SEP] |
| Over 50 | Disqualified. No campaign, no contact sourced. | [D-24SEP], [CNS] |
| Approved verticals | Full words only: **accounting, law, aged care, healthcare, finance**. Campaign token `AgedCare`; filenames and tags "aged care". | [D-24SEP], [D-17SEP], [CNS] |
| Products | Two, both active: **ERMOS Edge** (cloud, Australian SOC 2 compliant server) and **ERMOS Dominion** (on-site). Fit is assessed for both, not Dominion alone. | [D-17SEP], [PROD] |
| Pricing context (sets the 10-seat floor) | Edge A$99/seat/month, 10-seat minimum. Dominion A$99/seat/month, 10-seat minimum, plus A$7,500 hardware per box; one box per 15 people (new box at seats 16, 31, 46). All AUD ex GST. | [D-24SEP], [D-28SEP] |
| Claims | Never describe Dominion as air-gapped or disconnected. "Air-gapped" may appear only as a phrase we detect on a prospect's site, never as an ERMOS claim. | [D-28SEP], [MSB] |
| Out of scope | Mortgage broking and insurance broking (not approved verticals). Partner/MSP firms are a separate channel ICP, not end buyers. | [D-24SEP], [ICP07] |
| Governance | Agents read Approved pages only; log SOP version per run; never edit a governed page; proposed rule changes go to 06 Proposed Changes. `00.archive admin..00` must not be used. | [MSB], [LGC] |

---

## 2. Source and tool map

| Tool / source | Role in extraction | Rule | Source |
|---|---|---|---|
| **Google Maps via Apify** (`compass/crawler-google-places`) | Raw firm discovery by segment × suburb | Writes one raw CSV per run to `01_raw`. No enrichment, no contact, no copy. Pilot first. | [SOP-GS], [SKILL-GS] |
| **Apollo** | Candidate sourcing (company + person search) and part of the enrichment waterfall | Apollo sources; the firm's own website verifies. A firm never reaches the list on Apollo data alone. Apollo headcount is indicative only. | [MSB], [B-ACC], [B-LAW] |
| **LinkedIn Sales Navigator** | List building and account mapping | Named in the eight-step engine; no SOP yet. | [MSB] |
| **Clay** | Enrichment (domain, headcount, industry, contacts, email status) | Clay output is never accepted without independent website validation; a matching Clay industry label never approves a firm on its own. Not named in the current Master System Brief (see §10). | [CLAY] |
| **BetterContact → Apollo** | Enrichment waterfall for verified contact data | Runs only on qualified firms. | [MSB] |
| **ZeroBounce** | Bounce check before enrolment | Mandatory before any Smartlead upload. | [MSB] |
| **Smartlead** (or Instantly) | Outreach platform only | Not a source of prospect intelligence. Receives human-approved rows only. | [MSB], [CLAY] |
| **RB2B, job changes, ad engagement** | Signal capture that triggers list building | Signal layer, not bulk TAM. | [MSB] |
| **Membership and regulator registers** | Verification (hard checks), and a candidate sourcing channel still under evaluation | See §6 per vertical. Directories as a *sourcing* channel are a hypothesis, not a ruling. | [LSE], [B-LAW], [B-HC], [B-FIN] |

**Channel framing.** Apollo is likely a research channel (who to approach), not an outreach channel. Any source that scores 2 or lower on trust transfer has to be justified as first touch or reclassified as research. Referral partners, MSPs and PI insurers must be ranked alongside the four tool families. [LSE]

**Skills in scope for Lead Gen:** `leadgen-google-scraper`, `leadgen-apollo-discovery`. The skill name, `SKILL.md` name and SOP page title must match exactly. [LGC], [MSB]

---

## 3. Pipeline stages and folders

Drive: `ERMOS / 3. DATA / PIPELINE` (folder id `1nIpskjvSHuK3dCXXubP9h_SeTXXn4bTe`) holds `01_raw`, `02_enriched`, `03_ready`, `_processed`. [DIR]

| Folder | What lands here | Who writes | Defined by |
|---|---|---|---|
| `01_raw` | Raw scrape or discovery output: one CSV plus `.run.json` per run, never overwritten | Lead Gen skills only (Lead Gen writes nowhere else) | [LGC], [SOP-GS] |
| `02_enriched` | Verified firm rows with enriched contacts | Enrichment stage (separate department) | Folder named only; **no SOP or schema yet** |
| `03_ready` | Rows cleared for Smartlead import (`SMARTLEAD_<campaign>.csv`) | After human approval | Import filename from [CNS]; **stage contract undefined** |
| `_processed` | Files already consumed downstream | n/a | Folder named only |

**End-to-end order (as specified across sources):**
signal or segment brief → raw discovery (`01_raw`) → website verification and tiering (ICP_Master) → enrichment waterfall (BetterContact, Apollo, Clay) → ZeroBounce → Brad approval → Smartlead import (`03_ready`) → Smartlead Extraction Register entry. [MSB], [CLAY], [SOP-GS]

---

## 4. Raw extraction schema: Google Maps scraper

Fixed 18 columns, in order: [SOP-GS], [SKILL-GS]

`segment, search_term, suburb_searched, firm_name, website, domain, phone, address, state, postcode, google_category, rating, reviews_count, place_id, maps_url, scraped_at, source, run_id`

- `segment` must be one of `accounting`, `law`, `healthcare`, `finance`, `aged-care`. Note that `aged-care` is hyphenated in the skill, while the house style is "aged care" in tags (see §10).
- `scraped_at` is ISO 8601, Sydney time. `source` is always `google_maps`.
- Dedup within the run on `domain`, falling back to `place_id` where there is no website.
- Filename: `<segment>_<suburb-or-multi>_<YYYY-MM-DD>_<HHMM>.csv`. The `.run.json` records actor input, run ids, row counts, SOP version and the cost Apify reported.

**Run rules** [SOP-GS]
- Pilot: 1 search term × 1 suburb, 20 places, spend cap US$1. A batch runs only after Brad passes the pilot.
- Batch default: 20 places per search, cap US$5 per run. Never raise a cap without Brad supplying the number.
- Paid add-ons off: contacts, social profiles, leads, reviews, images. Detail-page scraping stays off unless the pilot shows website or phone missing without it.
- Skip closed places. Country `au`, language `en`.
- Pilot pass criteria: file and `.run.json` in `01_raw`; at least 70% of rows have a domain; all 18 columns present; cost under US$1; no contact data added.
- Accounting defaults only: terms `accountant · accounting firm · chartered accountant · tax accountant · CPA`; pilot suburb Parramatta NSW; batch suburbs Sydney CBD, North Sydney, Chatswood and Parramatta (all NSW); name or category exclusions `H&R Block · Liberty Tax · ITP · Etax`.

**Execution status:** the SOP's metadata says Approved, but its body says DRAFT and "stop at Step 0". 06 Proposed Changes records this as BLOCKED until Brad resolves the pilot, the Apify price and workspace reachability. **Treat the scraper as not cleared to run.** [PC-GS]

---

## 5. ICP_Master sheet conventions (the verified firm register)

Sheet: `ICP_Master`, id `1cgunhz43AF45AReQm_IOSpdoI2L7MuTnx95icTH3INk`. Tabs: **Legend**, **Master** (about 1,219 rows), **Holding** (about 353 rows), **Exclusions** (about 381 rows). [ICPM]

**Legend rules** [ICPM]
- **One row per firm**, deduplicated on **Domain** across all segments. If the domain already exists, do not add a row: append the new segment to `Segment(s)` and fill the blank columns.
- **Segment(s):** every segment the firm qualifies for, semicolon separated (e.g. `Accounting; SMSF`).
- **Source segment:** the segment that first sourced the firm. Never changes once set.
- **Staff count:** verified from the firm's own team or about page, **not Apollo's headcount**.
- **Tier:** A = core fit plus at least one amplifying signal · B = core fit, no amplifier · C = right shape, something unresolved. A and B count toward a segment target; C is held in Master but not counted.
- **Verification evidence:** the URL or exact phrase that confirmed the fact. Required. A yes/no is not evidence.
- **Holding tab:** strong firms just below the floor and firms above the band, held for Brad's decision and not counted. *The Legend's current bands (3 to 4 below, 31 to 50 above) predate the 24 Sep ruling; see §10.*

**Master / Holding columns (24):**
`Firm name · Domain · Website · Segment(s) · Source segment · City / Region · Staff count · Services · Professional body · Segment signals · M365 or Copilot evidence · Contact 1 name/title/email/LinkedIn · Contact 2 name/title/email/LinkedIn · Signals found · Tier · Verification evidence · Notes / exclusion reason · Batch`

- `Segment signals` holds software (e.g. Xero, MYOB, Karbon, Class Super).
- `Batch` format: `YYYY-MM-DD · Segment · Metro · Apollo bucket` (e.g. `2026-08-13 · Accounting · Sydney · 11-20`).

**Exclusions columns (6):** `Firm name · Domain · Segment · Exclusion reason · Evidence (URL/phrase) · Batch`. Log every exclusion with its reason and never delete it. [ICPM], [B-ACC]

**Hygiene:** cell A1 on Master and Holding contains stray prompt text instead of a header. Clean it before any automated read. [ICPM]

---

## 6. Firmographic fit by approved vertical

Common to every brief: Apollo sources and the website verifies. Work in batches of one metro × one Apollo bucket (healthcare adds the sub-vertical), checkpoint every batch, dedup on domain and across segments, and **stop and flag a shortfall rather than widening criteria**. Apollo buckets 1–10, 11–20 and 21–50 are all searched; banding happens at verification. Geography in all briefs: Sydney, Melbourne, Queensland statewide (Brisbane, Gold Coast, Sunshine Coast, Toowoomba, Cairns, Townsville) and Canberra/ACT; regional NSW and VIC out unless approved. Multi-office firms qualify if the principal office is in region. [B-ACC], [B-LAW], [B-HC], [B-FIN]

> Size: every brief below says "Core 5–30, outliers 31–50, micro 1–4". For **outbound listing**, the 24 Sep band of 10 to 50 replaces those bands. The verification logic is carried; the size bands are not.

### Accounting [B-ACC], [ICPM]
- **Firm type:** public practice (accounting, tax, BAS and business services, audit, SMSF, advisory).
- **Hard check:** TPB-registered tax or BAS agent and/or CA ANZ, CPA Australia, IPA or SMSF Association membership, evidenced on the site.
- **Apollo:** industry Accounting (secondary net Financial Services). Keywords: chartered accountants, tax agent, BAS agent, business services, tax advisory, audit and assurance, SMSF. Tech where populated: Xero, MYOB, Microsoft 365.
- **Tier A amplifiers:** audit or SMSF named; named workpaper software (CaseWare, Xero Workpapers, MYOB AE/AO, Class Super, BGL, Karbon, FYI Docs and similar); seasonal or contract job ads; public statement on privacy, sovereignty or AI caution; multi-partner structure.
- **Disqualifiers:** solo setups; Big 4 and national networks or roll-ups (including association brands); offshore processing teams; non-regulated (bookkeeping-only, coaching, vCFO without confidentiality obligation); public commitment to running client data through a public cloud LLM. AI curiosity alone is **not** a disqualifier.

### Law [B-LAW]
- **Firm type:** commercial, litigation and disputes, corporate/M&A, property (including conveyancing within a law firm), family, wills and estates, employment, construction, insurance.
- **Hard check:** the regulator's public register, not a site badge. NSW Law Society; Victorian Legal Services Board & Commissioner; Queensland Law Society; ACT Law Society.
- **Counting:** count total staff, not lawyers. Fee-earner-only pages are banded provisionally and marked unconfirmed.
- **Apollo:** industry Law Practice (secondary Legal Services). Tech: Microsoft 365, LEAP, Smokeball, Actionstep.
- **Record:** `PMS product` and `PMS deployment` (Cloud-native / Server-based / Unknown). Neither value is filtered out.
- **Tier A amplifiers:** document-heavy core practice (litigation, M&A or due diligence, construction, insurance, estates disputes); identified PMS or DMS; fee-earner job ads; privilege or AI-caution statements; multi-partner structure.
- **Disqualifiers:** barristers and chambers (Apollo often shows a chambers as a 20 to 60 person firm); in-house legal teams; CLCs, legal aid, pro bono; offshore legal processing; legal-adjacent vendors; public cloud-LLM commitment. Standalone licensed conveyancers are **routed** to a holding file, not excluded.

### Healthcare [B-HC]
- **Sub-verticals, in priority order:** general practice → specialist consulting → allied health (where NDIS, WorkCover or CTP reporting is the qualifier). Record the sub-vertical in its own column.
- **Parked:** medico-legal and IME practices (a recorded decision). Dental, optometry, audiology and podiatry need approval before any build.
- **Ownership check comes first** (footer, privacy policy, careers portal, group directories). Corporate-owned clinics are excluded and the parent is recorded.
- **Hard check:** at least one named practitioner on the Ahpra public register.
- **Counting:** two numbers, Practitioner count and Total staff (contractors included). Band on total.
- **Record:** `Clinical software` and `Deployment` (Server-based / Cloud / Unknown); `Ambient scribe` (product or None found), which is a positive signal and not a disqualifier; `Accreditation` (AGPAL / QPA / none found).
- **Disqualifiers:** public hospitals and LHDs; private hospital groups; telehealth-only platforms; offshore transcription; health-adjacent non-clinical businesses; public commitment to putting identifiable patient data into a general-purpose LLM. Never qualify on diagnostic or clinical-decision-support interest.
- **Buyer:** the Practice Manager is the primary title.

### Finance [B-FIN]
- **Firm type (per the only brief available):** retail financial advice practices (comprehensive planning, retirement, risk, SMSF advice, aged care advice).
- **Hard check, done first and before any enrichment:** ASIC Financial Advisers Register. It also returns the licensee.
- **Record on every row:** `Licensee status` (Self-licensed / Authorised representative / Institutional) and `Licensee name`. Build self-licensed first, then authorised representatives (who are in scope, not excluded).
- **Mandatory cross-segment dedup** against the accounting rows by domain, trading name and street address before enrichment, because advice and accounting overlap heavily.
- **Disqualifiers:** licensees and dealer groups (look for "join us / become an AR" pages, at every size); institutionally owned or aligned practices; product manufacturers and platforms; stockbroking and institutional wealth; robo-advice; unlicensed money coaches and promoters; offshore paraplanning; public cloud-LLM commitment. Mortgage-only and insurance-only brokers are out of scope (§1).
- **Note:** advice software is overwhelmingly hosted. Do not spend time hunting for a deployment split.

### Aged care: no extraction criteria exist
The Drive aged care brief is an empty template ("Status: not started"). The 02 ICP & Sentiment database has no records. The healthcare brief routes aged care and NDIS providers to a separate `aged-care-ndis-candidates.xlsx`, holding only name, website, city and staff count. **Until Brad rules, capture only those four fields.** [B-AGE], [B-HC]

---

## 7. Size bands for extraction rows

| Band label | Staff | Outbound? | Source |
|---|---|---|---|
| `10–15` | 10 to 15 | Yes | Notion 01. ICP Master Database `Firm Size` options [ICPDB] |
| `16–30` | 16 to 30 | Yes | [ICPDB] |
| `31–45` | 31 to 45 | Yes | [ICPDB] |
| `46–50` | 46 to 50 | Yes | [ICPDB] |
| below 10 | 1 to 9 | No (product fit from 5, but not outbound) | [D-24SEP] |
| `TOO_LARGE` | over 50 | No. Disqualified | [D-24SEP], [CNS] |
| unresolved | n/a | Hold. Never default into the smallest band | [CNS] |

The ICP Master Database bands line up with the Dominion box thresholds (1 box to 15 people, new boxes at 16, 31 and 46) [D-28SEP]. That is an observation, not a recorded rationale.

---

## 8. Contact and enrichment field rules

- **Multi-thread:** two contacts per firm where available. Accounting and law: one Partner/Principal-level plus one Practice Manager/COO-level. Healthcare: Practice Manager first, then clinician-owner. Finance: Principal/Director plus Practice Manager. Search "Legal Practice Director" (law) and "Responsible Manager" (finance) explicitly. [B-ACC], [B-LAW], [B-HC], [B-FIN]
- **Named decision maker:** a real person with a title, never `info@`, `admin@` or `reception@`. [B-ACC]
- **Email status vocabulary:** Verified / Validated / Unverified / Guessed / Catch-all / Unavailable. Never fabricate an address. [CLAY]
- **No statutory citations in any cell** (e.g. Privacy Act, APP 8, Uniform Law, s912A). Facts about the firm go in the sheet; framing does not. The `Jurisdiction` column takes NSW / VIC / QLD / ACT (law adds the regulator name). [B-LAW], [B-HC], [B-FIN]
- **Blank is a correct answer** for signals that cannot be found. Apollo technographics on small AU firms are thin; never assert Copilot from Apollo. [B-ACC]
- **Review queues** before export: Approved (ready for Brad) · Rejected (recorded for learning) · Uncertain (Brad review) · Partnership opportunity · Data problem · Approved for Smartlead export · Held (contact data inadequate). Nothing is "Ready for Smartlead" without human approval. [CLAY]

**Smartlead import and naming** [CNS]
- Campaign format: `STATUS_VERTICAL_SIZE_JOB_VERSION`. Import file: `SMARTLEAD_<same name>.csv`. CSV columns `segment` (human-readable) and `tag` (link tag, e.g. `5-30-cm`).
- Job tokens (`Decision_Makers`, `Senior_Accountants`, `Client_Managers`, `Practice_Managers`, `IT_Specialists`, `General`) are ruled for accounting only. Other verticals need their own before a first campaign.

**Smartlead Extraction Register, Accounting** (id `1gmwkEl4Wa9udutJQoLfsLseOFeKLj3g783jT4aPQdJI`) [SER]
- Schema: `email · first_name · last_name · company · extraction · extracted_date`.
- State at 2 Oct 2026: one batch, `Extraction 1`, dated 2026-09-30, about 235 contact rows (roughly two per firm). The register holds personal data. Never copy rows into this repo.
- It has no `domain` column, so it cannot be joined to ICP_Master on the dedup key (see §10).

---

## 9. Extraction checklist (per firm, in order)

1. Vertical is approved (§1). Healthcare: run the ownership check. Finance: run the ASIC register check. Do these **first**.
2. Dedup on Domain against ICP_Master (all segments). Finance: also check trading name and address.
3. Count staff on the firm's own site and assign the §7 band. Over 50 → Exclusions. Unresolved → Tier C or Holding.
4. Run the vertical hard check (TPB/body, law register, Ahpra or ASIC) and record the evidence URL or phrase.
5. Check the vertical disqualifiers (§6). Log any exclusion with its reason.
6. Capture signals, or leave the cell blank. Assign Tier A/B/C per the ICP_Master Legend.
7. Enrich contacts only after steps 1 to 6 pass. Then ZeroBounce, Brad approval, import, and a register entry.

---

## 10. Excluded as superseded

| Left out | Where it came from | Superseded by |
|---|---|---|
| "1 to 50 staff cap"; bands `1-4 / 5-30 / 31-50`; 15-point scoring with size points favouring 5–30 | Drive `01 icp-brief.md` (accounting, 9 Sep) [B-ICP] | 24 Sep: outbound strictly 10 to 50 [D-24SEP] |
| Core 5–30 build bands; Micro 1–4 cohorts (caps 25/50); Outlier 31–40 / 41–50 as secondary passes | Drive briefs 01–04 (Aug) | 24 Sep outbound band [D-24SEP] |
| "15 to 100 seats" target | Aug SLT Q&A (not reread) | 24 Sep [D-24SEP] |
| P1/P2/P3 Smartlead profiles | Drive `ermos-smartlead-icp-profiles.md` (Aug, not reread) | 24 Sep size and vertical rulings |
| "10–100 seat" target in the title of the 24 Sep decision | 05 Decisions Log | Body of the same ruling (outbound 10 to 50) |
| Dominion A$2,599 + GST per month, "up to 30 staff", "no per-user licences", and the size-floor logic built on that price | Drive briefs and `01 icp-brief.md` | Per-seat pricing, 28 Sep [D-28SEP] |
| Dominion flat bands (A$2,499 / A$4,499 / A$6,499) | 24 Sep ruling | 28 Sep per-seat ruling [D-28SEP] |
| "Air-gapped" or "never leaves the premises" as product description | Drive briefs | 21 Sep and 28 Sep guardrails [D-28SEP] |
| Mortgage broker and insurance broker list builds | Drive `05-icp-mortgage-brokers-au.md`, `06-icp-insurance-brokers-au.md` | Not approved verticals [D-24SEP] |
| Acronym verticals (ACC, LAW, AGE, HLT, FIN; `Acct`) | Aged care brief template; legacy campaigns | Full words, 17 Sep [D-17SEP], [CNS] |
| Merge-field copy and Dominion-hardware email wording | Drive `ICP_MasterDerivedColumns20.md` (Aug) | Hormozi Standard v2.0, 29 Sep (copy is outside this file's scope) |
| Anything under `00.archive admin..00` (e.g. Sales & Market Intelligence ICP summaries) | Notion archive | Master System Brief rule 5 [MSB] |

---

## 11. Sources

| Key | Title | Location |
|---|---|---|
| D-24SEP | 05 Decisions Log: Hybrid pricing, 10–100 seat target market, partner standard (24 Sep 2026) | https://app.notion.com/p/3e577626a80981aca23bf476f648027b |
| D-28SEP | 05 Decisions Log: Dominion per-seat pricing model (28 Sep 2026) | https://app.notion.com/p/19294104ed9a4ae185badaaf7c2e3033 |
| D-17SEP | 05 Decisions Log: Client document system, full-word verticals (17 Sep 2026) | https://app.notion.com/p/3de77626a809815ea975f17a6ef82a4d |
| PROD | 05 Decisions Log: Product structure, two products (16 Sep 2026) | https://app.notion.com/p/3dd77626a8098164a50bf4eaf6296ba2 |
| MSB | 00. Master System Brief & System Rules | https://app.notion.com/p/fed5a5b00a4f4e419bba969ead145643 |
| LGC | 01 Lead Gen charter (Draft v0.1, 16 Sep) | https://app.notion.com/p/3dd77626a809811baa45d7ff665afa9a |
| SOP-GS | 03 SOPs: leadgen-google-scraper (v0.1) | https://app.notion.com/p/3dd77626a809812993b3c14047080fb7 |
| PC-GS | 06 Proposed Changes: scraper SOP marked Approved but says DRAFT | https://app.notion.com/p/b27a0ff8f47e45759471c49b3cd87c2a |
| CNS | 01 Standards: Campaign Naming Standard (Approved v3.0) | https://app.notion.com/p/3de77626a80981359117c6e9c0c1b53b |
| DIR | Drive Directory | https://app.notion.com/p/3dd77626a809814090b6eadcf647c31f |
| ICPDB | 01. ICP Master Database (schema; one Draft row) | https://app.notion.com/p/870efc8ba42c49cb93afebd461437b89 |
| ICP07 | 07 Integrators & MSPs (Partner ICP, Draft) | https://app.notion.com/p/3eb77626a8098175b5a9f41d4f8f2e5d |
| SKILL-GS | leadgen-google-scraper SKILL.md | local: `web-site-builder/skills/leadgen-google-scraper/SKILL.md` |
| ICPM | ICP_Master (Legend, Master, Holding, Exclusions) | Drive `1cgunhz43AF45AReQm_IOSpdoI2L7MuTnx95icTH3INk` |
| SER | Smartlead Extraction Register, Accounting (schema only) | Drive `1gmwkEl4Wa9udutJQoLfsLseOFeKLj3g783jT4aPQdJI` |
| B-ACC | 01-icp-accounting-advisory-au.md | Drive `1Q-hfFrcGo8rLJo9cEXPmMyYRhZuQeutlD9fuhyra4y4` |
| B-LAW | 02-icp-law-advisory-au.md | Drive `10XLzsk39YnxpgBegs8-sE2q_oLjaC2KEVGGlaLPwqT4` |
| B-HC | 03-icp-healthcare-au.md | Drive `1x7aMiGMR4b3nfuJm1QHlEsRswjl-ImfWcxVC8Xxv1_8` |
| B-FIN | 04-icp-financial-advisers-au.md | Drive `183zuJGyNBb3HhzVvZbJrouFRu6dCZ0E8C2NLybvyzEM` |
| B-AGE | 01 icp-brief.md (aged care template, not started) | Drive `1dXY3vVArV7zgH1iSmB7GF0oUzSbDQubn` |
| B-ICP | 01 icp-brief.md (accounting targeting profile, 9 Sep) | Drive `1tOyvw9jvBVPLEQESyHUg-Gc7M8LEjH5t` |
| LSE | ermos-gtm-lead-source-evaluation-prompt.md.docx | Drive `15UCD4SfO1mgzDMePbwhbhd6gKpdTGgfT` |
| CLAY | ERMOS Smartlead, Clay and ICP Validation Project.docx (7 Aug) | Drive `1buWcKE0tGwN5sbYNw6gkD7WAFUoY-p4G` |

---

## 12. Open conflicts / gaps for Brad

1. **Below-10 firms already in the pipeline.** ICP_Master carries Tier A/B firms with 5 to 9 staff, and Smartlead Extraction 1 (30 Sep) was drawn from that pool. Both predate or ignore the 24 Sep 10–50 rule. Should sub-10 rows be pulled from active sequences, moved to Holding, or allowed to finish?
2. **ICP_Master Holding definition is stale.** It holds "3–4 staff" and "31–50" firms, but 31–50 is now inside the outbound band and 5–9 is now outside it. The Legend needs a new rule.
3. **Campaign Naming Standard (Approved v3.0, 17 Sep) still uses `1-4 / 5-30 / 31-50`**, and `cohortFor()` enforces those bands. The ICP Master Database uses `10–15 / 16–30 / 31–45 / 46–50`. Which band vocabulary governs campaign names, tags and the Apps Script?
4. **Two tier systems.** ICP_Master Legend (A/B/C by core fit plus amplifier) versus the 9 Sep accounting brief (15-point score) and the Clay project (0–100 score). This file follows the Legend. Please confirm.
5. **Scraper SOP status.** Metadata says Approved, the body says DRAFT, and 06 Proposed Changes says keep execution stopped. Apify price per 1,000 places (US$1.50 or US$4) and Cowork reachability of api.apify.com are unconfirmed.
6. **Scraper SOP covers accounting only.** There are no ruled search terms, suburbs or exclusions for law, healthcare, finance or aged care.
7. **`leadgen-apollo-discovery` has no SOP** in 03 SOPs. The `02_enriched`, `03_ready` and `_processed` stage contracts and schemas are undefined.
8. **Clay's status is unclear.** It is in the Aug project doc but absent from the Master System Brief's eight-step engine (BetterContact, Apollo, ZeroBounce). The 03 Tech Stack & Schema Registry is empty.
9. **No Approved ICP records.** 02 ICP & Sentiment has zero rows. 01. ICP Master Database has only the Draft partner ICP. Every vertical criterion in §6 therefore rests on August Drive briefs, which were meant to be archived "once Notion ICP pages are Approved".
10. **Aged care has no ICP at all:** firm type, regulator, size logic, hard check and disqualifiers are all missing. The healthcare brief routes aged care away as a different regulator and buying process.
11. **Finance scope is undefined.** The only brief covers retail financial advice practices. Confirm whether "finance" also includes SMSF administrators, wealth managers or others. The Accounting Smartlead register already contains wealth-branded firms.
12. **The Master System Brief lists four verticals (omits aged care) and names Dominion as the primary offer.** The 24 Sep ruling lists five verticals and both products. The briefs score fit for Dominion only, so Edge fit criteria are absent.
13. **The Smartlead Extraction Register has no domain or campaign column**, so it cannot be deduped against ICP_Master on Domain, or tied to the campaign name the standard requires to match "in three places".
14. **Geography is brief-level only:** Sydney, Melbourne, QLD statewide, ACT; regional NSW and VIC out. No Notion ruling confirms it, and the Integrators page lists geography as an open decision.
15. **Membership directories as a sourcing channel** are untested hypotheses (Law Society, LIV, QLS, ALPMA, Doyle's). The NSW Bar Association listed there conflicts with the law brief's barrister exclusion.
16. **`aged-care` versus "aged care":** the scraper's segment token is hyphenated, but house style is `AgedCare` in campaigns and "aged care" in tags and filenames. Rule a pipeline token.
17. **ICP_Master hygiene:** cell A1 on Master and Holding holds pasted prompt text, not a header.
