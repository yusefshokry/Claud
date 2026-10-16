"""Print a YouTube video's transcript as timestamped lines.

Usage: python3 fetch_transcript.py <youtube-url-or-id>
Needs: python3 -m pip install youtube-transcript-api
"""
import re
import sys

from youtube_transcript_api import YouTubeTranscriptApi


def video_id(arg):
    m = re.search(r"(?:v=|youtu\.be/|shorts/|embed/|live/)([\w-]{11})", arg)
    return m.group(1) if m else arg.strip()


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    vid = video_id(sys.argv[1])
    transcript = YouTubeTranscriptApi().fetch(vid, languages=["en", "en-US", "en-GB"])
    for s in transcript.snippets:
        m, sec = divmod(int(s.start), 60)
        print(f"[{m:02d}:{sec:02d}] {s.text}")


if __name__ == "__main__":
    main()
