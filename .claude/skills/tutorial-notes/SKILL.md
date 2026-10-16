---
name: tutorial-notes
description: Turn a tutorial video (YouTube link, or a pasted transcript from a paid course) into a written Notion page Yusef can review and use to plan and strategize. Use when Yusef pastes a YouTube link, says "tutorial notes", "turn this video into notes", "summarize this tutorial/course lesson", or runs /tutorial-notes.
---

# Tutorial Notes

Yusef learns from tattoo/art tutorials and courses. He wants each one turned into a page he can read back and plan from (asked for on 2026-10-16), instead of rewatching.

## 1. Get the transcript

- **YouTube link:** run
  `python3 -m pip install -q youtube-transcript-api` (cloud containers start without it), then
  `python3 .claude/skills/tutorial-notes/fetch_transcript.py "<url>"`.
  Get the title and channel with WebFetch on the video URL, or from the oEmbed endpoint
  `https://www.youtube.com/oembed?url=<url>&format=json`.
  If there are no captions, say so and ask him to paste the description or chapter list instead.
- **Paid course site:** Claude can't log into his course accounts. Ask him to paste the lesson's transcript or captions text (most course players have a "Transcript" tab), or the lesson's written notes. If the session has the built-in browser and he's signed in there, that's an option too (load the built-in-browser skill first).

## 2. Write the page

Create one INBOX row (`collection://2c5e4241-b1a3-80b5-bedb-000b9ea93719`), never a standalone page:

- `Inbox` (title): the video title, shortened to 2–6 words if it's long
- `Area` = `["Note"]`; `Areas` = Portfolio (`https://app.notion.com/p/3f9e4241b1a381628887e3458e6ce762`) for tattoo/art, otherwise the closest Area
- `Parent item` = the Goal or Project it serves when clear (e.g. Linework → the Linework drills page); ask if it's unclear
- `Website` = the video URL
- icon `icons/document_blue` (not emoji)

Body, in this order:

1. **Source**: channel, length, link, date watched (today)
2. **TL;DR**: 2–3 sentences
3. **Key techniques**: the real how-to, in his terms (needle groupings, hand speed, stretch, voltage, angle, stencil prep, etc.), with `[mm:ss]` timestamps so he can jump back
4. **Step-by-step**: the procedure as a checklist he can follow at the table
5. **Mistakes to avoid**: what the teacher warns about
6. **Apply it**: 2–4 concrete drills or changes for his current focus (check `CURRENT PORTFOLIO FOCUS` in CLAUDE.md / the planner; Linework as of Oct 2026)
7. **Questions to test / open questions**
8. A toggle "Full transcript" holding the raw timestamped transcript

## 3. Close the loop

- Offer to add the "Apply it" drills as Tasks under the right parent, so the planner schedules them. Create them only if he says yes.
- Reply with the page link and the 3-line TL;DR. Don't paste the whole page into chat.
