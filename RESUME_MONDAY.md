# Resume on Monday

*Written 2 Oct 2026, at the end of a long session. Read this first; it's everything you need. You don't have to remember anything else.*

---

## The one-paragraph version

We built the foundation of the ERMOS GTM engine (rules, context, four SOPs) and proved the first piece works. A 20-company pilot scrape of accounting firms in Parramatta ran cleanly for under US$0.10, and it was correctly checked against ICP_Master. The next real milestone is **wave 1**: scraping about 48 business hubs to start growing the accounting list from ~700 towards 6,000 leads. Nothing is broken, nothing is half-sent, and no emails have gone out. Everything is saved and pushed to GitHub.

---

## Monday: start here (in this order)

**Step 1: open a new Claude Code session and paste this:**

> Read `RESUME_MONDAY.md` in the 2026-gtm-ops-engine repo and walk me through Monday's steps one at a time. Use the recommended defaults unless I say otherwise.

**Step 2: one settings change (5 minutes, only you can do it)**
So Claude can run the scraper itself:
1. In Claude Code on the web, open the **cloud environment menu** in the session title bar, then **Edit**.
2. Under **Network access**, add `api.apify.com`.
3. Add an environment variable named **`APIFY_TOKEN`**, set to your Apify API token (Apify → Settings → Integrations). **Don't paste the token into the chat.**
4. Start a **new** session (the change only applies to new sessions) and paste the sentence from Step 1.

**Step 3: say "go with the defaults" to the decisions below.** Or change any you disagree with. That's the only decision-making Monday needs.

**Step 4: Claude runs wave 1** (Claude does the work and shows you the result before anything else happens).

---

## Decisions waiting, with recommended defaults

You can accept all of these in one line: *"go with the defaults"*.

| # | Decision | Recommended default | Why |
|---|---|---|---|
| 1 | Wave 1 Apify spend cap | **US$30** | Worst case for wave 1 is US$22–58. Apify stops at the cap, so you can't overspend |
| 2 | Clay credit budget | **Run the first 200 firms only, then review** | Learn the real cost per lead before committing more credits |
| 3 | Emails per mailbox per day (Smartlead) | **40** | Safe sending for 9 warmed mailboxes: about 120 new contacts a day |
| 4 | Does "6,000 leads" mean contacts or firms? | **Contacts (decision-makers)** | Matches how Smartlead counts |
| 5 | Bookkeepers in the accounting list? | **Out for now** (held, not deleted) | Keeps the first campaigns tight. You can revisit later |
| 6 | Phone numbers | **Tier 1 and Tier 2 decision-makers only** | Saves Clay credits. Tier 3 phones are found when they reply |
| 7 | Geography for wave 1 | **Metro only** (the 48-location list) | Regional areas can be wave 2 |

---

## What's already done (no action needed)

**Repos (both pushed to GitHub):**
- `BP-888/2026-gtm-ops-engine`, branch `main`: rules (`CLAUDE.md`), context files, SOPs, the task list and pilot outputs.
- `BP-888/web-site-builder`, branch `claude/brave-darwin-ohugkg`: the upgraded Google Maps scraper and the safe batch runner (`scripts/run_wave.sh`).

**SOPs written** (all drafts you can review whenever you like; nothing waits on them):

| SOP | What it does | State |
|---|---|---|
| SOP-1A-01 Backtesting | Learn from won and lost deals | Final baseline |
| SOP-2B-01 Lookalikes | Find firms similar to your best ones (Discolike, Ocean.io, AI Ark pilot) | Draft |
| **SOP-2B-02 Accounting lead pipeline** | **The one we're running:** Google Maps → check ICP_Master → Clay → ICP_Master → Smartlead | Draft v0.3, pilot passed |
| SOP-5A-01 Reply handling | Sorts Smartlead replies; Interested → HubSpot + Slack alert | Draft v0.3 |

**Rules locked in** (in `CLAUDE.md`, so every future session follows them):
- Tools: HubSpot, Clay, Smartlead, Apollo and n8n, plus Google Workspace, Notion, Slack and the Claude API. Ask before adding anything new.
- **ICP_Master (Google Drive) is the master list for cold leads. HubSpot only gets accounts that reply with interest.**
- Tiers by staff count: **T3** = 1–9, **T1** = 10–30, **T2** = 31–50. Over 50 = not contacted.
- Cost-first order: scrape cheaply → check ICP_Master → enrich only new firms → find 1–2 decision-makers → ICP_Master → Smartlead.
- Outreach asks "Reply yes". Interested people get the 3-minute AI health check survey (no booking links).
- Dominion is described as "air-gapped" (no data out; only inbound health checks and patches).

**Pilot result (2 Oct):** 20 Parramatta firms. 13 are net-new and ready for Clay. 2 were already in ICP_Master (the check worked). 3 are held (bookkeepers / unclear), and 1 has no website. Files are in `outputs/pipeline/`.

---

## After wave 1 (later in the week; no need to think about this Monday)
1. Run the new firms through Clay (enrich, tier, 1–2 decision-makers).
2. Write the results into ICP_Master (Master / Holding / Exclusions tabs).
3. Set up the three Smartlead campaigns (T1, T2, T3) with "Reply yes" copy.
4. You approve the first batch, and it goes to Smartlead.
5. Later: build the n8n automations so all of this runs by itself.

---

## Small housekeeping (whenever convenient)
- In ICP_Master, cell **A1** on the Master and Holding tabs contains stray pasted text. Change it back to `Firm name`.
- There are **two** files called ICP_Master in Drive. The real one was edited on 1 Oct; the older one (20 Aug) can be renamed "ICP_Master (old)" to avoid confusion.
- The full open-task list is in `TASKS.md` (aged care brief, partner pricing doc, Will's network check, partner agreement v0.9, tier re-mapping, partner service hours). None of it blocks the accounting sprint.

---

*If anything here looks wrong or confusing on Monday, just tell Claude, "explain step X more simply". There are no irreversible actions waiting, and nothing will be sent without your OK.*
