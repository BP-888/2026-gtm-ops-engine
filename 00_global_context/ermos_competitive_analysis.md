# ERMOS Competitive Analysis

Purpose: one reference for the competitive landscape that drives positioning, signal tracking and messaging for ERMOS Edge and ERMOS Dominion.

Synthesised 2 Oct 2026 from Notion Ermos HQ (ERMOS RevOps Operating System) and Google Drive. Updated 2 Oct 2026 with Brad's rulings.
Status: **Draft for Brad's review.** Not a client-facing asset. Brad's rulings of 2 Oct 2026 (cited "Brad ruling, 2 Oct 2026 [R-02OCT]") supersede the Notion Decisions Log and Claims Register where they conflict. Otherwise the Claims Register (veto rank 1) and the 05 Decisions Log override this file.

Verification labels used below:
- **Ruled**: Brad ruling (R-02OCT, 05 Decisions Log or the Claims Register). Canonical.
- **Verified (date)**: checked against the vendor's primary source on that date and recorded in Notion. Re-check before external use.
- **Unverified**: sits in a guide marked "Needs verification", or no primary source recorded. Internal use only.
- **ERMOS estimate / inference**: our own model or reasoning, not a vendor fact.

All six 09 Competitive Decision Guides are Status "Needs verification" with no Last verified date (audit reports 23 Sep, 28 Sep and 1 Oct 2026). Treat every competitor figure as call-prep intelligence, not copy, unless marked Verified.

---

## 1. ERMOS baseline (current rulings only)

| Item | Current position | Source / status |
|---|---|---|
| Products | ERMOS Edge (cloud, Australian SOC 2 compliant server). ERMOS Dominion (isolated on-premises perimeter in the client's office). ERMOS AI is the engine behind both (formerly ERMOS IQ, name retired). | Claims Register product facts, 16 and 21 Sep 2026. Ruled |
| Edge price | A$99/seat/month ex GST, 10-seat minimum (A$990/month), no ceiling. 12 months upfront: 20% off, A$950.40/seat/yr. VIP A$49.50/seat/month, no stacked discount. | Decisions Log, Edge scaling rules, 24 Sep 2026. Ruled |
| Dominion price | A$99/seat/month ex GST, 10-seat minimum. A$7,500 hardware one-off per box; one box per 15 people (new box at seats 16, 31, 46...). No upfront discount. No Dominion VIP price currently approved. | Decisions Log, Dominion per-seat pricing, 28 Sep 2026 (supersedes 24 Sep flat bands). Ruled |
| Dominion connectivity | **Air-gapped.** Strict definition: no egress; no documentation or data can flow out. Only inbound pings for health checks and inbound patch updates are permitted. | Brad ruling, 2 Oct 2026 [R-02OCT]. Ruled. Network configuration confirmation and C-002 re-issue pending (open item 1) |
| Target | Firms of 1 to 50 staff (sweet spot 10–50); accounting, law, aged care, healthcare, finance. Tiers by size only: **Tier 1** 10–30, **Tier 2** 31–50, **Tier 3** 1–9. Over 50 disqualified. Tier 3 firms still pay the 10-seat minimum (ERMOS arithmetic). | Brad ruling, 2 Oct 2026 [R-02OCT]. Ruled. Note: the competitive guides still say "1–30 staff" (out of date). |

Worked examples at current pricing (ERMOS arithmetic from the rulings above): 10 seats Edge A$990/month, Dominion A$990/month + A$7,500. 15 seats A$1,485/month either product (Dominion 1 box). 30 seats A$2,970/month (Dominion 2 boxes, A$15,000). 50 seats A$4,950/month (Dominion 4 boxes, A$30,000).

## 2. The core position: a control model, not compliance by logo

From the Master Executive Decision Guide (Needs verification, but the framing is consistent with the Claims Register):

- Do not sell "compliance by logo". Sell a clearer control model. Enterprise branding does not answer: where is content stored, where is inference performed, which tools/connectors/logs sit outside a regional boundary, is content used for training, who controls access and offboarding, what audit evidence can the practice produce.
- **Storage at rest is not the same as inference location.** Several vendors now offer Australian storage or Sydney endpoints for some products; few guarantee the full workload.
- **The diligence unit is the whole workload and contract**, not the vendor name: model, store, connectors, logs, support paths.
- ERMOS Edge is processed in Australia by an audited provider. ERMOS Dominion runs an isolated, air-gapped on-premises perimeter: data is processed inside the firm's own office and nothing flows out (R-02OCT). **The practice keeps its professional obligations in either case.** ERMOS gives evidence and controls; it never guarantees a legal or compliance outcome.

## 3. Competitor set at a glance

Named in prospect copy (approved 29 Sep 2026, Claims Register usage rules and Hormozi Standard s8): **ChatGPT, Claude, Gemini, Grok.** Microsoft 365 Copilot has a full decision guide and flyer but is **not** on the 29 Sep approved naming list (see Open conflicts).

| Competitor | Where it sits for our ICP | Main ERMOS angle | Guide |
|---|---|---|---|
| ChatGPT (OpenAI) | Highest shadow-AI usage on personal Plus/Pro logins; Business from 2 seats | Personal-login fragmentation; AU storage is not AU inference | f27d5ad2 (Needs verification) |
| Claude (Anthropic) | Personal Pro/Max logins; Enterprise has 20-seat floor | Seat floor and usage billing; no AU inference on Anthropic's own API/apps | 61b7da3f (Needs verification; verified fact set approved 18 Sep) |
| Gemini (Google) | Bundled in Google Workspace; Workspace shops | Workspace Data Regions offer no Australian option; Drive oversharing | 1b003c7f (Needs verification) |
| Grok (xAI) | Consumer SuperGrok logins; Grok Business | Consumer training default; no documented AU endpoint | 84474623 (Needs verification) |
| Microsoft 365 Copilot | Default incumbent in M365 practices; cheaper on licence cost (do not lead on price) | Data sovereignty: data may rest onshore but inference can run offshore; permission inheritance / oversharing; build-vs-buy for Studio agents | 0b736aaf (Needs verification; tier facts verified 21 Sep) |
| Build-it-yourself (OpenAI API, Copilot Studio, Vertex AI, Claude Code, Grok API) | Firms with an IT partner or in-house developer | Firm becomes a software company: keys, logging, regional mapping, variable cost | Section 4–5 of each guide |

## 4. Per-competitor positioning and facts

### 4.1 ChatGPT (OpenAI)

| Fact | Value | Status |
|---|---|---|
| Data at rest | Australia available to eligible **new** ChatGPT Enterprise/Edu workspaces | Verified (ticked in guide checklist; OpenAI help 9903489) |
| Inference residency | Regions listed: Europe, US, UAE. Australia not listed. Non-GPU processing may still be global. | Verified (same source) |
| Business plan | Standard US$20/user/mo annual (US$25 monthly); Premium US$100 annual (US$125 monthly); minimum 2 seats | Verified (ticked; OpenAI help 8792828) |
| Plus / Pro | US$20 / US$200 per month | Unverified (AU checkout not confirmed) |
| Enterprise price and minimum | Quote-based. **Do not use** "150 seats / ~US$108k" | Unverified, banned until written quote |
| Training defaults | Plan-specific | Unverified |

Positioning: Australian storage does not establish Australian inference. Personal accounts fragment acceptable use, offboarding and audit evidence. Compare like with like: ChatGPT Business genuinely centralises admin from 2 seats, so do not present consumer weaknesses as if they apply to every tier.

### 4.2 Claude (Anthropic)

Verified fact set (06 Proposed Changes 3df77626...c058, Status Approved, verified 18 Sep 2026):

| Fact | Value | Status |
|---|---|---|
| Pro / Max | US$20/mo; Max from US$100/mo | Verified 18 Sep (claude.com/pricing) |
| Enterprise seat | US$20/seat/mo billed annually, includes no usage; all usage at standard API rates | Verified 18 Sep (Help Centre 11526368) |
| Enterprise minimum | 20 seats; seats cannot be removed mid-term (self-serve) | Verified 18 Sep (Help Centre 13393991) |
| Spend controls | Admins can set org and user spend limits | Verified 18 Sep. So "uncapped API" is retired |
| Enterprise-only features | Audit logs, SCIM, compliance API, custom retention | Verified 18 Sep |
| Inference location | Anthropic API/apps: "us" or "global" only; no Australian option; workspace storage US only | Verified 18 Sep |
| Via AWS Bedrock | Australian geo profiles exist | Noted 18 Sep; so "no AU inference" is true for Anthropic's own API only |
| Training (Pro/Max) | Each user's own setting | Verified 18 Sep |
| Power-user usage | ~US$13/active day; US$150–250/developer/mo | Verified 18 Sep (Claude Code costs doc) |
| Standard-user usage US$120/mo | ERMOS estimate, unsourced | Label as estimate |

Positioning: the 20-seat Enterprise floor matters for firms under 20 staff (ERMOS minimum is 10 seats). Enterprise seat fee excludes usage, so total cost is variable. The guide body still carries retired lines ("~US$13,500/yr", "fails TPB", "uncapped") that the approved change removed; do not quote the guide body.

### 4.3 Gemini (Google)

| Fact | Value | Status |
|---|---|---|
| Workspace Data Regions | US, Europe or no preference. Not Australia | Verified (ticked; Google Workspace admin docs) |
| Coverage | Gemini prompts/responses can be covered for storage **and** processing in selected regions | Verified (ticked) |
| Google Cloud / Gemini Enterprise Agent Platform | Sydney endpoints published for supported models | Verified (ticked) |
| Workspace pricing | Business Starter US$7, Standard US$14, Plus US$22 /user/mo (1-yr) | Verified (ticked) |
| Gemini Enterprise | Business from US$21; Standard/Plus from US$30 /seat/mo; usage extra | Verified (ticked) |
| Minimums, quotas, metering triggers | Not confirmed | Unverified |

Positioning: "Workspace", "Gemini Enterprise" and "Vertex AI" are different paths. A blanket "all Gemini inference is offshore" claim is **inaccurate**. Argue instead: standard Workspace has no Australian region; a Google Cloud build can use Sydney but must map every model, connector, log and store. Gemini respects existing permissions, so poorly governed Drive sharing becomes more consequential.

### 4.4 Grok (xAI)

| Fact | Value | Status |
|---|---|---|
| SuperGrok | US$30/mo | Verified (ticked; x.ai/pricing) |
| SuperGrok Heavy | US$300/mo | Unverified |
| Grok Business | US$30/user/mo; RBAC, seat management, consolidated billing, no training on customer content | Verified (ticked; x.ai/grok/business) |
| Consumer training | Content may be used unless opted out or Private Chat (deleted within 30 days, with exceptions) | Verified (ticked; x.ai/legal/faq) |
| Regions | Global API endpoint may route between regions; limited US regional endpoint; no Australian endpoint documented | Verified (ticked; docs.x.ai regions) |
| Long-context API pricing | grok-4.6 rates double at ≥200k tokens; US endpoint 1.1× multiplier | Verified (ticked; docs.x.ai pricing) |
| App storage / inference location | Not confirmed | Unverified |

Positioning: separate consumer-account risk from Grok Business controls. Do not state every request is processed in the US.

### 4.5 Microsoft 365 Copilot

Tier architecture ruled 21 Sep 2026 (Decisions Log; guide callout verified against Microsoft Learn and Microsoft AU pricing on 21 Sep 2026):

| Tier | Price (AUD ex GST) | Scope | Status |
|---|---|---|---|
| Microsoft 365 Copilot (base) | A$44.90/user/mo on top of a qualifying M365 licence | Chat plus **internal agents** via Agent Builder; org-scoped, declarative, not autonomous, cannot publish externally | Ruled + Verified 21 Sep |
| Copilot Studio (add-on) | A$299.30/tenant/mo for 25,000 Copilot Credits, then metered (needs Azure subscription) | **Autonomous agents, multi-agent systems, publishing to external channels**, actions reaching external services | Ruled + Verified 21 Sep |
| Australian in-country processing for Copilot | Announced, due by end 2026 | Open; re-check monthly. When live, the processing row flips to a tick |
| Data at rest, AU tenants | Australia | Treat as a tick for Copilot, not a warning (21 Sep ruling) |

Scope ruling (21 Sep): ERMOS competes with Microsoft on **internal work only** (firm files, internal knowledge retrieval, internal workflows). External/client-facing bots are out of scope for collateral.

**Positioning ruled (Brad ruling, 2 Oct 2026 [R-02OCT]): position against Copilot on data sovereignty and security, not price.**

- Core line: Copilot data may rest onshore, but the AI processing (inference) can happen offshore. ERMOS Edge processes in Australia. ERMOS Dominion processes inside the firm's own office.
- Security point: offshore processing means client data leaves Australian jurisdiction during processing. That weakens onshore data-sovereignty assurances and the firm's ability to evidence where its data is processed. A SOC 2 report alone does not answer where processing happens.
- Do **not** say offshore processing "compromises SOC 2 compliance" or that Copilot is not SOC 2 compliant. SOC 2 is an audit attestation of a provider's controls, not a data-location standard, and Microsoft publishes SOC 2 reports. The claim would be inaccurate and an Australian Consumer Law risk (open item 2).
- Say inference "can" happen offshore; do not claim Microsoft routes prompts offshore for load balancing (retired, unverified).
- Microsoft's in-country processing for Australia is due by end 2026. Re-check monthly; if it lands, the inference-location argument weakens and Dominion's in-office processing carries the sovereignty case.

**Price reality (internal call-prep only; do not lead on price vs Copilot. ERMOS arithmetic from the figures above; excludes M365 base licences):**

| Seats | Copilot base | Copilot + Studio | ERMOS Edge (monthly) |
|---|---|---|---|
| 10 | A$449 | A$748 | A$990 |
| 15 | A$674 | A$973 | A$1,485 |
| 30 | A$1,347 | A$1,646 | A$2,970 |

ERMOS is dearer on licence cost at every size shown. Keep this table out of prospect copy and the flyer. **Win on sovereignty and control, then turnkey delivery, not on price** (R-02OCT).

Positioning that survives: Copilot is only as safe as SharePoint/OneDrive/Teams permissions (describe inherited access and stale permissions; never say the AI "breaches" permissions). Studio-built autonomous workflows make the firm the software builder, with a credit meter.

## 5. Where ERMOS wins and loses

| ERMOS tends to win | ERMOS tends to lose or must not overclaim |
|---|---|
| Staff using ChatGPT/Claude/Gemini/Grok on personal logins with client data (C-005 positioning, Edge) | Pure licence cost against Copilot base or Copilot + Studio (do not compete on price) |
| M365 practices that want client data processed in Australia (Edge) or inside the office (Dominion), not just stored onshore (R-02OCT) | Any argument that Copilot is not SOC 2 compliant or that offshore processing breaks SOC 2 |
| Firm needs Australian processing evidence today (Edge) or an on-premises perimeter (Dominion) | Firms whose IT partner can build a mapped Sydney-endpoint Vertex or Bedrock workload |
| Firms under 20 staff facing Claude Enterprise's 20-seat floor | Firms satisfied with ChatGPT Business or Grok Business admin and no-training terms |
| M365 tenants with messy permissions; partner uneasy about oversharing | Once Microsoft AU in-country processing goes live (end 2026), the Copilot location argument weakens |
| Highly sensitive matters (litigation, medical records, HNW financial data): Dominion | Any argument resting on "fails TPB/Law Society": the TPB sets no onshore mandate (TPB(GS) 55/2026, per 18 Sep correction) |
| Firm does not want to become a software company (build vs buy) | Firms needing external, client-facing bots (out of ERMOS collateral scope) |

## 6. Approved claims vs retired claims

**Approved (Claims Register, veto rank 1):**

| # | Claim | Scope |
|---|---|---|
| C-001 | "100% AI, 0% risk" | Dominion only. Australian Consumer Law read still open |
| C-002 | "Air-gapped." Definition must travel with it: no egress, no documentation or data flows out; only inbound health-check pings and inbound patch updates. | Dominion only. Brad ruling, 2 Oct 2026 [R-02OCT]; Claims Register entry to be re-issued and network configuration confirmed (open item 1) |
| C-003 | "Completely sovereign" / "100% sovereign compliant" | Dominion only |
| C-004 | "SOC 2 compliant" (never "SOC compliant") | Edge |
| C-005 | "Secure, onshore alternative to public AI" | Edge only; positions against loose personal logins, no claims about vendors' own security |
| C-006 | "Uptime monitored 24/7" | Dominion; no SLA or uptime % |
| T-001 | "YOUR EXPERTISE. OUR ENGINE. SECURED ONSHORE." | Partner agreements only |
| — | Edge described as "processed in Australia by an audited provider" | Edge (usage rule) |
| — | Against Copilot: "Copilot data may rest onshore, but AI processing can happen offshore. ERMOS Edge processes in Australia; ERMOS Dominion processes inside your own office." | Brad ruling, 2 Oct 2026 [R-02OCT]. Sovereignty and control, not price |

**Retired or banned (do not use):**
- "Air-gapped" for Edge (Edge is cloud). For Dominion, "air-gapped" is approved only with the R-02OCT definition.
- "Runs disconnected", "no cloud path" for any product (21 Sep 2026; R-02OCT reinstated only "air-gapped"). Dominion receives inbound pings and patches, so it is not disconnected.
- Dominion telemetry-out wording: "one-way health telemetry out", "management telemetry out" (superseded by R-02OCT).
- "Offshore processing compromises SOC 2 compliance" / "Copilot is not SOC 2 compliant" (inaccurate; ACL risk; see 4.5).
- Price-led copy against Copilot (R-02OCT).
- ERMOS IQ / ErmosIQ, Edgeway, ERMOS Edge+, "ERMOS On-Premise Box", "the box".
- Edge: "nothing leaves", "never leaves the country", "guaranteed", "absolute", "no client data egress", "0% risk".
- "Fails TPB and Law Society" / "immediate audit liability" / "compliant today" / "exceeds audit standards".
- US CLOUD Act framing (unsourced).
- "Microsoft routes prompts offshore to balance Azure load" (unverified); "building agents requires Copilot Studio" (wrong: base includes internal agents).
- Claude: "~US$13,500/yr Enterprise", "uncapped API", "no Australian inference" without the "Anthropic's own API" qualifier.
- ChatGPT: "150-seat / US$108k Enterprise floor".
- "Pay strictly per active headcount", "zero billing surprises", "no per-seat licences", "one price, every employee", "unlimited users", "flat fee" (all contradicted by current per-seat pricing).
- Not yet released for Edge: "sovereign", "unmetered", "autonomous" (flyer v6.4 open items).
- Prospect copy: no hyphens or dashes; no pricing in cold copy; no invented statistics (Hormozi Standard, 29 Sep).

## 7. Objection handling (call prep; replies escalate pricing to Brad)

| Objection | Response line (must map to an approved claim) |
|---|---|
| "We already use Copilot / ChatGPT." | Acknowledge, ask one curious question about how client files are handled today, move to nurture. Never invent a benchmark (Hormozi Standard s6). |
| "Copilot is cheaper." | Do not contest price. Shift to sovereignty: Copilot data may rest onshore, but AI processing can happen offshore; Edge processes in Australia, Dominion inside the firm's own office. Then inherited permissions and Studio build effort (AU in-country processing due end 2026; re-check). |
| "Microsoft is SOC 2 audited." | Correct; credit it. SOC 2 attests a provider's controls; it does not say where processing happens. Ask whether the firm can evidence where its client data is processed. |
| "ChatGPT Enterprise stores data in Australia." | True for eligible new Enterprise workspaces. Ask where inference runs: Australia is not a listed ChatGPT inference region. |
| "Gemini has data regions." | It does: US, Europe or no preference. Not Australia in Workspace. Sydney exists for some Google Cloud models, which is a build project. |
| "Claude Enterprise has audit logs." | Correct. It also has a 20-seat minimum, usage billed on top, and Anthropic's own API offers "us" or "global" only. |
| "Grok Business doesn't train on our data." | Correct; credit it. The open question is processing location: no Australian endpoint is documented. |
| "Our IT partner can build it on Azure / Vertex / Bedrock." | Build vs buy: firm owns keys, logging, connector review, regional mapping, incident response, variable cost. ERMOS is turnkey (Edge environment stood up in week 1, C-007, pending confirmation it is in the master register). |
| "Is it air-gapped?" | Dominion: yes. No egress; no documentation or data flows out. The only traffic is inbound health-check pings and inbound patch updates (R-02OCT; pending Will's network confirmation, open item 1). Edge is cloud, not air-gapped. |
| "Does this make us compliant?" | No product transfers professional obligations. ERMOS gives location evidence and firm-managed access. |

## 8. Technographic signals (for signal tracking and prioritisation)

ERMOS inference unless noted. None of these is validated against conversion data yet. Competitor signals feed signal tracking and prioritisation, not tier; tier is set by firm size only (section 1, R-02OCT).

| Signal | Indicates | Use |
|---|---|---|
| Microsoft 365 tenant (MX to outlook.com / protection.outlook.com; SharePoint, Teams, Entra in tech stack) | Copilot is the default incumbent path | Tag "M365"; lead with data sovereignty (inference location), then oversharing and build-vs-buy; no price-led copy |
| Copilot or Copilot Studio named in job ads, LinkedIn posts, IT partner case studies | Copilot already licensed or being evaluated | Prioritise; Microsoft playbook |
| Azure / Power Platform / Power Automate in stack | Build-it-yourself capacity | Build-vs-buy angle |
| Google Workspace (MX to google.com) | Gemini bundled | Tag "Workspace"; lead with no AU Workspace region and Drive sharing |
| Google Cloud / Vertex AI in stack | Possible custom build on Sydney endpoints | Lower priority unless firm lacks developer capacity |
| ChatGPT, Claude, Grok mentioned in staff profiles, firm blog, policies, or no AI policy visible | Shadow AI on personal logins | Core Edge C-005 angle; name the tool in copy |
| AWS (Bedrock) in stack | Possible AU-region Claude via Bedrock | Do not use the "no AU inference" line |
| Practice data systems: Xero, MYOB, Class Super, BGL Simple Fund 360, XPM, FYI Docs, Practice Ignition | Handles client tax/trust/fund data daily | Sensitivity proxy for accounting (Drive: Dominion Apollo Targeting Brief, 13 Aug 2026; predates current pricing but technographics still valid) |
| Firm size 1–50, regulated vertical | Inside target market | Sets tier only (Tier 1 10–30, Tier 2 31–50, Tier 3 1–9; over 50 disqualified). Under 20 adds the Claude 20-seat-floor angle; 16+ adds a second Dominion box |

## 9. Regulatory and market drivers

| Driver | Detail | Source / status |
|---|---|---|
| Privacy Act APP 1.7 | From 10 Dec 2026 privacy policies must disclose substantially automated decisions that use personal information (incl. AI) | Reseller Partner Presentation (27 Aug 2026), no citation in deck. Consistent with the Privacy and Other Legislation Amendment Act 2024 commencement; **verify against OAIC before use** |
| TPB position | TPB sets no onshore processing mandate | TPB(GS) 55/2026, cited in approved 18 Sep correction. Do not claim competitors "fail" TPB |
| Law Society / professional rules | Interpretations not yet validated | Unverified; needs qualified adviser |
| Shadow AI | "70%+ of knowledge workers in AU SMEs estimated to use unsanctioned AI" | Reseller deck, **no source cited**. Do not use (Hormozi: no invented statistics) |
| Privacy as #1 barrier | "39% of AU small businesses name privacy & security as #1 AI barrier" | Reseller deck, **no source cited**. Do not use until sourced |
| NSW Reconstruction Authority incident | Oct 2025: contractor uploaded ~12,000 rows of flood-victim data to an AI tool, ~3,000 people affected | Reseller deck, no citation in deck. Publicly reported; verify primary source (NSW Government statement) before use |
| Market size | A$142B AI contribution by 2030; A$115B gen AI; 79% professional services adoption; edge AI 20–29% CAGR | Reseller deck, attributed to reports (AI Opportunities Report 2025, Tech Council/Microsoft, Grand View, MarketsandMarkets). Unverified; partner/investor context only, not prospect copy |
| Microsoft AU processing | Copilot in-country processing due end 2026 | Copilot guide, open. Monthly re-check; weakens the inference-location argument when live |

## 10. Source index

- Notion 05 Decisions Log: Edge scaling rules (3e577626a80981849c3ee2c7aa1f457f, 24 Sep); Dominion per-seat pricing (19294104ed9a4ae185badaaf7c2e3033, 28 Sep).
- Notion 01 Standards: Claims Register (3dd77626a80981d6ac46ead2de3e501e, Approved v0.2, body still says DRAFT).
- Notion 04 Playbooks: Hormozi Standard v2.0 (3de77626a809816a834cd1a767b93ee3, Approved 29 Sep).
- Notion 09 Competitive Decision Guides: Master (bd7b7822), Copilot (0b736aaf), ChatGPT (f27d5ad2), Claude (61b7da3f), Gemini (1b003c7f), Grok (84474623). All Needs verification, last edited 21 Sep.
- Notion 06 Proposed Changes: Claude verified fact set (3df77626a80981cc9213ebb4e770c058, Approved); audits 23 Sep (b65736de), 28 Sep (25b12868), 1 Oct (da85d9e1).
- Notion 10 Collateral: ERMOS vs Microsoft 365 Copilot A4 flyer v6.4 (3df77626a809812c8a93e65cadda9379, Draft).
- Drive: Ermos_Reseller_Partner_Presentation (12TbojK9...); Dominion Apollo Targeting Brief (1d7q3EiW...); "AI competitive analysis_Top 5 vs. ERMOS" (1daFtP_c...) returned no extractable text.

## Excluded as superseded

- All ERMOS prices in the competitive guides and flyers: 21 Sep swap (Edge A$999/A$1,499; Dominion A$1,499/A$1,999 + hardware), 18 Sep figures, A$2,599 + GST, and 24 Sep Dominion flat bands. Stale per the 24 Sep and 28 Sep rulings.
- Firm-size cost tables in the ChatGPT, Claude and Copilot flyers and the guides' pricing sections (marked STALE, 24 Sep), and the "1:5 power-user" US$ planning tables (ERMOS planning assumption, unverified competitor figures).
- Copilot guide body: US$30 SKU and US$200 Studio pack pricing, CLOUD Act, offshore dynamic routing, "fails TPB", ERMOS "compliant today" matrix.
- Claude guide body: ~US$13,500 Enterprise, "default training", "fails TPB", "uncapped".
- Reseller Partner Presentation product claims: air-gapped without the R-02OCT definition, "no internet path out", ErmosIQ, "one price, every employee / no per-seat licences", "compliance-ready", Dominion-only framing.
- Aug 2026 Smartlead ICP profiles and accounting outreach topics: flat fee, unlimited users, A$2,599 + GST, ErmosIQ.
- Microsoft scope note that the Copilot flyer has "no Studio column" (v5.0); v6.0+ carries both Microsoft columns.
- Notion 00.archive content: not used.
- 21 Sep 2026 retirement of "air-gapped" for Dominion: superseded by R-02OCT.
- Claims Register C-002 corrected wording ("Not air-gapped. One-way health telemetry out, one-way signed ERMOS updates in, no path to firm data from outside"; "Management telemetry out, signed updates in"): superseded by R-02OCT.
- Outbound target band "10–50 seats" and any A/B/C or score-based tiering from competitor signals: superseded by R-02OCT (1–50 staff, size-only tiers).

## Open conflicts / gaps for Brad

1. **Dominion air-gapped: network confirmation (Will).** Confirm the actual network configuration matches the strict no-egress definition: health-check responses and patch retrieval must not create an outbound data path. Any outbound health telemetry would make the claim inaccurate. Claims Register C-002 needs re-issuing with the R-02OCT wording, and Hormozi Standard s2 ("air-gapped") should carry the definition.
2. **SOC 2 wording adjusted (Brad to confirm).** The R-02OCT ruling said offshore processing "compromises SOC 2 compliance". This file does not carry that as a claim: SOC 2 is an audit attestation of a provider's controls, not a data-location standard, and Microsoft publishes SOC 2 reports, so the claim is inaccurate and an Australian Consumer Law risk. Replaced with: offshore processing takes client data outside Australian jurisdiction during processing, weakening onshore sovereignty assurances and the firm's ability to evidence where data is processed; a SOC 2 report alone does not answer where processing happens.
3. **Competitive guides unverified.** All six are Needs verification with no Last verified date; guide bodies still carry retired claims below the correction callouts and 1–30 staff targeting. Rebuild or keep held.
4. **Microsoft naming.** 29 Sep ruling names ChatGPT, Claude, Gemini and Grok for prospect copy. Is Microsoft 365 Copilot approved for prospect copy, or flyer/call prep only?
5. **Claude Enterprise minimum.** The Master guide checklist says do not use the 20-seat claim; the approved 18 Sep fact set verified 20 seats. Confirm the 20-seat floor is cleared for use and apply the fact set to the Claude guide.
6. **Dominion VIP.** No Dominion VIP price is approved after 28 Sep; older VIP rows remain in 07 Commercial Economics.
7. **C-001 "0% risk"** Australian Consumer Law read still outstanding.
8. **C-007** ("environment stood up in week 1") is cited by the Hormozi Standard but not listed in the master Claims Register page fetched 30 Sep; confirm before using in objection handling.
9. **Market stats** in the Reseller deck (70%+ shadow AI, 39% barrier) have no cited source; APP 1.7 date and NSW incident need primary-source confirmation.
10. **Drive slides** "AI competitive analysis_Top 5 vs. ERMOS" returned no text (likely image-only); review manually for anything not captured here.
11. **Technographic signals** in section 8 are ERMOS inference; validate against Apollo/Clay data before relying on them for prioritisation.
12. **Microsoft AU in-country processing** due end 2026: set a monthly re-check owner. If it lands, the Copilot inference-location argument weakens.
