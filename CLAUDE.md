# About Yusef

Personal context file, loaded automatically at the start of every session in this repo. Keep it current as things change — don't let it go stale.

- Name: Yusef Shokry
- Email: yusef.shokry@gmail.com
- Timezone: America/New_York

## Current goals (as of Sep 2026)

Stated directly, unfiltered — treat these as real, not aspirational filler:

1. **Build a tattoo portfolio** — already has a real, detailed plan (see below), just needs execution.
2. **Get into a tattoo shop full-time / land an apprenticeship.**
3. **Compete in tattoo conventions/competitions** — net new, no plan yet.
4. **Practice as much as possible** — largely covered by the portfolio project's weekly workflow, not a separate goal.
5. **Work out 4–5x a week.**
6. **Keep a very clean apartment.**
7. **Meal prep every week.**
8. **Find a better-paying job** — likely a day job distinct from the tattoo career, since the tattoo plan assumes working another job in the meantime.

Goals 1, 2, and 4 are all facets of one Notion Goal: "Work full time as an artist at a tattoo studio." Goals 3, 5, 6, 7, 8 are new as of this conversation and may not be tagged/created in Notion yet — check before assuming they exist.

## The Notion productivity system

Workspace hub: the **"Data Base"** page (https://app.notion.com/p/2c5e4241b1a380d89335ee6c00b40316), which contains:

- **INBOX database** (`collection://2c5e4241-b1a3-80b5-bedb-000b9ea93719`) — a single GTD-style capture database for everything: goals, projects, tasks, chores, journal entries, gratitude. Key properties:
  - `Area (1)` (multi-select): Goal / Project / Task / Chore / Journal / Gratitude — what kind of item it is
  - `Area` (multi-select): life domain — Career, Financial, Portfolio, Health, Home, Education, social, organize, Journal, Adhoc
  - `Priority`: Urgent / Important / Maintenance / Optional
  - `Year` (2026/2027/2028) and `Quarter` (Q1–Q4 / Whole Year) — added this conversation, for the year/quarter dashboard views
  - `Parent item` / `Sub-item` relations — builds the Goal → Project → Task hierarchy
  - `Recurrence`, `Chore Day` (Day 1 / Day 2) — for recurring chores
- Views on Data Base page: TODAY, INBOX (with TASKS/PROJECTS/GOALS/CHORES/SORT/Journal sub-views), plus a **"🎯 GOALS: Year & Quarter Overview"** section added this conversation:
  - Year Overview (board, grouped by Year)
  - Quarter Overview (board, grouped by Quarter, filtered to Year=2026)
  - Goals Calendar (2026) — single-month calendar view
  - Full Year Timeline (2026) — whole-year Gantt-style timeline
  - Q1–Q4 Timelines (2026) — one Timeline view per quarter, ~3 months wide each (Notion has no native 3-month calendar grid — this is the workaround)
- **"Tattoo portfolio" project** (https://app.notion.com/p/358e4241b1a380ab9359fc379a917b1a) — a genuinely thorough 12-week plan: shop-list building, portfolio piece quotas (25–35 pieces, flash sheets, studies), weekly production workflow, shop outreach scripts, follow-up rules, and month-by-month milestones. This already exists — don't recreate it, just execute and keep it tagged into the Year/Quarter system.
- **Weekly Planning Ritual** page — a 15–20 min weekly reset: load shifts first, pick 1–2 Chore Days, pick 3–5 Freelance/Portfolio priorities for the week by Priority tag, check only "today" daily.
- **Time Block Log** page — running log of plan-vs-actual diffs (see routines below).
- **Journal** template (in INBOX) — daily entries with First action / Top 3 / Gratitude / Brain dump / Obstacle / Countermove / Review sections.

## Google Calendar structure — CRITICAL, do not forget this

Yusef does **not** use one calendar. He has separate dedicated Google Calendars per life category, and any calendar work must read/write the correct one per category — never default to "primary" only:

- **Day Job (Aura Spa)**: `578cc7fbd1b9c7db2fdd164357b355bbb87c0e2f83c7cb5c6aab8b24a727653f@group.calendar.google.com` — real fixed work shifts.
- **Work out**: `186f72fc85e73cf340e6caa0b8db80dda6ebc5334bd0b9b4b8ea666506f03813@group.calendar.google.com` — see WORKOUT CADENCE below.
- **Domestic Work**: `c88ab45ca2997c86699233b2da8363ddaa9898625b007b862bef87781c93b75d@group.calendar.google.com` — chores (e.g. recurring "Home Reset").
- **Deep work**: `family14328514273165591333@group.calendar.google.com` — the **single** calendar for all focused/portfolio/career work (tattoo practice, portfolio pieces, shop outreach, job search, interview prep, study). Consolidated onto this one calendar; do not split by sub-category.
- **Deep work (Education/study)**: `1ed72572c6fda9c0c79e2b8d6fbf0ccbfd4bfcd24480e0034505b8f7e00c5393@group.calendar.google.com` and **Deep work (Portfolio)**: `a840d9cf5e81af47d79e9a0c415f20fed71907d1737b5dbadb4572c02ecabb84@group.calendar.google.com` — legacy calendars, may still hold old/manual events; read-only for busy-time checks, never write new events here.
- **Social**: `8633e1e133451641ead284fd8dadb923a77f4dfdd5705dd6004c4429012592d1@group.calendar.google.com`
- **Habbits**: `15215199da3cd0c11908b7743b7393cd001ed09e04a8d06e07220e5ff916a2f3@group.calendar.google.com` — light routine/checklist blocks. NOT a hard blocker for scheduling — other blocks may overlap them.
- **Swim / personal**: his actual "primary" calendar (`yusef.shokry@gmail.com`), summary "Swim Open Hour" — recurring real Swim hours. Blocks time but is excluded from category tracking/reporting ("swim block should always be ignored" for reporting purposes, though it still counts as busy time for scheduling).

Every calendar above is a hard blocker for scheduling purposes except Habbits.

**Plan-then-prune philosophy**: a calendar block is an intention. If Yusef does the thing, he leaves the block; if not, he deletes it himself. Automation should never delete, move, or resize a block Yusef created himself — only he prunes his own blocks. He also actively edits blocks in real time (including ones automation created), so always re-fetch current state fresh rather than trusting a prior plan.

Google Calendar's description field does **not** reliably render `<a href>` HTML links in Yusef's client — use plain bare URLs, not HTML anchors.

## Standing automations (Routines)

- **"Morning brief"** (weekdays, 12:00 UTC) — renders the `/morning` skill brief. Custom Sections added this conversation: "This Quarter's Goals" (pulled from Notion, dropped if empty) and "Daily Gratitude" (always renders, links to today's Journal entry if one exists).
- **"Morning time-block snapshot"** (9:00 AM ET) and **"Evening plan vs. actual"** (6:30 PM ET) — diff the day's actual calendar against the morning snapshot, message a summary, and log it to the Time Block Log page.
- **"Daily time-block planner"** (trigger `trig_01SxVC4k5qacHY1gwWhAWht8`, fires 13:15 UTC / ~9:15 AM ET) — reads all the calendars above plus open Notion INBOX tasks (`Area (1)` contains "Task", not checked), then auto-schedules new blocks into real open gaps. Key standing rules baked into this Routine (see the trigger's own prompt for full detail — this is a summary for other sessions/environments):
  - **Earliest start 9:30am ET** on any calendar — Yusef wakes ~8am and needs time before he can focus.
  - **Workout cadence**: maintains roughly one ~2-hour Work out block every day (generally evening, ~18:00-22:00, sliding around that day's Day Job shift), as a standing daily habit — not tied to a Notion task. Never double-books a day that already has one.
  - **Planning horizon**: Work out and Deep work are scheduled as far out as the Day Job calendar is already booked (checks up to +30 days for the furthest real shift). Domestic Work / Day-Job-prep tasks stay scoped to today only. Paces roughly a week of real Deep work progress per run rather than dumping the whole horizon at once.
  - **One portfolio goal per week** (the most important Deep work pacing rule): Yusef gets through about one portfolio/tattoo goal per week, not one per session — a goal is either a specific flash/design piece (pipeline: digital file → print → stencil → dry → tattoo, each its own session) or an ongoing skill-practice goal (e.g. linework/line-consistency drills — worked in reps across the week). Every individual portfolio session needs a **minimum of 90 minutes** (multi-step, can take hours) — never schedule shorter. Never start a second portfolio goal in the same week just because there's spare time.
  - **Standing permission to delete**: the Routine may delete/replace Deep work events *it created itself* without asking first (e.g. to fix a mistake or reorganize the week) — never events Yusef created himself.
  - **Standing permission to edit descriptions**: may refresh the description (never the time) of a Deep work block Yusef created himself, when it's generic/stale, to add a concrete intention.
  - Description field = forward-looking **intentions** only (what he plans to do), never phrased as already-done — that's separate from his own "ta-da list" of what he actually completed, which he adds himself afterward.
- **"VIDA Reston application - watch for reply"** (trigger `trig_01NSVG4G9KDA3hNLcihmk1md`, daily 13:00 UTC) — quiet Gmail check for a real reply to the Reston JMA application; stays silent unless an actual reply (not a bulk/list email) arrives.

## Other tools built

- **Quarter Glance** artifact — a standalone 3-month calendar page (prev/next month navigation, click a day to leave a note, saved to browser local storage only — not synced to Notion).

## Working preferences — important

- Prefers **structure only**: build the scaffolding (fields, views, templates) but let him fill in and tag his own data rather than auto-populating or guessing on his behalf.
- Gets frustrated by tooling for its own sake — infrastructure with nothing real in it isn't help. When in doubt, prioritize getting one real, concrete next action in front of him over building another view or section.
- Currently mid-transition: building a tattoo career while likely holding a day job; also doing a debt/credit investigation (mentioned in an earlier Journal entry) — relevant context for the "better paying job" and financial goals.
- Swims regularly (recurring "Swim hours" calendar blocks, ~mornings and evenings).
- **Standing permanent full permission (given 2026-09-22, widened 2026-09-22, generalized to everything 2026-09-22): default to acting, not asking.** He'd rather have something done and fix a mistake afterward than be stopped for approval mid-task. This applies across the board — calendar (creating/moving/deleting events, inviting people), Notion (pages, tasks, databases, routine prompts), Gmail, and any other tool available in this environment — not just the time-block planning system. Look up whatever's needed on your own (attendee emails from calendar/Gmail history, task URLs, etc.), do the thing, then report what was done. Don't pause mid-task to ask "should I proceed" or preview a plan before acting. The only things that still warrant a check-in first are truly catastrophic/irreversible actions with no fix-it-afterward path (e.g. sending real money, git force-push or history rewrite, permanently deleting an entire database/workspace with no recovery) — genuinely rare, and even then err toward finding the reversible version of the action rather than stalling.
