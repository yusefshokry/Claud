---
name: tutorial-notes
description: Transcribe a video (YouTube link, playlist, or a pasted transcript from a paid course) into a Notion note, then work out how it plugs into Yusef's system, plans and strategy, and apply it. Use when Yusef pastes a video link, says "transcribe this", "tutorial notes", "turn this video into notes", "how do I use this video", "add this to my plan", or runs /tutorial-notes. Works for tattoo technique and for productivity, business, fitness or money videos.
---

# Tutorial Notes: video → notes → into the system

Yusef asked for this on 2026-10-16. He wants to watch tutorials and courses once, then have each one turned into:
- a written page he can review, and
- concrete changes to his plans, tasks and routines.

A summary that sits unused isn't enough. Every run must end with something in his system changed or queued.

## 1. Get the transcript

- **YouTube video:**
  - `python3 -m pip install -q youtube-transcript-api yt-dlp` (cloud containers start without them)
  - Transcript: `python3 .claude/skills/tutorial-notes/fetch_transcript.py "<url>"`
  - Title, channel and length: `python3 -m yt_dlp -q --skip-download --print "%(title)s | %(channel)s | %(duration_string)s" "<url>"` (ignore its JS-runtime warning)
- **Playlist or channel:** list it with `python3 -m yt_dlp -q --flat-playlist --print "%(title)s | %(url)s" "<url>"`. Ask which videos to do first, unless he said "all". Then process one video per note.
- **Paid course:** you can't log into his accounts. Ask him to paste the lesson's transcript (most players have a Transcript tab) or the written notes. If the session has the built-in browser and he's signed in there, use that instead (load the built-in-browser skill first).
- **No captions:** say so. Ask him for the description or chapter list, or a pasted transcript. Don't summarize from the title alone.

## 2. Write the note (INBOX row, never a standalone page)

Data source: `collection://2c5e4241-b1a3-80b5-bedb-000b9ea93719`.

Properties:
- `Inbox`: the title, shortened to 2–6 words.
- `Area`: `["Note"]`.
- `Areas`: the matching area:
  - Portfolio (`https://app.notion.com/p/3f9e4241b1a381628887e3458e6ce762`) for tattoo and art
  - Career (`…3f9e4241b1a38107ada0f8d1984feb75`)
  - Finance (`…3f9e4241b1a381179442cd68f3bcdb97`)
  - Domestic (`…3f9e4241b1a381078d71d8d3de444756`)
  - Admin (`…3f9e4241b1a381e08c2bd2be1d53a763`)
- `Parent item`: the Goal or Project it serves.
- `Website`: the URL.
- Icon: `icons/document_blue`.

Body:
1. **Source**: channel, length, link, date.
2. **TL;DR**: 2–3 sentences.
3. **Key ideas / techniques**: the real substance in his terms, with `[mm:ss]` timestamps.
4. **Step-by-step**: a checklist he can follow, when the video teaches a procedure.
5. **Mistakes to avoid**.
6. **Integration plan**: see step 3.
7. A toggle **Full transcript** holding the raw timestamped text.

If the "Build tattoo course notes system" project has topic pages by then (one page per skill area), also add the key points to the matching topic page and link back to this note.

## 3. Plug it into the system (the point of this skill)

For each takeaway, decide where it belongs and act. Search INBOX first; never duplicate an existing task.

| Takeaway type | Where it goes | What you do |
|---|---|---|
| A drill or practice method | The current portfolio focus (Linework as of Oct 2026) or the relevant art task | Create Task rows under that parent with `Effort` and `Priority` set, so the daily planner schedules them. Update the parent's body. |
| A better way to do something he already does | The existing task or project page | Add a "Learned from: <note>" line and update its steps. |
| A purchase (tool, supply, course) | A Task row with the price in the body | Mark it "wait for budget" unless it's under ~$20 or he asked. Money is tight. |
| A change to how his week runs (session length, order, routines) | The daily planner or Strategist rules | Write paste-ready instruction text. The planner's prompt can only be edited from its own chat ("⚡ Daily time-block planner"). Put the paste text in the note under **System changes** and tell him. |
| A strategy shift (career path, outreach approach, goals) | The Q4 page and the Strategy Log | Add it to the Strategy Log's Running priorities or Open questions (https://app.notion.com/p/3fbe4241b1a381228661d0643d7cbdae), so the daily Strategist builds on it. |
| A repeatable process worth automating | A new skill or routine | Build it if it's small. Otherwise log a Claude-owned Task describing it. |

Write the **Integration plan** section as a list: *takeaway → where → change → done / waiting on you*, with links to every row you created or changed.

If it's unclear where something belongs or whether he wants it, ask with the question tool instead of guessing (his rule since 2026-10-16). Batch the questions and put the recommended option first.

## 4. Close out

Reply in 4–6 lines:
- link to the note
- the TL;DR
- what you changed in his system
- anything waiting on him (paste text, a purchase decision, questions)

Don't paste the whole note into chat.
