# GTM Playbook 2026: Hierarchy Map

**Purpose:** the "GTM Playbook 2026" blueprint (`GTM_Playbook_2026.pdf` in this folder, by Dan Rosenthal / workflo) restructured as **Phases → Components → SOPs**, so every SOP has one fixed address.
**Status:** Brad's governing blueprint ("the bible"). Restructured 2 Oct 2026.

## Naming convention

| Level | Definition | ID format | Example |
|---|---|---|---|
| **Phase** | A major GTM milestone. One horizontal band of the blueprint. | `Phase N` | Phase 2: Broad TAM Mapping |
| **Component** | A specific sub-module inside a Phase. One box (or box group) on the blueprint. | `Component NX` | Component 2B: Find Lookalikes |
| **SOP** | An actionable, step-by-step guide living under one Component. A Component may have several. | `SOP-NX-##` | SOP-2B-01: Generating Lookalike Audiences |

SOP files are named `SOP-NX-##_<Title_With_Underscores>.md` and saved in the repo folder that owns their Phase (table below).

**Tools:** the tools listed for each Component are the blueprint's logos (Salesforce removed: ERMOS uses HubSpot only). They are candidates, not ERMOS decisions. Each SOP decides and tests the actual tools (R-02OCT: tools are tested at each step, never locked in). Logos without a readable label are marked "unlabelled".

## Phase to folder ownership

| Phase | Repo folder |
|---|---|
| Phase 1 | `01_backtest_and_icp/` |
| Phases 2–3 | `02_tam_and_research/` |
| Phase 4 and Phases 7–9 | `03_enrichment_and_activation/` |
| Phases 5–6 | `04_signal_tracking/` |
| Final Output | `outputs/` (generated artefacts) |

---

## Phase 1: Backtest and ICP Modeling
*Learn from closed deals, then define who to target.*

| Component | Blueprint boxes | Tools shown | SOPs |
|---|---|---|---|
| **1A: Backtest Model** | Backtest Model → CRM Sync → Closed Won (Analyze Highest Spend Customers; Interview AEs and CSMs) / Closed Lost (Look for Commonalities) | HubSpot | **SOP-1A-01 Backtesting Closed-Won and Closed-Lost** *(v1.0 Final baseline, 2 Oct 2026)* |
| **1B: ICP Model** | Firmographics · Technographics · Account Fit Signals | n/a | SOP-1B-01 Building the ICP Model *(planned)* · SOP-1B-02 Aged Care ICP Brief *(planned, TASKS T-001)* |

## Phase 2: Broad TAM Mapping
*Turn the ICP into a broad list of candidate accounts.*

| Component | Blueprint boxes | Tools shown | SOPs |
|---|---|---|---|
| **2A: Firmographic Fits** | Firmographic Fits | Apollo, Sales Navigator, ZoomInfo | SOP-2A-01 Firmographic TAM Pull *(planned)* |
| **2B: Find Lookalikes** | Find Lookalikes | Discolike, Ocean.io, AI Ark (all three confirmed for a 30-record AU accuracy pilot) | **SOP-2B-01 Generating Lookalike Audiences** *(Draft, 2 Oct 2026)* |

## Phase 3: Account Research and Scoring
*Verify, tier and package the accounts worth pursuing.*

| Component | Blueprint boxes | Tools shown | SOPs |
|---|---|---|---|
| **3A: Account Research** | Account Research | Clay (logo) | SOP-3A-01 Account Verification and Research *(planned)* |
| **3B: Account Scoring and Tiering** | Account Scoring → Tier 1 · Tier 2 · Tier 3 | Two unlabelled logos | SOP-3B-01 Size-Based Tiering *(planned)* |
| **3C: Enriched Target Account List** | Enriched TAL | n/a | SOP-3C-01 Building the Enriched TAL *(planned)* |

## Phase 4: ABM, Contact Sourcing and CRM Upload
*Warm up Tier 1, find the buying committee, load the CRM.*

| Component | Blueprint boxes | Tools shown | SOPs |
|---|---|---|---|
| **4A: ABM Ads and Focused Adspend** | ABM Ads → Focused Adspend (loops back to Tier 1) | HubSpot, LinkedIn | SOP-4A-01 Tier 1 ABM Ads *(planned)* |
| **4B: Contact Sourcing** | Decision Maker · Influencer · Champion | n/a | SOP-4B-01 Buying Committee Mapping *(planned)* |
| **4C: CRM Upload** | Companies · Custom Properties · Contacts | n/a | SOP-4C-01 CRM Upload and Property Schema *(planned)* |

## Phase 5: Signal Tracking
*Capture intent across the three pillars.*

| Component | Signals | Tools shown |
|---|---|---|
| **5A: 1st-Party Signals** | CRM Data · Marketing Sequences · Outreach Replies · Product Usage · Webinar Attendance · Gated Content · Website Visits · Meeting Forms | HubSpot · Beehiiv, Customer.io · Outbound Sync, Nooks · Amplitude, Mixpanel · LinkedIn, Lu.ma · Webflow, Gamma · Warmly, RB2B · Chili Piper, Apollo |
| **5B: 2nd-Party Signals** | Ad Engagements · Partner Signals · Review Sites · LinkedIn Engagement · Champion Tracking · Warm Intros | ZenABM, Fibbler · Crossbeam, PartnerStack · G2, Capterra · Jungler, Clay · Clay, UserGems · Commsor, The Swarm |
| **5C: 3rd-Party Signals** | Technographic Signals · People Data · News · Social Signals · Job Openings · Funding Announcements | BuiltWith, Sumble · Clay, Apollo · Clay, Google News · Trigify, PhantomBuster · TheirStack, PredictLeads · Crunchbase, Pitchbook |

SOPs: **SOP-5A-01 Automated Outbound Reply Management** *(Draft, 2 Oct 2026; also runs 6A, 7B and 7D for reply events)* · SOP-5B-01 (uses `meeting_ermos_comarket.md` for partner signals) *(planned)* · SOP-5C-01 *(planned)*.

## Phase 6: Awareness Scoring
*Convert signal density into one stage per account.*

| Component | Blueprint boxes | SOPs |
|---|---|---|
| **6A: Awareness Score** | Identified → Aware → Interested → Considering → Selecting | SOP-6A-01 Awareness Stage Assignment *(planned)* |

## Phase 7: Routing and CRM Actions
*Turn stage changes into actions.*

| Component | Tools shown | SOPs |
|---|---|---|
| **7A: Custom Events/Objects** | HubSpot | SOP-7A-01 *(planned)* |
| **7B: Lead Routing** | HubSpot, Clay | SOP-7B-01 *(planned; partner routing waits on the open partner questions)* |
| **7C: CRM Tasks** | HubSpot | SOP-7C-01 *(planned)* |
| **7D: Slack Notifications** | Slack | SOP-7D-01 *(planned)* |

## Phase 8: Demand Generation
*Activate accounts by scale.*

| Component | Channels (tools shown) | SOPs |
|---|---|---|
| **8A: Demand Generation 1:1** | Warm Intros (Gmail) · Gifting Campaigns (unlabelled) · Event Invites (unlabelled) · Manual Outreach (Apollo) · Automated Outbound (two unlabelled; moved here per ERMOS ruling) | SOP-8A-01 *(planned)* |
| **8B: Demand Generation 1:Many** | Parallel Dialing (unlabelled) · Targeting Ads (LinkedIn, Meta, Google) · Public Events (unlabelled) · Social Content (YouTube, LinkedIn, X) · On-Site Content (Webflow) · Video Outreach (unlabelled) · Connection Request (LinkedIn) | SOP-8B-01 *(planned)* |

**ERMOS ruling (2 Oct 2026):** Automated Outbound sits under **1:1**, as in `CLAUDE.md` section 4, even though the blueprint draws it under 1:Many.

## Phase 9: CRM Push-Back and GTM Flywheel
*Close the loop and keep it turning.*

| Component | Blueprint boxes | SOPs |
|---|---|---|
| **9A: Push Back to CRM** | Push Back to CRM (HubSpot) | SOP-9A-01 *(planned)* |
| **9B: GTM Flywheel** | Awareness → Education → Selection → Commit → Onboarding → Adoption → Expansion | SOP-9B-01 *(planned)* |

## Final Output
**Accounts Mapped + Company Tiers + Stakeholder Maps + Signals + Awareness Scores = Prioritization.** This is produced in `outputs/`, not a Phase with its own SOPs.

---

## ERMOS notes for SOP authors

- **Phase 1 backtest:** ERMOS is early-stage. The closed-won base is the beta customers (law and accounting beta SoWs) plus any signed partners, with little or no closed-lost data. SOP-1A-01 must say how to backtest with a small sample, and what to capture from now on.
- **CRM:** HubSpot is ERMOS's only CRM (Brad, 2 Oct 2026). The blueprint's Salesforce logos are dropped. **n8n** runs every background workflow and every CRM injection.
- **Component 3B tiers** are size-only (R-02OCT): Tier 1 = 10–30, Tier 2 = 31–50, Tier 3 = 1–9. In the blueprint, Tier 1 also gets Focused Adspend (4A).
- **Order of drafting:** the default order is top to bottom. Brad chose SOP-2B-01 as the first SOP (2 Oct 2026). It assumes interim seed sets until SOP-1A-01 and SOP-1B-01 exist.
