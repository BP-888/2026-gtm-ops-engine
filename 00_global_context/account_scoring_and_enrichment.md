# Account Scoring, Tiering and Enrichment

**Purpose:** the operating rules for tiering ERMOS target accounts, mapping their buying committee, and enriching and verifying them before any outreach.

- Synthesised 2 Oct 2026 from Notion Ermos HQ and Google Drive. Updated 2 Oct 2026 with Brad's rulings, cited as "Brad ruling, 2 Oct 2026 [R-02OCT]"
- Status: **Draft for Brad's review**
- Precedence: R-02OCT overrides the Notion 05 Decisions Log wherever they conflict. Otherwise Notion Ermos HQ (05 Decisions Log first) overrides Drive. Drive briefs are cited only where Notion has no equivalent and nothing later supersedes them.
- Scope: account scoring and enrichment only. Copy scoring (the 100-point copy mandate, 9 Sep, Drive `09 copy-scoring-mandate.md` 1e6XXx_j6NEDtuo7MEky5oULzLqHS7Y7r) scores copy, not accounts. Do not mix the two.

---

## 1. Governing constraints (apply before any tiering)

| Rule | Value | Source |
|---|---|---|
| Products | ERMOS Edge (cloud, Australian SOC 2 server) and ERMOS Dominion (on site unit). Both active. ERMOS AI replaces ERMOS IQ | 05 Decisions Log, 16 Sep: https://app.notion.com/3dd77626a8098164a50bf4eaf6296ba2 and https://app.notion.com/3dd77626a80981df8ddcee4583482ecc |
| Outbound size band | **Any ICP firm with 1 to 50 staff.** Sweet spot 10 to 50. Firms with 1 to 9 staff are in scope as Tier 3 | R-02OCT |
| Over 50 staff | Disqualified, do not contact. Not a tier, not parked | R-02OCT; Campaign Naming Standard v3.0: https://app.notion.com/p/3de77626a80981359117c6e9c0c1b53b |
| Approved verticals | accounting, law, aged care, healthcare, finance. Full words only (`AgedCare` in campaign names) | 24 Sep ruling; Campaign Naming Standard v3.0 |
| Edge commercial terms | A$99 per seat per month, 10-seat minimum (a commercial term, not a targeting floor) | 05 Decisions Log, 24 Sep: https://app.notion.com/3e577626a80981849c3ee2c7aa1f457f |
| Dominion pricing | Per seat model (28 Sep). Pricing is not used in scoring and never appears in cold copy | https://app.notion.com/19294104ed9a4ae185badaaf7c2e3033; Hormozi Standard s.5 |
| Unresolved headcount | No tier until verified on the firm's own website. Hold the row; never default it into a tier | R-02OCT; Campaign Naming Standard v3.0, s.3 |
| Dominion claim | Described as **air-gapped**: no egress, so no documentation or data can flow out; only inbound pings for health checks and inbound patch updates are permitted | R-02OCT |
| Enrichment tools | None locked in. Tested at each step during implementation, then chosen (section 6) | R-02OCT |
| Governance | Read Approved pages only; log the SOP version used; agent-found issues go to 06 Proposed Changes | 00. Master System Brief, s.5: https://app.notion.com/p/fed5a5b00a4f4e419bba969ead145643 |

**Implementation task: re-map cohorts to tiers.** The `1-4` / `5-30` / `31-50` cohorts and `cohortFor()` (set 9 Sep, Drive `01 icp-brief.md` 1tOyvw9jvBVPLEQESyHUg-Gc7M8LEjH5t) map to Tier 3 / Tier 1 / Tier 2. Re-tier on verified staff count, because `5-30` also holds 5 to 9 staff firms, which are Tier 3. Still to update: `cohortFor()` code, the Campaign Naming Standard v3.0 size token and link tags, the ICP_Master `Tier` column and Legend, and the `Holding` tab definition. The Notion `01. ICP Master Database` Firm Size property (`10–15`, `16–30`, `31–45`, `46–50`; collection://9adc880f-b801-4414-b4ed-3f17e9c7065e) nests inside Tiers 1 and 2 and needs a 1 to 9 value. This is implementation work, not an open conflict.

---

## 2. Tier definitions

**Account tier = size only** (R-02OCT). Staff count is verified on the firm's own website.

| Tier | Verified staff | Notes |
|---|---|---|
| **Tier 1** | 10 to 30 | Sweet spot |
| **Tier 2** | 31 to 50 | Sweet spot |
| **Tier 3** | 1 to 9 | In scope |
| No tier | Unverified | Held until verified; not counted |
| Disqualified | Over 50 | Do not contact |

Boundaries at exactly 10 and 30 await Brad's confirmation (Open conflicts 1). No numeric score is used.

**Core fit (qualification, all verticals)** is a pass/fail gate before tiering. Each item needs recorded evidence:
1. Verified staff count of 1 to 50, counted on the firm's own site (R-02OCT; ICP_Master Legend "Staff count").
2. Onshore delivery, with no offshore production team (vertical briefs, s.3).
3. Regulated practice, confirmed on a register or badge (see 2.2).
4. In region. The briefs use Sydney, Melbourne, Queensland statewide and Canberra/ACT, with regional NSW and VIC out unless approved (Drive `01-icp-accounting-advisory-au` 1Q-hfFrcGo8rLJo9cEXPmMyYRhZuQeutlD9fuhyra4y4, s.2.2). Geography has no Notion ruling yet (Open conflicts 6).
5. Not disqualified (section 4) and independently owned, with local purchasing authority.
6. A named decision maker. A real person with a title, not `info@`.

**Hold, do not guess:** staff count unconfirmed; fee-earner-only, practitioner-only or adviser-only team page (record provisional count); generic contact only; ownership or licensee status ambiguous; site unreachable or no team page. These rows go to `Holding` or the Uncertain review queue until resolved (vertical briefs, s.7).

### 2.1 Amplifying signals by vertical

These are **not tier criteria**. They feed signal tracking and awareness scoring, and set outreach priority within a tier and sub-vertical (R-02OCT).

| Vertical | Amplifiers | Source |
|---|---|---|
| Accounting | Audit or SMSF services named; named workpaper software; seasonal or contract job ad; public statement on data security, privacy, sovereignty or AI caution; multi-partner structure | `01-icp-accounting-advisory-au` s.7 |
| Law | Core practice in commercial litigation, M&A/due diligence, construction, insurance or estates disputes; identified practice or document management system; job ads for solicitors, paralegals or law clerks; public statement on privilege, confidentiality, sovereignty or AI caution; multi-partner structure | Drive `02-icp-law-advisory-au` 10XLzsk39YnxpgBegs8-sE2q_oLjaC2KEVGGlaLPwqT4, s.7 |
| Healthcare | AGPAL/QPA accreditation; published policy or patient information set; NDIS, WorkCover, CTP, insurer or court reporting; high referral or correspondence volume; accredited teaching or registrar practice; named practice manager or practice manager job ad; ambient AI scribe in use; multi-practitioner independent structure | `03-icp-healthcare-au` 1x7aMiGMR4b3nfuJm1QHlEsRswjl-ImfWcxVC8Xxv1_8, s.7 |
| Finance (advice practices) | Self-licensed (own AFSL); ongoing service or annual review offering; paraplanner on staff or advertised; Professional Year supervision; SOA production evident; own research library or APL; AI meeting-note tool in use; multi-adviser independent structure | Drive `04-icp-financial-advisers-au` 183zuJGyNBb3HhzVvZbJrouFRu6dCZ0E8C2NLybvyzEM, s.7 |
| Aged care | Pending: T-001 (repo root `TASKS.md`) | T-001 |
| Partner ICP (integrators, MSPs; partner recruitment, not end customers, so no R-02OCT tier) | Healthcare or legal client evidence; ISO 27001 / Essential Eight / sovereignty language; Microsoft Solutions Partner; Copilot or LLM resale; founder-led AI thought leadership. Status Draft | Notion `07 Integrators & MSPs`: https://app.notion.com/p/3eb77626a8098175b5a9f41d4f8f2e5d |

**Data-sovereignty mindset** (privacy page specifying onshore hosting, or posts on sovereignty, on premises or privilege and AI) is rare but the strongest signal in accounting and law: prioritise first within the tier (accounting brief s.5; law brief s.5).

### 2.2 Regulatory verification (part of core fit)

| Vertical | Hard check |
|---|---|
| Accounting | TPB registration and/or CA ANZ, CPA Australia, IPA or SMSF Association badge (accounting brief s.6) |
| Law | Regulator public register (Law Society of NSW, Victorian Legal Services Board & Commissioner, Queensland Law Society, ACT Law Society), not a website badge (law brief s.6) |
| Healthcare | Ahpra public register, with at least one named practitioner (healthcare brief s.6) |
| Finance | ASIC Financial Advisers Register. Done **first**, before any contact enrichment. Returns licensee status (finance brief s.1.1, s.6) |

### 2.3 Numeric scoring

None. Tier is size only and signals set priority within a tier (R-02OCT). Legacy schemes are listed under Excluded.

---

## 3. Firmographic and technographic criteria

**Firmographic** (record facts, with evidence):
- Staff count, counted as **total people at the site**, not fee-earners. Law sites often list lawyers only; GP and specialist sites list clinicians only (contractors included); advice practices list advisers only. Record both numbers where they differ, and mark provisional where total staff is not determinable (law s.2.1; healthcare s.2.3; finance s.2.3).
- Vendor headcount (Apollo, Clay or any other tool) is indicative only. The firm's own team or about page is the source of truth (ICP_Master Legend; all briefs).
- Ownership and structure. Independent, multi-partner, multi-office (principal office in region). In healthcare, check corporate ownership **first** (footer, privacy policy, careers portal). In finance, record licensee status and licensee name on every row (healthcare s.3.1; finance s.2.1).
- Service mix and sub-vertical (healthcare priority: GP, then specialist, then allied health; s.2.1).
- Jurisdiction. Fixed values NSW / VIC / QLD / ACT, populated on every row. **No statutory citations in any cell** (law s.10.3; healthcare s.10.3; finance s.10).

**Technographic** (record product, do not interpret in the row):

| Vertical | Stack to capture | Source |
|---|---|---|
| Accounting | Xero, MYOB, Class Super, BGL Simple Fund 360, CaseWare, Xero Workpapers, MYOB AE/AO, Reckon APS, Access HandiSoft, Karbon, FYI Docs, Suralink, AuditDashboard, Dext, Hubdoc, WorkflowMax | accounting brief s.5; ICP_Master "Segment signals" |
| Law | PMS product **and** deployment (cloud native: LEAP, Smokeball, Clio, Actionstep, hosted NetDocuments; server based: FilePro, LawMaster, Affinity, Practice Evolve, on premises iManage). Neither side is filtered out | law brief s.5.1 |
| Healthcare | Clinical software **and** deployment (server based: Best Practice, Medical Director, Genie, Zedmed, Shexie; cloud: Bp Omni, Helix, Gentu, Clinic to Cloud, Halaxy, Cliniko, Nookal, Power Diary, Coreplus, Splose); ambient scribe (Heidi, Lyrebird, Patientnotes) | healthcare s.5.1, s.5.2 |
| Finance | Advice software (Xplan, AdviceOS, AdviserLogic, Plutosoft, WealthO2, Practifi, Salesforce FSC, Class); AI note tool (Jump, Zocks, Finmate). No deployment split expected | finance s.5.1, s.5.2 |
| All | M365 or Copilot evidence from job ads or LinkedIn, with source. Vendor tech data on small AU firms is thin and stale: **never assert Copilot from it** | all briefs, s.5 |

Signal bucket for this repo's pipeline: technographic, job-ad and people-data signals are 3rd-party signals (CLAUDE.md, Signal Tracking).

---

## 4. Disqualifiers

**Hard (log every exclusion with reason and evidence; never delete the log)**, from ICP_Master Exclusions tab and briefs s.3:
- Over 50 staff (R-02OCT; Campaign Naming Standard).
- Offshore production (accounting, legal drafting or review, transcription or scribing, paraplanning).
- Not regulated: bookkeeping-only, vCFO or coaching with no registration, unlicensed finance businesses.
- Roll-ups, national networks and associations; branch offices whose purchasing sits elsewhere; Big 4 and large mid-tier.
- Corporate-owned clinics; public hospitals, LHDs and HHSs; private hospital groups; telehealth-only platforms (healthcare s.3).
- Licensees and dealer groups (tested at every size); bank, insurer or platform owned advice; product manufacturers; robo-advice (finance s.3.1).
- Barristers and chambers; in-house legal teams; community legal centres (law s.3).
- Core-functionality fail: payments, fintech, crypto, software or lending companies with finance labels, which go to the partner track, not prospects; AI tools for advisers, which are a competitor signal; non-AU firms (Drive `ermos-smartlead-icp-profiles.md` 1TkXN2edcqzvXpIl1GIxyav0RiO0Vuhij, shared disqualifiers; Clay validation doc, Step 5).
- **Publicly committed to running client data through a public cloud LLM, on public evidence only.** AI curiosity, AI policies, scribes and note tools are **not** disqualifiers (all briefs, s.3 guard).
- Healthcare: never qualify on clinical AI, diagnostics, triage or decision-support interest (healthcare s.0, s.5).

**Route, do not discard:** standalone conveyancers, aged care and NDIS providers (from the healthcare build), pharmacy, mortgage brokers and insurance brokers each go to their own holding file with name, website, city and staff count only (law s.3.1; healthcare s.2.1; finance s.3).

**Contact-level:** records with `email_status: guessed` or a missing consent basis never go to Smartlead (`ermos-smartlead-icp-profiles.md`, shared disqualifiers).

**Aged care disqualifiers:** pending: T-001.

---

## 5. Buying committee and stakeholder map

Mapped to this repo's Decision Maker / Influencer / Champion roles. Base roles come from Drive `01 icp-brief.md` (Buying committee), with vertical variants from the briefs.

| Repo role | ERMOS role | Typical titles | Vertical notes |
|---|---|---|---|
| **Decision Maker** | Economic buyer | Managing Partner, Partner, Director, Principal, Owner | Law: Legal Practice Director is the statutory title in incorporated practices, so search it explicitly (law s.4). Finance: Principal/Director; Responsible Manager signals self-licensing (finance s.2) |
| **Champion** | Operational champion | Practice Manager, General Manager, Operations Manager, COO | **Healthcare: Practice Manager is first contact, not fallback** (healthcare s.2). Law: Practice Manager is the operational decision maker above about 12 staff (law s.4) |
| **Influencer** | Technical evaluator | IT provider or MSP, internal IT lead (`IT_Specialists`: IT Manager, Systems Administrator, Head of Technology, Practice Systems Manager) | Engage after interest exists, never as the first commercial target (`01 icp-brief.md`). Campaign job value `IT_Specialists` was ruled for the `31-50` cohort only, i.e. Tier 2 after re-mapping (Campaign Naming Standard s.4) |
| **Influencer** | Workflow validator | Senior Manager, Senior Accountant, Client Manager | Accounting job values `Senior_Accountants`, `Client_Managers` (Campaign Naming Standard s.4) |
| **External approver** | Licensee (finance, authorised representatives only) | Licensee's approved-tools owner | Not a contact to source. Record licensee name; it is the approval gatekeeper (finance s.2.1) |

Contact rules:
- Two contacts per firm where available: one Partner/Principal level, one Practice Manager level. Healthcare reverses the order (all briefs, s.4).
- Roughly one contact per five staff, capped at five per firm. Never send identical messaging to several people in the same firm at the same time (`01 icp-brief.md`, Contact strategy).
- Job values other than accounting's are not yet ruled per vertical (Campaign Naming Standard s.4). See Open conflicts 4.

---

## 6. Enrichment workflow

Notion sets an eight-step engine (00. Master System Brief, s.2). This is the tiering and enrichment slice of it, with the Drive verification rules layered in. **No tool is locked in** (R-02OCT): each step states what it must achieve, and tools are tested at that step during implementation before one is chosen.

**Principles (whatever the tool):** verify facts on the firm's own website; never trust a vendor field alone; waterfall to maximise find rate at the lowest cost; deduplicate on domain; bounce-check before any send; human approval before outreach; blank is a correct answer.

| # | Step | Rule | Source |
|---|---|---|---|
| 1 | Source candidates | Saved searches per metro and size bucket, or raw discovery by segment × suburb. Raw discovery writes CSV only, with no enrichment or contact data | Master Brief s.2; accounting brief s.4; SOP `leadgen-google-scraper` v0.1: https://app.notion.com/p/3dd77626a809812993b3c14047080fb7 |
| 2 | Dedup | On **domain**, across all segments, before any spend. If present, append to `Segment(s)` (semicolon separated) and fill blanks; never add a row. `Source segment` never changes. Finance: also check accounting rows by trading name and street address before enriching | ICP_Master Legend; finance s.1.1 |
| 3 | Register check | Regulator lookup first where one exists (ASIC first for finance). If it fails, stop and spend nothing further | section 2.2 |
| 4 | Website verification | Staff count, ownership, service mix and onshore status from the firm's own site. Record the **URL or exact phrase**, never yes/no. A firm never reaches the list on vendor data alone | ICP_Master Legend; briefs s.1.1, s.6 |
| 5 | AI qualification | Agent checks against the ICP (regulated Australian firm in an approved vertical, 1 to 50 verified staff; over 50 fails) and returns strict Pass/Fail with a machine-readable JSON reason | Master Brief s.2 step 3, s.3 Phase 2; R-02OCT |
| 6 | Tier | Size only: Tier 1 (10–30), Tier 2 (31–50), Tier 3 (1–9). Unverified count or unresolved core fit goes to `Holding`, no tier, not counted | R-02OCT |
| 7 | Contact enrichment | Waterfall to verified contact data on qualified firms only, maximising find rate while minimising cost and duplicate calls | Master Brief s.2 step 4, s.3 Phase 3 |
| 8 | Cross-check | Existing record vs vendor data vs ERMOS website research. Flag missing, conflicting, wrong domain, wrong headcount, too-junior contacts and keyword-only fits. **No approval on a vendor industry label alone** | Clay validation doc 1buWcKE0tGwN5sbYNw6gkD7WAFUoY-p4G |
| 9 | Deliverability | Bounce check before enrolment. Email status values: Verified, Validated, Unverified, Guessed, Catch-all, Unavailable. **Never fabricate an address** | Master Brief s.2 step 5; Clay validation doc |
| 10 | Derive personalisation | `observation`, `workflow`, `stack` (section 7) | `ICP_MasterDerivedColumns20.md` |
| 11 | Review queue | Approved: Ready for Brad / Rejected: Recorded for Learning / Uncertain: Brad Review Required / Partnership Opportunity / Data Problem / Approved for Smartlead Export / Held: Contact Data Not Adequate | Clay validation doc |
| 12 | **Human approval** | No record is `Ready for Smartlead` without Brad's approval. No live import, sequence activation or sending without explicit approval. "Nothing ships without Brad's approval" | Clay validation doc; Hormozi Standard s.8: https://app.notion.com/p/3de77626a809816a834cd1a767b93ee3 |
| 13 | Export | `SMARTLEAD_<Vertical>_<Size>_<Job>_vN.csv` with `segment` and `tag` columns, matching the campaign name character for character | Campaign Naming Standard v3.0 |

**Candidate tools under test** (not the stack): sourcing: Apify Google Maps scraper, Apollo, LinkedIn Sales Navigator; firm and contact enrichment: Apollo, Clay, BetterContact; deliverability: ZeroBounce. Record which tool supplied each value so results can be compared before a choice is made.

Run discipline: batch = one metro × one employee bucket (× sub-vertical in healthcare). Checkpoint to the master after each batch. If tool credits run out, stop and report; never substitute unverified rows. On shortfall, stop and flag; never widen geography, size or vertical to hit a number (briefs s.1.1, s.9). A blank cell is a correct answer; never fabricate a signal (briefs s.5).

**SOP gate:** 03 SOPs holds no Enrichment SOP. The only Lead Gen SOP (`leadgen-google-scraper`) is Approved in the database but its callout still says DRAFT, and it is logged as BLOCKED in 06 Proposed Changes (https://app.notion.com/p/b27a0ff8f47e45759471c49b3cd87c2a). Under Master Brief s.5 rule 1, this workflow has no Approved SOP to execute against yet.

---

## 7. Derived personalisation columns

Source: Drive `ICP_MasterDerivedColumns20.md` (1jKimSrCry1HlVY3-NNleygG3qbH1dk1ju3VZONmgQHI).

| Column | Derived from | Fallback (always a full sentence) |
|---|---|---|
| `observation` | Staff count, Signals found, Services, Professional body | "Client files are the part of the practice that cannot be casually moved." |
| `workflow` | Services | "It works from the workpapers and letters your practice already produces." |
| `stack` | Segment signals (software) | "It sits alongside whatever your practice already runs rather than replacing any of it." |

Rules:
- Every value is a complete sentence, not a token swap.
- **Assert nothing the `Verification evidence` column does not already carry.**
- Zero hyphens and dashes, consistent with the 29 Sep ruling: https://app.notion.com/3ea77626a8098173946ece02b5b08876.
- A row with no signal is a **thin row**. Its observation comes from the services mix; flag it for a short manual site check before send.
- Merge contract fields: `firm`, `domain` (join key), `first`, `full`, `title`, `email`, `staff`, `tier`, `observation`, `workflow`, `stack`, `stack_is_fallback`, `derived_from`, `a1_words`, `a2_words`, `a3_words`.
- In the 20-firm pilot only 10 of 20 had a named stack. The software signal is the most valuable field to backfill.

The column mechanism stands. The sequence copy those columns were written into (Aug, "Variant A") predates the Hormozi Standard and is not current copy. See Excluded.

---

## 8. Enrichment output schema

**Base (ICP_Master `Master` sheet, columns A to X, one row per firm, contacts as columns):**
Firm name · Domain · Website · Segment(s) · Source segment · City / Region · Staff count · Services · Professional body · Segment signals · M365 or Copilot evidence · Contact 1 name · Contact 1 title · Contact 1 email · Contact 1 LinkedIn · Contact 2 name · Contact 2 title · Contact 2 email · Contact 2 LinkedIn · Signals found · Tier · Verification evidence · Notes / exclusion reason · Batch

Companion sheets: `Holding` (same columns) and `Exclusions` (Firm name, Domain, Segment, Exclusion reason, Evidence, Batch).

**Vertical extensions** (add as columns; populate on every row of that vertical):

| Vertical | Extra columns |
|---|---|
| All non-accounting | Segment, Tier, Jurisdiction (NSW/VIC/QLD/ACT) |
| Law | Fee-earner count, Practice areas, Regulator register confirmed (Y/N + URL), PMS product, PMS deployment |
| Healthcare | Sub-vertical, Ownership, Practitioner count, Total staff, Workload signals, Accreditation, Ahpra verification, Clinical software, Deployment, Ambient scribe |
| Finance | Licensee status, Licensee name, Adviser count, Total staff, ASIC register verification, Workload signals, Advice software, AI note tool, Professional membership |

**Validation and operational fields** (adapted from the Clay validation doc, tool-agnostic): Enrichment source (tool per value), Vendor company name, Vendor domain, Vendor industry, Vendor employee count, ERMOS validated industry, ERMOS employee estimate, ERMOS core-functionality description, Data agreement status, Data conflict notes, Vendor enrichment confidence, ERMOS research confidence, Final ICP classification, Recommended action, Email-verification status (per contact), Contact priority, Contact rationale, Human approval status, Ready for Smartlead, Smartlead import status, Campaign status, Last updated.

**Derived:** observation, workflow, stack, stack_is_fallback, derived_from (section 7).

**Not yet in schema:** an Awareness stage column (Identified to Selecting, CLAUDE.md) and a Smartlead sent / not sent indicator. Brad asked for the second in the ICP_Master sheet itself. See Open conflicts 7.

**`Tier` column:** Tier 1 / Tier 2 / Tier 3 by verified staff count (R-02OCT); blank while held. Currently still holds A/B/C (implementation task, section 1).

---

## Excluded as superseded

- **24 Sep "outbound strictly 10 to 50" rule**, and treating under-10 firms as outside outbound (05 Decisions Log, 24 Sep). Superseded by R-02OCT (1 to 50; sub-10 firms are Tier 3).
- **Tier A / B / C** (core fit plus amplifier) as the account tier (ICP_Master Legend). Superseded by R-02OCT (size-only tiers). The amplifier lists are kept as signals (section 2.1).
- **All numeric account scores:** the accounting `/15` priority score (`01 icp-brief.md`, 9 Sep) and the Aug Clay validation 0 to 100 "starting framework". Superseded by R-02OCT.
- **Fixed enrichment stack:** BetterContact then Apollo plus ZeroBounce (Master System Brief) and Clay as primary enrichment (Aug Clay project). Superseded by R-02OCT (candidate tools under test, section 6).
- **21 Sep retirement of "air-gapped"** as an ERMOS claim (https://app.notion.com/3e277626a80981f4b844e7811f42671b) and the related guardrails. Superseded by R-02OCT (air-gapped, no-egress definition).
- **1 to 50 cap with the `1-4` / `5-30` / `31-50` bands as the size vocabulary** (`01 icp-brief.md`, 9 Sep; template brief 1M_gBaxgukgVJn-ha385d4zbxA0H7udGP). Replaced by R-02OCT tiers (re-map, section 1). Earlier 15 to 100 and "10 to 100 seat target market" figures are also superseded.
- **Core 5 to 30 band, Micro 1 to 4 cohorts and the 500-firm targets** in the four Aug vertical briefs, and ICP_Master `Holding` treating 31 to 50 as "above the band". Superseded by R-02OCT.
- **Dominion "AUD $2,599 + GST per month", "up to 30 staff", "Dominion Core (up to 15 staff)", flat-fee "no per-seat licences" framing** (icp-brief, healthcare and finance briefs, Aug profiles). Superseded by 24 Sep and 28 Sep pricing rulings.
- **ErmosIQ / ERMOS IQ** naming. Now ERMOS AI.
- **Aug Smartlead profiles' copy decisions**: neutral "Ermos team" sender, no-fear framing, P1/P2/P3 campaign profiles. Superseded by the Hormozi Standard (29 Sep) and Campaign Naming Standard v3.0. Its disqualifier list is retained above.
- **Derived-columns sequence copy** (sign-off, "one pager" CTA, Dominion "hardware sits in your office" mechanism). Superseded by Hormozi Standard s.5. The column method is retained.
- **Archived Notion `00.archive admin..00`** (Sales & Market Intelligence, Runbooks). Excluded per Master Brief s.5.

---

## Open conflicts / gaps for Brad

1. **Tier boundaries.** Brad wrote 10–30 / 30–50 / 1–10, which overlap. This file applies 1–9 / 10–30 / 31–50. Confirm the boundary at exactly 10 staff (Tier 3 or Tier 1) and at exactly 30 (Tier 1 or Tier 2).
2. **Governed pages still carry the old rules.** The Notion 05 Decisions Log (24 Sep 10 to 50 rule; 21 Sep air-gapped retirement) and the Campaign Naming Standard v3.0 (`1-4` / `5-30` / `31-50` cohorts) need updating to match R-02OCT via 06 Proposed Changes. So do the Master System Brief (fixed enrichment stack; four verticals listed, aged care omitted) and Hormozi Standard s.8 (forbids "air-gapped", now contradicting R-02OCT and its own s.2).
3. **Dominion air-gapped, technical check.** Will to confirm Dominion's network configuration matches the strict no-egress definition: health-check replies and patch retrieval must not open an outbound data path, so the air-gapped claim is defensible.
4. **Canonical ICP module is nearly empty.** Notion `01. ICP Master Database` holds only the Draft Partner ICP row, and `02 ICP & Sentiment` has no rows. Vertical ICPs live only in Aug Drive briefs. Campaign job values are ruled for accounting titles only.
5. **Dominion pricing check.** The Master Brief states Dominion at A$99 per seat with A$7,500 per 15-person box; confirm this matches the 28 Sep per-seat ruling.
6. **Geography** (Sydney, Melbourne, Queensland statewide, ACT; regional NSW and VIC out) comes only from Aug Drive briefs, with no Notion ruling.
7. **No Approved Enrichment SOP**, and the scraper SOP is BLOCKED (Approved status vs DRAFT callout). Also missing: an Awareness stage column and a Smartlead sent indicator in ICP_Master. ICP_Master cells A1 (Master and Holding) and C2 hold pasted prompt text instead of headers and data.
