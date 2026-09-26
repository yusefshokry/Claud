---
name: plan-gaps
description: Find gaps in Yusef's Notion plans (Goals, Projects, Tasks) and flesh them out into concrete, ordered, dependency-linked next actions. Use when Yusef says "flesh out", "fill the gaps", "break this down", "what's the next step for X", "plan gaps", or runs /plan-gaps — for one named plan or the whole INBOX.
---

# Plan Gaps

Turn vague or stalled plans in Yusef's Notion INBOX into chains of small, concrete actions, with real dependencies linked, so every open plan has a doable next step. This runs on demand (it replaced the daily "Plan Gap Filler" routine on 2026-09-26, because Yusef wants to steer it rather than have it fire unattended).

## Scope

- **Argument given** (e.g. `/plan-gaps apartment`, "flesh out the XMAS plan"): work only on that plan and everything under it. Find it by title search in the INBOX; if several match, take the closest and say which one you used.
- **No argument**: sweep every open Goal, Project and Task. Be comprehensive: no cap on how many items you cover. Yusef explicitly asked for thorough over minimal.

## Data

- INBOX data source: `collection://2c5e4241-b1a3-80b5-bedb-000b9ea93719`
- Fields that matter: `Inbox` (title), `.` (done checkbox, `__YES__`/`__NO__`), `Area (1)` (Goal / Project / Task / Chore / Journal / Gratitude / Inventory / Shop / Question), `Area` (life domain), `Priority` (Urgent / Important / **Maintence** — that spelling / Optional), `Year`, `Quarter`, `Date`, `Parent item` / `Sub-item` (hierarchy), **`Blocked by` / `Blocking`** (cross-plan dependencies), `today`.
- Shop outreach lives in INBOX rows with `Area (1)` = Shop (`Shop Tier`, `Outreach Status`, `First Visit`, `Next Follow-up`, `Who to Approach`, `Shop Notes`) — not in Contacts. Contacts (`collection://fa3d2aa0-501f-49e0-85a8-2615f0fb2c5b`) holds people.
- Query with `notion-query-data-sources` (SQL). Sub-item/Blocked-by columns come back as URL arrays; query those URLs to get titles and done state.

## 1. Find the gaps

Pull every unchecked row in scope whose `Area (1)` contains Goal, Project or Task, plus its sub-items (open and done). A gap is:

- a Goal with no open Project/Task under it
- a Project with no open Task under it
- a Task that is really several steps, is vague ("plan X", "figure out Y", a bare noun, a "how do I…?" question), or waits on something that hasn't happened (info from a person, a booking, a purchase, a document, an appointment) — and has no open sub-tasks
- a chain whose open steps don't actually reach the parent's outcome (missing middle or last step)
- a dated item within ~90 days with no prep steps
- a cross-plan dependency that isn't linked yet (e.g. a trip that needs the passport task first)
- one of Yusef's stated goals with no Goal row at all (see CLAUDE.md "Current goals"; check for similar titles first)

**Skip:** Chores, Journal, Gratitude, Inventory rows (unless one hides a real purchase decision), done items, and clutter (untitled rows, "(1)" duplicates, "Test", bare Photoshop/Clip Studio hotkey names). List clutter in the report; never touch it.

**Respect holds** (read CLAUDE.md fresh — it is the source of truth; at time of writing):
- FROZEN: "pay paypal Debt" and "Negotiate with adobe Support to wave cancel fee." and their "⏸ FROZEN" sub-tasks.
- Reston presentation + GM/membership-advisor outreach: on hold until VIDA Reston actually replies.
- Portfolio locked to Linework (reps mode): don't build chains for other portfolio pieces.
- Things Yusef says are already done (e.g. Thanksgiving time off requested) are done.

## 2. Read before you write

For each gap, fetch the page and its parent. Pull real facts from wherever they live — the page body, related Notion pages (e.g. the Tattoo career game plan), Gmail, Google Calendar, Era_Context finance data. The quality bar is **specific to Yusef's actual situation**: names, amounts, phone numbers, links, dates, what's already been done. A step that could appear in anyone's to-do list ("set a budget", "do research") is only acceptable when it's genuinely the next move, and even then it should carry his real numbers in the Why line.

Check existing structures before inventing new ones (the shop list is Shop rows; people are Contacts; groceries are Grosseries children; gift ideas are the 🎁 Gift Ideas table on the XMAS page).

## 3. Write the chain

Create sub-tasks with `notion-create-pages` in the INBOX data source:

- `Parent item` = the gap's URL. `Area (1)` = `["Task"]`. Copy `Area`, `Priority`, `Year`, `Quarter` from the parent.
- As many steps as the outcome really needs, first action to finish line (usually 3–8). A Goal gets milestones and the first concrete actions under the first one.
- Title: one physical action, verb first, finishable in one sitting, numbered in order: `1) Text Matt: ask what flight home he booked`. Continue numbering when extending an existing chain.
- Missing info is its own step: `Ask <person> for <thing>`. Never guess names, dates or prices.
- Body: `Why: <how this unblocks the parent, with the specific facts>` then `Added by /plan-gaps on <date>`.
- **Link real dependencies with `Blocked by`** (value = array of page URLs) whenever a step can't start until something in *another* plan is done — e.g. China trip ← Apply for passport; max rent ← take-home pay step; print pieces ← portfolio book. Within one chain, numbering is enough.
- Never duplicate an existing sub-item in substance. Don't set `today`. Don't touch calendars — the Daily time-block planner schedules only the lowest-numbered open, unblocked step of each chain.

## 4. Never

Check, uncheck, rename, delete, re-prioritize or re-parent anything Yusef created, or edit his page bodies. Rows this skill created (body says "Added by /plan-gaps" or "Added by Plan Gap Filler") you may fix, re-title, mark done, or mark `⏸ FROZEN` when he says so.

## 5. Report

One grouped message: each parent (with Notion URL) → the numbered steps added, any `Blocked by` links made, then one line each for clutter spotted and for what was deliberately left alone (frozen / held / locked). No questions, no filler. Act first; state any assumption afterward so he can correct it.
