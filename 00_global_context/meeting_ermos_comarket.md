# Meeting Ermos CoMarket: partner and co-marketing context

**Purpose:** the baseline for 2nd-party "Partner Signals" and warm intros: partner tiers and terms, named partners, co-marketing motions, lead ownership, and the meeting decisions behind them.
**Synthesised 2 Oct 2026 from Notion Ermos HQ, Google Drive and Wispr Flow. Updated 2 Oct 2026 with Brad's rulings [R-02OCT], his partner rulings [R-02OCT-P], partner agreement v0.8 and the 30 Sep meeting notes.**
**Status:** Draft for Brad's review.

> **Source note.** No record titled "Meeting Ermos CoMarket" exists. Searches covered Drive and Notion titles and content ("CoMarket", "co-market", "co-marketing", "partner", "Mitronics", "Mayweathers", "founding partner", "webinar") and Wispr Flow by keyword and date. Wispr Flow returned no meetings at all. This file is built from:
> (a) Notion 12 Partner Ecosystem and 05 Decisions Log rulings (24 Sep to 1 Oct 2026), which govern;
> (b) the action log extracted from the **"GTM & Partner Planning, 26 Aug 2026"** meeting (Drive `tasks.json`, id `11h0NPooJaPbEVNCm520nRt6Fywh41cqr`), the closest thing to a partner/co-marketing meeting record;
> (c) the two SLT Meeting #1 agendas (26 Aug) and the Founding Partner deck (27 Aug), for intent only. Their figures are mostly superseded (see the end of this file);
> (d) Brad's **"Meeting Notes, Wed 30th September"** email to David and Will (Gmail), the most recent partner and distribution meeting record.

> **Ground zero for partner rules [R-02OCT-P].** "ERMOS Partner Agreement - IT Reseller", **Draft v0.8, 30 Sep 2026** (Brad's package; read in full from the copy uploaded 2 Oct), as amended by Brad's partner rulings of 2 Oct 2026. Section 2 is built from that agreement and those rulings. Where Notion or older docs differ, section 2 wins.

> **Naming rule.** John A. and John Moustache are the same person. Internal docs (including this repo) use **John Moustache**. External and partner-facing docs use **John A.**

---

## 1. Rules that govern (canonical as at 2 Oct 2026)

All figures AUD, ex GST. Where an older doc disagrees, these win.

| Topic | Rule | Source |
|---|---|---|
| Products | Two products: **ERMOS Edge** (cloud, AU, SOC 2) and **ERMOS Dominion** (on-site). Dominion is **air-gapped**: no egress, and no documentation or data can flow out. Only inbound pings for health checks and inbound patch updates are permitted. | Brad ruling, 2 Oct 2026 [R-02OCT] (reverses the 21 Sep retirement); products per 05 Decisions Log (16 Sep) |
| Edge price | A$99/seat/month, 10-seat minimum. | 05 Decisions Log, "Hybrid pricing…partner ecosystem standard" (24 Sep), 3e577626-a809-81ac-a23b-f476f648027b |
| Dominion price | A$99/seat/month, 10-seat minimum (A$990). A$7,500 hardware per box. One box per 15 people. No upfront discount. No VIP price approved. | "Dominion per-seat pricing model" (28 Sep) |
| End-customer target | Firms of **1 to 50 staff**; sweet spot 10 to 50. Over 50 disqualified. Account tiers by size: **Tier 1 = 10–30, Tier 2 = 31–50, Tier 3 = 1–9**. Verticals: accounting, law, aged care, healthcare, finance. Healthcare and law are the immediate priority (30 Sep meeting notes). | [R-02OCT]; verticals "Hybrid pricing…" (24 Sep) |
| Partner ICP | IT integrators, MSPs, AI consultants, IT managers, cloud and Microsoft 365 specialists. Distribution now prioritises these over generic telco channels (30 Sep meeting notes). Approved integrator verticals: Healthcare and Law (prioritised), plus Accounting, Aged Care and Finance (added 1 Oct). Partner firm size **not ruled**. | 01 ICP Master, "07 Integrators & MSPs (Partner ICP)", 3eb77626-a809-8175-b5a9-f41d4f8f2e5d; Gmail "Meeting Notes, Wed 30th September" |

## 2. Partner tiers and terms

**Source of truth [R-02OCT-P]:** "ERMOS Partner Agreement - IT Reseller", **Draft v0.8, 30 Sep 2026** (Brad's package, uploaded 2 Oct), **as amended by Brad's partner rulings of 2 Oct 2026**. Where the rulings and v0.8 differ, the rulings win. The agreement text itself still needs updating to match (TASKS.md T-004). The Notion Partner Standard Terms are being updated to match this section.

### 2.1 IT Reseller: commercial terms

| Term | Rule | Source |
|---|---|---|
| Appointment | Non-exclusive reseller of ERMOS Edge and ERMOS Dominion in an agreed territory. No sub-resellers without ERMOS's written agreement. | v0.8 cl 2.1, 2.3, 6.2 |
| Commission | **25% of recurring software subscription Fees, for the life of the subscription**, when the partner takes on the client relationship. **Condition:** the partner provides a minimum level of ongoing service (a set number of hours, **number TBD**) to help the client and resolve tickets and issues in real time. If the service condition lapses, the commission condition is not met (consequence TBD). | Ruling 2 Oct (removes the 24-month Commission End Date in v0.8 cl 1.1, 8.1, D.1) |
| Fees definition | Recurring software subscription only. Excludes the Dominion unit, one-off hardware and third-party professional services. | v0.8 cl 1.1, D.7 |
| ERMOS-generated leads | Flat **15%** of subscription Fees when ERMOS passes the lead and the partner closes it, paid only while the partner stays on call as a managed service for a set number of hours (**number TBD**; managed service terms TBD). | v0.8 D.2 |
| Achievement bonus | Extra **5%** on first-year new subscriptions above **A$100,000 net new ARR**, rolling four quarters. | v0.8 D.4 |
| Invoicing | **ERMOS invoices every client directly** for the ongoing subscription and **remits the partner's commission monthly**. The partner-invoices / wholesale-rate option is retired. | Ruling 2 Oct (replaces v0.8 cl 2.2 partner form, 8.4(b), D.3 second half) |
| Dominion setup fee | A$1,000 one-off per Dominion unit the partner deploys (working assumption: one day of setup). When it is paid is TBD. | v0.8 cl 8.7, D.6, D.8 |
| Edge onboarding | No setup fee. Customers self-onboard. | v0.8 D.6 |
| Onboarding call | Mandatory 1-hour call for every customer, Edge and Dominion. Who runs it is TBD in v0.8. (The 1 Oct Notion ruling made the Edge induction call partner-run and unpaid.) | v0.8 cl 3, Sched C |
| Pricing | Partner negotiates within the **ERMOS pricing structure document** (covers 0–10 and 10–50 person firms; not published). Discounts agreed with ERMOS first. Price List changes need 30 days' notice before the next quarter. **The pricing structure document is not drafted** (TASKS.md T-002). | v0.8 cl 8.2, 8.3, D.9 |
| Additional work | Indicative A$500/day for work beyond standard setup (skills, advanced ingestion, extra onboarding help). Whether it's fixed, a floor or a guide is TBD. Under the invoicing ruling, it's unclear who invoices partner service work (see questions). | v0.8 D.10 |
| Late payment | 1.5% a month, or the legal maximum if lower | v0.8 cl 8.5 |
| After termination | Commission continues on existing Customer Agreements, unless terminated for partner breach | v0.8 cl 14.4 |

### 2.2 Partner service packages (v0.8 D.11)
ERMOS runs its own outbound marketing to direct customers to partners offering these packages. In internal docs they're called **service packages**, to avoid a clash with the account Tiers 1–3 in the scoring files.

| Package (v0.8 label) | What the customer gets | Pricing |
|---|---|---|
| Service package 1 ("Tier 1: Onboarding") | Basic onboarding beyond the automated onboarding and the 1-hour call | TBD |
| Service package 2 ("Tier 2: Workflows and systems") | Building out workflows and systems on ERMOS | Indicative A$500/day (to confirm) |
| Service package 3 ("Tier 3: Managed service") | Bespoke, always-on managed service | TBD (monthly fee or guideline) |

### 2.3 Deal registration and provisioning (ruling 2 Oct)
1. The partner registers a deal by **confirming the client with ERMOS**.
2. ERMOS **sets up the backend instance** for that client.
3. Everything for that client, including invoicing details, is managed through that instance. The instance is the system of record for the client, the partner attribution and the commission basis.
4. ERMOS may reject an Order on reasonable grounds, with reasons. An Order binds once the customer signs a Customer Agreement or a purchase order accepting its terms (v0.8 cl 3).

### 2.4 Referring partner and Managed Service Partner (ruled 24 Sep; check against v0.8)
- **Referring partner:** 25% for the life of the recurring subscription (eligible client: Edge 10+ seats or one Dominion unit). ERMOS owns the contract and bills the client. This is consistent with the 2 Oct invoicing ruling.
- **Managed Service Partner:** sets up skills and agents, invoices the client directly for services, and keeps 100% of service revenue. Indicative A$500/day. Delivery onshore in Australia only.
- v0.8 covers only the IT Reseller tier, so whether these two remain separate tiers or fold into the reseller agreement's service packages is an open question.

### 2.5 Rules for all partners
- Partners describe ERMOS using **approved Schedule B / Claims Register wording only**, and make no warranties beyond those authorised (v0.8 cl 5, 11.3).
- **Schedule B in v0.8 is out of date:** it says Dominion has "management telemetry out". Under [R-02OCT] Dominion is air-gapped (no egress, only inbound health pings and patch updates). Schedule B must be updated before issue (TASKS.md T-004).
- Partners are non-exclusive. ERMOS may appoint other partners. No volume of leads is committed (v0.8 cl 7).
- Privacy Act compliance and Data Incident notification on both sides (v0.8 cl 15).
- Variations must be in writing and confirmed on the ERMOS side by Will, David and Brad (v0.8 Part A s4).

## 3. Named partners and status

Only names already in company docs. No contact details here.

| Partner | Type | Status at 2 Oct 2026 | Source |
|---|---|---|---|
| **John Moustache** (external name: John A.) | Founding consultant. He is to act as the **hub, the central point of collaboration between AI consultants, managed service teams and IT integrators**. He is the technical authority at integrator briefings and the feedback channel at initial client meetings. | **Signing the partnership agreement.** He will present his intended level of involvement in the next week or two (from 2 Oct). The 24 Sep Notion draft (v0.1, referring + MSP, equity out of scope) is superseded by whatever he signs. On 30 Sep he was asked to propose his model (equity partner vs reseller/integrator) and to prioritise the Mayweathers proof of concept. | Brad ruling 2 Oct; Gmail "Meeting Notes, Wed 30th September"; 12 Partner Ecosystem 3e577626-a809-8141-be15-dcd82f494b6f |
| **Mitronics** (spelt "Metronics" in the 26 Aug action log) | ICT and hardware supplier, an old client of Will's, already selling screens and monitors into law firms. Named as the first MSP channel partner and installer. | Action: **Will to approach as a legal-sector channel partner, due 16 Sep** (T30). The Business Plan has a Mitronics webinar in M1 and reseller/delivery terms negotiated in M4–6. **No agreement or outcome found.** | `tasks.json` (GTM & Partner Planning, 26 Aug); "ERMOS Dominion — Business Plan" (Draft), 3de77626-a809-81d8-a1e2-d1ed86866e6f |
| **Mayweathers** | Law firm in a 90-day legal beta on Edge (a beta "partnership", **not a channel partner**). Its sandbox is where the A$500/day MSP rate is being tested. | SoW **Draft v1.1 (10 Sep)**, flagged stale by the 24 Sep pricing ruling. Planned as the first named case study. | Drive "Mayweathers 90-Day Legal Beta SoW v1.1", 1IAzuHe1b2-Dm5ZRRufd5j_ZwoER6IT3nAdHWx_MPY2I; "Hybrid pricing…" (24 Sep) |
| **D&L Partners** | Accounting firm in a 90-day accounting beta on Edge (beta customer, not a channel partner) | SoW **Draft v1.1 (14 Sep)**, flagged stale by the 24 Sep ruling | Drive "2026-09-14 ERMOS 90-Day Accounting Beta SoW (D&L Partners)", 1ecLOuNgl8cw0e6GDlyWLCOilE69-kUzRHUqx79XNF2o |
| David's existing channel partners (unnamed) | Partners David has worked with before | Action T16: review the existing channel process with them and come back with targets (due 16 Sep). No outcome found. | `tasks.json` (26 Aug) |
| Olympus | Hardware build supplier (a technology partner, not a channel partner) | Action T28: Will to send box specs for a build quote, with NDAs first (T29) | `tasks.json` (26 Aug) |

**Warm-intro networks named in the 26 Aug meeting:** Will's lawyer network (T31), the accounting firm David has lined up (T34), and Brad's accountant contacts, including an AI-interested contact and a 15-person practice (T32). All three founders were asked to name end-user prospects (T33, needs an owner).

## 4. Co-marketing motions

| Motion | What is on record | Status | Source |
|---|---|---|---|
| ERMOS outbound directing customers to partners | ERMOS runs its own outbound to direct customers to partners offering service packages 1–3. The allocation rule, and whether the 15% ERMOS-lead rate applies, are TBD. | **Agreed in principle (v0.8 D.11); allocation not ruled** | Agreement v0.8 D.11 |
| Partner-led outreach | Partners bring and register their own clients (section 2.3), run discovery, and deploy Dominion units | Ruled 2 Oct | Section 2.3 |
| Partner collateral | "ERMOS Dominion — partner offer (IT consultants and MSPs)" v2.0, blue default and red alternate. The only CTA is Brad's booking calendar; no raw URLs. Four architecture claims are unsourced. Flagged stale on 24 Sep. | **Draft, do not distribute** | 10 Collateral, 3e377626-a809-81ab-9f46-dba102d1a0d6; harness: "Outbound Collateral Best Practice (Reference 02: Product & Partner Harness)" (Approved v1.0, 22 Sep), 3e377626-a809-812a-b040-cac9be11a284 |
| Integrator Boardroom deck | Partner-facing deck. Brad's 1 Oct rulings added claims (signed and tested updates; no external model calls on Edge; one known location for Dominion data) as Proposed Changes, and expanded the integrator verticals. | Claims still Proposed | 06 Proposed Changes (e.g. 3ec77626-a809-8133-8d48-f3d7a83f18cd); Partner ICP page |
| Founding partner programme | The 27 Aug deck pitches an enhanced founding commission, territory/vertical priority, co-marketing support (joint case studies, collateral, introductions) and input into certification and the roadmap. Founding cohort target: 3–5 signed by day 90. | **Pitch only; terms never ruled** | Drive "Ermos_Reseller_Partner_Presentation", 12TbojK9bmj9dcYOr3mI1AKdmplyNAExgKRvNVd1_SyM; SLT agenda 15vQdPm_qN7cb3wQ5mp2cKECzeSxWCmlmL20PDVGgMw4 |
| Joint events and webinars | Business Plan: partners about 40% of demand, paid spend "webinar-centred", CPD-style talks with the live box, a Mitronics webinar in M1. SLT agenda item 7 asks about launch cohort timing and co-marketing with hardware/software partners. | **Plan/agenda only; no decision recorded** | Business Plan (Draft); SLT agendas 15vQdPm… and 1Uo0btgdFcYMPNJVjXyOAlXDMcxE2Gus02lpiOuhgE90 |
| Partner certification and Q&A portal | v1 certification (presentation plus questionnaire) due 16 Sep (T18), full module set due 14 Oct (T19), partner Q&A behind a login due 14 Oct (Will, T21). The certification also works as the partner sales hook. | Not started at 26 Aug; no later update found | `tasks.json` (26 Aug) |
| Integrator boardroom briefings | Exclusive 10-person boardroom partner briefings to gather feedback and accelerate learning; John positioned as technical authority. Brad drafts the deck (capabilities, compliance posture, certification steps). | **Agreed 30 Sep**; owners David (host) and Brad (deck) | Gmail "Meeting Notes, Wed 30th September" |
| Integrator recruitment campaign | Integrators first: automated integrator webinar on why to use ERMOS, bespoke integrator landing pages with sign-up (Will); integrator ICP cold email list (thousands), webinar, outbound ads and cold outreach (Brad); outbound calls to IT/AI consultants and MSPs (David) | **Agreed 30 Sep** | Same |
| Vertical webinars | Niche webinars for law, accounting and health showcasing ERMOS workflows, with bespoke landing pages (Will); matching webinar, ads and cold campaigns (Brad) | **Agreed 30 Sep** | Same |
| Case-study and content co-production | Capture John's data-leak account verbatim as a case study (T7). Run a Mayweathers problems-and-workflows focus group (T10). LinkedIn is educational, "not marketing content" (Brad, T24). | Not started at 26 Aug | `tasks.json` (26 Aug) |

## 5. Lead ownership and routing

What is ruled:
1. **Deal registration:** the partner confirms the client with ERMOS. ERMOS sets up the client's backend instance, which then holds the client record, partner attribution and invoicing details (ruling 2 Oct; section 2.3).
2. **Billing:** ERMOS invoices every client directly and remits partner commission monthly (ruling 2 Oct).
3. **Partner-sourced clients:** 25% for life, provided the partner meets the minimum ongoing-service condition (ruling 2 Oct).
4. **ERMOS-generated leads closed by a partner:** flat 15%, while the partner stays on call as a managed service (v0.8 D.2).
5. **Orders:** ERMOS may accept or reject each Order with reasons. Discounts need ERMOS approval first (v0.8 cl 3, 8.2).

What is not ruled (do not automate on these):
- **Conflict rule:** what happens when a partner registers a client that is already in an ERMOS outbound sequence or awareness stage, and how long a registration is protected.
- **Allocation rule** for routing ERMOS-generated customers to partners (v0.8 D.11).

## 6. What counts as a Partner Signal (proposed mapping for `04_signal_tracking`)

This is not a ruling. It is a mapping drawn from the sources above, for Brad to confirm. All items fall in the 2nd-Party pillar.

| Signal | Example evidence | Suggested routing |
|---|---|---|
| Partner referral or introduction | Named partner (e.g. John Moustache) introduces a 1–50-staff firm in an approved vertical | Warm Intro (1:1). Check eligibility (Edge 10+ seats or 1 Dominion unit). Record the referring partner for commission. |
| Founder-network warm intro | Lawyers (Will), accountants (Brad), the accounting firm (David) from the 26 Aug actions | Warm Intro (1:1). Founder owns the contact. |
| Partner client-base overlap | Target firm is a known client of an integrator or MSP that meets the Partner ICP (Healthcare/Legal evidence, ISO 27001 / Essential Eight language, Copilot/LLM resale) | Hold for partner-led outreach. Do not cold-sequence until a conflict rule exists. |
| Prospective partner engagement | An integrator books via the partner offer CTA, or engages with the Boardroom deck or founding partner deck | Route as a partner-recruitment prospect against the Partner ICP (no R-02OCT account tier), not as an end-customer signal |
| Beta and case-study references | Mayweathers or D&L referencing ERMOS, once named-case-study consent is given under their SoW | Social proof for law and accounting. Use only after the case study is approved. |
| Joint event attendance | Attendance at a partner webinar or CPD session (none held on record) | 1st-party once ERMOS hosts; 2nd-party if the partner hosts |

## 7. Decisions and actions from relevant meetings

| Date | Meeting / ruling | Decision or action | Owner | Due / status | Source |
|---|---|---|---|---|---|
| 26 Aug | GTM & Partner Planning | Research and propose the partner commission structure (David floated 25% but would not commit without data) | Unassigned | 16 Sep; **resolved by the 24 Sep ruling** | `tasks.json` T15 |
| 26 Aug | GTM & Partner Planning | Meet John and bring him in as a partner-consultant | Unconfirmed (David likely) | 27 Aug; led to the 24 Sep draft agreement | T6; John A. page |
| 26 Aug | GTM & Partner Planning | Approach Mitronics as a legal-sector channel partner | Will | 16 Sep; outcome not recorded | T30 |
| 26 Aug | GTM & Partner Planning | Define the operational process for partner-led deals (leaning towards ERMOS billing the end user) | Will (inferred) | 16 Sep; billing settled 24 Sep, process not documented | T17 |
| 26 Aug | GTM & Partner Planning | Build the partner pitch and sales narrative with industry trend data. David will not front alone. | Unassigned | 16 Sep; 27 Aug deck produced | T40 |
| 26 Aug | GTM & Partner Planning | Supply the product docs partners need for certification | Will | 16 Sep; blocked on David's learning outline | T20 |
| 26 Aug | SLT Meeting #1 (agenda) | Lock partner commission; founding partner bonus yes/no; channel priority (ICT/MSP first recommended); co-marketing at launch | Not recorded | Agenda only, action table blank | 15vQdPm…; 1Uo0btg… |
| 24 Sep | Founders' meeting (via Decisions Log) | Referral 25% lifetime; MSPs keep 100% of services; onshore delivery only; partner performance benchmarks deferred | Brad | Ruled | 3e577626-a809-81ac-a23b-f476f648027b |
| 30 Sep | Cowork rulings on David's template | IT Reseller tier at 25%, 24-month cap, A$1,000 Dominion setup fee, invoicing, Fees definition | Brad | Ruled; agreement draft v0.5 in Sandbox | three 30 Sep entries above |
| 1 Oct | Ruling | Edge induction call is partner-run and unpaid | Brad | Ruled | Partner Standard Terms section 2 |
| 30 Sep | Founders' meeting (Brad's notes) | Pivot distribution to IT integrators, MSPs and AI consultants over telco; formalise John Moustache as technical advisor; 10-person boardroom briefings; integrator webinars, landing pages and outreach first | David, Brad, Will, John | Agreed | Gmail "Meeting Notes, Wed 30th September" |
| 30 Sep | Partner package | Brad sends "ERMOS Partner Agreement - IT Reseller - 2026-09-30.docx" to David for review; David to confirm updates | David | Awaiting David's changes | Gmail "Partnership draft agreement" |
| 1 Oct | Audit | **BLOCKED:** no IT Reseller agreement may be issued until the partner pricing structure exists | Brad | Open | 06 Proposed Changes, 0a498366-c11a-4ae1-b0bf-7ad845da5c53 |

---

## Excluded as superseded

- **A$2,500 success-only partner referral fee** (Dominion Business Plan). Replaced by 25% lifetime commission (24 Sep).
- **15 Sep Channel Partner Agreement draft** (Drive 155AreYUA_E9yreFOa85NEGlnUKVhwesidtXDZZqsarE). Its four roles and terms were never adopted: Closer 30%, Installer A$1,000 per site, Support Desk 10–15% trail, 40% stacking cap. The 24 Sep and 30 Sep standard replaced them. The only overlapping figure, A$1,000, now applies **per Dominion unit** to IT Resellers.
- **27 Aug Founding Partner deck figures and claims:** "no per-seat licences / one price every employee", a Dominion-only referral, and mortgage and insurance brokers as verticals. Retired by the rulings of 24 Sep (verticals) and 28 Sep (per-seat pricing). (Its "air-gapped" wording is valid again under [R-02OCT], but only with the strict no-egress definition.)
- **21 Sep retirement of "air-gapped"** and the C-002 wording "one-way health telemetry out". Superseded by [R-02OCT].
- **v0.8 24-month Commission End Date, and the partner-invoices / wholesale-rate option** (cl 1.1, 2.2, 8.1, 8.4(b), D.1, D.3). Superseded by the 2 Oct partner rulings.
- **John A. agreement Draft v0.1 (24 Sep)** as his engagement model. Superseded by the partnership agreement he is signing.
- **24 Sep "outbound strictly 10–50 seats" band.** Superseded by [R-02OCT]: 1–50 staff, sized into Tiers 1–3.
- **SLT agenda and Business Plan pricing:** A$2,599/unit/month, A$6,500 setup, A$10k/A$5k setup (T36), and Dominion flat bands (24 Sep). All replaced by the 28 Sep per-seat model.
- **Master Q&A seat band of 15–100.** Replaced by 1–50 [R-02OCT].
- **Dominion partner offer bullets** "No per-seat licensing: a fixed monthly fee per node", "firms up to 50 staff, sweet spot 5–30" and "high-margin hardware on every deployment". These conflict with per-seat pricing, with the 10–50 sweet spot, and with commission excluding hardware.
- Notion "00.archive admin..00" pages (Hormozi warm-outreach playbooks, Sales & Market Intelligence). These are archived and were not relied on.

## Remaining partner questions for Brad

Answered on 2 Oct and applied: commission term, invoicing, deal registration, John's identity and naming, and package scope (agreement v0.8). Still open:

1. **Minimum service hours:** how many hours of ongoing service per client keep the lifetime 25% (and the 15% on ERMOS leads) active? Is it per month? What happens if a partner falls short: is commission suspended, reduced, or the client reassigned?
2. **Service work invoicing:** ERMOS now invoices the subscription. Do partners still invoice their own service work (service packages 1–3, the A$500/day work, the Dominion setup) directly, or does that also run through the ERMOS instance?
3. **Registration conflicts:** if a partner registers a client that is already in an ERMOS campaign, who owns it, and how long is a registration protected?
4. **Routing rule:** how are ERMOS-generated customers allocated to partners (vertical, region, service package, capacity, rotation)?
5. **Onboarding call and setup fee:** who runs the mandatory 1-hour call for Dominion and reseller customers, and when is the A$1,000 setup fee paid?
6. **Referring partner and MSP tiers:** do they stay as separate agreements, or fold into the reseller agreement and its service packages?
7. **Pricing structure document:** who drafts it and by when? Every reseller agreement depends on it (TASKS.md T-002).

## Other open conflicts / gaps

1. **No "Meeting Ermos CoMarket" record exists.** The closest records are the 26 Aug GTM & Partner Planning actions and the 30 Sep meeting notes. Should this file be renamed?
2. **Mitronics status is unknown.** There's no record after the 26 Aug action, and the spelling is inconsistent (Mitronics/Metronics). The same goes for David's existing partners.
3. **Partner ICP firm-size band, target partner count and geography** are not ruled (Partner ICP open decisions 1–5).
4. **Collateral is stale or Draft:** the Dominion partner offer, the Mayweathers and D&L SoWs, and the Integrator Boardroom deck claims. Don't use any of them in partner co-marketing until they are re-approved. The boardroom deck (30 Sep action) should use the [R-02OCT] air-gapped definition.
5. **Notion is out of step.** The 05 Decisions Log, Claims Register C-002 and Partner Standard Terms still carry the pre-[R-02OCT] size and connectivity rules.
