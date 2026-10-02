# Handoff: project-agent run (moved from the cloud session to local, 2026-09-26)

Yusef asked for the project-agent to run over **all** his plans: remove redundancies and take on tasks. The cloud session started it and was then told to move the run to his local session. The 5 cloud agents were stopped mid-run.

- **Tattoo, career and debt:** unknown how far they got.
- **Home and travel:** had finished research but made **no Notion writes**.

Re-check the current Notion state before writing anything, so nothing gets done twice.

## Setup (local session)

1. Get the agent definition and the latest CLAUDE.md: `git fetch origin claude/gallant-curie-94hu8s` and check out or merge that branch in the `yusefshokry/Claud` repo. It holds:
   - `.claude/agents/project-agent.md`
   - `.claude/agents/job-hunter.md`
   - `.claude/skills/plan-gaps/SKILL.md`
   - `CLAUDE.md`
2. INBOX now has an **`Owner`** select (Yusef / Claude). Claude-owned tasks are research the agent took on; the cloud daily planner (`trig_018QcSWFB6jqndWKZDiv8Fgn`) never calendars them.

## Run

Launch one `project-agent` per cluster, in parallel if usage allows, otherwise one at a time. Each agent follows `.claude/agents/project-agent.md`.

Tell each agent:
- Don't call the question tool. Return every question in its `QUESTIONS` block, with no limit.
- Other agents cover the other clusters, so don't touch Goals outside its list.

1. **Tattoo:**
   - Work full time as an artist at a tattoo studio: https://app.notion.com/358e4241b1a3809dbd23f80324d6520e
   - Tattoo career game plan: https://app.notion.com/2c5e4241b1a38003a0f4f89b43c60849
   - Tattoo portfolio: https://app.notion.com/358e4241b1a380ab9359fc379a917b1a
   - Compete in tattoo conventions / competitions: https://app.notion.com/3e7e4241b1a381da9f9be6c919a4159e
   - The portfolio book row (https://app.notion.com/360e4241b1a3800ebd4fe898ae4ee928) and the "best 15" link row (https://app.notion.com/360e4241b1a380ef895ff3f396e3f486), plus their parent (https://app.notion.com/3dee4241b1a380ceb473f0908a3d103d)
   - Notes: Shop rows are context only. Cross-plan duplicates are likely, so merge them. The portfolio is locked to Linework.
2. **Career & income:**
   - Find a better-paying job: https://app.notion.com/3e7e4241b1a3816395fdd61c6109f8eb. Don't run a job search and don't add Job Lead rows.
   - VIDA Reston JMA prep: https://app.notion.com/2cae4241b1a3809c8b6fc5a69b3674a5 and its parent https://app.notion.com/3dde4241b1a380d39281e687668c2729. The Reston presentation and GM outreach stay **on hold** until VIDA replies.
   - Make 4k a month: https://app.notion.com/31ee4241b1a3804cbb77c016156facab
   - Electrician program: https://app.notion.com/334e4241b1a3809eaf42f9934b70232c
   - claud finance proocals: https://app.notion.com/3e5e4241b1a38014afc7c6dfaadfc46f
3. **Debt:**
   - Pay outstanding loan harming my credit: https://app.notion.com/35ae4241b1a380ea9114fa2a31c3e190
   - Skip the Frozen PayPal and Adobe items and their sub-tasks.
   - Sources: Gmail, Era_Context (read-only) and his Journal. Never pay anyone or contact a creditor; drafts to himself only.
4. **Home:**
   - Decorate: https://app.notion.com/322e4241b1a380a38b12daabeb3f584d
   - Keep a very clean apartment: https://app.notion.com/3e7e4241b1a3818a8a2af35b5309a4dd
   - Move to new apartment: https://app.notion.com/35ae4241b1a3803a8543e5e4b66ee54e. He has no car, so look Metro-reachable.
   - Meal prep every week: https://app.notion.com/3e7e4241b1a38103a74ec046722aa29d. The Weekly Meal Planner routine already covers meals.
   - Get a cat: https://app.notion.com/322e4241b1a38025a265c21e92e1f4a5
   - Leave Chore and grocery rows alone. Raise the Decorate-vs-Move conflict as a question.
5. **Travel & personal:**
   - Go on Vacations: https://app.notion.com/358e4241b1a380538008d6f7fb20fefd. It covers China (blocked by "Apply for passport"), Greenland and the beach Airbnb.
   - Lease Car: https://app.notion.com/358e4241b1a380069f40f72a49fa6d90
   - Fluent in Arabic: https://app.notion.com/358e4241b1a380938ff4c5c9afe10e9d
   - Get glp 1 RX: https://app.notion.com/3b6e4241b1a380c5b4cfccb093dee59f. Factual process and coverage info only.
   - Goal Setting Audio: https://app.notion.com/2c5e4241b1a380cc90b6c92f497cb427
   - Leave XMAS and Thanksgiving alone.

## After

1. Give Yusef a short summary per cluster covering:
   - what was researched, plus the key findings
   - the tasks Claude took on
   - the redundancies merged
   - each plan's next action
2. Ask him **all** the questions from the `QUESTIONS` blocks, 4 per question-tool call, with the recommended option first. This is the one exception to his "don't ask" rule.
3. Send his answers back to the matching agent so it can finish.
