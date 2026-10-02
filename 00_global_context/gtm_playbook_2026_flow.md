# GTM Playbook 2026: Flow Map

**Purpose:** a text map of the "GTM Playbook 2026" blueprint (`GTM_Playbook_2026.pdf` in this folder, by Dan Rosenthal / workflo). It numbers the sections so each SOP can name exactly which box it covers.
**Status:** Brad's governing blueprint ("the bible"), 2 Oct 2026. SOPs are written one section at a time, top to bottom.
**Tools:** the tools listed are the ones whose logos appear in the diagram. They are the blueprint's examples, not ERMOS decisions. Each SOP decides the actual tools (see `CLAUDE.md`, SOP Authoring Standard, and the R-02OCT rule that tools are tested, not locked in). Logos without a readable label are marked "unlabelled".

## Section order

| # | Section | Boxes in the diagram | Tools shown |
|---|---|---|---|
| S01 | **Backtest Model** | Backtest Model → CRM Sync → Closed Won (Analyze Highest Spend Customers; Interview AEs and CSMs) and Closed Lost (Look for Commonalities) → feeds ICP Model | HubSpot, Salesforce |
| S02 | **ICP Model** | Firmographics · Technographics · Account Fit Signals | n/a |
| S03 | **Broad TAM Map** | Firmographic Fits · Find Lookalikes | Firmographic: Apollo, Sales Navigator, ZoomInfo. Lookalikes: Discolike, Ocean.io, AI Ark |
| S04 | **Account Research** | Account Research | Clay (logo) |
| S05 | **Account Scoring** | Account Scoring → TIER 1 · TIER 2 · TIER 3 (Tier 1 has a dotted feedback loop from Focused Adspend) | Two unlabelled logos (one resembles Google, one an AI assistant) |
| S06 | **Enriched Target Account List (TAL)** | Enriched TAL | n/a |
| S07 | **ABM Ads** | ABM Ads → Focused Adspend (loops back to Tier 1) | HubSpot, LinkedIn |
| S08 | **Contact Sourcing** | Decision Maker · Influencer · Champion | n/a |
| S09 | **CRM Upload** | Companies · Custom Properties · Contacts | n/a |
| S10 | **Signal Tracking** | 1st-Party · 2nd-Party · 3rd-Party (detail below) | see below |
| S11 | **Awareness Score** | Identified → Aware → Interested → Considering → Selecting | n/a |
| S12 | **Routing and Actions** | Custom Events/Objects · Lead Routing · CRM Tasks · Slack Notifications | Custom Events: HubSpot, Salesforce. Lead Routing: HubSpot, Salesforce, Clay. CRM Tasks: HubSpot, Salesforce. Slack |
| S13 | **Demand Generation** | 1:1 and 1:Many (detail below) | see below |
| S14 | **Push Back to CRM** | Push Back to CRM | HubSpot, Salesforce |
| S15 | **GTM Flywheel** | Awareness → Education → Selection → Commit → Onboarding → Adoption → Expansion | n/a |
| S16 | **Final Output** | Accounts Mapped + Company Tiers + Stakeholder Maps + Signals + Awareness Scores = Prioritization | n/a |

## S10 Signal Tracking: detail

| Pillar | Signal | Tools shown |
|---|---|---|
| 1st-Party | CRM Data | HubSpot, Salesforce |
| 1st-Party | Marketing Sequences | Beehiiv, Customer.io |
| 1st-Party | Outreach Replies | Outbound Sync, Nooks |
| 1st-Party | Product Usage | Amplitude, Mixpanel |
| 1st-Party | Webinar Attendance | LinkedIn, Lu.ma |
| 1st-Party | Gated Content | Webflow, Gamma |
| 1st-Party | Website Visits | Warmly, RB2B |
| 1st-Party | Meeting Forms | Chili Piper, Apollo |
| 2nd-Party | Ad Engagements | ZenABM, Fibbler |
| 2nd-Party | Partner Signals | Crossbeam, PartnerStack |
| 2nd-Party | Review Sites | G2, Capterra |
| 2nd-Party | LinkedIn Engagement | Jungler, Clay |
| 2nd-Party | Champion Tracking | Clay, UserGems |
| 2nd-Party | Warm Intros | Commsor, The Swarm |
| 3rd-Party | Technographic Signals | BuiltWith, Sumble |
| 3rd-Party | People Data | Clay, Apollo |
| 3rd-Party | News | Clay, Google News |
| 3rd-Party | Social Signals | Trigify, PhantomBuster |
| 3rd-Party | Job Openings | TheirStack, PredictLeads |
| 3rd-Party | Funding Announcements | Crunchbase, Pitchbook |

All three pillars feed S11 Awareness Score. The 3rd-Party pillar also feeds S12 directly.

## S13 Demand Generation: detail

| Scale | Channel | Tools shown |
|---|---|---|
| 1:1 | Warm Intros | Gmail |
| 1:1 | Gifting Campaigns | unlabelled logo |
| 1:1 | Event Invites | unlabelled logo (sparkle) |
| 1:1 | Manual Outreach | Apollo (logo) |
| 1:Many | Automated Outbound | two unlabelled logos |
| 1:Many | Parallel Dialing | unlabelled logo |
| 1:Many | Targeting Ads | LinkedIn, Meta, Google |
| 1:Many | Public Events | unlabelled logo (sparkle) |
| 1:Many | Social Content | YouTube, LinkedIn, X |
| 1:Many | On-Site Content | Webflow |
| 1:Many | Video Outreach | unlabelled logo |
| 1:Many | Connection Request | LinkedIn |

**Difference from `CLAUDE.md`:** the diagram puts **Automated Outbound under 1:Many**. `CLAUDE.md` section 4 lists it under 1:1. Brad to confirm which governs.

## ERMOS notes for SOP authors

- **S01 Backtest:** ERMOS is early-stage. The closed-won base is the beta customers (law and accounting beta SoWs) plus any signed partners. There is little or no closed-lost data. The S01 SOP must say how the ICP is backtested with a small sample, and what gets captured from now on so the backtest gets stronger over time.
- **CRM:** the blueprint shows HubSpot and Salesforce. ERMOS's system of record must be confirmed in S01 (HubSpot is connected to this workspace; Smartlead and ICP_Master are the current working stores).
- **S05 tiers:** ERMOS Tier 1/2/3 are size-only (R-02OCT): Tier 1 = 10–30, Tier 2 = 31–50, Tier 3 = 1–9. In the blueprint, Tier 1 also gets Focused Adspend.
- **S10 Partner Signals:** see `meeting_ermos_comarket.md`. Partner registration runs through the client's ERMOS backend instance.
