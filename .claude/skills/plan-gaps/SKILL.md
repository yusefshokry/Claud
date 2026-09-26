---
name: plan-gaps
description: Find gaps in Yusef's Notion plans (Goals, Projects, Tasks) and flesh them out into short, concrete, dependency-linked next actions. Use when Yusef says "flesh out", "fill the gaps", "break this down", "what's the next step for X", "plan gaps", or runs /plan-gaps — for one named plan or the whole INBOX.
---

# Plan Gaps

Turn vague or stalled plans in Yusef's Notion INBOX into short chains of concrete actions, with real dependencies linked, so every open plan has a doable next step. On demand only (replaced the daily "Plan Gap Filler" routine on 2026-09-26).

## Scope

- **Argument given** (`/plan-gaps apartment`, "flesh out the XMAS plan"): only that plan and everything under it. Match by title; if several match, take the closest and say which.
- **No argument**: every open Goal, Project and Task. Be thorough — no cap on items covered.

## Data

- INBOX: `collection://2c5e4241-b1a3-80b5-bedb-000b9ea93719`
- `Inbox` (title) · `.` (done) · **`Frozen`** (archived-to-the-side state, like done) · `Area (1)` (Goal / Project / Task / Chore / Journal / Gratitude / Inventory / Shop / Question) · `Area` · `Priority` (Urgent / Important / **Maintence** / Optional) · `Year` · `Quarter` · `Date` · `Parent item` / `Sub-item` · **`Blocked by` / `Blocking`** · `today`
- Shop outreach = INBOX rows with `Area (1)` = Shop (`Shop Tier`, `Outreach Status`, `First Visit`, `Next Follow-up`). People = Contacts (`collection://fa3d2aa0-501f-49e0-85a8-2615f0fb2c5b`). Gift ideas = 🎁 Gift Ideas table on the XMAS page. Groceries = children of Grosseries.

## 1. Find gaps

Unchecked, unfrozen Goals/Projects/Tasks in scope, plus their sub-items. A gap is:
- a Goal with no open Project/Task under it; a Project with no open Task
- a Task that is vague ("plan X", a bare noun, a "how do I…?"), secretly several steps, or waiting on something that hasn't happened — with no open sub-tasks
- a chain whose open steps don't reach the outcome
- a dated item within ~90 days with no prep steps
- an unlinked cross-plan dependency
- a stated goal (CLAUDE.md "Current goals") with no Goal row — check for similar titles first

**Skip:** Chores, Journal, Gratitude, Inventory rows, done items, **Frozen items and anything under a Frozen parent**, and clutter (untitled, "(1)" duplicates, "Test", bare hotkey names — list it, never touch it).

**Respect** (read CLAUDE.md fresh; it's the source of truth): Reston presentation + GM outreach on hold until VIDA replies; portfolio locked to Linework (no chains for other pieces); things Yusef says are done are done.

## 2. Read first

Fetch the page and its parent. Pull real facts (page body, related pages like the Tattoo career game plan, Gmail, Calendar, Era_Context). If the page already names a contact, number or link, the step uses it (e.g. "Call JATC 26 (Mark)" not "Look up electrician programs").

## 3. Write the chain — Yusef's conventions

- **Titles: concise, 2–6 words, verb first, no numbering.** "Book passport appointment", "Ask Matt: beach weekend", "Pay Harris & Harris $274.95". Details go in the page body, not the title.
- **Icons** (always set `icon` on create):
  - Task / action step → `icons/checklist_yellow`
  - Goal → `icons/bullseye_<color>`; Project → `icons/wrench_<color>` (or `icons/chess-queen_<color>` for a game-plan/strategy doc)
  - `<color>` by area: Career/Portfolio → `blue`, Financial → `green`, Home/Health → `pink`, Education/social → `yellow`
- **Order = creation order.** Create a chain's steps in the order they must happen, in one call; the planner schedules the first open one in the parent's Sub-item order.
- Properties: `Parent item` = gap's URL; `Area (1)` = `["Task"]`; copy `Area`, `Priority`, `Year`, `Quarter` from the parent.
- Missing info is its own step: `Ask <person>: <thing>`. Never guess names, dates, prices.
- Body: one line `Why: …` with the specific facts (phone, link, amount, date), then `Added by /plan-gaps on <date>`.
- Cross-plan dependencies → set `Blocked by` (array of page URLs). Within a chain, creation order is enough.
- Only as many steps as the outcome truly needs; don't pad. Never duplicate an existing sub-item in substance. Don't set `today`. Don't touch calendars.

## 4. Never

Check, uncheck, rename, delete, re-prioritize, re-parent or freeze anything Yusef created, or edit his page bodies — unless he asks. Freezing is a state (`Frozen` checkbox), never a sub-task or a title prefix. Rows this skill created ("Added by /plan-gaps" / "Added by Plan Gap Filler") you may fix, re-title, check off or freeze when he says so.

## 5. Report

One grouped message: each parent (with Notion URL) → the steps added (titles only), `Blocked by` links made, then one line each for clutter spotted and anything deliberately left alone. No questions, no filler. Act first; state assumptions after.
