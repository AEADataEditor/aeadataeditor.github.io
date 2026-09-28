#!/usr/bin/env python3
"""Generate ICS calendar files from talk front matter.

Two steps, both run from the build workflow:

  generate_ics.py --add-metadata   before the Jekyll build: adds
      `ics: <talk file name>.ics` to the front matter of every talk lacking
      it (in the checkout only), so the talk layout links to the file.
  generate_ics.py                  after the Jekyll build: writes a calendar
      file to _site/ics/ for every dated talk. The event links back to the
      talk page on the website.

Front matter keys used:

  ics         optional file name of the calendar file (default "<slug>.ics")
  title       event summary
  date        event date (all-day event unless start_time is given)
  end_date    optional last day of a multi-day event
  start_time  optional, "HH:MM" (24h)
  end_time    optional, "HH:MM" (24h); defaults to one hour after start_time
  timezone    optional IANA zone for start/end_time (default America/New_York)
  location, venue, joint, mainurl   included in location/description
"""

import re
import sys
from datetime import date, datetime, timedelta, timezone
from pathlib import Path
from zoneinfo import ZoneInfo

import yaml

BASE_URL = "https://aeadataeditor.github.io"
TALKS_DIR = Path("_talks")
OUTPUT_DIR = Path("_site/ics")
DEFAULT_TZ = "America/New_York"
PRODID = "-//AEA Data Editor//aeadataeditor.github.io//EN"

FRONT_MATTER = re.compile(r"\A---\s*\n(.*?)\n---\s*(?:\n|\Z)", re.DOTALL)


def parse_front_matter(path):
    m = FRONT_MATTER.match(path.read_text(encoding="utf-8"))
    if not m:
        return {}
    data = yaml.safe_load(m.group(1))
    return data if isinstance(data, dict) else {}


def esc(text):
    """Escape a TEXT value per RFC 5545."""
    return (str(text).replace("\\", "\\\\").replace(";", "\;")
            .replace(",", "\\,").replace("\r\n", "\n").replace("\n", "\\n"))


def fold(line):
    """Fold a content line to 75 octets (RFC 5545 3.1)."""
    out, cur, size = [], "", 0
    for ch in line:
        n = len(ch.encode("utf-8"))
        if size + n > (75 if not out else 74):
            out.append(cur)
            cur, size = "", 0
        cur += ch
        size += n
    out.append(cur)
    return "\r\n ".join(out)


def to_date(value):
    if isinstance(value, datetime):
        return value.date()
    if isinstance(value, date):
        return value
    return datetime.strptime(str(value).strip(), "%Y-%m-%d").date()


def to_time(value):
    if isinstance(value, int):  # YAML parses 12:30 as a sexagesimal int
        raise ValueError(f"quote time values in front matter: {value}")
    return datetime.strptime(str(value).strip(), "%H:%M").time()


def build_event(path, fm):
    slug = path.stem
    start_day = to_date(fm["date"])
    url = f"{BASE_URL}/talks/{slug}"
    uid = f"{slug}@aeadataeditor.github.io"
    now = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")

    lines = ["BEGIN:VEVENT", f"UID:{uid}", f"DTSTAMP:{now}"]
    if fm.get("start_time"):
        tz = ZoneInfo(fm.get("timezone") or DEFAULT_TZ)
        start = datetime.combine(start_day, to_time(fm["start_time"]), tz)
        if fm.get("end_time"):
            end_day = to_date(fm["end_date"]) if fm.get("end_date") else start_day
            end = datetime.combine(end_day, to_time(fm["end_time"]), tz)
        else:
            end = start + timedelta(hours=1)
        fmt = "%Y%m%dT%H%M%SZ"
        lines += [f"DTSTART:{start.astimezone(timezone.utc).strftime(fmt)}",
                  f"DTEND:{end.astimezone(timezone.utc).strftime(fmt)}"]
    else:
        last = to_date(fm["end_date"]) if fm.get("end_date") else start_day
        lines += [f"DTSTART;VALUE=DATE:{start_day.strftime('%Y%m%d')}",
                  f"DTEND;VALUE=DATE:{(last + timedelta(days=1)).strftime('%Y%m%d')}"]

    lines.append(f"SUMMARY:{esc(fm.get('title', slug))}")

    where = ", ".join(str(fm[k]) for k in ("venue", "location") if fm.get(k))
    if where:
        lines.append(f"LOCATION:{esc(where)}")

    desc = []
    if fm.get("type"):
        desc.append(str(fm["type"]))
    if fm.get("joint"):
        joint = fm["joint"] if isinstance(fm["joint"], list) else [fm["joint"]]
        desc.append("Joint with: " + ", ".join(map(str, joint)))
    if fm.get("mode"):
        desc.append(f"Mode: {fm['mode']}")
    if fm.get("mainurl"):
        desc.append(f"Event information: {fm['mainurl']}")
    desc.append(f"More information: {url}")
    lines.append(f"DESCRIPTION:{esc(chr(10).join(desc))}")
    lines.append(f"URL:{url}")
    lines.append("END:VEVENT")
    return lines


def build_calendar(path, fm):
    lines = ["BEGIN:VCALENDAR", "VERSION:2.0", f"PRODID:{PRODID}",
             "CALSCALE:GREGORIAN", "METHOD:PUBLISH"]
    lines += build_event(path, fm)
    lines.append("END:VCALENDAR")
    return "\r\n".join(fold(l) for l in lines) + "\r\n"


def add_metadata():
    """Insert `ics: <slug>.ics` into the front matter of talks lacking it."""
    count = 0
    for path in sorted(TALKS_DIR.glob("*.md")):
        text = path.read_text(encoding="utf-8")
        m = FRONT_MATTER.match(text)
        if not m or parse_front_matter(path).get("ics"):
            continue
        # drop an empty `ics:` line, if any, then add the entry
        block = re.sub(r"^ics:[ \t]*$\n?", "", m.group(1), flags=re.MULTILINE)
        block += f"\nics: {path.stem}.ics"
        path.write_text(text[:m.start(1)] + block + text[m.end(1):], encoding="utf-8")
        count += 1
    print(f"added ics metadata to {count} talk(s)")


def main():
    if "--add-metadata" in sys.argv[1:]:
        add_metadata()
        return
    count = 0
    for path in sorted(TALKS_DIR.glob("*.md")):
        fm = parse_front_matter(path)
        if not fm.get("date"):
            print(f"warning: {path} has no date; skipped", file=sys.stderr)
            continue
        name = fm.get("ics") or f"{path.stem}.ics"
        name = Path(str(name)).name  # no path components
        if not name.endswith(".ics"):
            name += ".ics"
        OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
        (OUTPUT_DIR / name).write_text(build_calendar(path, fm), encoding="utf-8", newline="")
        count += 1
        print(f"wrote {OUTPUT_DIR / name}")
    print(f"{count} ICS file(s) generated")


if __name__ == "__main__":
    main()
