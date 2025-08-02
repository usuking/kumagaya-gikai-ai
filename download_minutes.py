#!/usr/bin/env python3
"""Simple downloader for local assembly minutes.

This script fetches an index page and downloads files (PDF/TXT/HTML) linked
from it. It uses only the Python standard library so it can run in restricted
environments.
"""

from __future__ import annotations

import argparse
import os
import re
from html.parser import HTMLParser
from urllib.parse import urljoin, urlparse
from urllib.request import urlopen, urlretrieve, URLError


class MinutesLinkParser(HTMLParser):
    """HTML parser that collects links to minutes files."""

    def __init__(self, base_url: str) -> None:
        super().__init__()
        self.base_url = base_url
        self.links: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str]]) -> None:
        if tag.lower() != "a":
            return
        href = dict(attrs).get("href")
        if not href:
            return
        href = href.strip()
        # Capture common minute file types.
        if re.search(r"\.(pdf|txt|html?)$", href, re.IGNORECASE):
            self.links.append(urljoin(self.base_url, href))


def download_minutes(index_url: str, output_dir: str) -> list[str]:
    """Download minutes files linked from *index_url* to *output_dir*.

    Returns a list of file paths that were saved.
    """

    try:
        with urlopen(index_url) as resp:
            html = resp.read().decode("utf-8", errors="ignore")
    except URLError as exc:
        raise SystemExit(f"Failed to fetch {index_url}: {exc}")

    parser = MinutesLinkParser(index_url)
    parser.feed(html)

    os.makedirs(output_dir, exist_ok=True)
    saved_paths = []
    for link in parser.links:
        filename = os.path.basename(urlparse(link).path)
        if not filename:
            continue
        destination = os.path.join(output_dir, filename)
        try:
            urlretrieve(link, destination)
        except URLError as exc:
            print(f"Failed to download {link}: {exc}")
            continue
        print(f"Downloaded {link} -> {destination}")
        saved_paths.append(destination)
    return saved_paths


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Download local assembly minutes files from an index page"
    )
    parser.add_argument(
        "index_url",
        help="URL of the page that lists minute files",
    )
    parser.add_argument(
        "-o",
        "--output",
        default="minutes",
        help="Directory to store downloaded files (default: minutes)",
    )
    args = parser.parse_args()
    download_minutes(args.index_url, args.output)


if __name__ == "__main__":
    main()
