# Notion change log: Brad's rulings, 2 Oct 2026

Workspace: ERMOS RevOps Operating System (Ermos HQ). Applied by Claude Code session, 2 Oct 2026, on Brad's instruction to overwrite superseded rules. Every edited page got a dated note ("Updated 2 Oct 2026 per Brad's rulings (Decisions Log)") at or next to the changed text. No pages deleted. Nothing under `00.archive admin..00` touched. Historical Decisions Log entries not edited.

## Decisions Log entries created (05 Decisions Log, all Date 2026-10-02, Decided by Brad, Verified Confirmed)

| # | Decision | Dept | URL |
|---|---|---|---|
| 1 | Firm size 1–50 staff (sweet spot 10–50, over 50 disqualified); account Tiers 1/2/3 by verified staff count replace all numeric scoring and A/B/C tiers (R1, R2, R4) | HQ | https://app.notion.com/p/3ed77626a8098160be7cc4896b508c0f |
| 2 | Enrichment tooling is tool-agnostic: no single tool locked in (R3) | Enrichment | https://app.notion.com/p/3ed77626a809810da141f9db5a8200ee |
| 3 | Dominion is "air-gapped": strict definition, no egress; only inbound health-check pings and inbound patch updates (R5) | HQ | https://app.notion.com/p/3ed77626a80981f59fb6df0ee90d277a |
| 4 | Copilot positioning: data sovereignty and security, onshore data at rest vs offshore AI processing (R6) | Outreach | https://app.notion.com/p/3ed77626a80981c58474c3b628b05444 |
| 5 | IT Reseller partner terms: lifetime 25% with minimum service, ERMOS invoices all clients, deal registration via backend instance; John Moustache / John A. naming (P1–P5) | HQ | https://app.notion.com/p/3ed77626a809816990b5c5eaec82a30c |

Note: R3 was filed under Department "Enrichment" (closest existing option) rather than HQ.

## Pages and schema updated (20)

| Page | URL | What changed |
|---|---|---|
| Claims Register (master) | https://app.notion.com/p/3dd77626a80981d6ac46ead2de3e501e | C-002 rewritten to air-gapped / no egress (inbound pings and patch updates only); C-001, C-003, C-006, T-001 justifications and Dominion product fact aligned; usage rule now approves "air-gapped" for Dominion only; Copilot positioning rule added (no SOC 2 claim); open check for Will; Version v0.3, Last ruled 2026-10-02. |
| Claims Register: accounting | https://app.notion.com/p/3de77626a80981c6988ff129d5f6b1d2 | Migration note updated; two Dominion supportable claims reworded to air-gapped / nothing flows out. |
| Claims Register: law | https://app.notion.com/p/3de77626a80981719314f393049073a3 | Migration note updated; section 4 Dominion claim reworded; 17 Sep "RETIRED" ruling replaced with "RESTORED 2 Oct 2026" (Dominion only). |
| Campaign Naming Standard | https://app.notion.com/p/3de77626a80981359117c6e9c0c1b53b | WHO BY SIZE now account Tiers with proposed tokens `T1` (10–30), `T2` (31–50), `T3` (1–9), plus `TOO_LARGE`/`Inbox`; job-by-Tier mapping; legacy cohort re-map; proposed link tags `t1-dm` etc. (pending Apps Script change); examples, CSV values and history updated; roster kept as historical. Tokens marked as proposal pending Brad. |
| 00. Master System Brief & System Rules | https://app.notion.com/p/fed5a5b00a4f4e419bba969ead145643 | Target ICPs now 1–50 (sweet spot 10–50, >50 disqualified) and include aged care; Tier definitions added; Dominion described as air-gapped; 8-step engine made tool-agnostic with best-practice principles; Phase 2/3 commands updated; "Do not call Dominion air-gapped" guardrail replaced; Copilot guardrail added. |
| Hormozi Standard | https://app.notion.com/p/3de77626a809816a834cd1a767b93ee3 | s.2 Dominion lever confirmed (air gapped, no hyphen in prospect copy); s.8 air-gapped retirement replaced with Dominion-only approval; Copilot positioning added to s.8; "5-30 cohorts" hyphen exemption changed to Tier ranges; s.10 migration note updated. |
| Partner Standard Terms | https://app.notion.com/p/3e577626a80981dda522dcc71b132db0 | Section 4: source of truth Draft v0.8 as amended; deal registration; lifetime 25% with minimum service (hours TBD); ERMOS invoices every client (wholesale option retired); 24-month cap removed; ERMOS-generated leads 15% flat; bonus 5% above A$100,000 net new ARR; A$500 day rate; service packages 1–3; open items refreshed. Ruled date and Notes property updated. |
| Managed Service Partner Agreement: John A. | https://app.notion.com/p/3e577626a8098141be15dcd82f494b6f | Internal-only callout added (John A. = John Moustache; internal vs external naming; hub role; v0.8 is source of truth, this draft not yet reconciled); air-gapped line corrected; registration process filled per P3 (section 3 and Schedule 1). |
| 07 Integrators & MSPs (Partner ICP) | https://app.notion.com/p/3eb77626a8098175b5a9f41d4f8f2e5d | Note callout only: flags that partner Tier A/B and partner size band are not covered by the account-tier ruling; content unchanged. |
| 01. ICP Master Database (schema) | https://app.notion.com/p/870efc8ba42c49cb93afebd461437b89 | Firm Size select options replaced: 10–15/16–30/31–45/46–50 → `10–30 (Tier 1)`, `31–50 (Tier 2)`, `1–9 (Tier 3)`, with property description. Safe: the only row had no Firm Size value. |
| ERMOS Dominion — Business Plan | https://app.notion.com/p/3de77626a80981d8a1e2d1ed86866e6f | Warning callout connectivity paragraph rewritten (air-gapped restored; fleet-ops telemetry row flagged for Will) and firm-size note added; seat-range line replaced with 1–50 / sweet spot 10–50. Rest of Will's draft untouched. |
| ERMOS vs. The Market: Master Executive Decision Guide | https://app.notion.com/p/bd7b78226bab4ce89d0b02075f8aa343 | Connectivity callout replaced (air-gapped); s.5 telemetry sentence replaced; target audience 1–30 → 1–50 plus aged care. |
| ERMOS vs. ChatGPT guide | https://app.notion.com/p/f27d5ad2885c4463a1cc1e15f266acac | Same three edits as the Master guide. |
| ERMOS vs. Microsoft 365 Copilot guide | https://app.notion.com/p/0b736aaf4d02426a87300c29fbe28e1e | Connectivity callout, telemetry sentence and target audience updated. |
| ERMOS vs. Google Gemini guide | https://app.notion.com/p/1b003c7f35b542389388f76afc94c2f7 | Connectivity callout, telemetry sentence and target audience updated. |
| ERMOS vs. Claude guide | https://app.notion.com/p/61b7da3fcb30418b87fed1e9102ef5a2 | Connectivity callout and telemetry sentence updated (no matching target-audience line found). |
| ERMOS vs. Grok guide | https://app.notion.com/p/84474623da304e75816e7985b67ca858 | Connectivity callout, telemetry sentence and target audience updated. |
| DTM ERMOS Dominion Core DTM Playbook | https://app.notion.com/p/0f4dae72061f43eeba62f859ebcf4c97 | Target 10–50 → 1–50 with Tiers (notes Dominion 10-seat minimum still applies); "Do not call Dominion air-gapped" guardrail replaced. |
| Ermos Edge — Product Field Guide | https://app.notion.com/p/795989f2044e4dd9bd682c45f0ca5737 | Four Dominion telemetry references changed to air-gapped / inbound only; "Never say" list now bans air-gapped for Edge only. |
| 90-Day Beta SoW: ERMOS Edge (08 Master Templates) | https://app.notion.com/p/3de77626a809810fbc31fd192ab17895 | Section 10 Dominion option and maintenance bullet reworded to air-gapped with inbound pings and patch updates; change-notes toggle updated. Edge outbound health reporter (Schedule 2) left as is (Edge is not air-gapped). |

## Needs manual update / decisions

1. **Tier boundaries:** 10 = Tier 1 and 30 = Tier 1 applied pending Brad's confirmation (Brad wrote 10–30 / 30–50 / 1–10).
2. **Campaign tokens:** `T1`/`T2`/`T3` and the `t1-dm` style link tags are a proposal. Brad to approve; `cohortFor()` in the capture Apps Script, the live check page, the handover doc and email links must change together before any new tag is used. Confirm which roster campaigns have sent (sent campaigns keep their names).
3. **T3 job values:** whether 5–9 staff firms in `T3` take roles other than `Decision_Makers` (TBD).
4. **Will:** confirm the Dominion network configuration matches "air-gapped = no egress; inbound health-check pings and inbound patch updates only". The Business Plan fleet-ops row ("content-free telemetry → central console") and C-006's monitoring basis depend on it.
5. **Brad:** confirm the adjusted Copilot/SOC 2 wording (no claim that Copilot is not SOC 2 compliant).
6. **Copilot decision guide:** not repositioned on R6 beyond the connectivity fixes. The guide is under separate verification; its body and the Master guide's Copilot row should be rewritten to the sovereignty framing when verified.
7. **Partner terms TBD:** minimum ongoing service hours for lifetime commission; commission where an IT Reseller does not take on the client relationship; the ERMOS pricing structure document.
8. **John A. MSP Agreement v0.1:** needs a full reconcile against "ERMOS Partner Agreement - IT Reseller" Draft v0.8 as amended, which is a structural rewrite. Only an internal note and two surgical fixes were made.
9. **07 Integrators & MSPs (Partner ICP):** whether the account-tier ruling also retires partner Tier A/B and sets the partner size band. Not ruled; left unchanged.
10. **ICP Master Database:** it holds only the Partner ICP row. There are no end-client ICP rows (accounting, law, aged care and the rest) to tag with Tiers. The aged care ICP brief is pipeline task TASKS.md T-001.
11. **Dominion 10-seat minimum vs Tier 3 (1–9 staff):** a commercial question for pricing; not changed.
12. **Competitive guides' pricing callouts** (21 Sep A$999/A$1,499 etc.) look stale against the 24/28 Sep per-seat pricing. Out of scope; not touched.
13. **Not checked or not edited:** 10 Collateral pages (e.g. "ERMOS Dominion — partner offer (IT consultants and MSPs)", flyers) and Drive or PDF assets may still carry "not air-gapped" or telemetry wording. 06 Proposed Changes items (e.g. "CONFLICT: Approved Hormozi Standard still calls Dominion air-gapped", 1 Oct C-002-based claim proposals) are now moot or need re-review.
14. **Historical Decisions Log entries** (21 Sep air-gapped retirement, 24 Sep 10–50 rule, 28 Sep per-seat entry saying "Do not call Dominion air-gapped") left as history. The new entries name what they supersede.

## Errors

- Two `update_content` attempts on Claims Register: law failed on a non-matching old string (heading markup). They were retried with a smaller anchor and succeeded.
- The target-audience line on the Claude guide was not found, so that edit was skipped.
- No other errors.
