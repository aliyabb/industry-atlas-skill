#!/usr/bin/env python3
"""Check RSS/Atom feeds and export the working ones to OPML.

    python3 tools/check_feeds.py feeds.yaml --opml 14-Monitoring/feeds.opml --markdown feeds-table.md

feeds.yaml is a list:

    - {folder: A-Daily, name: TechCrunch, url: https://techcrunch.com/feed/, html: https://techcrunch.com/}

A feed passes when it answers HTTP 200 and looks like RSS/Atom/XML (content
type or the first bytes of the body). Many sites block scripts (403) but work
in a real reader: those are reported separately so a human can try them.
Standard library only; no API keys.
"""
import argparse
import concurrent.futures
import datetime as dt
import pathlib
import sys
import urllib.error
import urllib.request
from xml.sax.saxutils import quoteattr

import yaml

USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_0) IndustryAtlasFeedCheck/1.0"


def check(feed):
    request = urllib.request.Request(feed["url"], headers={"User-Agent": USER_AGENT, "Accept": "*/*"})
    try:
        with urllib.request.urlopen(request, timeout=15) as response:
            head = response.read(2048).lstrip()
            ctype = response.headers.get("Content-Type", "")
            looks_like_feed = any(t in ctype for t in ("xml", "rss", "atom")) or head[:5] == b"<?xml" \
                or b"<rss" in head[:300] or b"<feed" in head[:300]
            return feed, response.status, ctype, "ok" if looks_like_feed else "not a feed"
    except urllib.error.HTTPError as e:
        return feed, e.code, "", "blocked" if e.code in (401, 403, 429) else "error"
    except Exception as e:  # network errors, timeouts, TLS problems
        return feed, 0, "", f"error: {type(e).__name__}"


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("feeds")
    parser.add_argument("--opml", help="write working feeds to this OPML file")
    parser.add_argument("--markdown", help="write a Markdown table of working feeds to this file")
    parser.add_argument("--title", default="Industry Atlas feeds")
    args = parser.parse_args()

    feeds = yaml.safe_load(pathlib.Path(args.feeds).read_text(encoding="utf-8")) or []
    with concurrent.futures.ThreadPoolExecutor(max_workers=12) as pool:
        results = list(pool.map(check, feeds))

    ok = [r for r in results if r[3] == "ok"]
    for feed, status, ctype, verdict in sorted(results, key=lambda r: (r[3] != "ok", r[0]["folder"], r[0]["name"])):
        print(f"{verdict:14} {status:>3}  {feed['folder']:24} {feed['name']:32} {feed['url']}")
    print(f"\n{len(ok)}/{len(results)} feeds working (checked {dt.date.today()})")

    if args.opml:
        folders = {}
        for feed, *_ in ok:
            folders.setdefault(feed["folder"], []).append(feed)
        lines = ['<?xml version="1.0" encoding="UTF-8"?>', '<opml version="2.0">', "  <head>",
                 f"    <title>{args.title} (checked {dt.date.today()})</title>", "  </head>", "  <body>"]
        for folder, items in folders.items():
            lines.append(f"    <outline text={quoteattr(folder)} title={quoteattr(folder)}>")
            for f in items:
                html = f" htmlUrl={quoteattr(f['html'])}" if f.get("html") else ""
                lines.append(f"      <outline type=\"rss\" text={quoteattr(f['name'])} title={quoteattr(f['name'])} "
                             f"xmlUrl={quoteattr(f['url'])}{html}/>")
            lines.append("    </outline>")
        lines += ["  </body>", "</opml>", ""]
        pathlib.Path(args.opml).write_text("\n".join(lines), encoding="utf-8")
        print(f"wrote {args.opml}")

    if args.markdown:
        rows = ["| Folder | Source | Feed URL |", "|---|---|---|"]
        rows += [f"| {f['folder']} | {f['name']} | {f['url']} |" for f, *_ in ok]
        failed = [r for r in results if r[3] != "ok"]
        if failed:
            rows += ["", "| Source | Result | URL |", "|---|---|---|"]
            rows += [f"| {f['name']} | {verdict} ({status}) | {f['url']} |" for f, status, _, verdict in failed]
        pathlib.Path(args.markdown).write_text("\n".join(rows) + "\n", encoding="utf-8")
        print(f"wrote {args.markdown}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
