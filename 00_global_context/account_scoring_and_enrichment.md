# Account Scoring, Tiering and Enrichment

**Purpose:** the operating rules for tiering ERMOS target accounts, mapping their buying committee, and enriching and verifying them before any outreach.

- Synthesised 2 Oct 2026 from Notion Ermos HQ and Google Drive
- Status: **Draft for Brad's review**
- Precedence: Notion Ermos HQ (05 Decisions Log first) overrides Drive. Drive briefs are cited only where Notion has no equivalent and nothing later supersedes them.
- Scope: account scoring and enrichment only. Copy scoring (the 100-point copy mandate, 9 Sep, Drive `09 copy-scoring-mandate.md` 1e6XXx_j6NEDtuo7MEky5oULzLqHS7Y7r) scores copy, not accounts. Do not mix the two.

---

## 1. Governing constraints (apply before any score)

| Rule | Value | Source |
|---|---|---|
| Products | ERMOS Edge (cloud, Australian SOC 2 server) and ERMOS Dominion (on site unit). Both active. ERMOS AI replaces ERMOS IQ | 05 Decisions Log, 16 Sep: https://app.notion.com/3dd77626a8098164a50bf4eaf6296ba2 and https://app.notion.com/3dd77626a80981df8ddcee4583482ecc |
| Outbound size band | **10 to 50 seats/staff, strictly.** Every list and campaign holds firms in this band only | 05 Decisions Log, 24 Sep, ruling 2: https://app.notion.com/3e577626a80981aca23bf476f648027b |
| Product sweet spot | 5 to 50 seats (commercial planning only, not an outbound filter) | same |
| Over 50 staff | Disqualified, do not contact. Not a cohort, not parked | Campaign Naming Standard v3.0: https://app.notion.com/p/3de77626a80981359117c6e9c0c1b53b |
| Approved verticals | accounting, law, aged care, healthcare, finance. Full words only (`AgedCare` in campaign names) | 24 Sep ruling; Campaign Naming Standard v3.0 |
| Edge commercial floor | A$99 per seat per month, 10-seat minimum | 05 Decisions Log, 24 Sep: https://app.notion.com/3e577626a80981849c3ee2c7aa1f457f |
| Dominion pricing | Per seat model (28 Sep). Pricing is not used in scoring and never appears in cold copy | https://app.notion.com/19294104ed9a4ae185badaaf7c2e3033; Hormozi Standard s.5 |
| Unresolved headcount | Not assignable. Hold the row; never default it into a band | Campaign Naming Standard v3.0, s.3 |
| Governance | Read Approved pages only; log the SOP version used; agent-found issues go to 06 Proposed Changes | 00. Master System Brief, s.5: https://app.notion.com/p/fed5a5b00a4f4e419bba969ead145643 |

**Re-banding required.** The `1-4` / `5-30` / `31-50` cohorts and `cohortFor()` (set 9 Sep, Drive `01 icp-brief.md` 1tOyvw9jvBVPLEQESyHUg-Gc7M8LEjH5t; still live in the Campaign Naming Standard v3.0 and link tags) do not express the 10 to 50 outbound rule. Under the current ruling, `1-4` is out entirely and `5-30` must be split at 10. The Notion `01. ICP Master Database` Firm Size property already carries `10–15`, `16–30`, `31–45`, `46–50` (collection://9adc880f-b801-4414-b4ed-3f17e9c7065e), but those values are not ruled as campaign cohorts. Until Brad rules, treat any firm under 10 verified staff as outside outbound, whatever cohort the legacy logic assigns. See Open conflicts 1.

---

## 2. Tier definitions

Canonical definition (Drive `ICP_Master`, Legend tab, 1cgunhz43AF45AReQm_IOSpdoI2L7MuTnx95icTH3INk):

| Tier | Definition | Counts toward segment target |
|---|---|---|
| **A** | Core fit plus at least one amplifying signal | Yes |
| **B** | Core fit, no amplifier | Yes |
| **C** | Right shape, something unresolved | No. Held in the same sheet |

**Core fit (all verticals)** means all of the following, each with recorded evidence:
1. Verified staff count of 10 to 50, counted on the firm's own site (24 Sep ruling; ICP_Master Legend "Staff count").
2. Onshore delivery, with no offshore production team (vertical briefs, s.3).
3. Regulated practice, confirmed on a register or badge (see 2.2).
4. In region. The briefs use Sydney, Melbourne, Queensland statewide and Canberra/ACT, with regional NSW and VIC out unless approved (Drive `01-icp-accounting-advisory-au` 1Q-hfFrcGo8rLJo9cEXPmMyYRhZuQeutlD9fuhyra4y4, s.2.2). Geography has no Notion ruling yet (Open conflicts 6).
5. Not disqualified (section 4) and independently owned, with local purchasing authority.
6. A named decision maker. A real person with a title, not `info@`.

**Tier C triggers:** staff count unconfirmed; fee-earner-only, practitioner-only or adviser-only team page; generic contact only; ownership or licensee status ambiguous; no workload signal (healthcare and finance); site unreachable or no team page ("Tier C, not a guess"). Sources: vertical briefs, s.7.

**Tiering runs within a band and sub-vertical, not across them** (law brief s.7; healthcare brief s.7).

### 2.1 Amplifying signals by vertical (any one lifts B to A)

| Vertical | Amplifiers | Source |
|---|---|---|
| Accounting | Audit or SMSF services named; named workpaper software; seasonal or contract job ad; public statement on data security, privacy, sovereignty or AI caution; multi-partner structure | `01-icp-accounting-advisory-au` s.7 |
| Law | Core practice in commercial litigation, M&A/due diligence, construction, insurance or estates disputes; identified practice or document management system; job ads for solicitors, paralegals or law clerks; public statement on privilege, confidentiality, sovereignty or AI caution; multi-partner structure | Drive `02-icp-law-advisory-au` 10XLzsk39YnxpgBegs8-sE2q_oLjaC2KEVGGlaLPwqT4, s.7 |
| Healthcare | AGPAL/QPA accreditation; published policy or patient information set; NDIS, WorkCover, CTP, insurer or court reporting; high referral or correspondence volume; accredited teaching or registrar practice; named practice manager or practice manager job ad; ambient AI scribe in use; multi-practitioner independent structure | `03-icp-healthcare-au` 1x7aMiGMR4b3nfuJm1QHlEsRswjl-ImfWcxVC8Xxv1_8, s.7 |
| Finance (advice practices) | Self-licensed (own AFSL); ongoing service or annual review offering; paraplanner on staff or advertised; Professional Year supervision; SOA production evident; own research library or APL; AI meeting-note tool in use; multi-adviser independent structure | Drive `04-icp-financial-advisers-au` 183zuJGyNBb3HhzVvZbJrouFRu6dCZ0E8C2NLybvyzEM, s.7 |
| Aged care | **None defined.** No aged care list-build brief found in Notion or Drive | Gap (Open conflicts 4) |
| Partner ICP (integrators, MSPs) | Tier A = core + healthcare or legal client evidence + one of ISO 27001 / Essential Eight / sovereignty language, Microsoft Solutions Partner, Copilot or LLM resale, founder-led AI thought leadership. Status Draft | Notion `07 Integrators & MSPs`: https://app.notion.com/p/3eb77626a8098175b5a9f41d4f8f2e5d |

**Data-sovereignty mindset** (privacy page specifying onshore hosting, or posts on sovereignty, on premises or privilege and AI) is rare but an instant Tier A in accounting and law (accounting brief s.5; law brief s.5).

### 2.2 Regulatory verification (part of core fit)

| Vertical | Hard check |
|---|---|
| Accounting | TPB registration and/or CA ANZ, CPA Australia, IPA or SMSF Association badge (accounting brief s.6) |
| Law | Regulator public register (Law Society of NSW, Victorian Legal Services Board & Commissioner, Queensland Law Society, ACT Law Society), not a website badge (law brief s.6) |
| Healthcare | Ahpra public register, with at least one named practitioner (healthcare brief s.6) |
| Finance | ASIC Financial Advisers Register. Done **first**, before any contact enrichment. Returns licensee status (finance brief s.1.1, s.6) |

### 2.3 Numeric scoring

**No ratified numeric account-scoring weights exist in Notion Ermos HQ.** Tiering is rule based (A/B/C above). Two legacy point schemes exist in Drive. Neither is ratified, and one is built on superseded bands (see Excluded and Open conflicts 2). Do not compute a points score for prioritisation until Brad rules one.

---

## 3. Firmographic and technographic criteria

**Firmographic** (record facts, with evidence):
- Staff count, counted as **total people at the site**, not fee-earners. Law sites often list lawyers only; GP and specialist sites list clinicians only (contractors included); advice practices list advisers only. Record both numbers where they differ, and mark provisional where total staff is not determinable (law s.2.1; healthcare s.2.3; finance s.2.3).
- Apollo headcount is indicative only. The firm's own team or about page is the source of truth (ICP_Master Legend; all briefs).
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
| All | M365 or Copilot evidence from job ads or LinkedIn, with source. Apollo tech data on small AU firms is thin and stale: **never assert Copilot from it** | all briefs, s.5 |

Signal bucket for this repo's pipeline: technographic, job-ad and people-data signals are 3rd-party signals (CLAUDE.md, Signal Tracking).

---

## 4. Disqualifiers

**Hard (log every exclusion with reason and evidence; never delete the log)**, from ICP_Master Exclusions tab and briefs s.3:
- Over 50 staff (Campaign Naming Standard). Under 10 staff for outbound (24 Sep ruling).
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

---

## 5. Buying committee and stakeholder map

Mapped to this repo's Decision Maker / Influencer / Champion roles. Base roles come from Drive `01 icp-brief.md` (Buying committee), with vertical variants from the briefs.

| Repo role | ERMOS role | Typical titles | Vertical notes |
|---|---|---|---|
| **Decision Maker** | Economic buyer | Managing Partner, Partner, Director, Principal, Owner | Law: Legal Practice Director is the statutory title in incorporated practices, so search it explicitly (law s.4). Finance: Principal/Director; Responsible Manager signals self-licensing (finance s.2) |
| **Champion** | Operational champion | Practice Manager, General Manager, Operations Manager, COO | **Healthcare: Practice Manager is first contact, not fallback** (healthcare s.2). Law: Practice Manager is the operational decision maker above about 12 staff (law s.4) |
| **Influencer** | Technical evaluator | IT provider or MSP, internal IT lead (`IT_Specialists`: IT Manager, Systems Administrator, Head of Technology, Practice Systems Manager) | Engage after interest exists, never as the first commercial target (`01 icp-brief.md`). Campaign job value `IT_Specialists` was ruled for `31-50` only (Campaign Naming Standard s.4) |
| **Influencer** | Workflow validator | Senior Manager, Senior Accountant, Client Manager | Accounting job values `Senior_Accountants`, `Client_Managers` (Campaign Naming Standard s.4) |
| **External approver** | Licensee (finance, authorised representatives only) | Licensee's approved-tools owner | Not a contact to source. Record licensee name; it is the approval gatekeeper (finance s.2.1) |

Contact rules:
- Two contacts per firm where available: one Partner/Principal level, one Practice Manager level. Healthcare reverses the order (all briefs, s.4).
- Roughly one contact per five staff, capped at five per firm. Never send identical messaging to several people in the same firm at the same time (`01 icp-brief.md`, Contact strategy).
- Job values other than accounting's are not yet ruled per vertical (Campaign Naming Standard s.4). See Open conflicts 5.

---

## 6. Enrichment workflow

Notion sets an eight-step engine (00. Master System Brief, s.2). This is the scoring and enrichment slice of it, with the Drive verification rules layered in.

| # | Step | Rule | Source |
|---|---|---|---|
| 1 | Source candidates | Apollo saved searches per metro and employee bucket, or Sales Navigator + Apollo. Google Maps via Apify is a separate SOP that writes raw CSV only, with no enrichment or contact data | Master Brief s.2; accounting brief s.4; SOP `leadgen-google-scraper` v0.1: https://app.notion.com/p/3dd77626a809812993b3c14047080fb7 |
| 2 | Dedup | On **domain**, across all segments. If present, append to `Segment(s)` (semicolon separated) and fill blanks; never add a row. `Source segment` never changes. Finance: also check accounting rows by trading name and street address before enriching | ICP_Master Legend; finance s.1.1 |
| 3 | Register check | Regulator lookup first where one exists (ASIC first for finance). If it fails, stop and spend nothing further | section 2.2 |
| 4 | Website verification | Staff count, ownership, service mix and onshore status from the firm's own site. Record the **URL or exact phrase**, never yes/no. A firm never reaches the list on Apollo data alone | ICP_Master Legend; briefs s.1.1, s.6 |
| 5 | AI qualification | Agent checks against the ICP (regulated Australian firm, 10 to 50 staff) and returns strict Pass/Fail with a machine-readable JSON reason | Master Brief s.2 step 3, s.3 Phase 2 |
| 6 | Tier | A / B / C per section 2. Firms outside the band or ambiguous go to the `Holding` sheet for Brad, not counted | ICP_Master Legend |
| 7 | Contact enrichment | Waterfall to verified contact data, maximising find rate while minimising API cost and duplicate calls. Clay is named as primary enrichment in the Aug project; Notion names BetterContact then Apollo (Open conflicts 3) | Master Brief s.2 step 4, s.3 Phase 3; Clay validation doc 1buWcKE0tGwN5sbYNw6gkD7WAFUoY-p4G |
| 8 | Three-way comparison | Existing record vs Clay vs ERMOS website research. Flag missing, conflicting, wrong domain, wrong headcount, too-junior contacts and keyword-only fits. **No approval on a Clay industry label alone** | Clay validation doc |
| 9 | Deliverability | ZeroBounce bounce check before enrolment. Email status values: Verified, Validated, Unverified, Guessed, Catch-all, Unavailable. **Never fabricate an address** | Master Brief s.2 step 5; Clay validation doc |
| 10 | Derive personalisation | `observation`, `workflow`, `stack` (section 7) | `ICP_MasterDerivedColumns20.md` |
| 11 | Review queue | Approved: Ready for Brad / Rejected: Recorded for Learning / Uncertain: Brad Review Required / Partnership Opportunity / Data Problem / Approved for Smartlead Export / Held: Contact Data Not Adequate | Clay validation doc |
| 12 | **Human approval** | No record is `Ready for Smartlead` without Brad's approval. No live import, sequence activation or sending without explicit approval. "Nothing ships without Brad's approval" | Clay validation doc; Hormozi Standard s.8: https://app.notion.com/p/3de77626a809816a834cd1a767b93ee3 |
| 13 | Export | `SMARTLEAD_<Vertical>_<Size>_<Job>_vN.csv` with `segment` and `tag` columns, matching the campaign name character for character | Campaign Naming Standard v3.0 |

Run discipline: batch = one metro × one employee bucket (× sub-vertical in healthcare). Checkpoint to the master after each batch. If Apollo credits run out, stop and report; never substitute unverified rows. On shortfall, stop and flag; never widen geography, band or vertical to hit a number (briefs s.1.1, s.9). A blank cell is a correct answer; never fabricate a signal (briefs s.5).

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
- A row with no amplifier is a **thin row**. Its observation comes from the services mix; flag it for a short manual site check before send.
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
| All non-accounting | Segment, Band, Jurisdiction (NSW/VIC/QLD/ACT) |
| Law | Fee-earner count, Practice areas, Regulator register confirmed (Y/N + URL), PMS product, PMS deployment |
| Healthcare | Sub-vertical, Ownership, Practitioner count, Total staff, Workload signals, Accreditation, Ahpra verification, Clinical software, Deployment, Ambient scribe |
| Finance | Licensee status, Licensee name, Adviser count, Total staff, ASIC register verification, Workload signals, Advice software, AI note tool, Professional membership |

**Validation and operational fields** (Clay validation doc): Clay company name, Clay domain, Clay industry, Clay employee count, ERMOS validated industry, ERMOS employee estimate, ERMOS core-functionality description, Data agreement status, Data conflict notes, Clay enrichment confidence, ERMOS research confidence, Final ICP classification, Recommended action, Email-verification status (per contact), Contact priority, Contact rationale, Human approval status, Ready for Smartlead, Smartlead import status, Campaign status, Last updated.

**Derived:** observation, workflow, stack, stack_is_fallback, derived_from (section 7).

**Not yet in schema:** an Awareness stage column (Identified to Selecting, CLAUDE.md) and a Smartlead sent / not sent indicator. Brad asked for the second in the ICP_Master sheet itself. See Open conflicts 7.

---

## Excluded as superseded

- **1 to 50 cap and the `1-4` / `5-30` / `31-50` bands as the outbound rule** (`01 icp-brief.md`, 9 Sep; template brief 1M_gBaxgukgVJn-ha385d4zbxA0H7udGP). Superseded by the 24 Sep 10 to 50 outbound rule. Earlier 15 to 100 and "10 to 100 seat target market" figures are also superseded by the same ruling's revision.
- **Core 5 to 30 band, Micro 1 to 4 cohorts and the 500-firm targets** in the four Aug vertical briefs, and ICP_Master `Holding` treating 31 to 50 as "above the band". Firms of 31 to 50 are now in band; firms under 10 are now out.
- **Accounting `/15` priority score** (`01 icp-brief.md`). Its size factor gave top points to 5 to 30 and points to 1 to 4.
- **Dominion "AUD $2,599 + GST per month", "up to 30 staff", "Dominion Core (up to 15 staff)", flat-fee "no per-seat licences" framing** (icp-brief, healthcare and finance briefs, Aug profiles). Superseded by 24 Sep and 28 Sep pricing rulings.
- **"Air-gapped" and "runs disconnected" as ERMOS claims** (Aug profiles, healthcare and law brief context). Retired 21 Sep: https://app.notion.com/3e277626a80981f4b844e7811f42671b. Prospect sites using the word remain a valid *signal*.
- **ErmosIQ / ERMOS IQ** naming. Now ERMOS AI.
- **Aug Smartlead profiles' copy decisions**: neutral "Ermos team" sender, no-fear framing, P1/P2/P3 campaign profiles. Superseded by the Hormozi Standard (29 Sep) and Campaign Naming Standard v3.0. Its disqualifier list is retained above.
- **Derived-columns sequence copy** (sign-off, "one pager" CTA, Dominion "hardware sits in your office" mechanism). Superseded by Hormozi Standard s.5. The column method is retained.
- **Archived Notion `00.archive admin..00`** (Sales & Market Intelligence, Runbooks). Excluded per Master Brief s.5.

---

## Open conflicts / gaps for Brad

1. **Size cohorts vs the 10 to 50 rule.** `cohortFor()`, the Campaign Naming Standard cohorts and link tags (`1-4`, `5-30`, `31-50`) still encode 9 Sep logic. The live roster includes `LIVE_Accounting_1-4_Decision_Makers_v1`. The Notion ICP Master Database offers `10–15 / 16–30 / 31–45 / 46–50`. Which cohort labels replace them, and do `cohortFor()` and the tags change together? Note also that 12 of the 20 pilot firms in `ICP_MasterDerivedColumns20.md` list fewer than 10 staff, so they fall outside outbound under the current rule.
2. **No ratified numeric account score.** Two unratified legacy schemes exist. One is the accounting `/15` score (superseded size factor). The other is the Aug Clay validation 0 to 100 "starting framework": industry 30, size 15, Australian location 10, regulated or sensitive data 15, document heavy 10, secure-AI need 10, decision makers available 5, evidence quality 5. Rule one, or confirm tiering stays purely A/B/C.
3. **Enrichment stack.** The Master Brief (Notion, 28 Sep) names a BetterContact then Apollo waterfall plus ZeroBounce. The Aug Clay project names Clay as primary enrichment. Which is current, and is Clay in or out?
4. **Aged care has no list-build brief**, no amplifiers, buyer roles or disqualifiers, despite being an approved vertical (24 Sep). The healthcare brief routes aged care and NDIS to a holding file. Separately, the Master System Brief callout lists only law, accounting, finance and healthcare.
5. **Canonical ICP module is nearly empty.** Notion `01. ICP Master Database` holds only the Draft Partner ICP row, and `02 ICP & Sentiment` has no rows. Vertical ICPs live only in Aug Drive briefs. Campaign job values are ruled for accounting titles only.
6. **Geography** (Sydney, Melbourne, Queensland statewide, ACT; regional NSW and VIC out) comes only from Aug Drive briefs, with no Notion ruling.
7. **No Approved Enrichment SOP**, and the scraper SOP is BLOCKED (Approved status vs DRAFT callout). Also missing: an Awareness stage column and a Smartlead sent indicator in ICP_Master. ICP_Master cells A1 (Master and Holding) and C2 hold pasted prompt text instead of headers and data.
8. **Minor:** Hormozi Standard s.2 still cites "Dominion: air-gapped in the client's office (C-002)", which contradicts its own s.8 and the 21 Sep retirement. Separately, the Master Brief states Dominion at A$99 per seat with A$7,500 per 15-person box; confirm this matches the 28 Sep per-seat ruling.
