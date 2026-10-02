# SOP-5A-01: Automated Outbound Reply Management

| Field | Value |
|---|---|
| SOP ID | SOP-5A-01 *(Brad's brief called it SOP-5B-01. Filed under 5A because outreach replies are a 1st-party signal in the hierarchy map; the ID can be changed on request)* |
| Phase | Phase 5: Signal Tracking |
| Component | Component 5A: 1st-Party Signals (Outreach Replies). Also executes **6A** (awareness update), **7B** (lead routing) and **7D** (Slack notifications) for reply events |
| Version | v0.2 |
| Status | **Draft for Brad's review** |
| Owner | Brad (Head of Sales & Operations) |
| Last updated | 2 Oct 2026 |
| Depends on | Smartlead campaigns live (Phase 8, Automated Outbound, 1:1) · HubSpot properties from SOP-1A-01 §6.3 · SOP-1A-01 pipeline (deals start at "Discovery Booked") |
| Feeds | SOP-6A-01 Awareness Stage Assignment *(planned)* · SOP-1A-01 (loss reasons, deal sources) · Phase 8 follow-up |

---

## 1. Overview & Context

**What this SOP achieves.** Every reply to an ERMOS Smartlead campaign is automatically:
1. captured the moment it lands;
2. cleaned and classified (Interested, Neutral, Not interested, OOO);
3. enriched and summarised, but only when it's worth the spend;
4. written to **HubSpot** as the single source of truth;
5. tagged back in **Smartlead**;
6. pushed to the owning rep in **Slack** with a one-paragraph lead summary and one-click actions.

No positive reply waits in an inbox. No unsubscribe request is missed. No reply data lives anywhere but HubSpot.

**How it aligns with the Phase.** An outreach reply is a **1st-Party Signal** (Phase 5A). This SOP is also the hand-off point into later Phases:
- **6A:** a reply moves the account's Awareness Score: Considering for any engaged reply, Selecting for a meeting request.
- **7B and 7D:** the reply is routed to an owner and surfaced in Slack.
- **Phase 8:** the rep acts: sends the 3-minute AI health check survey, answers a question, or books a meeting if the prospect asks for one.

**Final Output alignment.** It feeds **Signals** and **Awareness Scores** directly, and keeps **Stakeholder Maps** current: a reply from a new person, or a referral to the right person, adds a buying-committee contact.

**Blueprint source.** Brad's extract of the Workflows.io "Automated Outbound Reply Management" playbook (6 steps: capture → enrich + summary → clean → sentiment → route + tags + Slack IDs → interactive Slack). The adaptations to ERMOS rules are listed in §2.

## 2. Visuals & References

| Reference | Location |
|---|---|
| Playbook blueprint | `00_global_context/GTM_Playbook_2026.pdf`: 1st-Party Signal Tracking → Outreach Replies; Awareness Score; Lead Routing; Slack Notifications |
| Hierarchy map | `00_global_context/gtm_playbook_2026_flow.md`, Components 5A, 6A, 7B, 7D |
| Workflows.io technical reference | "Automated Outbound Reply Management" (6-step blueprint, supplied by Brad on 2 Oct 2026; URL TBD, because workflows.io is blocked in this environment) |
| Figma: Phase 5 overview | `[FIGMA PLACEHOLDER: Phase 5 Signal Tracking frame, link TBD]` |
| Figma: reply-management flow | `[FIGMA PLACEHOLDER: SOP-5A-01 n8n flow WF-5A-A/B, link TBD]` |
| Context: tiers, buying committee, verification rule | `00_global_context/account_scoring_and_enrichment.md` |
| Context: competitor mentions and objections | `00_global_context/ermos_competitive_analysis.md` |
| Context: partner-registered accounts | `00_global_context/meeting_ermos_comarket.md` |
| HubSpot properties and pipeline | `01_backtest_and_icp/SOP-1A-01_Backtesting_Closed_Won_and_Closed_Lost.md` §6.3 and step A2 |
| Vendor docs | Smartlead webhooks: https://api.smartlead.ai/api-reference/webhooks/events · Smartlead pause/resume lead: https://api.smartlead.ai/api-reference/campaigns/pause-lead · Smartlead OOO auto-reactivate: https://helpcenter.smartlead.ai/en/articles/99-auto-reactivate-ooo-replies-with-a-delay |

**Adaptations from the Workflows.io blueprint**

| Blueprint | ERMOS version | Rule behind it |
|---|---|---|
| Outreach tools Instantly / HeyReach | **Smartlead AI** only | Core Tech Stack |
| Database Supabase / Airtable | **HubSpot** only | HubSpot is the single source of truth |
| Order: enrich (step 2) before clean and classify (steps 3–4) | **Clean → classify → then enrich only Interested and Neutral replies** | No spend on OOO, unsubscribes or "not interested" (sprawl and cost control) |
| Claude cleans HTML and signatures | **n8n Code strips HTML, quoted threads and signatures first**; Claude only standardises what's left | Cheaper, faster and deterministic; fewer tokens per reply |
| Claude re-enrols OOO | **Smartlead's native OOO detection and auto-reactivate** is used. n8n only records it | Use the core tool's built-in feature before building one |
| Waterfall phone lookups (unspecified providers) | **Clay's third-party waterfall** for contact details and phone numbers (approved providers, billed through Clay credits) | Sourcing rule: Apollo finds companies, Clay enriches people |
| Four sentiment classes | The same four classes, plus **compliance sub-labels** (unsubscribe request, referral or wrong person, meeting request) | Australian Spam Act unsubscribe handling; buying-committee mapping |

## 3. Tools Required

| Tool | Role in this SOP | Access / credentials | Stack status |
|---|---|---|---|
| **Smartlead AI** | Sends campaigns; fires `EMAIL_REPLY` (and optionally `LEAD_CATEGORY_UPDATED`) webhooks; receives category updates and pause/resume calls; native OOO auto-reactivate | API key in the n8n credential store; webhook registered per campaign or globally | **Core** |
| **n8n** | Orchestrates everything: webhook intake, cleaning, AI calls, enrichment calls, HubSpot / Smartlead writes, Slack interactivity | ERMOS n8n instance (hosting TBD); credentials for every tool here | **Core** |
| **HubSpot** | System of record: contact, company, reply log, awareness stage, owner, tasks, deals | Private app token (CRM read/write, owners read, communication preferences) | **Core** |
| **Clay** | Firmographic and contact enrichment, **including the email and phone waterfall**, for Interested and Neutral replies whose HubSpot record is incomplete. The phone waterfall runs for Interested replies only | Clay workspace; a table with a webhook source and an HTTP callback to n8n | **Core** (waterfall providers approved) |
| **Apollo** | Not used in this SOP. Apollo is the company-sourcing tool (SOP-2B-02); people and phone enrichment run through Clay | n/a | **Core** (not used here) |
| **Claude API** | (1) standardise the cleaned reply, (2) classify sentiment with confidence, (3) write the lead summary and suggested next action | API key in the n8n credential store | **Infrastructure** |
| **Slack** | Interactive rep notifications (buttons call back into n8n); owner Slack ID found by email | Slack app with `chat:write`, `users:read.email` and interactivity enabled (Request URL = n8n webhook) | **Infrastructure** |

## 4. The Absolutes (Non-negotiables)

### Before starting (go-live)
1. **One webhook path, secured.** Smartlead posts only to the n8n production webhook URL, which carries a long secret path token. Payloads from unknown `campaign_id`s are rejected.
2. **HubSpot properties exist** (§6.3), plus the SOP-1A-01 pipeline and properties.
3. **Every active Smartlead campaign has an owner** mapped in the `Campaign_Owner_Map` (HubSpot owner email, with a fallback to Brad).
4. **Smartlead OOO auto-reactivate is switched on** in every active campaign, with the AI return-date extraction enabled.
5. **Credentials live only in n8n.** No keys in Slack messages, HubSpot notes, prompts or this repo.

### Every reply (run-time)
6. **Idempotent:** each reply is processed once. Dedupe key: `sha256(campaign_id + lead_email + time_replied)`, kept in n8n and on the HubSpot contact (`ermos_last_reply_id`). Smartlead retries never cause a double alert.
7. **Unsubscribe beats everything.** Any opt-out language ("unsubscribe", "remove me", "stop emailing") sets Do Not Contact in Smartlead **and** unsubscribes the contact from all email in HubSpot, **within 1 hour**. The Spam Act 2003 allows at most 5 business days. This applies whatever the sentiment class.
8. **Clean before AI:** HTML, quoted earlier messages and signature blocks are stripped in n8n **before** text goes to the Claude API, for accuracy and token cost. (Internal GTM data handling isn't restricted by ERMOS's product promises; see CLAUDE.md.)
9. **No auto-sent human replies.** The workflow never writes or sends a reply to a prospect on its own. Any email it sends (e.g. the AI health check survey) goes out only when a rep clicks a Slack button.
10. **Spend gates:** Clay enrichment runs only for `Interested` and `Neutral` replies with incomplete HubSpot data. Clay's phone waterfall runs only for `Interested` replies with no phone already in HubSpot.
11. **HubSpot is written before Slack is posted.** The Slack message links to a HubSpot record that already holds the reply.
12. **Tier is never set from enrichment alone.** Clay headcount sets `ermos_account_tier = Unverified` until the website-verified count exists (SOP-3B-01). Tiers: T3 1–9, T1 10–30, T2 31–50.

## 5. Step-by-Step Procedure

### Part A: One-off setup (Brad, about half a day)
1. **HubSpot:** create the properties in §6.3, and add the Lead Status values `Interested`, `Neutral`, `Not interested`, `Do Not Contact`.
2. **Slack:** create the "ERMOS Reply Bot" app with interactivity on. Set its Request URL to the n8n webhook for WF-5A-B, and install it to the workspace.
3. **Smartlead:**
   - register the webhook for the `EMAIL_REPLY` event, pointing at WF-5A-A;
   - optionally also `LEAD_CATEGORY_UPDATED`, as a cross-check;
   - switch on OOO auto-reactivate with return-date extraction in every campaign;
   - confirm the lead categories in the workspace include Interested, Meeting Request, Not Interested, Do Not Contact, Information Request, Out Of Office and Wrong Person, and add any that are missing.
4. **Clay:** create the table "5A Reply Enrichment", with:
   - a webhook source;
   - columns for company firmographics, a website staff-count lookup and contact title/LinkedIn;
   - an HTTP API column that posts results back to the WF-5A-A callback webhook.
5. **n8n:** import WF-5A-A and WF-5A-B, attach credentials, and fill `Campaign_Owner_Map`.
6. **Test:** send 8 seeded test replies covering every class and sub-label (§7), and confirm HubSpot, Smartlead and Slack each end up in the right state. Then switch on production.

### Part B: Automatic run per reply (WF-5A-A; target: Slack alert within 5 minutes)

**Step 1: Capture (n8n Webhook)**
1. Receive the Smartlead `EMAIL_REPLY` payload. Its fields include `from_email`, `to_email`, `subject`, `reply_body`, `preview_text`, `time_replied`, `campaign_id`, `campaign_name` and `sequence_number`.
2. Respond 200 immediately, then process asynchronously.
3. Compute the dedupe key and stop if it's already been seen.

**Step 2: Deterministic clean (n8n Code)**
1. Strip HTML to text, and cut quoted history (lines starting with `>`, "On … wrote:" blocks, forwarded headers).
2. Remove signature blocks (sign-off patterns, phone and address blocks, legal disclaimers).
3. Normalise whitespace and keep the first 4,000 characters.
4. Record `clean_method = deterministic`.

**Step 3: Standardise and classify (Claude API, one call, JSON output)**
- **Input:** the cleaned reply body, the subject, and the campaign's vertical and sequence step. No names, emails or phones beyond what's in the body itself.
- **Output:**
  - `sentiment`: one of `Interested`, `Neutral`, `Not interested`, `OOO`;
  - `sub_labels[]`: any of `unsubscribe_request`, `meeting_request`, `referral_or_wrong_person`, `info_request`, `competitor_mentioned`, `complaint_or_legal`;
  - `confidence` (0–1);
  - `return_date` (for OOO);
  - `referred_contact` (name and role, if stated);
  - `competitor` (if named);
  - `clean_text` (the standardised reply).
- The system prompt holds the class definitions in §6.4 and requires JSON only. Malformed JSON is retried once, then flagged.

**Step 4: Branch on outcome**

| Outcome | Action |
|---|---|
| `unsubscribe_request` in any class | **Compliance path:** Smartlead → category Do Not Contact, then pause the lead in all campaigns. HubSpot → unsubscribe from all email, Lead Status `Do Not Contact`. Log the reply. Slack: an information-only message to the owner. Stop. |
| `OOO` | HubSpot: log the reply, set `ermos_reply_category = OOO` and `ermos_ooo_return_date`. Smartlead's native auto-reactivate handles the restart. n8n only checks the lead isn't paused. No enrichment, no Slack. Stop. |
| `Not interested` | Smartlead → category Not Interested. HubSpot: log, Lead Status `Not interested`, `ermos_reengage_after` = reply date + 90 days. If a deal exists: Closed Lost with a coded reason (SOP-1A-01). Slack: a low-priority digest, not an alert. Stop. |
| `Neutral` | Continue to step 5 (enrichment only), then 6, 7 and 8 with a standard alert. |
| `Interested` (including a plain "yes" to the campaign's "Reply yes" ask) | Continue to steps 5 (enrichment + phone), 6, 7 and 8 with a priority alert. |

**Step 5: Enrich (only Interested and Neutral)**
1. Look up the contact and company in HubSpot by email, and by company domain from the email.
2. If the company's vertical, verified staff count, state or LinkedIn is missing, send the domain and email to the Clay table "5A Reply Enrichment". The Clay callback returns company firmographics, a website-derived staff estimate and contact title.
3. Write enrichment to HubSpot with `ermos_enrichment_source = Clay` and tier `Unverified` (unless the website-verified count already exists).
4. **Interested only, and no phone in HubSpot:** the Clay row is sent with `run_phone_waterfall = true`, so Clay's third-party waterfall looks up mobile and direct numbers. When the result arrives (WF-5A-C), it's written to HubSpot and the Slack thread is updated ("📞 phone found" or "no phone"). Sourcing rule: Apollo finds companies; Clay enriches people.

**Step 6: Summarise (Claude API)**
- **Input:** the clean reply, classification, HubSpot company and contact fields (vertical, tier, staff count, state, title, prior replies, awareness stage, open deal, partner registration) and the competitor mention.
- **Output (JSON):**
  - `summary`: 60 words or fewer, factual, no invented facts;
  - `buyer_role_guess`: Decision Maker / Influencer / Champion / Unknown;
  - `suggested_next_action`;
  - `objections[]`;
  - `talk_track_hint`: one line, pulled from `ermos_competitive_analysis.md` positioning when a competitor is named. Air-gapped wording for Dominion follows the strict definition.

**Step 7: Route and write back**
1. **HubSpot (written first):**
   - upsert contact and company;
   - log the reply as a note on the contact and company (clean text + summary);
   - set `ermos_reply_category`, `ermos_reply_sub_labels`, `ermos_reply_confidence`, `ermos_last_reply_at`, `ermos_reply_summary`, `ermos_last_reply_id`;
   - set the Lead Status;
   - set the company's `ermos_awareness_stage` by the rules in §6.5 (never downgrade);
   - set the buying-committee association label if inferred (flagged as inferred);
   - for `referral_or_wrong_person`, create the referred contact if a name and role are given (no email guessing), associate them with the company, and set a task for the owner.
2. **Owner:** use the HubSpot contact owner. If there is none, the `Campaign_Owner_Map` owner. If none, Brad. For partner-registered companies, the ERMOS owner gets the alert with a "Partner account: <partner name>" banner. Partner routing rules aren't ruled yet (see `meeting_ermos_comarket.md`).
3. **Smartlead:** set the lead category (Interested / Meeting Request / Information Request / Wrong Person) to match. For Interested, pause the lead's sequence so no automated follow-up goes out while the rep handles it.
4. **Slack ID:** call `users.lookupByEmail` with the owner's email. If that fails, post to the fallback channel and tag Brad.
5. **HubSpot task:** create one for the owner, due within 1 business hour (Interested) or 1 business day (Neutral), in Australia/Sydney time.

**Step 8: Interactive Slack notification**
Post a DM to the owner (and to the pipeline channel for Interested). The message holds:
- a header with the class, plus 📅 if it's a meeting request;
- the firm, vertical, tier (or `Unverified`), staff count and state;
- the contact and title;
- the summary, objections and talk-track hint;
- the latest reply (clean text, trimmed);
- phone status.

Buttons are handled by WF-5A-B:

| Button | Action in n8n |
|---|---|
| ✋ **Claim** | Sets the HubSpot owner to the clicker; updates the message ("Claimed by …") |
| 📋 **Send AI Health Check Survey** | Sends the approved survey reply (link to the **3-minute online AI health check survey**) in-thread through Smartlead from the campaign's mailbox. Logs it in HubSpot, and sets `ermos_survey_sent_at` |
| 💼 **Create deal** | Creates a HubSpot deal in "ERMOS New Business" at **Discovery Booked**. Source is `Outbound: Automated`, associated with company and contact (SOP-1A-01 fields) |
| 🙅 **Not interested** | Reclassifies as Not interested and runs that path (with reason picker) |
| 🚫 **Do not contact** | Runs the compliance path |
| ⏰ **Snooze 2 days** | Moves the HubSpot task due date and re-pings in 2 business days |
| 🔗 Open in HubSpot / 🔗 Open in Smartlead | Link buttons (no callback) |

### Part C: Human routine
- **Reps:** act on every Interested alert within 1 business hour, and every Neutral one within 1 business day (Sydney time).
- **Brad, weekly (20 minutes):** review the classification QA sample (§7) and the flag queue (§8).

## 6. Data Flow & Automation

### 6.1 n8n workflow WF-5A-A: "5A Reply Intake"

| # | Node | Purpose | Notes |
|---|---|---|---|
| 1 | **Webhook** (POST, secret path) | Receive Smartlead `EMAIL_REPLY` | Respond 200 immediately; reject unknown `campaign_id` |
| 2 | **Code: Dedupe** | Hash key; check n8n static data | Duplicate → stop |
| 3 | **Code: Clean** | Deterministic strip (§5 step 2) | n/a |
| 4 | **HTTP Request: Claude API** (classify) | JSON classification (§6.4) | Retry once on malformed JSON or 5xx; then flag `R05` |
| 5 | **Switch: outcome** | Unsubscribe / OOO / Not interested / Neutral / Interested | Unsubscribe is checked first |
| 6a | **Smartlead HTTP: category + pause** | Compliance / Not interested / Interested paths | Smartlead lead-category update endpoint and `.../leads/{lead_id}/pause` |
| 6b | **HubSpot: communication preferences** | Unsubscribe from all email (compliance path) | n/a |
| 7 | **HubSpot: Search / Upsert** contact + company | Load context | By email, then domain |
| 8 | **IF: needs enrichment** → **HTTP: Clay table webhook** → **Wait (webhook resume)** | Clay enrichment, resumed by the Clay callback | Timeout 10 minutes, then continue without (flag `R07`) |
| 9 | **IF: Interested and no phone** → set `run_phone_waterfall = true` on the Clay row (step 8) | Clay's phone waterfall column runs only when this flag is true | The phone result returns on the same Clay callback, or a second callback if it finishes later (WF-5A-C) |
| 10 | **HTTP Request: Claude API** (summary) | Lead summary JSON | n/a |
| 11 | **HubSpot: Update** contact, company, note, task, association labels | Write-back (HubSpot written first) | n/a |
| 12 | **Slack: users.lookupByEmail** → **Slack: chat.postMessage** (Block Kit with buttons) | Interactive alert | Store the Slack `ts` on the HubSpot contact (`ermos_slack_alert_ts`) to update the thread later |
| E | **Error Workflow** | Any failure → post the raw reply to the fallback channel as "UNPROCESSED REPLY", with campaign and time | A reply is never silently lost |

**WF-5A-B "5A Slack Actions":** Webhook (Slack interactivity) → verify the Slack signing secret → Switch on `action_id` → HubSpot / Smartlead calls (table in §5 step 8) → `chat.update` the original message.

**WF-5A-C "5A Clay Phone Callback":** Webhook (Clay HTTP column, fires when the phone waterfall completes) → match `reply_id` → HubSpot update phone → Slack thread reply "📞 phone found" (or "no phone").

**Optional cross-check WF-5A-D:** the Smartlead `LEAD_CATEGORY_UPDATED` webhook → compare with ERMOS's classification → a mismatch raises flag `R03`.

### 6.2 Normalised reply object (inside n8n)

| Field | Source |
|---|---|
| `reply_id` | sha256 dedupe key |
| `campaign_id`, `campaign_name`, `sequence_number` | Smartlead |
| `lead_email`, `mailbox_email` | Smartlead (`from_email`, `to_email`) |
| `time_replied` | Smartlead, converted to Australia/Sydney |
| `subject`, `raw_body` | Smartlead (raw kept only in n8n execution data, which is pruned; see Open Items) |
| `clean_text` | n8n Code, then Claude |
| `sentiment`, `sub_labels`, `confidence`, `return_date`, `competitor`, `referred_contact` | Claude classify |
| `summary`, `buyer_role_guess`, `suggested_next_action`, `objections`, `talk_track_hint` | Claude summary |
| `owner_email`, `slack_user_id` | HubSpot / Campaign_Owner_Map / Slack |

### 6.3 HubSpot properties (in addition to SOP-1A-01 §6.3)

| Object | Internal name | Type | Values |
|---|---|---|---|
| Contact | `ermos_reply_category` | Dropdown | `Interested` · `Neutral` · `Not interested` · `OOO` · `Do Not Contact` |
| Contact | `ermos_reply_sub_labels` | Multi-checkbox | `unsubscribe_request` · `meeting_request` · `referral_or_wrong_person` · `info_request` · `competitor_mentioned` · `complaint_or_legal` |
| Contact | `ermos_reply_confidence` | Number (0–1) | n/a |
| Contact | `ermos_reply_summary` | Multi-line text | Claude summary (latest) |
| Contact | `ermos_last_reply_at` | Datetime | Sydney time |
| Contact | `ermos_last_reply_id` | Single-line text | Dedupe key |
| Contact | `ermos_ooo_return_date` | Date | n/a |
| Contact | `ermos_reengage_after` | Date | Not-interested + 90 days |
| Contact | `ermos_phone_lookup` | Dropdown | `found_clay` · `not_found` · `not_requested` |
| Contact | `ermos_survey_sent_at` | Datetime | Set by the "Send AI Health Check Survey" button |
| Contact | `ermos_slack_alert_ts` | Single-line text | For thread updates |
| Contact | `ermos_enrichment_source` | Dropdown | `Clay` · `Apollo` · `Manual` · `Website verified` |
| Company | `ermos_awareness_stage` | Dropdown | `Identified` · `Aware` · `Interested` · `Considering` · `Selecting` |
| Company | `ermos_awareness_updated_at` | Datetime | n/a |

### 6.4 Classification definitions (in the Claude system prompt)
- **Interested:** wants to learn more, talk, see pricing or trial, or forwards internally with intent. Includes meeting requests (sub-label `meeting_request`).
- **Neutral:** asks a question or for information without committing, says "maybe later", or is a non-committal acknowledgement. Includes `info_request` and `referral_or_wrong_person` where no interest is expressed.
- **Not interested:** declines, already has a solution, or isn't relevant. Unsubscribe wording also adds `unsubscribe_request`.
- **OOO:** an automatic out-of-office or leave notice. Extract `return_date` if stated.
- **Confidence:** below 0.85 always flags (§8).

### 6.5 Awareness stage rules (company-level; never downgrade)

| Reply | `ermos_awareness_stage` |
|---|---|
| Interested + `meeting_request` | **Selecting** (high-intent: asking to meet) |
| Interested (no meeting request) | **Considering** (active engagement) |
| Neutral | **Considering** |
| Not interested / Do Not Contact | Unchanged (the reply is logged; re-engagement date set) |
| OOO | Unchanged |

### 6.6 Data flow summary

```
Smartlead (EMAIL_REPLY) ──webhook──► n8n WF-5A-A
   ├─ clean (n8n Code) ─► classify (Claude API)
   ├─ Unsubscribe ─► Smartlead DNC + pause ─► HubSpot unsubscribe ─► Slack info            [stop]
   ├─ OOO ─► HubSpot log (Smartlead native auto-reactivate restarts later)                  [stop]
   ├─ Not interested ─► Smartlead category ─► HubSpot log + re-engage date ─► Slack digest  [stop]
   └─ Interested / Neutral
        ├─ HubSpot lookup ─► (if gaps) Clay table ─callback─► n8n
        ├─ (Interested, no phone) Clay phone waterfall ─callback─► WF-5A-C ─► HubSpot phone + Slack thread
        ├─ summary (Claude API)
        ├─► HubSpot: contact, company, note, task, awareness stage   [system of record]
        ├─► Smartlead: category, pause sequence (Interested)
        └─► Slack DM + buttons ──clicks──► n8n WF-5A-B ─► HubSpot (owner, deal) / Smartlead (AI health check survey reply, DNC)
```

**System of record:** HubSpot. Smartlead holds sending state only. Slack is a notification surface, never a store. n8n execution data is transient.

## 7. Quality Assurance (QA) Guidelines

### What "Good" Looks Like

| Metric | Target |
|---|---|
| Interested alert latency | 95% within 5 minutes of `time_replied` |
| Unsubscribe compliance | 100% actioned in Smartlead and HubSpot within 1 hour (legal maximum 5 business days) |
| Classification accuracy | ≥ 90% agreement with Brad's labels on a weekly random sample of 20 replies (all classes represented) |
| Duplicate alerts | 0 |
| HubSpot completeness | 100% of replies logged on the contact; 100% of Interested have an owner and a task |
| Rep response | Interested actioned (button click or HubSpot activity) within 1 business hour, 90% of the time |
| Spend discipline | 0 enrichment or phone calls on OOO, unsubscribe or Not interested replies |

**A good alert reads like:** "🔥 INTERESTED: *[Firm]* (accounting, T1, 18 staff, NSW). Practice manager replied 'Yes, interested. We've been worried about staff pasting client files into ChatGPT.' Summary: positive reply to the 'Reply yes' ask; concern is staff using public AI with client data. Hint: lead with onshore processing and control. Next step: send the AI health check survey. [Claim] [Send AI Health Check Survey] [Create deal] …"

### What "Bad" Looks Like
- An unsubscribe treated as "Not interested" only, with the lead still sequenced elsewhere.
- Enrichment or phone credits spent on OOO auto-replies.
- Quoted email history or signatures classified as the reply, e.g. a "Thanks!" from an old thread read as Interested.
- Slack alerts pointing to a HubSpot record that doesn't have the reply yet.
- Two alerts for one reply (webhook retry), or alerts to the wrong rep.
- A tier set from Clay headcount, as if it were verified.
- A calendar or booking link sent as the first response: the next step is the AI health check survey.
- Automated follow-ups still going out after a prospect said "yes, let's talk".
- Invented details in the summary (a title, headcount or competitor not in the data).

## 8. Exception Handling

### Auto-Pass Criteria
These complete with no human review beyond the rep's normal alert:
1. **OOO** with confidence ≥ 0.85: logged, and Smartlead's native restart handles it.
2. **Not interested** with confidence ≥ 0.85 and no `complaint_or_legal`: categorised, logged and added to the digest.
3. **Unsubscribe** wording detected (any confidence): the compliance path runs automatically. Over-honouring an ambiguous opt-out is the safe default.
4. **Interested / Neutral** with confidence ≥ 0.85: full path. The human step is the rep acting on the alert, not a review.

### Flagging Triggers
Flags post to the fallback channel and set a HubSpot task for Brad. Brad reviews them weekly, or immediately for `R04` and `R06`.

| Code | Trigger | Handling |
|---|---|---|
| `R01_low_confidence` | Classification confidence < 0.85 | Alert goes out labelled "Needs review"; Brad confirms the class |
| `R02_mixed_signal` | Positive wording plus opt-out wording | Compliance path runs anyway; Brad checks whether to reach out manually and carefully |
| `R03_smartlead_mismatch` | Smartlead's own category disagrees with ERMOS's classification | Brad decides; the sample feeds prompt tuning |
| `R04_complaint_or_legal` | Complaint, threat, legal or privacy-request language | Pause the lead everywhere; Brad handles it personally |
| `R05_ai_failure` | Claude returned an error or malformed JSON twice | Raw reply goes to Slack as "UNPROCESSED". Owner handles it manually and labels it |
| `R06_partner_account` | Company is registered to a partner (backend instance) | Alert to the ERMOS owner with a partner banner. Routing waits for the partner rules |
| `R07_enrichment_timeout` | Clay callback didn't arrive within 10 minutes | Continue without it; re-queue enrichment |
| `R08_out_of_icp` | Website-verified staff count over 50, or the firm is clearly not Australian | Alert still goes out, with a "Disqualified by ICP" banner; Brad decides |
| `R09_unknown_sender` | Reply from an address that isn't the lead (forward or colleague) | Treat as a possible new buying-committee contact. Owner confirms the association |
| `R10_owner_unresolved` | No HubSpot owner, campaign owner or Slack ID found | Post to the fallback channel and tag Brad |

---

## Open Items

1. **SOP ID:** confirm SOP-5A-01 (1st-party pillar) or rename to SOP-5B-01 as in the brief.
2. **Resolved 2 Oct 2026 (Brad):** Clay's waterfall is the approved phone and contact source; there's no privacy restriction on the internal engine using the Claude API; no booking links (the CTA is "Reply yes" → AI health check survey).
3. **Survey link and reply wording:** the URL of the 3-minute online AI health check survey, and the approved in-thread reply that sends it. The wording follows the Hormozi Standard (no hyphens in prospect copy). Note: Notion's Hormozi Standard names the lead magnet "The 3-Minute AI Exposure Check". Confirm whether that's the same asset, and use one name everywhere.
4. **Survey completion signal:** when a prospect completes the survey, that's a 1st-party signal that should move the account to **Selecting**. It needs its own capture workflow (planned under 5A, Gated Content / Meeting Forms).
5. **Owner map:** the `Campaign_Owner_Map` entries for each live Smartlead campaign, and the fallback Slack channel name.
6. **Smartlead endpoints:** confirm the lead-category update endpoint path and the workspace's category list in the Smartlead API reference while building.
7. **n8n execution-data retention:** set pruning so raw reply bodies aren't kept longer than needed (suggest 14 days).
8. **Re-engage window:** confirm 90 days for Not interested.
9. **Workflows.io page URL:** add it for the reference table.

## Change Log

| Version | Date | Author | Change |
|---|---|---|---|
| v0.2 | 2 Oct 2026 | Claude Code for Brad | Clay waterfall replaces Apollo for phone and contact enrichment; privacy constraint removed for the internal engine; "Send booking link" replaced by "Send AI Health Check Survey"; "Reply yes" treated as Interested |
| v0.1 | 2 Oct 2026 | Claude Code for Brad | First draft from Brad's Workflows.io 6-step blueprint, adapted to the Core Tech Stack (Smartlead, HubSpot, n8n, Clay, Apollo, Claude API, Slack) |
